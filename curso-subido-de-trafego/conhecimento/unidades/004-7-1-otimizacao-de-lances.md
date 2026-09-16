---
type: unidades-aula
status: validado
title: "7.1 - Otimização de lances"
modulo: "004"
ordem: 69
aula_id: 6eb256cdf8528d10
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - cst_m04_a71_otimizacao_de_lances.pdf
  - transcricao.md
extraido_em: 2026-09-16
gerado_por: gpt-5.6-terra
retiradas: []
divisoes: []
fusoes: []
---

# 7.1 - Otimização de lances

## Contexto da aula

A aula trata da otimização de lances na Rede de Pesquisa do Google.
Parte da leitura do ritmo de gasto diário da campanha, chamado de pace.
Mostra a mudança de estratégia de CPC para CPA e ajustes nos grupos de anúncios.
Também apresenta ajustes por público, local, programação e dispositivo.
Os períodos indicados pelo professor são sugestões de análise, não regras rígidas.
A próxima aula cobre a otimização de palavras-chave nos grupos de anúncios.

## Unidades

### U:6eb256cdf8528d10:001 — Lance define o ritmo de gasto da campanha
```yaml
tipo: conceito
plataforma: [google-search]
tema: leilao-e-lances
tarefas: []
fonte: fala+pdf:cst_m04_a71_otimizacao_de_lances.pdf
faixa: 00:00:00–00:01:20
perecivel: false
confianca: alta
versao: 1
```
O lance funciona como acelerador da campanha e é um dos três fatores que definem a vitória no leilão.
Lance maior ganha mais leilões, aumenta as aparições e acelera o gasto; lance menor produz o efeito inverso.

### U:6eb256cdf8528d10:002 — Avalie o pace ao meio-dia
```yaml
tipo: regua
plataforma: [google-search]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala+pdf:cst_m04_a71_otimizacao_de_lances.pdf
faixa: 00:01:20–00:03:54
perecivel: false
confianca: alta
versao: 1
```
Use o meio-dia como referência para avaliar o pace, pois é a metade do dia.
Com verba de R$100/dia, gastar cerca de R$44 ou metade da verba perto desse horário indica um pace adequado.
Se ao meio-dia já gastou mais da metade ou os R$100, o lance pode estar alto; se gastou 10%, 5% ou R$5, pode estar baixo.

### U:6eb256cdf8528d10:003 — Distribua o gasto durante todo o dia
```yaml
tipo: regra
plataforma: [google-search]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala+pdf:cst_m04_a71_otimizacao_de_lances.pdf
faixa: 00:02:39–00:03:54
perecivel: false
confianca: alta
versao: 1
```
Prefira que a campanha gaste ao longo de todo o dia, em vez de consumir a verba em uma hora ou durante a manhã.
O professor afirma que atingir pessoas durante o dia inteiro deixa a conversão mais barata.

### U:6eb256cdf8528d10:004 — Troque de CPC para CPA após dados de conversão
```yaml
tipo: decisao
plataforma: [google-search]
tema: leilao-e-lances
tarefas: [escolher-estrategia-de-lance]
fonte: fala+pdf:cst_m04_a71_otimizacao_de_lances.pdf
faixa: 00:03:54–00:05:19
condicoes: "depois de 7 dias rodando ou após 10 a 20 conversões"
perecivel: false
confianca: alta
versao: 1
```
Se a campanha já rodou por 7 dias ou fez 10 a 20 conversões, considere trocar a estratégia de CPC para CPA, para o Google focar em conversões.
Antes de ter conversões, o professor usa CPC porque o Google ainda não sabe o que é uma conversão naquela campanha.

