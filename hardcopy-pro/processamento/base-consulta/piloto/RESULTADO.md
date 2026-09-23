# Resultado do piloto — Hardcopy Pro

20/09/2026. Plano em [../PLANO.md](../PLANO.md), fixado antes das execuções. Todos os números abaixo saem dos arquivos `.execucao.json`, `.inspecao.json` e `.julgamento.json` de `s5-high/`, `s5-high/ciclo1/`, `s5-high/final/` e `../calibracao/plantado/`.

Via de todas as chamadas: assinatura do Claude Code, `claude -p` headless 2.1.273, sem ferramentas, um processo isolado por chamada. Batch API não existe nesta via. O consumo é cota da assinatura e está medido em tokens. As 32 chamadas do piloto e da calibração terminaram com `stop_reason: tool_use` e `terminal_reason: completed`, sem recusa, sem erro de API e sem espera por limite de sessão.

Papéis: extrator e reparo de contrato Sonnet 5 `high`; inspetor Sonnet 5 `xhigh`, em execução separada; redator de correções Opus 5 `high`; juiz Fable 5.1 `xhigh`, sem transcrição, material nem repositório. A coordenação não escreveu nem reescreveu unidade.

## O que o piloto testou e o que deu

Seis entradas, escolhidas pelo que têm de difícil, não por serem típicas. O piloto não repetiu a comparação de extratores: o primeiro curso decidiu Sonnet 5 `high` com evidência.

| Aula | O que testa | Palavras | Unidades | Contrato na 1ª saída | Inspeção | Juiz, 1ª rodada | Ciclos | Estado |
|---|---|---:|---:|---|---|---|---:|---|
| `G02_A05` ouro | texto, régua 60/20, copy fictícia com números | 1.681 | 10 | 1 erro ("hoje" em U001) | 0 desvio, 1 faixa errada menor | **passa** | 0 | aprovada |
| `G08_A05` ouro | tela (Canva, ElevenLabs), trecho alucinado em inglês | 2.377 | 11 | 1 erro (âncora de U002 fora da faixa) | U002 e U006 com desvio, 2 de 11 faixas erradas, tudo classificado como menor | falha: fidelidade, aplicabilidade | 1 | aprovada no ciclo 1 |
| `G16_A02` | a mais longa, tela, laço de silêncio | 9.686 | 16 | limpa | 0 desvio, 3 omissões menores | **passa** | 0 | aprovada |
| `G02_A11` | VSL fictícia com números | 2.304 | 15 | 2 erros ("hoje" em U009 e U012) | 1 desvio menor (U009) | **passa** | 0 | aprovada |
| `G02_A12` | material avulso, sem transcrição | 0 (526 de material) | 10 | limpa no validador da hora; ver abaixo | 0 desvio; cópia bruta apontada em `contrato` | falha: contrato | 1 + conferência final | aprovada na rodada 3 |
| `G16_A09` | 205 palavras, sem conteúdo | 205 | 1 | limpa, aviso esperado | lastreada | **passa** | 0 | aprovada |

Seis de seis aprovadas. Quatro passaram de primeira. Zero citação não literal do inspetor nas 8 inspeções do piloto (6 integrais e 2 focais). Os quatro erros de contrato da primeira saída foram resolvidos pelo reparo de contrato (Sonnet 5 `high`, ciclo 0), antes da inspeção e fora da contagem de ciclos.

Leitura por aula:

- **`G02_A05`.** A copy fictícia de emagrecimento ficou como `exemplo`, com `condicoes` dizendo que preço, parcelas, garantia e credenciais são do texto inventado; nenhum número virou régua. A ambiguidade da fala ("O protagonista é 60%" e depois "O protagonista é 20%") foi preservada com `nota` e `confianca: media`. 9 ajustes menores registrados, nenhum aplicado.
- **`G08_A05`.** Reprovou por quatro falhas localizadas: 2 de 11 faixas erradas (18%, acima do teto de 10%); U002 listava cinco partes de anúncio com rótulos que o professor não usa ("Dor", "Promessa", "Chamada final"), quando a fala dá três movimentos; U006 tinha tema que levava ao lugar errado e uma condição inventada ("com o produto em mãos, valem as imagens do próprio produto"). O inspetor tinha classificado os quatro apontamentos como menores; o juiz os tratou como falha, o que repete a lição do primeiro curso de que gravidade é decisão do juiz e qualquer `desvio` leva a aula a ele. O Opus 5 corrigiu U001, U002, U006 e U007, a conferência focal confirmou e o juiz aprovou. O trecho alucinado em inglês (vozes de amostra do ElevenLabs) não foi usado como fonte. A técnica de baixar vídeo de terceiros do TikTok saiu com `perecivel: true` e a `nota` de contorno exigida.
- **`G16_A02`.** A aula mais longa rendeu 16 unidades e a extração usou 11.386 tokens de saída, 18% do teto de 64 mil do CLI. O risco de teto que existia no primeiro curso não existe aqui. O trecho degradado de 14:01 a 14:31 não foi usado.
- **`G02_A11`.** A VSL fictícia com números passou: os números ficaram em `exemplo`. O único `desvio` (U009, "terceira pessoa até o ponto de virada", que a fonte não diz) foi julgado ajuste menor.
- **`G16_A09`.** Uma unidade `limite`, como o FORMATO pede para aula sem conteúdo didático.

### Desvio de processo: a ouro `G08_A05` foi ao redator sem passar por Will

A rubrica diz que referência ouro que reprova vai para decisão humana e não entra na fila do redator. O `fcc_lote.py` não distingue ouro: a aula reprovou na rodada 1 e seguiu sozinha para o Opus 5. O resultado foi bom (quatro falhas localizadas, todas aceitas pelo critério, nenhuma falha nova), mas a decisão era de Will. Fica para ele confirmar `G08_A05` do `ciclo1/` como ouro. Não há mais aula ouro nos lotes, então o defeito do script não se repete; fica registrado.

## O bloqueio de `G02_A12` e o defeito de validador que ele revelou

O juiz reprovou a primeira versão por cópia bruta do material em U006 e U009 e perguntou por que `base_fcc.py` tinha dado zero erro. O redator parafraseou as duas no ciclo 1. Na rodada 2 o juiz bloqueou, sem gastar o ciclo 2, pedindo prova de ferramenta: as unidades estavam certas, faltava mostrar que a checagem roda contra o material.

Causa, medida: a checagem de 25 palavras comparava texto cru. O Markdown do material (ênfase com asterisco, marcadores de lista) e as marcações de tempo da transcrição quebravam a sequência. Era erro do pacote compartilhado, não falta de leitura do material. A sessão anterior da coordenação corrigiu: a comparação passou a ser por sequência de palavras, a mesma normalização da âncora. Prova em `tests/test_hardcopy.py`, `test_prova_pedida_pelo_juiz_no_piloto`.

Medição com o validador corrigido (`base_fcc.py` sha `bd90c4c5…`), maior sequência de palavras idêntica ao material:

| Unidade | v1 | ciclo 1 |
|---|---:|---:|
| U006 | 30, erro | 8 |
| U009 | 49, erro | 6 |
| U008 | 24 | 24 |
| U007 | 21 | 21 |
| demais | 7 a 19 | iguais |

A prova foi levada ao juiz em `s5-high/final/` (rodada 3, 4.652 tokens de saída), por um argumento novo do executor, `--prova`, que anexa saída de script ao pacote do juiz sem transcrição, material nem caminho do clone. Veredito: **passa**, zero falhas, ciclo 2 não consumido. U008 fica a uma palavra do limite; está dentro do contrato.

Alcance do defeito:

- As outras cinco aulas do piloto continuam com zero erros no validador corrigido.
- **Formato Criativo, já fechado:** com a checagem corrigida, `base_fcc.py --reviews --check` acusa 4 unidades com cópia de 25 palavras que passaram despercebidas: `M02_A03` U018, `M03_A01` U011, `M03_A02` U015 e `M04_A04` U013. Não foram corrigidas. Decisão de Will: corrigir pelas vias normais ou registrar como limitação. Enquanto isso o `--check` do primeiro curso falha nesta branch, de propósito.

## Calibração com erro plantado

