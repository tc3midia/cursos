# Calibração negativa

Fixtures com defeito conhecido, nomes neutros (`f1`…`f4`) para não vazar o defeito ao inspetor nem ao
juiz. O que cada uma tem e o veredito esperado ficam **só** em `esperado.jsonl` (lido pelo teste
`test_curso_subido_v2_revisao.py`). Inspetor e juiz não leem este README nem `esperado.jsonl`; recebem
a fixture como se fosse um artefato real. Ficam fora de `biblioteca/` e nunca entram no pacote do extrator.

Front matter da fixture: `type: fixture-calibracao`, `fixture: fN`, `type_original` (tipo do artefato copiado).
Laudo em `laudos/fixture-fN.md` (nesta pasta). Se um juiz aprovar uma fixture, a causa está na rubrica ou no papel
do juiz; corrige-se a causa, nunca se afrouxa a régua. Casos de calibração da consolidação (etapa 2)
entram em `consolidacao.md` quando a etapa começar.

## Registro 2026-09-14

As fixtures `f1`–`f3` foram julgadas (rodada 0) sobre cópias do ouro 8.3 **anteriores** às correções
das rodadas 1–2 do ouro; por isso os laudos delas também apontam defeitos reais do ouro daquela
versão (U:038, U:043, faixas de U:007/U:025). Depois que o ouro foi corrigido, as fixtures foram
regeneradas a partir da versão corrigida com os mesmos defeitos plantados, para que o teste de
"cópia com diferenças localizadas" continue válido. Os laudos `fixture-fN.md` não foram refeitos:
o veto esperado foi apanhado em todas, que é o que a calibração mede.
