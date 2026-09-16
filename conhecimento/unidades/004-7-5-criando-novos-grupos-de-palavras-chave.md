---
type: unidades-aula
status: validado
title: "7.5 - Criando novos grupos de palavras-chave"
modulo: "004"
ordem: 73
aula_id: d5fd0249c41087f6
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - cst_m04_a75_criando_novos_grupos_de_palavras_chave.pdf
  - transcricao.md
extraido_em: 2026-09-16
gerado_por: gpt-5.6-terra
retiradas: []
divisoes: []
fusoes: []
---

# 7.5 - Criando novos grupos de palavras-chave

## Contexto da aula

A aula mostra como incluir grupos novos em uma campanha da Rede de Pesquisa já em operação.
Parte da obtenção de ideias de palavras-chave e demonstra a duplicação de um grupo existente.
Também aborda a adaptação dos anúncios ao novo grupo e o acompanhamento após a publicação.
Palavras-chave negativas são citadas como assunto de uma aula anterior, sem nova explicação.

## Unidades

### U:d5fd0249c41087f6:001 — Alteração de lances foi a principal otimização do exemplo
```yaml
tipo: exemplo
plataforma: [google-search]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala
faixa: 00:00:00–00:00:41
perecivel: false
confianca: alta
versao: 1
```
Situação: uma campanha de Rede de Pesquisa já rodava havia algum tempo.
O que aconteceu: o custo por lead caiu da faixa de R$ 5 a R$ 6 para R$ 3,14.
Lógica: o professor atribui a principal queda à mudança de estratégia de lance e à otimização dos lances dos grupos de anúncio.

### U:d5fd0249c41087f6:002 — Consultar termos de pesquisa para obter ideias
```yaml
tipo: procedimento
plataforma: [google-search]
tema: palavras-chave
tarefas: [montar-lista-de-palavras-chave]
fonte: fala+pdf:cst_m04_a75_criando_novos_grupos_de_palavras_chave.pdf
faixa: 00:00:41–00:01:50
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: campanha com dados de termos de pesquisa.
1. No menu lateral, acesse palavras-chave ou termos de pesquisa.
2. Ordene por conversões para identificar o que mais converte.
3. Ordene por impressões para ver termos com maior volume de busca.
4. Escolha apenas termos para os quais você queira anunciar.

### U:d5fd0249c41087f6:003 — Buscar novas ideias além dos termos de pesquisa
```yaml
tipo: regra
plataforma: [google-search]
tema: palavras-chave
tarefas: [montar-lista-de-palavras-chave]
fonte: fala+pdf:cst_m04_a75_criando_novos_grupos_de_palavras_chave.pdf
faixa: 00:01:52–00:02:46
perecivel: false
confianca: alta
versao: 1
```
Volte à pesquisa de palavras-chave já feita e procure termos ainda não usados nas campanhas.
Use o Planejador de Palavras-chave, Answer the Public e reflexão própria para formar novas ideias de grupos.

### U:d5fd0249c41087f6:004 — Adicionar grupos gradualmente
```yaml
tipo: regua
plataforma: [google-search]
tema: estrutura-de-campanha
tarefas: [definir-estrutura-de-campanha]
fonte: fala
faixa: 00:02:46–00:03:17
condicoes: "ao expandir uma campanha com novos grupos"
perecivel: false
confianca: alta
versao: 1
```
Adicione 1 grupo de palavras-chave por vez, em ritmo de 1 por semana, e deixe a campanha rodar bem antes de incluir o próximo.
Não inclua 5 grupos de uma vez.

### U:d5fd0249c41087f6:005 — PDF recomenda no máximo dois grupos por inclusão
```yaml
tipo: fato-material
plataforma: [google-search]
tema: estrutura-de-campanha
tarefas: [definir-estrutura-de-campanha]
fonte: pdf:cst_m04_a75_criando_novos_grupos_de_palavras_chave.pdf
perecivel: false
confianca: alta
versao: 1
nota: "O PDF diz que dois grupos são suficientes; na fala, o professor recomenda adicionar um por vez."
```
Ao adicionar grupos de palavras-chave, o PDF orienta não inserir 5 grupos de uma vez e afirma que 2 grupos são suficientes.

### U:d5fd0249c41087f6:006 — Duplicar e adaptar um grupo existente
```yaml
tipo: procedimento
plataforma: [google-search]
tema: estrutura-de-campanha
tarefas: [replicar-campanhas-e-grupos]
fonte: fala+pdf:cst_m04_a75_criando_novos_grupos_de_palavras_chave.pdf
faixa: 00:03:17–00:04:54
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: ideias e lista de palavras-chave definidas para o novo grupo.
1. Na campanha desejada, abra grupos de anúncios, selecione um grupo existente, edite, copie e cole com Ctrl+V.
2. Edite o grupo duplicado e altere seu nome conforme a planilha de palavras-chave.
3. Dentro do novo grupo, selecione as palavras-chave existentes, edite e remova-as.
4. Use o ícone “+”, inclua as novas palavras-chave e salve.

