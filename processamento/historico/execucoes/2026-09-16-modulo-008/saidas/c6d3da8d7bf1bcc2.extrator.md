---
type: unidades-aula
status: rascunho
title: "9.Configuração do grupo de anúncio"
modulo: "008"
ordem: 128
aula_id: c6d3da8d7bf1bcc2
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - transcricao.md
extraido_em: 2026-09-16
gerado_por: gpt-5.6-terra
retiradas: []
divisoes: []
fusoes: []
---

# 9.Configuração do grupo de anúncio

## Contexto da aula

A aula configura grupos de anúncio para uma campanha de conversão no TikTok Ads.
Ela parte da hierarquia de públicos e demonstra opções de segmentação, posicionamento e otimização.
O exemplo usa uma página de captura com os eventos View Content e Subscribe.
A criação da Instant Page e a configuração final do anúncio ficam para aulas seguintes.

## Unidades

### U:c6d3da8d7bf1bcc2:001 — Nomeie o grupo pelo público anunciado
```yaml
tipo: regra
plataforma: [tiktok]
tema: nomenclatura
tarefas: [nomear-campanhas]
fonte: fala
faixa: "00:00:00–00:00:34"
perecivel: false
confianca: alta
versao: 1
```
Defina o nome do grupo de anúncio conforme o público para o qual será feito o anúncio.

### U:c6d3da8d7bf1bcc2:002 — Tipos de público na hierarquia do TikTok
```yaml
tipo: conceito
plataforma: [tiktok]
tema: publicos
tarefas: []
fonte: fala
faixa: "00:00:00–00:02:43"
perecivel: false
confianca: alta
versao: 1
```
A hierarquia apresentada tem Custom Audiences, públicos lookalike, interesses e comportamentos, e públicos abertos por demografia.
Custom Audiences incluem tráfego do site, engajamento, interações com a Business Account e formulários de leads.

### U:c6d3da8d7bf1bcc2:003 — Priorize públicos quentes e já testados
```yaml
tipo: regra
plataforma: [tiktok]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: "00:00:35–00:01:10"
perecivel: false
confianca: alta
versao: 1
```
Trate Custom Audiences como públicos mais qualificados; públicos quentes, públicos já testados e a lista de clientes são os melhores.

### U:c6d3da8d7bf1bcc2:004 — Lookalike exige uma Custom Audience de origem
```yaml
tipo: decisao
plataforma: [tiktok]
tema: publicos
tarefas: [montar-publicos-semelhantes]
fonte: fala
faixa: "00:01:10–00:01:53"
condicoes: "ao criar um público lookalike"
perecivel: false
confianca: alta
versao: 1
```
Se criar um público lookalike, use uma Custom Audience como origem.
O TikTok apresenta as opções Narrow, Balanced e Broad.

### U:c6d3da8d7bf1bcc2:005 — Públicos de interesse e comportamento não exigem origem
```yaml
tipo: conceito
plataforma: [tiktok]
tema: publicos
tarefas: []
fonte: fala
faixa: "00:01:10–00:02:43"
perecivel: false
confianca: alta
versao: 1
```
Interesses e comportamentos podem ser criados sem Custom Audience.
As quatro categorias demonstradas são interesses, interação com vídeos, interação com creators e interação com hashtags.

### U:c6d3da8d7bf1bcc2:006 — Use exclusão entre públicos quentes
```yaml
tipo: decisao
plataforma: [tiktok]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos]
fonte: fala
faixa: "00:02:48–00:03:48"
perecivel: false
confianca: alta
versao: 1
```
Se organizar públicos quentes, faça exclusões entre eles como no Meta Ads.
Entre públicos frios, o professor diz que não é necessário fazer exclusões.

### U:c6d3da8d7bf1bcc2:007 — Use evento para identificar visitantes da página
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos, montar-publicos-personalizados]
fonte: fala
faixa: "00:03:48–00:04:22"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: o evento View Content está instalado exclusivamente na página de captura.
1. Crie o público de pessoas que ativaram View Content.
2. Use esse público para representar quem visitou a página, quando não for possível criar público pela URL.

