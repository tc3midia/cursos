---
type: unidades-aula
status: validado
title: "12.0 - Janelas de conversão ou atribuição"
modulo: "001"
ordem: 16
aula_id: 88a3baf837def058
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - cst_m01_a12_janelas_de_conversao_ou_atribuicao.pdf
  - transcricao.md
extraido_em: 2026-09-14
gerado_por: opus-5
retiradas: []
divisoes: []
fusoes: []
---

# 12.0 - Janelas de conversão ou atribuição

## Contexto da aula

Aula técnica dentro do módulo de princípios do tráfego, sobre o mecanismo que decide qual anúncio, público ou campanha leva o crédito de uma conversão.
O professor define o conceito, mostra os fatores que contam (clique, visualização e visualização engajada), lista as janelas disponíveis no Meta e no Google e explica o que cada uma conta.
Fecha com os modelos de atribuição do Google, a recomendação de manter o padrão das plataformas e o critério para testar janelas diferentes.
Assume que o aluno já entendeu o que é conversão e o que é um teste, mas não assume nenhuma experiência com as telas de configuração.
Serve de primeiro contato: a configuração propriamente dita fica para as aulas de criação de campanha.

## Unidades

### U:88a3baf837def058:001 — Janela de conversão e janela de atribuição são o mesmo conceito
```yaml
tipo: conceito
plataforma: [meta, google]
tema: atribuicao
tarefas: []
fonte: fala
faixa: "00:00:00–00:00:59"
perecivel: false
confianca: alta
versao: 1
```
Os dois nomes descrevem a mesma coisa: o Meta usa "janela de atribuição" e o Google usa "janela de conversão".
No começo do Facebook Ads existiam os dois tipos separados, o que confundia todo mundo, e a plataforma passou a usar um nome só.

### U:88a3baf837def058:002 — O que a janela de atribuição decide
```yaml
tipo: conceito
plataforma: [meta, google]
tema: atribuicao
tarefas: []
fonte: "fala+pdf:cst_m01_a12_janelas_de_conversao_ou_atribuicao.pdf"
faixa: "00:00:59–00:03:29"
perecivel: false
confianca: alta
versao: 1
```
A janela é a forma pela qual a fonte de tráfego identifica qual anúncio, qual público e qual campanha respondem por uma conversão.
Sem ela não há como saber a quem creditar uma venda que acontece depois de mais de um contato do usuário com os anúncios.

### U:88a3baf837def058:003 — João, a garrafa d'água e os dois anúncios
```yaml
tipo: exemplo
plataforma: [meta]
tema: atribuicao
tarefas: [configurar-janela-de-atribuicao]
fonte: "fala+pdf:cst_m01_a12_janelas_de_conversao_ou_atribuicao.pdf"
faixa: "00:01:19–00:02:44"
perecivel: false
confianca: alta
versao: 1
```
Situação: João vê na timeline o anúncio de uma garrafa d'água, clica, entra no site, gosta do produto e adia a compra.
O que aconteceu: no dia seguinte outro anúncio da mesma garrafa aparece para ele em outra plataforma; dessa vez ele não clica, digita o endereço do site no buscador e compra.
Lógica: houve um clique num dia e uma visualização no outro, e é a janela configurada que decide qual dos dois anúncios recebe a conversão.

### U:88a3baf837def058:004 — Três fatores definem quem recebe a conversão
```yaml
tipo: conceito
plataforma: [meta, google]
tema: atribuicao
tarefas: []
fonte: "fala+pdf:cst_m01_a12_janelas_de_conversao_ou_atribuicao.pdf"
faixa: "00:02:46–00:04:12"
perecivel: false
confianca: alta
versao: 1
```
Os fatores que a janela considera são clique, visualização e visualização engajada.
No Meta existem apenas os dois primeiros; a visualização engajada só aparece no Google.

