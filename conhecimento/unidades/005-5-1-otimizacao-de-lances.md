---
type: unidades-aula
status: validado
title: "5.1 - Otimização de lances"
modulo: "005"
ordem: 87
aula_id: d664f2e4d62a6ff8
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - cst_m05_a51_otimizacao_de_lances.pdf
  - transcricao.md
extraido_em: 2026-09-16
gerado_por: gpt-5.6-terra
retiradas: []
divisoes: []
fusoes: []
---

# 5.1 - Otimização de lances

## Contexto da aula

A aula demonstra ajustes de lance em uma campanha de distribuição de conteúdo no YouTube.
Parte de uma campanha com grupos que recebem gastos desiguais e usa públicos, CPV, visualizações e taxa de visualização para decidir.
Cobre ajustes nos grupos de anúncios, na programação, nos dispositivos e nos locais.
A fala reforça que ajustes são testes baseados em lógica e acompanhamento, sem promessa de melhora.
A próxima aula trata da otimização de públicos.

## Unidades

### U:d664f2e4d62a6ff8:001 — Lance maior faz o Google gastar mais na campanha
```yaml
tipo: conceito
plataforma: [youtube]
tema: leilao-e-lances
tarefas: []
fonte: fala
faixa: "00:00:17–00:00:47"
perecivel: false
confianca: alta
versao: 1
```
O lance é um fator importante para vencer o leilão. Ao aumentá-lo, o Google tende a gastar mais na campanha, com resultado mais caro.

### U:d664f2e4d62a6ff8:002 — PDF orienta aumentar verba em públicos desejados
```yaml
tipo: fato-material
plataforma: [google]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: "pdf:cst_m05_a51_otimizacao_de_lances.pdf"
perecivel: false
confianca: media
versao: 1
nota: "PDF, p. 3: orienta aumentar a verba em todos os públicos desejados, principalmente quentes. A fala demonstra ajuste de lance, não aumento de verba."
```
O PDF orienta aumentar a verba nos públicos em que se quer mais gasto, especialmente nos públicos quentes, e observar outras métricas antes de mudar valores em alguns casos.

### U:d664f2e4d62a6ff8:003 — Rebalancear lances entre públicos quentes e frios
```yaml
tipo: decisao
plataforma: [youtube]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala
faixa: "00:01:19–00:03:20"
condicoes: "a campanha gasta mais em públicos frios do que o desejado"
perecivel: false
confianca: alta
versao: 1
```
Se a campanha estiver desbalanceada e gastar mais nos públicos frios, aumente o lance dos públicos quentes para forçar mais gasto neles.
No exemplo, o professor dobra os lances de públicos quentes qualificados.

### U:d664f2e4d62a6ff8:004 — Ignorar CPV com gasto e volume muito baixos
```yaml
tipo: decisao
plataforma: [youtube]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala
faixa: "00:03:20–00:04:33"
condicoes: "os públicos quase não gastaram nem tiveram visualizações suficientes"
perecivel: false
confianca: alta
versao: 1
```
Se os públicos somarem apenas R$ 4 de R$ 209 da campanha e tiverem poucas visualizações, aumente seus lances para começar a gerar gasto, sem decidir pelo custo por visualização nesse caso.

### U:d664f2e4d62a6ff8:005 — Aumentar menos o lance de público frio sem gasto
```yaml
tipo: decisao
plataforma: [youtube]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala
faixa: "00:04:00–00:04:33"
condicoes: "público frio sem gasto relevante"
perecivel: false
confianca: alta
versao: 1
```
Se um público frio não gastou, aumente seu lance para fazê-lo gastar, mas menos do que aumentaria um público quente.
No exemplo, a distribuição desejada fica em cerca de 40% a 50% para públicos quentes e 40% a 50% para frios.

### U:d664f2e4d62a6ff8:006 — Diferenciar lances de públicos frios pelo desempenho
```yaml
tipo: decisao
plataforma: [youtube]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala
faixa: "00:04:33–00:06:29"
condicoes: "públicos frios gastam e têm CPV semelhante"
perecivel: false
confianca: alta
versao: 1
```
Se dois públicos frios tiverem o mesmo CPV, compare também visualizações e taxa de visualização; deixe o lance do pior menor e o do melhor um pouco maior.
No exemplo, as taxas eram 3,27% e 2,93%, e o público pior recebeu redução maior.

### U:d664f2e4d62a6ff8:007 — Ajustes de lance exigem lógica e acompanhamento
```yaml
tipo: regra
plataforma: [youtube]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala
faixa: "00:05:16–00:06:29"
perecivel: false
confianca: alta
versao: 1
```
Não há certeza sobre os valores exatos de aumento ou redução; siga uma lógica baseada nos dados e espere alguns dias para observar o resultado do ajuste.

