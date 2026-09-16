---
type: unidades-aula
status: rascunho
title: "2.Explorando o TikTok Ads na prática"
modulo: "008"
ordem: 121
aula_id: ad283ee8d2df7cda
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

# 2.Explorando o TikTok Ads na prática

## Contexto da aula

A aula apresenta os menus principais do TikTok Ads para localização na interface.
Parte da entrada no Business Center, da vinculação de contas e do acesso ao Ads Manager.
Mostra a leitura por campanha, grupos de anúncio e anúncios, além de filtros, colunas e exportação.
Também situa os menus de ativos, pagamentos e configurações.
A criação de pixel, conversões e públicos fica para aulas posteriores.

## Unidades

### U:ad283ee8d2df7cda:001 — Business Center reúne as Business Centers da conta
```yaml
tipo: alerta-ui
plataforma: [tiktok]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:00:00–00:00:45"
perecivel: true
confianca: alta
versao: 1
```
Ao entrar em `business.tiktok.com.br`, a tela lista as Business Centers (BCs), equivalentes às Business Managers do Facebook.
No ícone de usuário também há opções para alterar o idioma e abrir User Settings.

### U:ad283ee8d2df7cda:002 — Vincular conta TikTok ao usuário em User Settings
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:00:00–00:01:24"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: acesso ao usuário que será associado à conta TikTok.
1. Abra User Settings pelo ícone de usuário.
2. Vincule a conta TikTok ao usuário, que possui e-mail e telefone associados.
A vinculação é feita no usuário, não diretamente no Business Center.

### U:ad283ee8d2df7cda:003 — Linha de crédito pode ser oferecida após maior investimento
```yaml
tipo: exemplo
plataforma: [tiktok]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:00:45–00:02:04"
perecivel: false
confianca: alta
versao: 1
```
Situação: a operação tinha uma Business Center com cartão de crédito.
O que aconteceu: após começar a investir mais no TikTok, recebeu a oferta de Credit Line e passou a usar outra BC com esse método.
Lógica: a linha de crédito foi considerada mais adequada à organização contábil da empresa.

### U:ad283ee8d2df7cda:004 — Recursos disponíveis dentro da Business Center
```yaml
tipo: alerta-ui
plataforma: [tiktok]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:01:24–00:02:04"
perecivel: true
confianca: alta
versao: 1
```
Na Business Center há áreas para membros, parceiros, contas de anúncio, audiências, catálogos, pixels, grupos de ativos e contas TikTok.
Parceiros permitem adicionar outra Business Center como parceira da sua BC.

### U:ad283ee8d2df7cda:005 — Dar acesso de uma conta TikTok à Business Center
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:02:04–00:02:43"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: o dono da conta TikTok deve poder autorizar o acesso.
1. Em TikTok Accounts, clique em Request Access, libere as duas opções mostradas e gere o QR Code.
2. Na conta TikTok, abra Amigos/Friends, use o botão de adicionar amigo e depois o de escanear QR Code.
3. Autorize o acesso da conta à Business Center.

### U:ad283ee8d2df7cda:006 — Verificação sustenta o uso de linha de crédito
```yaml
tipo: regra
plataforma: [tiktok]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:02:43–00:03:23"
condicoes: "para ter uma linha de crédito como método de pagamento"
perecivel: true
confianca: alta
versao: 1
```
Adicione na área de verificação os documentos adicionais solicitados pelo TikTok para obter linha de crédito.

### U:ad283ee8d2df7cda:007 — Alterações de dados cadastrais ficam em configurações
```yaml
tipo: alerta-ui
plataforma: [tiktok]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:02:43–00:03:23"
perecivel: true
confianca: alta
versao: 1
```
Use Configurações para alterar e-mail, senha e endereço.

### U:ad283ee8d2df7cda:008 — Abrir uma conta de anúncio pelo Business Center
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:03:23–00:04:01"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: existir uma conta de anúncio na Business Center.
1. Abra Advertiser Accounts.
2. Selecione a conta de anúncio desejada.
3. Abra Ads Manager para entrar na conta.

### U:ad283ee8d2df7cda:009 — Acesso direto ao Ads Manager pelo endereço ads.tiktok.com
```yaml
tipo: decisao
plataforma: [tiktok]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:03:23–00:04:01"
perecivel: true
confianca: alta
versao: 1
```
Quando quiser acessar a conta de anúncios sem passar pela Business Center, abra diretamente `ads.tiktok.com`.

### U:ad283ee8d2df7cda:010 — Preferir a visualização por campanha ao dashboard
```yaml
tipo: decisao
plataforma: [tiktok]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: fala
faixa: "00:04:01–00:04:37"
perecivel: true
confianca: alta
versao: 1
```
Quando for analisar a conta, prefira a aba de campanha ao dashboard; ela se parece mais com a visualização do Facebook.

### U:ad283ee8d2df7cda:011 — Filtrar campanhas por nome e outros critérios
```yaml
tipo: alerta-ui
plataforma: [tiktok]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: fala
faixa: "00:04:01–00:04:37"
perecivel: true
confianca: alta
versao: 1
```
Na aba de campanhas, filtre pelo nome da campanha, por métrica, objetivo ou segmentação.
Por exemplo, buscar “convite” mostra as campanhas cujo nome contém essa palavra.

