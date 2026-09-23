# Retomada: base de conhecimento do Hardcopy Pro

Escrito em 20/09/2026 para a coordenação continuar em outra sessão; atualizado no mesmo dia com o resultado do lote do piloto. Atualizado em 21/09/2026 com o fechamento do lote 1 (ver "Lotes fechados"). Conferir o estado real antes de agir; este arquivo é retrato, não garantia.

## Onde está

- Repositório `tc3midia/cursos`, clone em `~/cursos`, branch `task/hardcopy-pro-base-consulta`, criada de `task/formato-criativo-base-consulta` (`d0b1d05`). **Commits `fe5be93` e `684a085` enviados em 22/09/2026; branch ainda não integrada à `main`.** Fontes do curso lidas no commit `7470ca0`; desde 22/09/2026 o commit de referência é `42c88f6`, que só moveu as aulas para `transcricoes/` (um arquivo por aula, mesmo conteúdo).
- Todo comando deste curso roda com `CURSO=hardcopy-pro` na frente, a partir de `~/cursos/processamento`. Sem a variável, os scripts atendem o Formato Criativo.
- Tarefa no Jarvis 4: `projetos/tc3/frentes/cursos-base-de-conhecimento/tarefas/processar-hardcopy-pro.md`. Rota e calibrações do primeiro curso: `ferramentas/processamento-de-cursos/README.md`.

## Pronto

- `PLANO.md` (nesta pasta): inventário, o que o curso tem de diferente, código `Gxx_Ayy`, piloto, lotes, revisão, consumo esperado, ponto de parada.
- `../../conhecimento/FORMATO.md` e `taxonomia.md`: contrato v1, 10 tipos, 43 temas, 39 tarefas, 17 plataformas, tabela de grafias da transcrição, vocabulário com citações conferidas por script.
- `RUBRICA.md` e `papeis/`: os do primeiro curso, com uma seção "Próprio deste curso" em cada.
- `amostra.json`: ouro `G02_A05` e `G08_A05`; todas as 139 entradas vão a julgamento.
- Scripts em `~/cursos/processamento`: perfil por curso em `base_fcc.py`, aula só de material, campo `trilha`, regra de grafia deformada e de resíduo de silêncio, espera automática no limite de sessão em `fcc_executar.py`, `tests/test_hardcopy.py`. 28 testes passam. O `--reviews --check` do Formato Criativo passou a acusar 4 cópias brutas depois da correção da checagem de 25 palavras (ver o piloto, abaixo).
- Levantamento de conteúdo das 138 aulas por seis leitores: os relatórios ficaram no rascunho da sessão anterior e não estão no repositório. O que importava deles está no FORMATO, na taxonomia e no PLANO.

## Piloto, no momento da passagem

Pasta `piloto/s5-high/`. Seis aulas extraídas com Sonnet 5 `high` (48 mil tokens de saída; cache de 20,6 mil tokens lido a partir da segunda):

| Aula | O que testa | Unidades | Contrato na extração |
|---|---|---|---|
| `G02_A05` ouro | texto, régua 60/20, regra de garantia | 10 | "hoje" no corpo de U001 |
| `G08_A05` ouro | tela, trecho alucinado em inglês | 11 | âncora de U002 fora da faixa |
| `G16_A02` | mais longa, 9.686 palavras, tela, laço de silêncio | 16 | limpa |
| `G02_A11` | VSL fictícia com números | 15 | "hoje" em U009 e U012 |
| `G02_A12` | material avulso, sem transcrição | 10 | limpa |
| `G16_A09` | 205 palavras, sem conteúdo | 1 | limpa, aviso esperado |

O lote do piloto **terminou** depois que este arquivo foi escrito pela primeira vez. Comando usado:

```bash
cd ~/cursos/processamento && CURSO=hardcopy-pro python3 fcc_lote.py --pasta ../hardcopy-pro/processamento/base-consulta/piloto/s5-high --rotulo piloto-hc --aulas G02_A05 G08_A05 G16_A02 G02_A11 G02_A12 G16_A09 --julgar-todas
```

Resultado, em `piloto/s5-high/resumo-piloto-hc.json`:

| Aula | Veredito | Ciclos | Observação |
|---|---|---|---|
| `G02_A05` ouro | aprovada | 0 | |
| `G08_A05` ouro | aprovada | 1 | inspeção apontou U002 e U006 e faixa errada em 2 de 11; versão aprovada em `ciclo1/` |
| `G16_A02` | aprovada | 0 | a mais longa e mais degradada passou direto |
| `G02_A11` | aprovada | 0 | a da VSL fictícia; inspeção apontou U009 e o juiz aprovou |
| `G16_A09` | aprovada | 0 | uma unidade `limite` |
| `G02_A12` | **bloqueada pelo juiz** | 1 | ver abaixo |

Consumo do piloto: 28 chamadas, medido em tokens por modelo em `piloto/RESULTADO.md`. Custo nominal em dólar saiu dos relatórios por decisão de Will em 21/09/2026.

### O bloqueio de `G02_A12` e o defeito de validador que ele revelou

O juiz reprovou a primeira versão por cópia bruta do material em U006 e U009 (26 e 34 palavras seguidas) e perguntou por que `base_fcc.py` tinha dado zero erro. O redator corrigiu as duas no ciclo 1. Na conferência, o juiz bloqueou pedindo **prova de ferramenta**, sem gastar o ciclo 2: as unidades estão certas, falta mostrar que a checagem roda contra o material.

Ele tinha razão. A checagem de 25 palavras comparava texto cru, então as marcações de tempo da transcrição e o Markdown do material (`*vestígios*`, marcadores de lista) escondiam a cópia. Com segmentos de 8 palavras em média, ela praticamente nunca disparava. **Corrigido nesta sessão**: a comparação passou a ser por sequência de palavras (`word_seq`), a mesma da âncora. Prova em `tests/test_hardcopy.py`, `test_prova_pedida_pelo_juiz_no_piloto`: a versão 1 de `G02_A12` dá erro em U006 e U009, e a versão do `ciclo1/` dá zero. Falta levar essa prova ao juiz em uma conferência final de `G02_A12` e registrar o desfecho. As outras cinco aulas do piloto continuam com zero erro na checagem corrigida.

**Efeito no Formato Criativo, já publicado e enviado (`d0b1d05`):** com a checagem corrigida, `base_fcc.py --reviews --check` acusa 4 unidades com cópia de 25 palavras que passaram despercebidas: `M02_A03` U018, `M03_A01` U011, `M03_A02` U015 e `M04_A04` U013. Não foram corrigidas. É decisão de Will: corrigir pelas mesmas vias (Opus, conferência focal, juiz) ou registrar como limitação. **Will decidiu corrigir, em 21/09/2026**; trabalho em `formato-criativo-de-conteudo/processamento/base-consulta/lotes/correcao-copia/`. Enquanto isso, o `--check` do primeiro curso falha nesta branch, de propósito.

Depois da extração do piloto, o papel do extrator ganhou uma linha proibindo "hoje", "atualmente" e "neste momento". As seis extrações do piloto são anteriores a essa linha.

## Feito depois da passagem (segunda sessão, 20/09/2026)

- `G02_A12`: prova de ferramenta levada ao juiz em `piloto/s5-high/final/` (rodada 3, `julgar --prova`, argumento novo de `fcc_executar.py`). Veredito `passa`, ciclo 2 não consumido. Piloto com 6 de 6 aprovadas.
- Calibração com erro plantado: `calibracao/plantar.py`, `calibracao/gabarito.json`, laudos em `calibracao/plantado/`. 9 de 9 defeitos detectados pelo veto esperado, incluindo os três próprios do curso. Nenhuma mudança em papel ou rubrica.
- `piloto/RESULTADO.md` escrito, com consumo em tokens por modelo, papel e aula, e projeção para o curso: 6,4 a 7,1 milhões de tokens de saída de Sonnet 5, 1,85 a 2,0 milhões de Fable 5.1, 0,33 a 0,57 milhão de Opus 5, em 570 a 660 chamadas.
- Desvio de processo registrado: a ouro `G08_A05` reprovou na rodada 1 e foi ao redator sem decisão de Will, porque `fcc_lote.py` não distingue ouro. Aprovada no ciclo 1. Will confirma ou não como ouro.

