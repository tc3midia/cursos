#!/usr/bin/env python3
"""Executa os papéis da base Formato Criativo de Conteúdo em processos isolados do Claude Code.

Via: assinatura, `claude -p` headless, sem ferramentas, sem configurações do usuário e em diretório vazio.
Cada chamada recebe só o pacote do papel. O bloco fixo vai no system prompt, idêntico byte a byte entre
aulas, para o cache de prefixo. Cada execução grava um `.execucao.json` com modelo, esforço, os quatro
contadores de token, via e término. Batch API não existe nesta via.
"""
import argparse
import copy
import datetime
import json
import re
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import base_fcc as base  # noqa: E402

PAPEIS = base.PROC / 'papeis'
MODELS = {'claude-sonnet-5': 'sonnet-5', 'claude-opus-5': 'opus-5', 'claude-fable-5-1': 'fable-5.1'}
EFFORTS = ('low', 'medium', 'high', 'xhigh', 'max')
EMPTY = Path(tempfile.gettempdir()) / 'fcc-diretorio-vazio'
NULLABLE = {'type': ['string', 'null']}


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')


def cli_version():
    return subprocess.run(['claude', '--version'], capture_output=True, text=True).stdout.strip()


# ---------------------------------------------------------------- esquemas

def unit_schema(tax, with_number):
    props = {
        'titulo': {'type': 'string'}, 'tipo': {'type': 'string', 'enum': list(tax['tipos'])},
        'tema': {'type': 'string', 'enum': list(tax['temas'])},
        'tarefas': {'type': 'array', 'items': {'type': 'string', 'enum': list(tax['tarefas'])}},
        'plataformas': {'type': 'array', 'items': {'type': 'string', 'enum': list(tax['plataformas'])}},
        'fonte': {'type': 'string', 'enum': list(base.SOURCES)},
        'inicio': {'type': ['number', 'null']}, 'fim': {'type': ['number', 'null']},
        'condicoes': NULLABLE, 'perecivel': {'type': 'boolean'},
        'confianca': {'type': 'string', 'enum': ['alta', 'media', 'baixa']},
        'nota': NULLABLE, 'proposta_tag': NULLABLE, 'corpo': {'type': 'string'}, 'evidencia': {'type': 'string'},
    }
    if with_number:
        props = {'numero': {'type': 'integer'}, **props}
    return {'type': 'object', 'properties': props, 'required': list(props), 'additionalProperties': False}