### U:d5fd0249c41087f6:007 — Não anunciar uma promessa falsa
```yaml
tipo: regra
plataforma: [google-search]
tema: copy-e-roteiro
tarefas: [escrever-copy-e-roteiro]
fonte: fala
faixa: 00:04:57–00:06:11
perecivel: false
confianca: alta
versao: 1
```
Altere os anúncios para as novas palavras-chave, mas anuncie somente o que é verdade sobre a oferta.
Não use uma palavra-chave para prometer algo que você não ensina ou entrega.

### U:d5fd0249c41087f6:008 — Alterar pelo menos dois anúncios e testar outro sem mudança
```yaml
tipo: decisao
plataforma: [google-search]
tema: testes-e-experimentos
tarefas: [configurar-anuncio, rodar-testes-e-experimentos]
fonte: fala+pdf:cst_m04_a75_criando_novos_grupos_de_palavras_chave.pdf
faixa: 00:08:57–00:10:12
perecivel: true
confianca: alta
versao: 1
```
Quando adaptar anúncios ao novo grupo, altere pelo menos 2 anúncios para as novas palavras-chave.
Você pode deixar um anúncio sem alteração para testar se ele funciona tão bem quanto os alterados; o professor diz que o ideal é alterar tudo.

### U:d5fd0249c41087f6:009 — Monitorar o grupo novo conforme o período de otimização
```yaml
tipo: decisao
plataforma: [google-search]
tema: otimizacao
tarefas: [otimizar-palavras-chave]
fonte: fala+pdf:cst_m04_a75_criando_novos_grupos_de_palavras_chave.pdf
faixa: 00:09:35–00:10:12
perecivel: true
confianca: alta
versao: 1
```
Quando os anúncios estiverem rodando, monitore os resultados depois de alguns dias.
Volte para otimizar após 7, 5 ou 3 dias, conforme seu período de otimização.

### U:d5fd0249c41087f6:010 — Limitar a quantidade de grupos por campanha
```yaml
tipo: regua
plataforma: [google-search]
tema: estrutura-de-campanha
tarefas: [definir-estrutura-de-campanha]
fonte: fala+pdf:cst_m04_a75_criando_novos_grupos_de_palavras_chave.pdf
faixa: 00:10:12–00:10:37
perecivel: false
confianca: alta
versao: 1
```
Mantenha a campanha com no máximo 8 a 10 grupos de palavras-chave; 10 é o limite estourando.
Não fique com 50 grupos de palavras-chave.

### U:d5fd0249c41087f6:011 — Abrir espaço para uma ideia nova de grupo
```yaml
tipo: decisao
plataforma: [google-search]
tema: estrutura-de-campanha
tarefas: [definir-estrutura-de-campanha]
fonte: fala+pdf:cst_m04_a75_criando_novos_grupos_de_palavras_chave.pdf
faixa: 00:10:12–00:10:37
perecivel: false
confianca: alta
versao: 1
```
Se surgir mais de 10 ideias muito boas, pause um grupo que não está funcionando tão bem e teste a ideia nova.
Como alternativa, crie uma nova campanha para esse grupo de palavras-chave.