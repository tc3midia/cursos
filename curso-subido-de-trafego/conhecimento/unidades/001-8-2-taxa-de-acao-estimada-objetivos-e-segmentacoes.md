---
type: unidades-aula
status: validado
title: "8.2 - Taxa de ação estimada - objetivos e segmentações de campanhas"
modulo: "001"
ordem: 11
aula_id: b860f68ae836a8bf
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - Mapa Mental.txt
  - cst_m01_a8.2_taxa_de_acao_estimada_objetivos_e_segmentacoes.pdf
  - transcricao.md
extraido_em: 2026-09-14
gerado_por: opus-5
retiradas: []
divisoes: []
fusoes: []
---

# 8.2 - Taxa de ação estimada - objetivos e segmentações de campanhas

## Contexto da aula

Segunda parte da explicação do leilão: depois do lance, o professor apresenta a taxa de ação estimada como o fator que permite ganhar leilões sem depender só de dinheiro.
Ele define a taxa como probabilidade de quem vê o anúncio realizar o objetivo publicitário e separa isso em dois fatores controláveis: a escolha do objetivo de campanha e a escolha de quem vê o anúncio.
A parte de objetivos é tratada como trivial e adiada para os módulos de cada fonte de tráfego; a aula concentra-se em segmentação.
O professor apresenta a divisão de públicos em super quentes, quentes e frios, e depois percorre listas de públicos recomendados por modelo de negócio: negócio local, e-commerce, perpétuo e lançamento.
É uma aula de primeiro contato com nomenclatura, declaradamente conceitual: nada é criado dentro do gerenciador.
Assume que o aluno já viu a aula de leilão e a de lance, e deixa a criação prática dos públicos e o terceiro fator do leilão (o anúncio) para depois.

## Unidades

### U:b860f68ae836a8bf:001 — Lance tem teto: mais investimento encarece o resultado
```yaml
tipo: conceito
plataforma: [geral]
tema: leilao-e-lances
tarefas: []
fonte: "fala+pdf:cst_m01_a8.2_taxa_de_acao_estimada_objetivos_e_segmentacoes.pdf"
faixa: "00:00:00–00:01:10"
perecivel: false
confianca: alta
versao: 1
```
O lance é o acelerador da campanha: gastar mais significa ganhar mais leilões e aparecer mais, e a tendência é que o custo por resultado suba junto.
Não existe pagar o mesmo valor por venda a vida inteira enquanto o investimento cresce; pagar R$ 10 por venda pode se sustentar com R$ 100 por dia e não se sustenta com R$ 100 mil por dia.
Existem maneiras de gastar muito mantendo o custo relativamente baixo, e é para isso que servem os outros fatores do leilão.

### U:b860f68ae836a8bf:002 — Taxa de ação estimada é probabilidade, não fórmula
```yaml
tipo: conceito
plataforma: [geral]
tema: leilao-e-lances
tarefas: []
fonte: "fala+pdf:cst_m01_a8.2_taxa_de_acao_estimada_objetivos_e_segmentacoes.pdf"
faixa: "00:01:10–00:01:45"
perecivel: false
confianca: alta
versao: 1
```
A taxa de ação estimada é a probabilidade de a pessoa que vai ver o anúncio realizar o objetivo publicitário da campanha.
As documentações oficiais das fontes de tráfego não dizem qual é o cálculo dessa taxa, então o que importa é entender o conceito, não reproduzir uma fórmula.

### U:b860f68ae836a8bf:003 — Os dois fatores que você controla na taxa de ação estimada
```yaml
tipo: regra
plataforma: [geral]
tema: leilao-e-lances
tarefas: [escolher-objetivo-de-campanha, definir-segmentacao-demografica-e-interesses]
fonte: "fala+pdf:cst_m01_a8.2_taxa_de_acao_estimada_objetivos_e_segmentacoes.pdf"
faixa: "00:01:45–00:02:22"
perecivel: false
confianca: alta
versao: 1
```
Para elevar a taxa de ação estimada, trabalhe dois fatores e só eles: o objetivo publicitário da campanha e quem vai ver o anúncio.
Acertar os dois entrega tudo o que é preciso para ter uma taxa de ação estimada alta, sem depender de aumentar o lance.

