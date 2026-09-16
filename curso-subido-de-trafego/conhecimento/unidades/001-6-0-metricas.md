---
type: unidades-aula
status: validado
title: "6.0 - Métricas"
modulo: "001"
ordem: 7
aula_id: d33f0baf66274a3d
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - cst_m01_a06_metricas.pdf
  - transcricao.md
fontes_ignoradas:
  - Mapa Mental.txt: contém apenas o endereço do mapa mental, sem texto aproveitável
extraido_em: 2026-09-14
gerado_por: opus-5
retiradas: []
divisoes: []
fusoes: []
---

# 6.0 - Métricas

## Contexto da aula

Aula de reforço sobre métricas para quem já passou pelo ABC do tráfego. O professor divide o assunto em duas partes: primeiro o par métrica principal e métricas secundárias, que ele apresenta como a chave para parar de se perder no painel; depois um passeio pelas métricas que todo anunciante deveria reconhecer, com fórmula e leitura de cada uma.
Assume que o aluno já ouviu falar de lead, impressão e clique, e que já sabe que existe pixel; não ensina a instalar nada nem a mexer no gerenciador.
Toda demonstração de tela é feita no gerenciador do Meta, com a afirmação repetida de que o Google Ads funciona igual nesses pontos.
Não é uma aula de otimização: ela explica o que cada número significa e qual deles decide se a campanha deu certo, sem entrar em ajuste de campanha.
Etapas específicas de e-commerce e a lista completa de métricas ficam declaradamente para outras aulas e para a prática.

## Unidades

### U:d33f0baf66274a3d:001 — Dois tipos de métrica: principal e secundária
```yaml
tipo: conceito
plataforma: [geral]
tema: metricas-e-relatorios
tarefas: []
fonte: "fala+pdf:cst_m01_a06_metricas.pdf"
faixa: "00:00:00–00:01:20"
perecivel: false
confianca: alta
versao: 1
```
Existem dois tipos de métrica: a principal e as secundárias.
A métrica principal é uma só e define o sucesso ou o fracasso da campanha; as secundárias são todas as outras que influenciam esse resultado.
Quem diz que tem dificuldade em analisar métricas costuma ser quem ainda não separou os dois tipos.

### U:d33f0baf66274a3d:002 — A campanha é julgada por uma única métrica
```yaml
tipo: regra
plataforma: [geral]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios, definir-conversoes-e-metas]
fonte: fala
faixa: "00:01:20–00:01:55"
perecivel: false
confianca: alta
versao: 1
```
Escolha uma única métrica para dizer se a campanha deu certo ou não; não podem ser quinze.
O painel mostra centenas de números, mas só um deles decide o veredito da campanha.

### U:d33f0baf66274a3d:003 — Explicação da métrica aparece ao passar o mouse nas colunas
```yaml
tipo: alerta-ui
plataforma: [meta, google]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: "fala+pdf:cst_m01_a06_metricas.pdf"
faixa: "00:01:56–00:03:12"
perecivel: true
confianca: alta
versao: 1
```
Abra as colunas do gerenciador, escolha personalizar métricas e passe o mouse sobre o nome de qualquer métrica: aparece um painel com a definição dela.
Clicando em ver mais, a explicação fica mais detalhada, com a descrição de como o número é apurado.
O recurso existe nos dois gerenciadores, e o professor observa que pouca gente usa.

### U:d33f0baf66274a3d:004 — Método fuça e clica no gerenciador
```yaml
tipo: regra
plataforma: [meta, google]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: "fala+pdf:cst_m01_a06_metricas.pdf"
faixa: "00:03:13–00:03:30"
perecivel: false
confianca: alta
versao: 1
```
Entre no gerenciador periodicamente e vasculhe as métricas disponíveis para descobrir quais servem à sua estratégia.
O professor chama isso de fuça e clica: o painel explica cada métrica para quem se dá ao trabalho de mexer.

### U:d33f0baf66274a3d:005 — A métrica principal vem do objetivo da campanha
```yaml
tipo: regra
plataforma: [geral]
tema: metricas-e-relatorios
tarefas: [definir-conversoes-e-metas, escolher-objetivo-de-campanha]
fonte: "fala+pdf:cst_m01_a06_metricas.pdf"
faixa: "00:03:30–00:04:05"
perecivel: false
confianca: alta
versao: 1
```
Derive a métrica principal do objetivo: campanha de venda tem venda como métrica principal, campanha de engajamento tem engajamento, campanha de seguidores tem seguidores.
A relação entre objetivo e métrica principal é direta, sem exceção declarada na aula.

