---
type: unidades-aula
status: validado
title: "7.1 - Campanhas de Catálogo"
modulo: "002"
ordem: 45
aula_id: 7cc58e06ed6a16b7
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

# 7.1 - Campanhas de Catálogo

## Contexto da aula

A aula demonstra campanhas de catálogo no Meta Ads para e-commerces.
Explica duas formas de habilitar anúncios que usam informações dinâmicas do site.
Mostra conjuntos de produtos, combinações de públicos para remarketing e exemplos de segmentação.
Também percorre formatos, personalizações e textos dinâmicos do anúncio de catálogo.
Não aprofunda orçamento, atribuição nem configuração de Deep Link.

## Unidades

### U:7cc58e06ed6a16b7:001 — Duas formas de usar catálogo no Meta Ads
```yaml
tipo: conceito
plataforma: [meta]
tema: estrutura-de-campanha
tarefas: [criar-campanha-de-catalogo]
fonte: fala
faixa: "00:00:00–00:04:04"
perecivel: false
confianca: alta
versao: 1
```
O catálogo pode ser configurado na campanha ou apenas no anúncio, pela fonte do criativo.
Nas duas formas, o anúncio lê dinamicamente as informações dos produtos do site.

### U:7cc58e06ed6a16b7:002 — Habilitar catálogo na configuração da campanha de vendas
```yaml
tipo: procedimento
plataforma: [meta]
tema: estrutura-de-campanha
tarefas: [criar-campanha-de-catalogo]
fonte: fala
faixa: "00:00:00–00:01:19"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: campanha de vendas manual criada.
1. Na configuração da campanha, selecione a opção de catálogo.
2. Ative ou desative essa opção conforme queira usar ou retirar o catálogo da campanha.
3. Nomeie campanha, conjunto e anúncio conforme sua nomenclatura.

### U:7cc58e06ed6a16b7:003 — Catálogo altera opções do conjunto e do anúncio
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: estrutura-de-campanha
tarefas: [criar-campanha-de-catalogo]
fonte: fala
faixa: "00:01:19–00:02:44"
perecivel: true
confianca: alta
versao: 1
```
Com catálogo selecionado, o conjunto pede um conjunto de produtos e o tipo de público.
No anúncio, o catálogo já vem como fonte e há formatos de imagem ou vídeo, carrossel e coleção.
A mídia não é escolhida manualmente porque vem dinamicamente do site.

### U:7cc58e06ed6a16b7:004 — Escolher destino conforme existência de aplicativo
```yaml
tipo: decisao
plataforma: [meta]
tema: destino-e-landing-page
tarefas: [configurar-anuncio]
fonte: fala
faixa: "00:01:59–00:02:44"
perecivel: true
confianca: alta
versao: 1
```
Se houver aplicativo, use destino Advantage Plus para enviar pessoas ao aplicativo ou ao site.
Se não houver aplicativo, use destino Manual.

### U:7cc58e06ed6a16b7:005 — Usar catálogo somente na fonte do criativo
```yaml
tipo: procedimento
plataforma: [meta]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: "00:02:44–00:04:04"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: campanha sem catálogo na configuração da campanha.
1. Configure campanha, conversão e pixel como em uma campanha padrão.
2. No anúncio, abra a fonte do criativo.
3. Troque carregamento manual por catálogo.

### U:7cc58e06ed6a16b7:006 — Testar as duas configurações de catálogo
```yaml
tipo: regra
plataforma: [meta]
tema: testes-e-experimentos
tarefas: [criar-campanha-de-catalogo, rodar-testes-e-experimentos]
fonte: fala
faixa: "00:04:04–00:04:42"
perecivel: false
confianca: alta
versao: 1
```
Para qualquer loja online, teste campanhas de catálogo e campanhas normais que usam catálogo como fonte do criativo.
O professor não considera uma opção universalmente melhor que a outra.

### U:7cc58e06ed6a16b7:007 — Comparar cliques e conversões em catálogo
```yaml
tipo: procedimento
plataforma: [meta]
tema: testes-e-experimentos
tarefas: [escolher-estrategia-de-lance, rodar-testes-e-experimentos]
fonte: fala
faixa: "00:04:42–00:06:01"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: campanha de catálogo com conjunto de anúncios configurado.
1. Confira a meta de desempenho, pois o catálogo pode abrir com maximizar cliques no link.
2. Crie um conjunto focado em maximizar conversões.
3. Duplique-o de forma idêntica, mudando apenas para maximizar cliques.
4. Compare qual funciona melhor para o negócio.
```
condicoes: "O professor começaria por maximizar o número de conversões; não apresenta resposta definitiva."
```

