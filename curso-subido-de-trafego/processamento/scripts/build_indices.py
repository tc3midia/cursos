#!/usr/bin/env python3
"""Gera `_gerado/`, `visoes/temas/` e o índice (FORMATO.md §5, §6.5). Determinístico. Stdlib only.

    python3 processamento/scripts/build_indices.py [--root DIR] [--revisao DIR] [--check]

`--check` compara com o disco e sai com 1 se algo difere.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import unidades as lib  # noqa: E402
import validate_visoes as vv  # noqa: E402

INDICE_NOME = "indice.md"


def _grupo_por_unidade(root: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    for gid, g in lib.todos_grupos(root).items():
        for uid in g.meta.get("unidades") or []:
            out.setdefault(uid, gid)
    return out


def _linhas_jsonl(root: Path, manifest: dict) -> list[dict]:
    grupo = _grupo_por_unidade(root)
    linhas = []
    for path, arq in lib.iter_unidades(root):
        row = manifest.get(str(arq.front.get("aula_id", ""))) or {}
        for u in arq.unidades:
            m = u.meta
            linhas.append(
                {
                    "id": u.id,
                    "aula_id": u.aula_id,
                    "slug": path.stem,
                    "modulo": str(arq.front.get("modulo", row.get("modulo3", ""))),
                    "ordem": arq.front.get("ordem", row.get("ordem")),
                    "titulo": u.titulo,
                    "tipo": m.get("tipo"),
                    "plataforma": m.get("plataforma") if isinstance(m.get("plataforma"), list) else [m.get("plataforma")],
                    "tema": m.get("tema"),
                    "tarefas": m.get("tarefas") if isinstance(m.get("tarefas"), list) else [m.get("tarefas")],
                    "fonte": m.get("fonte"),
                    "faixa": m.get("faixa"),
                    "condicoes": m.get("condicoes"),
                    "perecivel": m.get("perecivel"),
                    "confianca": m.get("confianca"),
                    "versao": m.get("versao"),
                    "hash": lib.hash_unidade(u),
                    "corpo_hash": lib.hash_corpo(u),
                    "grupo": grupo.get(u.id),
                }
            )
    linhas.sort(key=lambda l: (l["modulo"], l["ordem"] or 0, l["id"]))
    return linhas


def _cobertura(linhas: list[dict], tax: lib.Taxonomia) -> list[dict]:
    idx: dict[tuple[str, str], list[str]] = defaultdict(list)
    for l in linhas:
        for t in l["tarefas"]:
            for p in l["plataforma"]:
                idx[(t, p)].append(l["id"])
    out = []
    for tarefa, info in tax.tarefas.items():
        plats = list(info["plataformas"])
        for p in plats:
            ids = sorted(idx.get((tarefa, p), []))
            if p != "geral":
                ids = sorted(set(ids) | set(idx.get((tarefa, "geral"), [])))
            out.append({"tarefa": tarefa, "plataforma": p, "n_unidades": len(ids), "ids": ids})
    return out


def _propostas(root: Path) -> str:
    por_texto: dict[str, list[str]] = defaultdict(list)
    for _, arq in lib.iter_unidades(root):
        for u in arq.unidades:
            if u.meta.get("proposta_tag"):
                por_texto[str(u.meta["proposta_tag"])].append(u.id)
    out = ["# Propostas de tag", "", "Agregadas de `proposta_tag`. Triagem no fim de cada módulo; zero restante é condição da etapa 3.", ""]
    if not por_texto:
        out.append("Nenhuma proposta pendente.")
    for texto in sorted(por_texto):
        out.append(f"- {texto} — {', '.join(f'`{i}`' for i in sorted(por_texto[texto]))}")
    return "\n".join(out) + "\n"


def _playbooks_por_unidade(root: Path) -> dict[str, set[str]]:
    out: dict[str, set[str]] = defaultdict(set)
    for p in sorted((root / "visoes" / "playbooks").glob("*.md")):
        for uid in set(lib.find_citacoes(p.read_text(encoding="utf-8"))):
            out[uid].add(p.stem)
    return out


def _paginas_tema(root: Path, linhas: list[dict], tax: lib.Taxonomia) -> dict[str, str]:
    unidades = lib.todas_unidades(root)
    por_tema: dict[str, list[dict]] = defaultdict(list)
    for l in linhas:
        por_tema[l["tema"]].append(l)
    tarefas_por_tema: dict[str, Counter] = defaultdict(Counter)
    for l in linhas:
        for t in l["tarefas"]:
            tarefas_por_tema[l["tema"]][t] += 1
    playbooks = _playbooks_por_unidade(root)
    paginas: dict[str, str] = {}
    for tema in sorted(por_tema):
        ls = por_tema[tema]
        out = [
            "---",
            "type: pagina-tema",
            "status: gerado",
            f"title: \"{tema}\"",
            f"tema: {tema}",
            f"account_id: {lib.ACCOUNT_ID}",
            "gerado_por: build_indices",
            "---",
            "",
            f"# Tema — {tema}",
            "",
            f"{tax.definicoes.get(tema, '')}",
            "",
            f"Página gerada por `build_indices.py`: zero prosa nova; não conta como citação. {len(ls)} unidades.",
            "",
        ]
        for tipo in tax.tipos:
            grupo = [l for l in ls if l["tipo"] == tipo]
            if not grupo:
                continue
            out.append(f"## {tipo} ({len(grupo)})")
            out.append("")
            for l in grupo:
                u = unidades[l["id"]]
                cond = f" · condição: {l['condicoes']}" if l.get("condicoes") else ""
                per = " · perecível" if l.get("perecivel") else ""
                out.append(f"### `{l['id']}` — {l['titulo']}")
                out.append(f"*{', '.join(l['plataforma'])} · {', '.join(l['tarefas']) or 'sem tarefa'} · [{l['slug']}](../../unidades/{l['slug']}.md){cond}{per}*")
                out.append("")
                out.extend(u.corpo)
                out.append("")
        relacionados: Counter = Counter()
        for outro, cnt in tarefas_por_tema.items():
            if outro == tema:
                continue
            comuns = set(cnt) & set(tarefas_por_tema.get(tema, ()))
            if comuns:
                relacionados[outro] = len(comuns)
        out.append("## Temas relacionados (coocorrência de tarefa)")
        out.append("")
        if relacionados:
            for outro, n in sorted(relacionados.items(), key=lambda kv: (-kv[1], kv[0])):
                out.append(f"- [{outro}]({outro}.md) — {n} tarefas em comum")
        else:
            out.append("- nenhum")
        out.append("")
        pbs = sorted({pb for l in ls for pb in playbooks.get(l["id"], ())})
        out.append("## Playbooks que citam unidades deste tema")
        out.append("")
        out.extend([f"- [{pb}](../playbooks/{pb}.md)" for pb in pbs] or ["- nenhum"])
        paginas[tema] = "\n".join(out) + "\n"
    return paginas


def _indice(root: Path, linhas: list[dict], tax: lib.Taxonomia, manifest: dict, temas: dict[str, str]) -> str:
    out = ["---", "type: wiki", "status: v2", "title: Curso Subido de Tráfego", f"account_id: {lib.ACCOUNT_ID}", "gerado_por: build_indices", "---", "", "# Curso Subido de Tráfego — índice (v2)", "", "Contrato: `README.md`. Gerado por `build_indices.py`.", ""]
    pbs = sorted(p.stem for p in (root / "visoes" / "playbooks").glob("*.md"))
    cks = sorted(p.stem for p in (root / "visoes" / "checklists").glob("*.md"))
    out.append("## Uso desta base")
    out.append("")
    out.append("A biblioteca reúne as unidades das aulas e os índices por tema. Validação por amostragem; as instruções de interface preservam o contexto histórico do curso.")
    out.append("")
    out.append("## Procedimentos disponíveis")
    out.append("")
    for tarefa in pbs:
        meta, _ = lib.parse_front_matter((root / "visoes" / "playbooks" / f"{tarefa}.md").read_text(encoding="utf-8"))
        out.append(f"- [{tarefa}](visoes/playbooks/{tarefa}.md) — status: {meta.get('status', 'não informado')}; escopo definido no próprio arquivo.")
    if not pbs:
        out.append("Nenhum playbook disponível.")
    out.extend([f"- [Checklist: {c}](visoes/checklists/{c}.md)" for c in cks] or ["Checklists ainda não produzidos. A transformação em rotinas do Gestor de Tráfego tem acompanhamento próprio, indicado no [README](README.md)."])
    out.append("")
    if (root / "visoes" / "glossario.md").exists():
        out.append("## Glossário")
        out.append("")
        out.append("- [glossário](visoes/glossario.md)")
        out.append("")
    out.append("## Páginas de tema (geradas)")
    out.append("")
    out.extend([f"- [{t}](visoes/temas/{t}.md)" for t in sorted(temas)] or ["- nenhuma ainda"])
    out.append("")
    out.append("## Unidades por aula")
    out.append("")
    processadas = {str(arq.front.get("aula_id", "")): (path, arq) for path, arq in lib.iter_unidades(root)}
    total_processadas = sum(aula_id in processadas for aula_id in manifest)
    total_unidades = sum(len(arq.unidades) for aula_id, (_, arq) in processadas.items() if aula_id in manifest)
    out.append(f"Grade completa: **{len(manifest)} aulas** · **{total_processadas} com unidades** · **{len(manifest) - total_processadas} a processar** · **{total_unidades} unidades disponíveis**.")
    out.append("")
    out.append("As aulas estão na ordem do curso. Os links abrem as unidades já extraídas; as demais estão marcadas como a processar. O status de cada arquivo permanece indicado.")
    out.append("")
    por_modulo: dict[str, list[dict]] = defaultdict(list)
    for row in sorted(manifest.values(), key=lambda row: (row["modulo3"], int(row["ordem"]))):
        por_modulo[row["modulo3"]].append(row)
    for aulas in por_modulo.values():
        out.append(f"### {aulas[0]['modulo']}")
        out.append("")
        feitas = [processadas[row["id"]] for row in aulas if row["id"] in processadas]
        n = sum(len(arq.unidades) for _, arq in feitas)
        out.append(f"{len(feitas)}/{len(aulas)} aulas com unidades · {n} unidades disponíveis.")
        out.append("")
        for row in aulas:
            if row["id"] in processadas:
                path, arq = processadas[row["id"]]
                out.append(f"- [{row['aula']}](unidades/{path.stem}.md) — {len(arq.unidades)} unidades · {arq.front.get('status', '')}")
            else:
                out.append(f"- {row['aula']} — a processar; unidades ainda não disponíveis")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def gerar(root: Path, revisao: str = "revisao") -> dict[str, str]:
    """Devolve {caminho relativo: conteúdo} de tudo que o script gera. Não grava."""
    root = Path(root)
    manifest = lib.load_manifest()
    tax = lib.load_taxonomia(root / "taxonomia.md")
    linhas = _linhas_jsonl(root, manifest)
    saidas: dict[str, str] = {}
    saidas["_gerado/unidades.jsonl"] = "".join(json.dumps(l, ensure_ascii=False, sort_keys=True) + "\n" for l in linhas)
    saidas["_gerado/cobertura.jsonl"] = "".join(json.dumps(l, ensure_ascii=False, sort_keys=True) + "\n" for l in _cobertura(linhas, tax))
    saidas["_gerado/propostas_tags.md"] = _propostas(root)
    temas = _paginas_tema(root, linhas, tax)
    for tema, conteudo in temas.items():
        saidas[f"visoes/temas/{tema}.md"] = conteudo
    saidas[INDICE_NOME] = _indice(root, linhas, tax, manifest, temas)
    return saidas


def escrever(root: Path, revisao: str = "revisao") -> dict[str, str]:
    root = Path(root)
    saidas = gerar(root, revisao)
    for rel, conteudo in saidas.items():
        p = lib.caminho_artefato(root, rel)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(conteudo, encoding="utf-8")
    for p in (root / "visoes" / "temas").glob("*.md"):
        if f"visoes/temas/{p.name}" not in saidas:
            p.unlink()
    linhas = vv.desatualizadas(root, revisao)
    (lib.diretorio_gerado(root) / "desatualizadas.md").write_text(vv.render_desatualizadas(linhas), encoding="utf-8")
    return saidas


def checar(root: Path, revisao: str = "revisao") -> list[str]:
    root = Path(root)
    saidas = gerar(root, revisao)
    difs = []
    for rel, conteudo in saidas.items():
        p = lib.caminho_artefato(root, rel)
        if not p.exists():
            difs.append(f"ausente: {rel}")
        elif p.read_text(encoding="utf-8") != conteudo:
            difs.append(f"difere: {rel}")
    for p in (root / "visoes" / "temas").glob("*.md"):
        if f"visoes/temas/{p.name}" not in saidas:
            difs.append(f"sobrando: visoes/temas/{p.name}")
    linhas = vv.desatualizadas(root, revisao)
    esperado = vv.render_desatualizadas(linhas)
    p = lib.diretorio_gerado(root) / "desatualizadas.md"
    if not p.exists() or p.read_text(encoding="utf-8") != esperado:
        difs.append("difere: _gerado/desatualizadas.md")
    return difs


def desatualizadas_vazio(texto: str) -> bool:
    return not any(l.startswith("| ") and not l.startswith("| artefato") for l in texto.splitlines())


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=str(lib.BASE_DEFAULT))
    ap.add_argument("--revisao", default="revisao")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args(argv)
    root = Path(args.root)
    if args.check:
        difs = checar(root, args.revisao)
        for d in difs:
            print(d)
        print("ok" if not difs else f"{len(difs)} diferenças")
        return 1 if difs else 0
    saidas = escrever(root, args.revisao)
    print(f"{len(saidas)} arquivos gerados em {root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
