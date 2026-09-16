# Amostra — S0 (calibração) e revisão final (S8)

## S0 — calibração (2026-09-13)

| artefato | papel | laudo |
|---|---|---|
| `unidades/001-8-3-anuncios-a-alma-do-seu-trafego-pago.md` (ouro) | inspetor → juiz | `laudos/1674fc3d8d94c601.md` |
| `unidades/005-4-0-minha-campanha-esta-gastando-toda-verba-em-um-unico-grupo-de-anuncio-e-agora.md` (ouro) | inspetor → juiz | `laudos/869445a4c64befbf.md` |
| `visoes/playbooks/diagnosticar-concentracao-de-verba.md` (piloto) | juiz | `laudos/playbook-diagnosticar-concentracao-de-verba.md` |
| `ferramentas/curso-subido/tests/calibracao/f1.md` | inspetor → juiz | `ferramentas/curso-subido/tests/calibracao/laudos/fixture-f1.md` |
| `ferramentas/curso-subido/tests/calibracao/f2.md` | inspetor → juiz | `ferramentas/curso-subido/tests/calibracao/laudos/fixture-f2.md` |
| `ferramentas/curso-subido/tests/calibracao/f3.md` | inspetor → juiz | `ferramentas/curso-subido/tests/calibracao/laudos/fixture-f3.md` |
| `ferramentas/curso-subido/tests/calibracao/f4.md` | juiz | `ferramentas/curso-subido/tests/calibracao/laudos/fixture-f4.md` |

Aceite: ouros e piloto `passa`; as quatro fixtures `falha` pelo veto esperado.

Trilha de rodadas (laudos arquivados como `<nome>.rodada-N.md`):

| artefato | r0 | r1 | r2 | r3 |
|---|---|---|---|---|
| ouro 8.3 | bloqueado (fidelidade: U:038 desfecho inventado) | bloqueado (fidelidade: U:043 frase sem lastro) | ver laudo vivo | — |
| ouro 005-4.0 | passa | passa (após retag `plataforma: [youtube]` e U:017) | — | — |
| playbook piloto | falha (aplicabilidade: subseção `google`) | falha (aplicabilidade: réguas citando decisao/exemplo/procedimento) | bloqueado (aplicabilidade: `google-display` vs etiqueta `google` nas unidades; causa no ouro) | passa (após correção da causa no ouro 005) |
| f1 | falha [fidelidade] ✓ | | | |
| f2 | falha [fidelidade, cobertura] ✓ | | | |
| f3 | falha [fidelidade, perecibilidade] ✓ | | | |
| f4 | falha [aplicabilidade] ✓ | | | |

O piloto ultrapassou o teto de 2 rodadas porque a terceira foi aberta pelo ciclo de correção
(unidade do ouro mudou ⇒ derivado revisto ⇒ juiz de novo), não pelo redator. Decisão de manter
esse tratamento cabe a Bravo 1 no CP1.

CP1 aprovado por Will em 2026-09-14; o tratamento da rodada 3 do piloto foi ratificado.

## S8 — revisão final

Definida no início da etapa 4: 2 ouros + 2 aulas por módulo escolhidas por hash (menor e maior
`aula_id`), excluindo as já revisadas na etapa 1 (18 arquivos) + 6 playbooks (1 por plataforma real,
maior nº de citações) + 2 checklists (`meta`, `google-search`).
