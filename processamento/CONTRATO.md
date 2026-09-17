# Contrato de extração: MAC 3.0 e Análises Extraordinárias

Adaptar o método do Curso Subido para duas bases de consulta independentes. As transcrições existentes são a fonte; não há nova transcrição nem verificação financeira externa. Não converter afirmações do instrutor em fatos verificados, garantias ou recomendações personalizadas.

## Entrega por curso

- `conhecimento/dados/<Mxx_Axx>.json`: uma aula por arquivo, conforme o esquema abaixo.
- A coordenação gera `conhecimento/unidades/<Mxx_Axx>.md`, índices de aulas e temas, manifesto com hashes e documentação do método.
- Não editar fontes, metadados ou legendas existentes. Não escrever fora do curso atribuído. Não fazer commit ou push.

## Esquema JSON da aula

Campos: `curso` (slug da pasta), `aula` (Mxx_Axx), `titulo` (da fonte), `contexto` (3 a 8 frases em lista), `unidades` (lista).

Cada unidade tem: `numero` (inteiro sequencial desde 1 na ordem da fonte), `titulo`, `tipo`, `tema`, `tarefas` (lista de slugs), `plataformas` (lista), `inicio` e `fim` (segundos na gravação), `condicoes` (texto ou null), `perecivel` (boolean), `confianca` (`alta`, `media`, `baixa`), `nota` (texto ou null), `corpo` (paráfrase), `evidencia` (trecho literal curto, máximo 24 palavras, que exista na transcrição após normalizar espaços), `versao` (1).

Tipos: `conceito`, `regra`, `regua`, `procedimento`, `decisao`, `exemplo`, `alerta-ui`, `limite`.
Temas: `fundamentos`, `gestao-de-risco`, `alavancagem`, `entradas-e-saidas`, `indicadores`, `suporte-e-resistencia`, `planejamento`, `gestao-emocional`, `plataformas`, `ecossistema`.
Plataformas: `geral`, `okx`, `tradingview`, `binance`, `outra`. Usar apenas plataforma explicitamente sustentada pela aula, `geral` quando independente de plataforma; marcar `outra` e explicar nome em nota quando necessário.
Tarefas: `compreender-metodo`, `dimensionar-exposicao`, `gerenciar-risco`, `avaliar-entrada`, `avaliar-saida`, `interpretar-indicadores`, `identificar-niveis`, `planejar-operacao`, `configurar-plataforma`, `acompanhar-operacao`, `gerenciar-emocoes`, `localizar-recursos`.

## Fidelidade e cobertura

Ler toda a aula. Extrair uma unidade por orientação distinta, preservando números, denominadores, condições, exceções, preferências, decisões, passos essenciais e limites expressos. Sem meta artificial de quantidade; uma síntese de dois parágrafos não substitui as orientações de uma aula longa. Repetições podem ser reunidas. Não usar recortes automáticos como substituto da interpretação.

As orientações devem ser atribuídas ao instrutor, sobretudo promessas de rentabilidade, ausência de perdas e uso de alavancagem. Não acrescentar correções, conclusões, resultados, justificativas ou recomendações externas. Dúvidas e nomes incertos ficam sinalizados em nota; baixar confiança. `confianca` mede fidelidade de interpretação, não eficácia financeira.

`inicio` e `fim` cobrem os trechos usados, na escala de tempo original 2×. Não dobrar tempos. `fim > inicio`. Tela, menus, condições de exchange, cotações, anúncios e disponibilidade de recursos são perecíveis. Exemplos datados preservam seu contexto e não viram previsão.

Procedimento: explicitar pré-condição e passos. Exemplo: situação, acontecimento e lógica apresentada, sem inventar desfecho. Limite: somente o que a fonte declara não cobrir. Evidência curta é âncora para inspeção, não prova suficiente de todas as partes da unidade; inspetor confere o trecho completo.

Não reutilizar autoria, selos, conta, taxonomia de publicidade, laudos nem unidades do Curso Subido. Autoria desta execução: Codex, modelo herdado não exposto no contrato. Status inicial: extraído; aprovação depende de revisão independente.

## Revisão planejada antes da extração

Inspeção independente de todas as 31 aulas, confrontando fonte e unidades. Amostra para julgamento separado: MAC M01_A07 (risco), M02_A06 (alavancagem), M04_A02 (tela); Análises M02_A02 (planejamento), M03_A05 (operação), M04_A01 (entrada). Julgamento usa artefatos e evidências do inspetor. Falha material requer correção localizada e reinspeção; amplia-se a revisão focal de padrão recorrente. Registrar alcance e hashes das versões inspecionadas. Não chamar amostragem de revisão integral.
