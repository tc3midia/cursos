---
type: unidades-aula
status: validado
title: "4.0 - Estruturas de campanha"
modulo: "002"
ordem: 24
aula_id: 522c2971f640b57f
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - transcricao.md
extraido_em: 2026-09-14
gerado_por: gpt-5.6-terra
retiradas: []
divisoes: []
fusoes: []
---

# 4.0 - Estruturas de campanha

## Contexto da aula

A aula apresenta a hierarquia de campanhas no Meta Ads e compara a nomenclatura com outras fontes de tráfego.
Explica quais definições ficam em campanha, conjunto de anúncios e anúncio.
Mostra que as definições disponíveis formam possibilidades de teste, sem propor configuração secreta.
As escolhas detalhadas de objetivo, públicos, testes e tipos de campanha ficam para aulas posteriores.

## Unidades

### U:522c2971f640b57f:001 — Hierarquia básica do Meta Ads
```yaml
tipo: conceito
plataforma: [meta]
tema: estrutura-de-campanha
tarefas: []
fonte: fala
faixa: "00:00:00–00:01:17"
perecivel: false
confianca: alta
versao: 1
```
No Meta Ads, a estrutura básica é campanha, conjunto de anúncios e anúncio.
Uma campanha contém conjuntos de anúncios, e cada conjunto contém anúncios.
No Google Ads, o equivalente ao conjunto de anúncios é chamado grupo de anúncios.

### U:522c2971f640b57f:002 — Identificar a hierarquia de uma nova fonte de tráfego
```yaml
tipo: procedimento
plataforma: [geral]
tema: estrutura-de-campanha
tarefas: [definir-estrutura-de-campanha]
fonte: fala
faixa: "00:06:52–00:08:07"
perecivel: false
confianca: alta
versao: 1
```
Pré-condição: entrada em uma fonte de tráfego ainda desconhecida.
1. Identifique quais estruturas a ferramenta possui e os nomes que ela usa.
2. Entenda o que é definido em cada nível da estrutura.
O LinkedIn Ads, por exemplo, usa grupos de campanhas, campanhas e anúncios.

### U:522c2971f640b57f:003 — Mais conjuntos não aumentam automaticamente o orçamento
```yaml
tipo: regra
plataforma: [meta]
tema: orcamento
tarefas: [definir-orcamento, definir-estrutura-de-campanha]
fonte: fala
faixa: "00:01:54–00:03:12"
perecivel: false
confianca: alta
versao: 1
```
Adicionar conjuntos de anúncios não faz, por si só, a campanha gastar mais.
Uma campanha com R$50,00 por dia pode ter de 4 a 8 conjuntos e continuar com o mesmo orçamento diário.

### U:522c2971f640b57f:004 — Verba mínima por conjunto de anúncios
```yaml
tipo: regua
plataforma: [meta]
tema: orcamento
tarefas: [definir-orcamento, definir-estrutura-de-campanha]
fonte: fala
faixa: "00:02:33–00:03:57"
condicoes: "cada conjunto de anúncios precisa receber pelo menos US$ 1, arredondado na aula para R$ 6 por dia"
perecivel: false
confianca: alta
versao: 1
```
Considere pelo menos US$ 1, aproximadamente R$ 6, por dia para cada conjunto de anúncios.
Com R$50,00 diários, 9 conjuntos receberiam R$5,55 cada; com R$60,00 diários, o nono conjunto passa a caber.

### U:522c2971f640b57f:005 — Escolher entre orçamento na campanha ou no conjunto
```yaml
tipo: conceito
plataforma: [meta]
tema: orcamento
tarefas: [definir-orcamento]
fonte: fala
faixa: "00:03:57–00:04:28"
perecivel: false
confianca: alta
versao: 1
```
O orçamento pode ficar na campanha, que distribui a verba entre os conjuntos, ou ser definido em cada conjunto.
Com seis conjuntos, por exemplo, é possível estabelecer R$10 por dia em cada um.