### U:d33f0baf66274a3d:006 — Métrica principal é sempre quantidade mais custo
```yaml
tipo: regra
plataforma: [geral]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios, definir-conversoes-e-metas]
fonte: "fala+pdf:cst_m01_a06_metricas.pdf"
faixa: "00:03:59–00:04:55"
perecivel: false
confianca: alta
versao: 1
nota: "O professor avisa de passagem que CPM já é custo por mil impressões, por isso custo por mensagem não recebe essa sigla."
```
Leia a métrica principal sempre em par: a quantidade e o custo daquela ação.
Se a principal é lead, o par é lead e custo por lead (CPL ou CPA); se é mensagem, é número de mensagens e custo por mensagem; se é seguidor, é seguidores e custo por seguidor.

### U:d33f0baf66274a3d:007 — Pixel só entra em site que é seu
```yaml
tipo: regra
plataforma: [geral]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos, definir-conversoes-e-metas]
fonte: "fala+pdf:cst_m01_a06_metricas.pdf"
faixa: "00:05:24–00:06:03"
perecivel: false
confianca: alta
versao: 1
```
Você só instala pixel e API de conversões onde tem acesso ao código: o seu próprio domínio.
Não dá para instalar pixel dentro de aplicativo de terceiro nem no site do concorrente, porque eles não são seus.
Tudo o que acontece fora do seu domínio fica sem medição.

### U:d33f0baf66274a3d:008 — Quando a conversão final não é mensurável, suba um passo no funil
```yaml
tipo: decisao
plataforma: [geral]
tema: metricas-e-relatorios
tarefas: [definir-conversoes-e-metas, ler-metricas-e-relatorios]
fonte: "fala+pdf:cst_m01_a06_metricas.pdf"
faixa: "00:06:04–00:07:55"
perecivel: false
confianca: alta
versao: 1
```
Quando a ação que você realmente quer acontece fora do seu alcance de medição, adote como métrica principal a última etapa do caminho que você consegue medir.
A métrica principal depende de duas coisas ao mesmo tempo: o que você busca e o que consegue medir.

### U:d33f0baf66274a3d:009 — Campanha de mensagem quando a venda fecha no WhatsApp
```yaml
tipo: exemplo
plataforma: [meta]
tema: metricas-e-relatorios
tarefas: [definir-conversoes-e-metas, escolher-objetivo-de-campanha]
fonte: "fala+pdf:cst_m01_a06_metricas.pdf"
faixa: "00:05:24–00:07:55"
perecivel: false
confianca: alta
versao: 1
```
Situação: o anunciante quer pedidos fechados no WhatsApp, mas não pode instalar pixel dentro do aplicativo.
O que aconteceu: o caminho do usuário tem cinco passos (ver o anúncio, clicar, abrir o site, abrir o WhatsApp, fazer o pedido) e o pixel mede os quatro primeiros; o pedido, não.
Lógica: a campanha é criada com objetivo de mensagens e a métrica principal passa a ser quem abriu o WhatsApp, a última etapa mensurável, mesmo que a finalidade do negócio seja vender.

### U:d33f0baf66274a3d:010 — Métricas secundárias são as etapas anteriores à principal
```yaml
tipo: conceito
plataforma: [geral]
tema: metricas-e-relatorios
tarefas: []
fonte: "fala+pdf:cst_m01_a06_metricas.pdf"
faixa: "00:07:55–00:08:39"
perecivel: false
confianca: alta
versao: 1
```
Secundárias são as métricas das etapas que vêm antes da principal no caminho do usuário e que afetam o resultado dela.
Na sequência de impressão, clique e abertura da página, as secundárias correspondentes são CPM, CPC e CTR, e o custo por visualização da página de destino.