### U:6eb256cdf8528d10:005 — Alterar a estratégia de lance para conversões
```yaml
tipo: procedimento
plataforma: [google-search]
tema: leilao-e-lances
tarefas: [escolher-estrategia-de-lance]
fonte: fala+pdf:cst_m04_a71_otimizacao_de_lances.pdf
faixa: 00:05:10–00:07:06
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: campanha com dados suficientes para alterar a estratégia de lance.
1. Na campanha, abra “configurações” no menu lateral e selecione “Lances”.
2. Clique em “mudar estratégia de lance” e, em “em qual métrica você quer focar?”, selecione “conversões”.
3. Defina o CPA desejado e clique em “salvar”.

### U:6eb256cdf8528d10:006 — Acompanhe a campanha 24 horas após trocar a estratégia
```yaml
tipo: regua
plataforma: [google-search]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala+pdf:cst_m04_a71_otimizacao_de_lances.pdf
faixa: 00:05:57–00:07:06
condicoes: "após mudar a estratégia de lance"
perecivel: false
confianca: alta
versao: 1
```
Espere 24 horas completas após alterar a estratégia de lance e confira o pace da campanha.
Se no dia seguinte, ao meio-dia, ela gastou toda a verba, diminua o lance; se gastou R$5 de R$100, aumente-o.

### U:6eb256cdf8528d10:007 — Aumente CPA desejado quando a conversão custa menos que o alvo
```yaml
tipo: decisao
plataforma: [google-search]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala+pdf:cst_m04_a71_otimizacao_de_lances.pdf
faixa: 00:07:06–00:08:29
condicoes: "custo por conversão abaixo do valor que você aceita pagar"
perecivel: false
confianca: alta
versao: 1
```
Se o custo por conversão estiver abaixo do valor que você aceita pagar, aumente um pouco o CPA desejado para acelerar o grupo de anúncios.
Não dobre o valor do lance.

### U:6eb256cdf8528d10:008 — Custo melhor cabe no valor aceito por conversão
```yaml
tipo: conceito
plataforma: [google-search]
tema: leilao-e-lances
tarefas: []
fonte: fala+pdf:cst_m04_a71_otimizacao_de_lances.pdf
faixa: 00:07:50–00:09:24
perecivel: false
confianca: alta
versao: 1
```
O custo por conversão mais barato não é necessariamente o melhor.
O professor considera melhor o custo que permanece dentro do valor que se está disposto a pagar, levando em conta também o volume de conversões.

### U:6eb256cdf8528d10:009 — Ajustar CPA desejado nos grupos de anúncios
```yaml
tipo: procedimento
plataforma: [google-search]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala+pdf:cst_m04_a71_otimizacao_de_lances.pdf
faixa: 00:07:20–00:10:46
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: estratégia de lance alterada e CPA desejado disponível nos grupos de anúncios.
1. Selecione o grupo de anúncios e localize a coluna “CPA desejado”.
2. Clique no ícone de lápis ao lado do valor.
3. Informe o novo valor e clique em “salvar”.

### U:6eb256cdf8528d10:010 — Diminua o lance gradualmente quando a conversão está acima do esperado
```yaml
tipo: decisao
plataforma: [google-search]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala+pdf:cst_m04_a71_otimizacao_de_lances.pdf
faixa: 00:10:13–00:14:48
condicoes: "custo por conversão acima do valor esperado"
perecivel: false
confianca: alta
versao: 1
```
Se o custo por conversão estiver acima do esperado, diminua o CPA desejado aos poucos.
O professor evita reduções que façam o grupo parar de gastar e usa exemplos de R$8 para R$3,50 e de R$32 para R$3,00.

### U:6eb256cdf8528d10:011 — Preserve mais o grupo que traz mais conversões
```yaml
tipo: decisao
plataforma: [google-search]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala
faixa: 00:11:26–00:13:23
condicoes: "grupo com maior volume de conversões"
perecivel: false
confianca: alta
versao: 1
```
Se um grupo trouxe mais conversões que os demais, trate-o com mais cautela ao reduzir o lance, mesmo que o custo por conversão seja semelhante.
O professor diz que não existe certo ou errado único e que cada gestor desenvolve sua lógica com experiência.