### U:88a3baf837def058:005 — As quatro janelas do Meta e o que cada uma conta
```yaml
tipo: regua
plataforma: [meta]
tema: atribuicao
tarefas: [configurar-janela-de-atribuicao]
fonte: "fala+pdf:cst_m01_a12_janelas_de_conversao_ou_atribuicao.pdf"
faixa: "00:03:29–00:05:33"
perecivel: false
confianca: alta
versao: 1
```
São quatro opções de janela:
1. Clique em 1 dia: só conta para o anúncio clicado nas últimas 24 horas.
2. Clique em 7 dias: só conta para o anúncio clicado nos últimos 7 dias.
3. Clique em 1 dia ou visualização em 1 dia: conta clique ou exibição dentro das últimas 24 horas.
4. Clique em 7 dias ou visualização em 1 dia: conta clique nos últimos 7 dias ou exibição nas últimas 24 horas.

### U:88a3baf837def058:006 — A analogia da memória curta
```yaml
tipo: conceito
plataforma: [geral]
tema: atribuicao
tarefas: []
fonte: "fala+pdf:cst_m01_a12_janelas_de_conversao_ou_atribuicao.pdf"
faixa: "00:04:12–00:05:33"
perecivel: false
confianca: alta
versao: 1
```
Explicação de um aluno da comunidade que o professor adota: se alguém leva um tapa na cara, a janela é o tempo em que a pessoa continua brava, e tudo que ela faz nesse período é consequência do tapa.
O tapa é o anúncio que impactou o usuário, a reação é o evento que a campanha recebe e a memória é o tempo de atribuição.
Janela maior significa anúncio com memória mais longa.

### U:88a3baf837def058:007 — Padrão do Meta: clique 7 dias ou visualização 1 dia
```yaml
tipo: regua
plataforma: [meta]
tema: atribuicao
tarefas: [configurar-janela-de-atribuicao]
fonte: "fala+pdf:cst_m01_a12_janelas_de_conversao_ou_atribuicao.pdf"
faixa: "00:05:33–00:06:54"
perecivel: false
confianca: alta
versao: 1
```
A configuração padrão do Meta é clique em 7 dias ou visualização em 1 dia, definida na campanha.
A maioria dos anunciantes vai ficar com essa opção.

### U:88a3baf837def058:008 — Conhecer as outras janelas mesmo usando o padrão
```yaml
tipo: regra
plataforma: [meta]
tema: testes-e-experimentos
tarefas: [rodar-testes-e-experimentos]
fonte: fala
faixa: "00:06:19–00:06:54"
perecivel: false
confianca: media
versao: 1
nota: "O professor diz que 'tem questão disso na certificação' sem dizer de qual certificação se trata."
```
Estude como funcionam as demais janelas mesmo que vá usar o padrão, porque o assunto cai em prova de certificação e porque trocar a janela é um dos testes possíveis.
Anote a troca de janela no caderno de testes.

### U:88a3baf837def058:009 — Janela pelo tempo de decisão do produto
```yaml
tipo: decisao
plataforma: [meta]
tema: atribuicao
tarefas: [configurar-janela-de-atribuicao]
fonte: "fala+pdf:cst_m01_a12_janelas_de_conversao_ou_atribuicao.pdf"
faixa: "00:06:55–00:07:31"
perecivel: false
confianca: alta
versao: 1
condicoes: "só quando decidir sair do padrão da plataforma"
```
Se o produto é de compra impulsiva e barato, com pouca decisão envolvida, use clique de 1 dia.
Se o produto exige pesquisa e comparação, como uma geladeira, use clique de 7 dias.
A régua é sempre o comportamento de compra do cliente: quanto mais demorada a decisão, maior a janela.

### U:88a3baf837def058:010 — Conversão sem clique entra pela visualização
```yaml
tipo: exemplo
plataforma: [meta]
tema: atribuicao
tarefas: [configurar-janela-de-atribuicao]
fonte: fala
faixa: "00:07:36–00:08:19"
perecivel: false
confianca: alta
versao: 1
```
Situação: o anúncio da garrafa aparece para a pessoa, que não clica em nada.
O que aconteceu: ela pesquisa o produto no buscador, entra no site por conta própria e compra no mesmo dia.
Lógica: com uma janela que inclui visualização de 1 dia, essa compra é contabilizada para o anúncio que foi apenas exibido, sem clique nenhum.

