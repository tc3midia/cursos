---
type: pagina-tema
status: gerado
title: "atribuicao"
tema: atribuicao
account_id: account.86ajrj8n9
gerado_por: build_indices
---

# Tema — atribuicao

janelas e modelos de atribuição, comparação entre plataformas e relatórios

Página gerada por `build_indices.py`: zero prosa nova; não conta como citação. 53 unidades.

## regra (13)

### `U:54dea110daddeb21:032` — Não existe traqueamento perfeito
*geral · ler-metricas-e-relatorios · [001-5-0-pixel-e-api-de-conversoes](../../unidades/001-5-0-pixel-e-api-de-conversoes.md)*

Entre no assunto sabendo que traqueamento perfeito não existe; quem espera rastrear cada pessoa vai se frustrar.
Ainda assim, há maneiras de identificar boa parte das pessoas e do caminho que elas fizeram até a empresa.

### `U:54dea110daddeb21:033` — Pixel e API são a base do traqueamento
*geral · instalar-pixel-e-eventos, ler-metricas-e-relatorios · [001-5-0-pixel-e-api-de-conversoes](../../unidades/001-5-0-pixel-e-api-de-conversoes.md)*

A primeira ferramenta de traqueamento é o próprio pixel somado à API de conversões, porque são eles que informam à fonte de tráfego o que acontece no site.
Com essa informação chegando, dá para ver qual anúncio, qual público e qual campanha geraram cada compra e medir o retorno do investimento.

### `U:54dea110daddeb21:034` — Google Analytics e UTMs completam o traqueamento
*geral · ler-metricas-e-relatorios · [001-5-0-pixel-e-api-de-conversoes](../../unidades/001-5-0-pixel-e-api-de-conversoes.md)*

Além do pixel e da API, use o Google Analytics com UTMs, que são os parâmetros de acompanhamento.
O Analytics serve para interpretar e identificar o que o usuário faz dentro do site; a UTM é o recurso que marca de onde ele chegou.
É essa dupla que a empresa do professor usa na operação do dia a dia.

### `U:54dea110daddeb21:039` — Pergunte ao cliente final como ele conheceu a empresa
*geral · ler-metricas-e-relatorios · [001-5-0-pixel-e-api-de-conversoes](../../unidades/001-5-0-pixel-e-api-de-conversoes.md)*

O método mais rudimentar de todos continua valendo: pergunte a quem compra onde ele conheceu a empresa.
A resposta costuma vir com a fonte nomeada, como anúncio no Instagram ou anúncio no Google.

### `U:54dea110daddeb21:040` — Lista de compradores com nome, e-mail, telefone e valor
*geral · ler-metricas-e-relatorios · [001-5-0-pixel-e-api-de-conversoes](../../unidades/001-5-0-pixel-e-api-de-conversoes.md)*

Monte, principalmente em negócio local, uma lista das pessoas que compraram, com nome, e-mail, telefone e valor da compra.
Ela resolve o caso de quem viu o anúncio pela internet e fechou a compra dentro do estabelecimento.

### `U:54dea110daddeb21:044` — Importa saber o tamanho da imperfeição
*geral · ler-metricas-e-relatorios · [001-5-0-pixel-e-api-de-conversoes](../../unidades/001-5-0-pixel-e-api-de-conversoes.md)*

Parte dos dados vai se perder no mapeamento, e isso é esperado.
O objetivo não é ter o traqueamento perfeito, e sim saber o quanto ele é imperfeito naquele negócio.

### `U:54dea110daddeb21:047` — O conjunto que o professor considera suficiente
*geral · instalar-pixel-e-eventos, ler-metricas-e-relatorios · [001-5-0-pixel-e-api-de-conversoes](../../unidades/001-5-0-pixel-e-api-de-conversoes.md)*