### U:6eb256cdf8528d10:012 — Regra básica para os lances dos grupos
```yaml
tipo: regra
plataforma: [google-search]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala+pdf:cst_m04_a71_otimizacao_de_lances.pdf
faixa: 00:13:23–00:14:48
perecivel: false
confianca: alta
versao: 1
```
Se está bom, aumente o lance; se está ruim, diminua; se está ok, mantenha.
Faça os ajustes aos poucos e não triplique os lances.

### U:6eb256cdf8528d10:013 — Espere a campanha rodar com CPA antes de ajustar grupos
```yaml
tipo: decisao
plataforma: [google-search]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala
faixa: 00:12:46–00:14:03
condicoes: "após trocar CPC por CPA"
perecivel: false
confianca: alta
versao: 1
```
Quando trocar a estratégia de CPC para CPA, deixe a campanha rodar alguns dias com CPA antes de começar a alterar os CPAs desejados dos grupos de anúncios.
O professor descreve a troca de estratégia como uma alteração grande.

### U:6eb256cdf8528d10:014 — Ajustar lances por público-alvo no grupo de anúncios
```yaml
tipo: procedimento
plataforma: [google-search]
tema: publicos
tarefas: [otimizar-lances]
fonte: fala+pdf:cst_m04_a71_otimizacao_de_lances.pdf
faixa: 00:14:25–00:19:04
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: campanha com ao menos 30 dias para reunir dados mais relevantes dos públicos.
1. Abra “grupos de anúncios” no menu lateral e entre no grupo que será alterado.
2. Abra “públicos-alvo” e clique em “mostrar tabela”.
3. Analise cada público e faça o ajuste de lance na coluna “ajuste de lance”.
4. Repita em cada grupo de anúncios.

### U:6eb256cdf8528d10:015 — Aumente o lance para público com conversão interessante
```yaml
tipo: decisao
plataforma: [google-search]
tema: publicos
tarefas: [otimizar-lances]
fonte: fala+pdf:cst_m04_a71_otimizacao_de_lances.pdf
faixa: 00:15:34–00:17:39
condicoes: "público convertendo mais por preço interessante"
perecivel: false
confianca: alta
versao: 1
```
Se um público estiver convertendo mais por preço interessante, aumente seu ajuste de lance, como 2%, para o Google pagar mais para aparecer a pessoas com esse perfil que pesquisam assuntos relacionados ao produto.

### U:6eb256cdf8528d10:016 — Espere 30 dias para otimizar públicos-alvo
```yaml
tipo: regua
plataforma: [google-search]
tema: publicos
tarefas: [otimizar-lances]
fonte: fala+pdf:cst_m04_a71_otimizacao_de_lances.pdf
faixa: 00:16:49–00:19:04
condicoes: "campanha em veiculação"
perecivel: false
confianca: alta
versao: 1
```
Comece a considerar os dados de públicos-alvo mais relevantes depois de 30 dias de campanha.
O professor normalmente otimiza os públicos-alvo a cada 30 dias, pois precisa de dados suficientes.

### U:6eb256cdf8528d10:017 — Ajuste também idade, gênero e renda
```yaml
tipo: regra
plataforma: [google-search]
tema: publicos
tarefas: [otimizar-lances]
fonte: fala+pdf:cst_m04_a71_otimizacao_de_lances.pdf
faixa: 00:19:04–00:20:33
perecivel: false
confianca: alta
versao: 1
```
Faça ajuste de lance em públicos-alvo, idade, gênero e renda quando quiser pagar mais para aparecer a um perfil específico que converte melhor.
O professor descreve esse ajuste fino como trabalhoso.

### U:6eb256cdf8528d10:018 — Frequência de ajuste dos grupos conforme duração
```yaml
tipo: decisao
plataforma: [google-search]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala
faixa: 00:17:39–00:19:04
perecivel: false
confianca: alta
versao: 1
```
Se a campanha vai rodar durante 365 dias por ano ou permanecer no ar, otimize os lances dos grupos mais ou menos a cada 7 dias.
Se a campanha vai rodar somente 30 dias, otimize a cada 1 ou 2 dias para conseguir cerca de 15 otimizações.

### U:6eb256cdf8528d10:019 — Abrir a análise de locais por estado
```yaml
tipo: procedimento
plataforma: [google-search]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala+pdf:cst_m04_a71_otimizacao_de_lances.pdf
faixa: 00:20:33–00:21:56
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: campanha com dados para avaliar resultados por local.
1. Abra “locais” no menu lateral e clique em “Brasil”.
2. Escolha visualizar os resultados por “Estados”.
3. Ordene as colunas por conversões ou custo por conversão.
4. Selecione o estado, clique em “editar” e em “adicionar segmentação e definir ajuste de lance”.

