# Processamento da base de conhecimento: Hardcopy Pro

Estado em 22/09/2026: **em andamento.** 100 de 139 entradas publicadas (lotes 1 a 7: grupos G01 a G12 completos), 818 unidades, validador com zero erros e 8 avisos esperados. As 100 passaram por inspeção integral com fonte e por julgamento sem fonte, e estão aprovadas. Este arquivo nasceu no fechamento do lote 1 e ganha uma seção por lote fechado.

Finalidade: tornar o curso consultável por agentes, como matéria-prima para skills e agentes da TC3. O leitor final é um agente. Voz textual, playbooks, checklists e consolidação entre aulas ficam fora desta etapa.

## Fontes

- Repositório `tc3midia/cursos`, fontes lidas no commit `7470ca0`; desde 22/09/2026 o commit de referência é `42c88f6`, que só moveu as aulas para `transcricoes/` (um arquivo por aula, mesmo conteúdo; legenda e segmentos saíram do repositório e deixaram de ser conferidos). Branch de trabalho `task/hardcopy-pro-base-consulta`, enviada.
- 138 aulas gravadas e 1 material avulso ("Surpresa", código `G02_A12`), 5 trilhas, 18 grupos, 271.924 palavras de transcrição.
- `CURSO=hardcopy-pro python3 base_fcc.py --inventory`, em 21/09/2026, depois da publicação do lote 1: 139 entradas, zero erros, nenhuma fonte alterada. Os avisos do inventário são a cauda da transcrição depois da duração do manifesto, registrada no PLANO.

Limitações das fontes, registradas e não corrigidas:

1. Transcrição automática (Whisper `large-v3-turbo`), sem conferência com o áudio. Vocabulário raro do curso sai deformado; o FORMATO fixa a grafia adotada por termo. A retranscrição com o vocabulário do curso no `initial_prompt` fica para o final, por decisão de Will.
2. Resíduo de silêncio e laço de repetição na transcrição. O FORMATO proíbe extrair desses trechos.
3. Boa parte do curso é aula de tela. O que ficou só na imagem não está na base; cada aula registra isso em `limite`.
4. Os tempos da transcrição podem estar deslocados em relação ao vídeo original (margem de captura). A faixa localiza o trecho na transcrição.

## Papéis e via

| Papel | Modelo | Esforço | Recebe |
|---|---|---|---|
| Coordenação | Fable 5.1 (sessão do Claude Code) | n/a | plano, inventário, resultados. Não escreve nem reescreve unidades |
| Extrator | `claude-sonnet-5` | `high` | bloco fixo + uma aula |
| Reparo de contrato | `claude-sonnet-5` | `high` | erros do validador + unidades afetadas + aula |
| Inspetor | `claude-sonnet-5` | `xhigh` | bloco fixo + aula + unidades, em execução separada, blocos de até 20 unidades |
| Redator de correções | `claude-opus-5` | `high` | falhas consolidadas + unidades afetadas + aula |
| Juiz | `claude-fable-5-1` | `xhigh` | unidades + evidência do inspetor + validador + rubrica. Sem transcrição, material ou clone |

Via: assinatura do Claude Code, `claude -p` headless, um processo isolado por chamada, em diretório vazio, sem ferramentas. Não há chave de API nem Batch API. O executor espera sozinho no limite de sessão. Cada chamada grava `<AULA>.<papel>.execucao.json` com modelo pedido e usado, esforço, via, início e fim, os quatro contadores de token, tokens de raciocínio, `stop_reason` e `terminal_reason`.

Consumo se mede em tokens da assinatura, por modelo e por papel (decisão de Will em 21/09/2026). "Entrada nova" é `input` mais `cache_creation`; "cache lido" é o bloco fixo do papel relido a cada chamada.

## Arquivos

- `../../conhecimento/FORMATO.md` (v2) e `../../conhecimento/taxonomia.md`: contrato e enums deste curso, congelados desde o lote 1.
- `PLANO.md`, `RUBRICA.md`, `papeis/`, `amostra.json`, `calibracao/`.
- `piloto/RESULTADO.md`: piloto, calibração com erro plantado, consumo e primeira projeção.
- `RETOMADA.md`: estado, decisões de Will e como rodar um lote.
- `revisao/inspecao/`, `revisao/julgamento/`: laudos publicados, um por aula, ligados por hash ao JSON da aula.
- `lotes/`: pastas de trabalho de cada lote, com as versões intermediárias. `execucoes/`: registro de cada chamada de modelo das aulas publicadas.

## Alcance da revisão

Regra deste curso, decidida por Will: inspeção com fonte em todas as aulas e julgamento em todas as aulas, desde o primeiro lote. Teto de dois ciclos de correção por aula, conferência focal depois da correção.

### Lote 1: G01 e G02 (trilha Hard Copy), fechado em 21/09/2026

18 extrações novas mais as 3 entradas do grupo já aprovadas no piloto (`G02_A05` ouro, `G02_A11`, `G02_A12`), que entraram só na publicação.

| Aula | Palavras | Unidades | Contrato na 1ª saída | Inspeção com fonte | Julgamento | Correção | Status |
|---|---:|---:|---|---|---|---|---|
| `G01_A01` | 765 | 3 | limpa | integral, 1 desvio (U1) | **passa** de primeira | n/a | revisado |
| `G01_A02` | 933 | 4 | 1 erro (marcador temporal em U4) | integral, 1 desvio (U2), 1 faixa errada (U3), 1 omissão material, 1 perecível | falha (fidelidade, perecibilidade) → **passa** | reparo de contrato + ciclo 1 (U2, U3), focal | revisado |
| `G01_A03` | 1.580 | 10 | limpa | integral, 1 desvio (U7), 3 omissões menores | falha (fidelidade) → **passa** | ciclo 1 (U7), focal | revisado |
| `G01_A04` | 1.067 | 3 | limpa | integral, faixa errada em 1 de 3 (U3), 1 omissão menor | falha (fidelidade, aplicabilidade) → **passa** | ciclo 1 (U2, U3), focal | revisado |
| `G01_A05` | 2.032 | 12 | limpa | integral, sem apontamento | **passa** de primeira | n/a | revisado |
| `G01_A06` | 1.249 | 10 | limpa | integral, 1 omissão menor | **passa** de primeira | n/a | revisado |
| `G01_A07` | 1.679 | 11 | limpa | integral, 1 omissão menor | **passa** de primeira | n/a | revisado |
| `G01_A08` | 1.004 | 6 | limpa | integral, sem apontamento | **passa** de primeira | n/a | revisado |
| `G01_A09` | 549 | 2 | limpa, aviso de menos de 3 unidades | integral, 1 desvio (U2), faixa errada em 1 de 2 (U1) | falha (fidelidade, aplicabilidade) → **passa** | ciclo 1 (U1, U2), focal | revisado |
| `G02_A01` | 434 | 5 | 1 erro (`fato-material` sem fonte material em U2) | integral, faixa errada em 1 de 5 (U4) | falha (fidelidade) → **passa** | reparo de contrato + ciclo 1 (U4), focal | revisado |
| `G02_A02` | 1.500 | 11 | 1 erro (título de U1 acima de 80 caracteres) | integral, faixa errada em 2 de 11, 1 perecível (U6) | falha (fidelidade, perecibilidade) → **passa** | reparo de contrato + ciclo 1 (U2, U3, U6, U10), focal | revisado |
| `G02_A03` | 1.740 | 8 | limpa | integral, 1 perecível (U3) | **passa** de primeira | n/a | revisado |
| `G02_A04` | 2.214 | 11 | limpa | integral, 3 desvios (U1, U3, U8), 1 faixa errada | falha (fidelidade) → **passa** | ciclo 1 (U1, U3, U8), focal | revisado |
| `G02_A05` ouro | 1.681 | 10 | piloto | piloto: integral | piloto: **passa** de primeira | reparo de contrato no piloto | ouro |
| `G02_A06` | 791 | 5 | limpa | integral, sem apontamento | **passa** de primeira | n/a | revisado |
| `G02_A07` | 1.667 | 11 | 1 erro (evidência de U2 fora da faixa) | integral, 1 desvio (U11), 2 perecíveis (U7, U11), 1 omissão menor | falha (fidelidade) → **passa** | reparo de contrato + ciclo 1 (U11), focal | revisado |
| `G02_A08` | 628 | 5 | limpa | integral, 1 perecível (U2) | **passa** de primeira | n/a | revisado |
| `G02_A09` | 2.247 | 13 | limpa | integral, 1 desvio (U13), 2 omissões menores | falha (aplicabilidade) → **passa** | ciclo 1 (U4), focal | revisado |
| `G02_A10` | 2.137 | 4 | limpa | integral, sem apontamento | **passa** de primeira | n/a | revisado |
| `G02_A11` | 2.304 | 15 | piloto | piloto: integral, 1 desvio menor (U9) | piloto: **passa** de primeira | reparo de contrato no piloto | revisado |
| `G02_A12` material | 0 (526 de material) | 10 | piloto | piloto: integral + focal | piloto: falha (contrato) → bloqueado pedindo prova de ferramenta → **passa** na rodada 3 | ciclo 1 (U6, U9) no piloto | revisado |

Medido no lote (18 extrações novas, 134 unidades):

- **18 de 18 aprovadas.** 9 passaram de primeira e 9 reprovaram na primeira rodada (50%). As 9 passaram no ciclo 1, com 17 unidades alteradas pelo Opus 5. Nenhuma chegou ao ciclo 2, nenhuma ficou bloqueada, nenhuma foi reextraída.
- **Por que reprovaram**, pelos vetos do juiz: fidelidade em 8 aulas, aplicabilidade em 3, perecibilidade em 2. As 18 falhas consolidadas caem em quatro tipos:
  - faixa que não cobre o que o corpo afirma (5 aulas: `G01_A02`, `G01_A04`, `G01_A09`, `G02_A01`, `G02_A02`). Em aula curta com poucas unidades, uma faixa errada já passa do teto de 10% da rubrica. `G01_A04` e `G02_A01` só tinham esse apontamento da inspeção. A correção pedida pelo juiz nesses casos foi mecânica: estender `inicio` ou `fim`, sem mexer no corpo;
  - corpo que troca o referente ou generaliza o que a fonte diz de um caso (`G01_A03` U7, `G01_A09` U2, `G02_A02` U10, `G02_A04` U1, U3 e U8, `G02_A07` U11);
  - perecível sem marca: preço de R$ 99 em `G01_A02` U2 e afirmação de mercado ("nunca vi em nenhuma VSL") em `G02_A02` U6;
  - unidade que não se entende sozinha ou com tarefa que leva ao lugar errado (`G01_A04` U2, `G01_A09` U1, `G02_A09` U4). A de `G02_A09` é a única falha em unidade que o inspetor tinha dado como lastreada: o passo "Garantia, só nas condições da aula" remete à aula em vez de dizer a condição.
