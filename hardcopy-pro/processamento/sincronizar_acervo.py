"""Gera a edição consultável das aulas já gravadas do Hardcopy Pro."""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path
from urllib.parse import quote

from transcrever import OUTPUT, SOURCE, SETTINGS, raw_path


REPO = Path(__file__).resolve().parents[1]
TRANSCRICOES = REPO / "transcricoes"  # desde 22/09/2026: um <aula>.md por aula; legenda, segmentos e metadados ficam só no acervo local. Rodar de novo reescreve o cabeçalho das transcrições e o README do curso.
DRIVE = "https://drive.google.com/drive/folders/1VmaxCRxWBsvGZ2xVyzc0WxQCfBlPM6js"
PLANNED_LESSONS = 138


def stamp(seconds: float, *, srt: bool = False) -> str:
    millis = max(0, round(seconds * 1000))
    hours, millis = divmod(millis, 3_600_000)
    minutes, millis = divmod(millis, 60_000)
    secs, millis = divmod(millis, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}{',' if srt else '.'}{millis:03d}"


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def is_transcription_artifact(content: str) -> bool:
    """Drop clear silence artifacts from readable text, retaining the raw segments."""
    if not re.search(r"\w", content, flags=re.UNICODE):
        return True
    words = re.findall(r"\w+", content.casefold(), flags=re.UNICODE)
    return len(words) >= 5 and len(set(words)) == 1


def trim_repetition_prefix(content: str) -> tuple[str, bool]:
    """Remove an unmistakable repeated word before otherwise usable speech."""
    match = re.match(r"^\s*(\w+)(?:[\s,.!?;:]+\1){7,}[\s,.!?;:]*(.*)$",
                     content, flags=re.IGNORECASE | re.UNICODE)
    if match and match.group(2).strip():
        return match.group(2).strip(), True
    return content, False


def transcribed_inventory() -> list[dict]:
    """Use the completed transcription snapshot while recording may continue."""
    items = []
    for path in (OUTPUT / "_dados").rglob("*.json"):
        relative = path.relative_to(OUTPUT / "_dados").with_suffix(".mkv")
        video = SOURCE / relative
        metadata_path = video.with_suffix(".json")
        if not video.is_file() or not metadata_path.is_file():
            raise RuntimeError(f"Fonte de transcrição ausente: {relative}")
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        if (metadata.get("curso") != "Hardcopy Pro"
                or metadata.get("arquivo") != video.name
                or metadata.get("tamanho_bytes") != video.stat().st_size
                or metadata.get("velocidade_reproducao") != "2x"):
            raise RuntimeError(f"Metadados divergentes: {relative}")
        items.append({"video": video, "relative": relative, "meta": metadata})
    return sorted(items, key=lambda item: item["relative"].as_posix())


