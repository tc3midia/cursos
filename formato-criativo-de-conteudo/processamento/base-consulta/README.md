# Processamento da base de conhecimento — Formato Criativo de Conteúdo

Estado em 20/09/2026: **biblioteca fechada.** 54 de 54 aulas publicadas, 831 unidades, validador com zero erros e 1 aviso. Todas as 54 aulas passaram por inspeção integral com fonte e por julgamento sem fonte, e estão aprovadas. O detalhe está em "Fechamento" e nos lotes abaixo.

Finalidade: tornar o curso consultável por agentes, como matéria-prima para skills e agentes da TC3. O leitor final é um agente. Voz textual, playbooks e checklists ficam fora desta etapa.

## Fontes

- Repositório `tc3midia/cursos`, commit de referência `aaff8b6daa998403849b9edf5393c023c30db8de`. Desde 22/09/2026 a referência é `42c88f61e5fe385bc2d190cc9a9c853addf3e653`, que só moveu as aulas para `transcricoes/` (um arquivo por aula, mesmo conteúdo); legenda e segmentos saíram do repositório e deixaram de ser conferidos.
- 54 aulas, 7 módulos (6, 10, 11, 10, 7, 8, 2), 160.297 palavras de transcrição. 43 aulas com material de apoio utilizável.
- `python3 processamento/base_fcc.py --inventory` confere contagem, títulos e compara cada transcrição, legenda, segmentos e material com o objeto Git do commit de referência. Em 19/09/2026: zero divergências. Os hashes ficam em `conhecimento/manifest.json` quando a base é gerada.

Limitações das fontes, registradas e não corrigidas:

1. Transcrição automática (Whisper `large-v3-turbo`), sem revisão integral contra o áudio. Nomes de criadores variam entre fala e material e dentro da mesma aula.
2. `M01_A01`: o MKV difere em 37.056 bytes do JSON histórico; o manifesto registra tamanho e SHA-256 do arquivo atual. Não afeta o texto.
3. `M02_A09`: o PDF de apoio repete o da aula 8. O material fica fora do pacote e entra em `fontes_ignoradas` com o motivo.
4. Módulos 6 e 7 não têm material de apoio.
5. Em todas as 54 aulas a transcrição termina depois da duração do manifesto (de 6 s a 249 s; o maior é `M02_A07`, que tem ocorrência de carregamento anotada nos metadados). É cauda do Whisper: legenda fantasma e repetição em laço. O FORMATO proíbe extrair desses trechos.
6. Conteúdo visual que a fala só aponta não existe na fonte. Vira `limite` na aula.

## Papéis e via

| Papel | Modelo | Esforço | Recebe |
|---|---|---|---|
| Coordenação | Fable 5.1 (sessão do Claude Code) | — | plano, inventário, resultados. Não escreve unidades |
| Extrator | `claude-sonnet-5` | `high` | bloco fixo + uma aula |
| Reparo de contrato | `claude-sonnet-5` | `high` | erros do validador + unidades afetadas + aula |
| Inspetor | `claude-sonnet-5` | `xhigh` | bloco fixo + aula + unidades, em execução separada |
| Redator de correções | `claude-opus-5` | `high` | falhas consolidadas + unidades afetadas + aula |
| Juiz | `claude-fable-5-1` | `xhigh` | unidades + evidência do inspetor + validador + rubrica. Sem transcrição, material ou clone |

Via: **assinatura do Claude Code**, `claude -p` headless, um processo isolado por chamada, em diretório vazio, sem ferramentas e sem configurações do usuário. Decisão de Will em 19/09/2026. Não há Batch API nesta via. O cache de prefixo funciona com o bloco fixo no system prompt e foi conferido por `cache_read_input_tokens`.

Cada chamada grava `<AULA>.<papel>.execucao.json` com modelo pedido e usado, esforço, via, início e fim, os quatro contadores de token, tokens de raciocínio, `stop_reason`, `terminal_reason`, custo nominal, hash do pacote e do resultado.

## Arquivos

- `../../conhecimento/FORMATO.md`, `../../conhecimento/taxonomia.md` — contrato e enums deste curso.
- `RUBRICA.md` — cinco vetos, gravidade, teto de dois ciclos.
- `papeis/` — papel de cada modelo e exemplos de granularidade (de outro domínio, de propósito).
- `piloto/PLANO.md` e `piloto/RESULTADO.md` — o que foi fixado antes e o que o piloto mostrou.
- `amostra.json` — aulas que vão a julgamento, fixadas antes da extração.
- `calibracao/` — casos com erro plantado, gabarito e laudos.
- `revisao/inspecao/`, `revisao/julgamento/` — laudos publicados, um por aula, ligados por hash ao JSON da aula. `revisao/ouro-M03_A06/` guarda os dois ciclos de correção da ouro.
- `lotes/` — pastas de trabalho de cada lote, com as versões intermediárias. `execucoes/` — registro de cada chamada de modelo das aulas publicadas.

## Comandos

Da raiz do repositório, Python 3, só biblioteca padrão:

```sh
python3 processamento/base_fcc.py --inventory
python3 -m unittest processamento/tests/test_base_fcc.py
python3 processamento/base_fcc.py --file <saida-temporaria>/<AULA>.json
python3 processamento/base_fcc.py --partial --reviews --write
python3 processamento/base_fcc.py --reviews --check
python3 processamento/fcc_executar.py extrair --aulas M01_A01 M01_A02 --modelo claude-sonnet-5 --esforco high --rotulo lote-m01 --saida <pasta-temporaria>
python3 processamento/fcc_relatorio.py <pasta>
```

`--partial` confere só o que existe e nunca serve como prova de conclusão.

## Alcance da revisão

Regra confirmada por Will em 19/09/2026: inspeção com fonte em todas as aulas; julgamento nas 16 aulas de `amostra.json` (2 ouro + 2 por módulo por ordem de `aula_id`); aula fora da amostra entra no julgamento como conferência adicional quando a inspeção aponta falha material ou perecível sem marca. Teto de dois ciclos de correção por artefato.

Ajuste da coordenação em 20/09/2026, registrado em `piloto/PLANO.md`: a conferência adicional passou a ser acionada por qualquer `desvio` ou `sem-lastro` do inspetor, mesmo classificado como menor, porque gravidade é decisão do juiz. O ajuste nasceu de `M01_A01` e se confirmou em `M02_A09` e `M02_A10`: as duas tinham só apontamentos "menores" e foram reprovadas pelo juiz por fidelidade.

### Lote 1 — módulo 1 e aulas ouro, fechado em 19/09/2026

| Aula | Unidades | Inspeção com fonte | Julgamento | Correção | Status |
|---|---:|---|---|---|---|
| `M01_A01` | 8 | integral, 0 material, 6 menores | fora da amostra, não julgada | — | validado |
| `M01_A02` | 13 | integral, 1 material (sigla CDF inventada) | amostra: falha → **passa** | 1 reparo de contrato + ciclo 1 (U3), conferência focal | revisado |
| `M01_A03` | 11 | integral, 0 material, 1 perecível sem marca | conferência adicional: falha → **passa** | ciclo 1 (U4, U10), conferência focal | revisado |
| `M01_A04` | 9 | integral, 0 material, 2 menores | fora da amostra, não julgada | — | validado |
| `M01_A05` | 10 | integral, 0 material, 2 perecíveis sem marca | conferência adicional: falha → **passa** | ciclo 1 (U3, U4, U7, U9), conferência focal | revisado |
| `M01_A06` | 2 | integral, sem apontamento | amostra: **passa** de primeira | — | revisado |
| `M03_A06` ouro | 18 | integral duas vezes + focal | falha → falha → **passa** | ciclo 1 (U12, U17) e ciclo 2 (U3, U8, U12, U18), por decisão de Will | ouro |
| `M05_A02` ouro | 21 | integral | **passa** de primeira | — | ouro |

O que isso significa e o que não significa:

- As 92 unidades passaram por inspeção com fonte. 75 estão em aulas julgadas e aprovadas; 17 (`M01_A01`, `M01_A04`) têm só validação de script e inspeção, sem julgamento.
- Conferência focal quer dizer: depois da correção, o inspetor conferiu só as unidades alteradas e a lista de falhas; as intactas mantiveram a evidência da inspeção integral anterior, com hash de unidade conferido como igual.
- `M03_A06` chegou ao teto de dois ciclos e passou no segundo. O primeiro rejulgamento foi feito sobre reinspeção integral, que reabriu a aula inteira e achou uma divergência fala × material que a primeira inspeção não tinha apontado. A partir dali a conferência passou a ser focal, como a rubrica manda.
- `M05_A02` foi julgada antes dos ajustes de contrato feitos na calibração (regra de perecível por plataforma, vocabulário do curso). Revalidada por script no contrato atual: zero erros. Não foi rejulgada.
- Ajustes menores registrados nos julgamentos (5 a 14 por aula) não foram aplicados. Aplicar muda hash e pede nova conferência.
- Inspeção e julgamento não ouviram o áudio. Erro de transcrição que mude o sentido só aparece se o material de apoio divergir.

Validadores no fechamento: `base_fcc.py --partial --reviews --check` com **zero erros e 1 aviso** (`M01_A06` com 2 unidades, abaixo da faixa 3–60; é a aula de oferta). 10 testes passando. Inspeções e julgamentos publicados batem, por hash, com os JSON publicados.

Cobertura no alcance já extraído: 31 combinações tarefa × plataforma presentes e 305 ausentes; 18 das 28 tarefas e 14 dos 35 temas têm alguma unidade. Os ausentes são esperados com 8 de 54 aulas e estão explícitos em `cobertura.jsonl`.

### Consumo do lote 1 (nominal, via assinatura, sem Batch API)