- **O juiz não seguiu a gravidade do inspetor nos dois sentidos.** `G01_A01` tinha um desvio e passou de primeira; `G02_A09` reprovou por unidade sem apontamento. Confirma a regra de levar tudo ao juiz.
- **Efeito da linha contra "hoje" no papel do extrator:** 1 erro de marcador temporal em 134 unidades (0,7%), contra 3 em 63 no piloto (4,8%). Os 4 erros de contrato da primeira saída (1 por aula, em 4 aulas) foram fechados pelo reparo de contrato, fora da contagem de ciclos.
- **Zero citação não literal** do inspetor nas 27 inspeções (18 integrais e 9 focais).
- 85 chamadas, todas com `stop_reason: tool_use` e `terminal_reason: completed`, sem recusa, sem erro de API e sem espera por limite de sessão. Tempo de parede: 7 minutos de extração e 50 de condução, com três chamadas em paralelo.

O que isso significa e o que não significa:

- As 169 unidades publicadas passaram por validação de script, inspeção integral com fonte e julgamento aprovado. 10 estão em aula `ouro` e 159 em aulas `revisado`.
- Conferência focal quer dizer: depois da correção, o inspetor conferiu só as unidades alteradas e a lista de falhas; as intactas mantiveram a evidência da inspeção integral, com hash de unidade conferido como igual.
- Os 18 julgamentos do lote carregam o contrato v2 (`83ec8b16`). Os 3 do piloto carregam o contrato v1 (`d8b5e6e0`): foram revalidados por script na v2, com zero erros, e não foram rejulgados. A v2 só mudou o caminho das páginas.
- Aprovado não quer dizer sem ressalva: os 21 julgamentos publicados registram 174 ajustes menores, nenhum aplicado. Aplicar muda hash e pede nova conferência.
- O juiz não vê a fonte. Erro que o inspetor não registrou e que não aparece no texto da unidade passa pelos dois.
- Ninguém ouviu o áudio. Esta trilha só tem um material escrito (`G02_A12`), então erro de transcrição que mude o sentido não tem contraprova.

Validadores no fechamento: `base_fcc.py --partial --reviews --check` com **21 aulas, zero erros e 1 aviso** (`G01_A09`, fecho de temporada com 2 unidades, abaixo da faixa 3 a 60). 29 testes passando (`python3 -m unittest discover -s tests`, sem `CURSO` no ambiente). Inspeções e julgamentos publicados batem, por hash, com os JSON publicados. 100 registros de execução em `execucoes/lote-g01-g02/`: 85 do lote e 15 das três aulas do piloto.

Perfil das 169 unidades: 65 regras, 30 exemplos, 21 limites, 19 conceitos, 13 estruturas, 10 decisões, 8 réguas, 3 procedimentos. 69 perecíveis. Confiança alta em 121, média em 46, baixa em 2. Fonte: 159 só fala, 10 só material. Uma unidade com aviso de contorno de política em `nota`. Nenhuma `proposta_tag`.

Cobertura no alcance já extraído: 41 combinações tarefa × plataforma presentes e 622 ausentes; 20 das 39 tarefas e 18 dos 43 temas têm alguma unidade. Os ausentes são esperados com 21 de 139 entradas e estão explícitos em `cobertura.jsonl`.

### Consumo do lote 1, em tokens

| Papel | Modelo e esforço | Chamadas | Entrada nova | Cache lido | Saída | Raciocínio, dentro da saída | Tempo |
|---|---|---:|---:|---:|---:|---:|---:|
| Extrator | `claude-sonnet-5` `high` | 18 | 147.513 | 491.892 | 110.119 | 37.419 | 1.080 s |
| Reparo de contrato | `claude-sonnet-5` `high` | 4 | 48.003 | 113.888 | 6.079 | 1.586 | 54 s |
| Inspetor | `claude-sonnet-5` `xhigh` | 27 | 367.241 | 654.405 | 503.066 | 427.691 | 4.757 s |
| Redator | `claude-opus-5` `high` | 9 | 99.575 | 160.336 | 35.587 | 16.240 | 389 s |
| Juiz | `claude-fable-5-1` `xhigh` | 27 | 261.377 | 537.389 | 230.668 | 140.175 | 2.645 s |

Por modelo: Sonnet 5 com 619 mil tokens de saída e 563 mil de entrada nova em 49 chamadas; Fable 5.1 com 231 mil de saída e 261 mil de entrada nova em 27; Opus 5 com 36 mil de saída e 100 mil de entrada nova em 9. O inspetor é 57% da saída do lote e 85% da saída dele é raciocínio.

Primeira passagem por faixa de tamanho, tokens de saída por aula (extração, reparo, inspeção integral e primeiro julgamento):

| Faixa | Aulas medidas | Sonnet 5 | Fable 5.1 | O piloto supunha |
|---|---:|---:|---:|---|
| menos de 500 palavras | 1 (`G02_A01`, 5 unidades) | 21,5 mil | 7,5 mil | 8 mil e 2 mil, de uma aula de 1 unidade |
| 500 a 999 palavras | 5 | 18,3 mil (de 10,9 a 27,9) | 6,8 mil | 30 mil e 9 mil, por interpolação |
| 1.000 palavras ou mais | 12 | 36,2 mil (de 18,5 a 50,9) | 12,0 mil | 50 mil e 14 mil |

Um ciclo de correção custou em média 4,0 mil tokens de saída de Opus, 8,0 mil de Sonnet na conferência focal e 5,1 mil de Fable (9 aulas). No piloto tinha custado 8 mil, 23 mil e 6 mil.

### Correção da projeção

O piloto previa, para a primeira passagem destas 18 aulas, 758 mil tokens de saída de Sonnet e 215 mil de Fable. O medido foi 547 mil e 185 mil: 28% e 14% abaixo. A faixa de 500 a 999 palavras, que não tinha ponto medido, saiu 39% abaixo da interpolação. A reprovação na primeira rodada foi de 50%, entre os dois cenários do piloto (33% e 57%); somando o piloto, 11 de 24 aulas (46%).

Faltam 115 entradas: 10 com menos de 500 palavras, 27 de 500 a 999 e 78 com 1.000 ou mais. Tokens de saída que faltam, com a correção somada (50% de reprovação na primeira linha, como o lote 1; 57% na segunda, como o Formato Criativo):

| Cenário | Sonnet 5 | Fable 5.1 | Opus 5 | Chamadas |
|---|---:|---:|---:|---:|
| Aulas longas como as do lote 1 (36 mil e 12 mil por aula) | 3,9 milhões | 1,45 milhão | 0,23 milhão | cerca de 540 |
| Aulas longas como as do piloto (50 mil e 14 mil por aula) | 5,1 milhões | 1,65 milhão | 0,26 milhão | cerca de 570 |

A projeção anterior para as mesmas 133 entradas era de 6,4 a 7,1 milhões de Sonnet, 1,85 a 2,0 milhões de Fable e 0,33 a 0,57 milhão de Opus. Com o lote 1 medido e o restante projetado, fica em 4,5 a 5,7 milhões de Sonnet, 1,7 a 1,9 milhão de Fable e 0,27 a 0,30 milhão de Opus.

Erro que resta na projeção: o lote 1 é a trilha de texto, com aulas de 1.345 palavras em média e 7,4 unidades por aula. O que falta tem 2.013 palavras por aula em média e muita aula de tela, que o piloto mostrou render de 11 a 16 unidades quando é longa. O consumo acompanha o número de unidades, não o de palavras (4,1 mil tokens de saída de Sonnet por unidade na primeira passagem do lote 1). O cenário de cima da tabela é o mais provável para os grupos de edição (G05, G16) e de escala (G18). A entrada nova cresce com o tamanho da transcrição: estimativa de 4 a 5 milhões de Sonnet, 1,7 milhão de Fable e 0,7 a 1,0 milhão de Opus para o que falta.

Tempo de parede: 57 minutos para 18 aulas, sem espera por limite de sessão em 85 chamadas. No mesmo ritmo, o que falta pede de 7 a 9 horas de execução, fora espera por limite.

### Lote 2: G03 e G04 (Hard Ads, Criatividade e Roteirização), fechado em 21/09/2026

13 extrações novas, nenhuma aula do piloto nestes grupos.

| Aula | Palavras | Unidades | Contrato na 1ª saída | Inspeção com fonte | Julgamento | Correção | Status |
|---|---:|---:|---|---|---|---|---|
| `G03_A01` | 754 | 4 | limpa | integral, 1 omissão menor | **passa** de primeira | n/a | revisado |
| `G03_A02` | 1.548 | 5 (2 na extração) | 4 erros, todos em U2 (corpo, forma de `decisao`, faixa inválida, evidência não literal) | integral, 1 desvio (U2), 3 omissões materiais, 2 menores | falha (cobertura, fidelidade) → **passa** | reparo de contrato + ciclo 1 (U2 corrigida; U3, U4 e U5 criadas), focal | revisado |
| `G03_A03` | 787 | 2 | 1 erro (tarefas vazias em U1) | integral, 1 omissão menor | **passa** de primeira | reparo de contrato | revisado |
| `G03_A04` | 1.186 | 6 | limpa | integral, 1 desvio (U3) | falha (fidelidade) → **passa** | ciclo 1 (U3), focal | revisado |
| `G03_A05` | 1.642 | 3 | limpa | integral, 1 faixa errada (U1), 1 desvio (U2), 1 omissão menor | falha (fidelidade) → **passa** | ciclo 1 (U1, U2), focal | revisado |
| `G03_A06` | 389 | 1 | limpa, aviso de menos de 3 unidades | integral, sem apontamento | **passa** de primeira | n/a | revisado |
| `G04_A01` | 725 | 4 | limpa | integral, faixa errada em 2 de 3 (U1, U2), 2 omissões menores | falha (fidelidade) → **passa** | ciclo 1 (U1, U2; U4 criada), focal | revisado |
| `G04_A02` | 911 | 7 | 1 erro (título de U2 acima de 80 caracteres) | integral, faixa errada em 2 de 7 (U3, U4) | falha (fidelidade) → **passa** | reparo de contrato + ciclo 1 (U3, U4), focal | revisado |
| `G04_A03` | 1.592 | 15 | 1 erro (tarefas vazias em U13) | integral, 2 desvios (U4, U6), 1 omissão menor | falha (fidelidade) → **passa** | reparo de contrato + ciclo 1 (U2, U4, U5), focal | revisado |
| `G04_A04` | 2.500 | 9 | 1 erro (evidência de U8 fora da faixa) | integral, 1 desvio (U2), 1 omissão menor | falha (fidelidade, aplicabilidade) → **passa** | reparo de contrato + ciclo 1 (U2, U6), focal | revisado |
| `G04_A05` | 1.651 | 7 | 2 erros (tarefas vazias em U1 e U5) | integral, 1 desvio (U7) | **passa** de primeira | reparo de contrato | revisado |
| `G04_A06` | 569 | 4 | limpa | integral, 1 desvio (U4) | **passa** de primeira | n/a | revisado |
| `G04_A07` | 590 | 4 | limpa | integral, 1 desvio (U2), 1 omissão menor | falha (fidelidade) → **passa** | ciclo 1 (U2), focal | revisado |