### U:6eb256cdf8528d10:020 — Limite ajustes de locais entre 1% e 3%
```yaml
tipo: regua
plataforma: [google-search]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala+pdf:cst_m04_a71_otimizacao_de_lances.pdf
faixa: 00:21:12–00:22:35
perecivel: false
confianca: alta
versao: 1
```
Faça aumentos ou reduções de lance por local entre 1% e 3%.
Esses ajustes se somam aos de público, idade e outros critérios, por isso o professor não recomenda ajustes grandes.

### U:6eb256cdf8528d10:021 — Ajustar lance de um estado
```yaml
tipo: procedimento
plataforma: [google-search]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala+pdf:cst_m04_a71_otimizacao_de_lances.pdf
faixa: 00:21:12–00:22:35
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: estado selecionado na visão de locais.
1. Clique em “editar” e em “adicionar segmentações e definir ajustes de lances”.
2. Escolha aumentar ou diminuir no campo “alterar ajuste de lance”.
3. Informe a porcentagem desejada e clique em “aplicar”.

### U:6eb256cdf8528d10:022 — Frequência para otimizar lances de locais
```yaml
tipo: decisao
plataforma: [google-search]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala+pdf:cst_m04_a71_otimizacao_de_lances.pdf
faixa: 00:22:35–00:24:26
perecivel: false
confianca: alta
versao: 1
```
Se a campanha ficar no ar por 1 ou 2 meses, otimize os locais a cada 7 dias.
Se a campanha ficar no ar para sempre ou por mais tempo, faça essa otimização a cada 21 ou 30 dias.

### U:6eb256cdf8528d10:023 — Ignore os sete primeiros dias na programação
```yaml
tipo: decisao
plataforma: [google-search]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala+pdf:cst_m04_a71_otimizacao_de_lances.pdf
faixa: 00:24:26–00:26:21
condicoes: "análise da programação de anúncios"
perecivel: false
confianca: alta
versao: 1
```
Quando analisar a programação de anúncios, desconsidere os primeiros 7 dias da campanha, pois ela ainda está adquirindo inteligência.
O professor demonstra a análise por dia da semana e não altera a própria campanha recente.

### U:6eb256cdf8528d10:024 — Frequência para otimizar a programação de anúncios
```yaml
tipo: decisao
plataforma: [google-search]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala+pdf:cst_m04_a71_otimizacao_de_lances.pdf
faixa: 00:24:26–00:26:21
perecivel: false
confianca: alta
versao: 1
```
Se a campanha ficar no ar por 1 ou 2 meses, otimize a programação de anúncios a cada 7 dias.
Se a campanha ficar no ar para sempre, faça essa otimização a cada 14 dias.

### U:6eb256cdf8528d10:025 — Consultar resultado por programação de anúncios
```yaml
tipo: alerta-ui
plataforma: [google-search]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala+pdf:cst_m04_a71_otimizacao_de_lances.pdf
faixa: 00:24:26–00:25:48
perecivel: true
confianca: alta
versao: 1
```
No menu lateral, “programação de anúncios” mostra o resultado das campanhas em cada dia da semana.
Aplique o mesmo critério: aumente o lance do que está bom e diminua o do que está ruim.

### U:6eb256cdf8528d10:026 — Ajustar lance por dispositivo
```yaml
tipo: procedimento
plataforma: [google-search]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala+pdf:cst_m04_a71_otimizacao_de_lances.pdf
faixa: 00:26:10–00:27:39
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: campanha com resultados disponíveis por dispositivo.
1. Abra “dispositivos” no menu lateral para ver smartphones, computadores e tablets.
2. Compare os resultados e altere a coluna “ajuste de lance”.
3. Trate com mais cautela o dispositivo que traz mais conversões.

