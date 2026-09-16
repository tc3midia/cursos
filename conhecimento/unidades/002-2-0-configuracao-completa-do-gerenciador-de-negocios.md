---
type: unidades-aula
status: validado
title: "2.0 - Configuração completa do Gerenciador de Negócios"
modulo: "002"
ordem: 20
aula_id: 887d4696c3467a94
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

# 2.0 - Configuração completa do Gerenciador de Negócios

## Contexto da aula

A aula demonstra a criação e a configuração inicial do Gerenciador de Negócios do Meta.
Parte de um perfil pessoal do Facebook e percorre BM, página, conta de anúncios, acessos, Instagram, WhatsApp, pixel, domínio e segurança.
O professor diferencia a estrutura comum de uma estrutura de contingência para nichos sensíveis.
A configuração técnica do pixel é deixada para outra aula.

## Unidades

### U:887d4696c3467a94:001 — Use um perfil do Facebook para iniciar a estrutura
```yaml
tipo: regra
plataforma: [meta]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:00:00–00:00:36"
perecivel: false
confianca: alta
versao: 1
```
Tenha um perfil no Facebook antes de criar BM, conta de anúncios, página, perfil comercial do Instagram, pixel e acessos.

### U:887d4696c3467a94:002 — Acesse uma das páginas de criação da BM
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:00:36–00:01:16"
perecivel: true
confianca: alta
versao: 1
```
Acesse `business.facebook.overview` ou `business.facebook.create`; as duas páginas podem levar ao mesmo lugar, mas uma delas pode sair do ar.
O material PDF da comunidade contém os dois links.

### U:887d4696c3467a94:003 — Cada perfil cria no máximo duas BMs
```yaml
tipo: regua
plataforma: [meta]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:01:16–00:01:57"
perecivel: false
confianca: alta
versao: 1
```
Cada perfil do Facebook pode criar 2 Business Managers, embora possa criar até 2.500 contas de anúncio.
Para criar mais BMs, use mais perfis.

### U:887d4696c3467a94:004 — Contingência usa mais de uma estrutura
```yaml
tipo: conceito
plataforma: [meta]
tema: conta-e-configuracao
tarefas: []
fonte: fala
faixa: "00:01:16–00:02:45"
perecivel: false
confianca: alta
versao: 1
```
Contingência é criar uma estrutura que permita continuar anunciando se ocorrer bloqueio.
Ela costuma envolver mais de um perfil, BM e conta de anúncios.

### U:887d4696c3467a94:005 — Antecipe a contingência em nichos sensíveis
```yaml
tipo: decisao
plataforma: [meta]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:01:57–00:03:18"
condicoes: "quando anuncia nicho sensível ou que faz promessas muito grandes"
perecivel: false
confianca: alta
versao: 1
```
Se anunciar um nicho sensível, estude bloqueios e contingência antes de ser bloqueado.
Para educação, negócio local ou e-commerce tranquilo, o professor diz para não entrar em desespero com bloqueios, mas recomenda que todos assistam às aulas sobre o tema.

### U:887d4696c3467a94:006 — Nomeie a BM com o negócio
```yaml
tipo: procedimento
plataforma: [meta]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:03:18–00:05:10"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: tela de criação de conta do Gerenciador de Negócios aberta.
1. Informe o nome do negócio; o professor prefere começar com “BM” seguido do nome da empresa.
2. Informe seu nome.
3. Cadastre um e-mail para a conta.
Prefira Gmail ou e-mail comercial da empresa; o professor apresenta outros provedores como opções possíveis.

### U:887d4696c3467a94:007 — Confirme o e-mail comercial da BM
```yaml
tipo: procedimento
plataforma: [meta]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:05:12–00:06:42"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: criação da BM enviada com um e-mail cadastrado.
1. Procure a mensagem do Facebook no e-mail inteiro; no Gmail ela pode aparecer na aba Social.
2. Abra a mensagem de confirmação do e-mail comercial.
3. Clique em confirmar para receber controle total da BM.
O perfil usado na criação já aparece com acesso ao Gerenciador de Negócios.

### U:887d4696c3467a94:008 — Solicite análise se a BM vier restrita
```yaml
tipo: procedimento
plataforma: [meta]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:06:42–00:08:53"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: a BM mostra restrição e impede criar contas de anúncios.
1. Inicie a solicitação de análise de acesso a publicar.
2. Confirme sua identidade pelo código enviado ao celular.
3. Envie um documento de identidade e carregue a imagem.
4. Aguarde a análise para a liberação da conta.