Medido no lote (13 aulas, 14.844 palavras, 71 unidades publicadas):

- **13 de 13 aprovadas.** 5 passaram de primeira e 8 reprovaram na primeira rodada (62%). As 8 passaram no ciclo 1, com 18 unidades alteradas ou criadas pelo Opus 5. Nenhuma chegou ao ciclo 2, nenhuma ficou bloqueada, nenhuma foi reextraída.
- **Por que reprovaram:** fidelidade nas 8 aulas, aplicabilidade em 1, cobertura em 1; 17 falhas consolidadas.
  - Faixa que não cobre o que o corpo afirma em 4 aulas (`G03_A05`, `G04_A01`, `G04_A02`, `G04_A07`); `G04_A02` só tinha isso, e a correção pedida foi estender `fim` sem mexer no corpo.
  - Corpo que afirma além da fala ou troca a ordem e o papel do que a fonte diz (`G03_A04` U3, `G03_A05` U2, `G04_A03` U2, U4 e U5, `G04_A04` U2, `G04_A07` U2).
  - Grafia deformada fora da tabela tratada como termo (`G03_A02` U2) e identificação por hipótese sem `nota` (`G04_A04` U6, "Ads Libraria").
  - Tarefa que não corresponde ao corpo (`G04_A04` U6).
  - **Cobertura, primeira vez no curso:** `G03_A02` saiu da extração com 2 unidades para 1.548 palavras. O inspetor apontou 3 omissões materiais, o juiz vetou por cobertura e o Opus 5 criou 3 unidades no ciclo 1. O controle funcionou sem reextração.
- **Extrator sem raciocínio.** Em 7 das 13 extrações o Sonnet 5 em `high` respondeu com zero token de raciocínio (no lote 1, 5 de 18). Somando os dois lotes: das 12 extrações sem raciocínio, 8 reprovaram na primeira rodada (67%); das 19 com raciocínio, 9 (47%). A amostra é pequena e a diferença não é conclusiva. O esforço é o mesmo em todas; quem decide raciocinar é o modelo. Fica em observação.
- Erros de contrato na primeira saída: 10 em 6 aulas, 4 deles de `tarefas` vazia fora de `conceito` e `limite`. Nenhum marcador temporal. Todos fechados pelo reparo de contrato.
- **Zero citação não literal** nas 21 inspeções (13 integrais e 8 focais).
- 69 chamadas, todas `tool_use` e `completed`, sem recusa, sem erro de API e sem espera por limite de sessão. Tempo de parede: 46 minutos.
- `G04_A05` e `G04_A06` tinham desvio apontado pelo inspetor e passaram de primeira: o juiz os tratou como ajuste menor.

Validadores no fechamento: `base_fcc.py --partial --reviews --check` com **34 aulas, zero erros e 3 avisos** de menos de 3 unidades (`G01_A09`, `G03_A03`, `G03_A06`). As três são aulas curtas de abertura ou fecho.

Consumo do lote 2, em tokens:

| Papel | Modelo e esforço | Chamadas | Entrada nova | Cache lido | Saída | Raciocínio, dentro da saída | Tempo |
|---|---|---:|---:|---:|---:|---:|---:|
| Extrator | `claude-sonnet-5` `high` | 13 | 77.615 | 353.665 | 46.135 | 11.608 | 454 s |
| Reparo de contrato | `claude-sonnet-5` `high` | 6 | 52.182 | 204.975 | 9.870 | 2.638 | 88 s |
| Inspetor | `claude-sonnet-5` `xhigh` | 21 | 209.202 | 456.288 | 356.606 | 305.785 | 3.431 s |
| Redator | `claude-opus-5` `high` | 8 | 71.969 | 160.336 | 42.687 | 22.676 | 451 s |
| Juiz | `claude-fable-5-1` `xhigh` | 21 | 173.903 | 433.251 | 151.893 | 78.014 | 1.704 s |

Por modelo: Sonnet 5 com 413 mil tokens de saída e 339 mil de entrada nova em 40 chamadas; Fable 5.1 com 152 mil e 174 mil em 21; Opus 5 com 43 mil e 72 mil em 8.

Primeira passagem, tokens de saída por aula: 6 aulas de 500 a 999 palavras com 21,3 mil de Sonnet e 7,1 mil de Fable; 6 aulas de 1.000 ou mais com 29,4 mil e 11,2 mil; 1 aula de menos de 500 com 6,2 mil e 3,7 mil. Por unidade publicada: 4,4 mil de Sonnet e 1,6 mil de Fable (no lote 1, 4,1 mil e 1,4 mil). Um ciclo custou em média 5,3 mil de Opus, 12,8 mil de Sonnet e 4,8 mil de Fable.

Correção da projeção depois do lote 2. Faltam 102 entradas (9 com menos de 500 palavras, 21 de 500 a 999, 72 com 1.000 ou mais; 216.611 palavras, 2.124 por aula). Médias acumuladas de primeira passagem, lotes 1 e 2 mais o piloto: 11,9 mil de Sonnet e 4,4 mil de Fable abaixo de 500 palavras; 20,0 mil e 7,0 mil de 500 a 999; 33,9 mil e 11,7 mil com 1.000 ou mais (36,8 mil e 12,1 mil contando as quatro do piloto). Reprovação na primeira rodada acumulada: 17 de 31 nos lotes (55%), 19 de 37 com o piloto. Ciclo médio acumulado: 4,6 mil de Opus, 10,3 mil de Sonnet, 5,0 mil de Fable.

| Cenário para as 102 que faltam | Sonnet 5 | Fable 5.1 | Opus 5 | Chamadas |
|---|---:|---:|---:|---:|
| Médias dos lotes 1 e 2, 55% de reprovação | 3,5 milhões | 1,3 milhão | 0,26 milhão | cerca de 510 |
| Aulas longas como as do piloto (50 mil e 14 mil), 62% de reprovação | 4,8 milhões | 1,5 milhão | 0,29 milhão | cerca de 530 |

Já consumido em saída, do piloto ao lote 2: Sonnet 5 com 1,34 milhão, Fable 5.1 com 0,52 milhão, Opus 5 com 0,09 milhão. Total projetado do curso: 4,8 a 6,1 milhões de Sonnet, 1,8 a 2,0 milhões de Fable, 0,35 a 0,38 milhão de Opus. O erro que resta é o mesmo: os grupos que vêm agora (G05 a G08, edição e anúncios por nicho) têm aulas mais longas e de tela, e o consumo acompanha o número de unidades.

### Lote 3: G05 e G06 (Hard Ads, Edição e Produtos com Dores), fechado em 21/09/2026

17 extrações novas, nenhuma aula do piloto nestes grupos. Primeiro lote com aulas longas de tela.

| Aula | Palavras | Unidades | Contrato na 1ª saída | Inspeção com fonte | Julgamento | Correção | Status |
|---|---:|---:|---|---|---|---|---|
| `G05_A01` | 2.449 | 12 | 1 erro (marcador temporal em U3) | integral, 1 desvio (U5), 1 faixa errada (U12) | falha (fidelidade, aplicabilidade) → **passa** | reparo de contrato + ciclo 1 (U4, U5, U9, U10), focal | revisado |
| `G05_A02` | 5.542 | 17 | limpa | integral, 1 faixa errada (U11), 4 omissões menores | falha (aplicabilidade) → **passa** | ciclo 1 (U1), focal | revisado |
| `G05_A03` | 3.748 | 12 | limpa | integral, 1 faixa errada (U4), 2 omissões menores | **passa** de primeira | n/a | revisado |
| `G05_A04` | 1.098 | 6 | limpa | integral, 4 desvios (U2, U3, U4, U6), 1 omissão menor | falha (fidelidade) → **passa** | ciclo 1 (U3, U4, U6), focal | revisado |
| `G05_A05` | 538 | 1 | limpa, aviso de menos de 3 unidades | integral, sem apontamento | **passa** de primeira | n/a | revisado |
| `G06_A01` | 1.929 | 13 | limpa | integral, 1 desvio (U8), 1 perecível | **passa** de primeira | n/a | revisado |
| `G06_A02` | 1.710 | 6 | 2 erros (títulos de U1 e U2 acima de 80 caracteres) | integral, faixa errada em 2 de 6 (U2, U6) | falha (fidelidade) → **passa** | reparo de contrato + ciclo 1 (U2, U6), focal | revisado |
| `G06_A03` | 1.697 | 5 | 1 erro (marcador temporal em U2) | integral, 2 omissões menores | **passa** de primeira | reparo de contrato | revisado |
| `G06_A04` | 3.781 | 17 | 1 erro (corpo de U14 com 9 linhas) | integral, 3 omissões menores | **passa** de primeira | reparo de contrato | revisado |
| `G06_A05` | 2.661 | 11 | limpa | integral, faixa errada em 2 de 11 (U1, U6), 3 desvios (U3, U8, U11), 2 omissões menores | falha (fidelidade) → **passa** | ciclo 1 (U1, U6, U8, U9, U11), focal | revisado |
| `G06_A06` | 1.390 | 5 | limpa | integral, sem apontamento | **passa** de primeira | n/a | revisado |
| `G06_A07` | 3.220 | 12 | limpa | integral, 4 desvios (U3, U4, U7, U10), 3 omissões menores | falha (fidelidade) → **passa** | ciclo 1 (U3, U4, U7), focal | revisado |
| `G06_A08` | 2.341 | 11 | limpa | integral, 1 omissão menor | **passa** de primeira | n/a | revisado |
| `G06_A09` | 2.570 | 8 | limpa | integral, 2 omissões menores | **passa** de primeira | n/a | revisado |
| `G06_A10` | 2.701 | 9 | limpa | integral, 1 desvio (U7), 1 omissão menor | falha (fidelidade) → **passa** | ciclo 1 (U7), focal | revisado |
| `G06_A11` | 4.516 | 15 | limpa | integral, 3 omissões menores | **passa** de primeira | n/a | revisado |
| `G06_A12` | 402 | 1 | limpa, aviso de menos de 3 unidades | integral, sem apontamento | **passa** de primeira | n/a | revisado |