def schema_for(role, tax):
    text = {'type': 'string'}
    if role == 'extrator':
        props = {'contexto': {'type': 'array', 'items': text}, 'unidades': {'type': 'array', 'items': unit_schema(tax, False)}}
    elif role == 'inspetor':
        finding = {'type': 'object', 'additionalProperties': False, 'required': ['numero', 'veredito', 'gravidade', 'trecho_fonte', 'explicacao'], 'properties': {
            'numero': {'type': 'integer'}, 'veredito': {'type': 'string', 'enum': ['lastreada', 'desvio', 'sem-lastro', 'faixa-errada']},
            'gravidade': {'type': 'string', 'enum': ['nenhuma', 'menor', 'material']}, 'trecho_fonte': text, 'explicacao': text}}
        omission = {'type': 'object', 'additionalProperties': False, 'required': ['inicio', 'trecho_fonte', 'descricao', 'gravidade', 'efeito_pratico'], 'properties': {
            'inicio': {'type': ['number', 'null']}, 'trecho_fonte': text, 'descricao': text,
            'gravidade': {'type': 'string', 'enum': ['menor', 'material']}, 'efeito_pratico': text}}
        perishable = {'type': 'object', 'additionalProperties': False, 'required': ['numero', 'problema'], 'properties': {'numero': {'type': 'integer'}, 'problema': text}}
        props = {'unidades': {'type': 'array', 'items': finding}, 'omissoes': {'type': 'array', 'items': omission},
                 'perecibilidade': {'type': 'array', 'items': perishable}, 'contrato': {'type': 'array', 'items': text},
                 'material': {'type': 'array', 'items': text}, 'resumo': text}
    elif role == 'juiz':
        vetoes = {'type': 'string', 'enum': ['contrato', 'fidelidade', 'cobertura', 'perecibilidade', 'aplicabilidade']}
        failure = {'type': 'object', 'additionalProperties': False, 'required': ['id', 'unidades', 'veto', 'evidencia', 'impacto', 'mudanca_minima', 'criterio_de_aceite'], 'properties': {
            'id': text, 'unidades': {'type': 'array', 'items': {'type': 'integer'}}, 'veto': vetoes, 'evidencia': text, 'impacto': text,
            'mudanca_minima': text, 'criterio_de_aceite': text}}
        props = {'veredito': {'type': 'string', 'enum': ['passa', 'falha', 'bloqueado']}, 'vetos': {'type': 'array', 'items': vetoes},
                 'contrato': text, 'fidelidade': text, 'cobertura': text, 'perecibilidade': text, 'aplicabilidade': text,
                 'falhas': {'type': 'array', 'items': failure}, 'ajustes_menores': {'type': 'array', 'items': text}, 'proximo': text}
    elif role == 'redator':
        props = {'unidades_corrigidas': {'type': 'array', 'items': unit_schema(tax, True)}, 'unidades_novas': {'type': 'array', 'items': unit_schema(tax, False)},
                 'retiradas': {'type': 'array', 'items': {'type': 'integer'}},
                 # O contexto da aula não é unidade: sem este campo, uma falha do juiz sobre o contexto não tinha por onde passar (G08_A06, lote 5).
                 'contexto': {'type': 'array', 'items': text, 'description': 'Só quando uma falha pedir mudança no contexto da aula: as 3 a 8 frases do contexto completas, na ordem, já reescritas. Sem pedido sobre o contexto, lista vazia.'},
                 'observacoes': text}
    else:
        raise ValueError(role)
    return {'type': 'object', 'properties': props, 'required': list(props), 'additionalProperties': False}


# ---------------------------------------------------------------- pacotes

def fixed_block(role):
    """Bloco fixo do papel: nenhum dado de aula, data ou identificador de execução entra aqui."""
    names = {'extrator': ['papeis/extrator.md', '../../conhecimento/FORMATO.md', '../../conhecimento/taxonomia.md', 'papeis/exemplos-de-granularidade.md'],
             'inspetor': ['papeis/inspetor.md', 'RUBRICA.md', '../../conhecimento/FORMATO.md', '../../conhecimento/taxonomia.md'],
             'juiz': ['papeis/juiz.md', 'RUBRICA.md', '../../conhecimento/FORMATO.md', '../../conhecimento/taxonomia.md'],
             'redator': ['papeis/redator.md', '../../conhecimento/FORMATO.md', '../../conhecimento/taxonomia.md']}[role]
    parts = []
    for name in names:
        path = (base.PROC / name).resolve()
        parts.append(f'<documento nome="{path.name}">\n{path.read_text().strip()}\n</documento>')
    return '\n\n'.join(parts) + '\n'


def source_block(row, text, material):
    parts = [f'<aula curso="{row["curso"]}" codigo="{row["aula"]}" modulo="{row["modulo_titulo"]}" titulo="{row["titulo"]}">']
    if text.strip():
        parts.append(f'<transcricao arquivo="transcricao.md" fim_segundos="{row["fim_transcricao_segundos"]:.0f}">\n{text.strip()}\n</transcricao>')
    else:
        parts.append('<transcricao_ausente motivo="aula só de material: todas as unidades têm fonte material, sem faixa"/>')
    if material:
        parts.append(f'<material arquivo="{Path(row["fontes"]["material"]["caminho"]).name}">\n{material.strip()}\n</material>')
    elif row['material_ignorado']:
        parts.append(f'<material_ignorado motivo="{row["material_ignorado"]}"/>')
    else:
        parts.append('<material_ausente/>')
    return '\n'.join(parts + ['</aula>'])


