---
type: unidades-aula
status: validado
title: "5.Atualizando seus públicos"
modulo: "008"
ordem: 124
aula_id: 4b095e6083b082f6
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

# 5.Atualizando seus públicos

## Contexto da aula

A aula corrige informações da aula anterior sobre atualização de públicos no TikTok.
Ela trata públicos personalizados de engajamento com anúncios e públicos semelhantes.
A demonstração mostra como evitar atualização manual escolhendo todos os grupos de anúncio.
Também esclarece o limite de públicos criados com grupos específicos e a atualização conforme o público-base.

## Unidades

### U:4b095e6083b082f6:001 — Criar público de engajamento para todos os anúncios de vídeo

```yaml
tipo: procedimento
plataforma: [tiktok]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: 00:00:00–00:02:47
perecivel: true
confianca: alta
versao: 1
```

Pré-condição: estar em Ativos > Audiences e iniciar a criação de uma Custom Audience de engajamento.
1. Em Ads Type, selecione Video Ads e escolha a ação desejada, como clique, impressão ou visualização de 25% do vídeo.
2. Não selecione nenhum grupo de anúncio; deixe a seleção como all.
3. Defina a janela, como pessoas que viram 25% de algum vídeo nos últimos 7 dias, e crie o público.
4. Nomeie o público com uma identificação de engajamento e os parâmetros usados, como vídeo, all, percentual e dias.

### U:4b095e6083b082f6:002 — Público de engajamento com all se atualiza sozinho

```yaml
tipo: decisao
plataforma: [tiktok]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: 00:01:12–00:02:47
condicoes: "na criação do público, nenhum grupo de anúncio é selecionado e a opção fica como all"
perecivel: true
confianca: alta
versao: 1
```

Se o público de engajamento ficar com all, ele inclui pessoas que realizaram a ação escolhida em qualquer anúncio de vídeo dentro da janela definida e se atualiza automaticamente, inclusive quando surgirem novos grupos de anúncio.

### U:4b095e6083b082f6:003 — Não selecione grupos para público que precisa acompanhar novos anúncios

```yaml
tipo: regra
plataforma: [tiktok]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: 00:01:59–00:03:26
perecivel: true
confianca: alta
versao: 1
```

Crie os públicos de vídeo visualizado recomendados na aula anterior com all, sem selecionar grupos de anúncio, para não precisar atualizá-los manualmente.

### U:4b095e6083b082f6:004 — Grupos selecionados em público não podem ser alterados depois

```yaml
tipo: decisao
plataforma: [tiktok]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: 00:02:48–00:04:38
perecivel: true
confianca: alta
versao: 1
```

Se você criar um público de vídeo visualizado selecionando grupos de anúncio específicos, ele permanece vinculado somente a esses grupos; não é possível editar o público para incluir outros depois.

### U:4b095e6083b082f6:005 — Apply to Ad Groups aplica o público, não adiciona grupos à origem

```yaml
tipo: alerta-ui
plataforma: [tiktok]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: 00:03:55–00:04:38
perecivel: true
confianca: alta
versao: 1
```

No detalhe de um público, o botão Apply to Ad Groups adiciona esse público a grupos de anúncio ativos da conta. Ele não serve para adicionar novos grupos de anúncio à composição do público.

### U:4b095e6083b082f6:006 — Lookalikes são atualizados automaticamente com a origem

```yaml
tipo: decisao
plataforma: [tiktok]
tema: publicos
tarefas: [montar-publicos-semelhantes]
fonte: fala
faixa: 00:04:38–00:06:49
condicoes: "o público-base ou público de origem continua se atualizando"
perecivel: true
confianca: alta
versao: 1
```

Quando o público-base se atualiza sozinho, o público lookalike também se atualiza automaticamente; não é necessário entrar nele para fazer refresh manual.

### U:4b095e6083b082f6:007 — Histórico da audiência mostra atualizações do lookalike

```yaml
tipo: alerta-ui
plataforma: [tiktok]
tema: publicos
tarefas: [montar-publicos-semelhantes]
fonte: fala
faixa: 00:04:38–00:06:10
perecivel: true
confianca: alta
versao: 1
```

Dentro de um público lookalike, a aba ou menu Audience History mostra as ocasiões em que o público foi atualizado, inclusive atualizações automáticas e refresh feito manualmente.

### U:4b095e6083b082f6:008 — Refresh manual não altera lookalike com origem parada

```yaml
tipo: decisao
plataforma: [tiktok]
tema: publicos
tarefas: [montar-publicos-semelhantes]
fonte: fala
faixa: 00:05:33–00:06:49
condicoes: "o público-base não está se atualizando"
perecivel: true
confianca: alta
versao: 1
```

Se o público-base não se atualiza, não faça refresh no lookalike esperando mudança, porque ele permanece igual.

### U:4b095e6083b082f6:009 — Lookalike observado recebeu auto refresh a cada 3 ou 4 dias

```yaml
tipo: regua
plataforma: [tiktok]
tema: publicos
tarefas: [montar-publicos-semelhantes]
fonte: fala
faixa: 00:06:10–00:06:49
condicoes: "exemplo de um lookalike cujo público-base Clique 180 Dias se atualizava"
perecivel: true
confianca: alta
versao: 1
```

No histórico do exemplo, o lookalike recebeu atualizações automáticas em vários dias, aproximadamente a cada 3 ou 4 dias.

### U:4b095e6083b082f6:010 — Use o Ad Group ID para incluir grupos específicos

```yaml
tipo: procedimento
plataforma: [tiktok]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: 00:06:49–00:08:41
perecivel: true
confianca: alta
versao: 1
```

Pré-condição: você quer criar um público a partir de grupos de anúncio específicos de uma campanha.
1. Abra a campanha e localize os grupos de anúncio que devem compor o público.
2. Copie o Ad Group ID de cada grupo.
3. Na criação da Custom Audience de engajamento, pesquise cada ID pelo campo de busca ou ícone de lupa e adicione os grupos encontrados.
4. Salve o novo público com a ação e o percentual de visualização desejados.

### U:4b095e6083b082f6:011 — Crie outro público para incluir grupos após salvar

```yaml
tipo: decisao
plataforma: [tiktok]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: 00:08:00–00:08:50
perecivel: true
confianca: alta
versao: 1
```

Se precisar incluir mais grupos de anúncio depois de salvar um público criado com grupos específicos, crie um novo público, porque o público salvo não pode ser modificado.