---
type: unidades-aula
status: validado
title: "1.0 - Estruturas Iniciais"
modulo: "002"
ordem: 19
aula_id: f4736e839d1e5cb0
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

# 1.0 - Estruturas Iniciais

## Contexto da aula

A aula apresenta as estruturas usadas para anunciar no Meta Ads.
Distingue perfil pessoal, página do Facebook, perfil comercial do Instagram, conta de anúncios e gerenciador de negócios.
Também orienta a separação entre a propriedade dos ativos do cliente e o acesso do gestor de tráfego.
A criação detalhada dessas estruturas fica para as próximas aulas.

## Unidades

### U:f4736e839d1e5cb0:001 — Perfil pessoal do Facebook é necessário para anunciar
```yaml
tipo: regra
plataforma: [meta]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: 00:00:00–00:01:12
perecivel: false
confianca: alta
versao: 1
```
Para anunciar no Meta Ads, tenha um perfil pessoal no Facebook.
Sem perfil no Facebook, não é possível criar a página no Facebook.

### U:f4736e839d1e5cb0:002 — Criar um perfil pessoal no Facebook
```yaml
tipo: procedimento
plataforma: [meta]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: 00:00:00–00:00:33
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: acesso ao site facebook.com.
1. Clique em "criar uma nova conta".
2. Crie a conta pessoal.

### U:f4736e839d1e5cb0:003 — Faça o perfil parecer uma pessoa real
```yaml
tipo: procedimento
plataforma: [meta]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: 00:00:33–00:01:12
perecivel: false
confianca: alta
versao: 1
```
Pré-condição: perfil pessoal criado no Facebook.
1. Coloque uma foto e adicione alguns amigos.
2. Envie mensagens, faça publicações e mantenha o perfil pessoal.
Isso reduz a chance de o Facebook entender que o perfil não existe.

### U:f4736e839d1e5cb0:004 — Página do Facebook é a estrutura que patrocina anúncios
```yaml
tipo: conceito
plataforma: [meta]
tema: conta-e-configuracao
tarefas: []
fonte: fala
faixa: 00:01:12–00:01:53
perecivel: false
confianca: alta
versao: 1
```
Os anúncios no Facebook são patrocinados pela página, não pelo perfil pessoal.
Página é uma estrutura profissional; perfil é sempre pessoal.

### U:f4736e839d1e5cb0:005 — Criar uma página pelo perfil do Facebook
```yaml
tipo: procedimento
plataforma: [meta]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: 00:01:53–00:02:36
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: perfil pessoal no Facebook.
1. No perfil, abra "ver mais" se necessário e entre em "páginas".
2. Clique em "criar uma nova página" e preencha as informações.
A página também pode ser criada no gerenciador de negócios.

### U:f4736e839d1e5cb0:006 — Perfil comercial do Instagram é uma transformação do perfil pessoal
```yaml
tipo: conceito
plataforma: [meta]
tema: conta-e-configuracao
tarefas: []
fonte: fala
faixa: 00:02:36–00:03:17
perecivel: false
confianca: alta
versao: 1
```
No Instagram, o perfil pessoal pode ser transformado em perfil comercial; não são estruturas separadas como perfil e página no Facebook.
O perfil profissional pode exibir categoria como empreendedor, criador digital ou produtor de conteúdo.

### U:f4736e839d1e5cb0:007 — Prefira perfil comercial ao perfil de criador de conteúdo
```yaml
tipo: decisao
plataforma: [meta]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: 00:03:18–00:04:38
perecivel: false
confianca: alta
versao: 1
```
Se for transformar o perfil do Instagram em profissional, prefira o perfil comercial.
Segundo o professor, ele permite criar públicos de remarketing para anunciar a quem interagiu com publicações, enquanto o perfil de criador perde recursos, principalmente de anúncios online.

### U:f4736e839d1e5cb0:008 — Anúncios no Instagram usam o perfil comercial
```yaml
tipo: regra
plataforma: [meta]
tema: conta-e-configuracao
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:03:56–00:04:38
perecivel: false
confianca: alta
versao: 1
```
Para fazer anúncios por um perfil no Instagram, use o perfil comercial do Instagram.
Quando o anúncio aparece no Instagram, quem anuncia é esse perfil comercial.

### U:f4736e839d1e5cb0:009 — Conta de anúncios e gerenciador de anúncios são a mesma estrutura
```yaml
tipo: conceito
plataforma: [meta]
tema: conta-e-configuracao
tarefas: []
fonte: fala
faixa: 00:04:39–00:05:17
perecivel: true
confianca: alta
versao: 1
```
Conta de anúncios, gerenciador de anúncios e CA são nomes usados para a estrutura onde se criam campanhas e anúncios.
O professor a apresenta como a tela que será usada frequentemente.

### U:f4736e839d1e5cb0:010 — Conta de anúncios é gratuita e exige perfil pessoal
```yaml
tipo: regua
plataforma: [meta]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: 00:04:39–00:05:17
perecivel: false
confianca: alta
versao: 1
```
Criar uma conta de anúncios é 100% gratuito.
Qualquer pessoa pode criá-la desde que tenha um perfil pessoal no Facebook.

