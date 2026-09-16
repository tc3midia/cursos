---
type: unidades-aula
status: validado
title: "1.0 - Configurações Iniciais"
modulo: "003"
ordem: 55
aula_id: 7d799930d747fec1
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - cst_m03_a01_configuracoes_iniciais.pdf
  - transcricao.md
extraido_em: 2026-09-14
gerado_por: opus-5
retiradas: []
divisoes: []
fusoes: []
---

# 1.0 - Configurações Iniciais

## Contexto da aula

Primeira aula do módulo de Google, dedicada a abrir a conta de anúncios e deixá-la pronta para
anunciar. O professor cria uma conta do zero em aba anônima, sem campanha, e percorre os menus de
faturamento, acesso e segurança, preferências e contas vinculadas.
Em seguida abre uma conta do Google Analytics ao vivo, mostra onde fica o código de acompanhamento e
vincula Analytics e canal do YouTube ao Google Ads.
Assume que o aluno ainda não tem conta em nenhuma das três ferramentas e que não domina o Analytics.
Não ensina configuração de tags nem de pixel; só indica onde isso é tratado e adia o pixel para a
aula seguinte.

## Unidades

### U:7d799930d747fec1:001 — As três configurações iniciais da conta do Google Ads
```yaml
tipo: regra
plataforma: [google]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: "fala+pdf:cst_m03_a01_configuracoes_iniciais.pdf"
faixa: "00:00:00–00:00:58"
perecivel: false
confianca: alta
versao: 1
```
Depois de criar a conta, faça três configurações antes de anunciar: método de pagamento, vínculo do YouTube com o Google Ads e vínculo do Google Analytics com o Google Ads.
O vínculo com o YouTube serve para o Google Ads reconhecer quem assiste aos seus vídeos.
Não ter canal no YouTube nem conta no Analytics não impede: crie as duas agora, mesmo sem dominar as ferramentas, para já deixar tudo no lugar.

### U:7d799930d747fec1:002 — Criar a conta no Google Ads sem campanha
```yaml
tipo: procedimento
plataforma: [google]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: "fala+pdf:cst_m03_a01_configuracoes_iniciais.pdf"
faixa: "00:00:58–00:02:37"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: um e-mail Google que será o gerenciador das campanhas e um navegador aberto.
1. Pesquise no Google como criar conta no Google Ads e entre pelo primeiro resultado, ou vá direto ao endereço oficial da plataforma.
2. Clique em "começar agora" e faça login com o e-mail e a senha que vão gerenciar as campanhas.
3. Se o e-mail já tiver conta, o Google leva direto ao painel dela; use o botão de nova conta no topo e confirme que quer criar outra.
4. Pule as opções de meta da publicidade e clique em "alterar para o modo especialista" no fim da página.
5. Na tela que pede uma campanha, desça até a barra inferior e clique em "criar uma conta sem uma campanha".
6. Confira os dados e clique em "enviar". A conta está criada.

### U:7d799930d747fec1:003 — Conferir país de faturamento, fuso e moeda antes de enviar
```yaml
tipo: regra
plataforma: [google]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:02:04–00:02:37"
perecivel: false
confianca: alta
versao: 1
```
Antes de confirmar a criação da conta, confira os três campos da tela: país de faturamento, fuso horário e unidade monetária.
O país de faturamento é aquele onde você emite nota fiscal.

### U:7d799930d747fec1:004 — Refazer o login para sair da visão de iniciante
```yaml
tipo: alerta-ui
plataforma: [google]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:02:38–00:03:17"
perecivel: true
confianca: alta
versao: 1
```
Logo depois de criar a conta, a única opção liberada é "explorar minha conta", e ela abre um painel reduzido, de iniciante.
Saia e entre de novo pelo endereço do Google Ads, escolha a conta recém-criada na lista e o painel aparece completo, com o menu lateral e as informações do topo.

### U:7d799930d747fec1:005 — Ferramentas e configurações concentra os menus da conta
```yaml
tipo: alerta-ui
plataforma: [google]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: "fala+pdf:cst_m03_a01_configuracoes_iniciais.pdf"
faixa: "00:03:17–00:03:56"
perecivel: true
confianca: alta
versao: 1
```
Quase todos os menus de ferramentas e configurações da conta ficam num único lugar: a aba "ferramentas e configurações" da barra superior, dividida em seis seções.
Clicar nela abre a lista completa de ferramentas; é de lá que saem faturamento, acesso e segurança, preferências e contas vinculadas.

### U:7d799930d747fec1:006 — Fuça e clica: abrir todos os menus da ferramenta
```yaml
tipo: regra
plataforma: [google]
tema: fundamentos-e-carreira
tarefas: [formar-se-como-gestor]
fonte: "fala+pdf:cst_m03_a01_configuracoes_iniciais.pdf"
faixa: "00:03:56–00:04:31"
perecivel: false
confianca: alta
versao: 1
```
Depois da aula, reserve um tempo para abrir um a um os menus da conta e ver o que cada um oferece, inclusive os que você ainda não entende, como estratégias de lance.
Isso não gasta verba e é aprender tráfego na prática; segundo o professor, a maioria dos gestores nunca abriu todos esses menus, e quem abre entra na minoria que costuma ter mais resultado.

### U:7d799930d747fec1:007 — Configurar o pagamento em Faturamento, Resumo
```yaml
tipo: procedimento
plataforma: [google]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: "fala+pdf:cst_m03_a01_configuracoes_iniciais.pdf"
faixa: "00:04:31–00:05:31"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: conta criada e um cartão de crédito ou de débito em mãos.
1. Abra "ferramentas e configurações" na barra superior.
2. Vá à seção de faturamento e clique em "resumo" para ver as informações de cobrança.
3. Preencha todas as informações de pagamento com o cartão.
4. Confira os dados, aceite os termos de uso e clique em "enviar".

