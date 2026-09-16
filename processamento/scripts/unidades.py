"""Biblioteca da base atômica do Curso Subido de Tráfego (v2). Stdlib only.

Implementa o que `FORMATO.md` e `taxonomia.md` descrevem: manifest, slugs, parser plano de YAML,
parser do arquivo de unidades, hash por unidade, citações, grupos e `insumos_hash`.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE_DEFAULT = ROOT / "conhecimento"
FERRAMENTA = ROOT / "processamento"
METODO = FERRAMENTA / "metodo"
CLONE_DEFAULT = Path(os.environ.get("CURSO_SUBIDO_CLONE", str(ROOT)))
FONTE_REPO = "tc3midia/curso-subido-trafego-transcricoes"
FONTE_COMMIT = "f188775"
ACCOUNT_ID = "account.86ajrj8n9"
PROMOTED_BY = "human.will"
PDFTOTEXT = shutil.which("pdftotext") or "/opt/homebrew/bin/pdftotext"

RE_ID = re.compile(r"U:([0-9a-f]{16}):(\d{3})")
RE_ID_FULL = re.compile(r"^U:([0-9a-f]{16}):(\d{3})$")
RE_GRUPO = re.compile(r"G:([a-z0-9-]+):(\d{3})")
RE_BLOCO = re.compile(r"^### (U:[0-9a-f]{16}:\d{3}) — (.+?)\s*$", re.M)
RE_GRUPO_HEAD = re.compile(r"^### (G:[a-z0-9-]+:\d{3}) — (.+?)\s*$", re.M)
RE_FAIXA = re.compile(r"^(\d{2}):(\d{2}):(\d{2})\s*[–-]\s*(\d{2}):(\d{2}):(\d{2})$")
RE_TIMESTAMP = re.compile(r"(\[\d{1,2}:|\b\d{1,2}:\d{2}(?::\d{2})?\b)")
RE_HOJE = re.compile(r"\b(hoje|atualmente|neste momento)\b", re.I)

# Slugs que a v1 encurtou à mão; a v2 preserva o nome do memo.
SLUG_OVERRIDES = {
    "b860f68ae836a8bf": "001-8-2-taxa-de-acao-estimada-objetivos-e-segmentacoes",
}

GERADO_POR = {"sonnet-5", "opus-5", "fable-5.1", "gpt-5.6-sol", "gpt-5.6-terra", "gpt-6-astra"}
STATUS_UNIDADES = {"rascunho", "validado", "revisado", "ouro"}
CONFIANCA = {"alta", "media", "baixa"}
TIPOS_SEM_TAREFA = {"conceito", "limite"}
CAMPOS_SEMANTICOS = ("tipo", "plataforma", "tema", "tarefas", "fonte", "faixa", "condicoes", "perecivel", "confianca")
ORDEM_META = ("tipo", "plataforma", "tema", "tarefas", "fonte", "faixa", "condicoes", "perecivel", "confianca", "versao", "nota", "proposta_tag")


# ----------------------------------------------------------------------------- manifest / clone


def diretorio_gerado(root: Path) -> Path:
    """Dados técnicos fora da biblioteca; bases avulsas continuam autocontidas."""
    return FERRAMENTA / "dados" if Path(root).resolve() == BASE_DEFAULT.resolve() else Path(root) / "_gerado"


def diretorio_revisao(root: Path, revisao: str = "revisao") -> Path:
    if Path(root).resolve() == BASE_DEFAULT.resolve() and revisao == "revisao":
        return FERRAMENTA / "revisao"
    return Path(root) / revisao


def diretorio_metodo(root: Path) -> Path:
    return METODO if Path(root).resolve() == BASE_DEFAULT.resolve() else Path(root) / "revisao"


def caminho_artefato(root: Path, relativo: str) -> Path:
    """Resolve os identificadores históricos sem alterar os selos existentes."""
    if relativo.startswith("_gerado/"):
        return diretorio_gerado(root) / relativo.removeprefix("_gerado/")
    if relativo.startswith("revisao/"):
        return diretorio_revisao(root) / relativo.removeprefix("revisao/")
    return Path(root) / relativo


def referencia_artefato(root: Path, path: Path) -> str:
    root, path = Path(root).resolve(), Path(path).resolve()
    if path.is_relative_to(root):
        return str(path.relative_to(root))
    return "revisao/" + str(path.relative_to(diretorio_revisao(root).resolve()))


def slugify(texto: str) -> str:
    s = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s


def load_manifest(clone: Path | None = None) -> dict[str, dict]:
    """aula_id -> linha do manifest, acrescida de `modulo3`, `slug`, `pasta`."""
    clone = Path(clone or CLONE_DEFAULT)
    rows = {}
    with open(clone / "manifest.jsonl", encoding="utf-8") as fh:
        for line in fh:
            if not line.strip():
                continue
            row = json.loads(line)
            m = re.match(r"Módulo (\d{3})", row["modulo"])
            row["modulo3"] = m.group(1)
            row["slug"] = SLUG_OVERRIDES.get(row["id"], f"{row['modulo3']}-{slugify(row['aula'])}")
            row["pasta"] = clone / row["saida_relativa"]
            rows[row["id"]] = row
    return rows


def clone_commit(clone: Path | None = None) -> str:
    clone = Path(clone or CLONE_DEFAULT)
    try:
        out = subprocess.run(["git", "-C", str(clone), "rev-parse", "--short=7", "HEAD"], capture_output=True, text=True, check=True)
        return out.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ""


def verificar_fontes(clone: Path | None = None) -> list[str]:
    """Confere os bytes da fonte f188775; novos commits de derivados não a invalidam."""
    clone = Path(clone or CLONE_DEFAULT)
    baseline = FERRAMENTA / "dados" / "fontes-originais.json"
    dados = json.loads(baseline.read_text(encoding="utf-8"))
    if dados.get("fonte_commit") != FONTE_COMMIT:
        return ["versão da referência de fontes incompatível"]
    erros = []
    for rel, esperado in dados["arquivos"].items():
        p = clone / rel
        if not p.is_file():
            erros.append(f"fonte ausente: {rel}")
        elif hashlib.sha256(p.read_bytes()).hexdigest() != esperado:
            erros.append(f"fonte alterada: {rel}")
    return erros


def pdftotext_disponivel() -> bool:
    return bool(PDFTOTEXT) and os.path.exists(PDFTOTEXT)


def fontes_no_disco(row: dict) -> list[str]:
    """Nomes de transcricao.md + PDFs + txt da pasta da aula (o que pode entrar em `fontes`)."""
    pasta = Path(row["pasta"])
    nomes = []
    for p in sorted(pasta.iterdir()):
        if p.name == "transcricao.md" or p.suffix.lower() in {".pdf", ".txt"}:
            nomes.append(p.name)
    return nomes


def texto_fonte(row: dict, nome: str) -> str:
    p = Path(row["pasta"]) / nome
    if p.suffix.lower() == ".pdf":
        out = subprocess.run([PDFTOTEXT, "-layout", str(p), "-"], capture_output=True, text=True)
        return out.stdout
    return p.read_text(encoding="utf-8", errors="replace")


def transcricao_sem_cabecalho(texto: str) -> str:
    _, body = parse_front_matter(texto)
    return body


# ----------------------------------------------------------------------------- YAML plano


def _escalar(v: str):
    v = v.strip()
    if v == "":
        return ""
    if v == "[]":
        return []
    if v.startswith("[") and v.endswith("]"):
        inner = v[1:-1].strip()
        return [] if not inner else [_escalar(x) for x in _split_virgulas(inner)]
    if (v[0] == '"' and v[-1] == '"') or (v[0] == "'" and v[-1] == "'"):
        return v[1:-1]
    if v in ("true", "True"):
        return True
    if v in ("false", "False"):
        return False
    if v in ("null", "~"):
        return None
    if re.fullmatch(r"-?\d+", v):
        return int(v)
    if re.fullmatch(r"-?\d+\.\d+", v):
        return float(v)
    return v


def _split_virgulas(s: str) -> list[str]:
    partes, atual, aspas = [], "", None
    for ch in s:
        if aspas:
            atual += ch
            if ch == aspas:
                aspas = None
        elif ch in "\"'":
            aspas = ch
            atual += ch
        elif ch == ",":
            partes.append(atual)
            atual = ""
        else:
            atual += ch
    if atual.strip():
        partes.append(atual)
    return partes


def parse_bloco_yaml(texto: str) -> dict:
    """Parser plano: `chave: valor`, listas inline `[a, b]`, listas em bloco `- x`, strings entre aspas."""
    dados: dict = {}
    chave_lista = None
    for raw in texto.splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw.lstrip().startswith("- ") and chave_lista is not None:
            item = raw.strip()[2:]
            dados[chave_lista].append(_escalar(item))
            continue
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):(.*)$", raw)
        if not m:
            raise ValueError(f"linha YAML inválida: {raw!r}")
        chave, resto = m.group(1), m.group(2)
        if resto.strip() == "":
            dados[chave] = []
            chave_lista = chave
        else:
            dados[chave] = _escalar(resto)
            chave_lista = None
    return dados


def parse_front_matter(texto: str) -> tuple[dict, str]:
    if not texto.startswith("---\n"):
        return {}, texto
    fim = texto.find("\n---", 4)
    if fim < 0:
        return {}, texto
    return parse_bloco_yaml(texto[4:fim]), texto[fim + 4 :].lstrip("\n")


def _yaml_escalar(v) -> str:
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    if isinstance(v, list):
        return "[" + ", ".join(_yaml_escalar(x) for x in v) + "]"
    if v is None:
        return "null"
    s = str(v)
    if s == "" or re.search(r'[:#"\[\]{}]', s) or s != s.strip() or s.lower() in {"true", "false", "null"}:
        return '"' + s.replace('"', '\\"') + '"'
    return s


# ----------------------------------------------------------------------------- unidades


@dataclass
class Unidade:
    id: str
    titulo: str
    meta: dict
    corpo: list[str]
    linha: int = 0

    @property
    def aula_id(self) -> str:
        return self.id.split(":")[1]

    @property
    def nnn(self) -> int:
        return int(self.id.split(":")[2])


@dataclass
class ArquivoUnidades:
    front: dict
    titulo: str
    contexto: list[str]
    unidades: list[Unidade]
    erros_parse: list[str] = field(default_factory=list)
    path: Path | None = None


def parse_arquivo_unidades(texto: str, path: Path | None = None) -> ArquivoUnidades:
    front, body = parse_front_matter(texto)
    erros: list[str] = []
    titulo = ""
    m = re.search(r"^# (.+)$", body, re.M)
    if m:
        titulo = m.group(1).strip()
    contexto: list[str] = []
    mc = re.search(r"^## Contexto da aula\s*$(.*?)^## Unidades\s*$", body, re.M | re.S)
    if mc:
        contexto = [l.strip() for l in mc.group(1).splitlines() if l.strip()]
    else:
        erros.append("seções `## Contexto da aula` e `## Unidades` ausentes ou fora de ordem")
    idx_unidades = body.find("## Unidades")
    corpo_unidades = body[idx_unidades:] if idx_unidades >= 0 else body
    offset_linha = texto[: texto.find(corpo_unidades)].count("\n") if corpo_unidades else 0
    heads = list(RE_BLOCO.finditer(corpo_unidades))
    unidades: list[Unidade] = []
    for i, h in enumerate(heads):
        fim = heads[i + 1].start() if i + 1 < len(heads) else len(corpo_unidades)
        bloco = corpo_unidades[h.end() : fim]
        my = re.match(r"\s*```yaml\n(.*?)\n```\n?(.*)$", bloco, re.S)
        if not my:
            erros.append(f"{h.group(1)}: bloco sem fence ```yaml```")
            continue
        try:
            meta = parse_bloco_yaml(my.group(1))
        except ValueError as exc:
            erros.append(f"{h.group(1)}: {exc}")
            continue
        corpo = [l.rstrip() for l in my.group(2).splitlines() if l.strip()]
        unidades.append(Unidade(h.group(1), h.group(2).strip(), meta, corpo, offset_linha + corpo_unidades[: h.start()].count("\n") + 1))
    return ArquivoUnidades(front, titulo, contexto, unidades, erros, path)


def serializar_unidade(u: Unidade) -> str:
    linhas = [f"### {u.id} — {u.titulo}", "```yaml"]
    chaves = [k for k in ORDEM_META if k in u.meta] + [k for k in u.meta if k not in ORDEM_META]
    for k in chaves:
        linhas.append(f"{k}: {_yaml_escalar(u.meta[k])}")
    linhas.append("```")
    linhas.extend(u.corpo)
    return "\n".join(linhas) + "\n\n"


def _span_bloco(texto: str, uid: str) -> tuple[int, int] | None:
    m = re.search(rf"^### {re.escape(uid)} — .*$", texto, re.M)
    if not m:
        return None
    prox = re.search(r"^### U:", texto[m.end() :], re.M)
    fim = m.end() + prox.start() if prox else len(texto)
    return m.start(), fim


def substituir_unidade(texto: str, u: Unidade) -> str:
    """Troca o bloco com o ID de `u` pela serialização de `u`; erro se o bloco não existe."""
    span = _span_bloco(texto, u.id)
    if span is None:
        raise KeyError(u.id)
    return texto[: span[0]] + serializar_unidade(u) + texto[span[1] :]


def remover_unidade(texto: str, uid: str) -> str:
    span = _span_bloco(texto, uid)
    if span is None:
        raise KeyError(uid)
    return texto[: span[0]] + texto[span[1] :]


def iter_unidades(root: Path):
    for p in sorted((Path(root) / "unidades").glob("*.md")):
        yield p, parse_arquivo_unidades(p.read_text(encoding="utf-8"), p)


def todas_unidades(root: Path) -> dict[str, Unidade]:
    out = {}
    for _, arq in iter_unidades(root):
        for u in arq.unidades:
            out[u.id] = u
    return out


def retiradas(root: Path) -> set[str]:
    out = set()
    for _, arq in iter_unidades(root):
        out.update(arq.front.get("retiradas") or [])
    return out


def _canon_corpo(corpo: list[str]) -> str:
    return "\n".join(re.sub(r"\s+", " ", l).strip() for l in corpo)


def hash_unidade(u: Unidade) -> str:
    partes = [u.id]
    for k in CAMPOS_SEMANTICOS:
        v = u.meta.get(k)
        if isinstance(v, list):
            v = sorted(str(x) for x in v)
        partes.append(f"{k}={json.dumps(v, ensure_ascii=False, sort_keys=True)}")
    partes.append(_canon_corpo(u.corpo))
    return hashlib.sha256("\n".join(partes).encode("utf-8")).hexdigest()


def hash_corpo(u: Unidade) -> str:
    return hashlib.sha256(_canon_corpo(u.corpo).encode("utf-8")).hexdigest()


def parse_faixa(s: str) -> tuple[int, int] | None:
    m = RE_FAIXA.match(str(s).strip())
    if not m:
        return None
    a = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + int(m.group(3))
    b = int(m.group(4)) * 3600 + int(m.group(5)) * 60 + int(m.group(6))
    return a, b


# ----------------------------------------------------------------------------- taxonomia


@dataclass
class Taxonomia:
    plataformas: list[str]
    temas: list[str]
    tarefas: dict[str, dict]
    tipos: list[str]
    definicoes: dict[str, str]


def load_taxonomia(path: Path) -> Taxonomia:
    texto = Path(path).read_text(encoding="utf-8")
    secoes: dict[str, str] = {}
    atual = None
    for line in texto.splitlines():
        m = re.match(r"^## (.+)$", line)
        if m:
            atual = m.group(1).strip()
            secoes[atual] = ""
        elif atual:
            secoes[atual] += line + "\n"
    definicoes: dict[str, str] = {}

    def bullets(nome):
        out = []
        for m in re.finditer(r"^- `([a-z0-9-]+)` — (.+)$", secoes.get(nome, ""), re.M):
            out.append(m.group(1))
            definicoes[m.group(1)] = m.group(2).strip()
        return out

    tarefas: dict[str, dict] = {}
    for line in secoes.get("Tarefas", "").splitlines():
        m = re.match(r"^\| `([a-z0-9-]+)` \| ([a-z]+) \| ([a-z0-9, -]+) \| (.+?) \|$", line)
        if m:
            tarefas[m.group(1)] = {
                "grupo": m.group(2),
                "plataformas": [p.strip() for p in m.group(3).split(",") if p.strip()],
                "definicao": m.group(4).strip(),
            }
            definicoes[m.group(1)] = m.group(4).strip()
    return Taxonomia(bullets("Plataformas"), bullets("Temas"), tarefas, bullets("Tipos"), definicoes)


# ----------------------------------------------------------------------------- citações / grupos / hashes


def find_citacoes(texto: str) -> list[str]:
    return [f"U:{a}:{b}" for a, b in RE_ID.findall(texto)]


def find_citacoes_grupos(texto: str) -> list[str]:
    return [f"G:{a}:{b}" for a, b in RE_GRUPO.findall(texto)]


@dataclass
class Grupo:
    id: str
    titulo: str
    meta: dict
    resolucao: list[str]


def parse_grupos(texto: str) -> tuple[dict, list[Grupo], list[str]]:
    front, body = parse_front_matter(texto)
    heads = list(RE_GRUPO_HEAD.finditer(body))
    grupos, erros = [], []
    for i, h in enumerate(heads):
        fim = heads[i + 1].start() if i + 1 < len(heads) else len(body)
        bloco = body[h.end() : fim]
        my = re.match(r"\s*```yaml\n(.*?)\n```\n?(.*)$", bloco, re.S)
        if not my:
            erros.append(f"{h.group(1)}: bloco sem fence ```yaml```")
            continue
        try:
            meta = parse_bloco_yaml(my.group(1))
        except ValueError as exc:
            erros.append(f"{h.group(1)}: {exc}")
            continue
        grupos.append(Grupo(h.group(1), h.group(2).strip(), meta, [l.strip() for l in my.group(2).splitlines() if l.strip()]))
    return front, grupos, erros


def hash_grupo(g: Grupo) -> str:
    partes = [g.id, json.dumps({k: g.meta.get(k) for k in ("tipo", "unidades", "canonica", "evidencia")}, sort_keys=True, ensure_ascii=False), _canon_corpo(g.resolucao)]
    return hashlib.sha256("\n".join(partes).encode("utf-8")).hexdigest()


def todos_grupos(root: Path) -> dict[str, Grupo]:
    out = {}
    pasta = Path(root) / "consolidacao"
    if pasta.exists():
        for p in sorted(pasta.glob("*.md")):
            _, grupos, _ = parse_grupos(p.read_text(encoding="utf-8"))
            for g in grupos:
                out[g.id] = g
    return out


def sha256_file(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def insumos_hash(pares_unidades: dict[str, str], pares_grupos: dict[str, str], formato_hash: str, taxonomia_hash: str) -> str:
    linhas = [f"{k}\t{v}" for k, v in pares_unidades.items()] + [f"{k}\t{v}" for k, v in pares_grupos.items()]
    linhas.sort()
    linhas.append(f"FORMATO\t{formato_hash}")
    linhas.append(f"TAXONOMIA\t{taxonomia_hash}")
    return hashlib.sha256("\n".join(linhas).encode("utf-8")).hexdigest()


def substituir_campo_front(texto: str, campo: str, valor: str) -> str:
    """Troca (ou insere) `campo: valor` no front matter, sem tocar no corpo."""
    if not texto.startswith("---\n"):
        return texto
    fim = texto.find("\n---", 4)
    head, resto = texto[4:fim], texto[fim:]
    if re.search(rf"^{campo}:.*$", head, re.M):
        head = re.sub(rf"^{campo}:.*$", f"{campo}: {valor}", head, count=1, flags=re.M)
    else:
        head = head + f"\n{campo}: {valor}"
    return "---\n" + head + resto


def ler_jsonl(path: Path) -> list[dict]:
    p = Path(path)
    if not p.exists():
        return []
    return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
