#!/usr/bin/env python3
"""Conduz um lote já extraído da base FCC até o veredito: reparo de contrato, inspeção, julgamento e correções.

Só aplica as regras fixadas em RUBRICA.md e piloto/PLANO.md. Não decide nada: aula bloqueada, com erro de
contrato residual ou reprovada depois do teto de dois ciclos fica fora da publicação e aparece no resumo.
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import base_fcc as base  # noqa: E402

RUNNER = Path(__file__).resolve().parent / 'fcc_executar.py'


def run(role, lessons, model, effort, label, **folders):
    if not lessons:
        return
    cmd = [sys.executable, str(RUNNER), role, '--aulas', *lessons, '--modelo', model, '--esforco', effort, '--rotulo', label, '--paralelo', '3']
    for key, value in folders.items():
        if value is True:
            cmd.append(f'--{key}')
        elif value is not None:
            cmd += [f'--{key}', str(value)]
    print(f'>> {role} {" ".join(lessons)}', flush=True)
    subprocess.run(cmd, check=False)


def contract_errors(folder, lesson, rows, tax):
    row, text, segments, material = rows[lesson]
    return base.validate_lesson(row, text, segments, material, json.loads((folder / f'{lesson}.json').read_text()), tax)[0]


TIME_REFERENCE = re.compile(r'\s*\(?\b(a partir de|em torno de|por volta de|perto de|entre|de|até|após|depois de)\s+(o minuto\s+)?\d{1,2}:\d{2}(:\d{2})?'
                            r'(\s*(a|e|até|–|-)\s*\d{1,2}:\d{2}(:\d{2})?)?\)?', re.I)


def strip_context_times(folder, lesson):
    """Erro mecânico recorrente: o extrator localiza trecho degradado pelo relógio no contexto da aula. O script retira só a referência de tempo."""
    path = folder / f'{lesson}.json'
    data = json.loads(path.read_text())
    changed = []
    for i, sentence in enumerate(data['contexto']):
        if base.TIME_IN_BODY.search(sentence):
            cleaned = ' '.join(TIME_REFERENCE.sub('', sentence).split()).replace(' ,', ',').replace(' .', '.')
            if cleaned != sentence and not base.TIME_IN_BODY.search(cleaned):
                changed.append({'antes': sentence, 'depois': cleaned})
                data['contexto'][i] = cleaned
    if changed:
        data.setdefault('correcoes', []).append({'ciclo': 0, 'por': 'script', 'unidades': [], 'retiradas': [], 'observacoes': 'Erro mecânico de contrato no contexto da aula: retirada a referência de tempo. ' + json.dumps(changed, ensure_ascii=False)})
        path.write_text(base.dump(data))
    return changed


def verdict(folder, lesson):
    path = folder / f'{lesson}.julgamento.json'
    return json.loads(path.read_text())['veredito'] if path.exists() else None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pasta', type=Path, required=True)
    parser.add_argument('--rotulo', required=True)
    parser.add_argument('--aulas', nargs='+', required=True)
    parser.add_argument('--julgar-todas', action='store_true', help='leva ao juiz toda aula indicada, com ou sem apontamento da inspeção')
    args = parser.parse_args()
    folder = args.pasta.resolve()
    tax = base.taxonomy()
    rows = {r[0]['aula']: r for r in base.inventory()}
    sample = set(json.loads((base.PROC / 'amostra.json').read_text())['aulas'])
    summary = {}

    # 1. Reparo de contrato: uma tentativa, antes de qualquer inspeção. Não conta como ciclo de correção.
    for lesson in args.aulas:
        strip_context_times(folder, lesson)
    broken = [a for a in args.aulas if contract_errors(folder, a, rows, tax)]
    run('corrigir', broken, 'claude-sonnet-5', 'high', f'{args.rotulo}-reparo', rodada=0, entrada=folder, saida=folder)
    for lesson in args.aulas:
        errors = contract_errors(folder, lesson, rows, tax)
        if errors:
            summary[lesson] = {'estado': 'erro de contrato residual', 'pasta': str(folder), 'erros': errors}
    alive = [a for a in args.aulas if a not in summary]

    # 2. Inspeção com fonte em todas as aulas.
    run('inspecionar', alive, 'claude-sonnet-5', 'xhigh', args.rotulo, entrada=folder, saida=folder, bloco=20)
    to_judge = []
    for lesson in alive:
        path = folder / f'{lesson}.inspecao.json'
        if not path.exists():
            summary[lesson] = {'estado': 'inspeção falhou', 'pasta': str(folder)}
            continue
        report = json.loads(path.read_text())
        # Gravidade é decisão do juiz: desvio ou sem-lastro leva a aula a julgamento mesmo quando o inspetor o classifica como menor.
        material = ([f['numero'] for f in report['unidades'] if f['gravidade'] == 'material' or f['veredito'] in ('desvio', 'sem-lastro')]
                    + ['omissão' for o in report['omissoes'] if o['gravidade'] == 'material'])
        # A rubrica reprova acima de 10% de faixas erradas: a conta é objetiva e também leva a aula ao juiz.
        data = json.loads((folder / f'{lesson}.json').read_text())
        ranged = sum(1 for u in data['unidades'] if u['inicio'] is not None)
        wrong = sum(1 for f in report['unidades'] if f['veredito'] == 'faixa-errada')
        if ranged and wrong / ranged > 0.10:
            material.append(f'faixa-errada {wrong}/{ranged}')
        reason = 'amostra' if lesson in sample else ('conferência adicional' if material or report['perecibilidade'] else None)
        if args.julgar_todas and not reason:
            reason = 'julgamento integral decidido por Will em 20/09/2026'
        if reason:
            to_judge.append(lesson)
        summary[lesson] = {'estado': 'inspecionada, fora do julgamento', 'pasta': str(folder), 'julgamento': reason,
                           'inspecao': {'material': material, 'perecibilidade': [p['numero'] for p in report['perecibilidade']], 'nao_literais': len(report['citacoes_nao_literais'])}}

    # 3. Julgamento sem fonte e até dois ciclos de correção com conferência focal.
    run('julgar', to_judge, 'claude-fable-5-1', 'xhigh', args.rotulo, entrada=folder, inspecao=folder, saida=folder, rodada=1)
    current = {lesson: folder for lesson in to_judge}
    for cycle in (1, 2):
        failing = [a for a in to_judge if verdict(current[a], a) == 'falha']
        if not failing:
            break
        previous, target = (folder if cycle == 1 else folder / 'ciclo1'), folder / f'ciclo{cycle}'
        label = f'{args.rotulo}-ciclo{cycle}'
        run('corrigir', failing, 'claude-opus-5', 'high', label, rodada=cycle, entrada=previous, julgamento=previous, saida=target)
        fixed = [a for a in failing if (target / f'{a}.json').exists() and not contract_errors(target, a, rows, tax)]
        run('inspecionar', fixed, 'claude-sonnet-5', 'xhigh', label, focal=True, entrada=target, inspecao=previous, julgamento=previous, saida=target)
        run('julgar', fixed, 'claude-fable-5-1', 'xhigh', label, entrada=target, inspecao=target, julgamento=previous, saida=target, rodada=cycle + 1)
        for lesson in failing:
            if lesson in fixed:
                current[lesson] = target
            else:
                summary[lesson].update({'estado': f'correção do ciclo {cycle} não fechou o contrato', 'pasta': str(target)})
                to_judge.remove(lesson)
    for lesson in to_judge:
        result = verdict(current[lesson], lesson)
        cycles = 0 if current[lesson] == folder else int(current[lesson].name[-1])
        state = {'passa': 'aprovada', 'falha': 'reprovada depois do teto de dois ciclos: pendente para Will', 'bloqueado': 'bloqueada pelo juiz: pendente para Will', None: 'julgamento falhou'}[result]
        summary[lesson].update({'estado': state, 'pasta': str(current[lesson]), 'ciclos': cycles})
    (folder / f'resumo-{args.rotulo}.json').write_text(base.dump(summary))
    print(base.dump(summary))


if __name__ == '__main__':
    sys.exit(main())