### U:7cc58e06ed6a16b7:008 — Conjunto de produtos define o que será anunciado
```yaml
tipo: conceito
plataforma: [meta]
tema: estrutura-de-campanha
tarefas: [criar-campanha-de-catalogo]
fonte: fala
faixa: "00:05:23–00:07:22"
perecivel: false
confianca: alta
versao: 1
```
CP significa conjunto de produtos: é o grupo de produtos que será anunciado na campanha de catálogo.
O CP pode ser filtrado por identificação, título, marca, preço, gênero, faixa etária, tamanho, material e preço promocional.

### U:7cc58e06ed6a16b7:009 — Criar conjunto de produtos com filtros
```yaml
tipo: procedimento
plataforma: [meta]
tema: estrutura-de-campanha
tarefas: [criar-campanha-de-catalogo]
fonte: fala
faixa: "00:06:01–00:07:22"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: catálogo de produtos disponível no conjunto de anúncios.
1. Clique em mais para criar um conjunto de produtos e dê um nome a ele.
2. Escolha o atributo para filtrar os itens.
3. Defina o valor do filtro, como preço maior que R$ 50 ou maior que R$ 120.
4. Salve o grupo de produtos resultante.

### U:7cc58e06ed6a16b7:010 — Manter CP de todos os produtos e curvas A, B e C
```yaml
tipo: regra
plataforma: [meta]
tema: estrutura-de-campanha
tarefas: [criar-campanha-de-catalogo]
fonte: fala
faixa: "00:07:23–00:09:37"
perecivel: false
confianca: alta
versao: 1
```
Deixe criado o CP de todos os produtos, que tende a ser o mais usado, e CPs das curvas A, B e C.
A curva A reúne produtos com maior saída; B e C classificam os demais produtos pela metodologia apresentada.

### U:7cc58e06ed6a16b7:011 — Distribuição apresentada para curvas A, B e C
```yaml
tipo: regua
plataforma: [meta]
tema: estrutura-de-campanha
tarefas: [criar-campanha-de-catalogo]
fonte: fala
faixa: "00:08:15–00:08:56"
perecivel: false
confianca: alta
versao: 1
```
Na explicação usada pelo professor, a curva A são 20% dos itens e 80% da receita.
A curva B são 30% dos itens e 15% da receita; a curva C são 50% dos itens e 5% da receita.
```
nota: "O professor menciona que há explicações diferentes para a categorização."
```

### U:7cc58e06ed6a16b7:012 — Criar CPs específicos para lógica do negócio
```yaml
tipo: regra
plataforma: [meta]
tema: estrutura-de-campanha
tarefas: [criar-campanha-de-catalogo]
fonte: fala
faixa: "00:08:56–00:10:56"
perecivel: false
confianca: alta
versao: 1
```
Crie CPs específicos quando a lógica comercial exigir produtos diferentes para cada interação.
Também vale criar CPs de ticket mais alto, produtos de maior saída, produtos em promoção e produtos com alta conversão e pouca compra.
Produtos em promoção precisam de atualização constante.

### U:7cc58e06ed6a16b7:013 — Usar CP de anúncio e CP de segmentação
```yaml
tipo: conceito
plataforma: [meta]
tema: publicos
tarefas: [criar-campanha-de-catalogo]
fonte: fala
faixa: "00:10:58–00:12:51"
perecivel: false
confianca: alta
versao: 1
```
O CP de anúncio contém os produtos que serão promovidos.
O CP de segmentação define os produtos com que as pessoas interagiram antes de receber o anúncio.
Interagir pode significar visualizar, adicionar ao carrinho ou comprar.

### U:7cc58e06ed6a16b7:014 — Combinar CPs de anúncio e de segmentação
```yaml
tipo: regra
plataforma: [meta]
tema: publicos
tarefas: [criar-campanha-de-catalogo]
fonte: fala
faixa: "00:11:28–00:12:51"
perecivel: false
confianca: alta
versao: 1
```
Use todos os produtos para todos os produtos como combinação comum.
Também é possível anunciar um CP para quem interagiu com ele próprio ou para quem interagiu com outro CP.

### U:7cc58e06ed6a16b7:015 — Testar catálogo no anúncio em vez de prospecção por campanha
```yaml
tipo: decisao
plataforma: [meta]
tema: estrutura-de-campanha
tarefas: [criar-campanha-de-catalogo, rodar-testes-e-experimentos]
fonte: fala
faixa: "00:12:52–00:14:13"
perecivel: true
confianca: media
versao: 1
nota: "O professor declara que é sua opinião, sem documentação, e reconhece discordâncias."
```
Se quiser encontrar possíveis clientes sem interação prévia, o professor considera equivalente desativar catálogo na campanha e selecionar catálogo no anúncio.
Segundo a opinião dele, as duas formas preservam o mesmo poder de segmentação.

### U:7cc58e06ed6a16b7:016 — Conferir configurações após alterar a campanha
```yaml
tipo: regra
plataforma: [meta]
tema: estrutura-de-campanha
tarefas: [criar-campanha-de-catalogo]
fonte: fala
faixa: "00:14:13–00:14:52"
perecivel: true
confianca: alta
versao: 1
```
Depois de alterar a campanha, confira as configurações novamente porque o Meta pode resetá-las.

### U:7cc58e06ed6a16b7:017 — Público de visualização ou carrinho exclui compradores
```yaml
tipo: conceito
plataforma: [meta]
tema: publicos
tarefas: [criar-campanha-de-catalogo]
fonte: fala
faixa: "00:14:52–00:16:34"
perecivel: true
confianca: alta
versao: 1
```
Na opção de promover produtos para quem visualizou ou adicionou ao carrinho, os compradores já aparecem excluídos.
O prazo pode ser alterado; adicionar ao carrinho sem compra nos últimos 7 dias não é a mesma segmentação de visualizar ou adicionar nos últimos 14 dias.

### U:7cc58e06ed6a16b7:018 — Usar upsell para cruzar interação entre CPs
```yaml
tipo: conceito
plataforma: [meta]
tema: publicos
tarefas: [criar-campanha-de-catalogo]
fonte: fala
faixa: "00:16:34–00:18:00"
perecivel: true
confianca: alta
versao: 1
```
No upsell, anuncie um conjunto de produtos para pessoas que visualizaram ou adicionaram ao carrinho produtos de outro CP.
Na tela demonstrada, essa opção não indicava exclusão de quem comprou.

### U:7cc58e06ed6a16b7:019 — Usar venda cruzada para compradores de outro CP
```yaml
tipo: conceito
plataforma: [meta]
tema: publicos
tarefas: [criar-campanha-de-catalogo]
fonte: fala
faixa: "00:18:00–00:18:42"
perecivel: true
confianca: alta
versao: 1
```
Na venda cruzada, anuncie determinados produtos para pessoas que compraram produtos de outro CP.
O exemplo mostra produtos de curva A para pessoas que compraram qualquer produto nos últimos 14 dias.

### U:7cc58e06ed6a16b7:020 — Preferir combinação personalizada para segmentar catálogo
```yaml
tipo: regra
plataforma: [meta]
tema: publicos
tarefas: [criar-campanha-de-catalogo]
fonte: fala
faixa: "00:18:42–00:21:38"
perecivel: true
confianca: alta
versao: 1
```
Use combinação personalizada para controlar CP anunciado, CP de segmentação, tipo de interação, prazo e exclusões.
O professor diz usar apenas essa opção porque ela permite reproduzir as combinações mostradas acima.

### U:7cc58e06ed6a16b7:021 — Expandir ou limitar com públicos personalizados
```yaml
tipo: procedimento
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-personalizados, criar-campanha-de-catalogo]
fonte: fala
faixa: "00:20:57–00:24:19"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: combinação personalizada configurada e público personalizado disponível.
1. Para expandir, inclua o público adicional para alcançar quem está em um grupo ou no outro.
2. Para limitar, exija que a pessoa pertença à combinação de catálogo e ao público adicional.
3. Na nomenclatura de limitação, use “i” para indicar que as duas condições são exigidas.