Com pixel e API de conversões bem instalados via Google Tag Manager, mais Google Analytics e UTMs configuradas, o traqueamento já está resolvido para a maioria dos casos.
Para situações específicas, acrescente página isolada por fonte, canal de venda exclusivo, a pergunta ao cliente e a lista de compradores.
O professor afirma que esse conjunto é mais do que o bastante.

### `U:54dea110daddeb21:048` — Não existe ferramenta de traqueamento perfeito
*geral · ler-metricas-e-relatorios · [001-5-0-pixel-e-api-de-conversoes](../../unidades/001-5-0-pixel-e-api-de-conversoes.md)*

Desconfie de qualquer ferramenta vendida como solução de traqueamento perfeito, porque ela não existe.
O argumento do professor é que nenhuma empresa faz esse trabalho melhor que o Google, então confie nos dados do Google Analytics.

### `U:88a3baf837def058:012` — Manter o padrão da plataforma
*meta, google · configurar-janela-de-atribuicao · [001-12-0-janelas-de-conversao-ou-atribuicao](../../unidades/001-12-0-janelas-de-conversao-ou-atribuicao.md)*

Fique com a configuração padrão de atribuição tanto no Meta quanto no Google.
Pelos testes do professor, o padrão é o que funciona melhor para praticamente todo anunciante.

### `U:88a3baf837def058:021` — Testar janela só depois de rodar no padrão
*meta, google · rodar-testes-e-experimentos · [001-12-0-janelas-de-conversao-ou-atribuicao](../../unidades/001-12-0-janelas-de-conversao-ou-atribuicao.md)*

Não mexa na janela no início: rode tráfego com o padrão por um tempo e só depois entre nos testes de atribuição.

### `U:2e7295a14c7a318f:022` — Google Analytics tende a ser mais confiável para essa leitura
*meta · ler-metricas-e-relatorios · [002-6-13-configurando-o-destino-de-campanhas](../../unidades/002-6-13-configurando-o-destino-de-campanhas.md)*

Para ler dados trazidos pelos parâmetros de URL, o professor afirma que o Google Analytics tende a ser mais confiável que o Meta.

### `U:c27d506b3f3b9659:018` — Primeira configuração vai de último clique
*google · configurar-janela-de-atribuicao · [003-2-0-configurando-seu-pixel](../../unidades/003-2-0-configurando-seu-pixel.md) · condição: conta nova, sem histórico de campanhas*

Na primeira configuração da conta, use o último clique: sem histórico, o modelo baseado em dados não está disponível.

### `U:845d213226687b73:009` — Cookie evita que a mesma pessoa veja as duas campanhas
*google-search · rodar-testes-e-experimentos · [004-8-0-rascunhos-e-experimentos](../../unidades/004-8-0-rascunhos-e-experimentos.md)*

Use a divisão com base em cookie; segundo o professor, ela torna o resultado mais apurado porque a mesma pessoa não vê campanhas diferentes.

## regua (9)

### `U:88a3baf837def058:005` — As quatro janelas do Meta e o que cada uma conta
*meta · configurar-janela-de-atribuicao · [001-12-0-janelas-de-conversao-ou-atribuicao](../../unidades/001-12-0-janelas-de-conversao-ou-atribuicao.md)*

São quatro opções de janela:
1. Clique em 1 dia: só conta para o anúncio clicado nas últimas 24 horas.
2. Clique em 7 dias: só conta para o anúncio clicado nos últimos 7 dias.
3. Clique em 1 dia ou visualização em 1 dia: conta clique ou exibição dentro das últimas 24 horas.
4. Clique em 7 dias ou visualização em 1 dia: conta clique nos últimos 7 dias ou exibição nas últimas 24 horas.

### `U:88a3baf837def058:007` — Padrão do Meta: clique 7 dias ou visualização 1 dia
*meta · configurar-janela-de-atribuicao · [001-12-0-janelas-de-conversao-ou-atribuicao](../../unidades/001-12-0-janelas-de-conversao-ou-atribuicao.md)*

A configuração padrão do Meta é clique em 7 dias ou visualização em 1 dia, definida na campanha.
A maioria dos anunciantes vai ficar com essa opção.