## Decisões de Will em 21/09/2026

- **Estrutura da biblioteca espelha o curso.** Páginas de aula e índice seguem as mesmas pastas, nomes e ordem do Hardcopy Pro (5 trilhas, 18 grupos, material em `Materiais/`), como o criador organizou. `unidades.jsonl` e `cobertura.jsonl` continuam únicos, com trilha e grupo por linha. É mudança de contrato (FORMATO seção 6 e gerador), feita antes do lote 1.
- Decisões 1, 2, 3 e 5 mantidas: base única com enum único, todas as aulas vão ao juiz, sem nova comparação de extratores, técnicas de contorno registradas com aviso.
- Decisão 7: corrigir as 4 unidades do Formato Criativo com cópia bruta.
- **Métrica de consumo é token da assinatura.** Custo nominal em dólar sai dos relatórios e das projeções.
- Retranscrição com o vocabulário do curso: fica para o final.
- Decisão 6: **`G08_A05` (versão de `piloto/s5-high/ciclo1/`) aceita por Will como ouro**, depois de ler `piloto/ouro-G08_A05-para-aprovacao.md`.
- Decisão 4: o material "Surpresa" mora em `unidades/Materiais/01 Hard Copy/Surpresa.md`, onde o curso o guarda; o código interno `G02_A12` continua. Will não objetou.
- Inspetor continua em `xhigh`. O teste de inspetor em `high` com os defeitos plantados foi oferecido e Will preferiu seguir com `xhigh`.
- **Lote 1 liberado por Will em 21/09/2026.** Daqui em diante, lotes um por vez, sem nova consulta, salvo ouro reprovada, aula bloqueada depois do teto de ciclos ou mudança de contrato.

## Feito em 21/09/2026

- Estrutura espelhada no curso: FORMATO v2 (seção 6), `page_path` e índice por pasta em `base_fcc.py`, teste em `tests/test_hardcopy.py`. Seis aulas do piloto revalidadas por script no contrato novo, zero erros; não rejulgadas.
- Correção das 4 unidades do Formato Criativo: Opus 5, conferência focal, juiz com `--prova`; quatro `passa`; publicadas; `--reviews --check` do primeiro curso de volta a zero erros. Registro no README de lá.
- Página de leitura da ouro `G08_A05` para o aceite de Will: `piloto/ouro-G08_A05-para-aprovacao.md`.
- Relatórios reescritos em tokens.

## Lotes fechados

Detalhe, consumo e projeção de cada lote no `README.md` desta pasta, que nasceu no fechamento do lote 1.

| Lote | Grupos | Fechado em | Entradas publicadas | Reprovadas na 1ª rodada | Estado |
|---|---|---|---:|---:|---|
| 1 | G01, G02 | 21/09/2026 | 21 (18 novas + `G02_A05`, `G02_A11`, `G02_A12` do piloto) | 9 de 18, todas aprovadas no ciclo 1 | publicado, `--check` com zero erros e 1 aviso (`G01_A09`) |
| 2 | G03, G04 | 21/09/2026 | 13 | 8 de 13, todas aprovadas no ciclo 1 | publicado, `--check` com zero erros e 3 avisos (`G01_A09`, `G03_A03`, `G03_A06`) |
| 3 | G05, G06 | 21/09/2026 | 17 | 7 de 17, todas aprovadas no ciclo 1 | publicado, `--check` com zero erros e 5 avisos de aula curta |
| 4 | G07 | 22/09/2026 | 13 | 7 de 13; 6 aprovadas no ciclo 1 e `G07_A05` no ciclo 2 | publicado, `--check` com zero erros e 6 avisos de aula curta |
| 5 | G08, G09 | 22/09/2026 | 17 (16 novas + `G08_A05` ouro do piloto) | 15 de 16; 13 no ciclo 1, `G08_A02` no ciclo 2, `G08_A06` no teto e resolvida na rodada 4 por decisão de Will | publicado, `--check` com zero erros |
| 6 | G10 | 22/09/2026 | 7 | 6 de 7, todas aprovadas no ciclo 1 | publicado, `--check` com zero erros e 7 avisos de aula curta |
| 7 | G11, G12 | 22/09/2026 | 12 | 7 de 12, todas aprovadas no ciclo 1 | publicado, `--check` com zero erros e 8 avisos de aula curta |

