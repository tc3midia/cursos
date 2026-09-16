#!/usr/bin/env python3
"""Validador dos arquivos de unidades (FORMATO.md §1–§4). Stdlib only.

    python3 processamento/scripts/validate_unidades.py [--root DIR] [--modulo 001 | --arquivo slug] [--json] [--sem-fontes]

Exit 1 se houver erro. Warnings não falham.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import unidades as lib  # noqa: E402

MIN_UNIDADES = 3
DENSIDADE = (3, 60)
SHINGLE = 25

CAMPOS_OBRIGATORIOS = ("type", "status", "title", "modulo", "ordem", "aula_id", "account_id", "promoted_by", "fonte_repo", "fonte_commit", "fontes", "extraido_em", "gerado_por", "retiradas", "divisoes", "fusoes")
META_OBRIGATORIA = ("tipo", "plataforma", "tema", "tarefas", "fonte", "perecivel", "confianca", "versao")
META_PERMITIDA = set(lib.ORDEM_META)
RE_NUMERO = re.compile(r"(\d|R\$|%|\bx\b|\bvezes\b|\bdias?\b|\bhoras?\b|\bsemanas?\b|\bmeses\b|\bminutos?\b)")
NUMERAIS_POR_EXTENSO = (
    "um", "uma", "dois", "duas", "três", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez",
    "onze", "doze", "treze", "catorze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte",
    "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa", "cem", "mil", "metade", "dobro", "triplo",
)
RE_NUMERAL_EXTENSO = re.compile(r"\b(" + "|".join(NUMERAIS_POR_EXTENSO) + r")\b", re.I)


RE_TELA = re.compile(
    r"(\b(abra|abrir|acesse|acessar|v[aá]|entre|entrar) (a|o|na|no|em|até) (aba|menu|painel|guia|se[cç][aã]o|tela)\b"
    r"|\b(na|no|da|do|pela|pelo) (aba|menu|guia) [A-ZÀ-Ú\"“«]|\bbot[aã]o [A-ZÀ-Ú\"“«]|\bpasse o mouse\b|\bcaminho de clique\b)",
    re.I,
)
TIPOS_TELA = {"procedimento", "regra", "decisao", "regua", "fato-material", "alerta-ui"}


def descreve_tela(texto: str) -> bool:
    """Corpo com caminho de tela (abra a aba, no menu X, botão X, passe o mouse): descrição de interface, perecível por definição.
    Menção a clique como métrica ou a clicar como ação do usuário não conta."""
    return bool(RE_TELA.search(texto))


def tem_numero(texto: str) -> bool:
    """Régua precisa de número: dígito, unidade ou numeral por extenso da lista fechada."""
    return bool(RE_NUMERO.search(texto) or RE_NUMERAL_EXTENSO.search(texto))


def _shingles(texto: str) -> set[str]:
    palavras = re.findall(r"\w+", texto.lower())
    return {" ".join(palavras[i : i + SHINGLE]) for i in range(0, max(0, len(palavras) - SHINGLE + 1))}


def validar_texto(texto: str, *, slug: str, manifest: dict, taxonomia: lib.Taxonomia, fontes_disco: list[str], prev: dict | None = None, textos_fonte: dict[str, str] | None = None) -> tuple[list[str], list[str]]:
    """Valida um arquivo de unidades. Devolve (erros, warnings). `prev` = {id: {hash, versao}} do JSONL commitado."""
    erros: list[str] = []
    warns: list[str] = []
    arq = lib.parse_arquivo_unidades(texto)
    erros.extend(arq.erros_parse)
    f = arq.front

    for campo in CAMPOS_OBRIGATORIOS:
        if campo not in f:
            erros.append(f"front matter: campo obrigatório ausente `{campo}`")
    if erros:
        return erros, warns

    row = manifest.get(str(f.get("aula_id")))
    if row is None:
        erros.append(f"front matter: aula_id `{f.get('aula_id')}` não está no manifest")
        return erros, warns
    if row["slug"] != slug:
        erros.append(f"front matter: aula_id `{f['aula_id']}` corresponde ao slug `{row['slug']}`, arquivo é `{slug}`")
    if f["type"] != "unidades-aula":
        erros.append("front matter: type deve ser `unidades-aula`")
    if f["status"] not in lib.STATUS_UNIDADES:
        erros.append(f"front matter: status `{f['status']}` inválido")
    if str(f["title"]) != row["aula"]:
        erros.append(f"front matter: title `{f['title']}` difere do manifest `{row['aula']}`")
    if str(f["modulo"]) != row["modulo3"]:
        erros.append(f"front matter: modulo `{f['modulo']}` difere do manifest `{row['modulo3']}`")
    if f["ordem"] != row["ordem"]:
        erros.append(f"front matter: ordem `{f['ordem']}` difere do manifest `{row['ordem']}`")
    if f["account_id"] != lib.ACCOUNT_ID:
        erros.append(f"front matter: account_id deve ser `{lib.ACCOUNT_ID}`")
    if f["promoted_by"] != lib.PROMOTED_BY:
        erros.append(f"front matter: promoted_by deve ser `{lib.PROMOTED_BY}`")
    if f["fonte_repo"] != lib.FONTE_REPO:
        erros.append("front matter: fonte_repo inválido")
    if str(f["fonte_commit"]) != lib.FONTE_COMMIT:
        erros.append(f"front matter: fonte_commit deve ser `{lib.FONTE_COMMIT}`")
    if f["gerado_por"] not in lib.GERADO_POR:
        erros.append(f"front matter: gerado_por `{f['gerado_por']}` inválido")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(f["extraido_em"])):
        erros.append("front matter: extraido_em deve ser YYYY-MM-DD")
    fontes = f["fontes"] if isinstance(f["fontes"], list) else [f["fontes"]]
    if "transcricao.md" not in fontes:
        erros.append("front matter: fontes deve conter transcricao.md")
    for nome in fontes:
        if nome not in fontes_disco:
            erros.append(f"front matter: fonte `{nome}` não existe na pasta da aula")
    ignoradas = {}
    for item in f.get("fontes_ignoradas") or []:
        if isinstance(item, str) and ":" in item:
            k, v = item.split(":", 1)
            ignoradas[k.strip()] = v.strip()
    for nome in fontes_disco:
        if nome != "transcricao.md" and nome not in fontes and nome not in ignoradas:
            erros.append(f"front matter: `{nome}` está no disco e não aparece em fontes nem em fontes_ignoradas")
    for nome in ignoradas:
        warns.append(f"fonte ignorada: {nome} ({ignoradas[nome]})")
    for campo in ("retiradas", "divisoes", "fusoes"):
        if not isinstance(f[campo], list):
            erros.append(f"front matter: `{campo}` deve ser lista")
    retiradas = [str(x) for x in (f["retiradas"] if isinstance(f["retiradas"], list) else [])]
    for rid in retiradas:
        m = lib.RE_ID_FULL.match(rid)
        if not m or m.group(1) != f["aula_id"]:
            erros.append(f"retiradas: `{rid}` não é ID desta aula")

    if not (3 <= len(arq.contexto) <= 8):
        erros.append(f"Contexto da aula: {len(arq.contexto)} linhas (esperado 3–8)")
    for l in arq.contexto:
        if lib.RE_TIMESTAMP.search(l):
            erros.append("Contexto da aula: timestamp no texto")
        if "[[" in l:
            erros.append("Contexto da aula: `[[` no texto")
        if lib.RE_HOJE.search(l):
            erros.append("Contexto da aula: 'hoje/atualmente' no texto")

    if len(arq.unidades) < MIN_UNIDADES:
        erros.append(f"mínimo de {MIN_UNIDADES} unidades; arquivo tem {len(arq.unidades)}")
    if not (DENSIDADE[0] <= len(arq.unidades) <= DENSIDADE[1]):
        warns.append(f"densidade fora de {DENSIDADE[0]}–{DENSIDADE[1]}: {len(arq.unidades)} unidades")

    duracao = float(row["duracao_segundos"])
    shingles_fonte: set[str] | None = None
    if textos_fonte:
        shingles_fonte = set()
        for t in textos_fonte.values():
            shingles_fonte |= _shingles(t)

    vistos: set[int] = set()
    for u in arq.unidades:
        pre = f"{u.id}"
        if u.aula_id != f["aula_id"]:
            erros.append(f"{pre}: ID de outra aula")
        if u.nnn in vistos:
            erros.append(f"{pre}: ID duplicado")
        vistos.add(u.nnn)
        if u.id in retiradas:
            erros.append(f"{pre}: número retirado reutilizado (está em retiradas)")
        if not (1 <= len(u.titulo) <= 80):
            erros.append(f"{pre}: título com {len(u.titulo)} caracteres (1–80)")
        m = u.meta
        for campo in META_OBRIGATORIA:
            if campo not in m:
                erros.append(f"{pre}: metadado obrigatório ausente `{campo}`")
        for campo in m:
            if campo not in META_PERMITIDA:
                erros.append(f"{pre}: metadado desconhecido `{campo}`")
        if any(c not in m for c in META_OBRIGATORIA):
            continue
        tipo = m["tipo"]
        if tipo not in taxonomia.tipos:
            erros.append(f"{pre}: tipo `{tipo}` fora da taxonomia")
        plats = m["plataforma"] if isinstance(m["plataforma"], list) else [m["plataforma"]]
        if not plats:
            erros.append(f"{pre}: plataforma vazia")
        for p in plats:
            if p not in taxonomia.plataformas:
                erros.append(f"{pre}: plataforma `{p}` fora da taxonomia")
        if isinstance(m["tema"], list) or m["tema"] not in taxonomia.temas:
            erros.append(f"{pre}: tema `{m['tema']}` fora da taxonomia (exatamente 1)")
        tarefas = m["tarefas"] if isinstance(m["tarefas"], list) else [m["tarefas"]]
        for t in tarefas:
            if t not in taxonomia.tarefas:
                erros.append(f"{pre}: tarefa `{t}` fora da taxonomia")
        if not tarefas and tipo not in lib.TIPOS_SEM_TAREFA:
            erros.append(f"{pre}: tarefas vazia só é permitida em conceito/limite (tipo `{tipo}`)")
        fonte = str(m["fonte"])
        mf = re.fullmatch(r"(fala|pdf:(.+)|txt:(.+)|fala\+pdf:(.+)|fala\+txt:(.+))", fonte)
        if not mf:
            erros.append(f"{pre}: fonte `{fonte}` inválida")
        else:
            nome = next((g for g in mf.groups()[1:] if g), None)
            if nome and nome not in fontes:
                erros.append(f"{pre}: fonte `{nome}` não está em fontes")
            if nome and nome.endswith(".pdf") and not fonte.split(":")[0].endswith("pdf"):
                erros.append(f"{pre}: `{nome}` é pdf mas fonte diz txt")
        inclui_fala = fonte.startswith("fala")
        if inclui_fala and "faixa" not in m:
            erros.append(f"{pre}: faixa obrigatória quando fonte inclui fala")
        if not inclui_fala and "faixa" in m:
            erros.append(f"{pre}: faixa proibida quando fonte é só pdf/txt")
        if "faixa" in m:
            fx = lib.parse_faixa(str(m["faixa"]))
            if fx is None:
                erros.append(f"{pre}: faixa `{m['faixa']}` fora do formato hh:mm:ss–hh:mm:ss")
            else:
                if fx[0] >= fx[1]:
                    erros.append(f"{pre}: faixa com início ≥ fim")
                if fx[1] > duracao + 2:
                    erros.append(f"{pre}: faixa termina em {fx[1]}s, além da duração {duracao:.0f}s")
        if not isinstance(m["perecivel"], bool):
            erros.append(f"{pre}: perecivel deve ser true/false")
        if tipo == "alerta-ui" and m["perecivel"] is not True:
            erros.append(f"{pre}: alerta-ui exige perecivel: true")
        if tipo in TIPOS_TELA and m["perecivel"] is not True and descreve_tela("\n".join(u.corpo)):
            erros.append(f"{pre}: descrição de tela (abra a aba, no menu X, botão X, passe o mouse) exige perecivel: true")
        if m["confianca"] not in lib.CONFIANCA:
            erros.append(f"{pre}: confianca `{m['confianca']}` inválida")
        if m["confianca"] == "baixa" and not m.get("nota"):
            erros.append(f"{pre}: confianca baixa exige nota")
        if m["confianca"] == "baixa":
            warns.append(f"{pre}: confianca baixa")
        if not isinstance(m["versao"], int) or m["versao"] < 1:
            erros.append(f"{pre}: versao deve ser inteiro ≥ 1")
        if m.get("proposta_tag"):
            warns.append(f"{pre}: proposta_tag {m['proposta_tag']}")
        if "condicoes" in m and not isinstance(m["condicoes"], str):
            erros.append(f"{pre}: condicoes deve ser string")

        corpo = u.corpo
        limite = 15 if tipo in {"procedimento", "exemplo"} else 8
        if not (1 <= len(corpo) <= limite):
            erros.append(f"{pre}: corpo com {len(corpo)} linhas (1–{limite})")
        texto_corpo = "\n".join(corpo)
        if lib.RE_TIMESTAMP.search(texto_corpo):
            erros.append(f"{pre}: timestamp no corpo")
        if "[[" in texto_corpo:
            erros.append(f"{pre}: `[[` no corpo")
        if "**[" in texto_corpo:
            erros.append(f"{pre}: marcador `**[` no corpo")
        if lib.RE_HOJE.search(texto_corpo):
            erros.append(f"{pre}: 'hoje/atualmente/neste momento' no corpo")
        if shingles_fonte is not None and _shingles(texto_corpo) & shingles_fonte:
            erros.append(f"{pre}: cópia bruta (25 palavras idênticas à fonte)")
        if tipo == "regua" and not tem_numero(texto_corpo):
            erros.append(f"{pre}: regua sem número ou unidade")
        if tipo == "procedimento":
            if not corpo or not corpo[0].startswith("Pré-condição:"):
                erros.append(f"{pre}: procedimento deve começar com `Pré-condição:`")
            if sum(1 for l in corpo if re.match(r"^\d+\. ", l)) < 2:
                erros.append(f"{pre}: procedimento exige lista numerada com ≥2 itens")
        if tipo == "decisao" and not (corpo and re.match(r"^(Se |Quando )", corpo[0])):
            erros.append(f"{pre}: decisao deve começar com `Se ` ou `Quando `")
        if tipo == "exemplo":
            for marca in ("Situação:", "O que aconteceu:", "Lógica:"):
                if marca not in texto_corpo:
                    erros.append(f"{pre}: exemplo sem `{marca}`")
        if tipo == "fato-material" and not fonte.startswith(("pdf:", "txt:")):
            erros.append(f"{pre}: fato-material exige fonte pdf:/txt:")

        if prev and u.id in prev:
            h = lib.hash_unidade(u)
            if h != prev[u.id]["hash"] and not (isinstance(m["versao"], int) and m["versao"] > prev[u.id]["versao"]):
                erros.append(f"{pre}: conteúdo mudou (hash) e versao não subiu (era {prev[u.id]['versao']})")

    presentes = {u.nnn for u in arq.unidades}
    retirados_n = set()
    for rid in retiradas:
        m = lib.RE_ID_FULL.match(rid)
        if m:
            retirados_n.add(int(m.group(2)))
    todos = presentes | retirados_n
    if todos:
        esperado = set(range(1, max(todos) + 1))
        furos = sorted(esperado - todos)
        if furos:
            erros.append(f"numeração com furo (presentes ∪ retirados deve ser 001..max): faltam {[f'{n:03d}' for n in furos]}")
    if presentes & retirados_n:
        erros.append("IDs presentes e retirados ao mesmo tempo")
    return erros, warns


def validar_root(root: Path, *, revisao: str = "revisao", modulo: str | None = None, arquivo: str | None = None, sem_fontes: bool = False) -> dict:
    root = Path(root)
    manifest = lib.load_manifest()
    taxonomia = lib.load_taxonomia(root / "taxonomia.md")
    prev_rows = lib.ler_jsonl(lib.diretorio_gerado(root) / "unidades.jsonl")
    prev = {r["id"]: {"hash": r["hash"], "versao": r["versao"]} for r in prev_rows}
    erros: list[str] = []
    warns: list[str] = []
    ids_globais: dict[str, str] = {}
    n_arquivos = 0
    erros.extend(lib.verificar_fontes())
    tarefas_com_unidade: set[str] = set()
    for path, arq in lib.iter_unidades(root):
        slug = path.stem
        if modulo and not slug.startswith(f"{modulo}-"):
            continue
        if arquivo and slug != arquivo:
            continue
        n_arquivos += 1
        row = manifest.get(str(arq.front.get("aula_id", "")))
        fontes_disco = lib.fontes_no_disco(row) if row else []
        textos = None
        if row and not sem_fontes:
            textos = {}
            for nome in fontes_disco:
                t = lib.texto_fonte(row, nome)
                textos[nome] = lib.transcricao_sem_cabecalho(t) if nome == "transcricao.md" else t
        e, w = validar_texto(path.read_text(encoding="utf-8"), slug=slug, manifest=manifest, taxonomia=taxonomia, fontes_disco=fontes_disco, prev=prev, textos_fonte=textos)
        erros.extend(f"{slug}: {x}" for x in e)
        warns.extend(f"{slug}: {x}" for x in w)
        for u in arq.unidades:
            if u.id in ids_globais:
                erros.append(f"{slug}: {u.id} duplicado em {ids_globais[u.id]}")
            ids_globais[u.id] = slug
            for t in u.meta.get("tarefas") or []:
                tarefas_com_unidade.add(t)
    if not modulo and not arquivo and n_arquivos:
        for t in taxonomia.tarefas:
            if t not in tarefas_com_unidade:
                warns.append(f"tarefa sem unidade: {t}")
    return {"arquivos": n_arquivos, "unidades": len(ids_globais), "erros": erros, "warnings": warns}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=str(lib.BASE_DEFAULT))
    ap.add_argument("--revisao", default="revisao")
    ap.add_argument("--modulo")
    ap.add_argument("--arquivo", help="slug do arquivo")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--sem-fontes", action="store_true", help="não compara com transcrição/PDF (mais rápido)")
    args = ap.parse_args(argv)
    r = validar_root(Path(args.root), revisao=args.revisao, modulo=args.modulo, arquivo=args.arquivo, sem_fontes=args.sem_fontes)
    if args.json:
        print(json.dumps(r, ensure_ascii=False, indent=1))
    else:
        for e in r["erros"]:
            print(f"ERRO  {e}")
        for w in r["warnings"]:
            print(f"WARN  {w}")
        print(f"{r['arquivos']} arquivos, {r['unidades']} unidades, {len(r['erros'])} erros, {len(r['warnings'])} warnings")
    return 1 if r["erros"] else 0


if __name__ == "__main__":
    sys.exit(main())
