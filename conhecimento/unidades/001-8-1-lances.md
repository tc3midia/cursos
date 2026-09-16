---
type: unidades-aula
status: validado
title: "8.1 - Lances"
modulo: "001"
ordem: 10
aula_id: 1d139aac50abcd1c
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - cst_m01_a8.1_lances.pdf
  - transcricao.md
extraido_em: 2026-09-14
gerado_por: opus-5
retiradas: []
divisoes: []
fusoes: []
---

# 8.1 - Lances

## Contexto da aula

Aula conceitual sobre o que é lance e o que é estratégia de lance nas duas maiores fontes de tráfego, Meta Ads e Google Ads.
O professor parte da analogia do leilão de boi para separar dar um lance por item de definir uma faixa de preço que a ferramenta persegue sozinha.
Mostra as telas de configuração das duas plataformas só para situar o aluno, sem ensinar a criar campanha.
Fecha com a mecânica do acelerador: lance maior gasta mais, aparece mais e encarece o resultado; lance menor faz o contrário.
Assume que o aluno já entendeu o que é leilão e que ainda não sabe escolher valores.
Deixa explicitamente para os módulos de Meta e de Google as demais estratégias de lance, o valor certo de cada lance e os outros fatores que decidem o leilão.

## Unidades

### U:1d139aac50abcd1c:001 — Lance é o orçamento ou o preço que você aceita pagar por resultado
```yaml
tipo: conceito
plataforma: [geral]
tema: leilao-e-lances
tarefas: []
fonte: "fala+pdf:cst_m01_a8.1_lances.pdf"
faixa: "00:00:00–00:00:38"
perecivel: false
confianca: alta
versao: 1
```
A palavra lance cobre duas coisas diferentes: a verba que você coloca nos anúncios e o valor que você aceita pagar por um determinado resultado.
Quanto mais dinheiro entra, maior é o lance no primeiro sentido; no segundo sentido o lance é um teto de preço por ação.
Usar os lances bem significa aparecer gastando o mínimo possível para o máximo de resultado dentro do orçamento existente.