Medido no lote (17 aulas, 42.293 palavras, 161 unidades publicadas):

- **17 de 17 aprovadas.** 10 passaram de primeira e 7 reprovaram na primeira rodada (41%). As 7 passaram no ciclo 1, com 19 unidades alteradas pelo Opus 5. Nenhuma chegou ao ciclo 2, nenhuma ficou bloqueada, nenhuma foi reextraída.
- **Por que reprovaram:** fidelidade em 6 aulas e aplicabilidade em 2; 16 falhas consolidadas.
  - Passo ou efeito de tela que a fala não nomeia, e corpo que afirma além da fala (`G05_A04` U3, U4 e U6, `G06_A05` U11, `G06_A07` U3, U4 e U7, `G06_A10` U7). É o risco próprio da aula de tela e o juiz pegou pelo trecho literal do inspetor.
  - Caso de um anúncio virando regra geral (`G05_A01` U5) e exemplo que não se entende sem a aula (`G05_A01` U9 e U10).
  - Termo do vocabulário explicado com definição que não é a da fonte (`G06_A05` U8, "plot da música").
  - Faixa que não cobre o corpo em 2 aulas (`G06_A02`, `G06_A05`); nas duas a correção foi só de `fim`.
  - Tarefa que não corresponde ao corpo (`G05_A01` U4).
  - **Aviso de contorno de política cobrado pelo juiz:** `G05_A02` U1 descreve baixar vídeo de terceiros sem marca d'água e a `nota` não começava pela frase que o FORMATO exige. Foi a única falha da aula. A decisão de Will sobre essas técnicas está sendo aplicada pela rubrica.
- Extrator sem raciocínio em 1 das 17 extrações (`G06_A02`, que reprovou). Acumulado dos três lotes: 9 de 13 extrações sem raciocínio reprovaram na primeira rodada (69%), contra 15 de 35 com raciocínio (43%). Nas aulas longas o modelo quase sempre raciocina.
- Erros de contrato na primeira saída: 5 em 4 aulas, 2 deles de marcador temporal (2 em 161 unidades). Todos fechados pelo reparo.
- **Zero citação não literal** nas 24 inspeções (17 integrais e 7 focais). Nenhuma aula passou de 20 unidades, então não houve inspeção em blocos.
- 76 chamadas, todas `tool_use` e `completed`, sem recusa e sem erro de API.
- **Primeira espera por limite de sessão do curso.** Às 13h35 três conferências focais receberam HTTP 429 ("session limit, resets 3:10pm"). O executor esperou sozinho 1 h 36 min e retomou sem intervenção; nada se perdeu. Tempo de parede do lote: 2 h 50 min, das quais 1 h 14 min de execução. Referência para planejar: a janela de sessão que começou por volta das 10h10 comportou os lotes 1 e 2 inteiros e quase todo o lote 3, cerca de 48 aulas, junto com a sessão da coordenação.
- `G05_A03` e `G06_A01` tinham apontamento do inspetor (uma faixa errada em 12, um desvio) e passaram de primeira.

Validadores no fechamento: `base_fcc.py --partial --reviews --check` com **51 aulas, zero erros e 5 avisos** de menos de 3 unidades (`G01_A09`, `G03_A03`, `G03_A06`, `G05_A05`, `G06_A12`), todas aulas curtas de abertura, recado ou fecho.

Consumo do lote 3, em tokens:

| Papel | Modelo e esforço | Chamadas | Entrada nova | Cache lido | Saída | Raciocínio, dentro da saída | Tempo |
|---|---|---:|---:|---:|---:|---:|---:|
| Extrator | `claude-sonnet-5` `high` | 17 | 209.414 | 453.219 | 134.753 | 58.367 | 1.376 s |
| Reparo de contrato | `claude-sonnet-5` `high` | 4 | 51.767 | 109.247 | 6.919 | 1.589 | 57 s |
| Inspetor | `claude-sonnet-5` `xhigh` | 24 | 525.277 | 496.555 | 630.923 | 549.283 | 6.043 s |
| Redator | `claude-opus-5` `high` | 7 | 133.418 | 120.252 | 38.691 | 20.236 | 418 s |
| Juiz | `claude-fable-5-1` `xhigh` | 24 | 278.805 | 474.513 | 219.353 | 130.599 | 2.529 s |

Por modelo: Sonnet 5 com 773 mil tokens de saída e 786 mil de entrada nova em 45 chamadas; Fable 5.1 com 219 mil e 279 mil em 24; Opus 5 com 39 mil e 133 mil em 7. O tempo do inspetor não inclui a espera por limite.

Primeira passagem, tokens de saída por aula: 15 aulas de 1.000 palavras ou mais (2.757 em média, 10,6 unidades) com 44,8 mil de Sonnet e 11,7 mil de Fable; 1 aula de 500 a 999 com 12,4 mil e 3,2 mil; 1 aula de menos de 500 com 7,7 mil e 2,2 mil. Por unidade publicada: 4,3 mil de Sonnet e 1,1 mil de Fable. O custo de Sonnet por unidade ficou estável nos três lotes (4,1, 4,4 e 4,3 mil); o de Fable por unidade caiu (1,4, 1,6 e 1,1 mil), porque o juiz gasta um piso por aula e as aulas deste lote têm mais unidades. Um ciclo custou em média 5,5 mil de Opus, 11,6 mil de Sonnet e 5,4 mil de Fable.

Correção da projeção depois do lote 3. Faltam 85 entradas (8 com menos de 500 palavras, 20 de 500 a 999, 57 com 1.000 ou mais; 174.318 palavras). As 57 longas têm cerca de 2.750 palavras em média, o mesmo tamanho das longas deste lote, então a média do lote 3 é o melhor ponto para elas. Reprovação na primeira rodada acumulada: 24 de 48 nos lotes (50%), 26 de 54 com o piloto. Ciclo médio acumulado: 4,9 mil de Opus, 10,6 mil de Sonnet, 5,1 mil de Fable.

| Cenário para as 85 que faltam | Sonnet 5 | Fable 5.1 | Opus 5 | Chamadas |
|---|---:|---:|---:|---:|
| Médias acumuladas por faixa (10,9, 19,3 e 38,8 mil de Sonnet; 3,9, 6,6 e 11,7 mil de Fable), 50% de reprovação | 3,1 milhões | 1,05 milhão | 0,21 milhão | cerca de 410 |
| Aulas longas como as do lote 3 (44,8 mil de Sonnet), 55% de reprovação | 3,5 milhões | 1,1 milhão | 0,23 milhão | cerca de 420 |

Já consumido em saída, do piloto ao lote 3: Sonnet 5 com 2,11 milhões, Fable 5.1 com 0,74 milhão, Opus 5 com 0,13 milhão. Total projetado do curso: 5,2 a 5,6 milhões de Sonnet, 1,8 a 1,85 milhão de Fable, 0,34 a 0,36 milhão de Opus. A faixa estreitou porque o lote 3 deu o primeiro ponto medido de aula longa de tela em volume. Em janelas de sessão, o que falta pede cerca de duas janelas de 5 horas.

### Lote 4: G07 (Hard Ads, Negócios Locais), fechado em 22/09/2026

13 extrações novas, nenhuma aula do piloto neste grupo. Primeiro lote rodado em outro dia: o cache de prefixo dos papéis foi regravado na primeira chamada de cada um.

| Aula | Palavras | Unidades | Contrato na 1ª saída | Inspeção com fonte | Julgamento | Correção | Status |
|---|---:|---:|---|---|---|---|---|
| `G07_A01` | 3.787 | 12 | limpa | integral, 2 desvios (U6, U8), 3 omissões materiais | falha (fidelidade) → **passa** | ciclo 1 (U8), focal | revisado |
| `G07_A02` | 896 | 7 | limpa | integral, 1 desvio (U2) | **passa** de primeira | n/a | revisado |
| `G07_A03` | 588 | 5 | 1 erro (evidência de U5 fora da faixa) | integral, 2 desvios (U1, U5) | **passa** de primeira | reparo de contrato | revisado |
| `G07_A04` | 2.840 | 15 | limpa | integral, 2 desvios (U2, U8), 3 omissões menores | falha (fidelidade) → **passa** | ciclo 1 (U8), focal | revisado |
| `G07_A05` | 2.177 | 10 (9 na extração) | limpa | integral, 1 desvio (U8), 1 omissão material, 1 menor | falha (fidelidade, cobertura) → falha (fidelidade, na U10 criada) → **passa** na rodada 3 | ciclo 1 (U8; U10 criada) + ciclo 2 (U10), focal nos dois | revisado |
| `G07_A06` | 1.642 | 5 | 1 erro (título de U5 acima de 80 caracteres) | integral, 1 sem-lastro (U3) | falha (fidelidade, aplicabilidade) → **passa** | reparo de contrato + ciclo 1 (U3, U5), focal | revisado |
| `G07_A07` | 4.198 | 10 (9 na extração) | limpa | integral, faixa errada em 3 de 9 (U2, U3, U6), 1 desvio (U7), 3 omissões menores | falha (fidelidade, aplicabilidade) → **passa** | ciclo 1 (U2, U3, U6, U9; U10 criada), focal | revisado |
| `G07_A08` | 4.938 | 7 | limpa | integral, 1 desvio (U5), 1 omissão material, 1 menor | falha (fidelidade) → **passa** | ciclo 1 (U5), focal | revisado |
| `G07_A09` | 2.857 | 8 | limpa | integral, 1 faixa errada (U1), 2 desvios (U4, U5), 2 omissões menores | falha (fidelidade) → **passa** | ciclo 1 (U1, U5), focal | revisado |
| `G07_A10` | 1.410 | 4 | limpa | integral, sem apontamento | **passa** de primeira | n/a | revisado |
| `G07_A11` | 1.959 | 5 | 1 erro (título de U3 acima de 80 caracteres) | integral, 3 omissões menores | **passa** de primeira | reparo de contrato | revisado |
| `G07_A12` | 1.223 | 11 | limpa | integral, 2 desvios (U2, U7), 3 omissões menores, 2 perecíveis | **passa** de primeira | n/a | revisado |
| `G07_A13` | 314 | 1 | limpa, aviso de menos de 3 unidades | integral, sem apontamento | **passa** de primeira | n/a | revisado |

