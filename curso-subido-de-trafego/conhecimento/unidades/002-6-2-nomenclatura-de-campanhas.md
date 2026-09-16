---
type: unidades-aula
status: validado
title: "6.2 - Nomenclatura de campanhas"
modulo: "002"
ordem: 32
aula_id: f5fd46cdb63a8963
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

# 6.2 - Nomenclatura de campanhas

## Contexto da aula
A aula apresenta um padrão de nomenclatura para campanha, grupo de anúncios e anúncio no Meta Ads.
Parte da escolha do objetivo da campanha e mostra como os nomes facilitam filtros e leitura de dados.
O professor defende consistência no padrão, mesmo quando existirem formas alternativas de separar informações.
Também demonstra campos e exemplos de nomes, deixando a explicação do grau de exclusão para aulas seguintes.

## Unidades

### U:f5fd46cdb63a8963:001 — Nomeie a campanha mesmo que o campo seja opcional
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: nomenclatura
tarefas: [nomear-campanhas]
fonte: fala
faixa: "00:00:00–00:00:36"
perecivel: true
confianca: alta
versao: 1
```
Ao criar a campanha, use a opção de dar nome à campanha mesmo sendo opcional. Nomeie também o conjunto de anúncios e o anúncio para permitir filtros pelos respectivos nomes.

### U:f5fd46cdb63a8963:002 — Deixe os dados a no máximo dois filtros
```yaml
tipo: regua
plataforma: [meta]
tema: nomenclatura
tarefas: [nomear-campanhas, ler-metricas-e-relatorios]
fonte: fala
faixa: "00:00:36–00:01:55"
condicoes: "o padrão de nomes deve permitir identificar campanhas e finalidades por filtros"
perecivel: false
confianca: alta
versao: 1
```
Organize os nomes para que os dados e resultados estejam a um ou dois filtros de distância, no máximo.

### U:f5fd46cdb63a8963:003 — Use nomes para separar gastos por finalidade
```yaml
tipo: exemplo
plataforma: [meta]
tema: nomenclatura
tarefas: [nomear-campanhas, ler-metricas-e-relatorios]
fonte: fala
faixa: "00:00:36–00:01:15"
perecivel: true
confianca: alta
versao: 1
```
Situação: havia 62 campanhas de um evento identificado pela sigla SG1, com R$ 1 milhão gasto no total.
O que aconteceu: ao filtrar o nome pela finalidade de captação, o painel mostrou R$ 970 mil gastos nessas campanhas.
Lógica: uma sigla e termos de finalidade no nome permitem isolar gastos de captação ou de lembrete.

### U:f5fd46cdb63a8963:004 — Padronização ajuda a análise e a otimização
```yaml
tipo: regra
plataforma: [meta]
tema: nomenclatura
tarefas: [nomear-campanhas, ler-metricas-e-relatorios]
fonte: fala
faixa: "00:01:15–00:02:33"
perecivel: false
confianca: alta
versao: 3
nota: "Classificação por gpt-5.6-sol: proposta `otimizar-campanhas` recusada; `nomear-campanhas` e `ler-metricas-e-relatorios` cobrem a orientação."
```
Use um padrão nos nomes de campanhas, conjuntos, grupos e anúncios para localizar dados mais rápido, visualizar a conta com clareza e tomar ações de otimização.

### U:f5fd46cdb63a8963:005 — Nome organizado não reduz custo por si só
```yaml
tipo: limite
plataforma: [meta]
tema: nomenclatura
tarefas: []
fonte: fala
faixa: "00:01:55–00:02:33"
perecivel: false
confianca: alta
versao: 1
```
Trocar somente o nome não torna o lead mais barato, não faz a campanha vender mais e não gera mais mensagens.

### U:f5fd46cdb63a8963:006 — Escolha colchetes ou underline como separador
```yaml
tipo: decisao
plataforma: [meta]
tema: nomenclatura
tarefas: [nomear-campanhas]
fonte: fala
faixa: "00:02:33–00:03:15"
perecivel: false
confianca: alta
versao: 1
```
Se for separar informações no nome, use colchetes ou underline; o professor considera parênteses horrorosos.

### U:f5fd46cdb63a8963:007 — Priorize repetir um padrão de nomenclatura
```yaml
tipo: regra
plataforma: [meta]
tema: nomenclatura
tarefas: [nomear-campanhas]
fonte: fala
faixa: "00:03:15–00:04:00"
perecivel: false
confianca: alta
versao: 1
```
Mais importante que escolher uma nomenclatura considerada boa é usar sempre o mesmo padrão, com informações que permitam entender a campanha ao bater o olho.

### U:f5fd46cdb63a8963:008 — Comece o nome pelo evento ou campanha de publicidade
```yaml
tipo: regra
plataforma: [meta]
tema: nomenclatura
tarefas: [nomear-campanhas]
fonte: fala
faixa: "00:04:00–00:04:42"
perecivel: false
confianca: alta
versao: 1
```
Coloque no início o identificador da campanha de publicidade ou evento, como DGT, SGT1, SGT2, SG1 ou S1; isso permite localizar suas campanhas com filtros.

### U:f5fd46cdb63a8963:009 — Estruture o nome da campanha com informações de leitura
```yaml
tipo: procedimento
plataforma: [meta]
tema: nomenclatura
tarefas: [nomear-campanhas]
fonte: fala
faixa: "00:04:42–00:06:23"
perecivel: false
confianca: alta
versao: 1
```
Pré-condição: ter definido a campanha ou evento que será divulgado.
1. Informe a campanha ou evento e, em seguida, o objetivo.
2. Inclua, quando fizer sentido, o posicionamento e o nível de aquecimento do público.
3. Finalize com uma breve descrição, como captação ou captação de leads.
4. Desenvolva o padrão conforme o negócio, mantendo as informações legíveis no nome.

### U:f5fd46cdb63a8963:010 — Use uma única palavra para cada classificação
```yaml
tipo: regra
plataforma: [meta]
tema: nomenclatura
tarefas: [nomear-campanhas]
fonte: fala
faixa: "00:06:57–00:08:21"
perecivel: false
confianca: alta
versao: 1
```
Após definir o padrão, mantenha os mesmos termos: se a classificação escolhida for “cadastro”, não alterne com “cadastros”.

### U:f5fd46cdb63a8963:011 — Categorize posicionamento e aquecimento no nome da campanha
```yaml
tipo: conceito
plataforma: [meta]
tema: nomenclatura
tarefas: [nomear-campanhas]
fonte: fala
faixa: "00:06:57–00:08:21"
perecivel: false
confianca: alta
versao: 1
```
No padrão apresentado, o posicionamento pode ser automático, Stories, Stories e Reels ou somente Reels. O público é classificado como quente, frio, morno ou amplo.

### U:f5fd46cdb63a8963:012 — Inclua idade somente se fizer parte do padrão
```yaml
tipo: decisao
plataforma: [meta]
tema: nomenclatura
tarefas: [nomear-campanhas]
fonte: fala
faixa: "00:06:26–00:08:21"
perecivel: false
confianca: alta
versao: 1
```
Se o padrão do negócio incluir variações de idade, coloque a idade no nome; depois de definido, mantenha essa convenção.

### U:f5fd46cdb63a8963:013 — Nomeie o grupo pelo grau de exclusão e público
```yaml
tipo: procedimento
plataforma: [meta]
tema: nomenclatura
tarefas: [nomear-campanhas]
fonte: fala
faixa: "00:07:39–00:09:35"
perecivel: false
confianca: alta
versao: 1
```
Pré-condição: ter definido o público, posicionamento e nível de aquecimento do grupo de anúncios.
1. Comece com o grau ou fator de exclusão, representado por X seguido de um número.
2. Acrescente espaço, tracinho, espaço e o posicionamento.
3. Repita o nível de aquecimento do público.
4. Termine com o nome do público.

### U:f5fd46cdb63a8963:014 — Grau de exclusão costuma ficar entre 0 e 10 ou 20
```yaml
tipo: regua
plataforma: [meta]
tema: nomenclatura
tarefas: [nomear-campanhas]
fonte: fala
faixa: "00:08:21–00:08:57"
perecivel: false
confianca: alta
versao: 1
```
O grau de exclusão é um X seguido de número, que pode variar de 0,0 ao infinito, mas normalmente fica em torno de 10 ou 20.

### U:f5fd46cdb63a8963:015 — Use AD e numeração para identificar o anúncio
```yaml
tipo: procedimento
plataforma: [meta]
tema: nomenclatura
tarefas: [nomear-campanhas]
fonte: fala
faixa: "00:09:35–00:10:28"
perecivel: false
confianca: alta
versao: 1
```
Pré-condição: existir uma identificação sequencial para os anúncios da campanha.
1. Comece o nome com AD, abreviação de anúncio em inglês.
2. Acrescente uma numeração sequencial, que pode ultrapassar 100 anúncios, como AD006 ou AD123.
3. Use espaço, tracinho, espaço.
4. Inclua uma identificação e uma breve descrição do anúncio.

### U:f5fd46cdb63a8963:016 — Faça a identificação do anúncio ser explicável pela equipe
```yaml
tipo: regra
plataforma: [meta]
tema: nomenclatura
tarefas: [nomear-campanhas]
fonte: fala
faixa: "00:10:28–00:11:04"
perecivel: false
confianca: alta
versao: 1
```
A identificação do anúncio não precisa ser compreendida por todos de imediato, mas os gestores que trabalham na conta devem saber explicá-la de forma simples para quem chegar.

### U:f5fd46cdb63a8963:017 — Relacione o nome do anúncio ao arquivo quando necessário
```yaml
tipo: exemplo
plataforma: [meta]
tema: nomenclatura
tarefas: [nomear-campanhas]
fonte: fala
faixa: "00:10:28–00:11:04"
perecivel: false
confianca: alta
versao: 1
```
Situação: um anúncio tinha a identificação V02L035 e a descrição “5 profissões”.
O que aconteceu: a identificação correspondia ao vídeo 2 do lote 3 e permitia encontrar o arquivo na pasta de anúncios.
Lógica: use uma identificação ligada ao arquivo e uma descrição breve para esclarecer o que é o anúncio.

### U:f5fd46cdb63a8963:018 — Não deixe o nome automático de anúncio duplicado
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: nomenclatura
tarefas: [nomear-campanhas, replicar-campanhas-e-grupos]
fonte: fala
faixa: "00:11:04–00:11:51"
perecivel: true
confianca: alta
versao: 1
```
Quando duplicar um anúncio, não mantenha o sufixo automático “- cópia” no nome. Renomeie-o dentro do padrão para conseguir se localizar na conta.

### U:f5fd46cdb63a8963:019 — Leia a estrutura completa para situar a campanha
```yaml
tipo: exemplo
plataforma: [meta]
tema: nomenclatura
tarefas: [nomear-campanhas, ler-metricas-e-relatorios]
fonte: fala
faixa: "00:11:54–00:12:33"
perecivel: false
confianca: alta
versao: 1
```
Situação: uma campanha contém um conjunto de anúncios e, dentro dele, um anúncio com nomes padronizados.
O que aconteceu: a leitura dos três nomes permite situar a campanha, entender sua função e identificar que tipo de métrica analisar.
Lógica: a nomenclatura hierárquica concentra informações operacionais para leitura rápida.
