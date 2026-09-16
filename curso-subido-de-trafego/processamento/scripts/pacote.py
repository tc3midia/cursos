#!/usr/bin/env python3
"""Monta o pacote de contexto para um subagente (extração, reextração, correção, inspeção, tarefa, plataforma, tema, órfãs).

    python3 processamento/scripts/pacote.py extracao <aula_id|slug> [--gerado-por MODELO] [--saida DIR]
    python3 processamento/scripts/pacote.py reextracao <aula_id|slug> [--gerado-por MODELO] [--saida DIR]
    python3 processamento/scripts/pacote.py correcao <aula_id|slug> --unidades U:x:007,U:x:021 --erros "<texto>" [--saida DIR]
    python3 processamento/scripts/pacote.py inspecao <aula_id|slug> [--saida DIR]
    python3 processamento/scripts/pacote.py tarefa <tarefa> [--saida DIR]
    python3 processamento/scripts/pacote.py plataforma <plataforma> [--saida DIR]
    python3 processamento/scripts/pacote.py tema <tema> [--saida DIR]
    python3 processamento/scripts/pacote.py orfas [--saida DIR]
    python3 processamento/scripts/pacote.py pendentes [--modulo 00X]

Sem `--saida`, imprime em stdout. Pacote dentro do repositório só em `_saida/**/temporarios/`.
`extracao|reextracao --saida` imprime `<caminho> <total> palavras (aula: <n>)`; `<n>` conta só
transcrição e PDFs em texto e é o que decide o modelo do extrator. `correcao|inspecao --saida`
imprime `<caminho> <total> palavras`. `pendentes` imprime `modulo<TAB>aula_id<TAB>slug<TAB>palavras`
das aulas sem arquivo em `unidades/`.

Pacotes por papel: extração e reextração levam FORMATO §1 a §4 (não o arquivo inteiro), taxonomia
e âncora do ouro; correção leva só o papel, FORMATO §1 a §4, o front matter, os blocos apontados,
a janela da transcrição de cada faixa (60 s de folga) e os PDFs citados na `fonte`; inspeção leva o
papel do inspetor, RUBRICA, FORMATO §8, o arquivo da aula e as fontes. Nunca inclui memos v1 nem
`historico/`.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import unidades as lib  # noqa: E402

OURO_SLUG = "001-8-3-anuncios-a-alma-do-seu-trafego-pago"
PLAYBOOK_OURO = "diagnosticar-concentracao-de-verba"
FOLGA_JANELA = 60  # segundos de folga para cada lado da faixa na correção
RE_SEGMENTO = re.compile(r"(\*\*\[(\d\d:\d\d:\d\d)[–-](\d\d:\d\d:\d\d)\]\*\*)")


def formato_secoes(root: Path, inicio: str, fim: str | None) -> str:
    """Trecho de FORMATO.md sem front matter, de `inicio` (inclusive) até `fim` (exclusive) ou o final."""
    _, corpo = lib.parse_front_matter((root / "FORMATO.md").read_text(encoding="utf-8"))
    trecho = corpo.split(inicio, 1)
    if len(trecho) < 2:
        raise SystemExit(f"FORMATO.md sem a seção `{inicio}`")
    texto = inicio + trecho[1]
    if fim:
        texto = texto.split(fim, 1)[0]
    return texto.rstrip() + "\n"


def formato_1_a_4(root: Path) -> str:
    return formato_secoes(root, "## 1.", "## 5.")


def formato_8(root: Path) -> str:
    return formato_secoes(root, "## 8.", None)


def janela_transcricao(texto: str, faixa: str, folga: int = FOLGA_JANELA) -> str:
    """Segmentos `**[hh:mm:ss–hh:mm:ss]**` da transcrição que tocam a faixa, com folga para cada lado."""
    fx = lib.parse_faixa(faixa)
    if fx is None:
        raise SystemExit(f"faixa `{faixa}` fora do formato hh:mm:ss–hh:mm:ss")
    a, b = fx[0] - folga, fx[1] + folga
    partes = RE_SEGMENTO.split(texto)
    out = []
    # split com 3 grupos devolve: [antes, marca, ini, fim, corpo, marca, ini, fim, corpo, ...]
    for i in range(1, len(partes), 4):
        marca, ini, fim, corpo = partes[i], partes[i + 1], partes[i + 2], partes[i + 3]
        seg = lib.parse_faixa(f"{ini}–{fim}")
        if seg and seg[1] >= a and seg[0] <= b:
            out.append(marca + corpo)
    return "".join(out).strip() + "\n"


def _row(manifest: dict, chave: str) -> dict:
    if chave in manifest:
        return manifest[chave]
    for r in manifest.values():
        if r["slug"] == chave:
            return r
    raise SystemExit(f"aula `{chave}` não encontrada no manifest")


def cabecalho(row: dict, fontes: list[str], gerado_por: str = "sonnet-5") -> str:
    linhas = [
        "---",
        "type: unidades-aula",
        "status: rascunho",
        f'title: "{row["aula"]}"',
        f'modulo: "{row["modulo3"]}"',
        f"ordem: {row['ordem']}",
        f"aula_id: {row['id']}",
        f"account_id: {lib.ACCOUNT_ID}",
        f"promoted_by: {lib.PROMOTED_BY}",
        f"fonte_repo: {lib.FONTE_REPO}",
        f"fonte_commit: {lib.FONTE_COMMIT}",
        "fontes:",
    ]
    linhas.extend(f"  - {f}" for f in fontes)
    linhas.extend([f"extraido_em: {dt.date.today().isoformat()}", f"gerado_por: {gerado_por}", "retiradas: []", "divisoes: []", "fusoes: []", "---", "", f"# {row['aula']}", "", "## Contexto da aula", "", "## Unidades", ""])
    return "\n".join(linhas)


def ancora_ouro(root: Path, n: int = 6) -> str:
    p = root / "unidades" / f"{OURO_SLUG}.md"
    if not p.exists():
        return "(ouro ainda não existe)"
    arq = lib.parse_arquivo_unidades(p.read_text(encoding="utf-8"))
    vistos: set[str] = set()
    escolhidas = []
    for u in arq.unidades:
        t = u.meta.get("tipo")
        if t not in vistos:
            vistos.add(t)
            escolhidas.append(u)
        if len(escolhidas) >= n:
            break
    return "".join(lib.serializar_unidade(u) for u in escolhidas)


def _textos_fonte(row: dict) -> list[tuple[str, str]]:
    """Textos da aula como entram no pacote: transcrição sem cabeçalho e PDFs em texto."""
    out = []
    for nome in lib.fontes_no_disco(row):
        t = lib.texto_fonte(row, nome)
        if nome == "transcricao.md":
            t = lib.transcricao_sem_cabecalho(t)
        out.append((nome, t))
    return out


def palavras_aula(row: dict) -> int:
    """Palavras só da parte da aula (transcrição e PDFs em texto), sem papel, FORMATO, taxonomia e âncora."""
    return sum(len(t.split()) for _, t in _textos_fonte(row))


def pendentes(root: Path, modulo: str | None = None) -> list[dict]:
    """Aulas do manifest sem arquivo em unidades/, com contagem de palavras da transcrição."""
    root = Path(root)
    feitos = {p.stem for p in (root / "unidades").glob("*.md")}
    out = []
    for row in sorted(lib.load_manifest().values(), key=lambda r: (r["modulo3"], r["ordem"])):
        if modulo and row["modulo3"] != modulo:
            continue
        if row["slug"] in feitos:
            continue
        palavras = len(lib.texto_fonte(row, "transcricao.md").split())
        out.append({"modulo": row["modulo3"], "aula_id": row["id"], "slug": row["slug"], "palavras": palavras})
    return out


def pacote_extracao(root: Path, chave: str, reextracao: bool = False, gerado_por: str = "sonnet-5") -> str:
    manifest = lib.load_manifest()
    row = _row(manifest, chave)
    fontes = lib.fontes_no_disco(row)
    partes = []
    partes.append(f"# PACOTE DE {'REEXTRAÇÃO' if reextracao else 'EXTRAÇÃO'} — {row['slug']}\n")
    partes.append(f"Arquivo de saída: `unidades/{row['slug']}.md`. Duração da aula: {row['duracao_segundos']:.0f} s. Palavras: {len(lib.texto_fonte(row, 'transcricao.md').split())}.\n")
    partes.append("## Papel\n\n" + (lib.diretorio_metodo(root) / "papeis" / "extrator.md").read_text(encoding="utf-8"))
    partes.append("## FORMATO.md §1 a §4 (arquivo, bloco, identidade, hash e versão)\n\n" + formato_1_a_4(root))
    partes.append("## taxonomia.md\n\n" + (root / "taxonomia.md").read_text(encoding="utf-8"))
    partes.append("## Âncora de granularidade (unidades do ouro)\n\n" + ancora_ouro(root))
    if reextracao:
        p = root / "unidades" / f"{row['slug']}.md"
        if p.exists():
            arq = lib.parse_arquivo_unidades(p.read_text(encoding="utf-8"))
            partes.append("## Unidades existentes (preserve o ID quando for a mesma unidade; novos números após o maior; retiradas/divisoes/fusoes no front matter)\n")
            partes.append(f"Retiradas já registradas: {arq.front.get('retiradas')}\n")
            partes.append("".join(f"- {u.id} — {u.titulo}\n  " + " / ".join(u.corpo) + "\n" for u in arq.unidades))
    partes.append("## Cabeçalho pré-preenchido (copie; ajuste `fontes` se ignorar algum PDF, registrando em `fontes_ignoradas`)\n\n```markdown\n" + cabecalho(row, fontes, gerado_por=gerado_por) + "```\n")
    for nome, t in _textos_fonte(row):
        partes.append(f"## FONTE: {nome}\n\n{t}\n")
    return "\n\n".join(partes)


def faixa_para_janela(unidades: list[lib.Unidade], uid: str, ignorar_propria: bool = False) -> str | None:
    """Faixa que delimita a janela da transcrição de uma unidade. Sem `faixa` própria, vai do início da
    faixa da unidade anterior (na ordem do arquivo) ao fim da faixa da seguinte, para o corretor achar o trecho."""
    idx = next((i for i, u in enumerate(unidades) if u.id == uid), None)
    if idx is None:
        return None
    propria = unidades[idx].meta.get("faixa")
    if propria and not ignorar_propria:
        return str(propria)
    antes = next((str(u.meta["faixa"]) for u in reversed(unidades[:idx]) if u.meta.get("faixa")), None)
    depois = next((str(u.meta["faixa"]) for u in unidades[idx + 1 :] if u.meta.get("faixa")), None)
    if not antes and not depois:
        return None
    a = lib.parse_faixa(antes)[0] if antes else lib.parse_faixa(depois)[0]
    b = lib.parse_faixa(depois)[1] if depois else lib.parse_faixa(antes)[1]
    fmt = lambda t: f"{t // 3600:02d}:{t % 3600 // 60:02d}:{t % 60:02d}"
    return f"{fmt(a)}–{fmt(b)}"


def _fontes_citadas(unidades: list[lib.Unidade]) -> list[str]:
    """Nomes de PDF/txt citados em `fonte` (pdf:x, txt:x, fala+pdf:x, fala+txt:x), sem repetição."""
    out: list[str] = []
    for u in unidades:
        fonte = str(u.meta.get("fonte", ""))
        if ":" in fonte:
            nome = fonte.split(":", 1)[1]
            if nome and nome not in out:
                out.append(nome)
    return out


def pacote_correcao(root: Path, chave: str, unidades: list[str], erros: str) -> str:
    """Correção pontual: papel, FORMATO §1 a §4, front matter, blocos apontados, janela da transcrição por faixa, PDFs citados, erros."""
    manifest = lib.load_manifest()
    row = _row(manifest, chave)
    p = root / "unidades" / f"{row['slug']}.md"
    if not p.exists():
        raise SystemExit(f"correção exige o arquivo `unidades/{row['slug']}.md`")
    texto_arquivo = p.read_text(encoding="utf-8")
    arq = lib.parse_arquivo_unidades(texto_arquivo)
    por_id = {u.id: u for u in arq.unidades}
    faltam = [uid for uid in unidades if uid not in por_id]
    if faltam:
        raise SystemExit(f"unidades não encontradas em `{p.name}`: {', '.join(faltam)}")
    alvos = [por_id[uid] for uid in unidades]
    front_raw = "---" + texto_arquivo.split("---", 2)[1] + "---"
    partes = [f"# PACOTE DE CORREÇÃO — {row['slug']}\n"]
    partes.append(
        f"Arquivo: `unidades/{row['slug']}.md`. Corrija só as unidades listadas em `## Unidades a corrigir`, editando os blocos "
        f"no lugar (mesmo ID, mesma posição). Toda unidade alterada sobe `versao`. Não renumere, não crie nem retire unidades, "
        f"não toque nas outras unidades nem no front matter. Não abra nenhum outro arquivo.\n"
    )
    partes.append("## Papel\n\n" + (lib.diretorio_metodo(root) / "papeis" / "extrator.md").read_text(encoding="utf-8"))
    partes.append("## FORMATO.md §1 a §4 (arquivo, bloco, identidade, hash e versão)\n\n" + formato_1_a_4(root))
    partes.append("## Front matter atual\n\n```yaml\n" + front_raw + "\n```\n")
    partes.append(f"## Unidades a corrigir ({len(alvos)})\n\n" + "".join(lib.serializar_unidade(u) for u in alvos))
    transcricao = None
    for u in alvos:
        propria = u.meta.get("faixa")
        faixa = faixa_para_janela(arq.unidades, u.id)
        if not faixa or not (propria or str(u.meta.get("fonte", "")).startswith("fala")):
            continue
        if transcricao is None:
            transcricao = lib.transcricao_sem_cabecalho(lib.texto_fonte(row, "transcricao.md"))
        origem = f"faixa {faixa}" if propria else f"sem faixa; janela pelas unidades vizinhas, {faixa}"
        partes.append(f"## Trecho da transcrição para {u.id} ({origem}, folga {FOLGA_JANELA} s)\n\n" + janela_transcricao(transcricao, faixa))
    fontes_disco = lib.fontes_no_disco(row)
    for nome in _fontes_citadas(alvos):
        if nome in fontes_disco:
            partes.append(f"## FONTE: {nome}\n\n{lib.texto_fonte(row, nome)}\n")
    partes.append("## Erros do validador\n\n" + erros.strip() + "\n")
    return "\n\n".join(partes)


def pacote_inspecao(root: Path, chave: str) -> str:
    """Inspeção: papel do inspetor, RUBRICA, FORMATO §8, arquivo da aula e fontes (transcrição sem cabeçalho, PDFs em texto)."""
    manifest = lib.load_manifest()
    row = _row(manifest, chave)
    p = root / "unidades" / f"{row['slug']}.md"
    if not p.exists():
        raise SystemExit(f"inspeção exige o arquivo `unidades/{row['slug']}.md`")
    partes = [f"# PACOTE DE INSPEÇÃO — {row['slug']}\n"]
    destino = lib.diretorio_revisao(root) / "laudos" / f"{row['id']}.evidencia.md"
    partes.append(f"Arquivo de saída (caminho físico): `{destino.resolve()}`. Identificador lógico: `revisao/laudos/{row['id']}.evidencia.md`. Artefato sob inspeção: `unidades/{row['slug']}.md`. Fonte bruta: as seções `FONTE:` deste pacote. Não abra nenhum outro arquivo.\n")
    partes.append("## Papel\n\n" + (lib.diretorio_metodo(root) / "papeis" / "inspetor.md").read_text(encoding="utf-8"))
    partes.append("## RUBRICA.md\n\n" + (lib.diretorio_metodo(root) / "RUBRICA.md").read_text(encoding="utf-8"))
    partes.append("## FORMATO.md §8\n\n" + formato_8(root))
    partes.append(f"## Artefato sob inspeção: unidades/{row['slug']}.md\n\n" + p.read_text(encoding="utf-8"))
    for nome, t in _textos_fonte(row):
        partes.append(f"## FONTE: {nome}\n\n{t}\n")
    return "\n\n".join(partes)


def _unidades_filtradas(root: Path, pred):
    out = []
    for path, arq in lib.iter_unidades(root):
        for u in arq.unidades:
            if pred(u):
                out.append((path.stem, arq, u))
    return out

def _render_unidades(itens) -> str:
    linhas = []
    slug_atual = None
    for slug, arq, u in itens:
        if slug != slug_atual:
            linhas.append(f"\n### Aula {slug} — {arq.front.get('title')}\n")
            slug_atual = slug
        linhas.append(lib.serializar_unidade(u))
    return "".join(linhas)


def _grupos_para(root: Path, ids: set[str]) -> str:
    out = []
    for gid, g in lib.todos_grupos(root).items():
        if set(g.meta.get("unidades") or []) & ids:
            out.append(f"### {gid} — {g.titulo}\n" + "\n".join(f"{k}: {g.meta[k]}" for k in ("tipo", "unidades", "canonica", "evidencia") if k in g.meta) + "\n" + "\n".join(g.resolucao) + "\n")
    return "\n".join(out) or "(nenhum grupo)\n"


def pacote_tarefa(root: Path, tarefa: str) -> str:
    tax = lib.load_taxonomia(root / "taxonomia.md")
    if tarefa not in tax.tarefas:
        raise SystemExit(f"tarefa `{tarefa}` fora da taxonomia")
    itens = _unidades_filtradas(root, lambda u: tarefa in (u.meta.get("tarefas") or []))
    ids = {u.id for _, _, u in itens}
    temas = {u.meta.get("tema") for _, _, u in itens}
    limites = _unidades_filtradas(root, lambda u: u.meta.get("tipo") == "limite" and u.meta.get("tema") in temas)
    partes = [f"# PACOTE DE PLAYBOOK — {tarefa}\n", f"Arquivo de saída: `visoes/playbooks/{tarefa}.md`. Plataformas esperadas na matriz: {', '.join(tax.tarefas[tarefa]['plataformas'])}. Definição: {tax.tarefas[tarefa]['definicao']}.\n"]
    partes.append("## Papel\n\n" + (lib.diretorio_metodo(root) / "papeis" / "sintetizador.md").read_text(encoding="utf-8"))
    partes.append("## FORMATO.md §6\n\n" + (root / "FORMATO.md").read_text(encoding="utf-8").split("## 6. Visões e consolidação", 1)[-1].split("## 7.", 1)[0])
    ouro = root / "visoes" / "playbooks" / f"{PLAYBOOK_OURO}.md"
    if ouro.exists() and tarefa != PLAYBOOK_OURO:
        partes.append("## Playbook ouro (âncora de forma)\n\n" + ouro.read_text(encoding="utf-8"))
    partes.append(f"## Unidades da tarefa ({len(itens)})\n" + _render_unidades(itens))
    partes.append("## Grupos da consolidação\n\n" + _grupos_para(root, ids))
    partes.append(f"## Unidades `limite` dos temas envolvidos ({len(limites)})\n" + _render_unidades(limites))
    return "\n\n".join(partes)


def pacote_plataforma(root: Path, plataforma: str) -> str:
    tax = lib.load_taxonomia(root / "taxonomia.md")
    if plataforma not in tax.plataformas:
        raise SystemExit(f"plataforma `{plataforma}` fora da taxonomia")
    tipos = {"regua", "regra", "decisao", "alerta-ui"}
    itens = _unidades_filtradas(root, lambda u: u.meta.get("tipo") in tipos and (plataforma in (u.meta.get("plataforma") or []) or "geral" in (u.meta.get("plataforma") or [])))
    partes = [f"# PACOTE DE CHECKLIST — {plataforma}\n", f"Arquivo de saída: `visoes/checklists/{plataforma}.md`.\n"]
    partes.append("## Papel\n\n" + (lib.diretorio_metodo(root) / "papeis" / "sintetizador.md").read_text(encoding="utf-8"))
    partes.append("## FORMATO.md §6.2\n\nPerguntas de auditoria em bullets; cada bullet cita ≥1 `U:` de tipo regua/regra/decisao/alerta-ui; `geral` entra em todas.\n")
    partes.append(f"## Unidades ({len(itens)})\n" + _render_unidades(itens))
    partes.append("## Grupos da consolidação\n\n" + _grupos_para(root, {u.id for _, _, u in itens}))
    return "\n\n".join(partes)


def pacote_tema(root: Path, tema: str) -> str:
    tax = lib.load_taxonomia(root / "taxonomia.md")
    if tema not in tax.temas:
        raise SystemExit(f"tema `{tema}` fora da taxonomia")
    itens = _unidades_filtradas(root, lambda u: u.meta.get("tema") == tema)
    partes = [f"# PACOTE DE CONSOLIDAÇÃO — {tema}\n", f"Arquivo de saída: `consolidacao/{tema}.md`.\n"]
    partes.append("## FORMATO.md §6.6\n\n" + (root / "FORMATO.md").read_text(encoding="utf-8").split("### 6.6 Consolidação", 1)[-1].split("## 7.", 1)[0])
    cand = lib.diretorio_gerado(root) / "candidatos_consolidacao.md"
    if cand.exists():
        partes.append("## Candidatos (pares por similaridade)\n\n" + cand.read_text(encoding="utf-8"))
    partes.append(f"## Unidades do tema ({len(itens)})\n" + _render_unidades(itens))
    return "\n\n".join(partes)


def pacote_orfas(root: Path) -> str:
    import validate_visoes as vv

    ids = set(vv.orfas(root))
    itens = _unidades_filtradas(root, lambda u: u.id in ids)
    partes = ["# PACOTE DE ÓRFÃS\n", "Arquivo de saída: `visoes/orfas.md` (tabela `| id | motivo |`, motivos da lista fechada em FORMATO.md §6.4).\n"]
    partes.append("## Papel\n\n" + (lib.diretorio_metodo(root) / "papeis" / "sintetizador.md").read_text(encoding="utf-8"))
    partes.append(f"## Unidades não citadas ({len(itens)})\n" + _render_unidades(itens))
    return "\n\n".join(partes)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("modo", choices=["extracao", "reextracao", "correcao", "inspecao", "tarefa", "plataforma", "tema", "orfas", "pendentes"])
    ap.add_argument("chave", nargs="?")
    ap.add_argument("--root", default=str(lib.BASE_DEFAULT))
    ap.add_argument("--saida", help="diretório onde gravar o pacote (fora do repo ou em _saida/**/temporarios/)")
    ap.add_argument("--modulo", help="filtro de módulo (3 dígitos) para `pendentes`")
    ap.add_argument("--unidades", help="`correcao`: IDs U:<aula_id>:<nnn> separados por vírgula")
    ap.add_argument("--erros", help="`correcao`: texto dos erros do validador")
    ap.add_argument("--gerado-por", choices=sorted(lib.GERADO_POR), help="`extracao|reextracao`: autoria do cabeçalho (default: sonnet-5)")
    args = ap.parse_args(argv)
    root = Path(args.root)
    aula: int | None = None
    if args.gerado_por is not None and args.modo not in ("extracao", "reextracao"):
        raise SystemExit("`--gerado-por` só pode ser usado em `extracao` ou `reextracao`")
    if args.modo == "pendentes":
        for r in pendentes(root, modulo=args.modulo):
            print(f"{r['modulo']}\t{r['aula_id']}\t{r['slug']}\t{r['palavras']}")
        return 0
    if args.modo in ("extracao", "reextracao"):
        row = _row(lib.load_manifest(), args.chave)
        texto = pacote_extracao(root, args.chave, reextracao=args.modo == "reextracao", gerado_por=args.gerado_por or "sonnet-5")
        nome = f"{args.modo}-{row['slug']}.md"
        aula = palavras_aula(row)
    elif args.modo == "correcao":
        if not args.unidades or args.erros is None:
            raise SystemExit("`correcao` exige --unidades e --erros")
        row = _row(lib.load_manifest(), args.chave)
        ids = [x.strip() for x in args.unidades.split(",") if x.strip()]
        texto, nome = pacote_correcao(root, args.chave, unidades=ids, erros=args.erros), f"correcao-{row['slug']}.md"
    elif args.modo == "inspecao":
        row = _row(lib.load_manifest(), args.chave)
        texto, nome = pacote_inspecao(root, args.chave), f"inspecao-{row['slug']}.md"
    elif args.modo == "tarefa":
        texto, nome = pacote_tarefa(root, args.chave), f"tarefa-{args.chave}.md"
    elif args.modo == "plataforma":
        texto, nome = pacote_plataforma(root, args.chave), f"plataforma-{args.chave}.md"
    elif args.modo == "tema":
        texto, nome = pacote_tema(root, args.chave), f"tema-{args.chave}.md"
    else:
        texto, nome = pacote_orfas(root), "orfas.md"
    if args.saida:
        saida = Path(args.saida).resolve()
        dentro = lib.ROOT.resolve() in saida.parents or saida == lib.ROOT.resolve()
        if dentro and "temporarios" not in saida.relative_to(lib.ROOT.resolve()).parts:
            raise SystemExit("pacote dentro do repositório só em _saida/<negocio>/<trabalho>/temporarios/")
        saida.mkdir(parents=True, exist_ok=True)
        (saida / nome).write_text(texto, encoding="utf-8")
        total = len(texto.split())
        print(saida / nome, f"{total} palavras" + (f" (aula: {aula})" if aula is not None else ""))
    else:
        print(texto)
    return 0


if __name__ == "__main__":
    sys.exit(main())
