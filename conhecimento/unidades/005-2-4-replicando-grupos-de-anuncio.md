---
type: unidades-aula
status: validado
title: "2.4 - Replicando grupos de anúncio"
modulo: "005"
ordem: 82
aula_id: 147e71289b14d87e
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - cst_m05_a24_replicando_grupos_de_anuncio.pdf
  - transcricao.md
extraido_em: 2026-09-16
gerado_por: gpt-5.6-terra
retiradas: []
divisoes: []
fusoes: []
---

# 2.4 - Replicando grupos de anúncio

## Contexto da aula

A aula demonstra como duplicar grupos de anúncios em uma campanha de YouTube.
O processo parte de um grupo existente e troca nome, segmentação e, quando aplicável, exclusões.
O professor usa públicos de canais, envolvimento, cadastros e segmentos personalizados como exemplos.
A decisão de excluir públicos depende da hierarquia escolhida; iniciantes podem prosseguir sem exclusões.
A otimização da campanha fica para uma aula posterior.

## Unidades

### U:147e71289b14d87e:001 — Abrir a campanha para visualizar os grupos de anúncios
```yaml
tipo: alerta-ui
plataforma: [youtube]
tema: estrutura-de-campanha
tarefas: [replicar-campanhas-e-grupos]
fonte: "fala+pdf:cst_m05_a24_replicando_grupos_de_anuncio.pdf"
faixa: "00:00:00–00:00:31"
perecivel: true
confianca: alta
versao: 1
nota: "O PDF orienta selecionar Anúncios no menu lateral e a campanha na barra superior; ver p. 2."
```
Para ver outros grupos de anúncios, saia do grupo aberto e entre na campanha pelo nome dela.
No PDF, o caminho começa em “anúncios” no menu lateral e segue pela seleção da campanha na barra superior.

### U:147e71289b14d87e:002 — Ordem para replicar um grupo de anúncios
```yaml
tipo: procedimento
plataforma: [youtube]
tema: estrutura-de-campanha
tarefas: [replicar-campanhas-e-grupos]
fonte: "fala+pdf:cst_m05_a24_replicando_grupos_de_anuncio.pdf"
faixa: "00:00:31–00:01:56"
perecivel: true
confianca: alta
versao: 1
nota: "O PDF apresenta a mesma ordem e inclui a exclusão da segmentação anterior como quinto passo; ver p. 2."
```
Pré-condição: estar na campanha e visualizar os grupos de anúncios.
1. Selecione o grupo que será a base e copie-o; o professor prefere Ctrl C e Ctrl V.
2. Cole a cópia sem selecionar opções adicionais na cópia.
3. Altere o nome do novo grupo conforme a hierarquia de públicos.
4. Remova a segmentação anterior e insira a nova.
5. Faça exclusões da segmentação anterior quando a hierarquia exigir.

### U:147e71289b14d87e:003 — Renomear o grupo copiado pela hierarquia de públicos
```yaml
tipo: alerta-ui
plataforma: [youtube]
tema: nomenclatura
tarefas: [replicar-campanhas-e-grupos, nomear-campanhas]
fonte: "fala+pdf:cst_m05_a24_replicando_grupos_de_anuncio.pdf"
faixa: "00:01:21–00:02:40"
perecivel: true
confianca: alta
versao: 1
nota: "O PDF indica alterar o nome pelo ícone de pincel e salvar; ver p. 3."
```
Depois de copiar, altere o nome do grupo novo segundo a hierarquia de públicos já criada e salve.
No exemplo, o grupo de envolvimento completo recebe a identificação 00.

### U:147e71289b14d87e:004 — Remover a segmentação de canais herdada
```yaml
tipo: procedimento
plataforma: [youtube]
tema: publicos
tarefas: [replicar-campanhas-e-grupos, definir-segmentacao-demografica-e-interesses]
fonte: "fala+pdf:cst_m05_a24_replicando_grupos_de_anuncio.pdf"
faixa: "00:02:40–00:04:10"
perecivel: true
confianca: alta
versao: 1
nota: "O procedimento do PDF para segmentação de canais está nas pp. 3–4."
```
Pré-condição: o novo grupo é uma cópia que herdou uma segmentação de canais.
1. Entre no novo grupo de anúncios.
2. Abra “conteúdo” e depois “canais” no menu lateral.
3. Selecione todos os canais.
4. Use “editar” e “remover” para retirar a segmentação herdada.