### U:d33f0baf66274a3d:011 — O funil é o caminho do usuário até o objetivo
```yaml
tipo: conceito
plataforma: [geral]
tema: metricas-e-relatorios
tarefas: []
fonte: fala
faixa: "00:08:39–00:09:22"
perecivel: false
confianca: alta
versao: 1
```
Funil é a sequência de etapas por onde a pessoa passa até chegar ao objetivo final, e cada etapa tem a sua métrica.
Num comércio eletrônico o caminho vai de impressão para clique, sessão no site, visualização do produto, adição ao carrinho, início de finalização de compra e compra.
Quando todas as etapas são mensuráveis, a compra costuma ser a métrica principal e as demais viram secundárias.

### U:d33f0baf66274a3d:012 — Não julgue a campanha por métrica secundária
```yaml
tipo: regra
plataforma: [geral]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: "fala+pdf:cst_m01_a06_metricas.pdf"
faixa: "00:09:24–00:10:10"
perecivel: false
confianca: alta
versao: 1
```
O erro mais comum do gestor é tratar métrica secundária como se ela definisse sucesso ou fracasso.
Secundária afeta a principal, mas não decide o veredito da campanha; só a principal decide.

### U:d33f0baf66274a3d:013 — CTR de 0,5% com R$ 500 por dia gerando R$ 5 mil
```yaml
tipo: exemplo
plataforma: [geral]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: fala
faixa: "00:10:10–00:11:26"
perecivel: false
confianca: alta
versao: 1
```
Situação: o gestor diz que a campanha está ruim porque o CTR ficou em 0,5%, abaixo do 1% que alguém lhe apresentou como referência.
O que aconteceu: ao ser perguntado, ele informa que gasta R$ 500 por dia e gera R$ 5 mil em vendas por dia, e admite que a campanha está boa.
Lógica: o CTR baixo aponta uma métrica secundária com espaço de melhoria, não uma campanha ruim; o julgamento fica com a métrica principal.

### U:d33f0baf66274a3d:014 — Melhorar uma secundária tende a puxar o resto
```yaml
tipo: conceito
plataforma: [geral]
tema: metricas-e-relatorios
tarefas: []
fonte: "fala+pdf:cst_m01_a06_metricas.pdf"
faixa: "00:10:48–00:11:26"
perecivel: false
confianca: alta
versao: 1
```
Uma métrica secundária fraca marca um ponto da campanha que pode melhorar, e ao melhorá-la o restante do funil tende a melhorar junto.
Isso não transforma a secundária em critério de sucesso: ela continua sendo influência, não veredito.

### U:d33f0baf66274a3d:015 — O que dá para medir depende de onde o pixel está
```yaml
tipo: regra
plataforma: [geral]
tema: pixel-e-eventos
tarefas: [definir-conversoes-e-metas, instalar-pixel-e-eventos]
fonte: "fala+pdf:cst_m01_a06_metricas.pdf"
faixa: "00:11:26–00:12:01"
perecivel: false
confianca: alta
versao: 1
```
Antes de escolher a métrica principal, liste o que o pixel instalado permite acompanhar dentro do seu site.
Quando o usuário sai do seu domínio para um aplicativo ou ferramenta de terceiro, a ação dele lá dentro deixa de ser medida.

### U:d33f0baf66274a3d:016 — Não tente decorar as métricas
```yaml
tipo: regra
plataforma: [geral]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: "fala+pdf:cst_m01_a06_metricas.pdf"
faixa: "00:12:01–00:12:36"
perecivel: false
confianca: alta
versao: 1
```
Existem centenas, talvez milhares de métricas nos gerenciadores, e não é para decorar nem para percorrer uma a uma.
Aprenda o conjunto principal e ganhe familiaridade com as demais pelo uso, no campo de batalha das campanhas.

### U:d33f0baf66274a3d:017 — Leads e CPA ou CPL
```yaml
tipo: conceito
plataforma: [geral]
tema: metricas-e-relatorios
tarefas: []
fonte: "fala+pdf:cst_m01_a06_metricas.pdf"
faixa: "00:12:36–00:13:20"
perecivel: false
confianca: alta
versao: 1
```
Lead é a pessoa que demonstrou interesse no que você divulga e entregou um canal de contato, seja no seu site, seja em formulário dentro da própria fonte de tráfego.
O custo por lead aparece como CPL ou CPA.