### U:522c2971f640b57f:006 — Anúncios não exigem aumento de verba
```yaml
tipo: regra
plataforma: [meta]
tema: estrutura-de-campanha
tarefas: [definir-estrutura-de-campanha]
fonte: fala
faixa: "00:04:28–00:05:25"
perecivel: false
confianca: alta
versao: 1
```
Colocar mais anúncios dentro de um conjunto não obriga a aumentar o orçamento.
Existe limite de anúncios, mas o professor afirma que normalmente ele não é atingido.

### U:522c2971f640b57f:007 — Meta distribui a verba entre oportunidades
```yaml
tipo: conceito
plataforma: [meta]
tema: orcamento
tarefas: [definir-orcamento]
fonte: fala
faixa: "00:05:25–00:06:13"
perecivel: false
confianca: alta
versao: 1
```
Quando a verba fica na campanha, o Meta pode concentrá-la em alguns conjuntos e anúncios e não gastar em outros.
O professor chama de oportunidades os lugares em que a plataforma busca obter o máximo de resultado.

### U:522c2971f640b57f:008 — Alternar liberdade e controle sobre a distribuição
```yaml
tipo: conceito
plataforma: [meta]
tema: orcamento
tarefas: [definir-orcamento]
fonte: fala
faixa: "00:06:13–00:06:52"
perecivel: false
confianca: alta
versao: 1
```
O professor diz que o gestor pode, em alguns casos, saber o que é melhor do que a plataforma.
A gestão funciona como uma gangorra entre dar liberdade ao Meta e tomar controle da distribuição.

### U:522c2971f640b57f:009 — Objetivo é definido na criação da campanha
```yaml
tipo: regra
plataforma: [meta, google, tiktok]
tema: objetivos
tarefas: [escolher-objetivo-de-campanha]
fonte: fala
faixa: "00:08:07–00:08:51"
perecivel: false
confianca: alta
versao: 1
```
Ao criar uma campanha, defina o objetivo.
O professor afirma que Meta Ads, Google Ads e TikTok Ads pedem essa definição na campanha.

### U:522c2971f640b57f:010 — Tipo de compra não é abordado nesta visão macro
```yaml
tipo: limite
plataforma: [meta]
tema: estrutura-de-campanha
tarefas: []
fonte: fala
faixa: "00:08:51–00:10:02"
perecivel: false
confianca: alta
versao: 1
```
A aula não entra no tipo de compra nem em especificidades de campanhas de conversão.
A explicação se concentra nos elementos mais importantes da estrutura.

### U:522c2971f640b57f:011 — Especificidades das campanhas ficam para aulas próprias
```yaml
tipo: limite
plataforma: [meta]
tema: objetivos
tarefas: []
fonte: fala
faixa: "00:10:02–00:10:44"
perecivel: false
confianca: alta
versao: 1
```
A aula não detalha as especificidades das campanhas de venda, envolvimento, mensagem, catálogo, alcance e lead.
Esses tipos de campanha terão aulas próprias.

### U:522c2971f640b57f:012 — Catálogo conecta produtos do e-commerce ao Meta
```yaml
tipo: conceito
plataforma: [meta]
tema: estrutura-de-campanha
tarefas: [criar-campanha-de-catalogo]
fonte: fala
faixa: "00:10:44–00:11:59"
perecivel: false
confianca: alta
versao: 1
```
Para e-commerce, o catálogo conecta a loja online ao Meta.
A plataforma passa a acessar produtos, tamanhos, cores, valores, detalhes e fotos para usar em anúncios.

### U:522c2971f640b57f:013 — Definições da campanha no Meta Ads
```yaml
tipo: conceito
plataforma: [meta]
tema: estrutura-de-campanha
tarefas: [criar-campanha, escolher-objetivo-de-campanha, definir-orcamento]
fonte: fala
faixa: "00:11:22–00:14:26"
perecivel: false
confianca: alta
versao: 1
```
Na campanha, defina objetivo, uso de catálogo, teste A/B e onde ficará o orçamento.
Defina também orçamento diário ou total, estratégia de lance, programação e nome da campanha.