### `U:88a3baf837def058:013` — Janelas do Google e o padrão de 30 dias
*google · configurar-janela-de-atribuicao · [001-12-0-janelas-de-conversao-ou-atribuicao](../../unidades/001-12-0-janelas-de-conversao-ou-atribuicao.md)*

O Google oferece mais opções de prazo que o Meta e permite janelas bem maiores: a de visualização chega a 90 dias, que é o máximo, e ainda aceita um valor personalizado.
O padrão do Google é 30 dias de clique e 1 dia de visualização engajada, e a de visualização engajada também pode ser aumentada até 30 dias.
Com janela longa, um anúncio veiculado agora pode receber conversão três meses depois, quando a pessoa finalmente comprar.
Quem não conhece bem o padrão de compra do seu usuário fica com o padrão do Google.

### `U:88a3baf837def058:014` — Visualização engajada são 10 segundos de vídeo
*google · configurar-janela-de-atribuicao · [001-12-0-janelas-de-conversao-ou-atribuicao](../../unidades/001-12-0-janelas-de-conversao-ou-atribuicao.md)*

A janela de visualização engajada do Google conta a partir do momento em que a pessoa assiste 10 segundos ou mais do anúncio de vídeo.

### `U:88a3baf837def058:020` — Conversão fora da janela não é atribuída
*meta, google · configurar-janela-de-atribuicao, ler-metricas-e-relatorios · [001-12-0-janelas-de-conversao-ou-atribuicao](../../unidades/001-12-0-janelas-de-conversao-ou-atribuicao.md)*

Com clique de 1 dia, só entra a conversão de quem clicou nas últimas 24 horas: quem clicou e comprou 48 horas depois não gera conversão para aquele anúncio.
A janela escolhida é também o tipo de conversão que a plataforma passa a valorizar e a procurar, valendo para Google, Meta, TikTok, Pinterest, LinkedIn e Twitter.

### `U:7c86762dc9b85fdf:016` — Preferência do professor por janela de 7 dias
*meta · configurar-janela-de-atribuicao · [002-6-5-conversao](../../unidades/002-6-5-conversao.md) · condição: preferência pessoal do professor; testar o que funciona para a campanha · perecível*

O professor prefere manter 7 dias nas campanhas porque, na opinião dele, isso traz mais dados.
A janela escolhida orienta o Meta a procurar pessoas com tendência de converter dentro daquele prazo.

### `U:7c86762dc9b85fdf:017` — Janela de engajamento considera 10 segundos de vídeo
*meta · configurar-janela-de-atribuicao · [002-6-5-conversao](../../unidades/002-6-5-conversao.md) · perecível*

A janela de engajamento considera quem assistiu pelo menos 10 segundos do vídeo.
O professor não vê sentido em mantê-la em 1 dia porque ela conta junto com a janela de visualização.

### `U:7c86762dc9b85fdf:018` — Google tem janela padrão de visualização de vídeo de 3 dias
*google · configurar-janela-de-atribuicao · [002-6-5-conversao](../../unidades/002-6-5-conversao.md)*

No Google, a janela de visualização de vídeo é de 3 dias por padrão e pode ser configurada para um prazo maior.

### `U:c27d506b3f3b9659:013` — Deixe a janela de conversão como veio
*google · configurar-janela-de-atribuicao · [003-2-0-configurando-seu-pixel](../../unidades/003-2-0-configurando-seu-pixel.md) · condição: primeiras configurações de conta*

Não mexa na janela de conversão no começo: mantenha os 30 dias que já vêm marcados.
É possível personalizar o prazo, por exemplo 20 dias, mas isso encurta o tempo em que os anúncios se lembram de quem clicou.
Só alongue quando o ciclo do negócio pedir: em venda de imóvel, em que o fechamento costuma levar 90 dias, faz sentido configurar esse prazo.

## procedimento (3)