| Papel | Modelo e esforço | Chamadas | input | output | cache_creation | cache_read | Nominal |
|---|---|---:|---:|---:|---:|---:|---:|
| Extrator | Sonnet 5 `high` | 6 + 2 ouro | 18 | 64.659 | 123.633 | 105.748 | US$ 1,16 |
| Reparo de contrato | Sonnet 5 `high` | 1 | 2 | 976 | 24.553 | 2.995 | US$ 0,11 |
| Inspetor | Sonnet 5 `xhigh` | 9 + 4 ouro | 26 | 304.394 | 296.041 | 144.200 | US$ 4,26 |
| Redator | Opus 5 `high` | 3 + 2 ouro | 12 | 26.957 | 114.934 | 68.930 | US$ 1,86 |
| Juiz | Fable 5.1 `xhigh` | 7 + 4 ouro | 22 | 120.933 | 188.916 | 113.318 | US$ 9,86 |

Total US$ 17,24 nominais para 8 aulas, fora as configurações descartadas do piloto e a calibração. Todas as 38 chamadas terminaram com `stop_reason: tool_use` e `terminal_reason: completed`, sem recusa e sem erro. Registros em `execucoes/lote-m01/` e `execucoes/ouro/`.

O módulo 1 custou US$ 1,60 por aula, acima da projeção do piloto, porque 4 das 6 aulas foram a julgamento e 3 precisaram de correção. As causas foram três: recurso do curso sem marca de perecível (5 unidades), sigla CDF desdobrada por invenção (corrigido no pacote com o vocabulário do FORMATO) e um erro real de conteúdo (numeração de passos em `M01_A03` U4).

### Revisão posterior de `M01_A01` (20/09/2026)

Will decidiu que estrutura do curso é perecível. A regra virou script (tema `curso-e-recursos` ou tarefa `usar-recursos-do-curso` exige `perecivel: true`) e foi aplicada por script a três unidades de `M01_A01`. A conferência focal dessas unidades achou um erro que a primeira inspeção tinha classificado como menor: o `limite` U8 dizia que o método vem "nos módulos seguintes", e a fonte diz que começa na aula seguinte, dentro do módulo 1. A aula foi a julgamento como conferência adicional, reprovada (U8 sem lastro, duas faixas erradas, um perecível), corrigida pelo Opus 5 no ciclo 1 e aprovada. Status atual: revisado. Com isso, o lote 1 tem 7 de 8 aulas julgadas; só `M01_A04` ficou com inspeção sem julgamento.

### Lote 2 — módulo 2, fechado em 20/09/2026

| Aula | Unidades | Inspeção com fonte | Julgamento | Correção | Status |
|---|---:|---|---|---|---|
| `M02_A01` | 14 | integral, 1 omissão material, 1 perecível | adicional: falha → **passa** | ciclo 1, focal | revisado |
| `M02_A02` | 8 | integral, só menores | não julgada | 1 reparo de contrato | validado |
| `M02_A03` | 18 | integral, 3 perecíveis | adicional: falha → **passa** | ciclo 1, focal | revisado |
| `M02_A04` | 19 | integral, 1 perecível | adicional: falha → **passa** | ciclo 1, focal | revisado |
| `M02_A05` | 19 | integral, sem apontamento material | amostra: **passa** de primeira | reparo de contrato | revisado |
| `M02_A06` | 24 | integral, só menores | não julgada | — | validado |
| `M02_A07` | 14 | integral, 1 desvio material, 1 omissão material, 1 perecível | adicional: falha → **passa** | reparo de contrato + ciclo 1, focal | revisado |
| `M02_A08` | 11 | integral, 1 perecível | amostra: falha → **passa** | reparo de contrato + ciclo 1, focal | revisado |
| `M02_A09` | 12 | integral, 2 desvios menores | adicional (gatilho ampliado): falha → falha só de contrato → **passa** | contexto corrigido pela coordenação, reparo de contrato, ciclo 1 (U9, U13), âncora da U9 corrigida por script com inspeção religada por hash | revisado |
| `M02_A10` | 10 | integral, 1 desvio e 1 sem-lastro menores | adicional (gatilho ampliado): falha → **passa** | reparo de contrato + ciclo 1, focal | revisado |

- 149 unidades no módulo, todas inspecionadas com fonte. 117 em aulas julgadas e aprovadas; 32 (`M02_A02`, `M02_A06`) só com script e inspeção.
- 8 das 10 aulas foram a julgamento e 7 reprovaram na primeira passagem. Todas passaram no ciclo 1. Nenhuma chegou ao teto.
- `M02_A09` não usa material de apoio: o PDF da aula repete o da aula 8 e está em `fontes_ignoradas`.
- O que reprovou: perecível sem marca em 5 aulas, quase sempre referência a outro módulo, documento ou IA do curso; faixa que não cobre o que o corpo afirma; caso analisado virando regra do formato; divergência fala × material resolvida em silêncio; duas omissões materiais. Só 1 das reprovações foi exclusivamente por perecibilidade.
- Erros mecânicos recorrentes do extrator: título acima de 80 caracteres, cópia de 25 palavras em unidade que reproduz roteiro analisado, relógio citado no contexto para localizar trecho degradado. O papel do extrator foi reforçado para os próximos módulos e a retirada de relógio do contexto virou passo de script.

