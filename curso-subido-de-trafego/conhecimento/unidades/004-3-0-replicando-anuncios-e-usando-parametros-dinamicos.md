---
type: unidades-aula
status: validado
title: "3.0 - Replicando anúncios e usando parâmetros dinâmicos"
modulo: "004"
ordem: 64
aula_id: 7e4aeaa8c3d22a71
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - cst_m04_a03_replicando_anuncios_usando_parametros_dinamicos.pdf
  - transcricao.md
extraido_em: 2026-09-16
gerado_por: gpt-5.6-terra
retiradas: []
divisoes: []
fusoes: []
---

# 3.0 - Replicando anúncios e usando parâmetros dinâmicos

## Contexto da aula

A aula demonstra como replicar anúncios em uma campanha da Rede de Pesquisa do Google.
Parte de uma campanha que contém grupo de anúncios, palavras-chave e anúncios.
Mostra variações de títulos e descrições, incluindo parâmetros dinâmicos de palavra-chave, contagem regressiva e local.
Explica cuidados de segmentação e a distribuição de verba entre anúncios de um mesmo grupo.
A replicação de grupos de anúncios fica para a próxima aula.

## Unidades

### U:7e4aeaa8c3d22a71:001 — Hierarquia usada para criar variações de anúncios
```yaml
tipo: conceito
plataforma: [google-search]
tema: estrutura-de-campanha
tarefas: [definir-estrutura-de-campanha]
fonte: "fala+pdf:cst_m04_a03_replicando_anuncios_usando_parametros_dinamicos.pdf"
faixa: "00:00:00–00:00:27"
perecivel: false
confianca: alta
versao: 1
```
Na campanha há um grupo de anúncios; dentro dele ficam palavras-chave relacionadas e os anúncios.
A replicação parte de um anúncio já criado dentro desse grupo.

### U:7e4aeaa8c3d22a71:002 — Replicar anúncio não aumenta o orçamento diário
```yaml
tipo: regra
plataforma: [google-search]
tema: orcamento
tarefas: [definir-orcamento, configurar-anuncio]
fonte: fala
faixa: "00:00:00–00:00:27"
perecivel: false
confianca: alta
versao: 1
```
Replicar anúncios não faz o Google cobrar mais do que o valor diário definido; ele concentra mais dinheiro no anúncio que performa melhor.