def main() -> None:
    items = transcribed_inventory()
    state = json.loads((OUTPUT / "status.json").read_text(encoding="utf-8"))
    if (state["videos_complete"] != len(items)
            or state["videos_total"] != len(items) or state["errors"]):
        raise RuntimeError(f"Transcrição incompleta: {state['videos_complete']}/{state['videos_total']}; arquivos={len(items)}; erros={state['errors']}")
    if len(items) > PLANNED_LESSONS:
        raise RuntimeError(f"Mais gravações que as {PLANNED_LESSONS} aulas inventariadas: {len(items)}")
    partial = len(items) < PLANNED_LESSONS
    index = ["# Hardcopy Pro — índice das transcrições", "",
             f"{len(items)} gravações completas disponíveis no acervo em 19/09/2026. Transcrição automática em português pelo Whisper `large-v3-turbo` na GPU; não revisada integralmente contra o áudio.",
             ("O módulo 0 a 100K ainda está incompleto na origem local. " if partial else
              "As 138 aulas previstas no índice local estão gravadas. ") +
             "Tentativas e trechos parciais não entram na contagem de aulas.", ""]
    manifest = []
    previous_group = None
    for item in items:
        video = item["video"]
        relative = item["relative"]
        raw = json.loads(raw_path(item).read_text(encoding="utf-8"))
        if (raw["settings"] != SETTINGS or raw["source_size_bytes"] != video.stat().st_size
                or raw["source_relative_path"] != relative.as_posix()):
            raise RuntimeError(f"Transcrição divergente: {relative}")
        metadata = item["meta"]
        title = metadata["titulo"]
        group = relative.parent
        page_path = TRANSCRICOES / group / f"{video.stem}.md"
        page_path.parent.mkdir(parents=True, exist_ok=True)
        lines = [f"# {title}", "",
                 "Transcrição automática por Whisper `large-v3-turbo` em GPU, em português. Não revisada integralmente contra o áudio.",
                 "Artefatos inequívocos de silêncio (pontuação solta ou uma palavra repetida) foram omitidos do texto; os segmentos brutos do Whisper ficam no acervo local, fora do repositório.",
                 f"Grupo: {group.as_posix()}. [Acervo no Drive]({DRIVE}).",
                 f"Vídeo: `{video.name}`. Duração original: {metadata['duracao_original']}. SHA-256: `{raw['source_sha256']}`.",
                 "A gravação ocorreu em 2×. Os tempos abaixo seguem a aula original.", ""]
        omitted_artifacts = 0
        trimmed_prefixes = 0
        for segment in raw["segments"]:
            content = segment["text"].strip()
            if not content:
                continue
            if is_transcription_artifact(content):
                omitted_artifacts += 1
                continue
            content, trimmed = trim_repetition_prefix(content)
            trimmed_prefixes += int(trimmed)
            lines.extend([f"[{stamp(segment['start'])}–{stamp(segment['end'])}] {content}", ""])
        write(page_path, "\n".join(lines).rstrip() + "\n")
        if group != previous_group:
            index.extend([f"## {group.as_posix()}", ""])
            previous_group = group
        target = page_path.relative_to(TRANSCRICOES).as_posix()
        index.append(f"- [{title}]({quote(target, safe='/')})")
        manifest.append({"grupo": group.as_posix(), "titulo": title, "video": relative.as_posix(),
                         "arquivo": target, "origem": metadata["origem"],
                         "duracao_original": metadata["duracao_original"],
                         "tamanho_bytes": video.stat().st_size, "sha256": raw["source_sha256"],
                         "velocidade_gravacao": 2, "modelo": SETTINGS["model"]})
    for support in SOURCE.rglob("*.md"):
        if support.name == "_README.md" or any(part.startswith("_") for part in support.relative_to(SOURCE).parts):
            continue
        target = TRANSCRICOES / "Materiais" / support.relative_to(SOURCE)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(support, target)
    write(TRANSCRICOES / "00 - Índice geral.md", "\n".join(index).rstrip() + "\n")
    write(TRANSCRICOES / "manifest.jsonl", "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in manifest))
    coverage = ("O módulo 0 a 100K ainda não foi gravado por inteiro; o curso publicado aqui é uma seleção parcial. "
                if partial else "As 138 aulas previstas no índice local estão gravadas e transcritas. ")
    write(REPO / "README.md", "# Hardcopy Pro — transcrições\n\n"
          f"[Índice das {len(items)} aulas disponíveis](transcricoes/00%20-%20%C3%8Dndice%20geral.md) · [manifesto](transcricoes/manifest.jsonl) · [vídeos no Drive]({DRIVE})\n\n"
          "As transcrições foram geradas das gravações completas existentes em 19/09/2026, uma por aula em `transcricoes/`, nas pastas de trilha e grupo do curso; o material avulso fica em `transcricoes/Materiais/`. "
          + coverage +
          "Os textos automáticos não tiveram revisão integral contra o áudio; artefatos inequívocos de silêncio foram omitidos do texto. "
          "Os vídeos aguardam revisão audiovisual integral.\n")
    print(json.dumps({"videos": len(items), "manifest": len(manifest)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