### `U:54dea110daddeb21:036` — Página isolada por fonte com carimbo no CRM
*geral · ler-metricas-e-relatorios · [001-5-0-pixel-e-api-de-conversoes](../../unidades/001-5-0-pixel-e-api-de-conversoes.md)*

Pré-condição: poder criar páginas separadas no site e ter uma ferramenta de e-mail (CRM) recebendo os cadastros.
1. Crie uma página de captura por fonte de tráfego, com o nome da fonte no endereço (por exemplo, aulas-meta e aulas-pesquisa).
2. Divulgue cada endereço apenas nos anúncios da fonte correspondente.
3. Configure a página para aplicar uma etiqueta no contato que se cadastra ali, com o nome da fonte.
4. Leia os cadastros por etiqueta no CRM para saber de onde veio cada pessoa.
O professor classifica o método como rudimentar e diz que funciona muito bem.

### `U:1c750220ccdd4d82:012` — Criar meta de destino no Google Analytics Universal
*google · definir-conversoes-e-metas · [004-7-7-como-utilizar-o-google-optimize-para-fazer-teste-a-b-com-paginas](../../unidades/004-7-7-como-utilizar-o-google-optimize-para-fazer-teste-a-b-com-paginas.md) · perecível*

Pré-condição: acesso ao Google Analytics Universal e conhecimento do final da URL de conversão.
1. Em “administrador”, abra “metas” e clique em “nova meta”.
2. Selecione “personalizado”, nomeie a meta e escolha o tipo “destino”.
3. Em detalhes, selecione “começa com”, informe o final da URL e salve.

### `U:1c750220ccdd4d82:013` — Vincular o Optimize ao Analytics e selecionar a meta
*google · definir-conversoes-e-metas, rodar-testes-e-experimentos · [004-7-7-como-utilizar-o-google-optimize-para-fazer-teste-a-b-com-paginas](../../unidades/004-7-7-como-utilizar-o-google-optimize-para-fazer-teste-a-b-com-paginas.md) · perecível*

Pré-condição: existir uma meta de destino no Google Analytics.
1. Em “medição e objetivos” no Optimize, clique no ícone de pincel do campo “Google Analytics”.
2. Verifique a vinculação e deixe selecionado “todos os dados do website”.
3. Em “objetivo principal”, escolha a meta criada na lista.
4. Se a meta recém-criada não aparecer, atualize a página e procure-a novamente.

## decisao (8)

### `U:54dea110daddeb21:037` — Quando quiser separar por temperatura de público, prefira Analytics e UTMs
*geral · ler-metricas-e-relatorios · [001-5-0-pixel-e-api-de-conversoes](../../unidades/001-5-0-pixel-e-api-de-conversoes.md)*

Quando a ideia for desdobrar as páginas isoladas por temperatura de público, criando um endereço para o frio e outro para o quente, saiba que isso dá muito mais trabalho.
O professor diz que o efeito é muito parecido usando Google Analytics e UTMs, que é o caminho adotado na empresa dele.

### `U:54dea110daddeb21:038` — Quando o cliente é negócio local, use um WhatsApp só do tráfego pago
*geral · ler-metricas-e-relatorios · [001-5-0-pixel-e-api-de-conversoes](../../unidades/001-5-0-pixel-e-api-de-conversoes.md) · condição: cliente é negócio local com atendimento por WhatsApp*

Quando o negócio local concentra tudo em um número de WhatsApp, chegam ali cliente de aplicativo de entrega, quem achou a empresa organicamente, cliente antigo e quem veio dos anúncios, sem distinção.
Nesse caso, crie um canal de venda exclusivo do tráfego pago — um WhatsApp separado — para saber que todo contato daquele número veio da campanha.

### `U:88a3baf837def058:009` — Janela pelo tempo de decisão do produto
*meta · configurar-janela-de-atribuicao · [001-12-0-janelas-de-conversao-ou-atribuicao](../../unidades/001-12-0-janelas-de-conversao-ou-atribuicao.md) · condição: só quando decidir sair do padrão da plataforma*

