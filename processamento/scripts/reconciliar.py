#!/usr/bin/env python3
"""Reconcilia uma reextração com o arquivo de unidades já existente.

    python3 processamento/scripts/reconciliar.py <antigo.md> <novo.md> [--saida ARQ]
        [--divisao U:x:002=2,3 ...] [--fusao U:x:002+U:x:003=4 ...]

A numeração do arquivo novo (vinda do extrator) é descartada; só o conteúdo importa.
IDs das unidades antigas que casam são preservados; unidades novas recebem números
depois do maior (presentes ∪ retiradas); antigas sem par vão para `retiradas`.
Sem `--saida` imprime o texto reconciliado; o relatório sai em stderr como JSON.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import unidades as lib  # noqa: E402

JACCARD_MINIMO = 0.6


def _numero(uid: str) -> int:
    return int(uid.rsplit(":", 1)[1])


def _palavras(u: lib.Unidade) -> set[str]:
    texto = " ".join(u.corpo).lower()
    return set(re.findall(r"\w+", texto))


def _jaccard(a: set[str], b: set[str]) -> float:
    if not a and not b:
        return 1.0
    return len(a & b) / len(a | b)


def _casar(nova: lib.Unidade, candidatas: list[lib.Unidade]) -> lib.Unidade | None:
    """Título igual (slug) vence; senão, a candidata de maior Jaccard de corpo, se ≥ 0,6."""
    slug = lib.slugify(nova.titulo)
    for c in candidatas:
        if lib.slugify(c.titulo) == slug:
            return c
    pal = _palavras(nova)
    melhor, score = None, 0.0
    for c in candidatas:
        j = _jaccard(pal, _palavras(c))
        if j > score:
            melhor, score = c, j
    return melhor if score >= JACCARD_MINIMO else None


def _lista_front(valores: list[str]) -> str:
    return lib._yaml_escalar(list(valores))


def _corpo_ate_unidades(texto: str) -> str:
    """Tudo do texto novo até o primeiro bloco `### U:` (front matter, título, contexto, `## Unidades`)."""
    m = lib.RE_BLOCO.search(texto)
    if m:
        return texto[: m.start()].rstrip("\n") + "\n\n"
    idx = texto.find("## Unidades")
    if idx < 0:
        raise ValueError("arquivo novo sem seção `## Unidades`")
    fim = texto.find("\n", idx)
    return texto[: fim if fim >= 0 else len(texto)].rstrip("\n") + "\n\n"


def reconciliar(
    texto_antigo: str,
    texto_novo: str,
    divisoes: list[tuple[str, list[int]]] | None = None,
    fusoes: list[tuple[list[str], int]] | None = None,
) -> tuple[str, dict]:
    antigo = lib.parse_arquivo_unidades(texto_antigo)
    novo = lib.parse_arquivo_unidades(texto_novo)
    if antigo.erros_parse or novo.erros_parse:
        raise ValueError("erro de parse: " + "; ".join(antigo.erros_parse + novo.erros_parse))
    aula = str(antigo.front.get("aula_id", ""))
    if not aula or str(novo.front.get("aula_id", "")) != aula:
        raise ValueError("aula_id ausente ou diferente entre antigo e novo")

    vivas: dict[str, lib.Unidade] = {u.id: u for u in antigo.unidades}
    retiradas_prev = [str(x) for x in (antigo.front.get("retiradas") or [])]
    divisoes_prev = [str(x) for x in (antigo.front.get("divisoes") or [])]
    fusoes_prev = [str(x) for x in (antigo.front.get("fusoes") or [])]
    proximo = max([_numero(i) for i in list(vivas) + retiradas_prev], default=0) + 1

    # Unidades novas que saem de divisão ou fusão não passam pelo casamento automático.
    origem_divisao: dict[int, str] = {}
    origem_fusao: dict[int, list[str]] = {}
    consumidas: set[str] = set()
    for antigo_id, posicoes in divisoes or []:
        if antigo_id not in vivas:
            raise ValueError(f"divisão de ID inexistente: {antigo_id}")
        consumidas.add(antigo_id)
        for p in posicoes:
            origem_divisao[p - 1] = antigo_id
    for antigos_ids, pos in fusoes or []:
        for a in antigos_ids:
            if a not in vivas:
                raise ValueError(f"fusão de ID inexistente: {a}")
        consumidas.update(antigos_ids)
        origem_fusao[pos - 1] = list(antigos_ids)
    for i in list(origem_divisao) + list(origem_fusao):
        if not 0 <= i < len(novo.unidades):
            raise ValueError(f"posição {i + 1} fora do arquivo novo ({len(novo.unidades)} unidades)")

    casadas: list[str | None] = [None] * len(novo.unidades)
    for i, u in enumerate(novo.unidades):
        if i in origem_divisao or i in origem_fusao:
            continue
        par = _casar(u, [v for vid, v in vivas.items() if vid not in consumidas])
        if par is not None:
            casadas[i] = par.id
            consumidas.add(par.id)

    rel: dict[str, list[str]] = {"preservadas": [], "novas": [], "retiradas": [], "divisoes": [], "fusoes": []}
    filhas_divisao: dict[str, list[str]] = {}
    blocos: list[lib.Unidade] = []
    for i, u in enumerate(novo.unidades):
        meta = dict(u.meta)
        if casadas[i]:
            velha = vivas[casadas[i]]
            nova = lib.Unidade(velha.id, u.titulo, meta, list(u.corpo))
            versao_antiga = int(velha.meta.get("versao", 1))
            meta["versao"] = versao_antiga + 1 if lib.hash_unidade(nova) != lib.hash_unidade(velha) else versao_antiga
            rel["preservadas"].append(velha.id)
        else:
            nid = f"U:{aula}:{proximo:03d}"
            proximo += 1
            meta["versao"] = 1
            nova = lib.Unidade(nid, u.titulo, meta, list(u.corpo))
            rel["novas"].append(nid)
            if i in origem_divisao:
                filhas_divisao.setdefault(origem_divisao[i], []).append(nid)
            if i in origem_fusao:
                rel["fusoes"].append(f"{', '.join(origem_fusao[i])} → {nid}")
        blocos.append(nova)
    for antigo_id, filhas in filhas_divisao.items():
        rel["divisoes"].append(f"{antigo_id} → {', '.join(filhas)}")

    preservadas = set(rel["preservadas"])
    rel["retiradas"] = [vid for vid in vivas if vid not in preservadas]

    # Blocos por ID crescente: preservadas primeiro, novas (inclusive filhas de divisão e fusão) no fim.
    blocos.sort(key=lambda b: _numero(b.id))
    texto = _corpo_ate_unidades(texto_novo) + "".join(lib.serializar_unidade(b) for b in blocos)
    texto = lib.substituir_campo_front(texto, "retiradas", _lista_front(retiradas_prev + rel["retiradas"]))
    texto = lib.substituir_campo_front(texto, "divisoes", _lista_front(divisoes_prev + rel["divisoes"]))
    texto = lib.substituir_campo_front(texto, "fusoes", _lista_front(fusoes_prev + rel["fusoes"]))
    return texto, rel


def _parse_divisao(s: str) -> tuple[str, list[int]]:
    antigo_id, _, pos = s.partition("=")
    if not antigo_id or not pos:
        raise argparse.ArgumentTypeError(f"--divisao espera U:x:nnn=2,3 (recebeu {s!r})")
    return antigo_id.strip(), [int(p) for p in pos.split(",") if p.strip()]


def _parse_fusao(s: str) -> tuple[list[str], int]:
    antigos, _, pos = s.partition("=")
    if not antigos or not pos:
        raise argparse.ArgumentTypeError(f"--fusao espera U:x:nnn+U:x:mmm=4 (recebeu {s!r})")
    return [a.strip() for a in antigos.split("+") if a.strip()], int(pos)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("antigo")
    ap.add_argument("novo")
    ap.add_argument("--saida", help="arquivo onde gravar o texto reconciliado (default: stdout)")
    ap.add_argument("--divisao", action="append", default=[], type=_parse_divisao, metavar="U:x:nnn=2,3")
    ap.add_argument("--fusao", action="append", default=[], type=_parse_fusao, metavar="U:x:nnn+U:x:mmm=4")
    args = ap.parse_args(argv)
    texto, rel = reconciliar(
        Path(args.antigo).read_text(encoding="utf-8"),
        Path(args.novo).read_text(encoding="utf-8"),
        divisoes=args.divisao,
        fusoes=args.fusao,
    )
    if args.saida:
        Path(args.saida).write_text(texto, encoding="utf-8")
    else:
        sys.stdout.write(texto)
    print(json.dumps(rel, ensure_ascii=False, indent=2), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