### U:7d799930d747fec1:008 — Cartão abre a conta, boleto vira saldo depois
```yaml
tipo: regra
plataforma: [google]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: "fala+pdf:cst_m03_a01_configuracoes_iniciais.pdf"
faixa: "00:04:31–00:05:31"
perecivel: false
confianca: alta
versao: 1
```
Para configurar o pagamento no início é preciso um cartão de crédito ou de débito; não dá para começar só com boleto.
Com o cartão cadastrado, você pode depois emitir um boleto no valor que quiser e usá-lo como saldo dentro da conta.
O cadastro aceita tanto pessoa física quanto organização.

### U:7d799930d747fec1:009 — Dar acesso a outras pessoas em Acesso e segurança
```yaml
tipo: procedimento
plataforma: [google]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: "fala+pdf:cst_m03_a01_configuracoes_iniciais.pdf"
faixa: "00:05:33–00:06:10"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: estar no painel da conta e ter o e-mail de quem vai receber acesso.
1. Na barra superior, abra "ferramentas e configurações" e clique em "acesso e segurança".
2. A tela lista o seu e-mail como dono; clique no botão de mais, no canto superior, para adicionar alguém.
3. Informe o e-mail da pessoa e preencha as atribuições de acesso.
4. Confira e clique em "enviar convite".

### U:7d799930d747fec1:010 — Sempre dê nome à conta de anúncios
```yaml
tipo: regra
plataforma: [google]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: "fala+pdf:cst_m03_a01_configuracoes_iniciais.pdf"
faixa: "00:06:10–00:06:50"
perecivel: false
confianca: alta
versao: 1
```
Nomeie toda conta de anúncios que criar, em vez de deixar o nome padrão, porque é assim que você identifica de quem é cada conta e mantém as campanhas organizadas.
Preencha também os dados de contato por completo.

### U:7d799930d747fec1:011 — O que fica em Preferências
```yaml
tipo: alerta-ui
plataforma: [google]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: "fala+pdf:cst_m03_a01_configuracoes_iniciais.pdf"
faixa: "00:06:10–00:06:50"
perecivel: true
confianca: alta
versao: 1
```
Em "preferências", dentro da barra superior, ficam o idioma da conta, o formato do número (separador decimal por ponto ou por vírgula), o nome da conta e os dados de contato.

### U:7d799930d747fec1:012 — O que são contas vinculadas
```yaml
tipo: conceito
plataforma: [google]
tema: conta-e-configuracao
tarefas: []
fonte: "fala+pdf:cst_m03_a01_configuracoes_iniciais.pdf"
faixa: "00:06:50–00:07:31"
perecivel: false
confianca: alta
versao: 2
nota: "triagem 003: proposta de tarefa vincular-contas-externas recusada na sessão, tag mais próxima mantida"
```
Contas vinculadas são as contas de outras ferramentas que você associa ao Google Ads para usar os dados delas nos anúncios.
Nesta configuração inicial as duas que interessam são o canal do YouTube e o Google Analytics.

### U:7d799930d747fec1:013 — Criar a conta no Google Analytics
```yaml
tipo: procedimento
plataforma: [google]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: "fala+pdf:cst_m03_a01_configuracoes_iniciais.pdf"
faixa: "00:07:31–00:10:06"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: uma conta Google e, se houver, o endereço do site.
1. Pesquise no Google como criar conta no Google Analytics, entre no site oficial e clique em "começar a avaliação".
2. Dê um nome à conta, usando um nome óbvio de reconhecer.
3. Marque os dados que quer compartilhar com o Google.
4. Crie a propriedade com um nome igualmente óbvio e ajuste fuso horário, país e moeda.
5. Informe o tamanho da empresa e marque os objetivos de uso da ferramenta.
6. Se tiver site, ative o fluxo de web, coloque a URL e dê nome ao fluxo.
7. Clique em criar e aceite os termos.