### U:b860f68ae836a8bf:004 — Objetivos ficam para os módulos de cada fonte
```yaml
tipo: limite
plataforma: [geral]
tema: objetivos
tarefas: []
fonte: "fala+pdf:cst_m01_a8.2_taxa_de_acao_estimada_objetivos_e_segmentacoes.pdf"
faixa: "00:02:00–00:02:22"
perecivel: false
confianca: alta
versao: 1
```
Esta aula não ensina a configurar objetivos de campanha: a explicação densa de cada objetivo é adiada para os módulos específicos de cada fonte de tráfego.
Aqui os objetivos aparecem apenas como um dos dois fatores da taxa de ação estimada.

### U:b860f68ae836a8bf:005 — Quantidade de objetivos publicitários por plataforma
```yaml
tipo: regua
plataforma: [meta, google]
tema: objetivos
tarefas: [escolher-objetivo-de-campanha]
fonte: fala
faixa: "00:02:22–00:02:56"
perecivel: true
confianca: media
versao: 2
nota: "O professor diz 8 objetivos no Google Ads e se corrige para 7; a justificativa da exceção sai truncada na transcrição."
```
O Meta Ads tem 6 objetivos publicitários e o Google Ads tem 8, número que o professor corrige para 7 ao descontar um tipo de campanha que foge da contagem.

### U:b860f68ae836a8bf:006 — Escolha do objetivo segue o resultado desejado
```yaml
tipo: decisao
plataforma: [meta, google]
tema: objetivos
tarefas: [escolher-objetivo-de-campanha]
fonte: "fala+pdf:cst_m01_a8.2_taxa_de_acao_estimada_objetivos_e_segmentacoes.pdf"
faixa: "00:02:23–00:02:56"
perecivel: false
confianca: alta
versao: 1
```
Se você quer vendas, selecione vendas; se quer cadastros, selecione leads ou cadastro; se quer engajamento, selecione engajamento; se quer que as pessoas vejam o produto e lembrem da marca, selecione consideração de produto e de marca.
A seleção de objetivo é direta e não exige ponderação: o nome do objetivo corresponde ao resultado que você quer.

### U:b860f68ae836a8bf:007 — No Meta, mensagem fica escondida em engajamento
```yaml
tipo: regra
plataforma: [meta]
tema: objetivos
tarefas: [escolher-objetivo-de-campanha, criar-campanha-de-mensagem]
fonte: fala
faixa: "00:02:23–00:02:56"
perecivel: true
confianca: alta
versao: 1
```
Para pedir mensagens no WhatsApp, Direct ou Messenger no Meta, selecione o objetivo de engajamento, e não um objetivo com nome de mensagem.
Esse é o único objetivo traiçoeiro da lista, porque o nome não corresponde ao resultado pedido.

### U:b860f68ae836a8bf:008 — Segmentação é infinita e é onde está a dificuldade
```yaml
tipo: conceito
plataforma: [geral]
tema: publicos
tarefas: []
fonte: "fala+pdf:cst_m01_a8.2_taxa_de_acao_estimada_objetivos_e_segmentacoes.pdf"
faixa: "00:02:56–00:03:33"
perecivel: false
confianca: alta
versao: 1
```
As combinações de segmentação dentro do gerenciador são praticamente infinitas e ninguém testará todas em uma vida inteira.
Existe, porém, um consenso sobre quais segmentações usar, e é esse recorte que o curso ensina em vez de tentar cobrir o espaço todo.

