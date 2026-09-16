---
type: unidades-aula
status: validado
title: "4.1 - Resultado depois das alterações"
modulo: "005"
ordem: 85
aula_id: aac541c3081b91df
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - cst_m05_a41_resultado_depois_das_alteracoes.pdf
  - transcricao.md
extraido_em: 2026-09-16
gerado_por: gpt-5.6-terra
retiradas: []
divisoes: []
fusoes: []
---

# 4.1 - Resultado depois das alterações

## Contexto da aula

A aula mostra o resultado de um rebalanceamento de lances em uma campanha de vídeo.
O professor compara gasto, custo por visualização e distribuição de verba entre segmentações.
Ele apresenta o pace como leitura do gasto por hora contra o orçamento diário.
A aula termina com alternativas para continuar o diagnóstico caso a distribuição permaneça desbalanceada.

## Unidades

### U:aac541c3081b91df:001 — Rebalanceamento desloca gasto entre segmentações
```yaml
tipo: exemplo
plataforma: [youtube]
tema: otimizacao
tarefas: [otimizar-publicos-e-segmentacoes]
fonte: fala
faixa: "00:00:00–00:00:32"
perecivel: true
confianca: alta
versao: 1
```
Situação: a campanha gastava R$ 20,00 em sites e plataformas e nada em outras segmentações.
O que aconteceu: após baixar um lance e aumentar outros, o gasto foi forçado para essas outras segmentações.
Lógica: o professor usa a alteração de lance para redistribuir onde a verba é consumida.

### U:aac541c3081b91df:002 — Público menor pode elevar o custo por visualização
```yaml
tipo: conceito
plataforma: [youtube]
tema: metricas-e-relatorios
tarefas: []
fonte: fala
faixa: "00:00:33–00:01:07"
perecivel: true
confianca: media
versao: 1
nota: "O professor avalia como muito provável, e não como certeza, que as visualizações dos públicos menores sejam mais qualificadas."
```
Com os mesmos R$ 20,00 gastos, o custo por visualização subiu porque os públicos mostrados eram menores e o Google encontrou oportunidades mais caras.
O lance de sites e plataformas ficou baixo a ponto de o Google não conseguir gastar verba nesse trecho.

### U:aac541c3081b91df:003 — Aumentar lance para tentar equilibrar o gasto
```yaml
tipo: decisao
plataforma: [youtube]
tema: leilao-e-lances
tarefas: [otimizar-publicos-e-segmentacoes]
fonte: fala
faixa: "00:01:07–00:01:44"
perecivel: true
confianca: alta
versao: 1
```
Se sites e plataformas não estiverem recebendo gasto, altere o lance desse trecho para R$ 0,15 e observe se o Google começa a gastar nele.
O professor mantém iguais os três lances de envolvimento e só considera reduzir os lances superiores depois que houver gasto no trecho ajustado.

### U:aac541c3081b91df:004 — Meta de distribuição no exemplo de R$ 20,00
```yaml
tipo: regua
plataforma: [youtube]
tema: orcamento
tarefas: [definir-orcamento]
fonte: fala
faixa: "00:01:07–00:01:44"
perecivel: true
confianca: media
versao: 1
nota: "O professor diz querer metade dos R$ 20,00 em um trecho, mas em seguida cita R$ 5,00 como mínimo; os valores não correspondem à metade."
```
Na campanha de R$ 20,00, o professor quer que sites e plataformas gastem pelo menos R$ 5,00, em vez de manter todo o desbalanceamento mostrado.

### U:aac541c3081b91df:005 — Pace esperado ao meio-dia
```yaml
tipo: regua
plataforma: [youtube]
tema: metricas-e-relatorios
tarefas: [otimizar-publicos-e-segmentacoes]
fonte: fala+pdf:cst_m05_a41_resultado_depois_das_alteracoes.pdf
faixa: "00:01:44–00:02:23"
perecivel: false
confianca: alta
versao: 1
nota: "O PDF, p. 2, também orienta avaliar o pacing como gasto contínuo e não deixar a campanha gastar tudo na primeira hora nem encerrar o dia sem gastar."
```
Ao meio-dia, a campanha deve ter gasto mais ou menos 40% da verba diária.
No exemplo, R$ 5,00 de um orçamento diário de R$ 20,00 equivale a 25% e é um gasto mais desacelerado do que o indicado.

### U:aac541c3081b91df:006 — Usar o percentual gasto para ler se o lance está alto ou baixo
```yaml
tipo: decisao
plataforma: [youtube]
tema: leilao-e-lances
tarefas: [otimizar-publicos-e-segmentacoes]
fonte: fala+pdf:cst_m05_a41_resultado_depois_das_alteracoes.pdf
faixa: "00:02:24–00:03:34"
perecivel: false
confianca: media
versao: 1
nota: "A fala associa 1% da verba a R$ 2,00 apesar do orçamento de R$ 20,00 usado no exemplo; a inconsistência foi preservada."
```
Se ao meio-dia a campanha já tiver gasto 70% da verba, trate os lances como um pouco altos e tire o pé do acelerador.
Se ao meio-dia tiver gasto 1% da verba, citado como R$ 2,00, trate os lances como muito baixos.
Compare o gasto por hora com o orçamento para sentir se os lances estão altos ou baixos.

### U:aac541c3081b91df:007 — Próximas soluções para gasto ainda desbalanceado
```yaml
tipo: decisao
plataforma: [youtube]
tema: estrutura-de-campanha
tarefas: [otimizar-publicos-e-segmentacoes]
fonte: fala
faixa: "00:02:57–00:04:00"
perecivel: true
confianca: media
versao: 1
nota: "O nome do público excluído aparece na transcrição como “cadastrados nos aulas ao vivo”, formulação incerta."
```
Se o aumento para R$ 0,15 não deixar o gasto balanceado, remova a exclusão do público citado ou teste outra solução.
A outra solução apresentada é separar uma campanha só de público quente e outra só de público frio.

### U:aac541c3081b91df:008 — Ciclo após alterar a campanha
```yaml
tipo: procedimento
plataforma: [youtube]
tema: otimizacao
tarefas: [otimizar-publicos-e-segmentacoes]
fonte: fala+pdf:cst_m05_a41_resultado_depois_das_alteracoes.pdf
faixa: "00:03:34–00:04:00"
perecivel: false
confianca: alta
versao: 1
nota: "O PDF, p. 2, explicita comparar o histórico, esperar após a alteração e fazer novo diagnóstico; a fala enfatiza seguir diagnosticando e testando soluções."
```
Pré-condição: uma alteração de lance, segmentação ou exclusão já foi aplicada na campanha.
1. Espere um tempo e compare os resultados com o histórico da campanha.
2. Diagnostique o gasto e escolha uma solução para o problema encontrado.
3. Teste a solução, veja o resultado e continue o ciclo de diagnóstico e solução.
4. Se a campanha ainda gastar pouco ou nada, o PDF orienta aumentar o valor de lance.