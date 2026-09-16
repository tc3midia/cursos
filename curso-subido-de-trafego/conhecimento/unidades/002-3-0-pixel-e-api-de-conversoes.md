---
type: unidades-aula
status: validado
title: "3.0 - Pixel e API de Conversões"
modulo: "002"
ordem: 21
aula_id: cc1cb45cc04f075c
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

# 3.0 - Pixel e API de Conversões

## Contexto da aula
A aula trata das especificidades de Pixel e API de Conversões no Meta.
Ela pressupõe que o aluno tenha visto a aula mais ampla sobre o tema no módulo 1.
Mostra caminhos para criar, instalar e configurar um pixel pelo Gerenciador de Negócios e pelo Gerenciador de Eventos.
Eventos e conversões personalizadas ficam para a próxima aula.

## Unidades

### U:cc1cb45cc04f075c:001 — Assista à aula geral antes das especificidades do Meta
```yaml
tipo: regra
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: 00:00:00–00:01:22
perecivel: false
confianca: alta
versao: 1
```
Assista primeiro à aula de Pixel e API de Conversões do módulo 1; esta aula parte dela para tratar das particularidades do Meta.

### U:cc1cb45cc04f075c:002 — Esta aula foca nas especificidades de Pixel no Meta
```yaml
tipo: conceito
plataforma: [meta]
tema: pixel-e-eventos
tarefas: []
fonte: fala
faixa: 00:00:41–00:01:22
perecivel: false
confianca: media
versao: 1
nota: "A fonte chama a plataforma de MetaEdge; a taxonomia disponível usa meta."
```
A aula aborda Pixel e API de Conversões sob a perspectiva específica da plataforma Meta.

### U:cc1cb45cc04f075c:003 — Criar Pixel no Gerenciador de Negócios e liberar acessos
```yaml
tipo: procedimento
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: 00:01:22–00:02:02
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: estar no Gerenciador de Anúncios ou nas configurações do negócio.
1. Abra “Todas as ferramentas” e entre em “Configurações do negócio”.
2. Abra o menu “Pixel” e crie o Pixel.
3. Adicione pessoas e conceda acesso ao Pixel.
4. Conecte as contas de anúncio como ativos do Pixel.

### U:cc1cb45cc04f075c:004 — Um Pixel pode ser compartilhado com várias contas de anúncio
```yaml
tipo: regra
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: 00:01:22–00:02:35
perecivel: false
confianca: alta
versao: 1
```
Depois de criado na BM, conecte o Pixel às contas de anúncio que devem ter acesso a ele.

### U:cc1cb45cc04f075c:005 — Acessar o Gerenciador de Eventos pelo Gerenciador de Anúncios
```yaml
tipo: procedimento
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: 00:02:02–00:02:35
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: estar no Gerenciador de Anúncios.
1. Abra “Todas as ferramentas”.
2. Em “Gerenciar negócios”, selecione “Gerenciador de eventos”.
3. Use os caminhos disponíveis pela BM ou pela conta de anúncios para chegar ao mesmo gerenciador.

### U:cc1cb45cc04f075c:006 — Alterar o contexto aberto no Gerenciador de Eventos
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: 00:02:35–00:03:15
perecivel: true
confianca: alta
versao: 1
```
O Gerenciador de Eventos pode abrir uma conta de anúncios; use o seletor para trocar para a BM ou para outra conta de anúncios.

### U:cc1cb45cc04f075c:007 — Leia alertas do Gerenciador de Eventos sem se desesperar
```yaml
tipo: regra
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: 00:03:15–00:03:51
perecivel: true
confianca: alta
versao: 1
```
Leia os alertas exibidos, mas não conclua que há um problema só porque o alerta aparece em vermelho; segundo o professor, muitas vezes eles não indicam algo relevante.

### U:cc1cb45cc04f075c:008 — Pixel sem atividade pode indicar código não instalado corretamente
```yaml
tipo: decisao
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: 00:03:51–00:04:29
perecivel: true
confianca: alta
versao: 1
```
Se o Pixel não recebeu nenhuma atividade, verifique a instalação do código no site.

### U:cc1cb45cc04f075c:009 — Criar Pixel pelo Gerenciador de Eventos
```yaml
tipo: procedimento
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: 00:04:29–00:06:04
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: estar no Gerenciador de Eventos.
1. Clique em “Conectar fontes de dados”.
2. Selecione a fonte de dados web.
3. Nomeie o conjunto de dados.
4. Clique em “Criar” para criar o Pixel.

