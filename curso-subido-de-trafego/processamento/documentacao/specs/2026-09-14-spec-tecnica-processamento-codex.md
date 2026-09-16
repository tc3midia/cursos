# Curso Subido no Codex: proposta para decidir

Data: 2026-09-14. Revisão 2, após o feedback de Will.

**Aprovada para implementação e piloto em 14/09/2026.** Will respondeu “vamos seguir a sua recomendação”. A distribuição abaixo será testada; a escolha definitiva e a retomada do módulo 002 dependem dos resultados.

**Decisão após o piloto:** Will confirmou o uso de três modelos com funções diferentes e pediu o início do módulo 002. Terra extrai e inspeciona em contextos separados, Sol corrige e Astra julga a amostra. A rota vigente está no [plano de sessões](../planos/2026-09-14-plano-de-sessoes.md); as seções abaixo preservam a proposta que foi testada. O estado da execução está em tarefas.md (registro no Jarvis 4: `projetos/tc3/frentes/curso-subido-base-atomica/tarefas.md`).

## 1. A recomendação em uma frase

**Atualização de qualidade, 15/09/2026:** Will retirou a reextração automática de módulo por falhas na amostra. A [regra vigente](../2026-09-15-regra-qualidade-e-retrabalho.md) adota correção localizada, distinção entre falhas materiais e ajustes menores e resolução de divergências antes de repetir trabalho. A decisão de modelos permanece; referências históricas a critérios anteriores nas specs não prevalecem sobre essa atualização.

**Sol produz e corrige, Terra confere a fonte e Astra julga a amostra. Os scripts cuidam das verificações de formato.**

Vamos manter o processo do Claude: alguém transforma a aula em orientações, outro confere se elas correspondem ao que o professor ensinou e outro decide se o resultado passa. A adaptação escolhe quem faz cada parte no Codex.

## 2. Qual modelo faz cada trabalho

| Trabalho | Modelo proposto | Por que começar assim | Quando subir de modelo |
|---|---|---|---|
| **Extrair:** transformar a aula em orientações separadas | **Sol**, esforço médio | Precisa interpretar condições, números e procedimentos. Uma omissão pode comprometer todo o restante. | Astra somente se houver dificuldade de interpretação que persista após correção; aula longa, sozinha, não basta. |
| **Inspecionar:** comparar orientações e fonte, apontando erros e omissões | **Terra**, esforço médio | É uma comparação delimitada, adequada para testar um modelo de menor custo. Ele precisa apresentar provas do que encontrou. | Sol se o teste mostrar que Terra deixa passar erros ou se houver ambiguidade que não consiga resolver. |
| **Julgar:** decidir se a aula revisada passa | **Astra**, esforço alto | Concentrar o modelo mais forte na decisão de qualidade. Recebe orientações, provas da inspeção e regras de avaliação. | Já é o nível mais forte desta proposta. |
| **Corrigir:** ajustar o conteúdo apontado como errado | **Sol**, esforço médio | Recebe o problema e o trecho necessário para resolvê-lo. | Astra se a correção continuar errando por interpretação. |
| **Coordenar:** chamar cada papel, salvar resultados e acompanhar etapas | **Sol**, esforço médio, em uma futura sessão de execução | O fluxo já está definido. A coordenação precisa seguir os passos e conferir resultados. | Dúvidas de conteúdo seguem para o papel responsável. Esta proposta não troca o modelo da conversa atual. |
| **Conferir formato:** campos, IDs, arquivos e referências | **Scripts existentes** | Essas regras já podem ser verificadas pelo código. | Erros de conteúdo seguem para o corretor; não criar um agente só para repetir a checagem do script. |

“Esforço” é quanto raciocínio pedimos ao modelo. Começar no médio evita pedir esforço alto para todas as tarefas. Só aumentamos quando houver um erro concreto que justifique.

**O Astra participa das revisões previstas na amostra do plano. Não acrescentamos uma revisão Astra a todas as 107 aulas por causa desta adaptação.** No teste inicial, as duas aulas escolhidas serão revisadas por completo.

Os nomes técnicos são `gpt-5.6-sol`, `gpt-5.6-terra` e `gpt-6-astra`. Estão disponíveis na lista de opções desta sessão; seu desempenho neste processo ainda precisa ser medido.

## 3. Por que essa divisão, e onde entra o Luna

