---
type: unidades-aula
status: rascunho
title: "8.1 - Otimização de lances"
modulo: "002"
ordem: 51
aula_id: 6989dafad4a10d
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - transcricao.md
extraido_em: 2026-09-15
gerado_por: gpt-5.6-terra
retiradas: []
divisoes: []
fusoes: []
---

# 8.1 - Otimização de lances

## Contexto da aula

A aula mostra, no Facebook Ads, como usar orçamento e estratégia de lance para otimizar campanhas.
Parte de campanhas já ativas, com custo por conversão, investimento e verba diária disponíveis.
O professor prioriza obter o maior volume de resultados dentro do custo aceitável.
A próxima aula trata das outras formas de otimização quando o rebalanceamento de verba não basta.

## Unidades

### U:6989dafadad4a10d:001 — Orçamento altera lance, custo e volume no menor custo
```yaml
tipo: conceito
plataforma: [meta]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala
faixa: 00:00:00–00:00:40
perecivel: false
confianca: alta
versao: 1
```
Com a estratégia de menor custo, orçamento maior eleva o lance, aumenta a aparição e o volume de resultados, mas pode encarecer o resultado.
Orçamento menor reduz lance, entrega e volume, podendo baratear o resultado.

### U:6989dafadad4a10d:002 — Reduza orçamento antes de pausar uma campanha ruim
```yaml
tipo: decisao
plataforma: [meta]
tema: otimizacao
tarefas: [otimizar-lances]
fonte: fala
faixa: 00:00:40–00:02:00
perecivel: false
confianca: alta
versao: 1
```
Se uma campanha tem resultado ruim, mantenha-a ativa e reduza um pouco o orçamento em vez de simplesmente pausá-la.
A redução pode trazer menos conversões no dia seguinte, mas com custo menor.

### U:6989dafadad4a10d:003 — Otimize pelo maior volume dentro do custo aceito
```yaml
tipo: regra
plataforma: [meta]
tema: otimizacao
tarefas: [otimizar-lances]
fonte: fala
faixa: 00:02:15–00:03:13
perecivel: false
confianca: alta
versao: 1
```
Ao otimizar, busque o maior número possível de resultados dentro do custo que você está disposto a pagar por conversão.

### U:6989dafadad4a10d:004 — Aceite custo maior para usar a verba disponível
```yaml
tipo: exemplo
plataforma: [meta]
tema: otimizacao
tarefas: [otimizar-lances]
fonte: fala
faixa: 00:01:15–00:02:14
perecivel: false
confianca: alta
versao: 1
```
Situação: a campanha gasta R$ 1.000, custa R$ 4,75 por conversão e a meta aceita é R$ 6.
O que aconteceu: o orçamento sobe para R$ 1.200, com previsão de 50 conversões em vez de 40 e custo de R$ 6.
Lógica: uma piora de custo pode ser aceitável quando entrega mais cadastros dentro do valor definido.

### U:6989dafadad4a10d:005 — Aumente verba quando o período está abaixo do potencial de gasto
```yaml
tipo: decisao
plataforma: [meta]
tema: otimizacao
tarefas: [otimizar-lances]
fonte: fala
faixa: 00:02:38–00:04:26
condicoes: "o custo por conversão permanece dentro do valor aceito e há verba para o período analisado"
perecivel: false
confianca: alta
versao: 1
```
Se os últimos 7 dias gastaram menos que os R$ 30 mil disponíveis e o custo está abaixo da meta, aumente os orçamentos para buscar mais conversões.
No exemplo, o professor prefere 5 mil conversões a R$ 6, com R$ 30 mil gastos, a 4.629 conversões a R$ 4,92, com R$ 22.785,68 gastos.

### U:6989dafadad4a10d:006 — Não existe percentual fixo para aumentar orçamento
```yaml
tipo: regra
plataforma: [meta]
tema: otimizacao
tarefas: [otimizar-lances]
fonte: fala
faixa: 00:04:26–00:05:51
perecivel: false
confianca: alta
versao: 1
```
Aumente os orçamentos de modo proporcional ao custo por resultado e ao custo que você aceita pagar; não há regra de subir apenas 20% ou 30%.
Se aceita pagar R$ 10 por conversão, o professor considera aceitável dobrar um orçamento de R$ 500 para R$ 1.000.

### U:6989dafadad4a10d:007 — Faça aumentos menores perto do custo-meta
```yaml
tipo: decisao
plataforma: [meta]
tema: otimizacao
tarefas: [otimizar-lances]
fonte: fala
faixa: 00:05:53–00:07:08
condicoes: "a meta do exemplo é custo por lead de R$ 6"
perecivel: false
confianca: alta
versao: 1
```
Se o custo já está perto da meta, aumente menos o orçamento para não ultrapassá-la.
No exemplo, R$ 1.000 por dia sobe para cerca de R$ 1.200; um orçamento de R$ 100 sobe para R$ 120; e R$ 2.000 pode ir para R$ 2.200 ou R$ 2.300.

### U:6989dafadad4a10d:008 — Diminua orçamento quando a meta de custo é mais baixa
```yaml
tipo: exemplo
plataforma: [meta]
tema: otimizacao
tarefas: [otimizar-lances]
fonte: fala
faixa: 00:07:10–00:07:48
perecivel: false
confianca: alta
versao: 1
```
Situação: a meta passa a ser R$ 3 por lead.
O que aconteceu: os orçamentos exemplificados caem para cerca de R$ 200, R$ 500, R$ 20 e de R$ 2.000 para R$ 1.000 por dia.
Lógica: uma meta de custo menor exige reduzir os orçamentos para tentar aproximar o custo por lead dela.