### U:cc1cb45cc04f075c:010 — Mantenha duas opções do Pixel ativadas
```yaml
tipo: procedimento
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: 00:06:04–00:06:41
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: estar nas configurações do Pixel criado.
1. Ative a correspondência automática do site.
2. Ative o rastreamento automático de eventos sem código.
3. Volte à visão geral e confirme se as opções continuaram ativadas.

### U:cc1cb45cc04f075c:011 — Há instalação pelo navegador e por eventos enviados do servidor
```yaml
tipo: conceito
plataforma: [meta]
tema: pixel-e-eventos
tarefas: []
fonte: fala
faixa: 00:06:42–00:07:14
perecivel: true
confianca: alta
versao: 1
```
O Pixel pode coletar eventos no navegador ou receber eventos enviados de um servidor; a segunda opção corresponde à API de Conversões.

### U:cc1cb45cc04f075c:012 — Use API de Conversões para melhor mapeamento de dados
```yaml
tipo: regra
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: 00:06:42–00:07:59
perecivel: false
confianca: alta
versao: 1
```
Use a API de Conversões, pois ela melhora o mapeamento dos dados do site e a identificação de pessoas pelo Pixel.

### U:cc1cb45cc04f075c:013 — Google Tag Manager é o caminho recomendado para instalar Pixel
```yaml
tipo: regra
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: 00:07:15–00:08:32
perecivel: false
confianca: alta
versao: 1
```
Aprenda Google Tag Manager para instalar o Pixel e a API de Conversões; o professor o apresenta como melhor amigo do Pixel.

### U:cc1cb45cc04f075c:014 — Escolher entre configurar API e Pixel na interface
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: 00:07:59–00:08:32
perecivel: true
confianca: alta
versao: 1
```
Para configurar a API, use “Configurar a API de Conversões”; para configurar o Pixel, use “Configurar o Pixel da Meta”.

### U:cc1cb45cc04f075c:015 — O identificador do Pixel é único
```yaml
tipo: conceito
plataforma: [meta]
tema: pixel-e-eventos
tarefas: []
fonte: fala
faixa: 00:08:33–00:09:16
perecivel: true
confianca: alta
versao: 1
```
O código do Pixel contém um número de identificação próprio; plataformas como Shopify, Loja Integrada, Trey e Hotmart podem pedir esse número.

### U:cc1cb45cc04f075c:016 — Instalar manualmente o código no head do site
```yaml
tipo: procedimento
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: 00:08:33–00:09:55
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: ter aberto a opção de adicionar o código manualmente.
1. Copie o código fornecido pelo configurador do Pixel.
2. Localize o número de identificação do Pixel no código.
3. Instale o código no head do site.
4. Clique em “Continuar”.

### U:cc1cb45cc04f075c:017 — Ative a correspondência automática avançada
```yaml
tipo: regra
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: 00:09:16–00:09:55
perecivel: true
confianca: alta
versao: 1
```
Ative sempre a correspondência automática avançada ao concluir a instalação manual do Pixel.

### U:cc1cb45cc04f075c:018 — Ferramenta de configuração de eventos exige Pixel instalado
```yaml
tipo: decisao
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [definir-conversoes-e-metas]
fonte: fala
faixa: 00:09:55–00:10:18
perecivel: true
confianca: alta
versao: 1
```
Se o Pixel já estiver instalado no site, use as ferramentas de configuração de eventos para associar ações de botões a eventos, como adicionar ao carrinho ou compra.

### U:cc1cb45cc04f075c:019 — Configurar Pixel por parceiros
```yaml
tipo: procedimento
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: 00:10:20–00:11:42
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: estar na visão geral do Pixel.
1. Clique em “Procurar parceiro”.
2. Escolha o parceiro da lista, como Google Tag Manager, Shopify, Magento, WordPress, Wix ou WooCommerce.
3. Siga o passo a passo de instalação apresentado pelo parceiro selecionado.

### U:cc1cb45cc04f075c:020 — Pixel pode ser criado em dois lugares
```yaml
tipo: conceito
plataforma: [meta]
tema: pixel-e-eventos
tarefas: []
fonte: fala
faixa: 00:11:01–00:12:00
perecivel: false
confianca: alta
versao: 1
```
O professor apresenta dois locais para criar o Pixel: o Gerenciador de Negócios e o Gerenciador de Eventos acessado pela conta de anúncios.

### U:cc1cb45cc04f075c:021 — Eventos e conversões personalizadas ficam para a próxima aula
```yaml
tipo: limite
plataforma: [meta]
tema: pixel-e-eventos
tarefas: []
fonte: fala
faixa: 00:11:42–00:12:00
perecivel: false
confianca: alta
versao: 1
```
A aula não detalha eventos nem conversões personalizadas; esses assuntos são deixados para a próxima aula.