Medido no lote (13 aulas, 28.829 palavras, 100 unidades publicadas, 2 delas criadas na correção):

- **13 de 13 aprovadas.** 6 passaram de primeira e 7 reprovaram na primeira rodada (54%). 6 passaram no ciclo 1; **`G07_A05` é a primeira aula do curso a chegar ao ciclo 2**, e passou na rodada 3. Nenhuma ficou bloqueada, nenhuma foi reextraída. 15 unidades alteradas ou criadas pelo Opus 5.
- **Por que reprovaram:** fidelidade nas 7, aplicabilidade em 2, cobertura em 1; 12 falhas consolidadas na primeira rodada.
  - Caso, exemplo ou preferência do professor escrito como regra geral (`G07_A01` U8, `G07_A04` U8, `G07_A05` U8, `G07_A07` U3). É o padrão desta trilha: o professor constrói anúncios para uma loja de sapatos e uma de seminovos hipotéticas, e o extrator generaliza.
  - Passo de tela que a fala não sustenta (`G07_A06` U3, `G07_A08` U5, `G07_A09` U5).
  - Faixa que não cobre o corpo (`G07_A07` U2, U3 e U6; `G07_A09` U1).
  - Cobertura: o "hackzinho" da vinheta no Canva ficou fora de `G07_A05`; o inspetor apontou, o juiz vetou e o Opus criou a U10. A U10 criada atribuiu o ajuste de brilho ao elemento errado e reprovou na rodada 2; o ciclo 2 corrigiu com a fala conferida passo a passo.
  - Aplicabilidade: ferramenta citada como exemplo tratada como plataforma da unidade (`G07_A06` U5, ElevenLabs) e tema que levava ao lugar errado (`G07_A07` U9).
- `G07_A03` e `G07_A12` tinham desvios apontados (2 cada; `G07_A12` também 2 perecíveis) e passaram de primeira.
- Erros de contrato na primeira saída: 3 em 3 aulas (2 títulos longos, 1 evidência fora da faixa). Nenhum marcador temporal. Todos fechados pelo reparo.
- **Zero citação não literal** nas 21 inspeções (13 integrais, 8 focais).
- 66 chamadas, todas `tool_use` e `completed`, sem recusa, sem erro de API e sem espera por limite de sessão. Tempo de parede: 1 h 44 min (21 min de extração).

**Mudança de comportamento do modelo, medida, sem mudança nossa.** Mesma versão do CLI (2.1.273), mesmo hash do bloco fixo de cada papel, contrato e papéis sem edição desde 20 e 21/09. Mesmo assim:

| Papel | Raciocínio médio por chamada, lote 3 (21/09) | Lote 4 (22/09) | Razão |
|---|---:|---:|---:|
| Extrator, Sonnet 5 `high` | 3.433 (1 de 17 sem raciocínio) | 26.444 (0 de 13 sem raciocínio) | 7,7× |
| Inspetor integral, Sonnet 5 `xhigh` | 28.312 | 47.737 | 1,7× |
| Juiz 1ª rodada, Fable 5.1 `xhigh` | 6.701 | 9.106 | 1,4× |

A saída média do extrator foi de 7,9 mil para 30,4 mil tokens por aula. O cache lido subiu 68 tokens em todos os papéis (extrator de 21.212 para 21.280; inspetor de 21.728 para 21.796), o que aponta um prefixo do CLI diferente sem edição nossa. O contrato não mudou: os julgamentos do lote 4 carregam o mesmo `contrato_sha256` dos lotes 1 a 3. O efeito na qualidade não aparece: a reprovação na primeira rodada (54%) está na faixa dos lotes anteriores (41% a 62%), e as causas são as mesmas. O efeito no consumo aparece: 10,7 mil tokens de saída de Sonnet por unidade publicada, contra 4,1 a 4,4 mil nos lotes 1 a 3.

Validadores no fechamento: `base_fcc.py --partial --reviews --check` com **64 aulas, zero erros e 6 avisos** de menos de 3 unidades (`G01_A09`, `G03_A03`, `G03_A06`, `G05_A05`, `G06_A12`, `G07_A13`).

Consumo do lote 4, em tokens:

| Papel | Modelo e esforço | Chamadas | Entrada nova | Cache lido | Saída | Raciocínio, dentro da saída | Tempo |
|---|---|---:|---:|---:|---:|---:|---:|
| Extrator | `claude-sonnet-5` `high` | 13 | 173.393 | 285.865 | 395.191 | 343.774 | 3.803 s |
| Reparo de contrato | `claude-sonnet-5` `high` | 3 | 46.488 | 70.391 | 9.339 | 5.285 | 74 s |
| Inspetor | `claude-sonnet-5` `xhigh` | 21 | 395.115 | 457.716 | 787.053 | 733.609 | 7.494 s |
| Redator | `claude-opus-5` `high` | 8 | 152.153 | 212.081 | 39.189 | 19.298 | 431 s |
| Juiz | `claude-fable-5-1` `xhigh` | 21 | 226.483 | 412.620 | 234.401 | 171.850 | 3.051 s |

Por modelo: Sonnet 5 com 1,19 milhão de tokens de saída e 615 mil de entrada nova em 37 chamadas; Fable 5.1 com 234 mil e 226 mil em 21; Opus 5 com 39 mil e 152 mil em 8. O lote 3, com 17 aulas e 161 unidades, tinha custado 773 mil de Sonnet.

Primeira passagem, tokens de saída por aula: 10 aulas de 1.000 palavras ou mais (8,7 unidades) com 90,7 mil de Sonnet e 13,6 mil de Fable; 2 de 500 a 999 com 71,3 mil e 10,0 mil; 1 de menos de 500 com 16,8 mil e 4,4 mil. Um ciclo custou em média 5,2 mil de Opus, 16,0 mil de Sonnet e 9,5 mil de Fable. O Fable por unidade ficou em 1,6 mil, como nos lotes anteriores.

Correção da projeção depois do lote 4. Faltam 72 entradas (7 com menos de 500 palavras, 18 de 500 a 999, 47 com 1.000 ou mais; 145.489 palavras). Dois cenários, porque não se sabe se o comportamento de 22/09 fica:

| Cenário para as 72 que faltam | Sonnet 5 | Fable 5.1 | Opus 5 | Chamadas |
|---|---:|---:|---:|---:|
| Ritmo dos lotes 1 a 3 (médias acumuladas até 21/09), 50% de reprovação | 2,6 milhões | 0,9 milhão | 0,18 milhão | cerca de 350 |
| Ritmo do lote 4 (22/09), 54% de reprovação | 6,3 milhões | 1,2 milhão | 0,20 milhão | cerca de 350 |

Já consumido em saída, do piloto ao lote 4: Sonnet 5 com 3,30 milhões, Fable 5.1 com 0,97 milhão, Opus 5 com 0,17 milhão. Total projetado do curso: 5,9 a 9,6 milhões de Sonnet, 1,85 a 2,2 milhões de Fable, 0,35 a 0,37 milhão de Opus. A incerteza que domina agora é o ritmo do modelo, não o tamanho das aulas. O lote 5 mede em qual dos dois ele está.

### Lote 5: G08 e G09 (Hard Ads, Produtos Físicos e Recapitulando), fechado em 22/09/2026

16 extrações novas mais a ouro `G08_A05`, aprovada no piloto e publicada só agora. `G08_A06` chegou ao teto de dois ciclos por um limite do executor e foi resolvida no mesmo dia por decisão de Will (ver abaixo).