Se o produto é de compra impulsiva e barato, com pouca decisão envolvida, use clique de 1 dia.
Se o produto exige pesquisa e comparação, como uma geladeira, use clique de 7 dias.
A régua é sempre o comportamento de compra do cliente: quanto mais demorada a decisão, maior a janela.

### `U:88a3baf837def058:018` — Comece pelo baseado em dados, senão último clique
*geral, google · configurar-janela-de-atribuicao · [001-12-0-janelas-de-conversao-ou-atribuicao](../../unidades/001-12-0-janelas-de-conversao-ou-atribuicao.md)*

Se a plataforma oferece o modelo baseado em dados, comece por ele: é o que o professor usa, porque sente as campanhas melhorarem com ele.
Quando a fonte de tráfego não tem baseado em dados, use último clique, que também ajuda a ler melhor os resultados.
Deixe o último clique como teste futuro e não gaste teste com os demais modelos.

### `U:88a3baf837def058:019` — Critério para testar uma janela diferente
*meta, google · rodar-testes-e-experimentos, configurar-janela-de-atribuicao · [001-12-0-janelas-de-conversao-ou-atribuicao](../../unidades/001-12-0-janelas-de-conversao-ou-atribuicao.md)*

Se for testar uma janela diferente do padrão, decida pelo comportamento de compra do usuário.
A pergunta que guia o teste é quanto tempo a pessoa costuma levar entre clicar no anúncio e decidir comprar.

### `U:7c86762dc9b85fdf:014` — Iniciante não deve mexer na configuração de atribuição
*meta · configurar-janela-de-atribuicao · [002-6-5-conversao](../../unidades/002-6-5-conversao.md) · perecível*

Se você é muito iniciante e tem dúvida sobre janela de atribuição, não mexa na configuração.
Para quem já é mais avançado, o professor menciona janela de clique de 1 dia e janela de visualização de nenhum dia.

### `U:7c86762dc9b85fdf:015` — Ajustar a janela ao padrão de conversão do usuário
*meta · configurar-janela-de-atribuicao · [002-6-5-conversao](../../unidades/002-6-5-conversao.md) · perecível*

Se a decisão de compra costuma levar mais tempo, como na compra de uma geladeira, prefira 7 dias em vez de 1 dia.
Se a ação costuma ocorrer no mesmo dia, como baixar um livro gratuito, 1 dia pode funcionar.
A recomendação do Meta, citada pelo professor, é usar a janela mais adequada ao comportamento do usuário.

### `U:c27d506b3f3b9659:017` — Último clique ou baseado em dados
*google · configurar-janela-de-atribuicao, definir-conversoes-e-metas · [003-2-0-configurando-seu-pixel](../../unidades/003-2-0-configurando-seu-pixel.md) · condição: o modelo baseado em dados só fica disponível em conta com histórico suficiente*

Se for escolher modelo de atribuição, fique entre último clique e baseado em dados: para o professor são os dois que fazem sentido.
O modelo baseado em dados distribui o crédito pelo histórico da conta e só abre quando há dados suficientes, então entra no futuro, com a conta mais rodada.
Consultores e funcionários do Google recomendam muito o baseado em dados; o professor usa último clique e sugere testar o outro depois para ver se melhora os anúncios.

## conceito (14)

### `U:54dea110daddeb21:031` — Traqueamento é rastrear comportamento e origem
*geral · sem tarefa · [001-5-0-pixel-e-api-de-conversoes](../../unidades/001-5-0-pixel-e-api-de-conversoes.md)*

Traquear é rastrear o comportamento do usuário e entender de onde ele veio.
Sem isso, quem recebe uma mensagem no WhatsApp não sabe se aquela pessoa pesquisou a marca no Google, viu um anúncio no Instagram ou no YouTube, nem de qual campanha e público ela saiu.

