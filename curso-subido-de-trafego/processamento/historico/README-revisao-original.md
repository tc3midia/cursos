# Revisão v2 — Curso Subido

Ordem por artefato:

1. Inspetor (`papeis/inspetor.md`, contexto fresco, lê transcrição+PDF) → `laudos/<aula_id>.evidencia.md`.
2. Juiz (`papeis/juiz.md`, contexto fresco, **sem** transcrição) → `laudos/<aula_id>.md` ou
   `laudos/playbook-<tarefa>.md`.
3. `falha` e rodada < 2 → Redator (`papeis/redator.md`) corrige só o listado, `versao`+1, e volta ao 1.
4. Ouro `bloqueado` → Bravo 1.

Rubrica: `RUBRICA.md`. Amostra: `amostra.md`. Fixtures: `ferramentas/curso-subido/tests/calibracao/`. Avaliação de uso: `avaliacao/`.
Modelos por papel: extrator Sonnet 5 (Opus 5 em aulas > 8k palavras), consolidação/sintetizador/redator
Opus 5, inspetor Sonnet 5, juiz Fable 5.1 em subagente, ouros e fixtures Fable 5.1 na sessão.
`gerado_por` no front matter de todo artefato.

Isolamento: se o juiz viu transcrição ou PDF, o laudo é inválido e se refaz noutro contexto.
