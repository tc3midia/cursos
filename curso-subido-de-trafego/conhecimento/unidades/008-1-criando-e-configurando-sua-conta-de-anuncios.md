---
type: unidades-aula
status: validado
title: "1.Criando e configurando sua conta de anúncios"
modulo: "008"
ordem: 120
aula_id: fd3d78155a2a415b
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

# 1.Criando e configurando sua conta de anúncios

## Contexto da aula

A aula demonstra a criação e a configuração inicial de uma estrutura de anúncios no TikTok Ads.
Ela passa pelo cadastro, dados de cobrança, Business Center, permissões, saldo e Advertiser Account.
Também apresenta os caminhos de navegação entre Business Center e Ads Manager.
A criação e a leitura detalhada de campanhas ficam para aulas posteriores.

## Unidades

### U:fd3d78155a2a415b:001 — Acessar o início do cadastro do TikTok Ads
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:00:00–00:01:27"
perecivel: true
confianca: media
versao: 1
nota: "O professor menciona ads.tiktok.com e, como alternativa, uma busca por “Ads Manager TikTok”; também testa um endereço falado como tiktok.com.br business."
```
Pré-condição: ainda não existe uma conta de anúncios TikTok.
1. Acesse ads.tiktok.com.
2. Se o endereço não abrir a página de criação, pesquise por “Ads Manager TikTok” e abra o primeiro link indicado.
3. Na página de cadastro, selecione “Sign Up Now” ou, na página TikTok for Business, “criar agora”.
4. Informe e-mail, senha, conclua a verificação e envie o cadastro.

### U:fd3d78155a2a415b:002 — Definir país, indústria, negócio, fuso e moeda corretamente
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:02:36–00:03:45"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: o cadastro inicial foi enviado e a tela pede os dados da conta.
1. Selecione o país e o tipo de indústria que mais se encaixa no negócio.
2. Informe o nome do negócio e o telefone, se o sistema exigir.
3. Defina o fuso horário e a moeda.
4. Não erre fuso horário nem moeda.

### U:fd3d78155a2a415b:003 — Preencher CNPJ no formato com pontuação
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:03:26–00:05:24"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: a configuração de cobrança solicita os dados empresariais.
1. Informe o CNPJ da empresa.
2. Inclua os pontos, a barra e o traço final no formato exibido.
3. Preencha endereço, CEP, rua e número do local.
4. Se o sistema acusar formato incorreto, confira especialmente se o traço final foi inserido.

### U:fd3d78155a2a415b:004 — Escolher entre pagamento automático e manual
```yaml
tipo: decisao
plataforma: [tiktok]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:05:24–00:06:13"
perecivel: true
confianca: alta
versao: 1
```
Se quiser pagar com cartão de crédito no modelo pós-pago, escolha pagamento automático.
Se preferir adicionar dinheiro à conta antes de gastar, escolha pagamento manual, descrito pelo professor como pré-pago.

### U:fd3d78155a2a415b:005 — Criar e configurar o Business Center
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:05:24–00:08:49"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: a conta inicial foi criada e a área “Business Center” está disponível.
1. Abra “Business Center” e informe o nome desejado para o centro de negócios.
2. Defina o fuso horário e descreva o negócio como agência ou anunciante.
3. Informe site e indústria.
4. Complete novamente os dados de pagamento, endereço, contato para invoices, e-mail, telefone e CNPJ se a tela solicitar.
5. Crie o Business Center.

### U:fd3d78155a2a415b:006 — Manter o idioma em inglês quando português não estiver disponível
```yaml
tipo: decisao
plataforma: [tiktok]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:07:59–00:08:49"
perecivel: true
confianca: alta
versao: 1
```
Quando a opção de idioma português não estiver disponível no Business Center, mantenha a interface em inglês.

### U:fd3d78155a2a415b:007 — Conceder acesso a membros no Business Center
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:08:49–00:09:28"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: o Business Center já foi criado.
1. Abra a área de pessoas.
2. Selecione “invite member”.
3. Informe o e-mail da pessoa.
4. Escolha acesso “admin” ou “standard”.
5. Adicione a pessoa à conta.

### U:fd3d78155a2a415b:008 — Conectar parceiros e localizar ativos no Business Center
```yaml
tipo: alerta-ui
plataforma: [tiktok]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:08:49–00:10:05"
perecivel: true
confianca: alta
versao: 1
```
A área “Partners” conecta o Business Center a outro Business Center.
“Advertiser accounts” corresponde à conta de anúncios; “Audiences” permite criar audiências dentro do Business Center.
A configuração de pagamento fica em “Finance”.

### U:fd3d78155a2a415b:009 — Dar a si mesmo permissão financeira
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:09:28–00:10:10"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: a página de pagamentos informa que apenas membros com permissão financeira podem visualizá-la.
1. Selecione a opção para atualizar o acesso.
2. Escolha “Finance manager”.
3. Confirme em “Update”.
4. Retorne à área de pagamentos.

### U:fd3d78155a2a415b:010 — Adicionar saldo mínimo na conta manual
```yaml
tipo: regua
plataforma: [tiktok]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:10:10–00:11:31"
condicoes: "pagamento manual"
perecivel: true
confianca: alta
versao: 1
```
Na área “Payments”, adicione o saldo que deseja gastar; o mínimo mostrado é R$ 60, em torno de US$ 10.
Após confirmar o valor, escolha cartão de crédito, boleto ou Pix para realizar o pagamento.

### U:fd3d78155a2a415b:011 — Criar uma Advertiser Account
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:10:49–00:12:05"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: o Business Center existe e não há uma Advertiser Account associada.
1. Em “Advertiser accounts”, selecione “Create new”; alternativamente, solicite acesso a uma conta existente.
2. Informe nome da conta, fuso horário e moeda.
3. Confira nome da companhia e local de registro, que podem vir preenchidos pelo Business Center.
4. Continue, confirme os dados de contato, aceite os termos de serviço e envie.

### U:fd3d78155a2a415b:012 — Usar o modo customizado no Ads Manager
```yaml
tipo: regra
plataforma: [tiktok]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:11:57–00:12:33"
perecivel: true
confianca: alta
versao: 1
```
No Ads Manager, escolha “custom mode”, indicado pelo professor como o modo mais avançado, em vez do modo simplificado.

### U:fd3d78155a2a415b:013 — Reconhecer as áreas principais do Ads Manager
```yaml
tipo: alerta-ui
plataforma: [tiktok]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:12:07–00:13:17"
perecivel: true
confianca: alta
versao: 1
```
“Dashboard” mostra a visão geral da conta; “Campaign” mostra a visão das campanhas.
“Asserts” é a área apontada para criar públicos, e “Reporting” permite ver relatórios.
Para voltar ao Business Center, clique no ícone que o professor identifica como uma maleta.

### U:fd3d78155a2a415b:014 — Separar Business Center e conta de anúncios por cliente
```yaml
tipo: regra
plataforma: [tiktok]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:13:17–00:13:53"
perecivel: false
confianca: alta
versao: 1
```
Tenha sempre um Business Center e uma conta de anúncio para cada cliente.
Se quiser mais de uma conta de anúncios para contingência, siga a mesma lógica aplicada pelo professor no Facebook Ads.

### U:fd3d78155a2a415b:015 — Editar dados e enviar verificação do negócio
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:13:53–00:14:31"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: o Business Center está criado.
1. Abra “Business Center information” para alterar e-mail de contato, nome da empresa ou imagem.
2. Abra a área de verificação.
3. Informe nome da empresa, endereço, contato, e-mail e telefone.
4. Envie os dados para verificação.

### U:fd3d78155a2a415b:016 — Preferir a visão de campanhas ao dashboard
```yaml
tipo: regra
plataforma: [tiktok]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: fala
faixa: "00:14:31–00:15:12"
perecivel: true
confianca: alta
versao: 1
```
Para ver o resumo de cada campanha, acesse a área “Campaigns”.
O professor não gosta muito da visão de “Dashboard”, que mostra uma visão geral e gasto por dia, e diz que a exploração será feita nas próximas aulas.

### U:fd3d78155a2a415b:017 — A aula não explora campanhas em detalhe
```yaml
tipo: limite
plataforma: [tiktok]
tema: estrutura-de-campanha
tarefas: []
fonte: fala
faixa: "00:12:07–00:15:12"
perecivel: false
confianca: alta
versao: 1
```
A aula mostra onde o Ads Manager direciona para criar campanhas, mas deixa a exploração de campanhas e do resumo delas para as próximas aulas.