A OpenAI apresenta Terra como equilíbrio entre capacidade e custo, Luna para trabalho de grande volume com prioridade em custo, Sol para trabalho profissional complexo e Astra para os trabalhos mais difíceis. **A divisão por papel acima é uma recomendação nossa para este processo**, não uma especialização comprovada nesses materiais. [Catálogo oficial](https://developers.openai.com/api/docs/models).

Luna pode ser candidato futuro para tarefas muito delimitadas. Não estou acrescentando um papel para ele agora: várias tarefas simples já são resolvidas pelos scripts. Para colocá-lo na extração ou inspeção, precisamos comparar sua qualidade e seu retrabalho com os demais.

## 4. Como economizar de verdade

Há três formas diferentes de economizar:

1. **Pagar menos pelo mesmo volume:** usar Sol ou Terra onde entregarem qualidade suficiente.
2. **Enviar e gerar menos texto:** cada papel recebe apenas o material necessário e devolve o resultado, sem longas explicações repetidas.
3. **Evitar refazer trabalho:** salvar cada aula concluída e corrigir apenas os trechos errados.

Exemplo: se duas orientações de uma aula estiverem erradas, o corretor recebe essas duas, o problema e os trechos que as sustentam. Ele não precisa extrair a aula inteira novamente. A inspeção posterior precisa corresponder à versão corrigida.

O juiz não lê a transcrição completa. Ele recebe as provas curtas produzidas pelo inspetor. Isso preserva a separação dos papéis e reduz a repetição da fonte.

Executar mais agentes ao mesmo tempo pode reduzir a espera, mas não reduz necessariamente tokens. Primeiro medimos uma aula por vez; depois, podemos trabalhar com duas simultâneas.

### Uma referência de preço, sem confundir com a assinatura

Valores de API por 1 milhão de tokens, consultados em 14/09/2026, sem cache ou condições especiais:

| Modelo | Texto recebido | Texto gerado |
|---|---:|---:|
| Luna | US$ 0,20 | US$ 1,20 |
| Terra | US$ 2 | US$ 12 |
| Sol | US$ 4 | US$ 20 |
| Astra | US$ 10 | US$ 50 |

Fonte: [catálogo oficial da OpenAI](https://developers.openai.com/api/docs/models). Esses preços ajudam a comparar os modelos; não são uma previsão de cobrança nem de consumo dos limites da sua assinatura Codex.

**O que vamos medir é o total gasto até a aula ficar aprovada, incluindo as correções.** Um modelo de menor preço pode perder a vantagem se precisar de várias tentativas. A própria OpenAI relata casos em que Astra usa menos tokens e reduz o custo total da tarefa; ainda não sabemos se isso acontece nas nossas aulas. [Orientação oficial sobre Astra](https://developers.openai.com/api/docs/guides/latest-model).

## 5. Um teste pequeno para escolher com evidência

Usar duas aulas já conhecidas: uma com resultado de referência aprovado e uma longa. Trabalhar em cópias, preservando a base existente.

1. Sol faz a extração, Terra confere a fonte e Astra julga o resultado das duas aulas.
2. Conferimos também os casos com erros conhecidos já existentes no projeto. Isso verifica se a revisão detecta o que deveria detectar, sem mostrar as respostas esperadas aos avaliadores.
3. Para testar economia adicional, Terra também extrai as mesmas duas aulas. As saídas passam pelo mesmo critério de avaliação, com contextos separados. Assim comparamos Sol e Terra no trabalho de maior volume.
4. Se Terra falhar na inspeção dos erros conhecidos, testar Sol nesse papel antes de continuar. Uma omissão do inspetor pode ficar invisível ao juiz, que não recebe a fonte completa.
5. Entregar uma tabela curta para Will: erros na primeira tentativa, correções necessárias, consumo total disponível e tempo por aula. Separar o custo desse experimento do custo esperado da operação.

**Critério de escolha:** entre as opções que preservarem números, condições, passos e fidelidade à fonte, escolher a que gastar menos no processo completo. O teste inicial orienta a escolha; a amostragem do plano continua verificando as aulas seguintes.

Se Terra empatar em qualidade e consumir menos, poderá assumir a extração. Se gerar retrabalho, Sol permanece. Se um papel falhar, ajustamos aquele papel antes de ampliar o processamento. Não subir todos para Astra por causa de um erro localizado.

## 6. O que precisa mudar por trás

São três ajustes de funcionamento:

- **Registrar o autor certo:** hoje os arquivos só aceitam nomes de modelos Claude. Precisam aceitar os modelos Codex escolhidos, sem alterar a autoria dos arquivos antigos.
- **Separar as conversas:** quem julga não pode receber o histórico de quem leu a transcrição. Cada papel começa com o material permitido para sua tarefa.
- **Retomar sem perder trabalho:** uma aula só conta como concluída depois das verificações. Salvar o que já passou evita repetir tudo se a sessão cair.

Os comandos, regras de conteúdo e etapas continuam na [spec original](2026-09-14-spec-tecnica-processamento.md) e no [plano de sessões](../planos/2026-09-14-plano-de-sessoes.md). A troca dos nomes aceitos exige atualizar os registros de dependência dos documentos afetados; isso não equivale a uma nova revisão de conteúdo. Os checkpoints e critérios de qualidade permanecem.

## 7. A decisão que esta proposta permite tomar

**Minha recomendação é começar o teste com Sol na produção, Terra na inspeção e Astra no julgamento, comparando também Terra como extrator nas mesmas duas aulas.**

Isso define o que testar, onde concentrar o modelo mais caro e como decidir uma redução adicional de consumo. Depois do teste, Will recebe os resultados e escolhe a distribuição para continuar o módulo 002.

O piloto foi executado. Os resultados, limites da medição e a recomendação após o teste estão no [relatório do piloto](../2026-09-14-resultado-piloto-codex.md). Ele é a referência para decidir a continuação; a matriz acima registra a hipótese testada.

---

Histórico: a [primeira versão técnica](2026-09-14-spec-tecnica-processamento-codex-v1-historico.md) foi preservada como proposta superada. A recomendação de Astra em todos os papéis foi retirada. A tarefa da frente (registro no Jarvis 4: `projetos/tc3/frentes/curso-subido-base-atomica/tarefas.md`) registra a aprovação, a implementação e o piloto em cópias temporárias.