**Depois do lote 7: 100 de 139 entradas publicadas, 818 unidades; faltam 37 por extrair (G13 a G18). Will mandou pausar em 22/09/2026 depois do fechamento do lote 7: nenhum processo rodando, lote 8 não lançado.** Retomar pelo lote 8 (G13 e G14, 12 aulas) só com ordem dele; depois G15+G16 (12 novas; `G16_A02` e `G16_A09` do piloto entram na publicação) e G17+G18 (13). Erro de contexto fora do reparo repetiu em `G10_A04`, `G12_A02` e `G12_A05`: mesmo tratamento de `G08_A10` (script + rodada própria com rótulo `<rotulo>-aNN` + `resumo-<rotulo>-final.json`). Corrigir o contexto antes da fase de reparo do lote não garante que a aula fique na rodada principal: em `G12_A02` a correção entrou no arquivo mas a aula ainda saiu como residual; conferir sempre o resumo.

**Resolvido em 22/09/2026, por decisão de Will:** `G08_A06` foi publicada depois de a coordenação gravar por script a frase do contexto ditada pelo juiz (`lotes/g08-g09/final-a06/`, `correcoes` com `ciclo: 3`, `por: script`) e de uma conferência focal final com inspetor e juiz (rodada 4, `passa`). Na mesma decisão Will aprovou as três mudanças de script abaixo, implementadas com teste (33 passando) e válidas a partir do lote 8: (1) campo `contexto` na saída do redator, aplicado pelo executor (`apply_fix` em `fcc_executar.py`); o papel `redator.md` não mudou; (2) `fcc_lote.py` não abre o ciclo 2 quando o ciclo 1 reprova só por falha sem unidade (fora cobertura) e o contexto não mudou; a aula sai como pendente para a coordenação; (3) `fcc_lote.py` retira do contexto o parêntese que cita grafia deformada, antes do reparo de contrato. Histórico do caso: `G08_A06` esgotou os dois ciclos porque a única falha restante é uma frase do `contexto`, que o redator escreveu nas observações e o executor não aplica (o contrato de saída do redator só transporta unidades). Unidades certas em `lotes/g08-g09/ciclo2/G08_A06.json`; frase substituta ditada pelo juiz na rodada 3 (`ciclo2/G08_A06.julgamento.json`, falha F1). Caminho proposto pelo juiz: coordenação grava a frase por script com registro em `correcoes`, conferência focal final (inspetor `--focal` + juiz rodada 4) restrita a F1, publica se `passa`. Não executar sem a decisão de Will. Decisão de script associada: campo de `contexto` na saída do redator (muda o esquema do papel) ou parada do ciclo em falha sem unidade no `fcc_lote.py`. Pasta de trabalho `lotes/g01-g02/`; a versão aprovada das 9 corrigidas está em `lotes/g01-g02/ciclo1/`; `G02_A12` foi publicada de `lotes/g01-g02/publicar-G02_A12/` (JSON e inspeção do `ciclo1/` do piloto, julgamento de `final/`). Registros de execução em `execucoes/lote-g01-g02/`.

Aprendido no lote 1, para os próximos:

- `fcc_publicar.py` não cria `conhecimento/dados/`; já existe agora.
- `fcc_relatorio.py` só lê `Mxx_Ayy`. O consumo por papel e modelo se soma direto dos `.execucao.json` (pasta do lote mais `ciclo1/` e `ciclo2/`), deixando de fora registro com `agregado_de_blocos: true`.
- Os testes rodam com `python3 -m unittest discover -s tests` **sem** `CURSO` no ambiente (29 passam). Com `CURSO=hardcopy-pro` forçado, os testes do Formato Criativo falham, e isso é esperado.
- Extração e condução podem ir encadeadas num `bash -c` só, em segundo plano. Lote de 18 aulas: 7 minutos de extração e 50 de condução, sem espera por limite de sessão.
- Lote 2: o extrator em `high` respondeu sem raciocínio em 7 de 13 extrações (5 de 18 no lote 1). `G03_A02` saiu com 2 unidades para 1.548 palavras; inspetor apontou omissão material, juiz vetou por cobertura e o Opus criou 3 unidades no ciclo 1. Medir isso a cada lote (`thinking_tokens` do registro do extrator contra reprovação).
- Lote 5: erro de contrato residual no `contexto` (grafia deformada) fica fora do reparo, por desenho do executor (`run_fix` só recebe erros de unidade e devolve "resta para a coordenação"). Tratamento usado em `G08_A10`: corrigir a frase por script com registro em `correcoes` (`por: script`, sem unidade), rodar `fcc_lote.py` só para a aula com rótulo próprio (`<rotulo>-a10`), e mesclar os dois resumos em `resumo-<rotulo>-final.json` para o `medicao/fechamento.py`.
- Lote 5: primeiras citações não literais do inspetor (4 em 3 inspeções); o executor lista e o juiz descarta. Primeiro HTTP 429 por limite de uso da assinatura ("out of usage credits", 30 min de espera automática), diferente do limite de sessão do lote 3.
- Lote 4 (22/09): o modelo passou a raciocinar muito mais com o mesmo pacote, sem mudança nossa (extrator 7,7×, inspetor 1,7×, juiz 1,4× em tokens de raciocínio; cache lido +68 tokens em todos os papéis). Sonnet por unidade foi de 4,3 mil para 10,7 mil. Qualidade igual. Comparar a cada lote o `thinking_tokens` médio do extrator com o do lote anterior; a projeção tem dois cenários por causa disso.
- Lote 4: `G07_A05` foi a primeira aula a usar o ciclo 2 (unidade criada no ciclo 1 saiu com passo de tela errado). Aprovada na rodada 3; publicada de `lotes/g07/ciclo2/` com `--execucoes lotes/g07 lotes/g07/ciclo1`.
- Lote 3: primeira espera por limite de sessão (HTTP 429 às 13h35, renovação às 15h10). O executor esperou 1 h 36 min sozinho e retomou sem perda. Uma janela de sessão comportou cerca de 48 aulas junto com a sessão da coordenação. O que falta pede cerca de duas janelas.
- Medições de fechamento em `medicao/` (só leitura, não chamam modelo): `python3 medicao/consumo.py lotes/<lote> lotes/<lote>/ciclo1` soma tokens por papel e modelo; `python3 medicao/fechamento.py lotes/<lote> <rotulo> G08_A05 G16_A02 G16_A09` dá as linhas da tabela, as falhas da primeira rodada, a primeira passagem por faixa e o que falta (as aulas do piloto ainda não publicadas vão no fim, para não contarem como pendentes).
- Causa mais comum de reprovação: faixa que não cobre o que o corpo afirma (5 de 9 aulas). A correção é mecânica (estender `inicio` ou `fim`). Candidata a regra de script ou reparo antes do juiz, se Will quiser mexer nisso; hoje segue pelo ciclo normal.

## Falta, na ordem

1. Lotes por grupo, um por vez, na ordem do curso; grupos pequenos vizinhos da mesma trilha andam juntos. Plano (lotes 1 a 7 já fechados, até G12): G13+G14 (12), G15+G16 (12 novas; `G16_A02` e `G16_A09` entram na publicação), G17+G18 (13).
2. Fechamento da base com o alcance real da revisão explicitado no `README.md` desta pasta. Commit e push feitos em 22/09/2026 a pedido de Will; os próximos, só quando ele pedir.
3. Retranscrição com o vocabulário do curso: no final.

## Como rodar um lote

De `~/cursos/processamento`, sempre com `CURSO=hardcopy-pro`. No zsh uma variável com várias aulas não se separa sozinha: escrever a lista de aulas por extenso no comando, ou rodar por script `bash`. Rodar em segundo plano e esperar a notificação; não relançar enquanto `pgrep -fl fcc_` mostrar processo vivo.