### U:d33f0baf66274a3d:018 — Mensagens iniciadas e custo por mensagem
```yaml
tipo: conceito
plataforma: [geral]
tema: metricas-e-relatorios
tarefas: []
fonte: "fala+pdf:cst_m01_a06_metricas.pdf"
faixa: "00:13:17–00:13:46"
perecivel: false
confianca: alta
versao: 1
```
Mensagem iniciada é a pessoa que abriu uma conversa com o anunciante, seja por WhatsApp, Direct ou Messenger.
O par dessa métrica é o custo por cada uma dessas conversas.

### U:d33f0baf66274a3d:019 — Impressões, alcance e frequência
```yaml
tipo: conceito
plataforma: [geral]
tema: metricas-e-relatorios
tarefas: []
fonte: "fala+pdf:cst_m01_a06_metricas.pdf"
faixa: "00:13:46–00:15:00"
perecivel: false
confianca: alta
versao: 1
```
Impressão conta quantas vezes o anúncio apareceu; alcance conta para quantas pessoas ele apareceu.
Se o anúncio apareceu cinco vezes para duas pessoas diferentes, são dez impressões e dois de alcance.
Frequência é a relação entre impressões e alcance, ou seja, quantas vezes em média cada pessoa viu o anúncio.

### U:d33f0baf66274a3d:020 — Cálculo do CPM
```yaml
tipo: regua
plataforma: [geral]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: "fala+pdf:cst_m01_a06_metricas.pdf"
faixa: "00:14:00–00:15:45"
perecivel: false
confianca: alta
versao: 1
```
CPM é o custo por mil impressões: custo vezes 1000 dividido pelo número de impressões.
A fonte de tráfego já calcula e exibe o CPM na coluna correspondente, mas saber a conta ajuda a ler o número.

### U:d33f0baf66274a3d:021 — Cálculo da frequência
```yaml
tipo: conceito
plataforma: [geral]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: fala
faixa: "00:15:00–00:15:45"
perecivel: false
confianca: alta
versao: 2
```
Frequência é impressões dividido por alcance.
Assim como o CPM, ela vem calculada pela fonte de tráfego; basta acrescentar a coluna ao relatório.

### U:d33f0baf66274a3d:022 — Cliques no link e cliques em todos
```yaml
tipo: conceito
plataforma: [geral]
tema: metricas-e-relatorios
tarefas: []
fonte: "fala+pdf:cst_m01_a06_metricas.pdf"
faixa: "00:15:45–00:17:16"
perecivel: false
confianca: alta
versao: 1
```
Há mais de um tipo de clique, e dois deles são os principais: clique no link e cliques em todos.
Clique no link conta apenas quem clicou no link que leva ao destino; cliques em todos conta qualquer clique no anúncio, inclusive no perfil ou em áreas que só expandem informação.
A mesma distinção existe nos dois gerenciadores.

### U:d33f0baf66274a3d:023 — Cálculo do CTR
```yaml
tipo: regua
plataforma: [geral]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: "fala+pdf:cst_m01_a06_metricas.pdf"
faixa: "00:17:16–00:18:53"
perecivel: false
confianca: alta
versao: 1
```
CPC é o custo por clique e CTR é a taxa de cliques: cliques divididos por impressões, multiplicado por 100 para virar porcentagem.
Com 1000 impressões e 100 cliques, o CTR é de 10%.
A fonte de tráfego entrega o CTR pronto na coluna de taxa de clique no link.

### U:d33f0baf66274a3d:024 — CTR como leitura da qualidade do anúncio
```yaml
tipo: conceito
plataforma: [geral]
tema: criativo
tarefas: []
fonte: "fala+pdf:cst_m01_a06_metricas.pdf"
faixa: "00:18:01–00:18:53"
perecivel: false
confianca: alta
versao: 1
```
O CTR costuma medir a qualidade do anúncio: quanto maior a taxa, mais gente está clicando e melhor o anúncio está se saindo.
É uma leitura de desempenho do criativo, não o veredito da campanha.

### U:d33f0baf66274a3d:025 — Para performance, use as métricas de link
```yaml
tipo: decisao
plataforma: [geral]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios, otimizar-anuncios]
fonte: fala
faixa: "00:18:53–00:19:39"
perecivel: false
confianca: alta
versao: 1
```
Quando o foco é performance, isto é, levar a pessoa até o site, prefira as métricas de clique no link às de cliques em todos.
As de link dizem quantos realmente seguiram para o destino; as de todos misturam cliques que não levam a lugar nenhum.