### U:88a3baf837def058:011 — A janela escolhida guia a otimização
```yaml
tipo: conceito
plataforma: [meta, google]
tema: atribuicao
tarefas: []
fonte: fala
faixa: "00:09:01–00:09:42"
perecivel: false
confianca: alta
versao: 1
```
A configuração de atribuição alinha a conversão que o sistema otimiza com a conversão que você quer medir.
Com uma janela de clique e visualização de 1 dia, a plataforma aprende com as conversões ocorridas nesse prazo e passa a buscar pessoas com probabilidade de converter nesse mesmo prazo.

### U:88a3baf837def058:012 — Manter o padrão da plataforma
```yaml
tipo: regra
plataforma: [meta, google]
tema: atribuicao
tarefas: [configurar-janela-de-atribuicao]
fonte: fala
faixa: "00:09:42–00:10:22"
perecivel: false
confianca: alta
versao: 1
```
Fique com a configuração padrão de atribuição tanto no Meta quanto no Google.
Pelos testes do professor, o padrão é o que funciona melhor para praticamente todo anunciante.

### U:88a3baf837def058:013 — Janelas do Google e o padrão de 30 dias
```yaml
tipo: regua
plataforma: [google]
tema: atribuicao
tarefas: [configurar-janela-de-atribuicao]
fonte: fala
faixa: "00:10:22–00:11:02"
perecivel: false
confianca: alta
versao: 1
```
O Google oferece mais opções de prazo que o Meta e permite janelas bem maiores: a de visualização chega a 90 dias, que é o máximo, e ainda aceita um valor personalizado.
O padrão do Google é 30 dias de clique e 1 dia de visualização engajada, e a de visualização engajada também pode ser aumentada até 30 dias.
Com janela longa, um anúncio veiculado agora pode receber conversão três meses depois, quando a pessoa finalmente comprar.
Quem não conhece bem o padrão de compra do seu usuário fica com o padrão do Google.

### U:88a3baf837def058:014 — Visualização engajada são 10 segundos de vídeo
```yaml
tipo: regua
plataforma: [google]
tema: atribuicao
tarefas: [configurar-janela-de-atribuicao]
fonte: fala
faixa: "00:11:02–00:11:41"
perecivel: false
confianca: alta
versao: 1
nota: "O professor chama o fator de 'engajamento' antes de se corrigir para 'visualização engajada' e confere a definição na própria interface."
```
A janela de visualização engajada do Google conta a partir do momento em que a pessoa assiste 10 segundos ou mais do anúncio de vídeo.

### U:88a3baf837def058:015 — Onde a janela é configurada em cada plataforma
```yaml
tipo: alerta-ui
plataforma: [meta, google]
tema: atribuicao
tarefas: [configurar-janela-de-atribuicao]
fonte: fala
faixa: "00:11:41–00:12:19"
perecivel: true
confianca: alta
versao: 1
```
No Meta a janela de atribuição é definida dentro da campanha.
No Google Ads a mesma configuração fica no evento de conversão, não na campanha.
Os lugares são diferentes, a lógica é a mesma.

### U:88a3baf837def058:016 — Modelo de atribuição existe só no Google
```yaml
tipo: conceito
plataforma: [google]
tema: atribuicao
tarefas: []
fonte: "fala+pdf:cst_m01_a12_janelas_de_conversao_ou_atribuicao.pdf"
faixa: "00:11:41–00:12:19"
perecivel: false
confianca: alta
versao: 1
```
Além da janela, o Google tem o modelo de atribuição, que determina quanto crédito cada interação com o anúncio recebe na conversão.
A janela diz quem pode receber; o modelo diz como a conversão é distribuída entre as interações.