### `U:88a3baf837def058:001` — Janela de conversão e janela de atribuição são o mesmo conceito
*meta, google · sem tarefa · [001-12-0-janelas-de-conversao-ou-atribuicao](../../unidades/001-12-0-janelas-de-conversao-ou-atribuicao.md)*

Os dois nomes descrevem a mesma coisa: o Meta usa "janela de atribuição" e o Google usa "janela de conversão".
No começo do Facebook Ads existiam os dois tipos separados, o que confundia todo mundo, e a plataforma passou a usar um nome só.

### `U:88a3baf837def058:002` — O que a janela de atribuição decide
*meta, google · sem tarefa · [001-12-0-janelas-de-conversao-ou-atribuicao](../../unidades/001-12-0-janelas-de-conversao-ou-atribuicao.md)*

A janela é a forma pela qual a fonte de tráfego identifica qual anúncio, qual público e qual campanha respondem por uma conversão.
Sem ela não há como saber a quem creditar uma venda que acontece depois de mais de um contato do usuário com os anúncios.

### `U:88a3baf837def058:004` — Três fatores definem quem recebe a conversão
*meta, google · sem tarefa · [001-12-0-janelas-de-conversao-ou-atribuicao](../../unidades/001-12-0-janelas-de-conversao-ou-atribuicao.md)*

Os fatores que a janela considera são clique, visualização e visualização engajada.
No Meta existem apenas os dois primeiros; a visualização engajada só aparece no Google.

### `U:88a3baf837def058:006` — A analogia da memória curta
*geral · sem tarefa · [001-12-0-janelas-de-conversao-ou-atribuicao](../../unidades/001-12-0-janelas-de-conversao-ou-atribuicao.md)*

Explicação de um aluno da comunidade que o professor adota: se alguém leva um tapa na cara, a janela é o tempo em que a pessoa continua brava, e tudo que ela faz nesse período é consequência do tapa.
O tapa é o anúncio que impactou o usuário, a reação é o evento que a campanha recebe e a memória é o tempo de atribuição.
Janela maior significa anúncio com memória mais longa.

### `U:88a3baf837def058:011` — A janela escolhida guia a otimização
*meta, google · sem tarefa · [001-12-0-janelas-de-conversao-ou-atribuicao](../../unidades/001-12-0-janelas-de-conversao-ou-atribuicao.md)*

A configuração de atribuição alinha a conversão que o sistema otimiza com a conversão que você quer medir.
Com uma janela de clique e visualização de 1 dia, a plataforma aprende com as conversões ocorridas nesse prazo e passa a buscar pessoas com probabilidade de converter nesse mesmo prazo.

### `U:88a3baf837def058:016` — Modelo de atribuição existe só no Google
*google · sem tarefa · [001-12-0-janelas-de-conversao-ou-atribuicao](../../unidades/001-12-0-janelas-de-conversao-ou-atribuicao.md)*

Além da janela, o Google tem o modelo de atribuição, que determina quanto crédito cada interação com o anúncio recebe na conversão.
A janela diz quem pode receber; o modelo diz como a conversão é distribuída entre as interações.

### `U:88a3baf837def058:017` — Os modelos de atribuição do Google
*google · sem tarefa · [001-12-0-janelas-de-conversao-ou-atribuicao](../../unidades/001-12-0-janelas-de-conversao-ou-atribuicao.md)*

Último clique: o último anúncio clicado leva a conversão inteira; é o modelo que o Meta usa.
Primeiro clique: quem leva é o primeiro anúncio clicado.
Linear: a conversão é dividida igualmente entre os anúncios clicados no caminho.
Iminência da conversão: dá mais crédito aos cliques mais próximos do momento da compra.
Baseado em posição: 40% para o primeiro clique, 40% para o último e 20% divididos entre os do meio.
Baseado em dados: usa o histórico de conversões da própria conta para calcular a contribuição real de cada interação.

### `U:7c86762dc9b85fdf:013` — Janela de atribuição define até quando crédito vai ao anúncio
*meta · sem tarefa · [002-6-5-conversao](../../unidades/002-6-5-conversao.md)*

