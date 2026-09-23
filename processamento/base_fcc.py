#!/usr/bin/env python3
"""Validação e geração determinística de base de conhecimento por curso (stdlib).

O curso vem da variável de ambiente CURSO (padrão: formato-criativo-de-conteudo). O que é próprio
de cada curso fica em PROFILES: commit das fontes, contagem por grupo, materiais e leitura do manifesto.

Adaptado de base_consulta.py. O JSON por aula em conhecimento/dados/ é a fonte editável;
unidades Markdown, unidades.jsonl, cobertura.jsonl e índices são derivados.
Os enums vêm de conhecimento/taxonomia.md, nunca deste arquivo.
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
PROFILES = {
    'formato-criativo-de-conteudo': {
        'base': 'aaff8b6daa998403849b9edf5393c023c30db8de',
        'aulas_por_grupo': {1: 6, 2: 10, 3: 11, 4: 10, 5: 7, 6: 8, 7: 2},
        # Materiais que não entram no pacote do extrator, com o motivo registrado.
        'materiais_ignorados': {
            'M02_A09': 'PDF de apoio da aula 9 repete o da aula 8 (Storytelling Visual); o Markdown só registra a divergência, sem conteúdo didático da aula',
        },
    },
    'hardcopy-pro': {
        'base': '7470ca05b1ba5a27a1081745df0d881b92aeaec6',
        # 18 grupos na ordem do manifesto; o grupo 2 inclui o material avulso como última aula.
        'aulas_por_grupo': {1: 9, 2: 12, 3: 6, 4: 7, 5: 5, 6: 12, 7: 13, 8: 10, 9: 7, 10: 7, 11: 6, 12: 6, 13: 6, 14: 6, 15: 5, 16: 9, 17: 5, 18: 8},
        'materiais_ignorados': {},
        # Grafias que a transcrição deforma e o contrato (FORMATO, seção 3) manda trocar fora de `evidencia` e `nota`.
        'grafias_deformadas': r'\b(Kinshu\w*|Kishu|Kensho|quinchu\w*|Kinshoten|Kenshu|Genketsu|Kim Shu|quinchotem|BSL|PSL|DSL|MVR|R[áa]dio Cop\w*|R[áa]dio Clop|RedCop\w*|Eleven (Lapse|Eves|Leves|Lex)|Level ?Labs|chat (de PT|EPT|IPT|APT)|VO3|VL3|Rengen|Qify|QI-Fi|Golderi|Vetorbi|UTM file|TapCut|ads librar\w*|Ads Libr\w+|Eds Libr\w+|Rodem Bump|ordenbump|Save from Mad|Tchekhov|ROD)\b',
        # Resíduo de silêncio da transcrição automática: nunca é âncora nem assunto.
        'residuos': r'Legenda Adriana Zanotto|Australian Broadcasting Corporation',
        # Material sem aula gravada: entra como aula só de material, no fim do grupo indicado.
        # Decisão de Will em 21/09/2026: páginas de aula e índice espelham as pastas do curso, como o criador organizou. Os dados de consulta continuam únicos.
        'espelha_curso': True,
        'materiais_avulsos': [
            {'grupo': '01 Hard Copy/2a Temporada - Kishotenketsu', 'pasta': 'hc_surpresa_estruturacao_de_copy',
             'titulo': 'Surpresa: estruturação de copy', 'arquivo': 'Materiais/01 Hard Copy/Surpresa/estruturacao_de_copy.md'},
        ],
    },
}
COURSE = os.environ.get('CURSO', 'formato-criativo-de-conteudo')
PROFILE = PROFILES[COURSE]
CDIR = ROOT / COURSE
KNOW = CDIR / 'conhecimento'
PROC = CDIR / 'processamento' / 'base-consulta'
BASE = PROFILE['base']
REPO = 'tc3midia/cursos'
LESSONS_PER_MODULE = PROFILE['aulas_por_grupo']
IGNORED_MATERIALS = PROFILE['materiais_ignorados']
DEFORMED = re.compile(PROFILE['grafias_deformadas'], re.I) if PROFILE.get('grafias_deformadas') else None
RESIDUE = re.compile(PROFILE['residuos'], re.I) if PROFILE.get('residuos') else None
STAMP = re.compile(r'^\[(\d\d):(\d\d):(\d\d)\.(\d{3})[–-](\d\d):(\d\d):(\d\d)\.(\d{3})\] ?', re.M)
SOURCES = ('fala', 'material', 'fala+material')
UNIT_FIELDS = {'numero', 'titulo', 'tipo', 'tema', 'tarefas', 'plataformas', 'fonte', 'inicio', 'fim', 'condicoes',
               'perecivel', 'confianca', 'nota', 'proposta_tag', 'corpo', 'evidencia', 'versao'}
HASH_FIELDS = ('tipo', 'plataformas', 'tema', 'tarefas', 'fonte', 'inicio', 'fim', 'condicoes', 'perecivel', 'confianca', 'corpo')
NUMBER = re.compile(r'\d|R\$|%|\b(um|uma|dois|duas|tr[eê]s|quatro|cinco|seis|sete|oito|nove|dez|onze|doze|quinze|vinte|trinta|quarenta|cinquenta|cem|mil|milh[ãõ]o|milh[õo]es|metade|dobro|triplo)\b', re.I)
FORBIDDEN_WORDS = re.compile(r'\b(hoje|atualmente|neste momento)\b', re.I)
TIME_IN_BODY = re.compile(r'\b\d{1,2}:\d{2}(:\d{2})?\b|\[\[|\*\*\[')


def sha(data):
    return hashlib.sha256(data).hexdigest()


def norm(text):
    return ' '.join(text.split())


def word_seq(text):
    """Sequência de palavras para comparar âncoras: sem marcações de tempo, caixa nem pontuação."""
    text = STAMP.sub(' ', text)
    return ' ' + ' '.join(re.sub(r'[^\w\s]', ' ', text.lower()).split()) + ' '


def clock(value):
    value = int(value)
    return f'{value // 3600:02}:{value % 3600 // 60:02}:{value % 60:02}'


def dump(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + '\n'


# ---------------------------------------------------------------- taxonomia

def taxonomy():
    """Lê os enums de taxonomia.md: seções `## Tipos|Temas|Tarefas|Plataformas`, itens "- `slug` — definição"."""
    text = (KNOW / 'taxonomia.md').read_text()
    result = {}
    for name in ('Tipos', 'Temas', 'Tarefas', 'Plataformas'):
        match = re.search(rf'^## {name}\n(.*?)(?=^## |\Z)', text, re.M | re.S)
        if not match:
            raise ValueError(f'taxonomia.md sem seção ## {name}')
        items = re.findall(r'^- `([a-z0-9-]+)` — (.+)$', match.group(1), re.M)
        if not items:
            raise ValueError(f'taxonomia.md: seção {name} vazia')
        result[name.lower()] = dict(items)
    return result


def contract_hash():
    lines = [f'{name}\t{sha((KNOW / name).read_bytes())}' for name in ('FORMATO.md', 'taxonomia.md')]
    return sha('\n'.join(lines).encode())


# ---------------------------------------------------------------- inventário

def parse_segments(text):
    spans = list(STAMP.finditer(text))
    segments = []
    for i, m in enumerate(spans):
        g = list(map(int, m.groups()))
        start = g[0] * 3600 + g[1] * 60 + g[2] + g[3] / 1000
        end = g[4] * 3600 + g[5] * 60 + g[6] + g[7] / 1000
        body = text[m.end():spans[i + 1].start() if i + 1 < len(spans) else len(text)]
        segments.append((start, end, body))
    return segments


def source_files(files):
    return {k: {'caminho': p.relative_to(ROOT).as_posix(), 'sha256': sha(p.read_bytes())} for k, p in files.items()}


def seconds(value):
    h, m, s = value.split(':')
    return int(h) * 3600 + int(m) * 60 + float(s)


def inventory_hardcopy():
    """Manifesto sem número de aula: o grupo e a ordem vêm da posição no manifesto; o aula_id vem da pasta, que é estável."""
    items = [json.loads(line) for line in (CDIR / 'manifest.jsonl').read_text().splitlines()]
    groups = list(dict.fromkeys(item['grupo'] for item in items))
    rows, order = [], defaultdict(int)

    def common(group, folder, title):
        number = groups.index(group) + 1
        order[number] += 1
        return {'curso': COURSE, 'aula': f'G{number:02}_A{order[number]:02}', 'aula_id': sha(f'{COURSE}/{folder}'.encode())[:16],
                'trilha': group.split('/')[0], 'modulo': f'{number:02}', 'modulo_titulo': group, 'ordem': order[number],
                'titulo': title, 'pasta': folder, 'fonte_repo': REPO, 'fonte_commit': BASE, 'material_ignorado': None}

    for item in items:
        source = CDIR / item['arquivo']
        folder = source.parent
        text = source.read_text()
        segments = parse_segments(text)
        if not segments:
            raise ValueError(f'Fonte sem timestamps: {source}')
        row = {**common(item['grupo'], folder.name, item['titulo']),
               'duracao_segundos': seconds(item['duracao_original']), 'fim_transcricao_segundos': max(s[1] for s in segments),
               'palavras_transcricao': len(text.split()), 'video_sha256': item['sha256'], 'video_bytes': item['tamanho_bytes'],
               'fontes': source_files({'transcricao': source, 'legenda': folder / 'legenda.srt', 'segmentos': folder / 'segmentos.json'})}
        rows.append((row, text, segments, None))
    for extra in PROFILE.get('materiais_avulsos', []):
        path = CDIR / extra['arquivo']
        row = {**common(extra['grupo'], extra['pasta'], extra['titulo']), 'duracao_segundos': 0, 'fim_transcricao_segundos': 0,
               'palavras_transcricao': 0, 'video_sha256': None, 'video_bytes': 0, 'fontes': source_files({'material': path})}
        rows.append((row, '', [], path.read_text()))
    rows.sort(key=lambda r: r[0]['aula'])
    return rows


def inventory():
    if COURSE == 'hardcopy-pro':
        return inventory_hardcopy()
    rows = []
    for line in (CDIR / 'manifest.jsonl').read_text().splitlines():
        item = json.loads(line)
        module = int(re.search(r'Módulo (\d\d)', item['modulo']).group(1))
        lesson = f'M{module:02}_A{item["aula"]:02}'
        source = CDIR / item['arquivo']
        folder = source.parent
        text = source.read_text()
        segments = parse_segments(text)
        if not segments:
            raise ValueError(f'Fonte sem timestamps: {source}')
        material = folder.parent / 'Materiais' / f'{folder.name}.md'
        files = {'transcricao': source, 'legenda': folder / 'legenda.srt', 'segmentos': folder / 'segmentos.json'}
        if material.exists():
            files['material'] = material
        row = {
            'curso': COURSE, 'aula': lesson, 'aula_id': sha(f'{COURSE}/{lesson}'.encode())[:16],
            'modulo': f'{module:02}', 'modulo_titulo': item['modulo'], 'ordem': item['aula'],
            'titulo': item['titulo'], 'pasta': folder.name,
            'duracao_segundos': item['duracao_original_segundos'],
            'fim_transcricao_segundos': max(s[1] for s in segments),
            'palavras_transcricao': len(text.split()),
            'fonte_repo': REPO, 'fonte_commit': BASE,
            'video_sha256': item['sha256'], 'video_bytes': item['tamanho_bytes'],
            'fontes': {k: {'caminho': p.relative_to(ROOT).as_posix(), 'sha256': sha(p.read_bytes())} for k, p in files.items()},
            'material_ignorado': IGNORED_MATERIALS.get(lesson) if material.exists() else None,
        }
        rows.append((row, text, segments, material.read_text() if material.exists() and lesson not in IGNORED_MATERIALS else None))
    rows.sort(key=lambda r: r[0]['aula'])
    return rows


def inventory_errors(rows):
    errors = []
    count = defaultdict(int)
    for row, *_ in rows:
        count[int(row['modulo'])] += 1
        if 'transcricao' in row['fontes'] and row['titulo'] != (CDIR / row['fontes']['transcricao']['caminho'].split('/', 1)[1]).read_text().splitlines()[0].removeprefix('# '):
            errors.append(f'{row["aula"]}: título do manifesto difere do cabeçalho da transcrição')
    if dict(count) != LESSONS_PER_MODULE:
        errors.append(f'Contagem por módulo divergente: {dict(count)}')
    if len({r[0]['aula_id'] for r in rows}) != len(rows):
        errors.append('aula_id repetido')
    return errors


def source_integrity(rows):
    """Compara cada fonte no disco com o objeto Git do commit de referência."""
    errors = []
    for row, *_ in rows:
        for kind, info in row['fontes'].items():
            blob = subprocess.run(['git', '-C', str(ROOT), 'show', f'{BASE}:{info["caminho"]}'], capture_output=True)
            if blob.returncode != 0:
                errors.append(f'{row["aula"]}: {kind} ausente no commit de referência')
            elif sha(blob.stdout) != info['sha256']:
                errors.append(f'{row["aula"]}: {kind} difere do commit de referência')
    return errors


# ---------------------------------------------------------------- validação

def unit_hash(row, u):
    canon = {'id': unit_id(row, u)}
    for field in HASH_FIELDS:
        value = u.get(field)
        if isinstance(value, list):
            value = sorted(value)
        if field == 'corpo':
            value = '\n'.join(norm(line) for line in value.splitlines() if line.strip())
        canon[field] = value
    return sha(json.dumps(canon, ensure_ascii=False, sort_keys=True).encode())


def unit_id(row, u):
    return f'U:{row["aula_id"]}:{u["numero"]:03}'


def must_be_perishable(u):
    """Marcação objetiva do contrato: o que o script pode decidir sozinho sobre `perecivel`."""
    return (u.get('tipo') == 'ferramenta' or not set(u.get('plataformas') or ['geral']) <= {'geral'}
            or u.get('tema') == 'curso-e-recursos' or 'usar-recursos-do-curso' in (u.get('tarefas') or []))


def validate_lesson(row, text, segments, material, data, tax):
    errors, warnings = [], []
    transcript = norm(text)
    material_text = norm(material) if material else ''
    transcript_words, material_words = word_seq(text), word_seq(material or '')

    def require(ok, message):
        if not ok:
            errors.append(f'{row["aula"]}: {message}')

    for field in ('curso', 'aula', 'titulo'):
        require(data.get(field) == row[field], f'{field} diferente da fonte')
    context = data.get('contexto', [])
    require(isinstance(context, list) and 3 <= len(context) <= 8 and all(isinstance(x, str) and x.strip() for x in context), 'contexto exige 3–8 frases')
    for sentence in context if isinstance(context, list) else []:
        require(not FORBIDDEN_WORDS.search(str(sentence)) and not TIME_IN_BODY.search(str(sentence)), 'contexto com marcador temporal ou timestamp')
        if DEFORMED and DEFORMED.search(str(sentence)):
            errors.append(f'{row["aula"]}: contexto com grafia deformada "{DEFORMED.search(str(sentence)).group(0)}"')
    retired = data.get('retiradas', [])
    require(isinstance(retired, list) and all(type(n) is int for n in retired), 'retiradas inválidas')
    units = data.get('unidades', [])
    require(isinstance(units, list) and len(units) >= 1, 'nenhuma unidade')
    numbers = [u.get('numero') for u in units if isinstance(u, dict)]
    require(len(set(numbers)) == len(numbers), 'numero repetido')
    if all(type(n) is int for n in numbers) and numbers:
        require(sorted(numbers + list(retired)) == list(range(1, max(numbers + list(retired)) + 1)), 'numeração com furo: presentes ∪ retiradas deve cobrir 001..max')
    if not 3 <= len(units) <= 60:
        warnings.append(f'{row["aula"]}: {len(units)} unidades, fora da faixa 3–60')
    for u in units:
        tag = f'U{u.get("numero", 0):03}' if type(u.get('numero')) is int else 'U???'
        missing = UNIT_FIELDS - u.keys()
        require(not missing, f'{tag}: campos ausentes {sorted(missing)}')
        if missing:
            continue
        require(isinstance(u['titulo'], str) and 1 <= len(u['titulo']) <= 80, f'{tag}: título fora de 1–80 caracteres')
        require(u['tipo'] in tax['tipos'], f'{tag}: tipo inválido {u["tipo"]!r}')
        require(u['tema'] in tax['temas'], f'{tag}: tema inválido {u["tema"]!r}')
        require(isinstance(u['tarefas'], list) and set(u['tarefas']) <= set(tax['tarefas']), f'{tag}: tarefas inválidas {u["tarefas"]!r}')
        require(bool(u['tarefas']) or u['tipo'] in ('conceito', 'limite'), f'{tag}: tarefas vazias só em conceito ou limite')
        require(isinstance(u['plataformas'], list) and bool(u['plataformas']) and set(u['plataformas']) <= set(tax['plataformas']), f'{tag}: plataformas inválidas {u["plataformas"]!r}')
        require(type(u['perecivel']) is bool, f'{tag}: perecivel não booleano')
        require(u['tipo'] != 'ferramenta' or u['perecivel'] is True, f'{tag}: ferramenta exige perecivel true')
        require(u['perecivel'] is True or not isinstance(u['plataformas'], list) or set(u['plataformas']) <= {'geral'}, f'{tag}: plataforma específica exige perecivel true')
        require(u['perecivel'] is True or not must_be_perishable(u), f'{tag}: recurso ou estrutura do curso exige perecivel true')
        require(u['confianca'] in ('alta', 'media', 'baixa'), f'{tag}: confiança inválida')
        require(u['confianca'] != 'baixa' or bool(u['nota']), f'{tag}: baixa confiança sem nota')
        require(type(u['versao']) is int and u['versao'] >= 1, f'{tag}: versão inválida')
        for optional in ('condicoes', 'nota', 'proposta_tag'):
            require(u[optional] is None or (isinstance(u[optional], str) and u[optional].strip()), f'{tag}: {optional} deve ser texto ou null')
        if u['proposta_tag']:
            require(re.match(r'^(tema|tarefa|plataforma): [a-z0-9-]+ — .+', u['proposta_tag']), f'{tag}: proposta_tag fora do padrão')
        body = u['corpo'] if isinstance(u['corpo'], str) else ''
        lines = [line for line in body.splitlines() if line.strip()]
        limit = 15 if u['tipo'] in ('procedimento', 'exemplo', 'estrutura') else 8
        require(1 <= len(lines) <= limit and len(body.strip()) > 15, f'{tag}: corpo com {len(lines)} linhas (limite {limit})')
        require(not TIME_IN_BODY.search(body), f'{tag}: timestamp ou marcação no corpo')
        require(not FORBIDDEN_WORDS.search(body), f'{tag}: marcador temporal no corpo')
        if DEFORMED:
            for field in ('titulo', 'corpo', 'condicoes'):
                found = DEFORMED.search(u[field] or '')
                require(not found, f'{tag}: grafia deformada "{found.group(0) if found else ""}" em {field}; usar a grafia adotada do FORMATO')
        if RESIDUE:
            require(not RESIDUE.search(str(u['evidencia']) + ' ' + body), f'{tag}: resíduo de silêncio da transcrição usado como fonte')
        if u['tipo'] == 'regua':
            require(NUMBER.search(body), f'{tag}: régua sem número')
        if u['tipo'] == 'procedimento':
            require(body.startswith('Pré-condição:') and len(re.findall(r'^\d+\. ', body, re.M)) >= 2, f'{tag}: procedimento exige "Pré-condição:" e ≥2 passos numerados')
        if u['tipo'] == 'estrutura':
            require(len(re.findall(r'^\d+\. ', body, re.M)) >= 2, f'{tag}: estrutura exige ≥2 partes numeradas')
        if u['tipo'] == 'decisao':
            require(body.startswith(('Se ', 'Quando ')), f'{tag}: decisão começa com "Se " ou "Quando "')
        if u['tipo'] == 'exemplo':
            require(all(mark in body for mark in ('Situação:', 'O que aconteceu:', 'Lógica:')), f'{tag}: exemplo exige Situação/O que aconteceu/Lógica')
        if u['tipo'] == 'fato-material':
            require(u['fonte'] == 'material', f'{tag}: fato-material exige fonte material')
        # Cópia bruta por sequência de palavras: marcação de tempo, caixa, pontuação e Markdown da fonte não escondem a cópia.
        words = word_seq(body).split()
        for haystack in (transcript_words, material_words):
            require(not any(' ' + ' '.join(words[i:i + 25]) + ' ' in haystack for i in range(max(0, len(words) - 24))), f'{tag}: cópia de 25 palavras no corpo')
        require(u['fonte'] in SOURCES, f'{tag}: fonte inválida {u["fonte"]!r}')
        require(u['fonte'] == 'fala' or bool(material_text), f'{tag}: fonte cita material, mas a aula não tem material utilizável')
        evidence = u['evidencia'] if isinstance(u['evidencia'], str) else ''
        require(1 <= len(evidence.split()) <= 24, f'{tag}: evidência exige 1–24 palavras')
        start, end = u['inicio'], u['fim']
        if u['fonte'] == 'material':
            require(start is None and end is None, f'{tag}: faixa proibida em fonte só material')
            require(bool(evidence) and word_seq(evidence) in material_words, f'{tag}: evidência não literal no material')
        else:
            valid = type(start) in (int, float) and type(end) in (int, float) and 0 <= start < end <= row['fim_transcricao_segundos'] + 2
            require(valid, f'{tag}: faixa inválida {start}–{end}')
            literal = bool(evidence) and word_seq(evidence) in transcript_words
            require(literal, f'{tag}: evidência não literal na transcrição')
            if valid and literal:
                window = word_seq(' '.join(s[2] for s in segments if s[0] < end and s[1] > start))
                require(word_seq(evidence) in window, f'{tag}: evidência fora da faixa')
    return errors, warnings


def review_errors(row, data_path, sample):
    errors = []
    current = sha(data_path.read_bytes())
    inspection = PROC / 'revisao' / 'inspecao' / f'{row["aula"]}.json'
    judgment = PROC / 'revisao' / 'julgamento' / f'{row["aula"]}.json'
    if inspection.exists():
        review = json.loads(inspection.read_text())
        if review.get('arquivo_sha256') != current:
            errors.append(f'{row["aula"]}: inspeção desatualizada')
    elif row['aula'] in sample:
        errors.append(f'{row["aula"]}: inspeção da amostra ausente')
    if row['aula'] in sample:
        if not judgment.exists():
            errors.append(f'{row["aula"]}: julgamento da amostra ausente')
        else:
            result = json.loads(judgment.read_text())
            if result.get('arquivo_sha256') != current or result.get('inspecao_sha256') != sha(inspection.read_bytes()):
                errors.append(f'{row["aula"]}: julgamento desatualizado')
            if result.get('veredito') != 'passa':
                errors.append(f'{row["aula"]}: julgamento não aprovado')
    return errors


# ---------------------------------------------------------------- geração

def yaml_value(value):
    if value is None:
        return None
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if isinstance(value, list):
        return '[' + ', '.join(value) + ']'
    if isinstance(value, (int, float)):
        return str(value)
    return json.dumps(value, ensure_ascii=False)


def source_label(row, u):
    name = Path(row['fontes']['material']['caminho']).name if 'material' in row['fontes'] else None
    return {'fala': 'fala', 'material': f'txt:{name}', 'fala+material': f'fala+txt:{name}'}[u['fonte']]


def unit_md(row, u):
    uid = unit_id(row, u)
    fields = [('tipo', u['tipo']), ('plataforma', u['plataformas']), ('tema', u['tema']), ('tarefas', u['tarefas']),
              ('fonte', None), ('faixa', None), ('condicoes', u['condicoes']), ('perecivel', u['perecivel']),
              ('confianca', u['confianca']), ('versao', u['versao']), ('evidencia', u['evidencia']), ('nota', u['nota']),
              ('proposta_tag', u['proposta_tag'])]
    lines = [f'<a id="{uid.lower().replace(":", "-")}"></a>', '', f'### {uid} — {u["titulo"]}', '```yaml']
    for key, value in fields:
        if key == 'fonte':
            lines.append(f'fonte: {source_label(row, u)}')
        elif key == 'faixa':
            if u['inicio'] is not None:
                lines.append(f'faixa: {clock(u["inicio"])}–{clock(u["fim"])}')
        elif value is not None:
            lines.append(f'{key}: {yaml_value(value)}')
    lines += ['```', u['corpo'].strip(), '']
    return '\n'.join(lines)


def page_path(row):
    """Caminho da página da aula dentro de `conhecimento/unidades/`. Curso espelhado: o mesmo caminho da pasta da fonte no curso."""
    if not PROFILE.get('espelha_curso'):
        return f'{row["aula"]}.md'
    source = next(iter(row['fontes'].values()))['caminho']
    return Path(source).parent.relative_to(COURSE).as_posix() + '.md'


def page_group(row):
    """Pasta do curso em que a aula mora, com o nome que o criador deu: trilha e grupo, ou `Materiais/...` para material avulso."""
    return Path(page_path(row)).parent.as_posix()


def lesson_md(row, data, status):
    names = (['transcricao.md'] if 'transcricao' in row['fontes'] else []) + ([Path(row['fontes']['material']['caminho']).name] if 'material' in row['fontes'] and not row['material_ignorado'] else [])
    front = ['---', 'type: unidades-aula', f'status: {status}', f'title: {json.dumps(row["titulo"], ensure_ascii=False)}',
             f'curso: {COURSE}', *([f'trilha: {json.dumps(row["trilha"], ensure_ascii=False)}'] if 'trilha' in row else []),
             *([f'grupo: {json.dumps(page_group(row), ensure_ascii=False)}'] if PROFILE.get('espelha_curso') else []), f'modulo: "{row["modulo"]}"', f'ordem: {row["ordem"]}', f'aula: {row["aula"]}', f'aula_id: {row["aula_id"]}',
             'account_id: account.86ajrj8n9', f'fonte_repo: {REPO}', f'fonte_commit: {BASE[:7]}', 'fontes:', *[f'  - {n}' for n in names]]
    if row['material_ignorado']:
        front += ['fontes_ignoradas:', f'  - {Path(row["fontes"]["material"]["caminho"]).name}: {json.dumps(row["material_ignorado"], ensure_ascii=False)}']
    front += [f'extraido_em: {data.get("extraido_em", "")}', f'gerado_por: {data.get("gerado_por", "")}',
              f'retiradas: {yaml_value([f"U:{row["aula_id"]}:{n:03}" for n in data.get("retiradas", [])])}', '---', '']
    body = [f'# {row["titulo"]}', '', '## Contexto da aula', '', *data['contexto'], '', '## Unidades', '']
    return '\n'.join(front + body + [unit_md(row, u) for u in data['unidades']]).rstrip() + '\n'


def lesson_status(row):
    judgment = PROC / 'revisao' / 'julgamento' / f'{row["aula"]}.json'
    inspection = PROC / 'revisao' / 'inspecao' / f'{row["aula"]}.json'
    if judgment.exists() and json.loads(judgment.read_text()).get('veredito') == 'passa':
        return 'ouro' if json.loads(judgment.read_text()).get('ouro') else 'revisado'
    return 'validado' if inspection.exists() else 'rascunho'


def generated(allow_partial=False):
    tax = taxonomy()
    rows = inventory()
    outputs = {f'{COURSE}/conhecimento/manifest.json': dump({'fonte_repo': REPO, 'fonte_commit': BASE, 'contrato_sha256': contract_hash(), 'aulas': [r[0] for r in rows]})}
    flat, entries, proposals = [], [], defaultdict(list)
    for row, text, segments, material in rows:
        path = KNOW / 'dados' / f'{row["aula"]}.json'
        if not path.exists():
            if allow_partial:
                continue
            raise ValueError(f'Aula ausente: {path}')
        data = json.loads(path.read_text())
        errors, _ = validate_lesson(row, text, segments, material, data, tax)
        if errors:
            raise ValueError('\n'.join(errors))
        status = lesson_status(row)
        entries.append((row, data, status))
        outputs[f'{COURSE}/conhecimento/unidades/{page_path(row)}'] = lesson_md(row, data, status)
        for u in data['unidades']:
            record = {'id': unit_id(row, u), 'aula': row['aula'], 'aula_id': row['aula_id'], **({'trilha': row['trilha']} if 'trilha' in row else {}),
                      **({'grupo': page_group(row), 'pagina': f'unidades/{page_path(row)}'} if PROFILE.get('espelha_curso') else {}), 'modulo': row['modulo'], 'ordem': row['ordem'],
                      'aula_titulo': row['titulo'], 'status_aula': status, **{k: u[k] for k in sorted(UNIT_FIELDS)}, 'hash': unit_hash(row, u)}
            flat.append(record)
            if u['proposta_tag']:
                proposals[u['proposta_tag']].append(record['id'])
    outputs[f'{COURSE}/conhecimento/unidades.jsonl'] = ''.join(json.dumps(r, ensure_ascii=False, sort_keys=True) + '\n' for r in flat)
    # Cobertura: toda combinação tarefa × plataforma da taxonomia aparece, inclusive as vazias.
    coverage = []
    for task in tax['tarefas']:
        for platform in tax['plataformas']:
            hits = [r for r in flat if task in r['tarefas'] and platform in r['plataformas']]
            coverage.append({'tarefa': task, 'plataforma': platform, 'n_unidades': len(hits), 'cobertura': 'presente' if hits else 'ausente',
                             'aulas': sorted({r['aula'] for r in hits}), 'ids': [r['id'] for r in hits]})
    outputs[f'{COURSE}/conhecimento/cobertura.jsonl'] = ''.join(json.dumps(r, ensure_ascii=False, sort_keys=True) + '\n' for r in coverage)

    def link(r):
        return f'- [{r["aula"]}: {r["titulo"]}](../{quote(r["pagina"]) if "pagina" in r else "unidades/" + r["aula"] + ".md"}#{r["id"].lower().replace(":", "-")}) · `{r["id"]}` · {r["tipo"]}' + (' · perecível' if r['perecivel'] else '')

    for kind, key, single in (('temas', 'tema', True), ('tarefas', 'tarefas', False)):
        for slug, definition in tax[kind].items():
            hits = [r for r in flat if (r[key] == slug if single else slug in r[key])]
            page = [f'# {slug}', '', definition, '', f'{len(hits)} unidades. Índice sem síntese nova; cada link abre a aula com a faixa e a fonte.', '']
            if not hits:
                page += ['Nada nas fontes processadas. Ausência registrada como ausência: o curso, no alcance já extraído, não cobre este item.', '']
            by_type = defaultdict(list)
            for r in hits:
                by_type[r['tipo']].append(r)
            for tipo in tax['tipos']:
                if by_type[tipo]:
                    page += [f'## {tipo}', '', *[link(r) for r in by_type[tipo]], '']
            outputs[f'{COURSE}/conhecimento/{kind}/{slug}.md'] = '\n'.join(page).rstrip() + '\n'
    index = [f'# Base de conhecimento: {COURSE}', '', f'{len(entries)}/{len(rows)} aulas · {len(flat)} unidades.', '',
             'Base para consulta por agentes. Dados de primeira classe: [unidades.jsonl](unidades.jsonl) e [cobertura.jsonl](cobertura.jsonl). '
             'Contrato em [FORMATO.md](FORMATO.md) e [taxonomia.md](taxonomia.md). O alcance real da revisão está em [processamento](../processamento/base-consulta/README.md).', '',
             '## Aulas', '']
    if PROFILE.get('espelha_curso'):
        # Mesma ordem e mesmos nomes de pasta do curso; material avulso por último, na pasta em que o curso o guarda.
        index += ['As pastas de `unidades/` repetem as do curso, com os nomes que o criador deu.', '']
        ordered = sorted(entries, key=lambda e: ('transcricao' not in e[0]['fontes'], e[0]['aula']))
        for group in dict.fromkeys(page_group(row) for row, _, _ in ordered):
            index += [f'### {group}', '', '| Aula | Título | Unidades | Status |', '|---|---|---:|---|']
            index += [f'| {row["aula"]} | [{row["titulo"]}](unidades/{quote(page_path(row))}) | {len(data["unidades"])} | {status} |' for row, data, status in ordered if page_group(row) == group]
            index.append('')
        index.pop()
    else:
        index += ['| Aula | Título | Unidades | Status |', '|---|---|---:|---|']
        index += [f'| {row["aula"]} | [{row["titulo"]}](unidades/{row["aula"]}.md) | {len(data["unidades"])} | {status} |' for row, data, status in entries]
    for kind in ('temas', 'tarefas'):
        index += ['', f'## {kind.capitalize()}', '']
        for slug in tax[kind]:
            n = sum(1 for r in flat if (r['tema'] == slug if kind == 'temas' else slug in r['tarefas']))
            index.append(f'- [{slug}]({kind}/{slug}.md): {n} unidades' + ('' if n else ' (ausente)'))
    outputs[f'{COURSE}/conhecimento/README.md'] = '\n'.join(index) + '\n'
    tags = ['# Propostas de tag', '', 'Agregadas por texto. Tag nova só entra na taxonomia por decisão registrada.', '']
    tags += [f'- {text}: {", ".join(ids)}' for text, ids in sorted(proposals.items())] or ['Nenhuma.']
    outputs[f'{COURSE}/conhecimento/propostas_tags.md'] = '\n'.join(tags) + '\n'
    return outputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inventory', action='store_true', help='só inventário, contagens e integridade das fontes')
    parser.add_argument('--partial', action='store_true')
    parser.add_argument('--reviews', action='store_true')
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--write', action='store_true')
    parser.add_argument('--file', help='validar um JSON de aula fora de conhecimento/dados (saída temporária)')
    args = parser.parse_args()
    rows = inventory()
    errors = inventory_errors(rows)
    if args.inventory:
        errors += source_integrity(rows)
        late = [f'{r[0]["aula"]}: transcrição termina {r[0]["fim_transcricao_segundos"] - r[0]["duracao_segundos"]:.0f}s depois da duração do manifesto' for r in rows if r[0]['fim_transcricao_segundos'] > r[0]['duracao_segundos'] + 2]
        print(dump({'aulas': len(rows), 'palavras': sum(r[0]['palavras_transcricao'] for r in rows), 'com_material': sum(1 for r in rows if r[3]), 'material_ignorado': [r[0]['aula'] for r in rows if r[0]['material_ignorado']], 'avisos': late, 'erros': errors}))
        return bool(errors)
    tax = taxonomy()
    by_lesson = {r[0]['aula']: r for r in rows}
    warnings = []
    if args.file:
        data = json.loads(Path(args.file).read_text())
        row, text, segments, material = by_lesson[data['aula']]
        errors, warnings = validate_lesson(row, text, segments, material, data, tax)
        print(dump({'aula': row['aula'], 'unidades': len(data.get('unidades', [])), 'erros': errors, 'avisos': warnings}))
        return bool(errors)
    sample = set(json.loads((PROC / 'amostra.json').read_text())['aulas']) if (PROC / 'amostra.json').exists() else set()
    data_files = {p.stem for p in (KNOW / 'dados').glob('*.json')}
    errors += [f'Dados sem fonte: {name}' for name in sorted(data_files - set(by_lesson))]
    for row, text, segments, material in rows:
        path = KNOW / 'dados' / f'{row["aula"]}.json'
        if path.exists():
            e, w = validate_lesson(row, text, segments, material, json.loads(path.read_text()), tax)
            errors += e
            warnings += w
            if args.reviews:
                errors += review_errors(row, path, sample)
        elif not args.partial:
            errors.append(f'{row["aula"]}: dados ausentes')
    if not errors:
        outputs = generated(args.partial)
        if args.write:
            for name, content in outputs.items():
                target = ROOT / name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(content)
        if args.check:
            errors += [f'Gerado divergente/ausente: {name}' for name, content in outputs.items() if not (ROOT / name).exists() or (ROOT / name).read_text() != content]
    print(dump({'curso': COURSE, 'aulas_fontes': len(rows), 'aulas_extraidas': len(data_files), 'erros': errors, 'avisos': warnings}))
    return bool(errors)


if __name__ == '__main__':
    sys.exit(main())