Nove defeitos plantados pela coordenação em cópias das duas ouro aprovadas (`G02_A05` de `s5-high/`, `G08_A05` de `s5-high/ciclo1/`), por `../calibracao/plantar.py`. Gabarito em `../calibracao/gabarito.json`, fora de qualquer pacote. As duas cópias passam no validador: nenhum dos nove é contável por script. Inspetor e juiz rodaram sem saber do gabarito. Seis classes vêm do primeiro curso e três são próprias deste.

| Defeito | Onde | Inspetor | Juiz |
|---|---|---|---|
| P1 número adulterado (60% do protagonista virou 70%, no corpo e na nota, com âncora trocada) | `G02_A05` U002 | desvio, material; achou as duas ocorrências de 60% | fidelidade ✔ |
| P2 condição suprimida ("se você é o expert" virou "qualquer que seja o produto") | `G02_A05` U007 | desvio, material | fidelidade ✔ |
| P3 **número de copy fictícia promovido a régua** (12 × R$ 9,90 e garantia de 7 dias) | `G02_A05` U009 | desvio, material; separou a origem de cada número e mostrou que o professor nega a garantia no fecho | fidelidade ✔ |
| P4 omissão (retirada a regra de dispensar garantia, valor e feedbacks) | `G02_A05` | omissão material, com trecho e tempo (573 s) | cobertura ✔ |
| P5 perecível escondido em unidade `geral` (preço de 99 reais, `perecivel: false`) | `G02_A05` U006 | apontou em perecibilidade | perecibilidade ✔ |
| P6 estimativa verbal promovida a régua ("um videozinho ali de 2, 3 minutos" virou "deve ter") | `G08_A05` U003 | desvio, material | fidelidade ✔ |
| P7 unidade sem lastro com âncora literal verdadeira (3000 K e melatonina, conhecimento externo) | `G08_A05` U012 | sem-lastro, material | fidelidade ✔ |
| P8 **passo de tela inventado** (copiar link, sem marca d'água, aba Uploads, zerar volume) | `G08_A05` U006 | sem-lastro, material; listou o que a fala sustenta e o que não | fidelidade ✔ |
| P9 **grafia deformada promovida a outro conceito** ("Cetix" virou painel, "linha leve" virou versão do modelo, sem nota e com confiança alta) | `G08_A05` U010 | sem-lastro, material | fidelidade ✔ |

**9 de 9 detectados, cada um pelo veto esperado.** Zero citação não literal. Nenhum veto falso sobre unidade intacta. No primeiro curso tinham sido 6 de 7, e o que escapou (perecível sem marca) é o P5 daqui, agora apontado pelos dois: a lista de perecíveis da rubrica e do papel do inspetor, ampliada depois daquela calibração, funcionou. Papéis e rubrica seguem como estão; nada a corrigir antes do lote.

Parte contável do defeito de grafia, conferida por script e não por modelo: trocar "Kishotenketsu" por "Kim Shu" no corpo de `G02_A05` U010 faz o validador devolver erro de contrato. Forma deformada que está na tabela do FORMATO nunca chega ao inspetor; a que não está (caso do P9) depende dele, e ele pegou.

Ruído medido: a unidade intacta `G08_A05` U008 saiu `lastreada` com ajuste menor na inspeção do piloto e `desvio` menor na da calibração, com a mesma fonte e o mesmo texto. O juiz tratou como ajuste menor nas duas vezes. Confirma que a gravidade do inspetor oscila e que a decisão tem de ser do juiz.

Consumo da calibração: 4 chamadas; inspetor com 20 mil e 31 mil tokens de saída, juiz com 13 mil e 14 mil.

## Defeitos do pacote achados no piloto

| Defeito | De quem | Estado |
|---|---|---|
| Cópia de 25 palavras comparada em texto cru não via cópia atravessando Markdown nem marcação de tempo | validador | corrigido, com teste; achou 4 unidades no curso já fechado |
| Juiz sem canal para receber prova de ferramenta | executor | corrigido: `julgar --prova <arquivo>`, com hash da prova no registro da execução |
| "hoje" no corpo em 3 unidades de 2 aulas | extrator | papel do extrator ganhou uma linha proibindo "hoje", "atualmente" e "neste momento". As seis extrações do piloto são anteriores a ela; o efeito só se mede no lote 1 |
| Aula ouro reprovada segue para o redator sem decisão humana | `fcc_lote.py` | não corrigido; não há mais ouro nos lotes |
| Na conferência focal, os itens de `contrato` da inspeção anterior são acumulados mesmo quando a correção já os resolveu. O juiz precisou descartá-los à mão em `G08_A05` e `G02_A12` | executor | não corrigido; custa atenção do juiz, não mudou veredito |

Nenhuma mudança em FORMATO, taxonomia, rubrica, papel do inspetor, do juiz ou do redator depois do começo do piloto. O cache de prefixo desses papéis está íntegro (20.123 tokens lidos pelo juiz e 21.220 pelo inspetor a partir da segunda chamada).

## Consumo medido

Medida em tokens, por decisão de Will em 21/09/2026: o que interessa é a cota da assinatura, não o custo nominal em dólar, que saiu deste relatório. Os registros brutos de execução guardam os quatro contadores, o raciocínio, a via e o `stop_reason`. "Entrada nova" é `input` mais `cache_creation`; "cache lido" é o bloco fixo do papel relido a cada chamada. Token de Fable e de Opus pesa mais na cota que token de Sonnet, por isso a conta é separada por modelo. O CLI não informa quanto da cota cada chamada consumiu.

Piloto, seis aulas, até a aprovação de todas (28 chamadas):

| Papel | Modelo e esforço | Chamadas | Entrada nova | Cache lido | Saída | Raciocínio, dentro da saída | Tempo |
|---|---|---:|---:|---:|---:|---:|---:|
| Extrator | Sonnet 5 `high` | 6 | 92.708 | 103.070 | 48.058 | 21.821 | 494 s |
| Reparo de contrato | Sonnet 5 `high` | 3 | 54.810 | 97.876 | 5.426 | 1.091 | 45 s |
| Inspetor | Sonnet 5 `xhigh` | 8 | 176.003 | 190.392 | 204.991 | 176.885 | 1.954 s |
| Redator | Opus 5 `high` | 2 | 40.478 | 19.534 | 12.120 | 5.588 | 126 s |
| Juiz | Fable 5.1 `xhigh` | 9 | 121.486 | 160.984 | 112.677 | 76.953 | 1.312 s |

Por modelo: Sonnet 5 com 258 mil tokens de saída e 324 mil de entrada nova; Fable 5.1 com 113 mil de saída e 121 mil de entrada nova; Opus 5 com 12 mil de saída e 40 mil de entrada nova. Calibração, 4 chamadas: Sonnet 5 com 51 mil de saída, Fable 5.1 com 27 mil.

Por aula, em milhares de tokens (entrada nova / cache lido / saída):

| Aula | Sonnet 5 | Fable 5.1 | Opus 5 | Observação |
|---|---|---|---|---|
| `G02_A05` | 91 / 28 / 40 | 30 / 0 / 11 | — | primeira chamada de cada papel: gravou o bloco fixo em cache, por isso a entrada nova alta |
| `G02_A11` | 42 / 61 / 52 | 14 / 20 / 17 | — | |
| `G16_A02` | 86 / 42 / 51 | 13 / 20 / 13 | — | 9.686 palavras |
| `G16_A09` | 4 / 42 / 8 | 3 / 20 / 2 | — | 205 palavras |
| `G08_A05` | 81 / 155 / 74 | 27 / 40 / 20 | 35 / 0 / 8 | primeira passagem: Sonnet 40 / 92 / 51, Fable 11 / 20 / 14 |
| `G02_A12` | 19 / 63 / 34 | 36 / 60 / 49 | 5 / 20 / 4 | o bloqueio custou duas rodadas a mais de juiz: 31 mil tokens de saída de Fable |

O que os números dizem:

- **O maior volume de tokens é raciocínio do inspetor.** 177 mil dos 205 mil tokens de saída do inspetor são raciocínio em `xhigh`. Em volume, o inspetor é 53% da saída do piloto e o juiz 29%. O juiz roda no modelo mais pesado para a cota.
- **O extrator é 13% da saída.** Baixar o esforço dele não economiza e piora o que chega aos outros dois.
- **O consumo por aula quase não depende do tamanho da transcrição** entre 1,7 mil e 9,7 mil palavras: cerca de 50 mil tokens de saída de Sonnet e 14 mil de Fable na primeira passagem. Depende do número de unidades e da evidência que o juiz lê.
- **Um ciclo de correção custa quase meia primeira passagem**: 8 mil de saída de Opus, 23 mil de Sonnet na conferência focal e 6 mil de Fable. A taxa de reprovação é o que mais mexe no total.
- **Alavanca de economia ainda não testada:** inspetor em `high` em vez de `xhigh`. A calibração com os nove defeitos plantados permite medir isso com duas chamadas: se o inspetor em `high` pegar os nove, o esforço cai para o curso inteiro. Fica como opção de Will; a configuração vigente é `xhigh`.

## Projeção para o curso

Faltam 133 entradas. Primeira passagem, por faixa de tamanho, com o que o piloto mediu (tokens de saída por aula):

| Faixa | Entradas que faltam | Sonnet 5 | Fable 5.1 | Base |
|---|---:|---:|---:|---|
| menos de 500 palavras | 11 | 8 mil | 2 mil | `G16_A09` |
| 500 a 999 palavras | 32 | 30 mil | 9 mil | **sem ponto medido**; interpolação |
| 1.000 palavras ou mais | 90 | 50 mil | 14 mil | média das quatro aulas medidas |

Total estimado que falta, em tokens de saída, com a correção somada:

| Cenário | Reprovação na 1ª rodada | Sonnet 5 | Fable 5.1 | Opus 5 | Chamadas |
|---|---:|---:|---:|---:|---:|
| Como o piloto | 33% (2 de 6; uma por defeito de validador já corrigido) | 6,4 milhões | 1,85 milhão | 0,33 milhão | cerca de 570 |
| Como o Formato Criativo | 57% (31 de 54) | 7,1 milhões | 2,0 milhões | 0,57 milhão | cerca de 660 |

Entrada nova estimada: 6 a 7 milhões de tokens de Sonnet, 2 a 2,5 milhões de Fable, 1,4 a 2,4 milhões de Opus. O cache lido fica na ordem de 10 milhões de Sonnet e 3,5 milhões de Fable.

Erro da projeção: seis aulas, nenhuma na faixa de 500 a 999 palavras, que tem 32 entradas. O lote 1 (G01 e G02, 18 entradas novas) corrige o número.

Tempo de parede: o lote do piloto levou 36 minutos para seis aulas com três chamadas em paralelo e um ciclo de correção; o lote 1 deve levar de 1,5 a 2,5 horas e o curso inteiro de 12 a 16 horas de execução, fora espera por limite de sessão. O piloto não bateu no limite em 32 chamadas; o curso vai bater, e o executor espera sozinho.

## Mudança de contrato depois do piloto, antes do lote 1

Decisão de Will em 21/09/2026: a biblioteca espelha o curso. Páginas de aula e índice passam a seguir as pastas, os nomes e a ordem que o criador deu (5 trilhas, 18 grupos, material em `Materiais/`); `unidades.jsonl` e `cobertura.jsonl` continuam únicos e ganham `grupo` e `pagina` por linha. FORMATO v2: muda só a seção 6 e o gerador (`page_path` em `base_fcc.py`, com teste). Nenhuma regra de unidade mudou.

Efeito: o hash do contrato mudou, então o cache de prefixo dos papéis é regravado na primeira chamada do lote 1. As seis aulas do piloto foram revalidadas por script no contrato novo, com zero erros, e não foram rejulgadas: os seis julgamentos carregam o hash do contrato v1, e isso fica registrado como limite, igual ao que o primeiro curso fez com `M05_A02`.

## Decisões de Will, 21/09/2026

1. `G08_A05` na versão do `ciclo1/` aceita como ouro, depois da leitura de `ouro-G08_A05-para-aprovacao.md`.
2. Mantidas as cinco decisões da coordenação. A primeira ganhou forma nova: base única de dados, com páginas e índice espelhando as pastas do curso. O material "Surpresa" fica em `Materiais/01 Hard Copy/`.
3. As 4 unidades do Formato Criativo com cópia bruta foram corrigidas pelas vias normais e publicadas; o `--check` de lá voltou a zero erros.
4. Consumo relatado em tokens. Inspetor continua em `xhigh`.
5. Retranscrição com o vocabulário do curso: fica para o final.
6. **Lote 1 (G01 e G02) liberado.**