### U:522c2971f640b57f:014 — Programação define quando o anúncio é veiculado
```yaml
tipo: conceito
plataforma: [meta]
tema: estrutura-de-campanha
tarefas: [criar-campanha]
fonte: fala
faixa: "00:13:11–00:14:26"
perecivel: false
confianca: alta
versao: 1
```
A programação define se o anúncio aparece todos os dias ou somente em horários determinados.
O professor exemplifica veiculação apenas do meio-dia às duas da tarde.

### U:522c2971f640b57f:015 — Nomear campanha e conjunto de anúncios
```yaml
tipo: regra
plataforma: [meta]
tema: nomenclatura
tarefas: [nomear-campanhas]
fonte: fala
faixa: "00:13:50–00:14:28"
perecivel: false
confianca: alta
versao: 1
```
Defina um bom nome para a campanha e para o conjunto de anúncios.
O professor trata essa definição como tão importante quanto as demais do nível correspondente.

### U:522c2971f640b57f:016 — Navegar entre níveis pelo topo do editor
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: estrutura-de-campanha
tarefas: [criar-campanha]
fonte: fala
faixa: "00:14:28–00:15:37"
perecivel: true
confianca: alta
versao: 1
```
No editor, clique no nível exibido na parte superior para ir de campanha a conjunto de anúncios.
Também é possível usar “avançar”, mas o professor prefere se guiar pela parte superior para saber onde está.

### U:522c2971f640b57f:017 — Conjunto de anúncios concentra mais definições
```yaml
tipo: conceito
plataforma: [meta]
tema: estrutura-de-campanha
tarefas: [definir-estrutura-de-campanha]
fonte: fala
faixa: "00:15:02–00:16:12"
perecivel: true
confianca: alta
versao: 1
```
O conjunto de anúncios é apresentado como a estrutura mais robusta, com mais definições que a campanha.
Na interface demonstrada, ele é organizado em caixas como conversão, criativo dinâmico, orçamento, público e posicionamento.

### U:522c2971f640b57f:018 — Definições da caixa de conversão
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [definir-conversoes-e-metas]
fonte: fala
faixa: "00:16:12–00:16:49"
perecivel: true
confianca: alta
versao: 1
```
Na caixa “conversão”, defina localização da conversão, meta de desempenho, pixel e evento de conversão.
A aula menciona que esses elementos serão aprofundados na criação.

### U:522c2971f640b57f:019 — Criativo dinâmico é ativado ou desativado no conjunto
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: "00:16:49–00:17:30"
perecivel: true
confianca: alta
versao: 1
```
Na caixa de criativo dinâmico, escolha entre ativar ou desativar o recurso.

### U:522c2971f640b57f:020 — CBO e ABO indicam onde está o orçamento
```yaml
tipo: conceito
plataforma: [meta]
tema: orcamento
tarefas: [definir-orcamento]
fonte: fala
faixa: "00:17:30–00:18:48"
perecivel: false
confianca: alta
versao: 1
```
CBO, ou Campaign Budget Optimization, é orçamento definido na campanha.
ABO, ou Adset Budget Optimization, é orçamento definido no grupo ou conjunto de anúncios.
O professor observa que CBO foi descontinuado como nome, mas continua sendo usado pelas pessoas.

### U:522c2971f640b57f:021 — Programação e período podem ser definidos no conjunto
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: orcamento
tarefas: [definir-orcamento]
fonte: fala
faixa: "00:18:16–00:19:27"
perecivel: true
confianca: alta
versao: 1
```
No conjunto de anúncios, defina horários, dias, início e término da campanha.
O orçamento só é definido nesse nível quando não foi colocado na campanha.