### U:7d799930d747fec1:014 — Compartilhar os dados com o Google
```yaml
tipo: regra
plataforma: [google]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: "fala+pdf:cst_m03_a01_configuracoes_iniciais.pdf"
faixa: "00:07:58–00:08:30"
perecivel: false
confianca: alta
versao: 1
```
Na criação da conta do Analytics, marque o compartilhamento de dados com o Google, porque as ferramentas melhoram com esses dados e essa melhora volta para quem anuncia.

### U:7d799930d747fec1:015 — Ajustar fuso, país e moeda na propriedade do Analytics
```yaml
tipo: regra
plataforma: [google]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: "fala+pdf:cst_m03_a01_configuracoes_iniciais.pdf"
faixa: "00:08:38–00:09:05"
perecivel: false
confianca: alta
versao: 1
```
Ao criar a propriedade, corrija fuso horário, país e moeda em vez de aceitar o padrão: para o Brasil, país Brasil, fuso de Brasília e moeda brasileira.
Dá para editar depois na página de administrador, mas o professor insiste em deixar certo já na criação.

### U:7d799930d747fec1:016 — Fluxo de dados de site só para quem tem site
```yaml
tipo: decisao
plataforma: [google]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:09:06–00:09:35"
condicoes: "criação da propriedade no Google Analytics"
perecivel: true
confianca: baixa
versao: 1
nota: "Na fala o professor ativa uma opção sem nomear qual é e só diz que quem não tem site não deve ativá-la; a leitura de que é o fluxo de dados de web vem do passo do PDF que pede clicar em web e informar a URL."
```
Se você tem site, ative a opção de fluxo de dados e informe a URL da página.
Se não tem site, deixe a opção desligada: o cadastro fica mais simples e nada se perde nesta etapa.

### U:7d799930d747fec1:017 — Configuração de tags e do Analytics fica fora da aula
```yaml
tipo: limite
plataforma: [google]
tema: conta-e-configuracao
tarefas: []
fonte: "fala+pdf:cst_m03_a01_configuracoes_iniciais.pdf"
faixa: "00:10:09–00:10:49"
perecivel: false
confianca: alta
versao: 1
```
A aula não ensina a configurar as tags nem as demais funcionalidades do Google Analytics; só cria a conta e localiza o código.
O professor remete esse conteúdo a cursos próprios de Google Tag Manager e de Google Analytics dentro da comunidade dele.

