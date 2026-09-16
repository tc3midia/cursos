---
type: unidades-aula
status: validado
title: "6.7 - União e separação de públicos"
modulo: "002"
ordem: 37
aula_id: 9245e2a1486b5af5
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - transcricao.md
extraido_em: 2026-09-15
gerado_por: gpt-5.6-terra
retiradas: []
divisoes: []
fusoes: []
---

# 6.7 - União e separação de públicos

## Contexto da aula

A aula explica como organizar públicos entre conjuntos de anúncios e campanhas no Meta Ads.
Define estrutura de campanha como a distribuição de diferentes públicos entre campanhas e conjuntos.
Apresenta cinco princípios para separar e cinco para unir públicos em conjuntos.
Também compara a organização de campanhas por verba, nível de aquecimento e posicionamento.
O professor declara que as escolhas variam conforme negócio e situação, sem regra geral única.

## Unidades

### U:9245e2a1486b5af5:001 — Estrutura de campanha organiza públicos
```yaml
tipo: conceito
plataforma: [meta]
tema: estrutura-de-campanha
tarefas: []
fonte: fala
faixa: "00:01:14–00:02:32"
perecivel: false
confianca: alta
versao: 1
```
Estrutura de campanha é a forma de distribuir diferentes públicos entre uma ou mais campanhas e seus conjuntos de anúncios.
Separar públicos quentes e frios em campanhas distintas, ou criar uma campanha por público, são estruturas diferentes e afetam o resultado.

### U:9245e2a1486b5af5:002 — Não existe regra geral para unir ou separar públicos
```yaml
tipo: regra
plataforma: [meta]
tema: estrutura-de-campanha
tarefas: [definir-estrutura-de-campanha]
fonte: fala
faixa: "00:03:06–00:03:49"
perecivel: false
confianca: alta
versao: 1
```
Não adote “sempre separar” ou “sempre juntar” públicos: a decisão varia conforme o negócio e a situação.

### U:9245e2a1486b5af5:003 — Separe para posicionamentos com anúncios próprios
```yaml
tipo: decisao
plataforma: [meta]
tema: posicionamentos-e-formatos
tarefas: [definir-estrutura-de-campanha, escolher-canais-e-posicionamentos]
fonte: fala
faixa: "00:03:49–00:07:41"
perecivel: true
confianca: alta
versao: 1
```
Se houver posicionamentos diferentes com anúncios diferentes para cada posicionamento, deixe o mesmo público em conjuntos de anúncios separados.
Feed e Stories são posicionamentos distintos; a imagem quadrada adequada ao Feed pode ficar cortada nos Stories, onde pode ser escolhida outra imagem.
Para usar enquete no anúncio, isole o posicionamento Stories do Instagram.