def units_block(data):
    return '<unidades_json>\n' + json.dumps({'contexto': data['contexto'], 'unidades': data['unidades']}, ensure_ascii=False, indent=1) + '\n</unidades_json>'


# ---------------------------------------------------------------- chamada

LIMIT_RETRIES = 12
LIMIT_TEXT = re.compile(r'session limit|usage limit|rate limit|limit reached', re.I)
RESET_AT = re.compile(r'resets?\s+(?:at\s+)?(\d{1,2})(?::(\d{2}))?\s*(am|pm)', re.I)


def limit_wait(raw, clock=None):
    """Segundos a esperar quando a chamada bateu no limite da assinatura; None quando o erro é outro ou não houve erro."""
    message = str(raw.get('result') or '')
    if not raw.get('is_error') or not (raw.get('api_error_status') == 429 or LIMIT_TEXT.search(message)):
        return None
    current = clock or datetime.datetime.now()
    match = RESET_AT.search(message)
    if not match:
        return 1800
    hour = int(match.group(1)) % 12 + (12 if match.group(3).lower() == 'pm' else 0)
    target = current.replace(hour=hour, minute=int(match.group(2) or 0), second=0, microsecond=0)
    if target <= current:
        target += datetime.timedelta(days=1)
    return int((target - current).total_seconds()) + 120


def call(role, system, user, schema, model, effort, timeout):
    EMPTY.mkdir(exist_ok=True)
    cmd = ['claude', '-p', '--model', model, '--effort', effort, '--system-prompt', system, '--tools', '', '--strict-mcp-config',
           '--setting-sources', '', '--disable-slash-commands', '--no-session-persistence', '--exclude-dynamic-system-prompt-sections',
           '--output-format', 'json', '--json-schema', json.dumps(schema, ensure_ascii=False, sort_keys=True)]
    started = now()
    waits = []
    while True:
        try:
            proc = subprocess.run(cmd, input=user, cwd=EMPTY, capture_output=True, text=True, timeout=timeout)
            raw = json.loads(proc.stdout) if proc.stdout.strip().startswith('{') else {'is_error': True, 'result': proc.stdout[-2000:], 'stderr': proc.stderr[-2000:]}
        except subprocess.TimeoutExpired:
            raw = {'is_error': True, 'result': f'timeout de {timeout}s', 'terminal_reason': 'timeout'}
        pause = limit_wait(raw)
        if pause is None or len(waits) >= LIMIT_RETRIES:
            break
        # Limite de sessão da assinatura: guarda a tentativa, espera a renovação e repete a mesma chamada.
        waits.append({'em': now(), 'status': raw.get('api_error_status'), 'mensagem': str(raw.get('result') or '')[:200], 'espera_segundos': pause})
        print(f'[limite de sessão] {role}: esperando {pause // 60} min', file=sys.stderr, flush=True)
        time.sleep(pause)
    usage = raw.get('usage') or {}
    record = {
        'papel': role, 'modelo_pedido': model, 'modelos_usados': sorted((raw.get('modelUsage') or {}).keys()), 'esforco': effort,
        'via': f'assinatura Claude Code, claude -p headless ({cli_version()}); sem Batch API', 'inicio': started, 'fim': now(),
        'duracao_ms': raw.get('duration_ms'), 'duracao_api_ms': raw.get('duration_api_ms'),
        'consumo': {k: usage.get(k) for k in ('input_tokens', 'output_tokens', 'cache_creation_input_tokens', 'cache_read_input_tokens')},
        'thinking_tokens': (usage.get('output_tokens_details') or {}).get('thinking_tokens'),
        'stop_reason': raw.get('stop_reason'), 'stop_details': raw.get('stop_details'), 'terminal_reason': raw.get('terminal_reason'),
        'subtype': raw.get('subtype'), 'is_error': raw.get('is_error'), 'api_error_status': raw.get('api_error_status'), 'num_turns': raw.get('num_turns'),
        'ferramentas_negadas': raw.get('permission_denials'), 'custo_nominal_usd': raw.get('total_cost_usd'),
        'esperas_por_limite': waits,
        'sistema_sha256': base.sha(system.encode()), 'pacote_sha256': base.sha((system + '\x00' + user + '\x00' + json.dumps(schema, sort_keys=True)).encode()),
    }
    output = raw.get('structured_output')
    if output is None and not raw.get('is_error'):
        try:
            output = json.loads(raw.get('result') or '')
        except ValueError:
            output = None
    if output is None:
        record['erro'] = (raw.get('result') or '')[:1500]
    return output, record


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(base.dump(value))


