"""Publica textos e metadados no repositório privado depois de 54 transcrições completas."""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path
from urllib.parse import quote

from transcrever import OUTPUT, SOURCE, SETTINGS, inventory, raw_path


REPO = Path(__file__).resolve().parents[1]
TRANSCRICOES = REPO / "transcricoes"  # desde 22/09/2026: um <aula>.md por aula; legenda, segmentos e metadados ficam só no acervo local. Rodar de novo reescreve o cabeçalho das transcrições e o README do curso.
MODULES = (
    "Módulo 01 - O método Formato Criativo de Conteúdo",
    "Módulo 02 - Formatos validados para copiar e colar",
    "Módulo 03 - Roteiro Simplificado",
    "Módulo 04 - Bastidores de Gravação",
    "Módulo 05 - Autenticidade com estratégia",
    "Módulo 06 - Vender sem ser chato",
    "Módulo 07 - Introdução à profissão Criador Estrategista",
)
DRIVE = "https://drive.google.com/drive/folders/1gyNrgFt6oDIlLWYqTkJ3mz2GFdR_H-ht"


def timestamp(seconds: float, *, srt: bool = False) -> str:
    milliseconds = max(0, round(seconds * 1000))
    hours, rem = divmod(milliseconds, 3_600_000)
    minutes, rem = divmod(rem, 60_000)
    secs, millis = divmod(rem, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}{',' if srt else '.'}{millis:03d}"


def title(item: dict) -> str:
    meta = item["meta"]
    value = meta.get("title") or meta.get("lesson")
    if isinstance(value, str):
        value = re.sub(r"^\d+\.\s*", "", value).strip()
    return value or item["slug"].replace("_", " ").capitalize()


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> None:
    items = inventory()
    status = json.loads((OUTPUT / "status.json").read_text(encoding="utf-8"))
    if status["videos_complete"] != 54 or status["errors"]:
        raise RuntimeError(f"Transcrição incompleta: {status['videos_complete']}/54, erros={status['errors']}")
    index = ["# Formato Criativo de Conteúdo — índice de transcrições", "",
             "54 aulas em sete módulos. Transcrição automática em português pelo Whisper `large-v3-turbo` na GPU; texto ainda não revisado integralmente contra o áudio.", ""]
    manifest = []
    current_module = None
    for item in items:
        video = item["video"]
        raw = json.loads(raw_path(item).read_text(encoding="utf-8"))
        if raw["settings"] != SETTINGS or raw["source_size_bytes"] != video.stat().st_size:
            raise RuntimeError(f"Transcrição divergente: {video}")
        module = MODULES[item["module"] - 1]
        page_path = TRANSCRICOES / module / f"{video.stem}.md"
        page_path.parent.mkdir(parents=True, exist_ok=True)
        course_title = title(item)
        source_seconds = item["meta"].get("sourceDurationSeconds")
        page = [f"# {course_title}", "",
                "Transcrição automática por Whisper `large-v3-turbo` em GPU, em português. Não revisada integralmente contra o áudio.",
                f"{module}. [Curso no Drive]({DRIVE}).",
                f"Vídeo: `{video.name}`. SHA-256: `{raw['source_sha256']}`.",
                f"Velocidade da gravação: {item['speed']}×. Os tempos abaixo seguem a aula original.", ""]
        omitted = []
        for segment in raw["segments"]:
            content = segment["text"].strip()
            if not content:
                continue
            if re.fullmatch(r"(?:AIDA\.\s*){8,}", content, flags=re.IGNORECASE):
                omitted.append({"start": segment["start"], "end": segment["end"],
                                "reason": "repetição espúria do prompt inicial; texto automático omitido"})
                continue
            page.extend([f"[{timestamp(segment['start'])}–{timestamp(segment['end'])}] {content}", ""])
        if omitted:
            page[6:6] = ["Um trecho inicial teve saída automática repetitiva omitida; o áudio desse trecho ainda precisa de revisão humana.", ""]
        write(page_path, "\n".join(page).rstrip() + "\n")
        support = video.with_suffix(".md")
        if support.is_file():
            material_dir = TRANSCRICOES / module / "Materiais"
            material_dir.mkdir(exist_ok=True)
            shutil.copy2(support, material_dir / support.name)
        if item["module"] != current_module:
            index.extend([f"## {module}", ""])
            current_module = item["module"]
        rel = page_path.relative_to(TRANSCRICOES).as_posix()
        index.append(f"- [Aula {item['lesson']}: {course_title}]({quote(rel, safe='/')})")
        manifest.append({
            "modulo": module, "aula": item["lesson"], "titulo": course_title,
            "video": f"{module}/{video.name}", "arquivo": rel,
            "duracao_original_segundos": source_seconds,
            "tamanho_bytes": video.stat().st_size, "sha256": raw["source_sha256"],
            "velocidade_gravacao": item["speed"], "modelo": SETTINGS["model"],
        })
    write(TRANSCRICOES / "00 - Índice geral.md", "\n".join(index).rstrip() + "\n")
    write(TRANSCRICOES / "manifest.jsonl", "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in manifest))
    write(REPO / "README.md", "# Formato Criativo de Conteúdo — transcrições\n\n"
          "[Índice das 54 aulas](transcricoes/00%20-%20%C3%8Dndice%20geral.md) · [manifesto](transcricoes/manifest.jsonl) · "
          f"[vídeos e apoios no Drive]({DRIVE})\n\n"
          "Sete módulos em `transcricoes/`, com um arquivo por aula e os materiais de apoio em `Materiais/`. "
          "O manifesto liga cada texto ao vídeo por tamanho e SHA-256. "
          "Whisper `large-v3-turbo` em GPU; transcrições automáticas ainda sem revisão integral contra o áudio. "
          "O acervo de vídeo também aguarda revisão audiovisual integral. "
          "Na aula 1 do módulo 1, o tamanho do MKV difere em 37.056 bytes do JSON histórico; "
          "o manifesto registra o tamanho e o SHA-256 do arquivo atual. "
          "O PDF de apoio da aula 9 do módulo 2 repete a aula 8, conforme anotado no respectivo Markdown.\n")
    print(json.dumps({"videos": len(items), "modules": len(MODULES), "manifest": len(manifest)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