### U:887d4696c3467a94:009 — Crie a conta de anúncios com fuso e moeda corretos
```yaml
tipo: procedimento
plataforma: [meta]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:09:29–00:11:17"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: acesso às configurações da BM.
1. Em contas de anúncios, escolha adicionar e criar nova conta.
2. Defina o nome da conta.
3. Configure o fuso horário e a moeda corretos antes de avançar.
4. Indique se a conta será usada pela sua empresa ou pela empresa de um cliente.
O nome pode ser alterado depois, mas o professor diz que fuso horário e moeda não podem ser trocados.

### U:887d4696c3467a94:010 — Escolha como adicionar página e conta de anúncios
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:09:29–00:10:44"
perecivel: true
confianca: alta
versao: 1
```
Em Páginas, escolha entre adicionar uma página própria, solicitar acesso a uma página de terceiros ou criar uma nova.
Em Contas de anúncios, escolha entre adicionar uma conta acessível, solicitar acesso ou criar nova conta.

### U:887d4696c3467a94:011 — Atribua pessoas ao criar a conta de anúncios
```yaml
tipo: procedimento
plataforma: [meta]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:11:17–00:12:28"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: nova conta de anúncios criada.
1. Selecione pelo menos uma pessoa para ter acesso à conta.
2. Escolha o nível de acesso de cada pessoa, como controle total ou gerenciamento de campanhas.
3. Atribua os acessos; o professor demonstra que a atribuição pode exigir selecionar um de cada vez.

### U:887d4696c3467a94:012 — Informe dados fiscais e forma de pagamento
```yaml
tipo: procedimento
plataforma: [meta]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:12:28–00:13:42"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: conta de anúncios criada e tela de pagamento aberta.
1. Informe os dados fiscais da empresa, incluindo CNPJ ou CPF.
2. Escolha o método de pagamento.
3. Preencha os dados solicitados e salve.
O professor cita cartão de crédito, PayPal e boleto bancário; Pix pode ser liberado depois na conta.

### U:887d4696c3467a94:013 — Sem pagamento não é possível anunciar
```yaml
tipo: regra
plataforma: [meta]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:13:07–00:13:42"
perecivel: false
confianca: alta
versao: 1
```
A conta de anúncios pode estar criada sem forma de pagamento, mas sem forma de pagamento não é possível anunciar.

### U:887d4696c3467a94:014 — Conecte o Instagram profissional, não o pessoal do gestor
```yaml
tipo: decisao
plataforma: [meta]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:13:42–00:14:20"
perecivel: true
confianca: alta
versao: 1
```
Se for conectar uma conta do Instagram, conecte o Instagram profissional que fará os anúncios, não o Instagram pessoal do gestor.
A conexão exige login e senha da conta do Instagram.

### U:887d4696c3467a94:015 — Adicione o WhatsApp Business por confirmação de código
```yaml
tipo: procedimento
plataforma: [meta]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:14:20–00:15:04"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: seção de contas do WhatsApp aberta na BM.
1. Escolha adicionar conta do WhatsApp.
2. Informe o país e o número do WhatsApp Business; para Brasil, o professor usa +55.
3. Informe o código recebido para adicionar o número.

### U:887d4696c3467a94:016 — Dê acessos por ativo depois de adicionar a pessoa
```yaml
tipo: procedimento
plataforma: [meta]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:14:20–00:22:32"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: a pessoa foi adicionada em Usuários > Pessoas pelo e-mail.
1. Abra o ativo, como página, conta de anúncios, Instagram, WhatsApp, pixel ou catálogo.
2. Escolha adicionar pessoas no ativo.
3. Selecione a pessoa, defina o nível de acesso e atribua.
Adicionar alguém no menu Pessoas não concede automaticamente acesso a todos os ativos.

