#!/usr/bin/env python3
"""Validador das visões, consolidação, órfãs e desatualização (FORMATO.md §6–§8). Stdlib only.

    python3 processamento/scripts/validate_visoes.py [--root DIR] [--revisao DIR] [--playbooks] [--consolidacao] [--orfas] [--desatualizadas] [--selar ARQ ...]

Sem flags: --playbooks --desatualizadas. Exit 1 se houver erro.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import unidades as lib  # noqa: E402

SECOES_PLAYBOOK = (
    "Quando usar",
    "Pré-condições",
    "Passos por plataforma",
    "Réguas e critérios de pronto",
    "Decisões",
    "Não fazer",
    "O que o curso não cobre",
    "Sem resolução no curso",
    "Perecível",
)
SECOES_COM_CITACAO = {"Quando usar", "Pré-condições", "Passos por plataforma", "Réguas e critérios de pronto", "Decisões", "Não fazer", "Perecível"}
MOTIVOS_ORFA = ("redundante com", "anedota sem ação", "perecível sem valor", "fora do escopo do gestor")
TIPOS_CHECKLIST = {"regua", "regra", "decisao", "alerta-ui"}


def _secoes(body: str) -> dict[str, str]:
    out: dict[str, str] = {}
    atual = None
    for line in body.splitlines():
        m = re.match(r"^## (.+?)\s*$", line)
        if m:
            atual = m.group(1)
            out[atual] = ""
        elif atual is not None:
            out[atual] += line + "\n"
    return out


def _bullets(texto: str) -> list[str]:
    return [l.strip() for l in texto.splitlines() if re.match(r"^\s*(-|\d+\.) ", l)]


def _contexto(root: Path):
    unidades = lib.todas_unidades(root)
    retirados = lib.retiradas(root)
    grupos = lib.todos_grupos(root)
    return unidades, retirados, grupos


def _checar_citacoes(pre: str, texto: str, unidades: dict, retirados: set, grupos: dict, erros: list[str]):
    for cid in lib.find_citacoes(texto):
        if cid in retirados:
            erros.append(f"{pre}: cita unidade retirada {cid}")
        elif cid not in unidades:
            erros.append(f"{pre}: cita ID inexistente {cid}")
    for gid in lib.find_citacoes_grupos(texto):
        if gid not in grupos:
            erros.append(f"{pre}: cita grupo inexistente {gid}")


def validar_playbook(path: Path, texto: str, unidades: dict, retirados: set, grupos: dict, taxonomia: lib.Taxonomia) -> list[str]:
    erros: list[str] = []
    pre = f"playbooks/{path.name}"
    front, body = lib.parse_front_matter(texto)
    if front.get("type") != "playbook":
        erros.append(f"{pre}: type deve ser playbook")
    tarefa = front.get("tarefa")
    if tarefa != path.stem:
        erros.append(f"{pre}: tarefa `{tarefa}` difere do nome do arquivo")
    if tarefa not in taxonomia.tarefas:
        erros.append(f"{pre}: tarefa `{tarefa}` fora da taxonomia")
    for campo in ("gerado_por", "insumos_hash", "status", "title"):
        if campo not in front:
            erros.append(f"{pre}: front matter sem `{campo}`")
    secoes = _secoes(body)
    ordem = [s for s in secoes if s in SECOES_PLAYBOOK]
    if ordem != list(SECOES_PLAYBOOK):
        erros.append(f"{pre}: seções fixas ausentes ou fora de ordem: {ordem}")
    for nome in SECOES_COM_CITACAO:
        for b in _bullets(secoes.get(nome, "")):
            if not lib.RE_ID.search(b):
                erros.append(f"{pre}: bullet sem citação em `{nome}`: {b[:60]}")
            elif not re.search(r"`U:[0-9a-f]{16}:\d{3}`\s*\.?\s*$", b):
                erros.append(f"{pre}: bullet não termina com citação em `{nome}`: {b[:60]}")
    passos = secoes.get("Passos por plataforma", "")
    subs = set(re.findall(r"^### ([a-z0-9-]+)\s*$", passos, re.M))
    if tarefa in taxonomia.tarefas:
        esperadas = set(taxonomia.tarefas[tarefa]["plataformas"])
        parcial = front.get("parcial_ate")
        faltam = esperadas - subs
        if faltam and not parcial:
            erros.append(f"{pre}: Passos por plataforma sem subseção para {sorted(faltam)}")
        for s in subs - esperadas:
            if s not in taxonomia.plataformas:
                erros.append(f"{pre}: subseção de plataforma `{s}` fora da taxonomia")
    _checar_citacoes(pre, body, unidades, retirados, grupos, erros)
    if "PENDENTE" in str(front.get("insumos_hash", "")):
        erros.append(f"{pre}: insumos_hash PENDENTE (rode --selar)")
    for l in body.splitlines():
        if lib.RE_HOJE.search(l) and not l.startswith("#"):
            erros.append(f"{pre}: 'hoje/atualmente' no texto")
            break
    return erros


def validar_checklist(path: Path, texto: str, unidades: dict, retirados: set, grupos: dict, taxonomia: lib.Taxonomia) -> list[str]:
    erros: list[str] = []
    pre = f"checklists/{path.name}"
    front, body = lib.parse_front_matter(texto)
    if front.get("type") != "checklist":
        erros.append(f"{pre}: type deve ser checklist")
    if front.get("plataforma") != path.stem or path.stem not in taxonomia.plataformas:
        erros.append(f"{pre}: plataforma inválida")
    for b in _bullets(body):
        ids = lib.find_citacoes(b)
        if not ids:
            erros.append(f"{pre}: bullet sem citação: {b[:60]}")
        for cid in ids:
            u = unidades.get(cid)
            if u and u.meta.get("tipo") not in TIPOS_CHECKLIST:
                erros.append(f"{pre}: {cid} é `{u.meta.get('tipo')}`; checklist cita só regua/regra/decisao/alerta-ui")
    _checar_citacoes(pre, body, unidades, retirados, grupos, erros)
    if "PENDENTE" in str(front.get("insumos_hash", "")):
        erros.append(f"{pre}: insumos_hash PENDENTE")
    return erros


def validar_glossario(path: Path, texto: str, unidades: dict, retirados: set, grupos: dict) -> list[str]:
    erros: list[str] = []
    pre = "glossario.md"
    front, body = lib.parse_front_matter(texto)
    if front.get("type") != "glossario":
        erros.append(f"{pre}: type deve ser glossario")
    for b in _bullets(body):
        if not lib.RE_ID.search(b):
            erros.append(f"{pre}: termo sem citação: {b[:60]}")
    _checar_citacoes(pre, body, unidades, retirados, grupos, erros)
    return erros


def validar_visoes(root: Path, taxonomia: lib.Taxonomia | None = None) -> list[str]:
    root = Path(root)
    taxonomia = taxonomia or lib.load_taxonomia(root / "taxonomia.md")
    unidades, retirados, grupos = _contexto(root)
    erros: list[str] = []
    for p in sorted((root / "visoes" / "playbooks").glob("*.md")):
        erros.extend(validar_playbook(p, p.read_text(encoding="utf-8"), unidades, retirados, grupos, taxonomia))
    for p in sorted((root / "visoes" / "checklists").glob("*.md")):
        erros.extend(validar_checklist(p, p.read_text(encoding="utf-8"), unidades, retirados, grupos, taxonomia))
    g = root / "visoes" / "glossario.md"
    if g.exists():
        erros.extend(validar_glossario(g, g.read_text(encoding="utf-8"), unidades, retirados, grupos))
    return erros


def validar_consolidacao(root: Path, taxonomia: lib.Taxonomia | None = None) -> list[str]:
    root = Path(root)
    taxonomia = taxonomia or lib.load_taxonomia(root / "taxonomia.md")
    unidades, retirados, _ = _contexto(root)
    erros: list[str] = []
    for p in sorted((root / "consolidacao").glob("*.md")):
        pre = f"consolidacao/{p.name}"
        front, grupos, e = lib.parse_grupos(p.read_text(encoding="utf-8"))
        erros.extend(f"{pre}: {x}" for x in e)
        if front.get("type") != "consolidacao" or front.get("tema") != p.stem or p.stem not in taxonomia.temas:
            erros.append(f"{pre}: front matter (type/tema) inválido")
        for g in grupos:
            if not g.id.startswith(f"G:{p.stem}:"):
                erros.append(f"{pre}: {g.id} não pertence ao tema {p.stem}")
            tipo = g.meta.get("tipo")
            if tipo not in {"duplicata", "conflito", "complemento", "condicional"}:
                erros.append(f"{pre}: {g.id} tipo `{tipo}` inválido")
            us = g.meta.get("unidades") or []
            if len(us) < 2:
                erros.append(f"{pre}: {g.id} precisa de ≥2 unidades")
            for cid in us + (g.meta.get("evidencia") or []) + ([g.meta["canonica"]] if g.meta.get("canonica") else []):
                if cid in retirados:
                    erros.append(f"{pre}: {g.id} cita unidade retirada {cid}")
                elif cid not in unidades:
                    erros.append(f"{pre}: {g.id} cita ID inexistente {cid}")
            if tipo == "condicional" and g.meta.get("canonica"):
                erros.append(f"{pre}: {g.id} condicional não admite canonica")
            if tipo == "conflito" and g.meta.get("canonica") and not g.meta.get("evidencia"):
                erros.append(f"{pre}: {g.id} conflito com canonica exige evidencia")
            if not g.resolucao:
                erros.append(f"{pre}: {g.id} sem resolucao")
    return erros


def orfas(root: Path) -> list[str]:
    """IDs com `tarefas` não vazia não citados por playbook, checklist ou glossário (páginas de tema não contam)."""
    root = Path(root)
    unidades = lib.todas_unidades(root)
    citadas: set[str] = set()
    for sub in ("playbooks", "checklists"):
        for p in (root / "visoes" / sub).glob("*.md"):
            citadas.update(lib.find_citacoes(p.read_text(encoding="utf-8")))
    g = root / "visoes" / "glossario.md"
    if g.exists():
        citadas.update(lib.find_citacoes(g.read_text(encoding="utf-8")))
    return sorted(uid for uid, u in unidades.items() if (u.meta.get("tarefas") or []) and uid not in citadas)


def validar_orfas(root: Path) -> list[str]:
    root = Path(root)
    erros: list[str] = []
    lista = orfas(root)
    p = root / "visoes" / "orfas.md"
    justificadas: dict[str, str] = {}
    if p.exists():
        for m in re.finditer(r"^\| `?(U:[0-9a-f]{16}:\d{3})`? \| (.+?) \|$", p.read_text(encoding="utf-8"), re.M):
            justificadas[m.group(1)] = m.group(2).strip()
    for uid in lista:
        motivo = justificadas.get(uid)
        if not motivo:
            erros.append(f"orfas: {uid} não citada e sem motivo em visoes/orfas.md")
        elif not any(motivo.startswith(x) for x in MOTIVOS_ORFA):
            erros.append(f"orfas: {uid} motivo fora da lista fechada: {motivo}")
    com_tarefa = sum(1 for u in lib.todas_unidades(root).values() if u.meta.get("tarefas"))
    if com_tarefa and len(lista) / com_tarefa > 0.15:
        erros.append(f"orfas: {len(lista)}/{com_tarefa} = {len(lista)/com_tarefa:.0%} > 15%; revisar playbooks antes de aceitar motivos")
    return erros


# ----------------------------------------------------------------------------- insumos_hash / desatualizadas


def _artefatos(root: Path, revisao: str) -> list[Path]:
    root = Path(root)
    out: list[Path] = []
    for sub in ("playbooks", "checklists"):
        out.extend(sorted((root / "visoes" / sub).glob("*.md")))
    for nome in ("glossario.md", "orfas.md"):
        p = root / "visoes" / nome
        if p.exists():
            out.append(p)
    out.extend(sorted((root / "consolidacao").glob("*.md")))
    laudos = lib.diretorio_revisao(root, revisao) / "laudos"
    if laudos.exists():
        # Laudos vivos apenas: evidências, rodadas arquivadas (`*.rodada-N.md`) e laudos de fixtures
        # (`fixture-*.md`, que julgaram cópias em calibracao/) são registro histórico, não derivado.
        out.extend(p for p in sorted(laudos.glob("*.md")) if not p.name.endswith(".evidencia.md") and not re.search(r"\.rodada-\d+\.md$", p.name) and not p.name.startswith("fixture-"))
    return out


def insumos_de(root: Path, path: Path, unidades: dict | None = None, grupos: dict | None = None) -> tuple[list[str], list[str]]:
    """IDs de unidades e grupos que o artefato cita (laudo de aula cita todas as vivas do arquivo)."""
    unidades = unidades if unidades is not None else lib.todas_unidades(root)
    grupos = grupos if grupos is not None else lib.todos_grupos(root)
    texto = path.read_text(encoding="utf-8")
    front, body = lib.parse_front_matter(texto)
    ids = set(lib.find_citacoes(body))
    gids = set(lib.find_citacoes_grupos(body))
    if front.get("type") == "laudo" and front.get("aula_id") and not ids:
        ids = {uid for uid in unidades if uid.split(":")[1] == str(front["aula_id"])}
    if front.get("type") == "consolidacao":
        _, gs, _ = lib.parse_grupos(texto)
        for g in gs:
            ids.update(g.meta.get("unidades") or [])
            ids.update(g.meta.get("evidencia") or [])
    return sorted(ids), sorted(gids)


def calcular_insumos_hash(root: Path, path: Path, unidades: dict | None = None, grupos: dict | None = None) -> str:
    root = Path(root)
    unidades = unidades if unidades is not None else lib.todas_unidades(root)
    grupos = grupos if grupos is not None else lib.todos_grupos(root)
    ids, gids = insumos_de(root, path, unidades, grupos)
    pu = {uid: lib.hash_unidade(unidades[uid]) for uid in ids if uid in unidades}
    pg = {gid: lib.hash_grupo(grupos[gid]) for gid in gids if gid in grupos}
    return lib.insumos_hash(pu, pg, lib.sha256_file(root / "FORMATO.md"), lib.sha256_file(root / "taxonomia.md"))


def _ler_selos(root: Path) -> dict[str, dict[str, dict]]:
    out: dict[str, dict[str, dict]] = defaultdict(dict)
    for r in lib.ler_jsonl(lib.diretorio_gerado(root) / "selos.jsonl"):
        out[r["artefato"]][r["insumo"]] = r
    return out


def _gravar_selos(root: Path, selos: dict[str, dict[str, dict]]) -> None:
    linhas = [r for art in selos.values() for r in art.values()]
    linhas.sort(key=lambda r: (r["artefato"], r["insumo"]))
    p = lib.diretorio_gerado(root) / "selos.jsonl"
    p.parent.mkdir(exist_ok=True)
    p.write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in linhas), encoding="utf-8")


def selar(root: Path, path: Path) -> str:
    """Grava `insumos_hash` no artefato e o registro por insumo em `_gerado/selos.jsonl`."""
    root = Path(root)
    unidades = lib.todas_unidades(root)
    grupos = lib.todos_grupos(root)
    h = calcular_insumos_hash(root, path, unidades, grupos)
    texto = path.read_text(encoding="utf-8")
    path.write_text(lib.substituir_campo_front(texto, "insumos_hash", h), encoding="utf-8")
    rel = lib.referencia_artefato(root, path)
    ids, gids = insumos_de(root, path, unidades, grupos)
    selos = _ler_selos(root)
    selos[rel] = {}
    for uid in ids:
        if uid in unidades:
            selos[rel][uid] = {"artefato": rel, "insumo": uid, "hash": lib.hash_unidade(unidades[uid]), "corpo_hash": lib.hash_corpo(unidades[uid])}
    for gid in gids:
        if gid in grupos:
            selos[rel][gid] = {"artefato": rel, "insumo": gid, "hash": lib.hash_grupo(grupos[gid]), "corpo_hash": None}
    selos[rel]["FORMATO"] = {"artefato": rel, "insumo": "FORMATO", "hash": lib.sha256_file(root / "FORMATO.md"), "corpo_hash": None}
    selos[rel]["TAXONOMIA"] = {"artefato": rel, "insumo": "TAXONOMIA", "hash": lib.sha256_file(root / "taxonomia.md"), "corpo_hash": None}
    _gravar_selos(root, selos)
    return h


def desatualizadas(root: Path, revisao: str = "revisao") -> list[dict]:
    """Compara o insumos_hash gravado com o atual; explica a mudança pelos selos por insumo."""
    root = Path(root)
    unidades = lib.todas_unidades(root)
    grupos = lib.todos_grupos(root)
    retirados = lib.retiradas(root)
    selos = _ler_selos(root)
    linhas: list[dict] = []
    for p in _artefatos(root, revisao):
        front, _ = lib.parse_front_matter(p.read_text(encoding="utf-8"))
        gravado = str(front.get("insumos_hash", ""))
        atual = calcular_insumos_hash(root, p, unidades, grupos)
        if gravado == atual:
            continue
        rel = lib.referencia_artefato(root, p)
        ids, gids = insumos_de(root, p, unidades, grupos)
        selo = selos.get(rel, {})
        explicado = False
        for uid in ids:
            if uid in retirados or uid not in unidades:
                linhas.append({"artefato": rel, "insumo": uid, "mudanca": "retirado"})
                explicado = True
            elif uid not in selo:
                linhas.append({"artefato": rel, "insumo": uid, "mudanca": "insumo novo"})
                explicado = True
            elif selo[uid]["hash"] != lib.hash_unidade(unidades[uid]):
                mud = "corpo" if lib.hash_corpo(unidades[uid]) != selo[uid].get("corpo_hash") else "metadado"
                linhas.append({"artefato": rel, "insumo": uid, "mudanca": mud})
                explicado = True
        for gid in gids:
            if gid not in grupos:
                linhas.append({"artefato": rel, "insumo": gid, "mudanca": "retirado"})
                explicado = True
            elif gid in selo and selo[gid]["hash"] != lib.hash_grupo(grupos[gid]):
                linhas.append({"artefato": rel, "insumo": gid, "mudanca": "grupo"})
                explicado = True
        for nome, arquivo in (("FORMATO", "FORMATO.md"), ("TAXONOMIA", "taxonomia.md")):
            if nome in selo and selo[nome]["hash"] != lib.sha256_file(root / arquivo):
                linhas.append({"artefato": rel, "insumo": arquivo, "mudanca": "formato"})
                explicado = True
        if not explicado:
            linhas.append({"artefato": rel, "insumo": "sem selo ou insumos_hash não selado", "mudanca": "formato"})
    return linhas


def render_desatualizadas(linhas: list[dict]) -> str:
    out = ["# Desatualizadas", "", "Artefatos cujo `insumos_hash` não bate com as unidades/grupos que citam. Gate: vazio.", "", "| artefato | insumo | mudança |", "|---|---|---|"]
    for l in linhas:
        out.append(f"| {l['artefato']} | {l['insumo']} | {l['mudanca']} |")
    return "\n".join(out) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=str(lib.BASE_DEFAULT))
    ap.add_argument("--revisao", default="revisao")
    ap.add_argument("--playbooks", action="store_true", help="valida playbooks, checklists e glossário")
    ap.add_argument("--consolidacao", action="store_true")
    ap.add_argument("--orfas", action="store_true")
    ap.add_argument("--desatualizadas", action="store_true")
    ap.add_argument("--selar", nargs="*", help="grava insumos_hash nos arquivos")
    args = ap.parse_args(argv)
    root = Path(args.root)
    if not (args.playbooks or args.consolidacao or args.orfas or args.desatualizadas or args.selar):
        args.playbooks = args.desatualizadas = True
    erros: list[str] = []
    if args.selar:
        for a in args.selar:
            print(f"selado {a}: {selar(root, Path(a))}")
    if args.playbooks:
        erros.extend(validar_visoes(root))
    if args.consolidacao:
        erros.extend(validar_consolidacao(root))
    if args.orfas:
        erros.extend(validar_orfas(root))
    if args.desatualizadas:
        linhas = desatualizadas(root, args.revisao)
        lib.diretorio_gerado(root).mkdir(parents=True, exist_ok=True)
        (lib.diretorio_gerado(root) / "desatualizadas.md").write_text(render_desatualizadas(linhas), encoding="utf-8")
        erros.extend(f"desatualizada: {l['artefato']} ← {l['insumo']} ({l['mudanca']})" for l in linhas)
    for e in erros:
        print(f"ERRO  {e}")
    print(f"{len(erros)} erros")
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