```bash
L=../hardcopy-pro/processamento/base-consulta/lotes/g01-g02
CURSO=hardcopy-pro python3 fcc_executar.py extrair --aulas <lista> --modelo claude-sonnet-5 --esforco high --rotulo lote-g01-g02 --saida $L
CURSO=hardcopy-pro python3 fcc_lote.py --pasta $L --rotulo lote-g01-g02 --aulas <lista> --julgar-todas
CURSO=hardcopy-pro python3 fcc_publicar.py --pasta <pasta com a versão aprovada> --rotulo lote-g01-g02 --aulas <aprovadas> --execucoes <pastas de ciclos anteriores>
CURSO=hardcopy-pro python3 base_fcc.py --partial --reviews --write && CURSO=hardcopy-pro python3 base_fcc.py --partial --reviews --check
```

- O `fcc_lote.py` faz reparo de contrato, inspeção em blocos de 20, julgamento e até dois ciclos com conferência focal, e grava `resumo-<rotulo>.json`. Aula aprovada no ciclo 1 ou 2 é publicada a partir de `ciclo1/` ou `ciclo2/`.
- O publicador exige, na mesma pasta, o JSON da aula, a inspeção e o julgamento ligados por hash. Para as aulas do piloto: `G02_A05`, `G02_A11`, `G16_A02` e `G16_A09` saem de `piloto/s5-high/`; `G08_A05` de `piloto/s5-high/ciclo1/`; `G02_A12` tem JSON e inspeção em `ciclo1/` e o julgamento que vale em `final/`, então montar uma pasta com os três antes de publicar.
- Juiz que pedir prova de ferramenta: `fcc_executar.py julgar ... --prova <arquivo de saída de script>`.
- O FORMATO mudou para a v2 depois do piloto: a primeira chamada de cada papel no lote 1 regrava o cache de prefixo. Depois disso, não editar FORMATO, taxonomia, rubrica nem papéis.
- Medir o efeito da linha contra "hoje" no papel do extrator: contar erros de marcador temporal na primeira saída do lote 1.
- Fechamento de cada lote no `README.md` desta pasta: tabela por aula (unidades, inspeção, julgamento, ciclos, status), consumo em tokens por modelo e papel, e correção da projeção. A faixa de 500 a 999 palavras não tem ponto medido; o lote 1 dá os primeiros.

## Decisões da coordenação que Will pode vetar

1. Uma base só para as cinco trilhas, com `trilha` como campo.
2. Todas as aulas vão a julgamento desde o primeiro lote.
3. O piloto não repete a comparação de três extratores; o primeiro curso já decidiu Sonnet 5 `high`.
4. O material "Surpresa" entra como aula só de material, `G02_A12`.
5. Técnicas do curso que contornam política de plataforma ou direito de terceiros são registradas com fidelidade, `perecivel: true` e aviso em `nota`.

Opção em aberto de Will: retranscrever com o vocabulário do curso no `initial_prompt` do Whisper. A causa provável das grafias deformadas é o prompt pobre, não a captura em 2×: o primeiro curso teve 37 de 54 aulas em 2× pelo mesmo processo, sem piora.

## Regras que valem

- A coordenação não escreve nem reescreve unidades. Extrai o Sonnet 5 `high`, inspeciona o Sonnet 5 `xhigh` em execução separada, corrige o Opus 5 `high`, julga o Fable 5.1 `xhigh` sem ver a fonte.
- Modelos pela assinatura, `claude -p` isolado; sem chave de API e sem Batch API. O executor espera sozinho quando bate o limite de sessão.
- Congelar FORMATO, taxonomia, rubrica e papéis antes do lote: qualquer edição invalida o cache de prefixo de todos os papéis e desatualiza julgamentos já feitos.
- Tudo que é contável vira regra de script antes de virar veto.
- Teto de dois ciclos de correção por aula, conferência focal depois da correção, inspeção em blocos de até 20 unidades.
- Registrar em cada execução: modelo, esforço, os quatro contadores de token, via e `stop_reason`. O custo em dólar é nominal.
- Não mexer nas fontes. Não importar enum do Formato Criativo nem do Curso Subido.