### U:ad283ee8d2df7cda:012 — Hierarquia de campanha, grupo de anúncio e anúncio
```yaml
tipo: conceito
plataforma: [tiktok]
tema: estrutura-de-campanha
tarefas: [definir-estrutura-de-campanha]
fonte: fala
faixa: "00:04:37–00:05:15"
perecivel: true
confianca: alta
versao: 1
```
A estrutura do TikTok Ads segue campanha, grupo de anúncio e anúncio, como no Facebook Ads.
Ao selecionar uma campanha, a aba de grupos mostra apenas os grupos daquela campanha.

### U:ad283ee8d2df7cda:013 — Selecionar o período do relatório
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: fala
faixa: "00:04:37–00:05:15"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: estar na visão de campanhas.
1. Abra o filtro de datas e escolha vida inteira, hoje, ontem, últimos 7 dias ou últimos 14 dias.
2. Para outro período, clique nas datas e selecione os dias e meses desejados.

### U:ad283ee8d2df7cda:014 — Personalizar colunas de métricas
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: fala
faixa: "00:05:15–00:05:51"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: estar na área de colunas do relatório.
1. Comece pelas colunas padrão.
2. Adicione as métricas que precisa analisar.
3. Passe o mouse sobre uma métrica para ler sua explicação quando não souber o significado.

### U:ad283ee8d2df7cda:015 — Manter 20 campanhas por página como padrão pessoal
```yaml
tipo: regua
plataforma: [tiktok]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: fala
faixa: "00:05:51–00:06:29"
condicoes: "quando não houver muitas campanhas ativas simultaneamente"
perecivel: true
confianca: alta
versao: 1
```
O professor deixa 20 campanhas por página, em vez de 50, porque não mantém muitas campanhas ativas ao mesmo tempo.

### U:ad283ee8d2df7cda:016 — Eventos é o menu de configuração do pixel
```yaml
tipo: alerta-ui
plataforma: [tiktok]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: "00:05:51–00:06:29"
perecivel: true
confianca: alta
versao: 1
```
Na aba Assets, Eventos é o menu em que se configura o pixel.

### U:ad283ee8d2df7cda:017 — Menus de ativos da conta
```yaml
tipo: alerta-ui
plataforma: [tiktok]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:05:51–00:07:14"
perecivel: true
confianca: alta
versao: 1
```
Em Assets, Criativos mostra informações dos anúncios, Audiências é onde se criam públicos e Catalogs serve para configurar catálogos de e-commerce.
Comentários reúne os comentários dos anúncios; Instant Pages não é uma preocupação por enquanto.

### U:ad283ee8d2df7cda:018 — Preferir colunas ao menu de relatórios
```yaml
tipo: decisao
plataforma: [tiktok]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: fala
faixa: "00:06:29–00:07:14"
perecivel: true
confianca: alta
versao: 1
```
Quando for ler o que ocorre nas campanhas, prefira o relatório em colunas na aba Campanha em vez da aba Reporting.

### U:ad283ee8d2df7cda:019 — Exportar relatório pela aba de campanha
```yaml
tipo: alerta-ui
plataforma: [tiktok]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: fala
faixa: "00:07:14–00:07:50"
perecivel: true
confianca: alta
versao: 1
```
Na aba Campanha, use o botão de exportar relatório para fazer o export no formato desejado.

### U:ad283ee8d2df7cda:020 — Trocar de conta e retornar à Business Center
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:07:14–00:07:50"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: estar dentro do Ads Manager.
1. Clique em Business Center para voltar à página anterior da BC.
2. Use o seletor no topo para mudar de conta de anúncio.
3. Abra o ícone de usuário para acessar as configurações da conta.

### U:ad283ee8d2df7cda:021 — User Settings concentra dados e conta TikTok vinculada
```yaml
tipo: alerta-ui
plataforma: [tiktok]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:07:50–00:08:33"
perecivel: true
confianca: alta
versao: 1
```
O User Settings aberto pelo ícone de usuário permite configurar telefone, e-mail, senha e a conta TikTok vinculada ao usuário.

### U:ad283ee8d2df7cda:022 — Payment mostra informações financeiras da conta de anúncios
```yaml
tipo: alerta-ui
plataforma: [tiktok]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:07:56–00:08:33"
perecivel: true
confianca: alta
versao: 1
```
Em Payment, consulte crédito disponível, valor devido, formas de pagamento, documentos e notas fiscais.

### U:ad283ee8d2df7cda:023 — Configurações gerais reúnem dados da conta e pagamento
```yaml
tipo: alerta-ui
plataforma: [tiktok]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:08:34–00:09:54"
perecivel: true
confianca: alta
versao: 1
```
Nas configurações gerais da conta de anúncios, informe nome da conta, dados do negócio, contato e informações de pagamento.
A área também exibe documentos da conta, como licença de CNPJ, documentos de indústria e documentos de anúncio quando solicitados.

### U:ad283ee8d2df7cda:024 — Pixel, conversões e públicos serão aprofundados depois
```yaml
tipo: limite
plataforma: [tiktok]
tema: pixel-e-eventos
tarefas: []
fonte: fala
faixa: "00:09:18–00:10:00"
perecivel: false
confianca: alta
versao: 1
```
A aula apenas localiza os menus; a criação do pixel e a configuração de conversões serão aprofundadas nas próximas aulas.
A criação de públicos dentro do TikTok Ads também fica para a aula subsequente.