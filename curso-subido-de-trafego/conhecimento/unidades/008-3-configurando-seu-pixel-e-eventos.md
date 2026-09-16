---
type: unidades-aula
status: validado
title: "3.Configurando seu pixel e eventos"
modulo: "008"
ordem: 122
aula_id: dac89e63e3935202
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

# 3.Configurando seu pixel e eventos

## Contexto da aula

A aula demonstra a criação e a configuração de pixel e eventos de web no TikTok Ads.
Ela compara a criação do pixel na Business Center e na Advertiser Account, e prioriza a instalação via Google Tag Manager.
Também mostra eventos por URL e por elemento da página, edição de regras e verificação com TikTok Pixel Helper.
O rastreamento de aplicativos e a API de conversões ficam fora do escopo prático desta aula.

## Unidades

### U:dac89e63e3935202:001 — Pixel pode ser criado em dois lugares no TikTok
```yaml
tipo: conceito
plataforma: [tiktok]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: "00:00:00–00:01:08"
perecivel: true
confianca: alta
versao: 1
```
O pixel pode ser criado na Business Center ou dentro da Advertiser Account.
Também é possível criá-lo na Business Center e compartilhá-lo com uma Advertiser Account; o professor diz que, no fim, o resultado é o mesmo.

### U:dac89e63e3935202:002 — Caminho para abrir a conta de anúncio no Business Center
```yaml
tipo: alerta-ui
plataforma: [tiktok]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:01:08–00:01:23"
perecivel: true
confianca: alta
versao: 1
```
Na Business Center, entre em Advertiser Account, selecione a conta de anúncio e use a opção para abrir essa conta no TikTok.

### U:dac89e63e3935202:003 — Eventos ficam nos ativos da conta de anúncio
```yaml
tipo: alerta-ui
plataforma: [tiktok]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: "00:01:25–00:02:43"
perecivel: true
confianca: alta
versao: 1
```
Na conta de anúncio, abra Assets, identificado pelo professor como ativos, e entre em Events.
Para criar um pixel de web em uma conta sem pixel, use Setup Web Events.

### U:dac89e63e3935202:004 — Rastreamento de aplicativos não é foco da aula
```yaml
tipo: limite
plataforma: [tiktok]
tema: pixel-e-eventos
tarefas: []
fonte: fala
faixa: "00:01:59–00:02:24"
perecivel: true
confianca: alta
versao: 1
```
A aula não ensina a configurar eventos de aplicativo.
Se houver aplicativo, o professor orienta contratar um desenvolvedor e entregar a ele as instruções de instalação.

### U:dac89e63e3935202:005 — Nomeie o pixel e escolha TikTok Pixel
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: "00:02:46–00:03:20"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: estar em Setup Web Events para criar um pixel.
1. Informe o nome que quiser para o pixel.
2. Entre na opção TikTok Pixel.
3. Avance para escolher o método de instalação.

### U:dac89e63e3935202:006 — API de conversões ainda não é ensinada
```yaml
tipo: limite
plataforma: [tiktok]
tema: pixel-e-eventos
tarefas: []
fonte: fala
faixa: "00:02:46–00:03:20"
perecivel: true
confianca: alta
versao: 1
```
A instalação pela API é descrita como ainda precária no TikTok e não é ensinada nesta aula.
O professor afirma que fará outra aula quando esse recurso estiver desenvolvido e em uso por ele.

### U:dac89e63e3935202:007 — Prefira instalar o pixel via Google Tag Manager
```yaml
tipo: regra
plataforma: [tiktok]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: "00:03:20–00:03:58"
perecivel: true
confianca: alta
versao: 1
```
Faça a instalação do TikTok Pixel via Google Tag Manager, entre as opções de instalação manual e plataformas parceiras.
A tela também lista plataformas parceiras como Shopify e Google Tag Manager.

### U:dac89e63e3935202:008 — Conecte o Google Tag Manager e deixe o TikTok publicar alterações
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: "00:03:58–00:05:25"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: ter acesso à conta, ao container e ao workspace corretos do Google Tag Manager.
1. Clique em Connect e faça login na conta do Google Tag Manager.
2. Selecione a conta, o container e o workspace exibidos.
3. Autorize a publicação do container e deixe o TikTok fazer as alterações automaticamente.
4. Ative automatic advanced matching e mantenha as duas opções mostradas selecionadas.
5. Avance para criar os eventos.

### U:dac89e63e3935202:009 — Evento é uma ação realizada no site
```yaml
tipo: conceito
plataforma: [tiktok]
tema: pixel-e-eventos
tarefas: [definir-conversoes-e-metas]
fonte: fala
faixa: "00:05:25–00:06:08"
perecivel: false
confianca: alta
versao: 1
```
Evento é qualquer ação da pessoa no site, como clicar em botão, entrar em página, enviar formulário ou pesquisar.
O TikTok permite rastrear essas ações por palavras da URL ou por interação com elementos da página.

