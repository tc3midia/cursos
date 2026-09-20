#!/usr/bin/env python3
"""Promove aulas conferidas de uma pasta de trabalho para a base FCC (stdlib).

Só publica aula com zero erros de contrato, inspeção do mesmo arquivo e, se estiver na amostra,
julgamento `passa` do mesmo arquivo e da mesma inspeção. Não chama modelo.
"""
import argparse
import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import base_fcc as base  # noqa: E402


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pasta', type=Path, required=True)
    parser.add_argument('--rotulo', required=True)
    parser.add_argument('--aulas', nargs='+', required=True)
    parser.add_argument('--execucoes', type=Path, nargs='*', default=[], help='pastas extras com .execucao.json da mesma aula (ciclos anteriores)')
    args = parser.parse_args()
    tax = base.taxonomy()
    rows = {r[0]['aula']: r for r in base.inventory()}
    sample = json.loads((base.PROC / 'amostra.json').read_text())
    problems, plan = [], []
    for lesson in args.aulas:
        data_path = args.pasta / f'{lesson}.json'
        inspection = args.pasta / f'{lesson}.inspecao.json'
        judgment = args.pasta / f'{lesson}.julgamento.json'
        row, text, segments, material = rows[lesson]
        errors, _ = base.validate_lesson(row, text, segments, material, json.loads(data_path.read_text()), tax)
        digest = base.sha(data_path.read_bytes())
        if errors:
            problems.append(f'{lesson}: {len(errors)} erros de contrato')
        if not inspection.exists() or json.loads(inspection.read_text())['arquivo_sha256'] != digest:
            problems.append(f'{lesson}: inspeção ausente ou de outra versão do arquivo')
        if lesson in sample['aulas'] or judgment.exists():
            verdict = json.loads(judgment.read_text()) if judgment.exists() else {}
            if verdict.get('arquivo_sha256') != digest or verdict.get('inspecao_sha256') != base.sha(inspection.read_bytes()):
                problems.append(f'{lesson}: julgamento ausente ou desatualizado')
            elif verdict.get('veredito') != 'passa':
                problems.append(f'{lesson}: julgamento {verdict.get("veredito")}')
        plan.append((lesson, data_path, inspection, judgment))
    if problems:
        print(base.dump({'publicado': [], 'recusado': problems}))
        return 1
    for lesson, data_path, inspection, judgment in plan:
        shutil.copy(data_path, base.KNOW / 'dados' / f'{lesson}.json')
        for source, folder in ((inspection, 'inspecao'), (judgment, 'julgamento')):
            if source.exists():
                target = base.PROC / 'revisao' / folder / f'{lesson}.json'
                target.parent.mkdir(parents=True, exist_ok=True)
                if folder == 'julgamento' and lesson in sample['ouro']:
                    # O selo de ouro não muda o parecer: inspecao_sha256 e arquivo_sha256 continuam os do juiz.
                    target.write_text(base.dump({**json.loads(source.read_text()), 'ouro': True}))
                else:
                    shutil.copy(source, target)
        records = base.PROC / 'execucoes' / args.rotulo
        records.mkdir(parents=True, exist_ok=True)
        for folder in [args.pasta, *args.execucoes]:
            for record in folder.glob(f'{lesson}.*.execucao.json'):
                # O nome guarda a pasta de origem: ciclos diferentes da mesma aula não se sobrescrevem.
                origin = folder.resolve().relative_to(base.PROC.resolve()).as_posix().replace('/', '.')
                shutil.copy(record, records / f'{origin}.{record.name}')
    print(base.dump({'publicado': [p[0] for p in plan], 'recusado': []}))
    return 0


if __name__ == '__main__':
    sys.exit(main())