### U:7cc58e06ed6a16b7:022 — Priorizar testes de combinações de públicos
```yaml
tipo: regra
plataforma: [meta]
tema: testes-e-experimentos
tarefas: [rodar-testes-e-experimentos, criar-campanha-de-catalogo]
fonte: fala
faixa: "00:23:41–00:24:19"
perecivel: false
confianca: alta
versao: 1
```
Teste expansão e limitação de públicos, mas priorize os tipos de combinação de públicos do catálogo.
Segundo o professor, essas combinações são o principal ponto a testar para buscar resultado.

### U:7cc58e06ed6a16b7:023 — Escalonar CPs conforme tempo desde o carrinho
```yaml
tipo: exemplo
plataforma: [meta]
tema: publicos
tarefas: [criar-campanha-de-catalogo, rodar-testes-e-experimentos]
fonte: fala
faixa: "00:24:24–00:25:56"
perecivel: false
confianca: alta
versao: 1
```
Situação: pessoas adicionaram produtos ao carrinho em períodos diferentes.
O que aconteceu: o professor propõe todos os produtos para carrinho em 7 dias, curva B para carrinho em 14 dias excluindo 7 dias e curva A para carrinho em 30 dias excluindo 14 dias.
Lógica: variar o CP anunciado conforme a hierarquia de recência e as exclusões.