### U:dac89e63e3935202:010 — Configure conversões por texto contido na URL
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: pixel-e-eventos
tarefas: [definir-conversoes-e-metas]
fonte: fala
faixa: "00:05:25–00:07:28"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: o pixel estar instalado nas páginas que devem ser rastreadas.
1. Escolha adicionar evento via URL keywords.
2. Selecione o tipo de evento.
3. Defina o texto da URL que identifica a página.
4. Salve a regra para disparar a conversão quando a URL contiver esse texto.

### U:dac89e63e3935202:011 — Página de confirmação pode acionar Subscribe
```yaml
tipo: exemplo
plataforma: [tiktok]
tema: pixel-e-eventos
tarefas: [definir-conversoes-e-metas]
fonte: fala
faixa: "00:06:08–00:07:28"
perecivel: true
confianca: alta
versao: 1
```
Situação: uma pessoa se cadastra em uma página de captura e chega a uma URL de confirmação.
O que aconteceu: o professor escolhe Subscribe e cria uma regra para a URL que contém `pedrosobral.com.br/aulas/confirmado`.
Lógica: a URL exclusiva da página posterior ao cadastro identifica a conversão de inscrição.

### U:dac89e63e3935202:012 — Uma conversão pode ter mais de uma URL
```yaml
tipo: regra
plataforma: [tiktok]
tema: pixel-e-eventos
tarefas: [definir-conversoes-e-metas]
fonte: fala
faixa: "00:07:28–00:09:31"
perecivel: true
confianca: alta
versao: 1
```
Adicione mais de uma regra de URL ao mesmo evento quando páginas diferentes representam a mesma conversão.
O professor exemplifica páginas de confirmação de aulas e de e-book sendo marcadas como Subscribe.

### U:dac89e63e3935202:013 — Páginas de captura podem ser View Content
```yaml
tipo: exemplo
plataforma: [tiktok]
tema: pixel-e-eventos
tarefas: [definir-conversoes-e-metas]
fonte: fala
faixa: "00:08:55–00:10:13"
perecivel: true
confianca: alta
versao: 1
```
Situação: páginas de captura e de e-book devem ser consideradas visualização de conteúdo.
O que aconteceu: o professor associa as URLs dessas páginas ao evento View Content.
Lógica: cada acesso a uma URL definida passa a ser tratado como visualização de conteúdo.

### U:dac89e63e3935202:014 — Evento por elemento rastreia interação específica
```yaml
tipo: conceito
plataforma: [tiktok]
tema: pixel-e-eventos
tarefas: [definir-conversoes-e-metas]
fonte: fala
faixa: "00:10:13–00:11:06"
perecivel: true
confianca: alta
versao: 1
```
Web elements permite configurar conversão conforme a interação da pessoa com um elemento do site.
Um botão pode disparar Click Button, e vários elementos podem ser incluídos no mesmo rastreamento.

### U:dac89e63e3935202:015 — Clique no botão não equivale necessariamente a inscrição
```yaml
tipo: decisao
plataforma: [tiktok]
tema: pixel-e-eventos
tarefas: [definir-conversoes-e-metas]
fonte: fala
faixa: "00:11:06–00:12:26"
perecivel: true
confianca: alta
versao: 2
nota: Correção mecânica da marcação de interface perecível apontada pelo validador; corpo e referência da fonte preservados.
```
Se o botão pode ser clicado sem concluir um cadastro, configure-o como Click Button, não como inscrição.
O professor exemplifica que repetir o clique ativa o evento de botão sem registrar uma inscrição na página.

### U:dac89e63e3935202:016 — URL keywords é o método mais usado para conversões
```yaml
tipo: regra
plataforma: [tiktok]
tema: pixel-e-eventos
tarefas: [definir-conversoes-e-metas]
fonte: fala
faixa: "00:11:49–00:13:06"
perecivel: true
confianca: alta
versao: 1
```
Use principalmente URL keywords para configurar conversões, associando o texto da URL acessada ao evento desejado.
O professor considera o rastreamento de elementos menos útil para trabalho com conversões.

### U:dac89e63e3935202:017 — Finalize a configuração dos eventos pelo Complete Setup
```yaml
tipo: alerta-ui
plataforma: [tiktok]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: "00:12:26–00:13:06"
perecivel: true
confianca: alta
versao: 1
```
Após configurar os eventos, use Complete Setup para concluir a instalação pelo Google Tag Manager.
O professor não conclui o exemplo na tela porque não quer instalar as conversões demonstradas.

