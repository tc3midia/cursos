#!/usr/bin/env python3
"""Soma o consumo em tokens dos .execucao.json de uma ou mais pastas, por papel e por modelo.

Uso: consumo.py <pasta> [<pasta> ...] [--aulas G01_A01 ...]
Registro com agregado_de_blocos: true fica fora da soma (os blocos já estão contados).
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

args = sys.argv[1:]
lessons = None
if '--aulas' in args:
    i = args.index('--aulas')
    lessons = set(args[i + 1:])
    args = args[:i]

ROLE = {'extrator': 'Extrator', 'inspetor': 'Inspetor', 'juiz': 'Juiz'}
by_role = defaultdict(lambda: defaultdict(int))
by_model = defaultdict(lambda: defaultdict(int))
stops = defaultdict(int)
waits = 0
errors = []
for folder in args:
    for path in sorted(Path(folder).glob('*.execucao.json')):
        r = json.loads(path.read_text())
        if lessons and r.get('aula') not in lessons:
            continue
        if r.get('agregado_de_blocos'):
            continue
        role = r['papel']
        if role == 'redator':
            role = 'Reparo de contrato' if '.ciclo0.' in path.name or r['modelo_pedido'] == 'claude-sonnet-5' else 'Redator'
        else:
            role = ROLE.get(role, role)
        model = '/'.join(r.get('modelos_usados') or []) or r['modelo_pedido']
        key = (role, model, r['esforco'])
        c = r['consumo']
        new = (c.get('input_tokens') or 0) + (c.get('cache_creation_input_tokens') or 0)
        for target in (by_role[key], by_model[model]):
            target['chamadas'] += 1
            target['entrada_nova'] += new
            target['cache_lido'] += c.get('cache_read_input_tokens') or 0
            target['saida'] += c.get('output_tokens') or 0
            target['raciocinio'] += r.get('thinking_tokens') or 0
            target['s'] += round((r.get('duracao_ms') or 0) / 1000)
        stops[(r.get('stop_reason'), r.get('terminal_reason'))] += 1
        waits += len(r.get('esperas_por_limite') or [])
        if r.get('is_error'):
            errors.append(path.name)

fmt = lambda n: f'{n:,}'.replace(',', '.')
print('| Papel | Modelo e esforço | Chamadas | Entrada nova | Cache lido | Saída | Raciocínio, dentro da saída | Tempo |')
print('|---|---|---:|---:|---:|---:|---:|---:|')
order = ['Extrator', 'Reparo de contrato', 'Inspetor', 'Redator', 'Juiz']
for key in sorted(by_role, key=lambda k: order.index(k[0]) if k[0] in order else 9):
    v = by_role[key]
    print(f'| {key[0]} | `{key[1]}` `{key[2]}` | {v["chamadas"]} | {fmt(v["entrada_nova"])} | {fmt(v["cache_lido"])} | {fmt(v["saida"])} | {fmt(v["raciocinio"])} | {fmt(v["s"])} s |')
print()
for model, v in sorted(by_model.items()):
    print(f'{model}: chamadas {v["chamadas"]}, entrada nova {fmt(v["entrada_nova"])}, cache lido {fmt(v["cache_lido"])}, saída {fmt(v["saida"])}')
print('stop/terminal:', dict(stops), '| esperas por limite:', waits, '| erros:', errors)
