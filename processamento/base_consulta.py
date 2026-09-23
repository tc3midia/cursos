#!/usr/bin/env python3
"""Validação e geração determinística das duas bases Águia Spread (stdlib)."""
import argparse
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import quote, unquote

ROOT = Path(__file__).resolve().parents[1]
BASE = '42c88f61e5fe385bc2d190cc9a9c853addf3e653'  # fontes lidas em 2130e27; 42c88f6 só moveu as aulas para transcricoes/ (22/09/2026)
COURSES = {'mac-3': 15, 'analises-extraordinarias': 16}
TYPES = set('conceito regra regua procedimento decisao exemplo alerta-ui limite'.split())
THEMES = set('fundamentos gestao-de-risco alavancagem entradas-e-saidas indicadores suporte-e-resistencia planejamento gestao-emocional plataformas ecossistema'.split())
TASKS = set('compreender-metodo dimensionar-exposicao gerenciar-risco avaliar-entrada avaliar-saida interpretar-indicadores identificar-niveis planejar-operacao configurar-plataforma acompanhar-operacao gerenciar-emocoes localizar-recursos'.split())
PLATFORMS = {'geral', 'okx', 'tradingview', 'binance', 'outra'}
SAMPLES = {'mac-3': ['M01_A07', 'M02_A06', 'M04_A02'], 'analises-extraordinarias': ['M02_A02', 'M03_A05', 'M04_A01']}
STAMP = re.compile(r'\*\*\[(\d\d:\d\d:\d\d)[–-](\d\d:\d\d:\d\d)\]\*\*')

def sha(data):
    return hashlib.sha256(data).hexdigest()

def norm(text):
    return ' '.join(text.split())

def seconds(value):
    h, m, s = map(int, value.split(':'))
    return 3600*h + 60*m + s

def timestamp(value):
    value = int(value)
    return f'{value//3600:02}:{value%3600//60:02}:{value%60:02}'