| Aula | Palavras | Unidades | Contrato na 1ª saída | Inspeção com fonte | Julgamento | Correção | Status |
|---|---:|---:|---|---|---|---|---|
| `G08_A01` | 3.524 | 13 | limpa | integral, 2 desvios (U6, U10), 2 omissões materiais, 2 menores | falha (fidelidade) → **passa** | ciclo 1 (U6), focal | revisado |
| `G08_A02` | 1.345 | 4 (3 na extração) | 1 erro (título de U2 acima de 80 caracteres) | integral, 1 faixa errada (U1), 1 desvio (U2), 1 omissão material, 1 menor | falha (fidelidade, cobertura, aplicabilidade) → falha (faixa de U3) → **passa** na rodada 3 | reparo de contrato + ciclo 1 (U1, U2, U3; U4 criada) + ciclo 2 (U3), focal nos dois | revisado |
| `G08_A03` | 1.142 | 7 | limpa | integral, 1 omissão menor, 2 citações não literais | falha (aplicabilidade: aviso de contorno ausente em U1 e U2) → **passa** | ciclo 1 (U1, U2), focal | revisado |
| `G08_A04` | 917 | 7 | limpa | integral, 2 desvios (U2, U5), 2 omissões menores | falha (fidelidade) → **passa** | ciclo 1 (U2, U5), focal | revisado |
| `G08_A05` ouro | 2.377 | 11 | piloto | piloto: integral + focal | piloto: falha → **passa** no ciclo 1; aceita como ouro por Will em 21/09 | ciclo 1 no piloto | ouro |
| `G08_A06` | 998 | 4 | limpa | integral, 1 faixa errada (U1), 1 desvio (U3) | falha (fidelidade) → falha → falha (teto de dois ciclos, só contexto) → **passa** na rodada 4 | ciclo 1 (U1, U3), ciclo 2 sem unidade alterada, contexto gravado por script pela coordenação com autorização de Will, conferência focal final | revisado |
| `G08_A07` | 2.001 | 7 | limpa | integral, 1 faixa errada (U7) | falha (fidelidade, aplicabilidade) → **passa** | ciclo 1 (U3, U7), focal | revisado |
| `G08_A08` | 1.072 | 6 | limpa | integral, 2 desvios (U1, U3) | falha (fidelidade) → **passa** | ciclo 1 (U1, U3), focal | revisado |
| `G08_A09` | 974 | 5 | limpa | integral, 1 faixa errada (U3), 1 desvio (U4), 2 omissões menores, 1 citação não literal | falha (fidelidade) → **passa** | ciclo 1 (U3, U4), focal | revisado |
| `G08_A10` | 1.079 | 5 | 3 erros (grafia deformada "Rádio Cop" no contexto e em U2; título de U4 acima de 80) | integral, 2 omissões menores, 1 citação não literal | falha (fidelidade) → **passa** | reparo de contrato (U2, U4) + contexto corrigido por script pela coordenação + ciclo 1 (U3), focal | revisado |
| `G09_A01` | 459 | 1 | limpa, aviso de menos de 3 unidades | integral, 1 desvio (U1) | falha (fidelidade) → **passa** | ciclo 1 (U1), focal | revisado |
| `G09_A02` | 1.207 | 6 | limpa | integral, 1 faixa errada (U3), 1 omissão material | falha (fidelidade) → **passa** | ciclo 1 (U3), focal | revisado |
| `G09_A03` | 777 | 6 | limpa | integral, 1 omissão menor | falha (fidelidade) → **passa** | ciclo 1 (U1), focal | revisado |
| `G09_A04` | 697 | 4 | limpa | integral, 1 desvio (U3) | **passa** de primeira | n/a | revisado |
| `G09_A05` | 5.255 | 22 (21 na extração) | 1 erro (título de U10 acima de 80) | integral em 2 blocos, 2 faixas erradas (U12, U20), 1 desvio (U19), 1 omissão material, 5 menores | falha (fidelidade, cobertura, aplicabilidade) → **passa** | reparo de contrato + ciclo 1 (U12, U19, U20; U22 criada), focal | revisado |
| `G09_A06` | 3.548 | 22 (20 na extração) | 1 erro (faixa inválida em U20) | integral, 2 omissões materiais, 1 menor | falha (cobertura) → **passa** | reparo de contrato + ciclo 1 (U16; U21 e U22 criadas), focal | revisado |
| `G09_A07` | 1.357 | 12 (11 na extração) | limpa | integral, 1 omissão material, 2 menores | falha (cobertura) → **passa** | ciclo 1 (U12 criada), focal | revisado |

Medido no lote (16 aulas novas, 26.352 palavras; 127 unidades novas publicadas mais 11 da ouro; 5 unidades criadas na correção):

- **16 de 16 aprovadas** (`G08_A06` depois da intervenção autorizada por Will, abaixo). Só `G09_A04` passou de primeira: **15 de 16 reprovaram na primeira rodada (94%)**, contra 41% a 62% nos lotes anteriores. 13 passaram no ciclo 1, `G08_A02` no ciclo 2 (a correção do ciclo 1 descreveu as três partes do anúncio dentro de U3 sem ampliar a faixa; o ciclo 2 ampliou `inicio` e passou), e `G08_A06` esgotou os dois ciclos. 30 unidades alteradas ou criadas pelo Opus 5.
- **Por que reprovaram:** fidelidade em 12 aulas, cobertura em 4, aplicabilidade em 4; 28 falhas consolidadas na primeira rodada.
  - Faixa que não cobre o corpo em 6 aulas (`G08_A02`, `G08_A06`, `G08_A07`, `G08_A09`, `G09_A02`, `G09_A05`).
  - Generalização, atribuição perdida ou critério da fonte omitido em 9 aulas (`G08_A01` U6, `G08_A02` U2, `G08_A04` U2 e U5, `G08_A06` U3, `G08_A08` U3, `G08_A09` U4, `G08_A10` U3, `G09_A01` U1, `G09_A03` U1, `G09_A05` U19).
  - **Cobertura em 4 aulas**, o maior número até aqui: `G08_A02`, `G09_A05`, `G09_A06` (2 omissões) e `G09_A07`. As aulas de recapitulação do G09 são longas e densas; o extrator deixou de fora passo de CapCut, exceção de sonorização e uma regra de texto na tela. 5 unidades criadas no ciclo 1, todas aprovadas.
  - **Aviso de contorno cobrado pelo juiz pela segunda vez:** `G08_A03` U1 e U2 (imagem de pessoa sem direito de uso; "antes" suavizado para passar na moderação) e `G09_A05` U19 (anúncio que o professor chama de "black"). A `nota` não começava pela frase exigida pelo FORMATO. É a única causa de reprovação de `G08_A03`.
  - Aplicabilidade: unidade que remete à "estrutura deste episódio" em vez de descrevê-la (`G08_A02` U3), ferramenta de exemplo tratada como plataforma (`G08_A07` U3) e tom de voz sem a escolha que a fala faz (`G08_A07` U7).
- **Primeiras citações não literais do inspetor no curso:** 4 em 3 inspeções (`G08_A03` 2, `G08_A09` 1, `G08_A10` 1), listadas pelo executor em `citacoes_nao_literais` e descartadas pelo juiz; nenhuma sustentou falha. Nas 106 inspeções anteriores eram zero.
- Erros de contrato na primeira saída: 6 em 4 aulas. Em `G08_A10` o reparo fechou os dois erros de unidade e deixou o do **contexto** (o reparo de contrato só recebe erros de unidade, por desenho do executor). A coordenação corrigiu a frase do contexto por script, com registro em `correcoes` (`por: script`, sem tocar em unidade), e rodou a aula sozinha por `fcc_lote.py` com o rótulo `lote-g08-g09-a10`; resumo mesclado em `lotes/g08-g09/resumo-lote-g08-g09-final.json`.
- Raciocínio do modelo continua no regime de 22/09: extrator com 24,7 mil tokens de raciocínio por chamada (lote 4: 26,4 mil), inspetor integral com 40,8 mil, juiz com 11,1 mil.
- 104 chamadas, todas `tool_use` e `completed`, sem recusa. **Uma espera por limite:** às 10h54 o juiz de `G08_A01` (ciclo 1) recebeu HTTP 429 "out of usage credits"; o executor esperou 30 minutos e retomou. É o limite de uso da assinatura, o mesmo que atingiu a sessão da coordenação no fim da manhã. Tempo de parede: 22 min de extração, 2 h 23 min de condução (com a espera) e 19 min da rodada de `G08_A10`.

**`G08_A06`: teto de dois ciclos por um limite do executor, não do conteúdo.** Na rodada 1 o juiz reprovou por dois pontos: U3 tratava como `regua` uma estimativa de preço do professor para o abajur fictício do anúncio comentado (R$ 79 de compra, R$ 169 a 189 de venda), e U1 tinha faixa curta. Pediu também que a frase 5 do `contexto` deixasse de chamar isso de "faixa de preço de referência". O Opus 5 corrigiu U1 e U3 no ciclo 1 (U3 virou `exemplo`, com `condicoes` dizendo que não é parâmetro de mercado) e escreveu a frase substituta do contexto nas observações, porque o contrato de saída do redator só transporta unidades. O executor não aplica mudança de contexto, então a frase original persistiu, e o juiz reprovou as rodadas 2 e 3 pela mesma falha, sem unidade envolvida. As 4 unidades estão certas e lastreadas; o que falta é uma frase do contexto que o juiz já ditou por extenso. O parecer da rodada 3 propõe: a coordenação grava a frase no JSON, uma conferência focal final com inspetor e juiz restrita a essa falha, e `bloqueado` se persistir. Versões em `lotes/g08-g09/`, `ciclo1/` e `ciclo2/`. **Will decidiu em 22/09/2026 seguir esse caminho.** A coordenação gravou a frase ditada pelo juiz em `lotes/g08-g09/final-a06/G08_A06.json`, com registro em `correcoes` (`ciclo: 3`, `por: script`, nenhuma unidade tocada; os quatro hashes de unidade conferidos iguais aos do ciclo 2). Conferência focal do inspetor (5,6 mil tokens de saída) e juiz na rodada 4 (6,3 mil): **passa**, zero falhas, 2 ajustes menores. Publicada; registros dos quatro ciclos em `execucoes/lote-g08-g09/`.

O mesmo limite do executor apareceu em 9 outras reprovações de primeira rodada nos lotes 2 a 5, em que o juiz pedia mudança de contexto junto com mudança de unidade; em todas o juiz aprovou o ciclo 1 sem a mudança de contexto aplicada, e nenhuma aula publicada carrega falha aberta. Will decidiu em 22/09/2026 fazer as duas coisas, e a coordenação implementou com teste antes do lote 8: (1) o esquema de saída do redator ganhou o campo `contexto` (lista de frases; vazia quando nenhuma falha pede mudança no contexto) e o executor o aplica, registrando `contexto: true` no histórico de `correcoes`; o papel `redator.md` não mudou; (2) o `fcc_lote.py` não abre o ciclo 2 quando o julgamento do ciclo 1 reprova só por falha sem unidade (fora cobertura) e o contexto não mudou entre as duas versões: a aula sai como "falha só de contexto não aplicada pelo redator: pendente para a coordenação". Junto, (3) o `fcc_lote.py` passou a retirar do contexto, antes do reparo de contrato, o parêntese que cita a grafia deformada da transcrição, como já fazia com o relógio; grafia deformada fora de parêntese continua indo para a coordenação. Testes em `tests/test_hardcopy.py` (`ContextoNoLote`, `RedatorContexto`); 33 testes passando. Nenhuma aula publicada foi tocada.

Validadores no fechamento: `base_fcc.py --partial --reviews --check` com **80 aulas, zero erros e 7 avisos** de menos de 3 unidades (`G01_A09`, `G03_A03`, `G03_A06`, `G05_A05`, `G06_A12`, `G07_A13`, `G09_A01`).