### U:d664f2e4d62a6ff8:008 — Ajustar lances pela programação de anúncios
```yaml
tipo: procedimento
plataforma: [youtube]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala
faixa: "00:06:29–00:07:42"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: a tela de programação de anúncios mostra resultados por dia da semana.
1. Entre na programação dos anúncios e compare CPV e taxa de visualização entre os dias.
2. Aumente 1% o lance nos dias com CPV melhor, como segunda e domingo no exemplo.
3. Reduza 1% nos dias com CPV mais caro e menores taxas de visualização, como quarta e quinta no exemplo.

### U:d664f2e4d62a6ff8:009 — Priorizar ajuste nos grupos antes dos ajustes finos
```yaml
tipo: regra
plataforma: [youtube]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala
faixa: "00:07:05–00:07:42"
perecivel: false
confianca: alta
versao: 1
```
Trate os ajustes de programação como refinamento; a prioridade é otimizar os lances dos grupos de anúncios.

### U:d664f2e4d62a6ff8:010 — Testar aumento de lance por dispositivo
```yaml
tipo: decisao
plataforma: [youtube]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala
faixa: "00:07:42–00:09:30"
condicoes: "há uma hipótese de que outro dispositivo pode trazer boas visualizações"
perecivel: true
confianca: alta
versao: 1
```
Se suspeitar que um dispositivo pode trazer boas visualizações, aumente seu lance para colocar a hipótese à prova.
O professor cita aumentos de 1%, 2% ou 3% para tablets e usa 5% no computador para forçar gasto.

### U:d664f2e4d62a6ff8:011 — Aumentar tablet só diante de oportunidade observada
```yaml
tipo: decisao
plataforma: [youtube]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala
faixa: "00:10:01–00:11:13"
condicoes: "comparação entre smartphone e tablet"
perecivel: true
confianca: alta
versao: 1
```
Se o tablet tiver CPV de 3 centavos, metade do smartphone no exemplo, aumente o lance do tablet para o Google gastar mais nele.
Quando smartphone e tablet tiverem o mesmo CPV, não aumente o lance do tablet apenas porque o smartphone recebe mais gasto.

### U:d664f2e4d62a6ff8:012 — Reverter ajuste de dispositivo com resultado ruim
```yaml
tipo: decisao
plataforma: [youtube]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala
faixa: "00:10:01–00:10:38"
condicoes: "o dispositivo passou a gastar mais, mas tem taxa de visualização ruim, CPV caro e poucas visualizações"
perecivel: false
confianca: alta
versao: 1
```
Se o aumento de lance fizer o dispositivo gastar muito com taxa de visualização ruim, CPV caro e poucas visualizações, volte atrás e diminua o lance.

### U:d664f2e4d62a6ff8:013 — Ajustar lance por estado na tela de locais
```yaml
tipo: procedimento
plataforma: [youtube]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala
faixa: "00:11:13–00:11:54"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: a campanha tem dados de desempenho por local.
1. Clique em “locais”, depois em “Brasil” e em “Estados”.
2. Clique no estado que será alterado e escolha “Editar”.
3. Adicione as segmentações e defina o ajuste de lance para aumentar ou diminuir o valor por estado.

### U:d664f2e4d62a6ff8:014 — Limitar ajuste normal por estado a 1%–3%
```yaml
tipo: decisao
plataforma: [youtube]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala
faixa: "00:11:54–00:12:32"
condicoes: "um estado apresenta CPV claramente mais baixo, como R$ 0,02 contra R$ 0,06 nos demais"
perecivel: false
confianca: alta
versao: 1
```
Se um estado estiver muito mais barato que os demais, aumente seu lance de 1% a 3%, nunca passando disso.
Quando quiser forçar gasto em um local com pouca entrega, um ajuste maior é possível, com risco de gasto excessivo nele.

### U:d664f2e4d62a6ff8:015 — Não mexer também pode ser otimização
```yaml
tipo: decisao
plataforma: [youtube]
tema: otimizacao
tarefas: [otimizar-lances]
fonte: fala
faixa: "00:12:32–00:14:06"
condicoes: "a campanha gastou pouco, os custos estão próximos ou não há distorção relevante"
perecivel: false
confianca: alta
versao: 1
```
Se não houver custo por visualização muito barato ou caro e a campanha ainda tiver pouco gasto, não faça ajuste.
Revise semanalmente os lances, dispositivos e programação; otimizar busca melhora, mas não garante que ela aconteça.