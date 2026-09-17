"""Transcrição local retomável do Formato Criativo de Conteúdo."""

from __future__ import annotations

import ctypes
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

import torch
import whisper


SOURCE = Path(r"D:\Cursos\Formato Criativo de Conteúdo")
OUTPUT = Path(r"D:\Cursos\Formato Criativo de Conteúdo - Transcrições")
MODEL = "large-v3-turbo"
SETTINGS = {"model": MODEL, "language": "pt", "beam_size": 5, "temperature": 0,
            "condition_on_previous_text": False,
            "initial_prompt": "Hanah e Alef. Formato Criativo de Conteúdo. SOFIA. AIDA."}
LESSON = re.compile(r"^m(\d+)_a(\d+)_(.+)\.mkv$")


def atomic_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(tmp, path)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def inventory() -> list[dict]:
    items = []
    for video in SOURCE.rglob("*.mkv"):
        if any(part.startswith("_") for part in video.relative_to(SOURCE).parts[:-1]):
            continue
        match = LESSON.match(video.name)
        if not match:
            raise ValueError(f"Vídeo sem identidade de aula: {video}")
        meta_path = video.with_name(video.name + ".json")
        if not meta_path.is_file():
            raise ValueError(f"Metadado ausente: {meta_path}")
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        expected_bytes = meta.get("bytes")
        if expected_bytes is not None and expected_bytes != video.stat().st_size and video.name != "m1_a1_boas_vindas.mkv":
            raise ValueError(f"Tamanho divergente: {video}")
        speed = int(meta.get("playbackSpeed") or 1)
        if speed not in (1, 2):
            raise ValueError(f"Velocidade não reconhecida: {video}")
        module, lesson = int(match[1]), int(match[2])
        items.append({"video": video, "meta": meta, "speed": speed,
                      "module": module, "lesson": lesson, "slug": match[3]})
    items.sort(key=lambda x: (x["module"], x["lesson"]))
    if len(items) != 54 or len({(x["module"], x["lesson"]) for x in items}) != len(items):
        raise ValueError(f"Inventário inesperado: {len(items)} vídeos")
    return items


def raw_path(item: dict) -> Path:
    return OUTPUT / "_dados" / f"m{item['module']}_a{item['lesson']}_{item['slug']}.json"


def valid(item: dict) -> bool:
    path = raw_path(item)
    if not path.is_file():
        return False
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return (data["source_sha256"] == sha256(item["video"])
                and data["settings"] == SETTINGS
                and data["playback_speed"] == item["speed"]
                and isinstance(data["segments"], list))
    except (KeyError, ValueError, TypeError):
        return False


def status(items: list[dict], done: set[str], errors: list[str]) -> None:
    atomic_json(OUTPUT / "status.json", {
        "updated_at_utc": datetime.now(timezone.utc).isoformat(),
        "settings": SETTINGS, "videos_total": len(items), "videos_complete": len(done),
        "errors": errors,
    })


def main() -> int:
    if not torch.cuda.is_available():
        raise RuntimeError("CUDA indisponível; sem fallback para CPU")
    items = inventory()
    done = {x["video"].name for x in items if valid(x)}
    errors: list[str] = []
    status(items, done, errors)
    print(f"GPU: {torch.cuda.get_device_name(0)}; {len(items) - len(done)} vídeos pendentes", flush=True)
    ctypes.windll.kernel32.SetThreadExecutionState(0x80000000 | 0x00000001)
    try:
        model = whisper.load_model(MODEL, device="cuda")
        for index, item in enumerate(items, 1):
            video = item["video"]
            if video.name in done:
                continue
            started = time.monotonic()
            print(f"[{index}/{len(items)}] Início: {video.name}", flush=True)
            try:
                video_hash = sha256(video)
                with tempfile.TemporaryDirectory(dir=OUTPUT) as tmp_dir:
                    wav = Path(tmp_dir) / "audio.wav"
                    command = ["ffmpeg", "-nostdin", "-v", "error", "-i", str(video),
                               "-vn", "-af", f"atempo={1 / item['speed']}",
                               "-ac", "1", "-ar", "16000", "-y", str(wav)]
                    subprocess.run(command, check=True)
                    result = model.transcribe(str(wav), language="pt", task="transcribe",
                                              fp16=True, beam_size=5, temperature=0,
                                              condition_on_previous_text=False,
                                              initial_prompt=SETTINGS["initial_prompt"], verbose=None)
                atomic_json(raw_path(item), {
                    "settings": SETTINGS, "source_video": video.name,
                    "source_sha256": video_hash, "source_size_bytes": video.stat().st_size,
                    "playback_speed": item["speed"],
                    "timestamp_basis": "original_lesson_seconds",
                    "transcribed_at_utc": datetime.now(timezone.utc).isoformat(),
                    "language_detected": result["language"],
                    "segments": [{"start": s["start"], "end": s["end"], "text": s["text"]}
                                 for s in result["segments"]],
                })
                done.add(video.name)
                print(f"[{index}/{len(items)}] Concluído em {time.monotonic() - started:.1f}s", flush=True)
            except Exception as exc:
                errors.append(f"{video.name}: {type(exc).__name__}: {exc}")
                print(f"ERRO: {errors[-1]}", file=sys.stderr, flush=True)
            status(items, done, errors)
    finally:
        ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