def literal_check(quotes, haystack):
    """Citações do inspetor que não existem literalmente na fonte. O juiz não vê a fonte; este número vai para ele."""
    return [q for q in quotes if q and base.word_seq(q) not in haystack]


# ---------------------------------------------------------------- papéis

def run_extract(args, lesson, tax, rows):
    row, text, segments, material = rows[lesson]
    out = args.saida / f'{lesson}.json'
    if out.exists() and not args.refazer:
        return f'{lesson}: já existe'
    output, record = call('extrator', fixed_block('extrator'), source_block(row, text, material), schema_for('extrator', tax), args.modelo, args.esforco, args.timeout)
    record.update({'aula': lesson, 'rotulo': args.rotulo, 'palavras_fonte': row['palavras_transcricao'], 'destino': str(out.relative_to(base.ROOT))})
    if output:
        units = [{'numero': n, **u, 'versao': 1} for n, u in enumerate(output['unidades'], 1)]
        # Marcação objetiva do contrato: plataforma específica ou tipo ferramenta implica perecível. O script aplica e registra.
        normalized = [u['numero'] for u in units if not u['perecivel'] and base.must_be_perishable(u)]
        for u in units:
            if u['numero'] in normalized:
                u['perecivel'] = True
        record['normalizacoes'] = {'perecivel_por_plataforma': normalized}
        data = {'curso': row['curso'], 'aula': lesson, 'titulo': row['titulo'], 'extraido_em': datetime.date.today().isoformat(), 'gerado_por': MODELS[args.modelo],
                'esforco': args.esforco, 'retiradas': [], 'contexto': output['contexto'], 'unidades': units}
        save(out, data)
        errors, warnings = base.validate_lesson(row, text, segments, material, data, tax)
        record.update({'resultado_sha256': base.sha(out.read_bytes()), 'unidades': len(units), 'validador': {'erros': errors, 'avisos': warnings}})
    save(args.saida / f'{lesson}.extrator.execucao.json', record)
    return f'{lesson}: {record.get("unidades", "falhou")} unidades, {len((record.get("validador") or {}).get("erros", []))} erros de contrato, saída {record["consumo"]["output_tokens"]}, cache lido {record["consumo"]["cache_read_input_tokens"]}'