Consumo do lote 2 (nominal, assinatura, sem Batch API), 56 chamadas, todas `stop_reason: tool_use` e `terminal_reason: completed`:

| Papel | Modelo e esforço | Chamadas | input | output | cache_creation | cache_read | Nominal |
|---|---|---:|---:|---:|---:|---:|---:|
| Extrator | Sonnet 5 `high` | 10 | 22 | 111.891 | 142.010 | 153.543 | US$ 1,72 |
| Reparo de contrato | Sonnet 5 `high` | 6 | 22 | 14.912 | 96.793 | 191.865 | US$ 0,57 |
| Inspetor | Sonnet 5 `xhigh` | 17 | 40 | 466.351 | 345.348 | 353.970 | US$ 6,12 |
| Redator | Opus 5 `high` | 7 | 14 | 43.539 | 118.899 | 81.270 | US$ 2,32 |
| Juiz | Fable 5.1 `xhigh` | 16 | 32 | 178.679 | 245.241 | 211.830 | US$ 13,89 |

Total US$ 24,62, ou US$ 2,46 por aula. O juiz é 56% disso. O custo por aula subiu em relação ao lote 1 porque 8 de 10 aulas foram julgadas e 7 corrigidas.

### Lote 3 — módulo 3, fechado em 20/09/2026

`M03_A06` é ouro e já estava publicada. As outras dez:

| Aula | Unidades | Inspeção com fonte | Julgamento | Correção | Status |
|---|---:|---|---|---|---|
| `M03_A01` | 13 | integral, 1 apontamento (U8) | adicional: falha → **passa** | reparo de contrato + ciclo 1, focal | revisado |
| `M03_A02` | 17 | integral, limpa | amostra: **passa** de primeira | — | revisado |
| `M03_A03` | 29 | integral, 2 apontamentos (U3, U20), 1 perecível | adicional: falha → **passa** | relógio retirado do contexto por script, reparo de contrato, ciclo 1, focal | revisado |
| `M03_A04` | 18 | integral, 2 apontamentos (U2, U9) | adicional: falha → **passa** | ciclo 1, focal | revisado |
| `M03_A05` | 13 | integral, limpa | não julgada | reparo de contrato | validado |
| `M03_A07` | 14 | integral, limpa | amostra: **passa** de primeira | — | revisado |
| `M03_A08` | 14 | integral, limpa | não julgada | relógio retirado do contexto por script, reparo de contrato | validado |
| `M03_A09` | 12 | integral, limpa | não julgada | — | validado |
| `M03_A10` | 8 | integral, 1 apontamento (U6) | adicional: **passa** de primeira | reparo de contrato | revisado |
| `M03_A11` | 9 | integral, 1 apontamento (U5) | adicional: **passa** de primeira | — | revisado |

- 147 unidades novas, todas inspecionadas com fonte. 108 em aulas julgadas e aprovadas; 39 (`M03_A05`, `M03_A08`, `M03_A09`) só com script e inspeção.
- 7 das 10 aulas foram a julgamento; 4 passaram de primeira e 3 no ciclo 1. Nenhuma chegou ao teto.
- Perecibilidade deixou de ser causa de reprovação: 1 apontamento em 10 aulas, contra 5 aulas em 10 no módulo 2. O que mudou foi o reforço no papel do extrator e a regra de script para recurso do curso.
- "Apontamento" aqui inclui `desvio` e `sem-lastro` que o inspetor classificou como menor: é o gatilho ampliado. Em `M03_A10` e `M03_A11` o juiz concordou que eram menores e aprovou.

Consumo do lote 3 (nominal, assinatura, sem Batch API), 41 chamadas, todas `stop_reason: tool_use` e `terminal_reason: completed`:

| Papel | Modelo e esforço | Chamadas | input | output | cache_creation | cache_read | Nominal |
|---|---|---:|---:|---:|---:|---:|---:|
| Extrator | Sonnet 5 `high` | 10 | 30 | 119.493 | 171.933 | 277.828 | US$ 1,94 |
| Reparo de contrato | Sonnet 5 `high` | 5 | 20 | 12.257 | 100.630 | 199.487 | US$ 0,57 |
| Inspetor | Sonnet 5 `xhigh` | 13 | 26 | 384.514 | 316.620 | 175.752 | US$ 5,15 |
| Redator | Opus 5 `high` | 3 | 6 | 14.589 | 69.658 | 40.635 | US$ 1,08 |
| Juiz | Fable 5.1 `xhigh` | 10 | 20 | 112.932 | 147.000 | 141.220 | US$ 8,62 |

Total US$ 17,35, ou US$ 1,74 por aula.

### Lote 4 — módulo 4, fechado em 20/09/2026