### U:147e71289b14d87e:005 — Inserir o novo público sem ampliar para semelhantes
```yaml
tipo: procedimento
plataforma: [youtube]
tema: publicos
tarefas: [replicar-campanhas-e-grupos, montar-publicos-personalizados]
fonte: "fala+pdf:cst_m05_a24_replicando_grupos_de_anuncio.pdf"
faixa: "00:04:10–00:05:10"
perecivel: true
confianca: alta
versao: 1
nota: "O PDF registra o caminho de público-alvo e a opção que não deve ser marcada; ver pp. 4–6."
```
Pré-condição: a segmentação anterior do grupo copiado foi removida.
1. Abra “público-alvo” no menu lateral.
2. Selecione “editar segmentos de público-alvo”.
3. Remova o público anterior pelo “x” em “1 item selecionado”, se ele ainda estiver listado.
4. Na aba “pesquisa”, busque e selecione o novo público.
5. Não selecione “alcance mais pessoas semelhantes aos seus públicos-alvo selecionados”.

### U:147e71289b14d87e:006 — Excluir públicos anteriores só com hierarquia de públicos
```yaml
tipo: decisao
plataforma: [youtube]
tema: publicos
tarefas: [replicar-campanhas-e-grupos, organizar-hierarquia-e-exclusao-de-publicos]
fonte: fala
faixa: "00:04:24–00:05:16"
condicoes: "A exclusão depende de a estrutura usar hierarquia entre os públicos."
perecivel: false
confianca: alta
versao: 1
```
Se os dois públicos ficam como 00 para aceitar competição e não reduzir seu tamanho, não faça exclusão.
Quando criar um público 01 abaixo de outro na hierarquia, inclua a exclusão dos públicos anteriores.

### U:147e71289b14d87e:007 — Configure exclusões no grupo, não na campanha
```yaml
tipo: alerta-ui
plataforma: [youtube]
tema: publicos
tarefas: [replicar-campanhas-e-grupos, organizar-hierarquia-e-exclusao-de-publicos]
fonte: "fala+pdf:cst_m05_a24_replicando_grupos_de_anuncio.pdf"
faixa: "00:07:45–00:10:17"
perecivel: true
confianca: alta
versao: 1
nota: "O PDF orienta abrir “exclusões”, usar “editar exclusões”, selecionar “excluir grupos de anúncios”, buscar o público e salvar; ver pp. 7–8."
```
Faça a exclusão no grupo de anúncios, não na campanha.
Em “exclusões”, abra “editar exclusões”, escolha “excluir grupos de anúncios”, informe o público a excluir e salve.

### U:147e71289b14d87e:008 — Não excluir o público de canais
```yaml
tipo: regra
plataforma: [youtube]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos]
fonte: fala
faixa: "00:08:31–00:09:40"
perecivel: false
confianca: alta
versao: 1
```
Não exclua o público de canais de nenhum lugar; o professor o trata como separado da hierarquia dos demais públicos.

### U:147e71289b14d87e:009 — Copiar sempre o último grupo criado
```yaml
tipo: regra
plataforma: [youtube]
tema: estrutura-de-campanha
tarefas: [replicar-campanhas-e-grupos]
fonte: "fala+pdf:cst_m05_a24_replicando_grupos_de_anuncio.pdf"
faixa: "00:10:17–00:11:13"
perecivel: true
confianca: alta
versao: 1
nota: "O PDF também determina repetir o processo usando o último grupo criado; ver p. 9."
```
Para replicar mais grupos, copie e cole sempre o último grupo de anúncio criado.

### U:147e71289b14d87e:010 — Permitir mais de uma nova segmentação
```yaml
tipo: decisao
plataforma: [youtube]
tema: publicos
tarefas: [replicar-campanhas-e-grupos, montar-publicos-personalizados]
fonte: fala
faixa: "00:11:14–00:12:17"
perecivel: true
confianca: alta
versao: 1
```
Se estiver em dúvida entre adicionar dois públicos, pode inserir os dois; o Google escolherá em qual gastar mais dinheiro.

### U:147e71289b14d87e:011 — Não travar a execução por dúvida sobre exclusões
```yaml
tipo: decisao
plataforma: [youtube]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos, replicar-campanhas-e-grupos]
fonte: "fala+pdf:cst_m05_a24_replicando_grupos_de_anuncio.pdf"
faixa: "00:13:01–00:14:32"
condicoes: "Quando houver dúvida ou trava sobre a hierarquia e as exclusões, especialmente no início."
perecivel: false
confianca: alta
versao: 1
nota: "O PDF dá a mesma orientação: não excluir públicos, fazer testes e priorizar executar bem; ver p. 9."
```
Se a hierarquia de públicos estiver travando você, não faça exclusões.
Crie os públicos que receberão anúncio e use numeração como 00, 01, 02 e 03 apenas para organização.