### U:b860f68ae836a8bf:009 — Divida sempre os públicos em três temperaturas
```yaml
tipo: regra
plataforma: [geral]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses, montar-publicos-personalizados]
fonte: "fala+pdf:cst_m01_a8.2_taxa_de_acao_estimada_objetivos_e_segmentacoes.pdf"
faixa: "00:03:33–00:04:09"
perecivel: false
confianca: alta
versao: 1
```
Organize toda segmentação em três categorias: públicos super quentes, públicos quentes e públicos frios.
Essa divisão é o padrão adotado no curso e na comunidade, e é a partir dela que se decide para quem anunciar primeiro.

### U:b860f68ae836a8bf:010 — O que é um público super quente
```yaml
tipo: conceito
plataforma: [geral]
tema: publicos
tarefas: []
fonte: "fala+pdf:cst_m01_a8.2_taxa_de_acao_estimada_objetivos_e_segmentacoes.pdf"
faixa: "00:04:11–00:06:06"
perecivel: false
confianca: alta
versao: 1
```
Público super quente é o de pessoas que quase realizaram a ação desejada ou que se envolveram com você muito recentemente, ou seja, com maior probabilidade de cumprir o objetivo da campanha.
Entram aí quem chegou à página e não se cadastrou, quem adicionou ao carrinho e não comprou, quem iniciou a finalização da compra e não comprou, quem entrou no site e não clicou em enviar mensagem, e quem chegou à página de vendas e não foi para o checkout.
A lista de clientes também pode ser super quente quando o negócio tem recompra.
Anunciar para esses públicos costuma sair mais barato, porque a taxa de ação estimada sobe.

### U:b860f68ae836a8bf:011 — Janela do super quente: 1 a 7 dias
```yaml
tipo: regua
plataforma: [geral]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: "00:06:08–00:07:18"
perecivel: false
confianca: alta
versao: 1
```
Trate como super quente o envolvimento recente de 1 a 7 dias: quem visitou o site, quem virou lead ou quem interagiu com você nesse intervalo.
Quem passou muito tempo no site também entra nessa faixa de alto potencial.

### U:b860f68ae836a8bf:012 — O que é um público quente
```yaml
tipo: conceito
plataforma: [geral]
tema: publicos
tarefas: []
fonte: "fala+pdf:cst_m01_a8.2_taxa_de_acao_estimada_objetivos_e_segmentacoes.pdf"
faixa: "00:07:18–00:08:09"
perecivel: false
confianca: alta
versao: 1
```
Público quente é o de quem já teve algum contato com você em algum momento: seguidores, quem se envolveu com seus perfis, quem visitou o site, baixou o aplicativo, viu um vídeo, viu um anúncio ou virou lead no passado.
A janela de envolvimento vai de 7 até 540 dias, ou seja, contatos mais antigos que os do super quente.
Envolvimento aqui vale para qualquer rede em que você anuncia, incluindo Facebook, Instagram, YouTube, TikTok, Pinterest, Twitter e LinkedIn.

### U:b860f68ae836a8bf:013 — Negócio local: raio de 1 a 3 km conta como público quente
```yaml
tipo: regua
plataforma: [geral]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: "00:08:09–00:08:52"
condicoes: "negócio local"
perecivel: false
confianca: alta
versao: 1
```
Em negócio local, trate o público de geolocalização próxima, num raio de 1 a 3 quilômetros, como público quente.
Mesmo sem conhecer a marca, a proximidade já torna a pessoa um comprador em potencial.

### U:b860f68ae836a8bf:014 — O que é um público frio e quais são seus tipos
```yaml
tipo: conceito
plataforma: [geral, google]
tema: publicos
tarefas: []
fonte: "fala+pdf:cst_m01_a8.2_taxa_de_acao_estimada_objetivos_e_segmentacoes.pdf"
faixa: "00:08:52–00:10:54"
perecivel: false
confianca: alta
versao: 1
```
Público frio é o de quem nunca teve contato com você, e é onde está a maioria das pessoas para praticamente qualquer anunciante.
Formam públicos frios os semelhantes, a geolocalização em geral, os públicos abertos (sem segmentação ou só com idade e gênero) e os de direcionamento detalhado, que são os famosos públicos de interesse.
No Google entram ainda os segmentos personalizados, montados por aplicativos usados, buscas feitas e sites acessados, além de públicos por canais e vídeos, público-alvo de mercado (intenção de compra num assunto) e público de afinidade.
A lista de públicos frios não acaba e os testes também não.