### U:d33f0baf66274a3d:026 — Visualizações e taxa de visualização
```yaml
tipo: conceito
plataforma: [geral]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: "fala+pdf:cst_m01_a06_metricas.pdf"
faixa: "00:19:39–00:20:26"
perecivel: false
confianca: alta
versao: 2
```
Em anúncio de vídeo, visualizações contam quantas pessoas assistiram e a taxa de visualização é visualizações divididas por impressões.
A lógica é a mesma do CTR: dentre as pessoas para quem o vídeo apareceu, que porcentagem parou para ver.

### U:d33f0baf66274a3d:027 — Seguidores e envolvimento
```yaml
tipo: conceito
plataforma: [geral]
tema: metricas-e-relatorios
tarefas: []
fonte: "fala+pdf:cst_m01_a06_metricas.pdf"
faixa: "00:20:00–00:20:26"
perecivel: false
confianca: alta
versao: 1
```
Seguidores e custo por seguidor mostram quantas pessoas passaram a seguir o perfil por causa do anúncio e quanto cada uma custou.
Envolvimento e custo por envolvimento seguem a mesma lógica de quantidade mais custo.

### U:d33f0baf66274a3d:028 — CPV X% e os marcos do vídeo
```yaml
tipo: conceito
plataforma: [meta]
tema: metricas-e-relatorios
tarefas: []
fonte: "fala+pdf:cst_m01_a06_metricas.pdf"
faixa: "00:20:26–00:21:00"
perecivel: false
confianca: media
versao: 1
nota: "O professor lista as reproduções em 25%, 50%, 75% e 95% no Meta, hesita sobre existir também o marco de 100% e diz que usa pouco essa métrica; o PDF cita 25%, 50%, 75% e 100%."
```
O CPV X% mede quantas pessoas passaram por um determinado momento do vídeo, nos marcos de reprodução de 25%, 50%, 75% e 95%.
Não é o número de pessoas que pararam ali: é o número de pessoas que alcançaram aquele ponto.

### U:d33f0baf66274a3d:029 — Marcos de vídeo e fórmulas de retorno caem na certificação
```yaml
tipo: regra
plataforma: [geral]
tema: fundamentos-e-carreira
tarefas: [ler-metricas-e-relatorios]
fonte: fala
faixa: "00:20:40–00:23:20"
perecivel: true
confianca: alta
versao: 1
```
Domine a leitura do CPV X% e as fórmulas de retorno antes da prova de certificação: o professor avisa que há questão sobre cada um desses pontos e que muita gente erra a do vídeo.

### U:d33f0baf66274a3d:030 — Converter porcentagem de vídeo em segundos
```yaml
tipo: regua
plataforma: [geral]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: fala
faixa: "00:21:00–00:22:09"
perecivel: false
confianca: alta
versao: 1
```
O marco é porcentagem da duração, então converta para o seu vídeo antes de interpretar.
Num vídeo de um minuto, 25% são 15 segundos, 50% são 30 segundos, 75% são 45 segundos e 95% são 57 segundos.
Num vídeo de dez minutos esses mesmos marcos correspondem a tempos diferentes.

### U:d33f0baf66274a3d:031 — "Pelo menos": os públicos de vídeo são aninhados
```yaml
tipo: conceito
plataforma: [meta]
tema: publicos
tarefas: []
fonte: fala
faixa: "00:22:11–00:25:36"
perecivel: false
confianca: alta
versao: 1
```
A palavra que decide a leitura é "pelo menos": quem consta no marco de 25% viu pelo menos aquele trecho, podendo ter visto muito mais.
Quem chegou ao marco mais alto passou obrigatoriamente por todos os anteriores, então os públicos de vídeo são aninhados, não grupos separados de pessoas.
Anunciar para o público do marco de 25% inclui também quem assistiu ao vídeo inteiro.

