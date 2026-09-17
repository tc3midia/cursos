"""Move as 54 aulas locais para sete módulos após a transcrição e cópia ao Drive."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import quote

from sincronizar_acervo import MODULES


SOURCE = Path(r"D:\Cursos\Formato Criativo de Conteúdo")
INDEX = SOURCE / "_README.md"
PATTERN = re.compile(r"^m([1-7])_a\d+_.+\.(?:mkv|md|json)$")


def main() -> None:
    files = [path for path in SOURCE.iterdir() if path.is_file() and PATTERN.match(path.name)]
    videos = [path for path in files if path.suffix == ".mkv"]
    if len(videos) != 54 or len(files) != 54 * 2 + 44 + 3:
        raise RuntimeError(f"Inventário inesperado: {len(videos)} vídeos, {len(files)} arquivos")
    if not INDEX.is_file():
        raise RuntimeError("Índice local ausente")
    content = INDEX.read_text(encoding="utf-8")
    replacements = 0
    for path in files:
        token = f"]({path.name})"
        if token in content:
            module = int(re.match(r"^m([1-7])_", path.name).group(1))
            rel = quote(MODULES[module - 1], safe="") + "/" + path.name
            content = content.replace(token, f"]({rel})")
            replacements += 1
    for path in files:
        module = int(re.match(r"^m([1-7])_", path.name).group(1))
        destination = SOURCE / MODULES[module - 1] / path.name
        if destination.exists():
            raise RuntimeError(f"Destino ocupado: {destination}")
    for path in files:
        module = int(re.match(r"^m([1-7])_", path.name).group(1))
        destination = SOURCE / MODULES[module - 1] / path.name
        destination.parent.mkdir(exist_ok=True)
        path.rename(destination)
    INDEX.write_text(content, encoding="utf-8")
    print(f"Arquivos movidos: {len(files)}; links atualizados: {replacements}")


if __name__ == "__main__":
    main()