def dump(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + '\n'

def inventory(course):
    rows = []
    for source in sorted((ROOT/course/'transcricoes').glob('Módulo */*.md')):
        text = source.read_text()
        lesson = re.match(r'M\d\d_A\d\d', source.stem).group()
        spans = list(STAMP.finditer(text))
        segments = [(seconds(m[1]), seconds(m[2]), text[m.end():spans[i+1].start() if i+1 < len(spans) else len(text)]) for i,m in enumerate(spans)]
        if not segments:
            raise ValueError(f'Fonte sem timestamps: {source}')
        row = {'curso': course, 'aula': lesson, 'aula_id': sha(f'{course}/{lesson}'.encode())[:16], 'titulo': text.splitlines()[0].removeprefix('# '), 'fonte': source.relative_to(ROOT).as_posix(), 'fonte_repo': 'tc3midia/cursos', 'fonte_commit': BASE, 'sha256': sha(source.read_bytes()), 'fim_segundos': max(s[1] for s in segments), 'escala_timestamps': 'gravacao-local-2x'}
        rows.append((row, text, segments))
    return rows

def validate_lesson(course, row, text, segments, data):
    errors = []
    source_text = norm(text)
    def require(ok, message):
        if not ok:
            errors.append(f'{course}/{row["aula"]}: {message}')
    for field, expected in [('curso', course), ('aula', row['aula']), ('titulo', row['titulo'])]:
        require(data.get(field) == expected, f'{field} diferente da fonte')
    context = data.get('contexto', [])
    require(isinstance(context, list) and 3 <= len(context) <= 8 and all(isinstance(x,str) and x.strip() for x in context), 'contexto exige 3–8 frases')
    units = data.get('unidades', [])
    require(isinstance(units, list) and len(units) > 0, 'unidades ausentes')
    previous = -1
    for n,u in enumerate(units, 1):
        tag = f'U{n:03}'
        fields = {'numero','titulo','tipo','tema','tarefas','plataformas','inicio','fim','condicoes','perecivel','confianca','nota','corpo','evidencia','versao'}
        require(fields <= u.keys(), f'{tag}: campos ausentes {sorted(fields-u.keys())}')
        require(u.get('numero') == n, f'{tag}: numero fora da sequência')
        require(isinstance(u.get('titulo'),str) and 1 <= len(u['titulo']) <= 100, f'{tag}: título inválido')
        require(u.get('tipo') in TYPES, f'{tag}: tipo inválido')
        require(u.get('tema') in THEMES, f'{tag}: tema inválido')
        require(isinstance(u.get('tarefas'),list) and set(u['tarefas']) <= TASKS, f'{tag}: tarefas inválidas')
        require(isinstance(u.get('plataformas'),list) and bool(u['plataformas']) and set(u['plataformas']) <= PLATFORMS, f'{tag}: plataformas inválidas')
        require(type(u.get('perecivel')) is bool, f'{tag}: perecivel não booleano')
        require(u.get('tipo') != 'alerta-ui' or u.get('perecivel') is True, f'{tag}: tela não perecível')
        require(u.get('confianca') in {'alta','media','baixa'}, f'{tag}: confiança inválida')
        require(u.get('confianca') != 'baixa' or bool(u.get('nota')), f'{tag}: baixa confiança sem nota')
        require(type(u.get('versao')) is int and u['versao'] >= 1, f'{tag}: versão inválida')
        for optional in ['condicoes','nota']:
            require(u.get(optional) is None or isinstance(u.get(optional),str), f'{tag}: {optional} inválida')
        body = u.get('corpo','')
        require(isinstance(body,str) and len(body.strip()) > 15, f'{tag}: corpo vazio/insuficiente')
        evidence = u.get('evidencia','')
        require(isinstance(evidence,str) and 1 <= len(evidence.split()) <= 24, f'{tag}: evidência exige 1–24 palavras')
        require(bool(evidence) and norm(evidence) in source_text, f'{tag}: evidência não literal na fonte')
        start,end = u.get('inicio'),u.get('fim')
        valid_time = type(start) in (int,float) and type(end) in (int,float) and 0 <= start < end <= row['fim_segundos']+1
        require(valid_time, f'{tag}: faixa inválida {start}–{end}')
        if valid_time:
            require(start >= previous, f'{tag}: sequência fora da ordem da fonte')
            previous = start
            window = ' '.join(s[2] for s in segments if s[0] < end and s[1] > start)
            require(bool(evidence) and norm(evidence) in norm(window), f'{tag}: evidência fora da faixa')
        words = norm(body).split()
        require(not any(' '.join(words[i:i+25]) in source_text for i in range(max(0,len(words)-24))), f'{tag}: cópia de 25 palavras no corpo')
    return errors

def review_errors(course,row,data_path):
    p=ROOT/course/'processamento/revisao/inspecao'/f'{row["aula"]}.json'
    if not p.exists():
        return [f'{course}/{row["aula"]}: inspeção ausente']
    review=json.loads(p.read_text())
    errors=[]
    if review.get('arquivo_sha256') != sha(data_path.read_bytes()):
        errors.append(f'{course}/{row["aula"]}: inspeção desatualizada')
    if review.get('veredito') != 'passa':
        errors.append(f'{course}/{row["aula"]}: inspeção não aprovada')
    units=json.loads(data_path.read_text())['unidades']
    if sorted(review.get('unidades_verificadas',[])) != list(range(1,len(units)+1)):
        errors.append(f'{course}/{row["aula"]}: cobertura incompleta da inspeção')
    if row['aula'] in SAMPLES[course]:
        judgment=ROOT/course/'processamento/revisao/julgamento'/f'{row["aula"]}.json'
        if not judgment.exists():
            errors.append(f'{course}/{row["aula"]}: julgamento da amostra ausente')
        else:
            result=json.loads(judgment.read_text())
            if result.get('arquivo_sha256') != sha(data_path.read_bytes()) or result.get('inspecao_sha256') != sha(p.read_bytes()):
                errors.append(f'{course}/{row["aula"]}: julgamento desatualizado')
            if result.get('veredito') != 'passa':
                errors.append(f'{course}/{row["aula"]}: julgamento não aprovado')
    return errors

def unit_id(row,u):
    return f'U:{row["aula_id"]}:{u["numero"]:03}'

def unit_md(row,u):
    uid=unit_id(row,u)
    anchor=uid.lower().replace(':','-')
    lines=[f'<a id="{anchor}"></a>', '', f'### {uid} — {u["titulo"]}', '', f'- Tipo: `{u["tipo"]}` · Tema: `{u["tema"]}`', f'- Tarefas: {", ".join(u["tarefas"]) or "sem tarefa operacional"}', f'- Plataformas: {", ".join(u["plataformas"])}', f'- Faixa: `{timestamp(u["inicio"])}–{timestamp(u["fim"])}` · Perecível: {"sim" if u["perecivel"] else "não"}', f'- Confiança na interpretação: {u["confianca"]} · Versão: {u["versao"]}']
    if u.get('condicoes'):
        lines.append(f'- Condições: {u["condicoes"]}')
    if u.get('nota'):
        lines.append(f'- Nota: {u["nota"]}')
    lines += ['',u['corpo'],'',f'> Âncora textual: “{u["evidencia"]}”','']
    return '\n'.join(lines)

def generated(course, allow_partial=False):
    rows=inventory(course)
    outputs={}
    manifest=[r[0] for r in rows]
    outputs[f'{course}/conhecimento/manifest.json']=dump({'fonte_commit':BASE,'aulas':manifest})
    entries=[]
    by_theme=defaultdict(list)
    flattened=[]
    for row,text,segments in rows:
        p=ROOT/course/'conhecimento/dados'/f'{row["aula"]}.json'
        if not p.exists():
            if allow_partial:
                continue
            raise ValueError(f'Aula ausente: {p}')
        data=json.loads(p.read_text())
        errors=validate_lesson(course,row,text,segments,data)
        if errors:
            raise ValueError('\n'.join(errors))
        entries.append((row,data))
        src=quote('../../'+row['fonte'].split('/',1)[1],safe='/')
        lines=[f'# {row["titulo"]}', '', f'Aula `{row["aula"]}` · Curso `{course}` · {len(data["unidades"])} unidades.', '', '## Contexto da aula', '', *data['contexto'], '', '## Fonte e limites', '', f'[Transcrição original]({src}) · Commit `{BASE}` · SHA-256 `{row["sha256"]}`.', '', 'Tempos da gravação local em 2×. O texto abaixo registra ensinamentos e afirmações do instrutor; confiança mede fidelidade de interpretação. Não comprova rentabilidade nem atualidade de telas e serviços. Alcance da revisão em [processamento](../../processamento/README.md).', '', '## Unidades', '']
        for u in data['unidades']:
            lines.append(unit_md(row,u))
            by_theme[u['tema']].append((row,u))
            flattened.append({'id':unit_id(row,u),'aula':row['aula'],**u,'hash':sha(dump(u).encode())})
        outputs[f'{course}/conhecimento/unidades/{row["aula"]}.md']='\n'.join(lines)+'\n'
    index=[f'# Base de conhecimento: {course}', '', f'{len(entries)}/{len(rows)} aulas · {len(flattened)} unidades · {len(by_theme)} temas.', '', 'Base de consulta das transcrições. Índices por tema agrupam unidades, sem resolver divergências entre aulas e sem criar recomendações financeiras novas.', '', '## Aulas', '', '| Aula | Título | Unidades |', '|---|---|---:|']
    for row,data in entries:
        index.append(f'| {row["aula"]} | [{row["titulo"]}](unidades/{row["aula"]}.md) | {len(data["unidades"])} |')
    index += ['', '## Temas', '']
    for theme,units in sorted(by_theme.items()):
        index.append(f'- [{theme}](temas/{theme}.md): {len(units)} unidades.')
        page=[f'# {theme}', '', 'Índice de unidades, sem síntese nova. Cada link abre a aula com a faixa e a fonte.', '']
        for row,u in units:
            uid=unit_id(row,u)
            anchor=uid.lower().replace(':','-')
            page.append(f'- [{row["aula"]}: {u["titulo"]}](../unidades/{row["aula"]}.md#{anchor}) · `{uid}` · {u["tipo"]}')
        outputs[f'{course}/conhecimento/temas/{theme}.md']='\n'.join(page)+'\n'
    index += ['', '## Contrato, fonte e revisão', '', '- [Manifesto e hashes](manifest.json)', '- [Método e alcance da revisão](../processamento/README.md)', '- [Contrato de dados](../../processamento/CONTRATO.md)', '- [Dados estruturados](dados/)', '']
    outputs[f'{course}/conhecimento/README.md']='\n'.join(index)
    outputs[f'{course}/conhecimento/unidades.jsonl']=''.join(json.dumps(r,ensure_ascii=False,sort_keys=True)+'\n' for r in flattened)
    return {name: content.rstrip()+'\n' for name,content in outputs.items()}

def check_links(outputs):
    errors=[]
    known=set(outputs)
    for name,content in outputs.items():
        if not name.endswith('.md'):
            continue
        for link in re.findall(r'\]\(([^)]+)\)',content):
            if '://' in link or link.startswith('#'):
                continue
            target=(ROOT/name).parent/unquote(link.split('#')[0])
            relative=target.resolve().relative_to(ROOT).as_posix()
            if not target.exists() and relative not in known:
                errors.append(f'{name}: link ausente {link}')
            elif '#' in link:
                anchor=link.split('#',1)[1]
                content_target=outputs.get(relative) if relative in outputs else target.read_text()
                if f'id="{anchor}"' not in content_target:
                    errors.append(f'{name}: âncora ausente {link}')
    return errors

def patch(outputs):
    result=['*** Begin Patch']
    for name,content in outputs.items():
        p=ROOT/name
        if p.exists() and p.read_text()==content:
            continue
        if p.exists():
            result += [f'*** Update File: {p}', '@@', *('-'+line for line in p.read_text().splitlines()), *('+'+line for line in content.splitlines())]
        else:
            result += [f'*** Add File: {p}', *('+'+line for line in content.splitlines())]
    result.append('*** End Patch')
    return '\n'.join(result)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--course',choices=COURSES,required=True)
    parser.add_argument('--partial',action='store_true')
    parser.add_argument('--reviews',action='store_true')
    parser.add_argument('--check',action='store_true')
    parser.add_argument('--patch',action='store_true')
    parser.add_argument('--only',help='emitir apenas um caminho gerado')
    args=parser.parse_args()
    errors=[]
    rows=inventory(args.course)
    if len(rows)!=COURSES[args.course]:
        errors.append('Contagem de fontes divergente')
    data_files=set((ROOT/args.course/'conhecimento/dados').glob('*.json'))
    expected={ROOT/args.course/'conhecimento/dados'/f'{r[0]["aula"]}.json' for r in rows}
    if data_files-expected:
        errors.append('Dados com aula sem fonte')
    for row,text,segments in rows:
        p=ROOT/args.course/'conhecimento/dados'/f'{row["aula"]}.json'
        if p.exists():
            try:
                data=json.loads(p.read_text())
                errors.extend(validate_lesson(args.course,row,text,segments,data))
                if args.reviews:
                    errors.extend(review_errors(args.course,row,p))
            except (ValueError,TypeError,KeyError) as e:
                errors.append(f'{p.name}: {e}')
        elif not args.partial:
            errors.append(f'{row["aula"]}: dados ausentes')
    if errors:
        print(dump({'erros':errors}))
        return 1
    outputs=generated(args.course,args.partial)
    if args.patch:
        if args.only:
            outputs={args.only:outputs[args.only]}
        print(patch(outputs))
        return 0
    if args.check:
        errors.extend(check_links(outputs))
        errors.extend(f'Gerado divergente/ausente: {name}' for name,content in outputs.items() if not (ROOT/name).exists() or (ROOT/name).read_text()!=content)
    print(dump({'curso':args.course,'aulas_fontes':len(rows),'aulas_extraidas':len(data_files),'arquivos_gerados':len(outputs),'erros':errors}))
    return bool(errors)

if __name__=='__main__':
    sys.exit(main())