### U:d33f0baf66274a3d:032 — Leitura de um vídeo de um minuto marco a marco
```yaml
tipo: exemplo
plataforma: [meta]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios, montar-publicos-personalizados]
fonte: fala
faixa: "00:23:08–00:25:36"
perecivel: false
confianca: alta
versao: 1
```
Situação: um vídeo de um minuto é divulgado e o relatório traz os quatro marcos de reprodução.
O que aconteceu: 1000 pessoas viram pelo menos 15 segundos, 600 pelo menos 30 segundos, 400 pelo menos 45 segundos e 200 pelo menos 57 segundos; parte do público abandonou entre um marco e outro.
Lógica: as 200 do último marco estão dentro das 400, que estão dentro das 600, que estão dentro das 1000; os números caem porque cada marco filtra quem seguiu assistindo, não porque sejam pessoas diferentes.

### U:d33f0baf66274a3d:033 — Público do marco mais alto costuma ser pequeno demais
```yaml
tipo: decisao
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-personalizados, otimizar-publicos-e-segmentacoes]
fonte: fala
faixa: "00:25:36–00:26:24"
condicoes: "público construído a partir de visualização de vídeo"
perecivel: false
confianca: alta
versao: 1
```
Quando montar público de visualização de vídeo, em geral não fique só no marco de 95%, porque ele deixa de fora quem já está qualificado.
Quem passou da metade do vídeo, no exemplo do vídeo de um minuto, já demonstrou interesse suficiente; usar apenas o marco mais alto descarta esse contingente e entrega um público muito pequeno.
Qual marco vale mais a pena depende do caso.

### U:d33f0baf66274a3d:034 — Connect Rate
```yaml
tipo: conceito
plataforma: [geral]
tema: destino-e-landing-page
tarefas: [ler-metricas-e-relatorios, otimizar-landing-page]
fonte: "fala+pdf:cst_m01_a06_metricas.pdf"
faixa: "00:27:06–00:27:50"
perecivel: false
confianca: alta
versao: 2
```
Connect Rate é a relação entre visualizações da página de destino e cliques no link.
Ele mostra quanta gente de fato abriu a página depois de clicar: quem clica e desiste porque a página demora conta como clique no link, mas não como visualização da página.
É uma métrica afetada pela velocidade do site.

### U:d33f0baf66274a3d:035 — Sessões e CPS
```yaml
tipo: conceito
plataforma: [geral]
tema: metricas-e-relatorios
tarefas: []
fonte: "fala+pdf:cst_m01_a06_metricas.pdf"
faixa: "00:27:50–00:28:10"
condicoes: "vocabulário usado em comércio eletrônico"
perecivel: false
confianca: alta
versao: 1
```
Sessão é cada visita ao site ou à loja, termo usado sobretudo em comércio eletrônico.
CPS é o custo por sessão, ou seja, quanto custou cada visita.

### U:d33f0baf66274a3d:036 — Adição ao carrinho e início de finalização de compra
```yaml
tipo: conceito
plataforma: [geral]
tema: metricas-e-relatorios
tarefas: []
fonte: "fala+pdf:cst_m01_a06_metricas.pdf"
faixa: "00:28:05–00:28:28"
perecivel: false
confianca: alta
versao: 1
```
Adição ao carrinho, chamada também pelo nome em inglês, conta quantas pessoas colocaram o produto no carrinho, com o custo correspondente.
Início de finalização de compra conta quem entrou na etapa de fechamento, já preenchendo dados de pagamento, também com o custo por ação.

### U:d33f0baf66274a3d:037 — Compras, CPA e valor de compras
```yaml
tipo: conceito
plataforma: [geral]
tema: metricas-e-relatorios
tarefas: []
fonte: "fala+pdf:cst_m01_a06_metricas.pdf"
faixa: "00:28:28–00:29:00"
perecivel: false
confianca: alta
versao: 1
```
Compras conta quantas pessoas compraram, CPA é o custo de cada compra e valor de compras é o quanto essas pessoas gastaram.
As três andam juntas na leitura de campanha de venda.

### U:d33f0baf66274a3d:038 — Taxas de conversão de lista, de site e de mensagens
```yaml
tipo: regua
plataforma: [geral]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: "fala+pdf:cst_m01_a06_metricas.pdf"
faixa: "00:29:00–00:30:01"
perecivel: false
confianca: alta
versao: 1
```
Taxa de conversão de lista é o número de compras dividido pelo número de leads: 100 compras vindas de 1000 leads dão 10%.
Taxa de conversão do site é o número de compras dividido pelo número de acessos, usada principalmente em comércio eletrônico.
Taxa de conversão de mensagens responde quantas conversas foram necessárias para gerar uma compra.