### U:88a3baf837def058:017 — Os modelos de atribuição do Google
```yaml
tipo: conceito
plataforma: [google]
tema: atribuicao
tarefas: []
fonte: "fala+pdf:cst_m01_a12_janelas_de_conversao_ou_atribuicao.pdf"
faixa: "00:12:19–00:13:33"
perecivel: false
confianca: alta
versao: 1
```
Último clique: o último anúncio clicado leva a conversão inteira; é o modelo que o Meta usa.
Primeiro clique: quem leva é o primeiro anúncio clicado.
Linear: a conversão é dividida igualmente entre os anúncios clicados no caminho.
Iminência da conversão: dá mais crédito aos cliques mais próximos do momento da compra.
Baseado em posição: 40% para o primeiro clique, 40% para o último e 20% divididos entre os do meio.
Baseado em dados: usa o histórico de conversões da própria conta para calcular a contribuição real de cada interação.

### U:88a3baf837def058:018 — Comece pelo baseado em dados, senão último clique
```yaml
tipo: decisao
plataforma: [geral, google]
tema: atribuicao
tarefas: [configurar-janela-de-atribuicao]
fonte: "fala+pdf:cst_m01_a12_janelas_de_conversao_ou_atribuicao.pdf"
faixa: "00:13:33–00:14:10"
perecivel: false
confianca: alta
versao: 1
nota: "O professor estende a regra ao dizer que o último clique é sempre sua primeira opção nas fontes de tráfego que não têm o modelo baseado em dados."
```
Se a plataforma oferece o modelo baseado em dados, comece por ele: é o que o professor usa, porque sente as campanhas melhorarem com ele.
Quando a fonte de tráfego não tem baseado em dados, use último clique, que também ajuda a ler melhor os resultados.
Deixe o último clique como teste futuro e não gaste teste com os demais modelos.

### U:88a3baf837def058:019 — Critério para testar uma janela diferente
```yaml
tipo: decisao
plataforma: [meta, google]
tema: atribuicao
tarefas: [rodar-testes-e-experimentos, configurar-janela-de-atribuicao]
fonte: fala
faixa: "00:14:10–00:14:45"
perecivel: false
confianca: alta
versao: 1
```
Se for testar uma janela diferente do padrão, decida pelo comportamento de compra do usuário.
A pergunta que guia o teste é quanto tempo a pessoa costuma levar entre clicar no anúncio e decidir comprar.

### U:88a3baf837def058:020 — Conversão fora da janela não é atribuída
```yaml
tipo: regua
plataforma: [meta, google]
tema: atribuicao
tarefas: [configurar-janela-de-atribuicao, ler-metricas-e-relatorios]
fonte: fala
faixa: "00:14:45–00:15:24"
perecivel: false
confianca: alta
versao: 1
```
Com clique de 1 dia, só entra a conversão de quem clicou nas últimas 24 horas: quem clicou e comprou 48 horas depois não gera conversão para aquele anúncio.
A janela escolhida é também o tipo de conversão que a plataforma passa a valorizar e a procurar, valendo para Google, Meta, TikTok, Pinterest, LinkedIn e Twitter.

### U:88a3baf837def058:021 — Testar janela só depois de rodar no padrão
```yaml
tipo: regra
plataforma: [meta, google]
tema: atribuicao
tarefas: [rodar-testes-e-experimentos]
fonte: fala
faixa: "00:15:24–00:16:02"
perecivel: false
confianca: alta
versao: 1
```
Não mexa na janela no início: rode tráfego com o padrão por um tempo e só depois entre nos testes de atribuição.

### U:88a3baf837def058:022 — O que a aula deixa para as aulas de campanha
```yaml
tipo: limite
plataforma: [meta, google]
tema: atribuicao
tarefas: []
fonte: "fala+pdf:cst_m01_a12_janelas_de_conversao_ou_atribuicao.pdf"
faixa: "00:15:24–00:16:04"
perecivel: false
confianca: alta
versao: 1
```
A aula é um primeiro contato com o assunto e não ensina a mexer nas configurações.
Onde clicar e como definir janela e modelo em cada plataforma fica para as aulas de criação de campanha, onde o professor promete repetir a recomendação de usar o padrão e relembrar os testes possíveis.
