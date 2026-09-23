#!/usr/bin/env python3
"""Mede o fechamento de um lote do Hardcopy Pro: linhas da tabela, falhas da 1a rodada, faixas e projeção.

Uso: fechamento.py <pasta-do-lote> <rotulo> [aulas do piloto já publicadas e fora do que falta...]
"""
import collections
import glob
import json
import os
import statistics as st
import sys
from pathlib import Path

sys.path.insert(0, '/Users/wilianrafaelribeiro/cursos/processamento')
os.environ['CURSO'] = 'hardcopy-pro'
import base_fcc as base  # noqa: E402

folder, label = Path(sys.argv[1]), sys.argv[2]
words = {r[0]['aula']: r[0]['palavras_transcricao'] for r in base.inventory()}
res = json.load(open(folder / f'resumo-{label}.json'))
fmt = lambda n: f'{n:,}'.replace(',', '.')
band = lambda w: '<500' if w < 500 else '500-999' if w < 1000 else '>=1000'

print('## LINHAS')
per = {}
fail_vetos = collections.Counter()
n_fail = n_falhas = n_alt = 0
nl = 0
for a in sorted(res):
    v = res[a]
    ex = json.load(open(folder / f'{a}.extrator.execucao.json'))
    errs = (ex.get('validador') or {}).get('erros', [])
    I = json.load(open(folder / f'{a}.inspecao.json'))
    nl += len(I['citacoes_nao_literais'])
    ap = collections.defaultdict(list)
    for f in I['unidades']:
        if f['veredito'] != 'lastreada':
            ap[f['veredito']].append(f'U{f["numero"]}')
    om = collections.Counter(o['gravidade'] for o in I['omissoes'])
    j = json.load(open(folder / f'{a}.julgamento.json'))
    final_dir = Path(v['pasta'])
    final = json.load(open(final_dir / f'{a}.json'))
    insp = ', '.join([f'{len(u)} {k} ({", ".join(u)})' for k, u in ap.items()]
                     + [f'{n} omissão {g}' for g, n in om.items()]
                     + ([f'{len(I["perecibilidade"])} perecível'] if I['perecibilidade'] else [])) or 'sem apontamento'
    if j['veredito'] == 'passa':
        jul = '**passa** de primeira'
    else:
        n_fail += 1
        n_falhas += len(j['falhas'])
        for x in j['vetos']:
            fail_vetos[x] += 1
        jul = f'{j["veredito"]} ({", ".join(j["vetos"])}) → {v["estado"]}'
    alt = []
    for c in final.get('correcoes', []):
        if c.get('ciclo', 0) >= 1:
            alt += [f'U{n}' for n in c.get('unidades', [])]
    n_alt += len(alt)
    rep = 'reparo de contrato' if errs else ''
    cor = ' + '.join(x for x in [rep, (f'ciclo {v.get("ciclos")} ({", ".join(alt)}), focal' if v.get('ciclos') else '')] if x) or 'n/a'
    errtxt = f'{len(errs)} erro: ' + '; '.join(e.split(': ', 1)[1] for e in errs) if errs else 'limpa'
    print(f'| `{a}` | {fmt(words[a])} | {len(final["unidades"])} | {errtxt} | integral, {insp} | {jul} | {cor} | {v["estado"]} |')
    s = collections.Counter()
    for sub, tag in (('.', 'p1'), ('ciclo1', 'c1'), ('ciclo2', 'c2')):
        for p in glob.glob(str(folder / sub / f'{a}.*.execucao.json')):
            r = json.load(open(p))
            if r.get('agregado_de_blocos'):
                continue
            s[f'{tag}_{r["modelo_pedido"].split("-")[1]}'] += r['consumo']['output_tokens']
    s['unidades'] = len(final['unidades'])
    s['think_extrator'] = ex.get('thinking_tokens') or 0
    per[a] = dict(s)

print('\n## RESUMO')
print('aulas', len(res), 'estados', dict(collections.Counter(v['estado'] for v in res.values())), 'reprovadas r1', n_fail, 'falhas', n_falhas, 'vetos', dict(fail_vetos), 'unidades alteradas', n_alt, 'nao literais', nl)
print('unidades finais', sum(p['unidades'] for p in per.values()), 'palavras', sum(words[a] for a in per), 'extrator sem raciocinio', [a for a, p in per.items() if not p['think_extrator']])

print('\n## FALHAS R1')
for a in sorted(res):
    j = json.load(open(folder / f'{a}.julgamento.json'))
    for f in j['falhas']:
        print(a, f['unidades'], f['veto'], '|', (f.get('mudanca_minima') or '')[:170].replace('\n', ' '))

print('\n## FAIXAS p1 (saida)')
groups = collections.defaultdict(list)
for a, p in per.items():
    groups[band(words[a])].append(p)
for b, v in groups.items():
    print(b, len(v), 'sonnet', round(st.mean(p.get('p1_sonnet', 0) for p in v)), 'fable', round(st.mean(p.get('p1_fable', 0) for p in v)), 'unid/aula', round(st.mean(p['unidades'] for p in v), 1))
cyc = [p for p in per.values() if 'c1_opus' in p]
if cyc:
    print('ciclo1 médio opus/sonnet/fable', round(st.mean(p['c1_opus'] for p in cyc)), round(st.mean(p.get('c1_sonnet', 0) for p in cyc)), round(st.mean(p.get('c1_fable', 0) for p in cyc)), 'n', len(cyc))
tot_s = sum(p.get('p1_sonnet', 0) for p in per.values())
tot_f = sum(p.get('p1_fable', 0) for p in per.values())
print('p1 total sonnet', tot_s, 'fable', tot_f, 'por unidade sonnet', round(tot_s / sum(p['unidades'] for p in per.values())), 'fable', round(tot_f / sum(p['unidades'] for p in per.values())))

print('\n## FALTA')
done = {p.stem for p in (base.KNOW / 'dados').glob('G*.json')} | set(sys.argv[3:])
rem = collections.Counter(band(w) for a, w in words.items() if a not in done)
print('faltam', sum(rem.values()), dict(rem), 'palavras', sum(w for a, w in words.items() if a not in done))