### U:b860f68ae836a8bf:015 — Como buscar uma taxa de ação estimada alta
```yaml
tipo: procedimento
plataforma: [geral]
tema: publicos
tarefas: [escolher-objetivo-de-campanha, definir-segmentacao-demografica-e-interesses]
fonte: "fala+pdf:cst_m01_a8.2_taxa_de_acao_estimada_objetivos_e_segmentacoes.pdf"
faixa: "00:10:54–00:11:32"
perecivel: false
confianca: alta
versao: 1
```
Pré-condição: objetivo de negócio definido e conhecimento de quais públicos você já possui.
1. Selecione o objetivo de campanha mais adequado ao resultado que você quer.
2. Foque primeiro nos públicos super quentes.
3. Depois nos públicos quentes.
4. Por último, nos públicos frios.

### U:b860f68ae836a8bf:016 — Sem público quente, comece pelo frio
```yaml
tipo: decisao
plataforma: [geral]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses, montar-publicos-personalizados]
fonte: "fala+pdf:cst_m01_a8.2_taxa_de_acao_estimada_objetivos_e_segmentacoes.pdf"
faixa: "00:11:32–00:12:10"
perecivel: false
confianca: alta
versao: 1
```
Se você está começando e não tem público quente nem super quente, comece anunciando para públicos frios em vez de travar.
Os públicos quentes se formam sozinhos conforme os anúncios rodam: aparecem seguidores, pessoas que se envolveram, visitantes e quem chegou ao checkout sem comprar.

### U:b860f68ae836a8bf:017 — Públicos recomendados para negócio local
```yaml
tipo: decisao
plataforma: [meta, google]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses, montar-publicos-personalizados, montar-lista-de-palavras-chave]
fonte: "fala+pdf:cst_m01_a8.2_taxa_de_acao_estimada_objetivos_e_segmentacoes.pdf"
faixa: "00:11:33–00:13:27"
condicoes: "negócio local"
perecivel: false
confianca: alta
versao: 1
```
Se o negócio é local, anuncie para: lista de clientes (quando há recompra), palavras-chave da marca e do nome, palavras-chave com busca local (produto ou nicho mais a cidade de atendimento).
Some geolocalização em raios crescentes, geolocalização somada a interesses óbvios do público-alvo e geolocalização em bairros específicos, como bairros de maior poder aquisitivo.
Complete com visitantes do site, um mix de públicos quentes e um mix de semelhantes de lista, envolvimento e site.
Sempre segmente a localização nesse tipo de negócio.

### U:b860f68ae836a8bf:018 — Geolocalização WAR: conquistar raios crescentes
```yaml
tipo: procedimento
plataforma: [geral]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: "fala+pdf:cst_m01_a8.2_taxa_de_acao_estimada_objetivos_e_segmentacoes.pdf"
faixa: "00:12:10–00:12:49"
condicoes: "negócio local"
perecivel: false
confianca: alta
versao: 1
```
Pré-condição: negócio com endereço físico de atendimento e campanha com segmentação por localização.
1. Comece anunciando num raio de 1 quilômetro em volta do negócio.
2. Aumente para 2 quilômetros.
3. Depois 3, 4 e 5 quilômetros, conquistando território por etapas como no jogo de tabuleiro que dá nome à tática.

### U:b860f68ae836a8bf:019 — Geolocalização WAR no detalhe fica em outro curso
```yaml
tipo: limite
plataforma: [geral]
tema: publicos
tarefas: []
fonte: fala
faixa: "00:12:10–00:12:50"
perecivel: false
confianca: alta
versao: 1
```
Esta aula apresenta a tática de raios crescentes apenas como nome na lista de públicos de negócio local.
O passo a passo detalhado é declarado como conteúdo do curso de tráfego para negócios locais, fora deste material.