### U:d33f0baf66274a3d:039 — Fórmulas de ROI e ROAS
```yaml
tipo: regua
plataforma: [geral]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: "fala+pdf:cst_m01_a06_metricas.pdf"
faixa: "00:30:01–00:31:27"
perecivel: false
confianca: alta
versao: 1
```
ROI é o retorno sobre o investimento total: faturamento menos custo total, dividido pelo custo total, vezes 100.
ROAS é o retorno sobre o investimento em anúncios online: faturamento dividido pelo valor gasto em anúncios, vezes 100.
A diferença está no que entra na conta: o ROI parte do lucro e considera todos os custos; o ROAS olha só o faturamento contra a verba de mídia.

### U:d33f0baf66274a3d:040 — Ticket médio
```yaml
tipo: conceito
plataforma: [geral]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: "fala+pdf:cst_m01_a06_metricas.pdf"
faixa: "00:31:27–00:32:06"
perecivel: false
confianca: alta
versao: 2
```
Ticket médio é o valor em compras dividido pelo número de compras, isto é, quanto cada cliente gasta em média.
Vale para qualquer negócio que venda mais de um produto, do comércio local à loja online, e todos deveriam trabalhar para aumentá-lo.

### U:d33f0baf66274a3d:041 — Rotina para tirar dúvida sobre uma métrica
```yaml
tipo: procedimento
plataforma: [meta, google]
tema: metricas-e-relatorios
tarefas: [formar-se-como-gestor]
fonte: fala
faixa: "00:32:06–00:33:20"
perecivel: true
confianca: alta
versao: 2
nota: "Triagem do módulo 001 (2026-09-14): proposta de tag aceita; tarefa `formar-se-como-gestor` no lugar de ['ler-metricas-e-relatorios']."
```
Pré-condição: dúvida sobre o significado de uma métrica específica.
1. Reveja o trecho da aula que trata daquela métrica.
2. Pesquise o termo em um buscador.
3. Abra as colunas do gerenciador e passe o mouse sobre a métrica para ler a explicação da própria plataforma.
4. Se a dúvida persistir, publique a pergunta na comunidade do curso.
O professor condiciona a ajuda da comunidade ao dever de casa: a pergunta vem depois da pesquisa, não antes.

### U:d33f0baf66274a3d:042 — A aula não esgota as métricas existentes
```yaml
tipo: limite
plataforma: [geral]
tema: metricas-e-relatorios
tarefas: []
fonte: "fala+pdf:cst_m01_a06_metricas.pdf"
faixa: "00:31:40–00:32:06"
perecivel: false
confianca: alta
versao: 1
```
A aula cobre apenas o conjunto que o professor considera essencial para qualquer anunciante; ele afirma que existem muitas outras métricas nos gerenciadores e que não vai percorrê-las.
Também não cobra memorização das fórmulas: o domínio das demais métricas vem do uso.

### U:d33f0baf66274a3d:043 — Métricas de e-commerce ficam para as aulas de e-commerce
```yaml
tipo: limite
plataforma: [geral]
tema: metricas-e-relatorios
tarefas: []
fonte: fala
faixa: "00:08:39–00:09:22"
perecivel: false
confianca: alta
versao: 1
```
O funil de comércio eletrônico é usado aqui só como ilustração das etapas.
A escolha de qual etapa focar em cada caso é remetida pelo professor às aulas de e-commerce, que esta não antecipa.

### U:d33f0baf66274a3d:044 — Definição divergente de taxa de conversão do site no PDF
```yaml
tipo: fato-material
plataforma: [geral]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: "pdf:cst_m01_a06_metricas.pdf"
perecivel: false
confianca: baixa
versao: 1
nota: "O material escrito define a taxa de conversão do site como leads divididos por acessos, enquanto na fala o professor a define como compras divididas por acessos; a aula não reconcilia as duas versões e não dá para saber qual delas o professor considera correta."
```
O material escrito apresenta a taxa de conversão do site como o número de leads dividido pelo número de acessos, apontada como métrica de comércio eletrônico.
A definição falada da mesma métrica usa compras no lugar de leads.