### U:7cc58e06ed6a16b7:024 — Ajustar janela de recompra ao ciclo do produto
```yaml
tipo: decisao
plataforma: [meta]
tema: publicos
tarefas: [criar-campanha-de-catalogo]
fonte: fala
faixa: "00:27:01–00:28:22"
condicoes: "A janela depende do negócio e da frequência de recompra do produto."
perecivel: false
confianca: alta
versao: 1
```
Quando o produto tiver ciclo de recompra mais longo, anuncie para quem comprou nos últimos 60 dias excluindo quem comprou nos últimos 30.
O exemplo de café considera que a recompra não costuma ocorrer 7 dias depois.

### U:7cc58e06ed6a16b7:025 — Testar todos os formatos e variações de catálogo
```yaml
tipo: regra
plataforma: [meta]
tema: testes-e-experimentos
tarefas: [configurar-anuncio, rodar-testes-e-experimentos]
fonte: fala
faixa: "00:28:39–00:30:38"
perecivel: false
confianca: alta
versao: 1
```
Teste imagem ou vídeo único, carrossel e coleção, com variações de título, etiqueta e texto.
O fato de o anúncio ser dinâmico não elimina a necessidade de testar muitas variações.

### U:7cc58e06ed6a16b7:026 — Ajustar corte e preenchimento das imagens do catálogo
```yaml
tipo: procedimento
plataforma: [meta]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: "00:30:38–00:32:55"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: anúncio de imagem ou vídeo único com CP selecionado.
1. Em editar criativos, abra cortar imagens e veja a prévia dos itens do CP.
2. Ajuste o zoom se as imagens ficarem mal enquadradas.
3. Teste preenchimento de cor automática ou branco.
4. Salve versões distintas quando o resultado visual mudar.

### U:7cc58e06ed6a16b7:027 — Usar tema com imagem transparente quando fizer sentido
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: "00:32:25–00:34:40"
perecivel: true
confianca: alta
versao: 1
```
Em tema dos itens, é possível carregar uma imagem como borda ou logotipo, ajustar tamanho, posição e opacidade.
Os temas funcionam melhor com fundo transparente; o professor diz que, na maior parte das vezes, não usa elemento algum.