### U:b860f68ae836a8bf:020 — Misture públicos quentes e semelhantes no mesmo grupo
```yaml
tipo: regra
plataforma: [meta]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos, montar-publicos-semelhantes]
fonte: "fala+pdf:cst_m01_a8.2_taxa_de_acao_estimada_objetivos_e_segmentacoes.pdf"
faixa: "00:13:27–00:14:09"
condicoes: "negócio local"
perecivel: false
confianca: alta
versao: 1
```
Junte todos os públicos quentes num mesmo grupo de anúncio em vez de separá-los, porque esse mix funciona bem em negócio local.
Faça o mesmo com os semelhantes: coloque no mesmo grupo mais de um semelhante, derivados de lista, de envolvimento e de site.

### U:b860f68ae836a8bf:021 — Lookalike é público semelhante
```yaml
tipo: conceito
plataforma: [meta]
tema: publicos
tarefas: []
fonte: fala
faixa: "00:13:31–00:14:09"
perecivel: false
confianca: alta
versao: 1
```
Lookalike e público semelhante são a mesma coisa: o termo em inglês virou apelido comum antes de a nomenclatura em português se firmar.

### U:b860f68ae836a8bf:022 — Públicos recomendados para e-commerce
```yaml
tipo: decisao
plataforma: [meta, google]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses, montar-publicos-personalizados, montar-publicos-semelhantes]
fonte: "fala+pdf:cst_m01_a8.2_taxa_de_acao_estimada_objetivos_e_segmentacoes.pdf"
faixa: "00:14:09–00:15:21"
condicoes: "e-commerce"
perecivel: false
confianca: alta
versao: 1
```
Se o negócio é e-commerce, use a lista de clientes com e sem valor de tempo de vida (LTV) e os públicos de comportamento no site nas janelas de 3, 7, 14, 30, 45, 60, 90 e 180 dias: iniciou a compra, adicionou ao carrinho, visitou produtos, visitou o site e se envolveu com o perfil.
Acrescente quem passou determinado tempo no site, a lista de leads e semelhantes de todos esses públicos.
Complete com interesses específicos do nicho, palavras-chave da marca e palavras-chave do produto ou nicho.
No Google, use segmentos personalizados, público-alvo de mercado e público de afinidade.

### U:b860f68ae836a8bf:023 — E-commerce: priorize regiões de frete mais barato
```yaml
tipo: regra
plataforma: [geral]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: "fala+pdf:cst_m01_a8.2_taxa_de_acao_estimada_objetivos_e_segmentacoes.pdf"
faixa: "00:14:44–00:15:21"
condicoes: "loja online com entrega"
perecivel: false
confianca: alta
versao: 1
```
Em loja online, use a geolocalização para concentrar o anúncio nas regiões em que o frete sai mais barato.

### U:b860f68ae836a8bf:024 — Perpétuo: públicos de vendas
```yaml
tipo: decisao
plataforma: [meta, google]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses, montar-publicos-personalizados, montar-publicos-semelhantes]
fonte: "fala+pdf:cst_m01_a8.2_taxa_de_acao_estimada_objetivos_e_segmentacoes.pdf"
faixa: "00:15:21–00:16:00"
condicoes: "perpétuo"
perecivel: false
confianca: alta
versao: 1
```
Se o modelo é perpétuo, separe os públicos entre vendas e remarketing; na frente de vendas use envolvimento de 1 a 30 dias, quem viu 50% de um vídeo de 1 a 30 dias, seguidores e inscritos de 60 a 180 dias e a lista de leads.
Some palavras-chave da marca e palavras-chave do produto ou nicho.
Use ainda semelhantes de clientes, de leads e de envolvimento, interesses óbvios do que você ensina, segmentações abertas, segmentos personalizados, público-alvo de mercado e de afinidade.