### U:f4736e839d1e5cb0:011 — Gerenciador de negócios organiza os ativos
```yaml
tipo: conceito
plataforma: [meta]
tema: conta-e-configuracao
tarefas: []
fonte: fala
faixa: 00:05:17–00:06:52
perecivel: false
confianca: alta
versao: 1
```
O gerenciador de negócios, também chamado BM ou Business Manager, é uma estrutura organizacional que gerencia ativos.
Nele podem ficar páginas, contas de anúncio, pixels, perfis comerciais do Instagram, domínios, catálogos, pessoas, cargos e formas de pagamento.

### U:f4736e839d1e5cb0:012 — Crie um gerenciador de negócios mesmo podendo anunciar sem ele
```yaml
tipo: regra
plataforma: [meta]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: 00:06:52–00:07:30
perecivel: false
confianca: alta
versao: 1
```
Embora seja possível anunciar somente com uma conta de anúncios, crie sempre um gerenciador de negócios.
O professor afirma que organização dá ROI, ou retorno de investimento.

### U:f4736e839d1e5cb0:013 — Acessar as configurações do negócio pela conta de anúncios
```yaml
tipo: procedimento
plataforma: [meta]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: 00:06:52–00:08:11
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: acesso à conta de anúncios.
1. Abra o menu lateral e clique em "todas as ferramentas".
2. Entre em "configurações do negócio"; se o nome estiver cortado, passe o mouse sobre ele.
A autenticação de dois fatores pode solicitar um código.

### U:f4736e839d1e5cb0:014 — Gerenciador de negócios reúne ativos e acessos
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: 00:07:30–00:08:11
perecivel: true
confianca: alta
versao: 1
```
Nas configurações do negócio há áreas para pessoas, parceiros, páginas, contas de anúncio, contas do Instagram, contas do WhatsApp, pixels, domínios e integrações.
O professor diz que todos os ativos do negócio ficam reunidos ali.

### U:f4736e839d1e5cb0:015 — Gerenciador de negócios é apresentado como estrutura mais segura
```yaml
tipo: regra
plataforma: [meta]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: 00:08:12–00:08:45
perecivel: false
confianca: alta
versao: 1
```
Tenha perfil no Facebook, página no Facebook, perfil comercial no Instagram, conta de anúncios e gerenciador de negócios.
Segundo o professor, ter um gerenciador de negócios torna a conta mais respeitável aos olhos do Meta Ads e dificulta bloqueios.

### U:f4736e839d1e5cb0:016 — Gestor precisa apenas do próprio perfil pessoal
```yaml
tipo: decisao
plataforma: [meta]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: 00:08:45–00:09:22
perecivel: false
confianca: alta
versao: 1
```
Se você é gestor de tráfego, tenha o seu perfil pessoal no Facebook.
Você não precisa criar página, perfil comercial do Instagram, conta de anúncios nem gerenciador de negócios para o negócio do cliente.

### U:f4736e839d1e5cb0:017 — Ativos de anúncio pertencem ao dono do negócio
```yaml
tipo: regra
plataforma: [meta]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: 00:09:22–00:11:46
perecivel: false
confianca: alta
versao: 1
```
Página, perfil comercial do Instagram, conta de anúncios e gerenciador de negócios devem pertencer ao dono do negócio.
O gestor recebe acesso aos ativos, mas não é dono; o cliente pode retirar esse acesso.

### U:f4736e839d1e5cb0:018 — Cliente adiciona o gestor em Pessoas no gerenciador de negócios
```yaml
tipo: procedimento
plataforma: [meta]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: 00:09:22–00:10:37
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: gerenciador de negócios pertencente ao cliente.
1. O cliente entra em "pessoas" no próprio gerenciador de negócios.
2. Adiciona o gestor e atribui acesso aos ativos necessários.
O cliente não deve dar acesso ao perfil pessoal dele.

### U:f4736e839d1e5cb0:019 — Oriente o cliente a criar os próprios ativos
```yaml
tipo: decisao
plataforma: [meta]
tema: fundamentos-e-carreira
tarefas: [configurar-conta]
fonte: fala
faixa: 00:10:37–00:11:46
perecivel: false
confianca: alta
versao: 1
```
Se o cliente não tiver as estruturas, instrua-o a criar o próprio gerenciador de negócios, conta de anúncios, perfil comercial do Instagram e página do Facebook.
Se ele não souber fazer, faça uma videochamada e explique a importância de ele manter o controle completo desses ativos.

### U:f4736e839d1e5cb0:020 — A criação detalhada das estruturas fica para depois
```yaml
tipo: limite
plataforma: [meta]
tema: conta-e-configuracao
tarefas: []
fonte: fala
faixa: 00:11:11–00:11:46
perecivel: false
confianca: alta
versao: 1
```
A aula não ensina como criar cada uma das estruturas; isso será tratado nas próximas aulas.