### U:6989dafadad4a10d:009 — Ajuste orçamento para chegar ao custo por cadastro aceito
```yaml
tipo: decisao
plataforma: [meta]
tema: otimizacao
tarefas: [otimizar-lances]
fonte: fala
faixa: 00:07:48–00:08:32
condicoes: "a campanha usa estratégia de lance de menor custo"
perecivel: false
confianca: alta
versao: 1
```
Se a meta for R$ 5 por lead, aumente um pouco os conjuntos próximos de R$ 5, mantenha o que já tem orçamento baixo e reduza o que precisa baixar custo.
A campanha está ótima nesse aspecto quando fica dentro do custo que você aceita pagar.

### U:6989dafadad4a10d:010 — Menor custo busca resultados baratos dentro do orçamento
```yaml
tipo: conceito
plataforma: [meta]
tema: leilao-e-lances
tarefas: [escolher-estrategia-de-lance]
fonte: fala
faixa: 00:08:34–00:09:23
perecivel: false
confianca: alta
versao: 1
```
A estratégia de menor custo busca gastar todo o orçamento obtendo os resultados mais baratos possíveis.
O professor diz usar essa estratégia em 99% das vezes.

### U:6989dafadad4a10d:011 — Limite de custo não é limite de lance
```yaml
tipo: conceito
plataforma: [meta]
tema: leilao-e-lances
tarefas: [escolher-estrategia-de-lance]
fonte: fala
faixa: 00:09:25–00:10:21
perecivel: false
confianca: alta
versao: 1
```
Limite de custo define quanto se quer pagar por resultado; limite de lance define o teto do lance no leilão.
Um limite de lance de R$ 5 por conversão não significa custo médio de R$ 5 por resultado.

### U:6989dafadad4a10d:012 — Comece campanhas com a estratégia de menor custo
```yaml
tipo: procedimento
plataforma: [meta]
tema: leilao-e-lances
tarefas: [escolher-estrategia-de-lance, criar-campanha]
fonte: fala
faixa: 00:10:21–00:11:37
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: estar criando uma campanha no Gerenciador de Anúncios.
1. Na configuração de otimização do orçamento da campanha, localize a estratégia de lances.
2. Selecione “menor custo” para começar.
3. Edite para “limite de custo” apenas se quiser informar quanto aceita pagar por conversão, resultado, engajamento ou visualização de vídeo.

### U:6989dafadad4a10d:013 — Não use limite de lance
```yaml
tipo: regra
plataforma: [meta]
tema: leilao-e-lances
tarefas: [escolher-estrategia-de-lance]
fonte: fala
faixa: 00:11:01–00:12:20
perecivel: false
confianca: alta
versao: 1
```
Não use limite de lance; o professor afirma nunca ter visto alguém obter resultado com essa estratégia.
Ele relata já ter visto resultados com limite de custo, mas observa resultados expressivos principalmente com menor custo.

### U:6989dafadad4a10d:014 — Controle de custo vira o acelerador no limite de custo
```yaml
tipo: conceito
plataforma: [meta]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala
faixa: 00:12:20–00:14:33
perecivel: true
confianca: alta
versao: 1
```
Com limite de custo, informe no grupo de anúncios o custo médio desejado por conversão; alguns resultados podem custar mais e outros menos.
Nesse modo, aumentar o controle de custo faz o Facebook gastar mais e diminuí-lo faz gastar menos.
O professor vê que campanhas com limite de custo normalmente não conseguem gastar todo o orçamento.

### U:6989dafadad4a10d:015 — Use orçamento como acelerador no menor custo
```yaml
tipo: regra
plataforma: [meta]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala
faixa: 00:13:47–00:15:46
condicoes: "a campanha usa estratégia de menor custo"
perecivel: false
confianca: alta
versao: 1
```
Comece com menor custo e trate o orçamento como acelerador: ao aumentá-lo, a campanha gasta mais, pode encarecer a conversão e gera mais volume; ao reduzi-lo, gasta menos, reduz volume e pode baratear o resultado.

### U:6989dafadad4a10d:016 — Não corte orçamento repetidamente para forçar custo baixo
```yaml
tipo: regra
plataforma: [meta]
tema: otimizacao
tarefas: [otimizar-lances]
fonte: fala
faixa: 00:15:10–00:16:20
perecivel: false
confianca: alta
versao: 1
```
Não fique apenas diminuindo o orçamento para tentar pagar R$ 3 por conversão; as campanhas podem parar de gerar volume de resultado.

### U:6989dafadad4a10d:017 — Rebalanceie a verba mantendo o budget diário
```yaml
tipo: procedimento
plataforma: [meta]
tema: orcamento
tarefas: [otimizar-lances, definir-orcamento]
fonte: fala
faixa: 00:16:20–00:16:55
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: conhecer a verba total diária e o custo por conversão de cada campanha ou conjunto.
1. Reduza a verba dos itens que precisam baixar custo; no exemplo de R$ 3.600 diários, um item cai para R$ 1.800.
2. Transfira parte da verba retirada para os itens com melhor condição de receber aumento.
3. Rebalanceie procurando gastar a verba diária total.