| Aula | Unidades | Inspeção com fonte | Julgamento | Correção | Status |
|---|---:|---|---|---|---|
| `M04_A01` | 19 | integral, 1 perecível | amostra: falha → **passa** | ciclo 1, focal | revisado |
| `M04_A02` | 23 | integral, 1 apontamento (U4) | adicional: **passa** de primeira | reparo de contrato | revisado |
| `M04_A03` | 10 | integral, sem apontamento material | amostra: falha → **passa** | reparo de contrato + ciclo 1, focal | revisado |
| `M04_A04` | 15 | integral, 1 apontamento (U1) | adicional: falha → **passa** | ciclo 1, focal | revisado |
| `M04_A05` | 11 | integral, 1 apontamento (U5) | adicional: falha → **passa** | reparo de contrato + ciclo 1, focal | revisado |
| `M04_A06` | 7 | integral, 1 apontamento (U5), 1 perecível | adicional: falha → **passa** | ciclo 1, focal | revisado |
| `M04_A07` | 8 | integral, faixa errada em 2 de 8 | adicional (gatilho de faixa): falha → **passa** | ciclo 1, focal | revisado |
| `M04_A08` | 14 | integral, 1 apontamento (U9) | adicional: **passa** de primeira | — | revisado |
| `M04_A09` | 15 | integral, limpa, faixa errada em 1 de 13 | não julgada | reparo de contrato | validado |
| `M04_A10` | 6 | integral, 2 apontamentos (U3, U6) | adicional: falha → **passa** | ciclo 1, focal | revisado |

- 128 unidades, todas inspecionadas com fonte. 113 em aulas julgadas e aprovadas; 15 (`M04_A09`) só com script e inspeção.
- 9 das 10 aulas foram a julgamento; 2 passaram de primeira e 7 no ciclo 1. Nenhuma chegou ao teto.
- `M04_A03` é a evidência de que inspeção sem apontamento material não garante aprovação: estava na amostra, o inspetor só registrou duas faixas erradas como menores, e o juiz reprovou porque 2 de 10 passa do limiar de 10% da rubrica. A conta virou gatilho de script e levou `M04_A07` a julgamento.
- As reprovações do módulo são de um tipo próprio dele: aula de bastidor de gravação em que o professor demonstra, e a unidade transforma a demonstração em regra geral; e faixa que não cobre tudo o que o corpo afirma.
- Limite da fonte que pesa neste módulo: muito do ensino está no que é mostrado na tela. As unidades só registram o que a fala ou o material descrevem, e cada aula tem `limite` dizendo o que ficou só na imagem.

Consumo do lote 4 (nominal), 54 chamadas, todas `stop_reason: tool_use` e `terminal_reason: completed`:

| Papel | Modelo e esforço | Chamadas | input | output | cache_creation | cache_read | Nominal |
|---|---|---:|---:|---:|---:|---:|---:|
| Extrator | Sonnet 5 `high` | 10 | 26 | 91.497 | 107.357 | 197.316 | US$ 1,38 |
| Reparo de contrato | Sonnet 5 `high` | 4 | 14 | 8.049 | 47.541 | 128.283 | US$ 0,30 |
| Inspetor | Sonnet 5 `xhigh` | 17 | 38 | 348.304 | 266.296 | 306.498 | US$ 4,61 |
| Redator | Opus 5 `high` | 7 | 18 | 30.015 | 79.608 | 138.789 | US$ 1,62 |
| Juiz | Fable 5.1 `xhigh` | 16 | 32 | 153.698 | 193.607 | 225.952 | US$ 11,61 |

Total US$ 19,52, ou US$ 1,95 por aula.

### Lote 5 — módulo 5, fechado em 20/09/2026

`M05_A02` é ouro e já estava publicada. As outras seis:

| Aula | Unidades | Inspeção com fonte | Julgamento | Correção | Status |
|---|---:|---|---|---|---|
| `M05_A01` | 18 | integral, 1 apontamento (U12) | amostra: falha → **passa** | ciclo 1, focal | revisado |
| `M05_A03` | 16 | integral, limpa | não julgada | reparo de contrato | validado |
| `M05_A04` | 10 | integral, limpa | não julgada | — | validado |
| `M05_A05` | 14 | integral, limpa | não julgada | reparo de contrato | validado |
| `M05_A06` | 22 | integral, limpa | não julgada | reparo de contrato (5 erros mecânicos) | validado |
| `M05_A07` | 16 | integral, 1 apontamento (U8) | amostra: falha → **passa** | ciclo 1, focal | revisado |

- 96 unidades novas, todas inspecionadas com fonte. 34 em aulas julgadas e aprovadas; **62 só com script e inspeção**. É o módulo com menor alcance de julgamento: só as duas aulas da amostra foram ao juiz, e as duas reprovaram na primeira passagem.
- As divergências entre fala e material que o levantamento inicial apontou em `M05_A01` e `M05_A03` aparecem registradas em `nota` nas unidades; o inspetor não acusou resolução silenciosa.

Consumo do lote 5 (nominal), 23 chamadas, todas concluídas sem erro:

| Papel | Modelo e esforço | Chamadas | input | output | cache_creation | cache_read | Nominal |
|---|---|---:|---:|---:|---:|---:|---:|
| Extrator | Sonnet 5 `high` | 6 | 12 | 69.393 | 76.112 | 87.096 | US$ 1,02 |
| Reparo de contrato | Sonnet 5 `high` | 3 | 8 | 6.410 | 47.782 | 65.734 | US$ 0,27 |
| Inspetor | Sonnet 5 `xhigh` | 8 | 16 | 223.195 | 166.852 | 117.168 | US$ 2,92 |
| Redator | Opus 5 `high` | 2 | 4 | 5.808 | 29.009 | 27.090 | US$ 0,45 |
| Juiz | Fable 5.1 `xhigh` | 4 | 8 | 39.388 | 61.100 | 56.488 | US$ 3,21 |