### U:522c2971f640b57f:022 — Definições de público no conjunto de anúncios
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses, montar-publicos-personalizados]
fonte: fala
faixa: "00:19:27–00:20:03"
perecivel: true
confianca: alta
versao: 1
```
No conjunto, escolha público salvo ou novo, público personalizado, localização, idade, gênero, interesses e idioma.
O idioma corresponde ao idioma do Facebook das pessoas alcançadas.

### U:522c2971f640b57f:023 — Segmentações podem ficar sem definição
```yaml
tipo: decisao
plataforma: [meta]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses, montar-publicos-personalizados]
fonte: fala
faixa: "00:19:27–00:20:41"
perecivel: false
confianca: alta
versao: 1
```
Se não definir localização, idade, gênero, interesses ou idioma, o anúncio alcança todas as opções correspondentes.
Também é possível não selecionar público personalizado.

### U:522c2971f640b57f:024 — Escolher posicionamento manual ou automático
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: posicionamentos-e-formatos
tarefas: [escolher-canais-e-posicionamentos]
fonte: fala
faixa: "00:20:04–00:20:41"
perecivel: true
confianca: alta
versao: 1
```
No conjunto de anúncios, defina se o posicionamento será manual ou automático.

### U:522c2971f640b57f:025 — Página e perfil comercial identificam o anunciante
```yaml
tipo: conceito
plataforma: [meta]
tema: estrutura-de-campanha
tarefas: [configurar-anuncio]
fonte: fala
faixa: "00:20:41–00:21:23"
perecivel: false
confianca: alta
versao: 1
```
No anúncio, defina a página ou o perfil comercial do Instagram que anunciará.
Também é possível anunciar em parceria entre duas páginas ou anunciar sozinho.

### U:522c2971f640b57f:026 — Criar anúncio novo ou usar publicação existente
```yaml
tipo: decisao
plataforma: [meta]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: "00:20:41–00:21:23"
perecivel: false
confianca: alta
versao: 1
```
Se quiser criar do zero, monte um anúncio novo.
Quando houver publicação no feed do Instagram ou Facebook, ela também pode ser usada como anúncio.

### U:522c2971f640b57f:027 — Anúncio manual e anúncio via catálogo
```yaml
tipo: decisao
plataforma: [meta]
tema: criativo
tarefas: [configurar-anuncio, criar-campanha-de-catalogo]
fonte: fala
faixa: "00:21:23–00:22:02"
perecivel: false
confianca: alta
versao: 1
```
Se o anúncio for manual, escolha imagem, vídeo e texto.
Quando usar catálogo em e-commerce, o Meta puxa do site as informações do anúncio.

### U:522c2971f640b57f:028 — Formato e mídia são definições separadas
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: posicionamentos-e-formatos
tarefas: [configurar-anuncio]
fonte: fala
faixa: "00:21:23–00:22:36"
perecivel: true
confianca: alta
versao: 1
```
No anúncio manual, escolha o formato: imagem, vídeo, carrossel ou coleção.
Depois de escolher o formato, envie a mídia correspondente, como imagens ou vídeos.

### U:522c2971f640b57f:029 — Recomendação para anúncios de vários anunciantes
```yaml
tipo: regra
plataforma: [meta]
tema: posicionamentos-e-formatos
tarefas: [configurar-anuncio]
fonte: fala
faixa: "00:21:23–00:22:36"
perecivel: true
confianca: media
versao: 1
nota: "O professor desconfia que a opção será descontinuada e recomenda deixá-la ativada se ela aparecer."
```
Mantenha ativada a opção de anúncio de vários anunciantes quando ela estiver disponível.
Se a opção não aparecer, o professor orienta apenas seguir adiante.

### U:522c2971f640b57f:030 — Campos de texto do anúncio
```yaml
tipo: conceito
plataforma: [meta]
tema: copy-e-roteiro
tarefas: [escrever-copy-e-roteiro, configurar-anuncio]
fonte: fala
faixa: "00:22:37–00:23:22"
perecivel: false
confianca: alta
versao: 1
```
O anúncio tem texto principal, título e descrição.
A descrição fica abaixo do título, pode ter uma ou duas frases e é apresentada como opcional.

### U:522c2971f640b57f:031 — Definições finais do anúncio
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: destino-e-landing-page
tarefas: [configurar-anuncio]
fonte: fala
faixa: "00:23:23–00:24:42"
perecivel: true
confianca: alta
versao: 1
```
No anúncio, escolha otimização de texto por pessoa, call to action, destino, rastreamento e parâmetros de URL.
O destino pode ser site, WhatsApp, experiência instantânea ou formulário de cadastro do Meta.

