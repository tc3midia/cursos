---
type: unidades-aula
status: validado
title: "5.2 - Públicos Semelhantes"
modulo: "002"
ordem: 27
aula_id: 485b9655e438f86f
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

# 5.2 - Públicos Semelhantes

## Contexto da aula
A aula apresenta públicos semelhantes no Meta Ads depois dos públicos personalizados.
Explica a origem do público, a escolha de localização e as faixas percentuais de semelhança.
Demonstra a criação pela interface e diferencia fontes baseadas em valor de outras fontes.
Relaciona o público semelhante ao objetivo da campanha e mostra o mix de semelhantes para negócios locais.
Localização, idade, gênero, direcionamento detalhado e idiomas ficam para aulas posteriores.

## Unidades

### U:485b9655e438f86f:001 — Público semelhante encontra pessoas parecidas com um público base
```yaml
tipo: conceito
plataforma: [meta]
tema: publicos
tarefas: []
fonte: fala
faixa: "00:00:00–00:01:55"
perecivel: false
confianca: alta
versao: 1
```
O público semelhante reúne pessoas parecidas com um público personalizado dado como público base.
Diferente do público personalizado, essas pessoas não precisam ter tido contato com o anunciante.

### U:485b9655e438f86f:002 — Público semelhante aparece na lista de públicos personalizados
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-semelhantes]
fonte: fala
faixa: "00:00:29–00:01:14"
perecivel: true
confianca: alta
versao: 1
```
Na seleção de público do conjunto de anúncios, a mesma lista permite selecionar público personalizado e público semelhante.
O professor considera que a identificação ideal da lista seria “públicos personalizados e semelhantes”.

### U:485b9655e438f86f:003 — Criar semelhante selecionando a fonte
```yaml
tipo: procedimento
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-semelhantes]
fonte: fala
faixa: "00:01:55–00:03:15"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: existir uma fonte para formar o público semelhante.
1. Clique em criar público e escolha público semelhante.
2. Selecione a fonte do público.
3. Para outras fontes, escolha uma página ou um público personalizado, como envolvimento com Instagram nos últimos 14 dias.
4. Crie o público semelhante a partir da fonte escolhida.

### U:485b9655e438f86f:004 — Fonte baseada em valor serve para e-commerces
```yaml
tipo: decisao
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-semelhantes]
fonte: fala
faixa: "00:01:55–00:03:15"
condicoes: "quando a fonte for baseada em valor"
perecivel: true
confianca: alta
versao: 1
```
Quando a fonte for baseada em valor, use-a para e-commerces; ela pode usar pessoas que compraram produtos de um catálogo determinado.
O professor diz que, no uso mais comum, utiliza-se público de outras fontes.

### U:485b9655e438f86f:005 — Localização do público semelhante deve ser um país
```yaml
tipo: regra
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-semelhantes]
fonte: fala
faixa: "00:03:15–00:03:59"
perecivel: true
confianca: alta
versao: 1
```
Selecione um país como localização do público semelhante, como Brasil; não use estado, como São Paulo.

### U:485b9655e438f86f:006 — Percentual maior amplia o público e reduz a semelhança
```yaml
tipo: regua
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-semelhantes]
fonte: fala
faixa: "00:03:15–00:04:39"
condicoes: "na localização Brasil demonstrada"
perecivel: true
confianca: alta
versao: 1
```
O público semelhante pode ir de 1% a 10%; 1% é a faixa mais parecida com o público base.
No exemplo, 2% tem 3,5 milhões de pessoas e uma porcentagem maior chega a 5,2 milhões, com menos semelhança.
A cada percentual demonstrado, o público cresce cerca de 1,7 milhões de pessoas; esse número varia com o tempo.

### U:485b9655e438f86f:007 — Prefira semelhante de 1% e amplie em negócios locais
```yaml
tipo: decisao
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-semelhantes]
fonte: fala
faixa: "00:04:00–00:04:39"
condicoes: "para negócios locais em região específica"
perecivel: false
confianca: alta
versao: 1
```
Se o semelhante de 0% a 1% ficar muito pequeno para negócio local, teste 2%, 3%, 4% ou 5%.
Normalmente use o público de 1%; 10% é raro e destinado a quando se quer muita escala.

### U:485b9655e438f86f:008 — Testar fatias separadas pela técnica da cebola
```yaml
tipo: procedimento
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-semelhantes]
fonte: fala
faixa: "00:04:39–00:05:22"
perecivel: true
confianca: media
versao: 1
nota: "A fala primeiro informa faixa de 1% a 10% e depois nomeia fatias como 0 a 1 e 0 a 2."
```
Pré-condição: criar vários públicos semelhantes a partir da mesma fonte.
1. Crie faixas como 0 a 1, 1 a 2, 2 a 3, 3 a 4, 4 a 5 e 5 a 6.
2. Teste as fatias separadamente.
3. Compare qual delas funciona melhor.
O professor afirma ter quase certeza de que a primeira porcentagem funciona melhor.

### U:485b9655e438f86f:009 — Formar semelhante a partir do evento mais próximo do objetivo
```yaml
tipo: decisao
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-semelhantes]
fonte: fala
faixa: "00:05:22–00:06:45"
perecivel: false
confianca: alta
versao: 1
```
Se buscar vendas, crie semelhante de quem comprou; sem muitas compras, use quem iniciou finalização de compra ou adicionou ao carrinho.
Se buscar seguidores, engajamento, visualização de vídeo ou cadastros, use respectivamente quem seguiu, engajou, visualizou vídeo ou cadastrou.
Crie o semelhante mais próximo do objetivo buscado; para cadastros, também pode usar quem chegou à página de captura sem cadastrar.

### U:485b9655e438f86f:010 — Usar mix de semelhantes para negócios locais
```yaml
tipo: procedimento
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-semelhantes]
fonte: fala
faixa: "00:06:45–00:07:57"
condicoes: "para negócios locais anunciados em região, cidade ou bairro específicos"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: existirem vários públicos semelhantes adequados ao negócio local.
1. Entre no mesmo conjunto de anúncios.
2. Adicione semelhantes de quem comprou, engajou, visualizou vídeo e seguiu.
3. Mantenha os vários públicos semelhantes 1% no mesmo grupo de anúncio.
Isso é chamado de mix de semelhantes e é usado porque a região específica pode deixar o público pequeno.

### U:485b9655e438f86f:011 — Públicos personalizados são necessários para semelhantes
```yaml
tipo: regra
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-personalizados, montar-publicos-semelhantes]
fonte: fala
faixa: "00:07:18–00:07:57"
perecivel: false
confianca: alta
versao: 1
```
Domine e tenha públicos personalizados para poder criar públicos semelhantes.
Sem públicos personalizados, restam públicos de localização, idade, gênero, direcionamento detalhado e idiomas.

### U:485b9655e438f86f:012 — Segmentações restantes ficam para próximas aulas
```yaml
tipo: limite
plataforma: [meta]
tema: publicos
tarefas: []
fonte: fala
faixa: "00:07:18–00:07:57"
perecivel: false
confianca: alta
versao: 1
```
A aula não explica públicos de localização, idade, gênero, direcionamento detalhado e idiomas; eles serão tratados nas próximas aulas.