### U:dac89e63e3935202:018 — Plataformas podem solicitar somente o ID do pixel
```yaml
tipo: conceito
plataforma: [tiktok]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: "00:13:06–00:13:41"
perecivel: true
confianca: alta
versao: 1
```
Na instalação em plataformas como Shopify ou Hotmart, o professor diz que, na maioria das vezes, basta copiar e colar o ID do pixel solicitado pela plataforma.

### U:dac89e63e3935202:019 — Eventos podem ser criados automaticamente pela Hotmart
```yaml
tipo: exemplo
plataforma: [tiktok]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: "00:13:41–00:14:24"
perecivel: true
confianca: alta
versao: 1
```
Situação: o pixel foi instalado dentro da Hotmart.
O que aconteceu: Initiate Checkout e Complete Payment aparecem como eventos criados automaticamente, enquanto Subscribe, Submit Form, Click Button e View Content foram criados pelo professor.
Lógica: a plataforma pode criar eventos relacionados ao seu próprio fluxo após receber a instalação do pixel.

### U:dac89e63e3935202:020 — Código base do pixel fica nas configurações do pixel
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: "00:14:24–00:15:38"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: estar na página do pixel criado.
1. Clique no nome do pixel e abra Configurações.
2. Mantenha ativadas as opções mostradas pelo professor.
3. Use View Base Code para obter o código base.
4. Cole o código no head do site quando fizer a instalação manualmente.

### U:dac89e63e3935202:021 — Access token da API está nas configurações do pixel
```yaml
tipo: alerta-ui
plataforma: [tiktok]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: "00:14:24–00:15:38"
perecivel: true
confianca: alta
versao: 1
```
As configurações do pixel também exibem a área para gerar o access token da API de conversões.
O professor informa onde encontrá-lo, mas não ensina a usar a API nesta aula.

### U:dac89e63e3935202:022 — Não use Custom Code para criar eventos
```yaml
tipo: regra
plataforma: [tiktok]
tema: pixel-e-eventos
tarefas: [definir-conversoes-e-metas]
fonte: fala
faixa: "00:15:38–00:17:16"
perecivel: true
confianca: alta
versao: 1
```
Não clique em Custom Code para configurar eventos; o professor diz que essa opção exige programador.
Use Event Builder, apresentado como a maneira mais simples para o gestor de tráfego.

### U:dac89e63e3935202:023 — Edite URL de evento existente sem repetir o tipo
```yaml
tipo: decisao
plataforma: [tiktok]
tema: pixel-e-eventos
tarefas: [definir-conversoes-e-metas]
fonte: fala
faixa: "00:17:16–00:18:38"
perecivel: true
confianca: alta
versao: 1
```
Se quiser considerar outra página como Subscribe, abra o evento Subscribe existente e adicione uma nova regra de URL.
Não crie outro Subscribe, pois a tela não permite repetir um tipo de evento já adicionado.

### U:dac89e63e3935202:024 — Salve os eventos após editar as regras
```yaml
tipo: alerta-ui
plataforma: [tiktok]
tema: pixel-e-eventos
tarefas: [definir-conversoes-e-metas]
fonte: fala
faixa: "00:17:16–00:18:38"
perecivel: true
confianca: alta
versao: 1
```
Depois de incluir ou editar as regras no Event Builder, use Save para deixar os eventos configurados.

### U:dac89e63e3935202:025 — Verifique instalação com TikTok Pixel Helper
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: "00:18:38–00:20:53"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: adicionar o TikTok Pixel Helper ao navegador.
1. Abra a página que deve conter o pixel.
2. Clique no TikTok Pixel Helper no navegador.
3. Confira os códigos de pixel identificados na página.
4. Execute a ação ou acesse a página de conversão e verifique o evento exibido.

### U:dac89e63e3935202:026 — Confirme o evento pela URL que aciona sua regra
```yaml
tipo: exemplo
plataforma: [tiktok]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: "00:19:50–00:21:37"
perecivel: true
confianca: alta
versao: 1
```
Situação: a regra Subscribe foi criada para uma URL que contém `/aulas/confirmado`.
O que aconteceu: ao abrir essa página, o TikTok Pixel Helper mostra Subscribe no Pixel Subido.
Lógica: o evento aparece porque a URL acessada contém o texto definido na regra do pixel.

### U:dac89e63e3935202:027 — Pixel habilita públicos de tráfego do website
```yaml
tipo: conceito
plataforma: [tiktok]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: "00:20:53–00:21:37"
perecivel: false
confianca: alta
versao: 1
```
Depois de verificar pixel e eventos, o rastreamento permite criar custom audiences de website traffic: pessoas que acessaram o site.