### U:c6d3da8d7bf1bcc2:008 — Prefira Website Externo para captar lead mais qualificado
```yaml
tipo: decisao
plataforma: [tiktok]
tema: destino-e-landing-page
tarefas: [criar-campanha]
fonte: fala
faixa: "00:04:24–00:05:03"
condicoes: "ao escolher entre Instant Page e Website Externo"
perecivel: true
confianca: alta
versao: 1
```
Quando escolher onde ficará o site, selecione Website Externo em vez de Instant Page, porque o professor considera o lead mais qualificado.

### U:c6d3da8d7bf1bcc2:009 — Otimize para o evento final da conversão
```yaml
tipo: regra
plataforma: [tiktok]
tema: pixel-e-eventos
tarefas: [definir-conversoes-e-metas]
fonte: fala
faixa: "00:04:24–00:05:54"
perecivel: true
confianca: alta
versao: 1
```
Selecione o pixel e use como evento de otimização o evento final do processo de conversão.
No exemplo, o cadastro concluído dispara Subscribe e a campanha é otimizada para esse evento.

### U:c6d3da8d7bf1bcc2:010 — Atualize a tela quando o evento não aparecer
```yaml
tipo: alerta-ui
plataforma: [tiktok]
tema: pixel-e-eventos
tarefas: [definir-conversoes-e-metas]
fonte: fala
faixa: "00:05:03–00:05:54"
perecivel: true
confianca: alta
versao: 1
```
Se o evento de otimização não aparecer na interface, atualize a tela; o professor relata que isso pode ocorrer por falha temporária.

### U:c6d3da8d7bf1bcc2:011 — Configuração de conversão só vale para campanha de conversão
```yaml
tipo: decisao
plataforma: [tiktok]
tema: objetivos
tarefas: [escolher-objetivo-de-campanha]
fonte: fala
faixa: "00:05:12–00:05:54"
condicoes: "em campanha de conversão"
perecivel: true
confianca: alta
versao: 1
```
Se a campanha for de conversão, configure pixel e evento de otimização.
Nas demais campanhas, configure o nome e o posicionamento.

### U:c6d3da8d7bf1bcc2:012 — Mantenha apenas o posicionamento TikTok
```yaml
tipo: regra
plataforma: [tiktok]
tema: posicionamentos-e-formatos
tarefas: [escolher-canais-e-posicionamentos]
fonte: fala
faixa: "00:05:12–00:05:54"
perecivel: true
confianca: alta
versao: 1
```
No posicionamento, deixe selecionado somente TikTok, pois o professor afirma que o lead vem mais qualificado.

### U:c6d3da8d7bf1bcc2:013 — Desative comentários diante de muito hate
```yaml
tipo: decisao
plataforma: [tiktok]
tema: configuracao-de-conta
tarefas: [configurar-anuncio]
fonte: fala
faixa: "00:05:55–00:07:48"
condicoes: "quando houver muitos comentários ofensivos ou reclamações"
perecivel: true
confianca: alta
versao: 1
```
Se houver muito hate nos anúncios, desligue os comentários.
Se a maioria dos comentários for positiva, mantenha-os ativos.

### U:c6d3da8d7bf1bcc2:014 — Comentários podem ser alterados depois
```yaml
tipo: alerta-ui
plataforma: [tiktok]
tema: configuracao-de-conta
tarefas: [configurar-anuncio]
fonte: fala
faixa: "00:06:33–00:07:48"
perecivel: true
confianca: alta
versao: 1
```
É possível iniciar a campanha com comentários desligados e ativá-los depois, ou desligá-los posteriormente.
Nos ativos, a área de comentários permite ver os comentários recebidos no anúncio.

### U:c6d3da8d7bf1bcc2:015 — Desative download de vídeo
```yaml
tipo: regra
plataforma: [tiktok]
tema: configuracao-de-conta
tarefas: [configurar-anuncio]
fonte: fala
faixa: "00:06:33–00:07:06"
perecivel: true
confianca: alta
versao: 1
```
Desative a opção de download de vídeo para não permitir que as pessoas baixem o criativo.

