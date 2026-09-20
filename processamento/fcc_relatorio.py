#!/usr/bin/env python3
"""Resume execuções, inspeções e julgamentos de uma ou mais pastas de trabalho da base FCC (stdlib)."""
import json
import sys
from collections import Counter
from pathlib import Path


def load(path):
    return json.loads(path.read_text()) if path.exists() else None


def summarize(folder):
    rows = []
    for data_path in sorted(p for p in folder.glob('M??_A??.json')):
        lesson = data_path.stem
        data = load(data_path)
        line = {'pasta': folder.name, 'aula': lesson, 'unidades': len(data['unidades']), 'tipos': dict(Counter(u['tipo'] for u in data['unidades']))}
        consumo = Counter()
        for record_path in sorted(folder.glob(f'{lesson}.*.execucao.json')):
            record = load(record_path)
            role = record['papel']
            line[role] = {'modelo': '/'.join(record['modelos_usados']) or record['modelo_pedido'], 'esforco': record['esforco'], **record['consumo'],
                          'thinking': record.get('thinking_tokens'), 'stop': record['stop_reason'], 'termino': record['terminal_reason'],
                          'erro': record.get('is_error'), 's': round((record.get('duracao_ms') or 0) / 1000), 'usd_nominal': round(record.get('custo_nominal_usd') or 0, 3)}
            if role == 'extrator':
                line['erros_contrato'] = (record.get('validador') or {}).get('erros', [])
            consumo['usd_nominal'] += record.get('custo_nominal_usd') or 0
            consumo['saida'] += record['consumo'].get('output_tokens') or 0
        inspection = load(folder / f'{lesson}.inspecao.json')
        if inspection:
            findings = Counter((f['veredito'], f['gravidade']) for f in inspection['unidades'] if f['veredito'] != 'lastreada' or f['gravidade'] != 'nenhuma')
            line['inspecao'] = {'cobriu_todas': inspection['unidades_verificadas'] == sorted(inspection['unidades_no_arquivo']),
                                'apontamentos': {f'{v}/{g}': n for (v, g), n in findings.items()},
                                'omissoes': dict(Counter(o['gravidade'] for o in inspection['omissoes'])), 'perecibilidade': len(inspection['perecibilidade']),
                                'citacoes_nao_literais': len(inspection['citacoes_nao_literais'])}
        judgment = load(folder / f'{lesson}.julgamento.json')
        if judgment:
            line['julgamento'] = {'veredito': judgment['veredito'], 'vetos': judgment['vetos'], 'falhas': len(judgment['falhas']), 'ajustes_menores': len(judgment['ajustes_menores'])}
        line['total'] = {'usd_nominal': round(consumo['usd_nominal'], 3), 'tokens_saida': consumo['saida']}
        rows.append(line)
    return rows


if __name__ == '__main__':
    for name in sys.argv[1:]:
        for row in summarize(Path(name)):
            print(json.dumps(row, ensure_ascii=False))