### U:b860f68ae836a8bf:025 — Perpétuo: públicos de remarketing
```yaml
tipo: decisao
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-personalizados, definir-segmentacao-demografica-e-interesses]
fonte: "fala+pdf:cst_m01_a8.2_taxa_de_acao_estimada_objetivos_e_segmentacoes.pdf"
faixa: "00:16:00–00:16:43"
condicoes: "perpétuo"
perecivel: false
confianca: alta
versao: 1
```
Se o modelo é perpétuo e a frente é remarketing, use quem iniciou a finalização de compra nos últimos 7 dias e quem caiu na página de vendas nos últimos 14 dias.
Trabalhe também as janelas longas: início de checkout de 7 a 540 dias e página de vendas de 14 a 540 dias.

### U:b860f68ae836a8bf:026 — Lançamento: públicos da etapa de captação
```yaml
tipo: decisao
plataforma: [meta, google]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses, montar-publicos-personalizados, montar-publicos-semelhantes]
fonte: "fala+pdf:cst_m01_a8.2_taxa_de_acao_estimada_objetivos_e_segmentacoes.pdf"
faixa: "00:16:43–00:17:31"
condicoes: "lançamento, etapa de captação"
perecivel: false
confianca: alta
versao: 1
```
Se o trabalho é de lançamento, divida os públicos por etapa; na captação use quem caiu na página de captura sem converter, quem viu os anúncios, quem iniciou checkout ou passou pela página de vendas antes.
Some envolvimento nas janelas de 1, 3, 7, 14, 30, 60, 180 e 365 dias, quem viu seus vídeos, quem se cadastrou em lançamentos antigos e quem já se cadastrou neste lançamento.
Complete com semelhantes de clientes e de cadastrados no evento, interesses do nicho e segmentações abertas.
No Google, use palavras-chave da marca, palavras-chave do produto ou nicho, segmentos personalizados e público-alvo de mercado.

### U:b860f68ae836a8bf:027 — Lembrete, aquecimento e evento: só os cadastrados
```yaml
tipo: decisao
plataforma: [meta]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: "fala+pdf:cst_m01_a8.2_taxa_de_acao_estimada_objetivos_e_segmentacoes.pdf"
faixa: "00:17:31–00:18:11"
condicoes: "lançamento, fases de lembrete, aquecimento e evento"
perecivel: false
confianca: alta
versao: 1
```
Quando o lançamento entra nas fases de lembrete, aquecimento e evento, anuncie apenas para quem se cadastrou no lançamento.

### U:b860f68ae836a8bf:028 — Lançamento: públicos da fase de carrinho
```yaml
tipo: decisao
plataforma: [meta]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses, montar-publicos-personalizados]
fonte: "fala+pdf:cst_m01_a8.2_taxa_de_acao_estimada_objetivos_e_segmentacoes.pdf"
faixa: "00:17:31–00:18:11"
condicoes: "lançamento, fase de carrinho"
perecivel: false
confianca: alta
versao: 1
```
Se o lançamento está na fase de carrinho, anuncie para quem iniciou o checkout ou chegou à página de vendas, para quem viu as aulas do evento e para quem se cadastrou no lançamento.
Inclua também o envolvimento de 14 dias e quem caiu na página de captura do lançamento.

### U:b860f68ae836a8bf:029 — Nesta altura basta conhecer as nomenclaturas
```yaml
tipo: conceito
plataforma: [geral]
tema: fundamentos-e-carreira
tarefas: []
fonte: "fala+pdf:cst_m01_a8.2_taxa_de_acao_estimada_objetivos_e_segmentacoes.pdf"
faixa: "00:18:11–00:18:48"
perecivel: false
confianca: alta
versao: 1
```
O volume de públicos apresentado é grande de propósito e não precisa ser assimilado de uma vez: o objetivo deste ponto do curso é reconhecer os nomes dos públicos.
O mantra é que a confusão é o primeiro passo do entendimento, e a repetição ao longo dos módulos é o que sedimenta o conteúdo.