### U:9245e2a1486b5af5:004 — Use edição de mídia para anúncios específicos por posicionamento
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: posicionamentos-e-formatos
tarefas: [configurar-anuncio]
fonte: fala
faixa: "00:05:44–00:07:41"
perecivel: true
confianca: alta
versao: 1
```
Na configuração do anúncio, selecione a imagem do Feed e use “editar” para definir a imagem dos Stories.
Use a opção de edição quando houver anúncios específicos para os posicionamentos.

### U:9245e2a1486b5af5:005 — Separe para garantir gasto ou analisar cada público
```yaml
tipo: decisao
plataforma: [meta]
tema: publicos
tarefas: [definir-estrutura-de-campanha, organizar-hierarquia-e-exclusao-de-publicos]
fonte: fala
faixa: "00:07:41–00:09:52"
perecivel: false
confianca: alta
versao: 1
```
Se quiser garantir gasto em determinado público ou analisar seus resultados isoladamente, coloque cada público em um conjunto de anúncios.
Quando dois públicos estão unidos, o Meta pode direcionar a verba a apenas um deles e não mostra seus resultados separadamente no Meta Ads.

### U:9245e2a1486b5af5:006 — Separe públicos com aquecimento muito diferente
```yaml
tipo: decisao
plataforma: [meta]
tema: publicos
tarefas: [definir-estrutura-de-campanha, organizar-hierarquia-e-exclusao-de-publicos]
fonte: fala
faixa: "00:09:52–00:11:10"
perecivel: false
confianca: alta
versao: 1
```
Se os públicos tiverem níveis de aquecimento muito diferentes, separe-os em conjuntos de anúncios.
Quem adicionou ao carrinho nos últimos 3 dias tem mais chance de comprar do que quem se envolveu há 365 dias; não misture público quente com lookalike de 1%.

### U:9245e2a1486b5af5:007 — Separe quando o anúncio fala para um público específico
```yaml
tipo: decisao
plataforma: [meta]
tema: publicos
tarefas: [definir-estrutura-de-campanha, configurar-anuncio]
fonte: fala
faixa: "00:11:11–00:12:23"
perecivel: false
confianca: alta
versao: 1
```
Se houver anúncio específico para determinado público, isole esse público em seu próprio conjunto de anúncios.
O anúncio pode abordar diretamente quem visitou a página de cadastro sem se cadastrar ou quem adicionou produto ao carrinho sem concluir a compra.

### U:9245e2a1486b5af5:008 — Una públicos quando a verba for muito pequena
```yaml
tipo: decisao
plataforma: [meta]
tema: orcamento
tarefas: [definir-orcamento, definir-estrutura-de-campanha]
fonte: fala
faixa: "00:12:24–00:14:03"
perecivel: false
confianca: alta
versao: 1
```
Se a verba for muito pequena, una públicos para reduzir a quantidade de conjuntos de anúncios.
Com R$18,00 por dia, o professor limita a campanha a no máximo 3 conjuntos, mantendo média de R$6,00 por conjunto.

### U:9245e2a1486b5af5:009 — Una públicos quando a segmentação for pequena
```yaml
tipo: decisao
plataforma: [meta]
tema: publicos
tarefas: [definir-estrutura-de-campanha, diagnosticar-campanha-sem-gasto]
fonte: fala
faixa: "00:14:03–00:15:08"
perecivel: false
confianca: alta
versao: 1
```
Se a segmentação for muito pequena, una públicos para aumentar a chance de o conjunto gastar dinheiro.
Exemplo: combinar envolvimento de 1 dia e adicionou ao carrinho quando o perfil tem 200 seguidores e o site ainda não chegou a 100 visitas.

### U:9245e2a1486b5af5:010 — Una públicos muito parecidos, salvo necessidade de isolá-los
```yaml
tipo: decisao
plataforma: [meta]
tema: publicos
tarefas: [definir-estrutura-de-campanha, organizar-hierarquia-e-exclusao-de-publicos]
fonte: fala
faixa: "00:15:08–00:17:05"
perecivel: false
confianca: alta
versao: 1
```
Se os públicos forem muito parecidos, una-os, desde que não queira garantir gasto, analisá-los isoladamente, comparar aquecimento ou usar anúncio específico.
Envolvimento no Facebook e Instagram, listas de quem baixou e-book 1 e 2, ou públicos que quase converteram são exemplos de públicos semelhantes.
Para testar dois lookalikes um contra o outro ou analisá-los isoladamente, separe-os.

### U:9245e2a1486b5af5:011 — Una conjuntos que não estão gastando dinheiro
```yaml
tipo: decisao
plataforma: [meta]
tema: otimizacao
tarefas: [diagnosticar-campanha-sem-gasto, otimizar-publicos-e-segmentacoes]
fonte: fala
faixa: "00:17:05–00:19:50"
perecivel: false
confianca: alta
versao: 1
```
Se conjuntos de anúncios não estiverem gastando dinheiro, una seus públicos, pois a segmentação pode estar pequena.
O professor chama a alternância entre unir e separar de técnica da sanfona.

### U:9245e2a1486b5af5:012 — Defina gasto mínimo em conjunto de campanha CBO
```yaml
tipo: procedimento
plataforma: [meta]
tema: orcamento
tarefas: [definir-orcamento, diagnosticar-campanha-sem-gasto]
fonte: fala
faixa: "00:17:41–00:19:03"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: campanha configurada como CBO e conjunto de anúncios que não está gastando dinheiro.
1. Abra a edição do conjunto de anúncios na campanha CBO.
2. Vá em “mais opções” e abra “limite de gasto”.
3. Adicione um mínimo de gasto para o conjunto.

### U:9245e2a1486b5af5:013 — Alternativas para controlar gasto por conjunto
```yaml
tipo: decisao
plataforma: [meta]
tema: orcamento
tarefas: [definir-orcamento, diagnosticar-campanha-sem-gasto]
fonte: fala
faixa: "00:17:53–00:19:50"
perecivel: true
confianca: alta
versao: 1
```
Se quiser forçar o gasto de um conjunto, use CBO com mínimo de gasto, use ABO para colocar a verba no conjunto ou separe conjuntos em campanhas diferentes.
Separar em campanhas pode ainda não fazer a campanha gastar; unir diferentes grupos é outra opção quando os públicos são pequenos.