Total US$ 7,86, ou US$ 1,31 por aula.

### Lote 6 — módulo 6, fechado em 20/09/2026

Módulo sem material de apoio: toda unidade tem `fonte: fala`.

| Aula | Unidades | Inspeção com fonte | Julgamento | Correção | Status |
|---|---:|---|---|---|---|
| `M06_A01` | 15 | integral, 2 apontamentos (U1, U7) | adicional: falha → **passa** | reparo de contrato + ciclo 1, focal | revisado |
| `M06_A02` | 17 | integral, 2 apontamentos (U4, U13) | adicional: falha → **passa** | reparo de contrato + ciclo 1, focal | revisado |
| `M06_A03` | 23 | integral, limpa | não julgada | — | validado |
| `M06_A04` | 16 | integral, 2 apontamentos (U11, U14) | adicional: **passa** de primeira | reparo de contrato | revisado |
| `M06_A05` | 7 | integral, 1 apontamento (U7) | amostra: **passa** de primeira | — | revisado |
| `M06_A06` | 18 | integral, 1 apontamento (U14) | adicional: falha → **passa** | ciclo 1, focal | revisado |
| `M06_A07` | 9 | integral, limpa | não julgada | — | validado |
| `M06_A08` | 15 | integral, limpa | amostra: **passa** de primeira | — | revisado |

- 120 unidades, todas inspecionadas com fonte. 88 em aulas julgadas e aprovadas; 32 (`M06_A03`, `M06_A07`) só com script e inspeção.
- 6 das 8 aulas foram a julgamento; 3 passaram de primeira e 3 no ciclo 1. Nenhuma chegou ao teto.

Consumo do lote 6 (nominal), 34 chamadas, todas concluídas sem erro:

| Papel | Modelo e esforço | Chamadas | input | output | cache_creation | cache_read | Nominal |
|---|---|---:|---:|---:|---:|---:|---:|
| Extrator | Sonnet 5 `high` | 8 | 18 | 99.121 | 102.123 | 142.478 | US$ 1,43 |
| Reparo de contrato | Sonnet 5 `high` | 3 | 8 | 4.730 | 36.225 | 64.181 | US$ 0,21 |
| Inspetor | Sonnet 5 `xhigh` | 11 | 24 | 312.152 | 262.441 | 193.613 | US$ 4,21 |
| Redator | Opus 5 `high` | 3 | 6 | 10.895 | 40.390 | 40.635 | US$ 0,70 |
| Juiz | Fable 5.1 `xhigh` | 9 | 18 | 105.320 | 123.675 | 127.098 | US$ 7,77 |

Total US$ 14,31, ou US$ 1,79 por aula.

### Lote 7 — módulo 7, fechado em 20/09/2026

Duas aulas longas, sem material de apoio, as duas na amostra.

| Aula | Unidades | Inspeção com fonte | Julgamento | Correção | Status |
|---|---:|---|---|---|---|
| `M07_A01` | 51 | integral em 3 blocos de 17 unidades, 3 apontamentos, 3 omissões menores | amostra: falha (4 de fidelidade) → **passa** | ciclo 1 (U9, U18, U30, U37), focal | revisado |
| `M07_A02` | 47 | integral em 3 blocos (16, 16, 15), 5 apontamentos, 3 omissões menores | amostra: falha (6 de fidelidade, 1 de aplicabilidade) → **passa** | reparo de contrato (7 erros mecânicos) + ciclo 1 (7 unidades), focal | revisado |

- Inspeção em blocos: a primeira tentativa, com as ~50 unidades numa chamada só, estourou o limite de 40 minutos por chamada do executor. Passou a rodar uma chamada por bloco de até 20 unidades; todas recebem a aula e o arquivo inteiro, cada uma confere só o seu bloco, e o bloco 1 faz a busca de omissões na fonte inteira. A segunda tentativa bateu no limite de sessão da assinatura (HTTP 429, seis chamadas) e foi refeita depois da renovação da cota. Os registros das duas tentativas ficaram guardados com `tentativa-timeout` e `tentativa-429` no nome.
- A extração usada é a deste lote, com o contrato final. A extração de `M07_A01` feita no piloto para testar tamanho não foi publicada.
- Oferta comercial e anúncio de formação futura estão em `limite`; preço, faturamento e números de mercado estão em `exemplo`, perecíveis. `M07_A02` é Q&A: as respostas viraram `decisao` ou `regra` com a situação de quem perguntou em `condicoes`.

Consumo do lote 7 (nominal), 17 chamadas concluídas, sem contar as 10 tentativas com erro:

| Papel | Modelo e esforço | Chamadas | input | output | cache_creation | cache_read | Nominal |
|---|---|---:|---:|---:|---:|---:|---:|
| Extrator | Sonnet 5 `high` | 2 | 4 | 102.704 | 119.169 | 29.032 | US$ 1,51 |
| Reparo de contrato | Sonnet 5 `high` | 1 | 2 | 5.191 | 54.847 | 13.452 | US$ 0,27 |
| Inspetor | Sonnet 5 `xhigh` | 8 | 16 | 332.348 | 721.019 | 73.230 | US$ 6,22 |
| Redator | Opus 5 `high` | 2 | 4 | 17.469 | 147.454 | 13.545 | US$ 1,92 |
| Juiz | Fable 5.1 `xhigh` | 4 | 8 | 81.268 | 185.921 | 42.366 | US$ 7,79 |

Total US$ 17,72, ou US$ 8,86 por aula. O registro somado que o executor grava por aula inspecionada em blocos leva `agregado_de_blocos: true` e não entra nas somas.

## Fechamento

Conferência final em 20/09/2026, sem `--partial`: `base_fcc.py --reviews --check` com **54 aulas, zero erros, 1 aviso** (`M01_A06`, aula de oferta, com 2 unidades). `--inventory` com zero divergências entre as fontes no disco e o commit `aaff8b6`. Nenhum arquivo de fonte foi alterado. 10 testes passando.

### O que foi entregue

- 54 arquivos em `conhecimento/dados/` e 54 páginas em `conhecimento/unidades/`, 831 unidades com ID citável.
- `unidades.jsonl` (831 linhas) e `cobertura.jsonl` (336 combinações tarefa × plataforma: 84 presentes, 252 ausentes, todas explícitas).
- 35 índices por tema e 28 por tarefa. Todo tema e toda tarefa da taxonomia têm ao menos uma unidade. Nenhuma `proposta_tag`: a taxonomia derivada do levantamento inicial aguentou o curso inteiro.
- `manifest.json` com hash de cada fonte e o commit de referência.
- Laudos: 54 inspeções e 54 julgamentos em `revisao/`, ligados por hash ao JSON publicado; ciclos de correção nas pastas de `lotes/`; calibração com gabarito em `calibracao/`.
- 287 registros de execução concluída em `execucoes/`, mais 10 de tentativas com erro.

Perfil das unidades: 290 regras, 149 exemplos, 130 conceitos, 50 decisões, 49 limites, 49 procedimentos, 42 estruturas, 35 fatos de material, 24 de ferramenta, 13 réguas. 296 perecíveis. Confiança alta em 581, média em 246, baixa em 4. Fonte: 575 só fala, 206 fala e material, 50 só material. 756 unidades são `geral`; as plataformas específicas mais presentes são Trello (29), SOFIA (24) e Instagram (16).

### Alcance real da revisão

| Alcance | Aulas | Unidades |
|---|---:|---:|
| Validação de contrato por script | 54 | 831 |
| Inspeção com fonte, integral | 54 | 831 |
| Julgamento sem fonte, aprovado | 54 (2 ouro + 52) | 831 |

- **Julgamento integral, decidido por Will em 20/09/2026.** A regra original julgava 16 aulas de amostra mais as conferências adicionais, o que levou 41 aulas ao juiz. As 13 restantes (`M01_A04`, `M02_A02`, `M02_A06`, `M03_A05`, `M03_A08`, `M03_A09`, `M04_A09`, `M05_A03`, `M05_A04`, `M05_A05`, `M05_A06`, `M06_A03`, `M06_A07`) foram julgadas depois, sobre a mesma inspeção já publicada. 11 passaram de primeira; `M04_A09` (fidelidade) e `M05_A03` (aplicabilidade) foram corrigidas no ciclo 1 e aprovadas. As tabelas dos lotes acima mostram o estado dessas aulas antes dessa rodada.
- O juiz reprovou na primeira passagem **31 das 54 aulas**: 29 das 41 que chegaram a ele por amostra ou por apontamento da inspeção, e 2 das 13 que a inspeção tinha dado como limpas. O filtro da inspeção, com os dois ajustes de gatilho, previu bem: 85% das aulas que ele deixou de fora passaram direto. Não previu tudo: 2 em 13 tinham falha que só o juiz viu.
- Todas as 31 reprovadas passaram depois de correção localizada pelo Opus 5: 30 no ciclo 1 e uma (`M03_A06`, ouro) no ciclo 2. `M02_A09` passou no ciclo 1 quanto ao conteúdo e precisou de um acerto mecânico de âncora por script antes da confirmação do juiz. Nenhuma estourou o teto, nenhuma foi reextraída, nenhuma ficou bloqueada. Não há falha material conhecida pendente.
- Os gatilhos da conferência adicional foram ampliados duas vezes pela coordenação, com registro em `piloto/PLANO.md`: qualquer `desvio` ou `sem-lastro`, mesmo menor; e faixa errada acima de 10%.
- Depois de cada correção a conferência foi focal: o inspetor conferiu as unidades alteradas e a lista de falhas, e as intactas mantiveram a evidência da inspeção integral, com hash de unidade conferido. A exceção é o primeiro rejulgamento de `M03_A06`, feito sobre reinspeção integral.
- Aprovado não quer dizer sem ressalva. Os ajustes menores registrados nos 54 julgamentos não foram aplicados.
- O contrato mudou durante o trabalho (perecível por plataforma, recurso e estrutura do curso, vocabulário do curso). Todas as aulas publicadas passam no validador do contrato final. Julgamentos anteriores a cada mudança não foram refeitos; é o caso de `M05_A02` e do módulo 1.
- O juiz não vê a fonte. Ele decide com as unidades e a evidência do inspetor, então um erro que o inspetor não registrou e que não aparece no texto da unidade passa pelos dois.
- Ninguém ouviu o áudio. A transcrição é automática. Erro de transcrição que mude o sentido só aparece quando o material de apoio diverge, e os módulos 6 e 7 não têm material.
- O que ficou só na imagem não está na base. Pesa mais no módulo 4.