A janela de atribuição determina por quanto tempo uma conversão pode ser atribuída a um clique ou visualização de anúncio.
No exemplo, um clique recebe crédito se a pessoa converter 5 dias depois sem interagir com outro anúncio; uma visualização pode receber crédito se a conversão ocorrer 13 horas depois sem nova interação.

### `U:2e7295a14c7a318f:021` — Parâmetros de URL identificam a origem do clique
*meta · ler-metricas-e-relatorios · [002-6-13-configurando-o-destino-de-campanhas](../../unidades/002-6-13-configurando-o-destino-de-campanhas.md)*

Parâmetros de URL adicionam informações à URL do site, como campanha, anúncio, conjunto de anúncios e posicionamento do clique.
Para ler essas informações, o professor diz que é necessário usar Google Analytics.

### `U:c27d506b3f3b9659:012` — O que é a janela de conversão
*google · sem tarefa · [003-2-0-configurando-seu-pixel](../../unidades/003-2-0-configurando-seu-pixel.md)*

A janela de conversão é por quanto tempo a ferramenta continua lembrando que a pessoa clicou no anúncio.
A analogia do professor: o anúncio é um tapa na cara e a janela é o tempo que você leva para esquecer que levou o tapa.
Exemplo do prazo: alguém clica no anúncio em primeiro de janeiro, encontra o site por outro caminho dias depois e se cadastra; a janela decide se aquele clique leva o crédito.

### `U:c27d506b3f3b9659:014` — Janela de conversão de visualização engajada
*google · sem tarefa · [003-2-0-configurando-seu-pixel](../../unidades/003-2-0-configurando-seu-pixel.md)*

Funciona como a janela de conversão, só que a partir do engajamento com o vídeo: a pessoa assistiu inteiro, curtiu ou interagiu de alguma forma.
O prazo diz por quanto tempo depois desse engajamento a conversão ainda pode ser creditada ao anúncio; o professor mantém 30 dias.

### `U:c27d506b3f3b9659:015` — Janela de conversão de visualização
*google · sem tarefa · [003-2-0-configurando-seu-pixel](../../unidades/003-2-0-configurando-seu-pixel.md)*

Aqui a pessoa não clicou: ela apenas viu o anúncio.
Se a conversão acontecer em até 24 horas depois dessa visualização — cadastro, compra ou o que for a conversão do negócio — o Google credita o resultado àquele anúncio.

### `U:c27d506b3f3b9659:016` — O que o modelo de atribuição decide
*google · sem tarefa · [003-2-0-configurando-seu-pixel](../../unidades/003-2-0-configurando-seu-pixel.md)*

Quando a pessoa clica em vários anúncios antes de converter, o modelo de atribuição decide qual deles leva o crédito.
No último clique, o crédito é do último anúncio clicado; há também primeiro clique e linear, entre vários que o Google oferece.
No linear o crédito se reparte: com três anúncios no caminho, cada um fica responsável por 0,33 daquela conversão.

## exemplo (2)

### `U:88a3baf837def058:003` — João, a garrafa d'água e os dois anúncios
*meta · configurar-janela-de-atribuicao · [001-12-0-janelas-de-conversao-ou-atribuicao](../../unidades/001-12-0-janelas-de-conversao-ou-atribuicao.md)*

Situação: João vê na timeline o anúncio de uma garrafa d'água, clica, entra no site, gosta do produto e adia a compra.
O que aconteceu: no dia seguinte outro anúncio da mesma garrafa aparece para ele em outra plataforma; dessa vez ele não clica, digita o endereço do site no buscador e compra.
Lógica: houve um clique num dia e uma visualização no outro, e é a janela configurada que decide qual dos dois anúncios recebe a conversão.

### `U:88a3baf837def058:010` — Conversão sem clique entra pela visualização
*meta · configurar-janela-de-atribuicao · [001-12-0-janelas-de-conversao-ou-atribuicao](../../unidades/001-12-0-janelas-de-conversao-ou-atribuicao.md)*