### U:887d4696c3467a94:017 — Crie ou solicite acesso a catálogos
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:15:04–00:15:47"
perecivel: true
confianca: alta
versao: 1
```
Em Fontes de dados > Catálogos, é possível solicitar acesso a um catálogo ou criar um novo catálogo.

### U:887d4696c3467a94:018 — Prefira criar o pixel dentro da BM
```yaml
tipo: decisao
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: "00:15:04–00:16:28"
perecivel: true
confianca: alta
versao: 1
```
Quando criar o pixel, prefira criá-lo dentro da BM em vez de dentro da conta de anúncios.
O professor diz que os dois locais resolvem, mas recomenda a BM.

### U:887d4696c3467a94:019 — Configure pessoas e ativos com acesso ao pixel
```yaml
tipo: procedimento
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: "00:22:32–00:23:47"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: pixel criado em Fontes de dados.
1. Adicione pessoas ao pixel e atribua o acesso necessário.
2. Em ativos conectados, adicione a conta de anúncios ao pixel.
3. Confirme que pessoas e conta de anúncios têm acesso ao pixel.
A conta de anúncios precisa ter acesso ao pixel para fazer anúncios.

### U:887d4696c3467a94:020 — A aula não configura tecnicamente o pixel
```yaml
tipo: limite
plataforma: [meta]
tema: pixel-e-eventos
tarefas: []
fonte: fala
faixa: "00:15:47–00:16:28"
perecivel: false
confianca: alta
versao: 1
```
A aula mostra onde criar o pixel e onde ficam fontes de dados, mas deixa a configuração do pixel para outro momento.

### U:887d4696c3467a94:021 — Verifique o domínio na BM
```yaml
tipo: procedimento
plataforma: [meta]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:16:28–00:17:56"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: domínio próprio e acesso à seção Domínios da BM.
1. Adicione o domínio na seção de adequação e segurança.
2. Copie a tag apresentada pela plataforma.
3. Cole a tag no `head` do HTML da página inicial e publique a página.
4. Siga as instruções apresentadas para concluir a verificação.
O professor diz que o domínio precisa estar verificado para anunciar.

### U:887d4696c3467a94:022 — Use o Centro de Segurança para proteger a conta
```yaml
tipo: procedimento
plataforma: [meta]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:17:56–00:18:39"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: acesso ao Centro de Segurança da BM.
1. Ative a autenticação de dois fatores.
2. Mantenha pelo menos dois administradores na conta de anúncios.
3. Verifique a empresa.
Se os indicadores não estiverem concluídos, use os botões exibidos para seguir a configuração.

### U:887d4696c3467a94:023 — Preencha e verifique as informações da empresa
```yaml
tipo: procedimento
plataforma: [meta]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:18:39–00:19:21"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: seção Informações da empresa aberta.
1. Informe razão social, endereço, foto e status da empresa.
2. Inicie a verificação da empresa.
3. Envie as comprovações solicitadas pela plataforma.
O professor orienta preencher tudo o que a plataforma pedir para demonstrar que a empresa existe.

### U:887d4696c3467a94:024 — Faça a validação de identidade com antecedência
```yaml
tipo: regua
plataforma: [meta]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:19:21–00:20:36"
condicoes: "quando a BM recebe bloqueio automático de confirmação de identidade"
perecivel: false
confianca: alta
versao: 1
```
Após enviar o código do celular e um documento, o professor indica aguardar 24 horas ou 48 horas pela aprovação para acessar a BM.

### U:887d4696c3467a94:025 — Acesse o Gerenciador de Anúncios após concluir a estrutura
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: conta-e-configuracao
tarefas: [criar-campanha]
fonte: fala
faixa: "00:24:28–00:25:05"
perecivel: true
confianca: alta
versao: 1
```
Depois de configurar domínio, verificação da empresa, autenticação de dois fatores e administrador secundário, abra Todas as ferramentas e entre no Gerenciador de Anúncios para começar a anunciar.