### U:1d139aac50abcd1c:002 — Estratégia de lance na configuração de campanha do Meta Ads
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: leilao-e-lances
tarefas: [escolher-estrategia-de-lance]
fonte: "fala+pdf:cst_m01_a8.1_lances.pdf"
faixa: "00:00:38–00:01:18"
perecivel: true
confianca: alta
versao: 1
```
Ao configurar a campanha no Meta Ads existe um ponto em que se escolhe o orçamento e a estratégia de lance da campanha.
As opções que aparecem nessa tela são volume mais alto, meta de custo por resultado, objetivo de retorno sobre investimento, limite de lance e outras opções.

### U:1d139aac50abcd1c:003 — Estratégia de lance na configuração de campanha do Google Ads
```yaml
tipo: alerta-ui
plataforma: [google]
tema: leilao-e-lances
tarefas: [escolher-estrategia-de-lance]
fonte: "fala+pdf:cst_m01_a8.1_lances.pdf"
faixa: "00:01:18–00:01:59"
perecivel: true
confianca: alta
versao: 1
```
No Google Ads a mesma etapa aparece como uma pergunta sobre em qual métrica a campanha deve focar.
É esse campo que define a estratégia de lance da campanha.

### U:1d139aac50abcd1c:004 — Leilão de boi: o lance é a faixa de preço, não o valor de cada item
```yaml
tipo: exemplo
plataforma: [geral]
tema: leilao-e-lances
tarefas: [escolher-estrategia-de-lance]
fonte: "fala+pdf:cst_m01_a8.1_lances.pdf"
faixa: "00:01:59–00:02:35"
perecivel: false
confianca: alta
versao: 1
```
Situação: num leilão de boi cada participante grita um valor por animal, oito mil, nove mil, dez mil, e o maior valor leva a peça.
O que aconteceu: o comprador muda a postura e anuncia que quer todo boi que custe até quatro mil reais; passou de quatro mil, ele não entra.
Lógica: nos anúncios online você não dá lance item a item, você declara a faixa de preço que aceita pagar e a ferramenta compra dentro dela.

### U:1d139aac50abcd1c:005 — Estratégia de lance é decidir como a ferramenta gasta seu dinheiro
```yaml
tipo: conceito
plataforma: [geral]
tema: leilao-e-lances
tarefas: []
fonte: "fala+pdf:cst_m01_a8.1_lances.pdf"
faixa: "00:02:35–00:03:09"
perecivel: false
confianca: alta
versao: 1
```
Quem dá o lance a cada exibição é a fonte de tráfego, de forma automática, e não o anunciante.
Não existe um momento em que você diz que paga um real para uma pessoa clicar e dois reais para outra converter.
A estratégia de lance é a instrução que organiza esse comportamento: você define como a plataforma vai gastar a sua verba nos leilões.

### U:1d139aac50abcd1c:006 — No Meta Ads, use a estratégia volume mais alto
```yaml
tipo: regra
plataforma: [meta]
tema: leilao-e-lances
tarefas: [escolher-estrategia-de-lance]
fonte: "fala+pdf:cst_m01_a8.1_lances.pdf"
faixa: "00:03:09–00:03:49"
perecivel: false
confianca: alta
versao: 1
```
Escolha volume mais alto como estratégia de lance no Meta Ads; o professor a usa em 99,9% dos casos.
Ele diz ter testado bastante as outras estratégias e nunca as viu render melhor que essa.
Essa opção obtém o máximo de resultados para o orçamento informado: você entrega cem reais por dia ou setecentos reais na semana e a plataforma busca o maior resultado possível com esse valor.

### U:1d139aac50abcd1c:007 — As demais estratégias de lance ficam para os módulos de Meta e Google
```yaml
tipo: limite
plataforma: [meta, google]
tema: leilao-e-lances
tarefas: []
fonte: "fala+pdf:cst_m01_a8.1_lances.pdf"
faixa: "00:03:49–00:04:24"
perecivel: false
confianca: alta
versao: 1
```
Esta aula não detalha cada estratégia de lance nem diz quando escolher uma ou outra.
O professor adia o assunto para os módulos dedicados ao Meta Ads e ao Google Ads, onde promete explorar também as demais estratégias.

### U:1d139aac50abcd1c:008 — Passe o mouse sobre as opções para ler a explicação da própria plataforma
```yaml
tipo: alerta-ui
plataforma: [google]
tema: leilao-e-lances
tarefas: [escolher-estrategia-de-lance]
fonte: "fala+pdf:cst_m01_a8.1_lances.pdf"
faixa: "00:03:49–00:04:55"
perecivel: true
confianca: alta
versao: 1
```
Na tela de estratégia de lance do Google Ads, cada opção traz uma descrição própria.
Posicione o mouse sobre a opção, ou sobre o ícone de interrogação ao lado do campo, e o texto explicativo aparece na seção lateral.
O professor trata isso como hábito a levar para toda a ferramenta, não só para esta tela.

### U:1d139aac50abcd1c:009 — CPA desejado é um custo médio, não um teto por conversão
```yaml
tipo: conceito
plataforma: [google]
tema: leilao-e-lances
tarefas: []
fonte: "fala+pdf:cst_m01_a8.1_lances.pdf"
faixa: "00:04:24–00:04:55"
perecivel: false
confianca: alta
versao: 1
```
Conversão é uma ação realizada no site, no aplicativo ou na loja, definida pelo anunciante.
Ao escolher foco em conversões, o campo de CPA desejado informa quanto você quer pagar por ação.
A estratégia então distribui os lances buscando o maior número de conversões sem estourar esse custo desejado, e conversões individuais podem sair acima ou abaixo do valor.

### U:1d139aac50abcd1c:010 — Defina o CPA desejado em vez de deixar o Google livre
```yaml
tipo: regra
plataforma: [google]
tema: leilao-e-lances
tarefas: [escolher-estrategia-de-lance]
fonte: "fala+pdf:cst_m01_a8.1_lances.pdf"
faixa: "00:04:56–00:05:30"
perecivel: false
confianca: alta
versao: 1
```
Preencha o custo por ação desejado ao usar a estratégia de conversões no Google Ads; o professor prefere sempre definir esse valor.
Deixar o campo em branco entrega mais liberdade à plataforma para gastar quanto quiser, e o comportamento passa a ser parecido com o do Meta Ads, onde você só dá a verba e o foco.

### U:1d139aac50abcd1c:011 — No Meta Ads o foco vem do objetivo da campanha, não do lance
```yaml
tipo: conceito
plataforma: [meta]
tema: leilao-e-lances
tarefas: []
fonte: fala
faixa: "00:05:30–00:06:06"
perecivel: false
confianca: alta
versao: 1
```
No Meta Ads você não informa o preço que aceita pagar por resultado; você informa o que quer que a plataforma persiga quando escolhe o objetivo da campanha.
Escolher venda como objetivo e cem reais por dia de verba equivale a pedir o máximo de vendas possível dentro desse valor.

### U:1d139aac50abcd1c:012 — No Meta o lance é o orçamento; no Google o lance é o valor por resultado
```yaml
tipo: conceito
plataforma: [meta, google]
tema: leilao-e-lances
tarefas: []
fonte: "fala+pdf:cst_m01_a8.1_lances.pdf"
faixa: "00:06:06–00:07:28"
perecivel: false
confianca: alta
versao: 1
```
Com volume mais alto no Meta Ads, lance e orçamento se confundem: você não declara que paga dez reais por venda, você declara que tem cem reais e quer o máximo de vendas.
No Google Ads o lance é lance no sentido literal, ou seja, quanto você está disposto a pagar por conversão, por clique ou pelo resultado escolhido.
Guardar essa diferença evita ler as duas plataformas com a mesma régua.

### U:1d139aac50abcd1c:013 — Quando sair do volume mais alto no Meta Ads
```yaml
tipo: decisao
plataforma: [meta]
tema: leilao-e-lances
tarefas: [escolher-estrategia-de-lance, rodar-testes-e-experimentos]
fonte: fala
faixa: "00:06:06–00:06:49"
perecivel: false
confianca: alta
versao: 1
```
Quando a intenção for rodar um teste fora do comum, aí sim troque a estratégia de volume mais alto por outra.
Fora dessa situação de teste deliberado, mantenha volume mais alto.

### U:1d139aac50abcd1c:014 — Opções de lance do Google: conversão, valor da conversão, clique e impressão
```yaml
tipo: conceito
plataforma: [google]
tema: leilao-e-lances
tarefas: []
fonte: "fala+pdf:cst_m01_a8.1_lances.pdf"
faixa: "00:06:49–00:08:02"
perecivel: false
confianca: media
versao: 1
nota: "Na fala o professor mistura as unidades de ROAS: cita querer ROAS de 150% ou 200% e, ao ler a descrição da plataforma, fala em R$ 5 de venda por R$ 1 gasto e num ROAS de 500. A unidade registra o mecanismo e evita fixar o número."
```
No Google Ads o lance pode ser dado por conversão, por valor da conversão, por clique ou por impressão, e em cada caso você informa quanto aceita pagar por aquela unidade.
Focar em valor da conversão é pedir um retorno sobre o investimento: você declara o ROAS que quer, isto é, quanto de venda quer para cada real gasto em anúncio.
O professor destaca as opções de valor da conversão e ROAS desejado, mas não diz aqui qual delas escolher.

### U:1d139aac50abcd1c:015 — Investir mais faz aparecer mais e encarece o resultado
```yaml
tipo: conceito
plataforma: [meta]
tema: leilao-e-lances
tarefas: [escalar-campanha]
fonte: "fala+pdf:cst_m01_a8.1_lances.pdf"
faixa: "00:08:02–00:09:56"
perecivel: false
confianca: alta
versao: 1
```
Quanto mais dinheiro entra na campanha, mais ela aparece, porque aparecer mais exige ganhar mais leilões.
Ganhar mais leilões significa pagar mais caro pela atenção das pessoas, então o custo por resultado tende a subir junto com a verba.
O contrário também vale: quem investe pouco aparece menos e costuma pagar mais barato por resultado do que quem investe muito.
É por isso que a escala é difícil para as grandes marcas, que precisam aparecer muitas vezes e por isso pagam caro para anunciar.

### U:1d139aac50abcd1c:016 — No Google, lance maior ganha mais leilões e gasta mais
```yaml
tipo: conceito
plataforma: [google]
tema: leilao-e-lances
tarefas: []
fonte: "fala+pdf:cst_m01_a8.1_lances.pdf"
faixa: "00:09:22–00:10:35"
perecivel: false
confianca: alta
versao: 1
```
No Google Ads a mesma mecânica aparece trocando a verba pelo lance: quanto mais você aceita pagar pelo resultado, mais leilões ganha, mais aparece e mais consegue gastar.
O preço vem junto: com um CPA desejado de cem você paga mais caro por conversão do que alguém que colocou cinco.

### U:1d139aac50abcd1c:017 — Lance muito baixo simplesmente não ganha leilão
```yaml
tipo: regra
plataforma: [google]
tema: leilao-e-lances
tarefas: [escolher-estrategia-de-lance]
fonte: "fala+pdf:cst_m01_a8.1_lances.pdf"
faixa: "00:09:56–00:10:35"
perecivel: false
confianca: alta
versao: 1
```
Não tente vencer o leilão pelo preço mínimo: um CPA desejado de um centavo tende a não ganhar leilão nenhum.
Quem vai ao leilão de boi querendo pagar um real não leva boi, porque sempre existe alguém disposto a pagar mais.
Seus concorrentes estão dando lances maiores que o seu, e por isso a estratégia do lance mais baixo não se sustenta.

### U:1d139aac50abcd1c:018 — O valor certo do lance fica para o módulo das fontes de tráfego
```yaml
tipo: limite
plataforma: [meta, google]
tema: leilao-e-lances
tarefas: []
fonte: "fala+pdf:cst_m01_a8.1_lances.pdf"
faixa: "00:10:36–00:11:06"
perecivel: false
confianca: alta
versao: 1
```
Esta aula não ensina como descobrir qual é o lance certo de uma campanha.
O professor adia o tema para o módulo de cada fonte de tráfego, onde mostrará as estimativas de lance que a plataforma oferece como ponto de partida.

### U:1d139aac50abcd1c:019 — O valor do lance se descobre testando
```yaml
tipo: regra
plataforma: [geral]
tema: leilao-e-lances
tarefas: [escolher-estrategia-de-lance, rodar-testes-e-experimentos]
fonte: "fala+pdf:cst_m01_a8.1_lances.pdf"
faixa: "00:10:36–00:11:06"
perecivel: false
confianca: alta
versao: 1
```
Trate a estimativa de lance da plataforma como norte e não como resposta: são os testes que mostram o valor capaz de ganhar os leilões.
O professor é categórico ao dizer que nada ensina mais sobre o valor do lance do que a experimentação.

### U:1d139aac50abcd1c:020 — O lance é o acelerador da campanha
```yaml
tipo: conceito
plataforma: [meta, google]
tema: leilao-e-lances
tarefas: []
fonte: fala
faixa: "00:11:09–00:11:52"
perecivel: false
confianca: alta
versao: 1
```
Pense no lance como o pedal do acelerador da campanha.
Pisar, ou seja, aumentar o lance, faz a campanha gastar mais, aparecer mais e pagar mais caro por aparição.
Tirar o pé, ou seja, reduzir o lance, faz aparecer menos e baratear a aparição.
No Meta Ads esse pedal é o orçamento; no Google Ads é o valor que você aceita pagar por resultado.

### U:1d139aac50abcd1c:021 — Ajuste o lance conforme o custo por resultado da campanha
```yaml
tipo: decisao
plataforma: [meta, google]
tema: otimizacao
tarefas: [otimizar-lances, escalar-campanha]
fonte: fala
faixa: "00:11:52–00:12:40"
perecivel: false
confianca: alta
versao: 1
```
Se a campanha está pagando caro demais pela conversão ou pela mensagem, tire o pé: invista menos, reduza o lance e o custo por resultado cai, ao preço de aparecer menos.
Se a campanha está com resultado bom, acelere: aumente o lance para gastar mais e colher mais resultado, aceitando que o custo suba.
O professor avisa que vai pedir para o aluno voltar a esta aula quando chegar nas aulas de otimização, porque é o lance que se mexe ali.

### U:1d139aac50abcd1c:022 — O lance não é o único fator que decide o leilão
```yaml
tipo: limite
plataforma: [geral]
tema: leilao-e-lances
tarefas: []
fonte: "fala+pdf:cst_m01_a8.1_lances.pdf"
faixa: "00:12:30–00:13:03"
perecivel: false
confianca: alta
versao: 1
```
A aula fecha dizendo que o lance não é a única coisa que faz ganhar o leilão: existem também a taxa de ação estimada e a qualidade do anúncio.
Esses dois fatores ficam para as próximas aulas e não são explicados aqui.