Situação: o anúncio da garrafa aparece para a pessoa, que não clica em nada.
O que aconteceu: ela pesquisa o produto no buscador, entra no site por conta própria e compra no mesmo dia.
Lógica: com uma janela que inclui visualização de 1 dia, essa compra é contabilizada para o anúncio que foi apenas exibido, sem clique nenhum.

## alerta-ui (1)

### `U:88a3baf837def058:015` — Onde a janela é configurada em cada plataforma
*meta, google · configurar-janela-de-atribuicao · [001-12-0-janelas-de-conversao-ou-atribuicao](../../unidades/001-12-0-janelas-de-conversao-ou-atribuicao.md) · perecível*

No Meta a janela de atribuição é definida dentro da campanha.
No Google Ads a mesma configuração fica no evento de conversão, não na campanha.
Os lugares são diferentes, a lógica é a mesma.

## limite (3)

### `U:54dea110daddeb21:035` — Analytics e UTMs têm curso próprio na comunidade
*geral · sem tarefa · [001-5-0-pixel-e-api-de-conversoes](../../unidades/001-5-0-pixel-e-api-de-conversoes.md) · perecível*

Esta aula não ensina Google Analytics nem UTMs: existe um curso específico na comunidade que cobre toda essa parte de traqueamento.

### `U:88a3baf837def058:022` — O que a aula deixa para as aulas de campanha
*meta, google · sem tarefa · [001-12-0-janelas-de-conversao-ou-atribuicao](../../unidades/001-12-0-janelas-de-conversao-ou-atribuicao.md)*

A aula é um primeiro contato com o assunto e não ensina a mexer nas configurações.
Onde clicar e como definir janela e modelo em cada plataforma fica para as aulas de criação de campanha, onde o professor promete repetir a recomendação de usar o padrão e relembrar os testes possíveis.

### `U:2e7295a14c7a318f:023` — Parâmetros dinâmicos ficam para o curso de Analytics
*meta · sem tarefa · [002-6-13-configurando-o-destino-de-campanhas](../../unidades/002-6-13-configurando-o-destino-de-campanhas.md) · perecível*

A aula não detalha o uso dos parâmetros dinâmicos de rastreamento do Meta.
O professor indica especificações de parâmetros dinâmicos e diz que o uso será aprendido no curso de Google Analytics, com link no material extra da aula.

## Temas relacionados (coocorrência de tarefa)

- [pixel-e-eventos](pixel-e-eventos.md) — 4 tarefas em comum
- [fundamentos-e-carreira](fundamentos-e-carreira.md) — 3 tarefas em comum
- [metricas-e-relatorios](metricas-e-relatorios.md) — 3 tarefas em comum
- [destino-e-landing-page](destino-e-landing-page.md) — 2 tarefas em comum
- [nomenclatura](nomenclatura.md) — 2 tarefas em comum
- [objetivos](objetivos.md) — 2 tarefas em comum
- [otimizacao](otimizacao.md) — 2 tarefas em comum
- [publicos](publicos.md) — 2 tarefas em comum
- [testes-e-experimentos](testes-e-experimentos.md) — 2 tarefas em comum
- [conta-e-configuracao](conta-e-configuracao.md) — 1 tarefas em comum
- [copy-e-roteiro](copy-e-roteiro.md) — 1 tarefas em comum
- [criativo](criativo.md) — 1 tarefas em comum
- [escala](escala.md) — 1 tarefas em comum
- [estrutura-de-campanha](estrutura-de-campanha.md) — 1 tarefas em comum
- [leilao-e-lances](leilao-e-lances.md) — 1 tarefas em comum
- [orcamento](orcamento.md) — 1 tarefas em comum
- [palavras-chave](palavras-chave.md) — 1 tarefas em comum

## Playbooks que citam unidades deste tema

- nenhum