Consumo do lote 5, em tokens (inclui os ciclos de `G08_A06` e a rodada de `G08_A10`; a ouro `G08_A05` está no piloto):

| Papel | Modelo e esforço | Chamadas | Entrada nova | Cache lido | Saída | Raciocínio, dentro da saída | Tempo |
|---|---|---:|---:|---:|---:|---:|---:|
| Extrator | `claude-sonnet-5` `high` | 16 | 150.065 | 319.200 | 454.230 | 394.926 | 4.202 s |
| Reparo de contrato | `claude-sonnet-5` `high` | 4 | 93.214 | 173.909 | 17.081 | 8.696 | 148 s |
| Inspetor | `claude-sonnet-5` `xhigh` | 34 | 532.628 | 762.860 | 1.103.631 | 1.024.327 | 10.632 s |
| Redator | `claude-opus-5` `high` | 17 | 201.391 | 378.020 | 85.028 | 43.015 | 924 s |
| Juiz | `claude-fable-5-1` `xhigh` | 33 | 355.353 | 660.192 | 397.469 | 288.376 | 5.100 s |

Por modelo: Sonnet 5 com 1,57 milhão de tokens de saída e 776 mil de entrada nova em 54 chamadas; Fable 5.1 com 397 mil e 355 mil em 33; Opus 5 com 85 mil e 201 mil em 17. O tempo do juiz não inclui a espera de 30 minutos.

Primeira passagem, tokens de saída por aula: 10 aulas de 1.000 palavras ou mais (10,4 unidades) com 96,5 mil de Sonnet e 16,7 mil de Fable; 5 de 500 a 999 com 56,7 mil e 13,2 mil; 1 de menos de 500 com 29,8 mil e 7,3 mil. Por unidade: 9,8 mil de Sonnet e 1,8 mil de Fable. Um ciclo custou em média 5,3 mil de Opus, 18,5 mil de Sonnet e 9,4 mil de Fable (15 ciclos).

Correção da projeção depois do lote 5. Faltam 57 entradas fora da base: 56 por extrair (6 com menos de 500 palavras, 14 de 500 a 999, 36 com 1.000 ou mais; 119.137 palavras) e `G08_A06` pendente. Médias do regime de 22/09 (lotes 4 e 5 somados): 23,3 mil de Sonnet e 5,9 mil de Fable abaixo de 500 palavras; 60,9 mil e 12,3 mil de 500 a 999; 93,6 mil e 15,2 mil com 1.000 ou mais; ciclo de 5,3 mil de Opus, 17,7 mil de Sonnet e 9,4 mil de Fable; reprovação de 76% (22 de 29).

| Cenário para as 56 que faltam extrair | Sonnet 5 | Fable 5.1 | Opus 5 | Chamadas |
|---|---:|---:|---:|---:|
| Regime de 21/09 (lotes 1 a 3), 50% de reprovação | 2,0 milhões | 0,68 milhão | 0,14 milhão | cerca de 260 |
| Regime de 22/09 (lotes 4 e 5), 76% de reprovação | 5,1 milhões | 1,16 milhão | 0,22 milhão | cerca de 310 |

Já consumido em saída, do piloto ao lote 5: Sonnet 5 com 4,87 milhões, Fable 5.1 com 1,37 milhão, Opus 5 com 0,26 milhão. Total projetado do curso: 6,9 a 10,0 milhões de Sonnet, 2,05 a 2,55 milhões de Fable, 0,40 a 0,48 milhão de Opus. Dois lotes seguidos no regime novo tornam o cenário de cima o mais provável.

### Lote 6: G10 (Hard Sounds), fechado em 22/09/2026

7 extrações novas, nenhuma aula do piloto neste grupo.

| Aula | Palavras | Unidades | Contrato na 1ª saída | Inspeção com fonte | Julgamento | Correção | Status |
|---|---:|---:|---|---|---|---|---|
| `G10_A01` | 1.064 | 6 | limpa | integral, 1 omissão menor, 1 citação não literal | **passa** de primeira | n/a | revisado |
| `G10_A02` | 954 | 7 | 1 erro (evidência de U3 fora da faixa) | integral, 3 desvios (U2, U3, U5) | falha (fidelidade, aplicabilidade) → **passa** | reparo de contrato + ciclo 1 (U2, U7), focal | revisado |
| `G10_A03` | 443 | 3 | limpa | integral, 1 faixa errada (U2) | falha (fidelidade) → **passa** | ciclo 1 (U2), focal | revisado |
| `G10_A04` | 608 | 4 | 1 erro (grafia deformada "TapCut" no contexto) | integral, sem apontamento | falha (fidelidade) → **passa** | contexto corrigido por script pela coordenação + ciclo 1 (U1), focal | revisado |
| `G10_A05` | 856 | 5 (6 na extração) | limpa | integral, 2 desvios (U3, U5) | falha (fidelidade) → **passa** | ciclo 1 (U5 retirada), focal | revisado |
| `G10_A06` | 3.889 | 15 | limpa | integral, 3 desvios (U8, U13, U14), 3 omissões menores | falha (fidelidade) → **passa** | ciclo 1 (U13), focal | revisado |
| `G10_A07` | 1.857 | 9 | limpa | integral, 1 desvio (U1), 3 omissões menores, 1 perecível | falha (fidelidade, aplicabilidade) → **passa** | ciclo 1 (U1, U2), focal | revisado |

Medido no lote (7 aulas, 9.671 palavras, 49 unidades publicadas):

- **7 de 7 aprovadas.** Só `G10_A01` passou de primeira: 6 de 7 reprovaram na primeira rodada (86%). As 6 passaram no ciclo 1; nenhuma chegou ao ciclo 2. 7 unidades alteradas ou retiradas pelo Opus 5 (a única retirada do curso até aqui: `G10_A05` U5 repetia U4 sem a condição da fonte).
- **Por que reprovaram:** fidelidade nas 6, aplicabilidade em 2; 8 falhas consolidadas. Afirmação além da fala em 4 aulas (`G10_A02` U2, `G10_A04` U1 com a atribuição de 9×16 e 16×9 a criativo e VSL, `G10_A06` U13, `G10_A07` U1 com uma glosa inventada para "sentimentalismo", termo que o FORMATO lista como usado sem definição na fonte); faixa que não cobre o corpo em 1 (`G10_A03` U2); unidade redundante em 1 (`G10_A05`); plataforma específica onde a orientação é geral em 2 (`G10_A02` U7, `G10_A07` U2).
- `G10_A04` saiu da extração com o erro de contexto fora do alcance do reparo (mesmo caso de `G08_A10`); corrigido por script pela coordenação, com registro em `correcoes`, e rodado sozinho com o rótulo `lote-g10-a04`. Resumo mesclado em `lotes/g10/resumo-lote-g10-final.json`.
- 1 citação não literal (`G10_A01`), descartada pelo juiz. Regime de raciocínio de 22/09 mantido: extrator com 23,6 mil tokens de raciocínio por chamada, inspetor integral com 43,8 mil, juiz com 10,6 mil.
- 40 chamadas, todas `tool_use` e `completed`, sem espera por limite. Tempo de parede: 1 h 00 min mais 13 min da rodada de `G10_A04`.

Validadores no fechamento: `base_fcc.py --partial --reviews --check` com **87 aulas, zero erros e 7 avisos** de aula curta (os mesmos do lote 5).

Consumo do lote 6, em tokens:

| Papel | Modelo e esforço | Chamadas | Entrada nova | Cache lido | Saída | Raciocínio, dentro da saída | Tempo |
|---|---|---:|---:|---:|---:|---:|---:|
| Extrator | `claude-sonnet-5` `high` | 7 | 80.878 | 152.166 | 189.105 | 165.149 | 1.841 s |
| Reparo de contrato | `claude-sonnet-5` `high` | 1 | 28.244 | 25.554 | 3.354 | 1.712 | 31 s |
| Inspetor | `claude-sonnet-5` `xhigh` | 13 | 150.886 | 283.348 | 394.712 | 366.366 | 3.774 s |
| Redator | `claude-opus-5` `high` | 6 | 56.813 | 147.103 | 28.649 | 16.175 | 328 s |
| Juiz | `claude-fable-5-1` `xhigh` | 13 | 111.023 | 268.203 | 145.174 | 108.487 | 1.887 s |

Por modelo: Sonnet 5 com 587 mil tokens de saída e 260 mil de entrada nova em 21 chamadas; Fable 5.1 com 145 mil e 111 mil em 13; Opus 5 com 29 mil e 57 mil em 6. Por unidade publicada: 10,6 mil de Sonnet e 2,0 mil de Fable. Primeira passagem por aula: 87,7 mil de Sonnet e 16,5 mil de Fable acima de 1.000 palavras (3 aulas), 66,7 mil e 12,6 mil de 500 a 999 (3), 56,5 mil e 9,9 mil abaixo de 500 (1, `G10_A03`, em que o extrator gastou 47 mil tokens de raciocínio para 3 unidades). Ciclo médio: 4,8 mil de Opus, 11,2 mil de Sonnet, 8,0 mil de Fable.

Correção da projeção depois do lote 6. Faltam 49 entradas por extrair (5 com menos de 500 palavras, 10 de 500 a 999, 34 com 1.000 ou mais; 109.466 palavras), mais `G08_A06` pendente. Regime de 22/09 com os lotes 4, 5 e 6 somados: 34,4 mil de Sonnet e 7,2 mil de Fable abaixo de 500 palavras; 62,6 mil e 12,4 mil de 500 a 999; 92,8 mil e 15,3 mil com 1.000 ou mais; ciclo de 5,2 mil de Opus, 16,3 mil de Sonnet e 9,1 mil de Fable; reprovação de 78% (28 de 36).

| Cenário para as 49 que faltam extrair | Sonnet 5 | Fable 5.1 | Opus 5 | Chamadas |
|---|---:|---:|---:|---:|
| Regime de 21/09 (lotes 1 a 3), 50% de reprovação | 1,8 milhão | 0,61 milhão | 0,12 milhão | cerca de 230 |
| Regime de 22/09 (lotes 4 a 6), 78% de reprovação | 4,6 milhões | 1,03 milhão | 0,20 milhão | cerca de 270 |