def inspect_in_blocks(args, lesson, user, numbers, tax):
    """Aula longa: uma chamada por bloco de unidades. Todas recebem a aula e o arquivo inteiro; só a primeira busca omissões."""
    size = -(-len(numbers) // -(-len(numbers) // args.bloco))
    blocks = [numbers[i:i + size] for i in range(0, len(numbers), size)]

    def one(item):
        index, block = item
        extra = ('\n\n<inspecao_em_blocos bloco="' + f'{index + 1} de {len(blocks)}' + '" unidades="' + ', '.join(map(str, block)) + '">\nA aula é longa e a inspeção foi dividida. '
                 'Verifique só as unidades listadas e devolva em `unidades` e `perecibilidade` apenas elas. As demais unidades estão no pacote como contexto: outra execução as confere. '
                 + ('Este bloco também faz a busca de omissões na fonte inteira, considerando todas as unidades do arquivo.' if index == 0 else 'Devolva `omissoes` vazio: a busca de omissões é feita pelo bloco 1.')
                 + '\n</inspecao_em_blocos>')
        result, rec = call('inspetor', fixed_block('inspetor'), user + extra, schema_for('inspetor', tax), args.modelo, args.esforco, args.timeout)
        rec.update({'aula': lesson, 'rotulo': args.rotulo, 'bloco': f'{index + 1}/{len(blocks)}', 'unidades_do_bloco': block})
        save(args.saida / f'{lesson}.inspetor.bloco{index + 1}.execucao.json', rec)
        return result, rec

    with ThreadPoolExecutor(max_workers=3) as pool:
        results = list(pool.map(one, enumerate(blocks)))
    consumo = {k: sum((r['consumo'].get(k) or 0) for _, r in results) for k in ('input_tokens', 'output_tokens', 'cache_creation_input_tokens', 'cache_read_input_tokens')}
    record = {**results[0][1], 'consumo': consumo, 'custo_nominal_usd': sum((r.get('custo_nominal_usd') or 0) for _, r in results), 'blocos': len(blocks), 'agregado_de_blocos': True,
              'is_error': any(r.get('is_error') for _, r in results), 'thinking_tokens': sum((r.get('thinking_tokens') or 0) for _, r in results)}
    if any(out is None for out, _ in results):
        return None, record
    merged = {'unidades': sorted([f for out, _ in results for f in out['unidades']], key=lambda f: f['numero']), 'omissoes': results[0][0]['omissoes'],
              'perecibilidade': [p for out, _ in results for p in out['perecibilidade']], 'contrato': [c for out, _ in results for c in out['contrato']],
              'material': [m for out, _ in results for m in out['material']], 'resumo': ' | '.join(out['resumo'] for out, _ in results)}
    return merged, record


def run_inspect(args, lesson, tax, rows):
    row, text, segments, material = rows[lesson]
    target = args.entrada / f'{lesson}.json'
    out = args.saida / f'{lesson}.inspecao.json'
    if out.exists() and not args.refazer:
        return f'{lesson}: já existe'
    data = json.loads(target.read_text())
    user = source_block(row, text, material) + '\n\n' + units_block(data)
    focal, previous = None, None
    if args.focal:
        # Conferência de correção: só a lista de falhas e as unidades cujo hash mudou. A evidência das intactas é preservada.
        previous = json.loads((args.inspecao / f'{lesson}.inspecao.json').read_text())
        failures = json.loads((args.julgamento / f'{lesson}.julgamento.json').read_text())['falhas'] if args.julgamento else []
        changed = [u['numero'] for u in data['unidades'] if previous['hashes_unidades'].get(str(u['numero'])) != base.unit_hash(row, u)]
        focal = sorted({n for f in failures for n in f['unidades']} | set(changed))
        user += ('\n\n<conferencia_focal unidades="' + ', '.join(map(str, focal)) + '">\nEsta é a conferência de um ciclo de correção. Verifique só as unidades listadas: se cada falha abaixo foi resolvida '
                 'pelo critério de aceite e se a alteração criou problema novo nelas. Devolva em `unidades` apenas essas unidades. As demais não mudaram e mantêm a evidência da inspeção anterior: '
                 'não as reabra nem procure melhoria editorial nelas. Em `omissoes`, registre só o que decorrer das falhas de cobertura da lista.\n'
                 + json.dumps(failures, ensure_ascii=False, indent=1) + '\nHistórico de correções do arquivo:\n' + json.dumps(data.get('correcoes', []), ensure_ascii=False, indent=1) + '\n</conferencia_focal>')
    numbers = [u['numero'] for u in data['unidades']]
    if args.bloco and not focal and len(numbers) > args.bloco:
        output, record = inspect_in_blocks(args, lesson, user, numbers, tax)
    else:
        output, record = call('inspetor', fixed_block('inspetor'), user, schema_for('inspetor', tax), args.modelo, args.esforco, args.timeout)
    record.update({'aula': lesson, 'rotulo': args.rotulo, 'arquivo_sha256': base.sha(target.read_bytes()), 'destino': str(out.relative_to(base.ROOT))})
    if output:
        haystack = base.word_seq(text) + base.word_seq(material or '')
        quotes = [f['trecho_fonte'] for f in output['unidades']] + [o['trecho_fonte'] for o in output['omissoes']]
        scope = 'integral: todas as unidades e busca de omissões na fonte inteira'
        if focal:
            alive = {u['numero'] for u in data['unidades']}
            fresh = {f['numero'] for f in output['unidades']}
            output['unidades'] = sorted([f for f in previous['unidades'] if f['numero'] in alive and f['numero'] not in focal and f['numero'] not in fresh] + output['unidades'], key=lambda f: f['numero'])
            output['perecibilidade'] = [p for p in previous['perecibilidade'] if p['numero'] in alive and p['numero'] not in focal] + output['perecibilidade']
            output['omissoes'] = previous['omissoes'] + output['omissoes']
            output['contrato'] = previous['contrato'] + output['contrato']
            output['material'] = previous['material'] + output['material']
            scope = (f'focal nas unidades {focal}; as demais mantêm a evidência da inspeção integral do arquivo {previous["arquivo_sha256"][:12]}, '
                     'com hash de unidade conferido como inalterado; omissões, contrato e material acumulados')
        result = {'aula': lesson, 'arquivo_sha256': record['arquivo_sha256'], 'gerado_por': MODELS[args.modelo], 'esforco': args.esforco,
                  'alcance': scope, 'conferencia_focal': focal,
                  'unidades_verificadas': sorted(f['numero'] for f in output['unidades']), 'unidades_no_arquivo': [u['numero'] for u in data['unidades']],
                  'hashes_unidades': {str(u['numero']): base.unit_hash(row, u) for u in data['unidades']},
                  'citacoes_nao_literais': literal_check(quotes, haystack), **output}
        save(out, result)
        record['resultado_sha256'] = base.sha(out.read_bytes())
    save(args.saida / f'{lesson}.inspetor.execucao.json', record)
    return f'{lesson}: inspeção {"ok" if output else "falhou"}, saída {record["consumo"]["output_tokens"]}, cache lido {record["consumo"]["cache_read_input_tokens"]}'


def run_judge(args, lesson, tax, rows):
    row, text, segments, material = rows[lesson]
    target = args.entrada / f'{lesson}.json'
    inspection = args.inspecao / f'{lesson}.inspecao.json'
    out = args.saida / f'{lesson}.julgamento.json'
    if out.exists() and not args.refazer:
        return f'{lesson}: já existe'
    data = json.loads(target.read_text())
    errors, warnings = base.validate_lesson(row, text, segments, material, data, tax)
    evidence = json.loads(inspection.read_text())
    # O juiz não recebe transcrição, material nem caminho do clone.
    user = '\n\n'.join([f'<aula codigo="{lesson}" titulo="{row["titulo"]}" tem_material="{"sim" if material else "nao"}" palavras_fonte="{row["palavras_transcricao"]}"/>', units_block(data),
                        '<evidencia_do_inspetor>\n' + json.dumps({k: evidence[k] for k in ('alcance', 'unidades_verificadas', 'citacoes_nao_literais', 'unidades', 'omissoes', 'perecibilidade', 'contrato', 'material', 'resumo')}, ensure_ascii=False, indent=1) + '\n</evidencia_do_inspetor>',
                        '<validador>\n' + json.dumps({'erros': errors, 'avisos': warnings}, ensure_ascii=False, indent=1) + '\n</validador>'])
    if args.julgamento:
        earlier = json.loads((args.julgamento / f'{lesson}.julgamento.json').read_text())
        user += ('\n\n<conferencia_de_correcao ciclo="' + str(len(data.get('correcoes', []))) + '">\nEste julgamento confere um ciclo de correção. Decida se cada falha da lista abaixo foi resolvida pelo critério de aceite '
                 'e se a alteração criou falha nova nas unidades alteradas. A evidência das unidades intactas foi preservada da inspeção anterior porque o hash delas não mudou; a rubrica manda não procurar '
                 'perfeição editorial no restante. Histórico de correções do arquivo:\n' + json.dumps(data.get('correcoes', []), ensure_ascii=False, indent=1)
                 + '\nFalhas do julgamento anterior:\n' + json.dumps(earlier['falhas'], ensure_ascii=False, indent=1) + '\n</conferencia_de_correcao>')
    proof = args.prova.read_text().strip() if args.prova else None
    if proof:
        # Prova de ferramenta pedida pelo juiz: saída de script produzida pela coordenação. Não traz transcrição, material nem caminho do clone.
        user += '\n\n<prova_da_coordenacao>\n' + proof + '\n</prova_da_coordenacao>'
    output, record = call('juiz', fixed_block('juiz'), user, schema_for('juiz', tax), args.modelo, args.esforco, args.timeout)
    record.update({'aula': lesson, 'rotulo': args.rotulo, 'arquivo_sha256': base.sha(target.read_bytes()), 'inspecao_sha256': base.sha(inspection.read_bytes()), 'destino': str(out.relative_to(base.ROOT))})
    if proof:
        record['prova_da_coordenacao_sha256'] = base.sha(proof.encode())
    if output:
        save(out, {'aula': lesson, 'arquivo_sha256': record['arquivo_sha256'], 'inspecao_sha256': record['inspecao_sha256'], 'rodada': args.rodada,
                   'gerado_por': MODELS[args.modelo], 'esforco': args.esforco, 'contrato_sha256': base.contract_hash(), **output})
        record['resultado_sha256'] = base.sha(out.read_bytes())
    save(args.saida / f'{lesson}.juiz.execucao.json', record)
    return f'{lesson}: {output["veredito"] if output else "falhou"} {output["vetos"] if output else ""}, saída {record["consumo"]["output_tokens"]}'


def apply_fix(data, output, affected, cycle, author):
    """Aplica a saída do redator a uma cópia do JSON da aula: unidades corrigidas (só as afetadas), novas, retiradas e, quando devolvido, o contexto."""
    new = copy.deepcopy(data)
    by_number = {u['numero']: u for u in new['unidades']}
    changed = []
    for u in output['unidades_corrigidas']:
        if u['numero'] in by_number and u['numero'] in affected:
            old = by_number[u['numero']]
            u['versao'] = old['versao'] + 1
            u['nota'] = u['nota'] or None
            old.clear()
            old.update(u)
            changed.append(u['numero'])
    highest = max([u['numero'] for u in new['unidades']] + new['retiradas'])
    for n, u in enumerate(output['unidades_novas'], highest + 1):
        new['unidades'].append({'numero': n, **u, 'versao': 1})
        changed.append(n)
    for n in output['retiradas']:
        if n in affected:
            new['unidades'] = [u for u in new['unidades'] if u['numero'] != n]
            new['retiradas'].append(n)
    context = output.get('contexto') or []
    if context:
        new['contexto'] = list(context)
    new['correcoes'] = new.get('correcoes', []) + [{'ciclo': cycle, 'por': author, 'unidades': changed, 'retiradas': output['retiradas'], 'contexto': bool(context), 'observacoes': output['observacoes']}]
    return new, changed


def run_fix(args, lesson, tax, rows):
    row, text, segments, material = rows[lesson]
    target = args.entrada / f'{lesson}.json'
    data = json.loads(target.read_text())
    if args.julgamento:
        judgment = json.loads((args.julgamento / f'{lesson}.julgamento.json').read_text())
    else:
        # Reparo de contrato: as falhas vêm do validador, antes de qualquer inspeção. Não conta como ciclo de correção.
        errors, _ = base.validate_lesson(row, text, segments, material, data, tax)
        found = [(int(m.group(1)), e) for e in errors if (m := re.search(r': U(\d{3}): ', e))]
        if not found:
            return f'{lesson}: sem erro de contrato em unidade' + (f'; resta para a coordenação: {errors}' if errors else '')
        judgment = {'falhas': [{'id': f'C{i}', 'unidades': [n], 'veto': 'contrato', 'evidencia': e, 'impacto': 'Com erro de contrato o arquivo não entra na base.',
                                'mudanca_minima': 'Corrigir só o campo apontado pelo validador, relendo a fonte se a correção tocar faixa ou evidência.',
                                'criterio_de_aceite': 'O validador deixa de apontar este erro e nenhum outro campo da unidade muda.'} for i, (n, e) in enumerate(found, 1)]}
    affected = sorted({n for f in judgment['falhas'] for n in f['unidades']})
    user = '\n\n'.join([source_block(row, text, material), '<falhas_consolidadas>\n' + json.dumps(judgment['falhas'], ensure_ascii=False, indent=1) + '\n</falhas_consolidadas>',
                        '<unidades_afetadas>\n' + json.dumps([u for u in data['unidades'] if u['numero'] in affected], ensure_ascii=False, indent=1) + '\n</unidades_afetadas>',
                        '<titulos_das_demais_unidades>\n' + '\n'.join(f'{u["numero"]:03} {u["titulo"]}' for u in data['unidades'] if u['numero'] not in affected) + '\n</titulos_das_demais_unidades>'])
    output, record = call('redator', fixed_block('redator'), user, schema_for('redator', tax), args.modelo, args.esforco, args.timeout)
    out = args.saida / f'{lesson}.json'
    record.update({'aula': lesson, 'rotulo': args.rotulo, 'ciclo': args.rodada, 'arquivo_anterior_sha256': base.sha(target.read_bytes()), 'destino': str(out.relative_to(base.ROOT))})
    if output:
        new, changed = apply_fix(data, output, affected, args.rodada, MODELS[args.modelo])
        save(out, new)
        errors, warnings = base.validate_lesson(row, text, segments, material, new, tax)
        record.update({'resultado_sha256': base.sha(out.read_bytes()), 'unidades_alteradas': changed, 'validador': {'erros': errors, 'avisos': warnings}})
    save(args.saida / f'{lesson}.redator.ciclo{args.rodada}.execucao.json', record)
    return f'{lesson}: correção {"aplicada" if output else "falhou"}, alteradas {record.get("unidades_alteradas")}, erros {len((record.get("validador") or {}).get("erros", []))}'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('papel', choices=['extrair', 'inspecionar', 'julgar', 'corrigir'])
    parser.add_argument('--aulas', nargs='+', required=True)
    parser.add_argument('--modelo', choices=MODELS, required=True)
    parser.add_argument('--esforco', choices=EFFORTS, required=True)
    parser.add_argument('--rotulo', required=True)
    parser.add_argument('--saida', type=Path, required=True)
    parser.add_argument('--entrada', type=Path, help='pasta com os JSON de aula a inspecionar, julgar ou corrigir')
    parser.add_argument('--inspecao', type=Path)
    parser.add_argument('--julgamento', type=Path)
    parser.add_argument('--prova', type=Path, help='julgar: arquivo de texto com prova de ferramenta pedida pelo juiz; entra no pacote como <prova_da_coordenacao>')
    parser.add_argument('--bloco', type=int, default=0, help='inspeção em blocos: máximo de unidades por chamada (aulas longas)')
    parser.add_argument('--focal', action='store_true', help='inspeção focal de correção: exige --inspecao (anterior) e --julgamento (lista de falhas)')
    parser.add_argument('--rodada', type=int, default=1)
    parser.add_argument('--paralelo', type=int, default=3)
    parser.add_argument('--timeout', type=int, default=2400)
    parser.add_argument('--refazer', action='store_true')
    args = parser.parse_args()
    for name in ('saida', 'entrada', 'inspecao', 'julgamento', 'prova'):
        if getattr(args, name):
            setattr(args, name, getattr(args, name).resolve())
    tax = base.taxonomy()
    rows = {r[0]['aula']: r for r in base.inventory()}
    runner = {'extrair': run_extract, 'inspecionar': run_inspect, 'julgar': run_judge, 'corrigir': run_fix}[args.papel]
    # A primeira aula roda sozinha para gravar o cache do bloco fixo; as demais leem dele em paralelo.
    print(runner(args, args.aulas[0], tax, rows), flush=True)
    with ThreadPoolExecutor(max_workers=args.paralelo) as pool:
        for line in pool.map(lambda lesson: runner(args, lesson, tax, rows), args.aulas[1:]):
            print(line, flush=True)


if __name__ == '__main__':
    sys.exit(main())