### U:c6d3da8d7bf1bcc2:016 — Teste otimização automatizada de criativos separadamente
```yaml
tipo: decisao
plataforma: [tiktok]
tema: testes-e-experimentos
tarefas: [rodar-testes-e-experimentos]
fonte: fala
faixa: "00:07:07–00:08:23"
condicoes: "ao testar otimização automatizada de criativos"
perecivel: true
confianca: alta
versao: 1
```
Se testar a otimização automatizada de criativos, crie um grupo de anúncio com essa opção ativada.
Para a primeira campanha focada em performance, não ative a opção.

### U:c6d3da8d7bf1bcc2:017 — Use segmentação customizada
```yaml
tipo: regra
plataforma: [tiktok]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: "00:08:23–00:09:04"
perecivel: true
confianca: alta
versao: 1
```
Use segmentação customizada e não selecione segmentação automatizada, pois ela retira a escolha de idade.

### U:c6d3da8d7bf1bcc2:018 — Exclua idades menores na segmentação do TikTok
```yaml
tipo: regra
plataforma: [tiktok]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: "00:08:23–00:09:04"
perecivel: true
confianca: alta
versao: 1
```
Faça sempre segmentação de idade, retire as idades menores e não anuncie para todas as idades, pois o professor relata haver muitas crianças no TikTok.

### U:c6d3da8d7bf1bcc2:019 — Ignore renda fora dos Estados Unidos
```yaml
tipo: decisao
plataforma: [tiktok]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: "00:08:23–00:09:04"
condicoes: "fora dos Estados Unidos"
perecivel: true
confianca: alta
versao: 1
```
Se a campanha não for nos Estados Unidos, ignore a segmentação de renda.

### U:c6d3da8d7bf1bcc2:020 — Exclua Subscribe do público de View Content
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: publicos
tarefas: [montar-publicos-personalizados, organizar-hierarquia-e-exclusao-de-publicos]
fonte: fala
faixa: "00:09:48–00:11:13"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: View Content identifica somente visitas à página de captura e Subscribe identifica o cadastro.
1. Inclua quem ativou View Content nos últimos 180 dias.
2. Exclua quem ativou Subscribe nos últimos 180 dias.
3. Nomeie o grupo conforme o público que caiu na página de captura.

### U:c6d3da8d7bf1bcc2:021 — Interesse de compra reduz escala e aumenta qualificação
```yaml
tipo: exemplo
plataforma: [tiktok]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: "00:11:13–00:14:39"
perecivel: true
confianca: alta
versao: 1
```
Situação: segmentação brasileira para pessoas acima de 25 anos interessadas em marketing e advertising.
O que aconteceu: o interesse de compra ficou entre 600 mil e 800 mil pessoas; o interesse geral chegou a 22 milhões.
Lógica: purchase intention é apresentado como público mais qualificado e com menos escala; interesse geral tem menos qualificação e mais escala.

### U:c6d3da8d7bf1bcc2:022 — Identifique no nome o tipo de interesse selecionado
```yaml
tipo: regra
plataforma: [tiktok]
tema: nomenclatura
tarefas: [nomear-campanhas]
fonte: fala
faixa: "00:13:09–00:13:50"
perecivel: true
confianca: alta
versao: 1
```
Registre no nome do grupo se foi selecionado purchase intention ou interesse geral, pois são públicos diferentes.

### U:c6d3da8d7bf1bcc2:023 — Pesquise interesses com tentativas e espera
```yaml
tipo: alerta-ui
plataforma: [tiktok]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: "00:11:55–00:14:39"
perecivel: true
confianca: alta
versao: 1
```
A busca de interesses pode não encontrar o termo de primeira; digite, espere um pouco e procure interesses adicionais que apareçam fora da lista.