### U:522c2971f640b57f:032 — Não decorar toda a lista de configurações
```yaml
tipo: regra
plataforma: [meta]
tema: fundamentos-e-carreira
tarefas: [criar-campanha]
fonte: fala
faixa: "00:24:04–00:25:29"
perecivel: false
confianca: alta
versao: 1
```
Não é necessário decorar todas as definições de uma campanha.
É necessário saber escolher cada definição da melhor maneira possível ao usar o Meta Ads.

### U:522c2971f640b57f:033 — Não existe configuração secreta
```yaml
tipo: regra
plataforma: [meta]
tema: estrutura-de-campanha
tarefas: [criar-campanha]
fonte: fala
faixa: "00:24:43–00:26:24"
perecivel: false
confianca: alta
versao: 1
```
Não trate objetivo, orçamento, lances, público ou outra configuração como fórmula secreta que faz a campanha funcionar.
Entenda cada opção e saiba quando selecioná-la.

### U:522c2971f640b57f:034 — Cada definição é uma possibilidade de teste
```yaml
tipo: conceito
plataforma: [meta]
tema: testes-e-experimentos
tarefas: [rodar-testes-e-experimentos]
fonte: fala
faixa: "00:26:00–00:27:42"
perecivel: false
confianca: alta
versao: 1
```
Cada escolha disponível na estrutura da campanha é uma possibilidade de teste.
O professor cita testes de objetivo, orçamento, lance, conversão, eventos, públicos, posicionamentos, formatos, mídia, textos, call to action e destino.

### U:522c2971f640b57f:035 — Combinar variáveis amplia os testes
```yaml
tipo: conceito
plataforma: [meta]
tema: testes-e-experimentos
tarefas: [rodar-testes-e-experimentos]
fonte: fala
faixa: "00:27:42–00:28:24"
perecivel: false
confianca: alta
versao: 1
```
Os testes não precisam ser isolados.
É possível combinar, por exemplo, títulos, formatos e públicos personalizados, gerando combinações infinitas.

### U:522c2971f640b57f:036 — Começar por estruturas já validadas
```yaml
tipo: decisao
plataforma: [meta]
tema: testes-e-experimentos
tarefas: [definir-estrutura-de-campanha, rodar-testes-e-experimentos]
fonte: fala
faixa: "00:28:24–00:29:55"
perecivel: false
confianca: alta
versao: 1
```
Quando estiver começando, siga as estruturas ensinadas no curso antes de inovar.
Essas estruturas não são imutáveis; depois, teste e aprenda sobre elas.

### U:522c2971f640b57f:037 — A aula não segue a ordem da tela
```yaml
tipo: limite
plataforma: [meta]
tema: estrutura-de-campanha
tarefas: []
fonte: fala
faixa: "00:30:30–00:31:42"
perecivel: false
confianca: alta
versao: 1
```
As próximas aulas abordarão os elementos da estrutura, mas não na mesma ordem exibida na interface.
O professor diz que objetivos, público, posicionamento, anúncio e conversão serão tratados ao longo do curso.

### U:522c2971f640b57f:038 — Conferir e publicar depois de montar as escolhas
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: estrutura-de-campanha
tarefas: [criar-campanha]
fonte: fala
faixa: "00:31:06–00:32:00"
perecivel: true
confianca: alta
versao: 1
```
Depois de estudar as peças, abra o gerenciador, clique em criar e faça as definições adequadas.
Ao final, use o botão de conferir e publicar mostrado na parte superior da interface.