### U:b860f68ae836a8bf:030 — Super quentes e quentes podem rodar ao mesmo tempo
```yaml
tipo: regra
plataforma: [geral]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: "00:18:48–00:19:23"
perecivel: false
confianca: alta
versao: 1
```
A ordem de prioridade entre super quentes e quentes não obriga a rodar um depois do outro: trabalhe os dois simultaneamente.
São esses dois grupos que entregam a maior taxa de ação estimada.

### U:b860f68ae836a8bf:031 — Anuncie sempre para frios: é onde mora a escala
```yaml
tipo: regra
plataforma: [geral]
tema: escala
tarefas: [escalar-campanha, definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: "00:19:23–00:20:00"
perecivel: false
confianca: alta
versao: 1
```
Mantenha público frio em qualquer divulgação, mesmo tendo muito público quente e super quente.
É no frio que está a maioria das pessoas e, portanto, a escala: crescer muito o resultado depende de gerar resultado para quem ainda não conhece você.
Anunciar para frios também é o que cria os públicos quentes que faltam.

### U:b860f68ae836a8bf:032 — A criação dos públicos fica para as aulas de segmentação
```yaml
tipo: limite
plataforma: [meta, google]
tema: publicos
tarefas: []
fonte: "fala+pdf:cst_m01_a8.2_taxa_de_acao_estimada_objetivos_e_segmentacoes.pdf"
faixa: "00:20:00–00:20:36"
perecivel: false
confianca: alta
versao: 1
```
Esta aula entrega uma lista de nomes de públicos e não mostra a configuração de nenhum deles.
A criação dentro do Meta Ads e do Google Ads é declarada como conteúdo das aulas de segmentação dos módulos seguintes, feita passo a passo junto com o aluno.

### U:b860f68ae836a8bf:033 — Onde ficam os públicos no Google Ads e no Meta
```yaml
tipo: alerta-ui
plataforma: [meta, google]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: "00:20:36–00:21:10"
perecivel: true
confianca: alta
versao: 1
```
No Google Ads os públicos ficam em biblioteca compartilhada, no gerenciador de público-alvo.
No Meta Ads eles ficam na aba de públicos do gerenciador.

### U:b860f68ae836a8bf:034 — Baixe o material da aula como apoio de implementação
```yaml
tipo: regra
plataforma: [geral]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: "00:21:10–00:21:47"
perecivel: false
confianca: alta
versao: 1
```
Baixe o material desta aula, que traz as listas de públicos em imagem, e guarde no computador.
Ele serve de consulta na hora de montar as campanhas, e a aula fica disponível para ser revista quando a prática começar.

### U:b860f68ae836a8bf:035 — Ciclo de estudo: assistir, pausar, implementar
```yaml
tipo: conceito
plataforma: [geral]
tema: fundamentos-e-carreira
tarefas: [formar-se-como-gestor]
fonte: fala
faixa: "00:21:10–00:21:47"
perecivel: false
confianca: alta
versao: 2
nota: "Triagem do módulo 001 (2026-09-14): proposta de tag aceita; tarefa `formar-se-como-gestor` no lugar de tarefas vazias."
```
O curso é feito para ser assistido duas vezes: a primeira para entender e a segunda em paralelo com a execução.
O ciclo é assistir o vídeo, pausar e implementar, repetidamente, referenciando a aula de como aprender tráfego pago.

### U:b860f68ae836a8bf:036 — O terceiro fator do leilão fica para a próxima aula
```yaml
tipo: limite
plataforma: [geral]
tema: leilao-e-lances
tarefas: []
fonte: fala
faixa: "00:22:56–00:23:04"
perecivel: false
confianca: alta
versao: 1
```
A aula cobre lance e taxa de ação estimada e declara que o terceiro fator do leilão, o anúncio, é assunto da aula seguinte.

### U:b860f68ae836a8bf:037 — Mapa mental de segmentações em ferramenta externa
```yaml
tipo: fato-material
plataforma: [geral]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: "txt:Mapa Mental.txt"
perecivel: true
confianca: alta
versao: 1
```
O material da aula inclui um mapa mental de segmentações hospedado no Whimsical, entregue como link externo e não como arquivo.