### U:9245e2a1486b5af5:014 — Una grupos para respeitar o limite de anúncios por página
```yaml
tipo: decisao
plataforma: [meta]
tema: estrutura-de-campanha
tarefas: [definir-estrutura-de-campanha]
fonte: fala
faixa: "00:19:03–00:21:11"
perecivel: false
confianca: alta
versao: 1
```
Se atingir o limite de anúncios por página do Facebook, una grupos de anúncios que repetem os mesmos anúncios.
No exemplo, 8 grupos com 5 anúncios cada somam 40 anúncios; ao unir dois grupos, ficam 7 grupos e 35 anúncios, dentro dos 35 restantes informados pelo Meta.

### U:9245e2a1486b5af5:015 — Mantenha poucos conjuntos de anúncios
```yaml
tipo: regua
plataforma: [meta]
tema: estrutura-de-campanha
tarefas: [definir-estrutura-de-campanha]
fonte: fala
faixa: "00:21:52–00:23:10"
perecivel: false
confianca: alta
versao: 1
```
O professor tenta manter 8 conjuntos de anúncios, no máximo 12; 4 é um número muito bom e ele procura ter mais de 1.
Se a campanha tiver 20 conjuntos, recomenda cortar alguns e unir públicos que puderem ser unidos.

### U:9245e2a1486b5af5:016 — Com pouquíssima verba, faça uma campanha só
```yaml
tipo: decisao
plataforma: [meta]
tema: estrutura-de-campanha
tarefas: [definir-estrutura-de-campanha, definir-orcamento]
fonte: fala
faixa: "00:23:11–00:24:04"
perecivel: false
confianca: alta
versao: 1
```
Se tiver pouquíssima verba, faça uma única campanha e controle os gastos por mínimos e máximos ou por ABO.

### U:9245e2a1486b5af5:017 — Separe campanhas por nível de aquecimento
```yaml
tipo: decisao
plataforma: [meta]
tema: estrutura-de-campanha
tarefas: [definir-estrutura-de-campanha, organizar-hierarquia-e-exclusao-de-publicos]
fonte: fala
faixa: "00:23:11–00:25:47"
perecivel: false
confianca: alta
versao: 1
```
Se não tiver pouquíssima verba, prefira separar campanhas por nível de aquecimento: público frio, morno e quente, ou apenas frio e quente.
O professor indica principalmente a divisão entre frio e quente para 99% dos anunciantes: públicos personalizados representam quem já teve contato; semelhantes e direcionamento detalhado representam quem não teve contato.

### U:9245e2a1486b5af5:018 — Público morno interagiu há mais de 60 dias
```yaml
tipo: conceito
plataforma: [meta]
tema: publicos
tarefas: []
fonte: fala
faixa: "00:24:04–00:25:47"
perecivel: false
confianca: alta
versao: 1
```
Público morno é formado por pessoas que interagiram com você há mais de 60 dias.

### U:9245e2a1486b5af5:019 — Campanhas podem ser separadas por posicionamento
```yaml
tipo: decisao
plataforma: [meta]
tema: posicionamentos-e-formatos
tarefas: [definir-estrutura-de-campanha, escolher-canais-e-posicionamentos]
fonte: fala
faixa: "00:25:49–00:27:37"
perecivel: true
confianca: alta
versao: 1
```
Se houver posicionamentos diferentes, você pode separá-los em campanhas, como campanhas de posicionamento automático, Stories ou Reels.
O professor apresenta isso como exemplo sujeito a testes constantes, não como configuração obrigatória para todo negócio.

### U:9245e2a1486b5af5:020 — Decida pela combinação dos fatores de união e separação
```yaml
tipo: regra
plataforma: [meta]
tema: estrutura-de-campanha
tarefas: [definir-estrutura-de-campanha]
fonte: fala
faixa: "00:27:37–00:29:14"
perecivel: false
confianca: alta
versao: 1
```
Ao decidir quantos conjuntos criar, responda “depende” e avalie os fatores para unir ou separar públicos.
A decisão se torna natural com disciplina, dedicação e implementação prática.