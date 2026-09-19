"""Transcrição local e retomável das gravações completas do Hardcopy Pro."""

from __future__ import annotations

import ctypes
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

import torch
import whisper


SOURCE = Path(r"D:\Cursos\Hardcopy Pro")
OUTPUT = Path(r"D:\Cursos\Hardcopy Pro - Transcrições")
MODEL = "large-v3-turbo"
SETTINGS = {"model": MODEL, "language": "pt", "beam_size": 5, "temperature": 0,
            "condition_on_previous_text": False,
            "initial_prompt": "Hardcopy Pro. Copywriting. Hard Ads. Hard Sounds. Inteligência Artificial."}


def atomic_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + ".tmp")
    temp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(temp, path)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def inventory() -> list[dict]:
    items = []
    for video in SOURCE.rglob("*.mkv"):
        relative = video.relative_to(SOURCE)
        if any(part.startswith("_") for part in relative.parts):
            continue
        meta_path = video.with_suffix(".json")
        if not meta_path.is_file():
            raise ValueError(f"Metadado ausente: {meta_path}")
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        if meta.get("curso") != "Hardcopy Pro" or meta.get("arquivo") != video.name:
            raise ValueError(f"Identidade divergente: {video}")
        if meta.get("tamanho_bytes") != video.stat().st_size:
            raise ValueError(f"Tamanho divergente: {video}")
        if meta.get("velocidade_reproducao") != "2x":
            raise ValueError(f"Velocidade não reconhecida: {video}")
        items.append({"video": video, "relative": relative, "meta": meta})
    items.sort(key=lambda x: x["relative"].as_posix())
    if not items:
        raise ValueError("Nenhuma aula completa encontrada")
    return items


def raw_path(item: dict) -> Path:
    return OUTPUT / "_dados" / item["relative"].with_suffix(".json")


def valid(item: dict) -> bool:
    path = raw_path(item)
    if not path.is_file():
        return False
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
        return (raw["settings"] == SETTINGS and raw["source_sha256"] == sha256(item["video"])
                and raw["source_size_bytes"] == item["video"].stat().st_size
                and isinstance(raw["segments"], list))
    except (KeyError, ValueError, TypeError):
        return False


def status(items: list[dict], done: set[str], errors: list[str]) -> None:
    total_seconds = sum(int(item["meta"].get("duracao_gravacao_segundos", 0) or 0) * 2 for item in items)
    atomic_json(OUTPUT / "status.json", {
        "updated_at_utc": datetime.now(timezone.utc).isoformat(),
        "settings": SETTINGS, "videos_total": len(items), "videos_complete": len(done),
        "original_hours_approx": round(total_seconds / 3600, 2), "errors": errors,
    })


def main() -> int:
    if not torch.cuda.is_available():
        raise RuntimeError("CUDA indisponível; sem fallback para CPU")
    items = inventory()
    done = {item["relative"].as_posix() for item in items if valid(item)}
    errors: list[str] = []
    status(items, done, errors)
    print(f"GPU: {torch.cuda.get_device_name(0)}; modelo: {MODEL}; pendentes: {len(items)-len(done)}/{len(items)}", flush=True)
    ctypes.windll.kernel32.SetThreadExecutionState(0x80000000 | 0x00000001)
    try:
        model = whisper.load_model(MODEL, device="cuda")
        for index, item in enumerate(items, 1):
            relative = item["relative"].as_posix()
            if relative in done:
                continue
            started = time.monotonic()
            print(f"[{index}/{len(items)}] Início: {relative}", flush=True)
            try:
                source_hash = sha256(item["video"])
                with tempfile.TemporaryDirectory(dir=OUTPUT) as temp_dir:
                    wav = Path(temp_dir) / "audio.wav"
                    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-i", str(item["video"]),
                                    "-vn", "-af", "atempo=0.5", "-ac", "1", "-ar", "16000",
                                    "-y", str(wav)], check=True)
                    result = model.transcribe(str(wav), language="pt", task="transcribe", fp16=True,
                                              beam_size=5, temperature=0, condition_on_previous_text=False,
                                              initial_prompt=SETTINGS["initial_prompt"], verbose=None)
                atomic_json(raw_path(item), {
                    "settings": SETTINGS, "source_relative_path": relative,
                    "source_sha256": source_hash, "source_size_bytes": item["video"].stat().st_size,
                    "playback_speed": 2, "timestamp_basis": "original_lesson_seconds",
                    "transcribed_at_utc": datetime.now(timezone.utc).isoformat(),
                    "language_detected": result["language"],
                    "segments": [{"start": seg["start"], "end": seg["end"], "text": seg["text"]}
                                 for seg in result["segments"]],
                })
                done.add(relative)
                print(f"[{index}/{len(items)}] Concluído em {time.monotonic()-started:.1f}s", flush=True)
            except Exception as exc:
                errors.append(f"{relative}: {type(exc).__name__}: {exc}")
                print(f"ERRO: {errors[-1]}", file=sys.stderr, flush=True)
            status(items, done, errors)
    finally:
        ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