### Consumo total (nominal, via assinatura, sem Batch API)

| Papel | Modelo e esforço | Chamadas | input | output | cache_creation | cache_read | Nominal |
|---|---|---:|---:|---:|---:|---:|---:|
| Extrator | Sonnet 5 `high` | 54 | 130 | 658.758 | 842.337 | 993.041 | US$ 10,16 |
| Reparo de contrato | Sonnet 5 `high` | 23 | 76 | 52.525 | 408.371 | 665.997 | US$ 2,29 |
| Inspetor | Sonnet 5 `xhigh` | 91 | 196 | 2.416.275 | 2.475.922 | 1.427.919 | US$ 34,35 |
| Redator | Opus 5 `high` | 32 | 72 | 161.248 | 667.182 | 450.725 | US$ 10,93 |
| Juiz | Fable 5.1 `xhigh` | 87 | 176 | 978.087 | 1.390.085 | 1.158.560 | US$ 77,00 |

**US$ 134,73 nominais em 287 chamadas**, todas com `stop_reason: tool_use` e `terminal_reason: completed`, sem recusa. Dentro disso, o julgamento integral das 13 aulas finais custou US$ 13,38 em 19 chamadas. Fora da base: US$ 13,30 (configurações descartadas do piloto, teste de tamanho e calibração). Total do trabalho: US$ 148,03 nominais, US$ 2,74 por aula. O juiz é 57% do custo das aulas publicadas, o inspetor 25% e o extrator 8%. Há mais 10 registros de tentativas com erro (2 por limite de tempo, 8 por limite de sessão da assinatura). A projeção feita no piloto (ordem de US$ 70) estava errada por baixo: supunha 16 julgamentos e foram 87 chamadas de juiz.

### Correção posterior: cópia bruta em 4 unidades (21/09/2026)

No piloto do Hardcopy Pro o juiz achou um defeito no validador compartilhado: a checagem de cópia de 25 palavras comparava texto cru, e o Markdown do material e as marcações de tempo escondiam a cópia. Com a comparação por sequência de palavras, esta base, já fechada, passou a acusar 4 unidades, todas de fonte `material`: `M02_A03` U018, `M03_A01` U011, `M03_A02` U015 e `M04_A04` U013 (28, 36, 27 e 33 palavras idênticas à fonte, nessa ordem). Will decidiu corrigir.

Via normal, em `lotes/correcao-copia/`: paráfrase pelo Opus 5 `high` só dessas unidades (rodada 3, reparo de contrato, não é ciclo de conteúdo), conferência focal pelo Sonnet 5 `xhigh` com a evidência das demais preservada por hash, e conferência do juiz Fable 5.1 `xhigh` com a saída de script da coordenação anexada por `julgar --prova`. As quatro unidades saíram `lastreada` na focal e as quatro aulas tiveram `passa`, sem falha. Maior sequência idêntica depois da correção: 17, 14, 11 e 16 palavras. Publicadas por `fcc_publicar.py`; `base_fcc.py --reviews --check` voltou a **zero erros e 1 aviso**, e `--inventory` segue sem divergência. Nenhum outro arquivo gerado mudou.

Consumo, em tokens (12 chamadas, todas `tool_use` e `completed`; por decisão de Will em 21/09/2026 o consumo passa a ser relatado em tokens da assinatura, não em dólar):

| Papel | Modelo e esforço | Chamadas | Entrada nova | Cache lido | Saída |
|---|---|---:|---:|---:|---:|
| Inspetor | `claude-sonnet-5` `xhigh` | 4 | 114.104 | 43.938 | 14.782 |
| Juiz | `claude-fable-5-1` `xhigh` | 4 | 83.000 | 42.366 | 20.502 |
| Redator | `claude-opus-5` `high` | 4 | 81.531 | 70.742 | 15.649 |

Os julgamentos anteriores dessas quatro aulas ficam em `lotes/correcao-copia/antes/`.

### Pendências

- Nenhuma falha material conhecida pendente na base.
- Aceite da entrega por Will.
- A base vive na branch `task/formato-criativo-base-consulta`; a integração à `main` do repositório de cursos depende de Will.