### U:7cc58e06ed6a16b7:028 — Testar etiqueta de informações do catálogo
```yaml
tipo: procedimento
plataforma: [meta]
tema: criativo
tarefas: [configurar-anuncio, rodar-testes-e-experimentos]
fonte: fala
faixa: "00:34:40–00:37:24"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: informações necessárias disponíveis no catálogo do site.
1. Em informações do catálogo, teste texto com sobreposição automático ou manual.
2. No manual, escolha preço, preço riscado, porcentagem de desconto ou frete grátis.
3. Ajuste opacidade, formato, fonte, cores e posição da etiqueta.
4. Compare uma versão com etiqueta de preço e outra sem etiqueta.
```
condicoes: "Frete grátis só aparece se o site tiver essa informação; preço com desconto não aparece para produto sem desconto."
```

### U:7cc58e06ed6a16b7:029 — Preferências do professor para etiqueta de catálogo
```yaml
tipo: regra
plataforma: [meta]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: "00:35:22–00:37:21"
perecivel: true
confianca: alta
versao: 1
```
O professor prefere usar etiqueta de preço em e-commerce, formato retângulo, texto branco e cor definida manualmente.
Ele cita azul, vermelho, preto ou rosa conforme a marca e não recomenda triângulo.

### U:7cc58e06ed6a16b7:030 — Inserir campos dinâmicos no texto e no título
```yaml
tipo: procedimento
plataforma: [meta]
tema: copy-e-roteiro
tarefas: [configurar-anuncio, escrever-copy-e-roteiro]
fonte: fala
faixa: "00:37:27–00:41:05"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: catálogo com nome, preço e, se desejado, descrição dos produtos.
1. Escreva o texto principal ou insira campos dinâmicos de nome, preço e descrição.
2. Faça o mesmo no título, deixando espaços adequados entre os campos.
3. Confira a prévia de mais de um produto antes de publicar.

### U:7cc58e06ed6a16b7:031 — Usar texto que se adapte a todos os produtos do CP
```yaml
tipo: regra
plataforma: [meta]
tema: copy-e-roteiro
tarefas: [configurar-anuncio, escrever-copy-e-roteiro]
fonte: fala
faixa: "00:41:41–00:43:07"
perecivel: false
confianca: alta
versao: 1
```
Quando o anúncio mostrar vários produtos, use texto dinâmico ou texto genérico que funcione para todos.
Não escreva uma copy específica de um produto se o catálogo também puder mostrar outros itens.

### U:7cc58e06ed6a16b7:032 — Escolher chamada para ação de catálogo
```yaml
tipo: regra
plataforma: [meta]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: "00:41:05–00:41:41"
perecivel: true
confianca: alta
versao: 1
```
Para a chamada para ação do anúncio de catálogo, o professor usa “Comprar agora” ou “Saiba mais”.

### U:7cc58e06ed6a16b7:033 — Configurar destino e rastreamento do anúncio
```yaml
tipo: procedimento
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [configurar-anuncio, instalar-pixel-e-eventos]
fonte: fala
faixa: "00:42:28–00:43:34"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: anúncio de catálogo pronto e pixel do site disponível.
1. Se não houver aplicativo, selecione destino Manual.
2. Se houver aplicativo, teste um anúncio para o site e outro com destino Advantage Plus.
3. No rastreamento, ative os eventos do site e selecione o pixel correto.
```
condicoes: "O professor orienta não configurar a parte de Deep Link nesta aula."
```

### U:7cc58e06ed6a16b7:034 — Finalizar com variações, conferência e publicação
```yaml
tipo: procedimento
plataforma: [meta]
tema: estrutura-de-campanha
tarefas: [criar-campanha-de-catalogo, configurar-anuncio]
fonte: fala
faixa: "00:43:07–00:43:34"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: anúncio de catálogo configurado com destino e rastreamento.
1. Crie vários anúncios e variações de criativo.
2. Duplique conjuntos de anúncios e insira as segmentações.
3. Confira as configurações e publique.

### U:7cc58e06ed6a16b7:035 — Limite da aula sobre Deep Link
```yaml
tipo: limite
plataforma: [meta]
tema: destino-e-landing-page
tarefas: []
fonte: fala
faixa: "00:43:07–00:43:34"
perecivel: false
confianca: alta
versao: 1
```
A aula não cobre a configuração de Deep Link.