Já consumido em saída, do piloto ao lote 6: Sonnet 5 com 5,46 milhões, Fable 5.1 com 1,51 milhão, Opus 5 com 0,29 milhão. Total projetado do curso: 7,3 a 10,0 milhões de Sonnet, 2,1 a 2,55 milhões de Fable, 0,41 a 0,49 milhão de Opus. Três lotes seguidos no regime novo: o cenário de baixo é o esperado.

### Lote 7: G11 e G12 (Hard IA), fechado em 22/09/2026

12 extrações novas, nenhuma aula do piloto nestes grupos. Trilha de ferramenta: a transcrição grafa Veo 3 como "VO3" o tempo todo.

| Aula | Palavras | Unidades | Contrato na 1ª saída | Inspeção com fonte | Julgamento | Correção | Status |
|---|---:|---:|---|---|---|---|---|
| `G11_A01` | 791 | 3 | limpa | integral, 1 omissão menor | **passa** de primeira | n/a | revisado |
| `G11_A02` | 2.188 | 13 | 1 erro (grafia "VO3" em U9) | integral, 3 desvios (U4, U7, U9), 2 omissões menores | **passa** de primeira | reparo de contrato | revisado |
| `G11_A03` | 3.720 | 14 | limpa | integral, 1 desvio (U3), 2 omissões menores | **passa** de primeira | n/a | revisado |
| `G11_A04` | 1.726 | 10 | 5 erros (4 títulos longos, evidência não literal em U8) | integral, 3 desvios (U1, U5, U7) | falha (fidelidade) → **passa** | reparo de contrato + ciclo 1 (U5), focal | revisado |
| `G11_A05` | 2.074 | 12 | limpa | integral, 2 desvios (U3, U7), 2 omissões menores, 1 citação não literal | falha (fidelidade) → **passa** | ciclo 1 (U1, U3, U7), focal | revisado |
| `G11_A06` | 568 | 2 | limpa, aviso de menos de 3 unidades | integral, sem apontamento | **passa** de primeira | n/a | revisado |
| `G12_A01` | 1.954 | 13 (10 na extração) | 3 erros (grafias "VO3" e "DSL") | integral, 2 desvios (U4, U6), 3 omissões materiais | falha (cobertura) → **passa** | reparo de contrato + ciclo 1 (U11, U12, U13 criadas), focal | revisado |
| `G12_A02` | 2.561 | 15 | 3 erros (grafia "VO3" no contexto e em U6; evidência não literal em U15) | integral, 1 faixa errada (U13), 2 omissões menores | falha (fidelidade) → **passa** | reparo de contrato + contexto por script + ciclo 1 (U7), focal | revisado |
| `G12_A03` | 3.057 | 4 | limpa | integral, 2 omissões menores | **passa** de primeira | n/a | revisado |
| `G12_A04` | 2.246 | 10 (9 na extração) | 2 erros (grafias "quinchotem" e "chat de PT") | integral, 1 desvio (U6), 1 omissão material, 1 menor | falha (cobertura) → **passa** | reparo de contrato + ciclo 1 (U10 criada), focal | revisado |
| `G12_A05` | 3.259 | 15 | 8 erros (grafia "VO3" no contexto e em 5 unidades; evidência não literal em U3) | integral, 1 desvio (U8), 1 omissão menor | falha (fidelidade) → **passa** | reparo de contrato + contexto por script + ciclo 1 (U8), focal | revisado |
| `G12_A06` | 1.796 | 15 (14 na extração) | limpa | integral, 3 desvios (U3, U6, U13), 1 omissão material | falha (fidelidade, cobertura) → **passa** | ciclo 1 (U3, U8; U15 criada), focal | revisado |

Medido no lote (12 aulas, 25.940 palavras, 126 unidades publicadas, 5 delas criadas na correção):

- **12 de 12 aprovadas.** 5 passaram de primeira e 7 reprovaram na primeira rodada (58%). As 7 passaram no ciclo 1; nenhuma chegou ao ciclo 2. 13 unidades alteradas ou criadas pelo Opus 5.
- **Por que reprovaram:** fidelidade em 5 aulas, cobertura em 3; 11 falhas consolidadas. Afirmação além da fala em 5 (`G11_A04` U5, `G11_A05` U3 e U7 com um piso de headline que a fala não dá, `G12_A02` U7 com passo de conferência inventado, `G12_A05` U8, `G12_A06` U3); cobertura em 3, com 5 unidades criadas (`G12_A01` três omissões materiais, `G12_A04` uma, `G12_A06` uma).
- **Erros de contrato na primeira saída: 22 em 7 aulas, o maior número do curso.** 15 são grafia deformada, quase todas "VO3" para Veo 3; a tabela do FORMATO pegou todas por script antes da inspeção. 2 estavam no `contexto` (`G12_A02`, `G12_A05`), fora do alcance do reparo, e a coordenação corrigiu por script, com registro em `correcoes`; as duas rodaram juntas com o rótulo `lote-g11-g12-a02a05` e o resumo mesclado está em `lotes/g11-g12/resumo-lote-g11-g12-final.json`. É o terceiro lote seguido com esse caso (`G08_A10`, `G10_A04`, agora duas): a citação da grafia deformada no contexto é hábito do extrator nesta trilha.
- 1 citação não literal (`G11_A05`), descartada pelo juiz. Regime de raciocínio de 22/09 mantido e um pouco acima: extrator com 29,9 mil tokens de raciocínio por chamada, inspetor integral com 52,9 mil, juiz com 9,8 mil.
- 63 chamadas, todas `tool_use` e `completed`, sem espera por limite. Tempo de parede: 21 min de extração, 1 h 06 min de condução, 35 min da rodada de `G12_A02` e `G12_A05`.

Validadores no fechamento: `base_fcc.py --partial --reviews --check` com **99 aulas, zero erros e 8 avisos** de aula curta (os 7 anteriores mais `G11_A06`).

Consumo do lote 7, em tokens:

| Papel | Modelo e esforço | Chamadas | Entrada nova | Cache lido | Saída | Raciocínio, dentro da saída | Tempo |
|---|---|---:|---:|---:|---:|---:|---:|
| Extrator | `claude-sonnet-5` `high` | 12 | 134.223 | 234.080 | 413.986 | 359.353 | 3.923 s |
| Reparo de contrato | `claude-sonnet-5` `high` | 6 | 105.277 | 162.870 | 35.446 | 18.838 | 274 s |
| Inspetor | `claude-sonnet-5` `xhigh` | 19 | 352.097 | 500.783 | 793.283 | 737.643 | 7.651 s |
| Redator | `claude-opus-5` `high` | 7 | 120.260 | 182.768 | 43.385 | 21.056 | 468 s |
| Juiz | `claude-fable-5-1` `xhigh` | 19 | 239.378 | 371.358 | 237.301 | 176.455 | 3.042 s |

Por modelo: Sonnet 5 com 1,24 milhão de tokens de saída e 592 mil de entrada nova em 37 chamadas; Fable 5.1 com 237 mil e 239 mil em 19; Opus 5 com 43 mil e 120 mil em 7. Por unidade publicada: 8,9 mil de Sonnet e 1,3 mil de Fable. Primeira passagem por aula: 104,3 mil de Sonnet e 14,4 mil de Fable acima de 1.000 palavras (10 aulas, 12,1 unidades por aula), 42,1 mil e 7,1 mil de 500 a 999 (2). Ciclo médio: 6,2 mil de Opus, 16,5 mil de Sonnet, 11,3 mil de Fable.

Correção da projeção depois do lote 7. Faltam 37 entradas por extrair (5 com menos de 500 palavras, 8 de 500 a 999, 24 com 1.000 ou mais; 83.526 palavras), mais `G08_A06` pendente. Regime de 22/09 com os lotes 4 a 7 somados: 34,4 mil de Sonnet e 7,2 mil de Fable abaixo de 500 palavras; 59,2 mil e 11,5 mil de 500 a 999; 96,3 mil e 15,0 mil com 1.000 ou mais; ciclo de 5,4 mil de Opus, 16,3 mil de Sonnet e 9,6 mil de Fable; reprovação de 73% (35 de 48).

| Cenário para as 37 que faltam extrair | Sonnet 5 | Fable 5.1 | Opus 5 | Chamadas |
|---|---:|---:|---:|---:|
| Regime de 21/09 (lotes 1 a 3), 50% de reprovação | 1,3 milhão | 0,45 milhão | 0,09 milhão | cerca de 175 |
| Regime de 22/09 (lotes 4 a 7), 73% de reprovação | 3,4 milhões | 0,75 milhão | 0,15 milhão | cerca de 200 |

Já consumido em saída, do piloto ao lote 7: Sonnet 5 com 6,70 milhões, Fable 5.1 com 1,75 milhão, Opus 5 com 0,33 milhão. Total projetado do curso: 8,0 a 10,1 milhões de Sonnet, 2,2 a 2,5 milhões de Fable, 0,42 a 0,48 milhão de Opus. O que falta são os grupos do 0 a 100K (G13 a G18), com `G16_A02` e `G16_A09` já aprovadas no piloto.

### Defeitos de script vistos no lote 1, sem efeito sobre aula publicada

- `fcc_publicar.py` não cria `conhecimento/dados/` na primeira publicação de um curso. A coordenação criou a pasta antes de publicar.
- `fcc_relatorio.py` só enxerga códigos `Mxx_Ayy`. O consumo deste README foi somado pela coordenação direto dos `.execucao.json`, com script que reproduz os números do piloto.

## Pendências

- 37 entradas por extrair depois do lote 7 (G13 a G18, trilha 0 a 100K; `G16_A02` e `G16_A09` já aprovadas no piloto entram na publicação do lote delas). **Processamento pausado por Will em 22/09/2026 depois do fechamento do lote 7; nenhum processo rodando, lote 8 não lançado.** As mudanças de script de 22/09 (campo `contexto` do redator, parada em falha só de contexto, parêntese de grafia deformada) valem a partir do lote 8. `G08_A05` (ouro), `G16_A02` e `G16_A09` já estão aprovadas no piloto e entram na publicação do lote do grupo delas.
- Retranscrição com o vocabulário do curso: no final, por decisão de Will.
- Commit e push: feitos em 22/09/2026 a pedido de Will (`fe5be93` corrige o Formato Criativo, `684a085` publica esta base); os próximos, só quando ele pedir. Base parcial copiada para a Biblioteca do Jarvis 4 na mesma data, só derivados de leitura.
