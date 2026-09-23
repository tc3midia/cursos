"""Valida o lote publicado de Hardcopy Pro contra o acervo local.

Registro datado: vale para o layout até o commit 0f82fa8 (aula em pasta, com legenda.srt, segmentos.json e Metadados/).
Desde 22/09/2026 o repositório guarda só a transcrição e os materiais, em transcricoes/; este script não roda no checkout atual.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote

from transcrever import OUTPUT, SOURCE


ROOT = Path(__file__).resolve().parents[1]
PLANNED_LESSONS = 138


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def validate() -> dict:
    rows = [json.loads(line) for line in (ROOT / "manifest.jsonl").read_text(encoding="utf-8").splitlines()]
    assert 113 <= len(rows) <= PLANNED_LESSONS, f"manifesto: {len(rows)}"
    assert len({row["video"] for row in rows}) == len(rows), "vídeo duplicado no manifesto"
    assert len({row["arquivo"] for row in rows}) == len(rows), "texto duplicado no manifesto"
    state = json.loads((ROOT / "status.json").read_text(encoding="utf-8"))
    assert state["videos_complete"] == len(rows) and not state["errors"]
    assert state["selection_partial_course"] == (len(rows) < PLANNED_LESSONS)
    index = (ROOT / "00 - Índice geral.md").read_text(encoding="utf-8")
    index_targets = [unquote(link) for link in re.findall(r"\]\(([^)]+\.md)\)", index)]
    assert set(index_targets) == {row["arquivo"] for row in rows}, "links do índice divergentes"
    omitted = 0
    captions = 0
    for row in rows:
        video = SOURCE / row["video"]
        lesson = ROOT / row["arquivo"]
        folder = lesson.parent
        raw = json.loads((folder / "segmentos.json").read_text(encoding="utf-8"))
        metadata = json.loads((ROOT / row["grupo"] / "Metadados" / f"{video.stem}.json").read_text(encoding="utf-8"))
        original_metadata = json.loads(video.with_suffix(".json").read_text(encoding="utf-8"))
        assert metadata == original_metadata, f"metadados: {video}"
        assert video.stat().st_size == row["tamanho_bytes"] == raw["source_size_bytes"] == metadata["tamanho_bytes"]
        assert sha256(video) == row["sha256"] == raw["source_sha256"], f"hash: {video}"
        assert raw["source_relative_path"] == raw["video_recording_relative_path"] == row["video"]
        assert raw["timestamp_basis"] == "original_lesson_seconds" and raw["playback_speed"] == 2
        segments = raw["segments"]
        assert segments and all(0 <= s["start"] <= s["end"] for s in segments), f"tempos: {video}"
        assert all(a["start"] <= b["start"] for a, b in zip(segments, segments[1:])), f"ordem: {video}"
        text = lesson.read_text(encoding="utf-8")
        srt = (folder / "legenda.srt").read_text(encoding="utf-8")
        assert row["titulo"] in text and row["sha256"] in text
        blocks = re.split(r"\n\s*\n", srt.strip()) if srt.strip() else []
        assert all(re.match(r"^\d+\n\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}\n", block) for block in blocks), f"SRT: {video}"
        assert [int(block.splitlines()[0]) for block in blocks] == list(range(1, len(blocks) + 1)), f"numeração SRT: {video}"
        assert len(blocks) + raw["readable_artifacts_omitted"] == sum(bool(s["text"].strip()) for s in segments), f"segmentos: {video}"
        omitted += raw["readable_artifacts_omitted"]
        captions += len(blocks)
    assert len(list(ROOT.rglob("transcricao.md"))) == len(rows)
    assert len(list(ROOT.rglob("legenda.srt"))) == len(rows)
    assert len(list(ROOT.rglob("segmentos.json"))) == len(rows)
    assert len(list(ROOT.rglob("Metadados/*.json"))) == len(rows)
    support = list((ROOT / "Materiais").rglob("*.md"))
    assert len(support) == 1, f"apoios Markdown: {len(support)}"
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert ("seleção parcial" in readme) == state["selection_partial_course"]
    return {"aulas": len(rows), "legendas": len(rows), "segmentos_json": len(rows),
            "metadados": len(rows), "apoios_markdown": len(support),
            "blocos_srt": captions, "artefatos_evidentes_omitidos": omitted,
            "hashes_sha256_verificados": len(rows)}


if __name__ == "__main__":
    print(json.dumps(validate(), ensure_ascii=False))