### U:7e4aeaa8c3d22a71:003 — Três formas de replicar um anúncio
```yaml
tipo: procedimento
plataforma: [google-search]
tema: criativo
tarefas: [configurar-anuncio]
fonte: "fala+pdf:cst_m04_a03_replicando_anuncios_usando_parametros_dinamicos.pdf"
faixa: "00:00:27–00:01:41"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: um anúncio existente selecionado no Google Ads.
1. Copie com CTRL-C, feche a faixa azul que informa a cópia e cole com CTRL-V.
2. Alternativamente, em “editar”, escolha “copiar”; volte a “editar” e escolha “colar”.
3. Como terceira opção, use o botão “+” para criar um anúncio responsivo da Rede de Pesquisa; o Google puxa dados do anúncio anterior.

### U:7e4aeaa8c3d22a71:004 — Use anúncio responsivo em vez do texto expandido descontinuado
```yaml
tipo: decisao
plataforma: [google-search]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: "00:01:05–00:02:20"
perecivel: true
confianca: alta
versao: 1
nota: "A tela demonstrada informa que anúncios de texto expandido não poderiam ser criados nem editados a partir de 30 de junho de 2022; informação perecível."
```
Quando a tela oferecer anúncio responsivo e anúncio de texto expandido, use o responsivo, pois o expandido é apresentado como descontinuado.

### U:7e4aeaa8c3d22a71:005 — Faça variações de títulos e descrições
```yaml
tipo: regra
plataforma: [google-search]
tema: criativo
tarefas: [configurar-anuncio]
fonte: "fala+pdf:cst_m04_a03_replicando_anuncios_usando_parametros_dinamicos.pdf"
faixa: "00:01:41–00:03:09"
perecivel: false
confianca: alta
versao: 1
```
Crie variações do anúncio mudando títulos, descrições ou ambos; também é possível manter um deles e alterar o outro.

### U:7e4aeaa8c3d22a71:006 — Configure inserção dinâmica de palavra-chave
```yaml
tipo: procedimento
plataforma: [google-search]
tema: criativo
tarefas: [configurar-anuncio]
fonte: "fala+pdf:cst_m04_a03_replicando_anuncios_usando_parametros_dinamicos.pdf"
faixa: "00:02:20–00:03:29"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: edição de um título ou descrição do anúncio responsivo.
1. Digite “{” para abrir as opções de parâmetros e selecione “inserção de palavra-chave”.
2. Informe uma palavra-chave padrão, usada se a inserção não der certo.
3. Escolha a capitalização da frase e clique em “aplicar”; o professor diz que não há modo certo para essa escolha.

### U:7e4aeaa8c3d22a71:007 — Palavra-chave dinâmica usa padrão acima de 30 caracteres
```yaml
tipo: regua
plataforma: [google-search]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: "00:03:29–00:05:10"
perecivel: false
confianca: alta
versao: 1
```
A inserção dinâmica pode trocar o título pelo termo pesquisado; se a pesquisa for maior do que 30 caracteres, o Google usa a palavra-chave padrão definida no anúncio.

### U:7e4aeaa8c3d22a71:008 — Controle termos da inserção dinâmica pelas palavras-chave
```yaml
tipo: decisao
plataforma: [google-search]
tema: palavras-chave
tarefas: [montar-lista-de-palavras-chave, configurar-anuncio]
fonte: "fala+pdf:cst_m04_a03_replicando_anuncios_usando_parametros_dinamicos.pdf"
faixa: "00:05:10–00:07:14"
condicoes: "ao usar inserção dinâmica de palavra-chave"
perecivel: false
confianca: alta
versao: 1
```
Se usar inserção dinâmica, segmente bem as palavras-chave para escolher para quais pesquisas o anúncio aparecerá.
Sem esse controle, o título pode exibir termos que você não desejaria, inclusive o nome de concorrentes.

### U:7e4aeaa8c3d22a71:009 — Configure a contagem regressiva pelo fuso da conta
```yaml
tipo: procedimento
plataforma: [google-search]
tema: criativo
tarefas: [configurar-anuncio]
fonte: "fala+pdf:cst_m04_a03_replicando_anuncios_usando_parametros_dinamicos.pdf"
faixa: "00:07:14–00:09:43"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: uma oferta ou ação com data e horário de término definidos.
1. Digite “{” no título ou na descrição e selecione “contagem regressiva”.
2. Defina a data final, o horário e quantos dias antes o anúncio começa a fazer a contagem.
3. Use o fuso horário da conta e clique em “aplicar”.

### U:7e4aeaa8c3d22a71:010 — Ligue a contagem quando ela puder começar
```yaml
tipo: decisao
plataforma: [google-search]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: "00:09:00–00:10:45"
condicoes: "ao usar contagem regressiva"
perecivel: false
confianca: alta
versao: 1
```
Quando a contagem regressiva puder começar no anúncio, ligue-a; não faz sentido ativá-la antes do período configurado.
Após o término, altere o anúncio.

### U:7e4aeaa8c3d22a71:011 — Contagem regressiva atualiza o anúncio automaticamente
```yaml
tipo: conceito
plataforma: [google-search]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: "00:08:08–00:10:45"
perecivel: false
confianca: alta
versao: 1
```
A contagem mostra o prazo restante no anúncio e se atualiza a cada pesquisa, chegando a exibir horas e minutos próximos do fim.
O professor a indica para algo com duração determinada, por usar escassez.

### U:7e4aeaa8c3d22a71:012 — Use inserção de local com texto padrão
```yaml
tipo: procedimento
plataforma: [google-search]
tema: criativo
tarefas: [configurar-anuncio]
fonte: "fala+pdf:cst_m04_a03_replicando_anuncios_usando_parametros_dinamicos.pdf"
faixa: "00:10:45–00:12:55"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: o anúncio deve adaptar cidade, estado ou país à localização da pessoa.
1. Digite “{” e selecione “inserção de local” no título ou na descrição.
2. Escolha se será inserida cidade, estado ou país.
3. Preencha o “texto padrão” com uma alternativa que caiba quando o nome do local for longo e clique em “aplicar”.

### U:7e4aeaa8c3d22a71:013 — Use parâmetros uma vez por anúncio quando necessário
```yaml
tipo: regra
plataforma: [google-search]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: "00:12:15–00:14:29"
perecivel: false
confianca: alta
versao: 1
```
Use keyword, countdown ou inserção de local uma vez no anúncio quando quiser; não é preciso repetir o parâmetro.
Os parâmetros podem ser colocados no título ou na descrição.

### U:7e4aeaa8c3d22a71:014 — Mantenha os termos relacionados ao grupo de anúncios
```yaml
tipo: regra
plataforma: [google-search]
tema: palavras-chave
tarefas: [configurar-anuncio]
fonte: fala
faixa: "00:13:49–00:14:29"
perecivel: false
confianca: alta
versao: 1
```
Ao alterar títulos e descrições, use palavras relacionadas às palavras-chave do grupo de anúncios para o qual o anúncio foi criado.

### U:7e4aeaa8c3d22a71:015 — Use pelo menos três anúncios por grupo
```yaml
tipo: regua
plataforma: [google-search]
tema: estrutura-de-campanha
tarefas: [definir-estrutura-de-campanha, configurar-anuncio]
fonte: "fala+pdf:cst_m04_a03_replicando_anuncios_usando_parametros_dinamicos.pdf"
faixa: "00:13:07–00:15:28"
perecivel: false
confianca: alta
versao: 1
```
Use 3 anúncios como mínimo em cada grupo de anúncios.
O Google pode destinar mais dinheiro ao anúncio que funciona melhor sem extrapolar o orçamento diário definido.

### U:7e4aeaa8c3d22a71:016 — Salve o anúncio e repita para o terceiro
```yaml
tipo: procedimento
plataforma: [google-search]
tema: criativo
tarefas: [configurar-anuncio]
fonte: "fala+pdf:cst_m04_a03_replicando_anuncios_usando_parametros_dinamicos.pdf"
faixa: "00:14:29–00:15:28"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: títulos, descrições e palavras do novo anúncio já foram ajustados para o grupo.
1. Clique em “salvar anúncio” para incluir a variação no grupo.
2. Clique em criar anúncio responsivo de pesquisa e repita as alterações para formar o terceiro anúncio.
3. Se quiser exibir um caminho na URL, ajuste-o para corresponder à página de destino.

### U:7e4aeaa8c3d22a71:017 — Replicação de grupos fica para a próxima aula
```yaml
tipo: limite
plataforma: [google-search]
tema: estrutura-de-campanha
tarefas: []
fonte: "fala+pdf:cst_m04_a03_replicando_anuncios_usando_parametros_dinamicos.pdf"
faixa: "00:15:28–00:16:50"
perecivel: false
confianca: alta
versao: 1
```
A aula não mostra como replicar grupos de anúncios; esse procedimento é apresentado na próxima aula.