### U:c6d3da8d7bf1bcc2:024 — Escolha a janela e a ação em interação de vídeo
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: "00:14:39–00:16:43"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: um assunto de vídeo foi selecionado na opção Video Interaction.
1. Escolha a ação: assistir até o fim, curtir, comentar ou compartilhar.
2. Selecione a janela disponível, como 7 ou 15 dias.
3. Misture ações se quiser formar públicos maiores.

### U:c6d3da8d7bf1bcc2:025 — Mais segmentações são combinadas como “ou”
```yaml
tipo: conceito
plataforma: [tiktok]
tema: publicos
tarefas: []
fonte: fala
faixa: "00:21:23–00:23:16"
perecivel: true
confianca: alta
versao: 1
```
Ao adicionar interesses, interações com creators ou hashtags, a pessoa pode cumprir uma opção ou outra.
Adicionar opções amplia o público, em vez de torná-lo mais específico.

### U:c6d3da8d7bf1bcc2:026 — Comece testando interesses
```yaml
tipo: decisao
plataforma: [tiktok]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses, rodar-testes-e-experimentos]
fonte: fala
faixa: "00:22:34–00:23:51"
perecivel: true
confianca: alta
versao: 1
```
Quando começar a testar segmentações por interesse e comportamento, comece pelos interesses.
O professor diz que, para ele, essa é a opção que mais funciona, mas orienta testar.

### U:c6d3da8d7bf1bcc2:027 — Remova segmentação incompleta pelo ícone de lixeira
```yaml
tipo: alerta-ui
plataforma: [tiktok]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: "00:17:41–00:18:23"
perecivel: true
confianca: alta
versao: 1
```
Se começar uma segmentação e desistir dela, remova-a pelo ícone de lixeira para não anunciar para esse público.
Confira ao lado se a estimativa de público está sendo preenchida.

### U:c6d3da8d7bf1bcc2:028 — Não use targeting expansion no exemplo de público quente
```yaml
tipo: regra
plataforma: [tiktok]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: "00:23:58–00:24:33"
perecivel: true
confianca: alta
versao: 1
```
Não selecione targeting expansion ao anunciar para o público de View Content; o professor afirma que o público ficaria muito ruim.

### U:c6d3da8d7bf1bcc2:029 — Orçamento do grupo só é definido se não estiver na campanha
```yaml
tipo: decisao
plataforma: [tiktok]
tema: orcamento
tarefas: [definir-orcamento]
fonte: fala
faixa: "00:23:58–00:24:33"
perecivel: true
confianca: alta
versao: 1
```
Se o orçamento não tiver sido definido na campanha, defina no grupo quanto ele gastará por dia.
No exemplo, o orçamento já está selecionado na campanha.

### U:c6d3da8d7bf1bcc2:030 — Programe horário de exibição ou mantenha All day
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: posicionamentos-e-formatos
tarefas: [configurar-anuncio]
fonte: fala
faixa: "00:24:33–00:25:13"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: o grupo de anúncio está com público e orçamento configurados.
1. Escolha dias e horário de veiculação, se o anúncio precisar aparecer apenas em uma janela.
2. Confira o resumo exibido pela interface.
3. Se quiser veicular todos os dias, selecione All day.

### U:c6d3da8d7bf1bcc2:031 — Mantenha Bid e otimização no padrão
```yaml
tipo: regra
plataforma: [tiktok]
tema: leilao-e-lances
tarefas: [escolher-estrategia-de-lance]
fonte: fala
faixa: "00:24:33–00:25:13"
perecivel: true
confianca: alta
versao: 1
```
Na parte de Bid e otimização, mantenha a configuração padrão e avance para a configuração do anúncio.

### U:c6d3da8d7bf1bcc2:032 — A configuração do anúncio fica para a próxima aula
```yaml
tipo: limite
plataforma: [tiktok]
tema: criativo
tarefas: []
fonte: fala
faixa: "00:25:13–00:25:19"
perecivel: false
confianca: alta
versao: 1
```
A aula encerra após a configuração do grupo de anúncio; a configuração do anúncio será tratada na próxima aula.