### U:7d799930d747fec1:018 — Onde fica o código de acompanhamento do Analytics
```yaml
tipo: alerta-ui
plataforma: [google]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: "fala+pdf:cst_m03_a01_configuracoes_iniciais.pdf"
faixa: "00:10:49–00:11:58"
perecivel: true
confianca: alta
versao: 1
```
A conta recém-criada nasce com duas propriedades: a versão nova do Analytics e a antiga, o Universal Analytics.
Para achar o código, troque de propriedade pelo seletor de contas no topo, entre na propriedade antiga, abra todos os dados do website e clique em "administrador", no fim do menu lateral.
Dentro do administrador, "informações de acompanhamento" mostra o código de acompanhamento e a tag global do site; ali ao lado ficam também o gerenciamento de acesso à conta e à propriedade, onde você libera acesso a colaboradores.

### U:7d799930d747fec1:019 — O número depois de UA é o código do Analytics
```yaml
tipo: conceito
plataforma: [google]
tema: pixel-e-eventos
tarefas: []
fonte: "fala+pdf:cst_m03_a01_configuracoes_iniciais.pdf"
faixa: "00:11:24–00:11:58"
perecivel: false
confianca: alta
versao: 1
```
Quando uma plataforma pede o código do Google Analytics, ela pode aceitar duas formas: o bloco inteiro da tag ou apenas o número que vem depois das letras UA no identificador.
É esse número que costuma ser pedido em cadastros de loja virtual.

### U:7d799930d747fec1:020 — O código do Analytics vai em todas as páginas do site
```yaml
tipo: regra
plataforma: [google]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: "fala+pdf:cst_m03_a01_configuracoes_iniciais.pdf"
faixa: "00:11:58–00:12:36"
perecivel: false
confianca: alta
versao: 1
```
O código do Analytics precisa ser instalado em todas as páginas do site, não só na inicial.
A instalação pode ser feita por você mesmo ou por um programador.

### U:7d799930d747fec1:021 — Vincular o Analytics ao Google Ads
```yaml
tipo: procedimento
plataforma: [google]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: "fala+pdf:cst_m03_a01_configuracoes_iniciais.pdf"
faixa: "00:12:36–00:12:40"
perecivel: true
confianca: media
versao: 2
nota: "O professor executa os últimos cliques em poucos segundos e não mostra a tela final; os nomes dos comandos vêm da fala e do PDF, sem confirmação visual descrita. triagem 003: proposta de tarefa vincular-contas-externas recusada na sessão, tag mais próxima mantida"
```
Pré-condição: conta do Analytics criada com o mesmo login usado no Google Ads.
1. Volte à aba do Google Ads e atualize a página; o Google Ads costuma já reconhecer que existe uma conta do Analytics vinculável.
2. Abra "contas vinculadas" na barra superior e localize o Google Analytics.
3. Clique para vincular todos os dados do website.
4. Marque a importação das métricas do site e clique em salvar.

### U:7d799930d747fec1:022 — Vincular o canal do YouTube ao Google Ads
```yaml
tipo: procedimento
plataforma: [google, youtube]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: "fala+pdf:cst_m03_a01_configuracoes_iniciais.pdf"
faixa: "00:12:40–00:13:52"
perecivel: true
confianca: alta
versao: 2
nota: "triagem 003: proposta de tarefa vincular-contas-externas recusada na sessão, tag mais próxima mantida"
```
Pré-condição: ser dono do canal e conseguir entrar nas configurações dele.
1. No Google Ads, abra "contas vinculadas" na barra superior, encontre o YouTube e clique em "detalhes".
2. Clique em adicionar um canal.
3. Abra o YouTube, copie a URL do canal e cole na busca; procurar pela URL é o caminho mais seguro, sem risco de escolher o canal errado.
4. Responda que o canal é seu quando a plataforma perguntar se você é o dono.
5. Vá ao YouTube e confirme o vínculo nas configurações do canal, liberando o acesso do Google aos dados dele.

### U:7d799930d747fec1:023 — Pixel fica para a próxima aula
```yaml
tipo: limite
plataforma: [google]
tema: pixel-e-eventos
tarefas: []
fonte: "fala+pdf:cst_m03_a01_configuracoes_iniciais.pdf"
faixa: "00:13:52–00:14:00"
perecivel: false
confianca: alta
versao: 1
```
A aula encerra com a conta pronta para começar: pagamento configurado, conta nomeada, Analytics e YouTube vinculados.
A configuração do pixel não é tratada aqui e fica para a aula seguinte.