### U:6eb256cdf8528d10:027 — Exemplo de ajuste por dispositivo
```yaml
tipo: exemplo
plataforma: [google-search]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala
faixa: 00:26:21–00:27:01
perecivel: false
confianca: alta
versao: 1
```
Situação: computador converte a R$5 e smartphone a R$9,90, mas o smartphone gerou mais conversões.
O que aconteceu: o professor reduziria 1% do lance do smartphone e aumentaria 2% do computador.
Lógica: o dispositivo com mais conversões é o “queridinho”, então mesmo indo pior recebe redução menor.

### U:6eb256cdf8528d10:028 — Frequência para otimizar dispositivos
```yaml
tipo: decisao
plataforma: [google-search]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala+pdf:cst_m04_a71_otimizacao_de_lances.pdf
faixa: 00:27:01–00:27:39
perecivel: false
confianca: alta
versao: 1
```
Se a campanha ficar no ar por 1 ou 2 meses, otimize dispositivos a cada 7 dias.
Se a campanha ficar no ar para sempre, faça essa otimização a cada 14 dias.

### U:6eb256cdf8528d10:029 — Organize as otimizações em calendário
```yaml
tipo: regra
plataforma: [google-search]
tema: otimizacao
tarefas: [otimizar-lances]
fonte: fala+pdf:cst_m04_a71_otimizacao_de_lances.pdf
faixa: 00:27:39–00:28:11
perecivel: false
confianca: alta
versao: 1
```
Crie eventos no calendário para os dias de cada tipo de otimização.
No início elas levam mais tempo; depois de pegar o jeito, o professor diz que consegue fazer as otimizações do Google em 20 minutos.

### U:6eb256cdf8528d10:030 — Períodos são sugestões, não regra rígida
```yaml
tipo: regra
plataforma: [google-search]
tema: otimizacao
tarefas: [otimizar-lances]
fonte: fala+pdf:cst_m04_a71_otimizacao_de_lances.pdf
faixa: 00:28:11–00:30:34
perecivel: false
confianca: alta
versao: 1
```
Use os períodos indicados como sugestões de análise e teste o que funciona melhor para o seu tráfego.
O professor não os apresenta como regra rígida.

### U:6eb256cdf8528d10:031 — Priorize otimizar lances dos grupos de anúncios
```yaml
tipo: decisao
plataforma: [google-search]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala
faixa: 00:28:48–00:30:34
condicoes: "quando for preciso escolher apenas uma otimização de lances"
perecivel: false
confianca: alta
versao: 1
```
Se tiver de escolher apenas uma otimização, não deixe de otimizar os lances dos grupos de anúncios.
Para campanha no ar por mais de 3 ou 4 meses, faça-a a cada 7 dias; para campanha de 1 ou 2 meses, a cada 1 ou 3 dias.

### U:6eb256cdf8528d10:032 — Próxima aula: novas palavras-chave
```yaml
tipo: limite
plataforma: [google-search]
tema: palavras-chave
tarefas: []
fonte: fala+pdf:cst_m04_a71_otimizacao_de_lances.pdf
faixa: 00:28:11–00:30:34
perecivel: false
confianca: alta
versao: 1
```
A aula não cobre a otimização de novas palavras-chave dentro dos grupos de anúncios; o professor a deixa para a próxima aula.