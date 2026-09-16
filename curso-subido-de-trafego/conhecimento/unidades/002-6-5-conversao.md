---
type: unidades-aula
status: validado
title: "6.5 - Conversão"
modulo: "002"
ordem: 35
aula_id: 7c86762dc9b85fdf
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

# 6.5 - Conversão

## Contexto da aula
A aula configura a parte de conversão no conjunto de anúncios do Meta após as escolhas de campanha.
Ela retoma objetivo, localização da conversão, meta de desempenho, pixel, evento e atribuição.
Assume que o aluno já estudou pixel, eventos, objetivos de campanha e janela de atribuição.
A demonstração usa uma campanha de cadastro para site como exemplo principal.
Campanhas e configurações específicas de Google Ads ficam para outro módulo.

## Unidades

### U:7c86762dc9b85fdf:001 — Alinhar localização da conversão ao objetivo da campanha
```yaml
tipo: decisao
plataforma: [meta]
tema: objetivos
tarefas: [definir-conversoes-e-metas]
fonte: fala
faixa: "00:00:00–00:02:04"
perecivel: true
confianca: alta
versao: 1
```
Se a campanha busca cadastros no aplicativo, selecione o aplicativo como localização; se busca levar pessoas ao site para se cadastrar, selecione o site.
Formulário instantâneo serve para cadastro feito dentro do próprio Meta ou Instagram.
O objetivo selecionado limita as localizações de conversão disponíveis.

### U:7c86762dc9b85fdf:002 — Escolher meta de reconhecimento pelo resultado desejado
```yaml
tipo: decisao
plataforma: [meta]
tema: objetivos
tarefas: [definir-conversoes-e-metas]
fonte: fala
faixa: "00:02:05–00:02:42"
perecivel: true
confianca: alta
versao: 1
```
Se o objetivo for reconhecimento, escolha alcance para atingir mais pessoas, impressões para aparecer mais vezes ou incrementalidade da lembrança para aumentar a lembrança do anúncio.

### U:7c86762dc9b85fdf:003 — Usar clique no link sem pixel no tráfego
```yaml
tipo: decisao
plataforma: [meta]
tema: objetivos
tarefas: [definir-conversoes-e-metas]
fonte: fala
faixa: "00:02:42–00:03:05"
condicoes: "campanha de tráfego sem pixel instalado no site"
perecivel: false
confianca: alta
versao: 1
```
Se não houver pixel instalado no site, use clique no link como meta de desempenho da campanha de tráfego.
Essa meta busca muitos cliques, sem foco equivalente no carregamento da página.

### U:7c86762dc9b85fdf:004 — Usar visualização da página com pixel instalado
```yaml
tipo: decisao
plataforma: [meta]
tema: objetivos
tarefas: [definir-conversoes-e-metas]
fonte: fala
faixa: "00:02:42–00:03:05"
condicoes: "campanha de tráfego com pixel instalado no site"
perecivel: false
confianca: alta
versao: 1
```
Se o pixel estiver instalado no site, use visualização da página para focar no carregamento da página.

### U:7c86762dc9b85fdf:005 — Meta de desempenho acompanha a localização escolhida
```yaml
tipo: regra
plataforma: [meta]
tema: objetivos
tarefas: [definir-conversoes-e-metas]
fonte: fala
faixa: "00:03:07–00:04:31"
perecivel: true
confianca: alta
versao: 1
```
A localização da conversão define a meta de desempenho que o Meta seleciona por padrão.
No aplicativo de mensagens e na página do Facebook, a meta adequada já vem selecionada; no anúncio, escolha visualização de vídeo ou interação com a publicação.

### U:7c86762dc9b85fdf:006 — Distinguir metas de promoção de aplicativo
```yaml
tipo: decisao
plataforma: [meta]
tema: objetivos
tarefas: [definir-conversoes-e-metas]
fonte: fala
faixa: "00:03:48–00:04:31"
perecivel: true
confianca: alta
versao: 1
```
Se a campanha de promoção de aplicativo buscar novos usuários, selecione instalação do aplicativo.
Se buscar uma ação específica, selecione evento no aplicativo, inclusive para usuários que já instalaram.

### U:7c86762dc9b85fdf:007 — Meta de cadastro maximiza conversões
```yaml
tipo: regra
plataforma: [meta]
tema: objetivos
tarefas: [definir-conversoes-e-metas]
fonte: fala
faixa: "00:03:48–00:04:31"
perecivel: true
confianca: alta
versao: 1
```
Para cadastro no site, formulário instantâneo ou Instagram Messenger, a meta de desempenho indicada é maximizar o número de conversões.

### U:7c86762dc9b85fdf:008 — Escolher entre quantidade e valor em vendas no site
```yaml
tipo: decisao
plataforma: [meta]
tema: objetivos
tarefas: [definir-conversoes-e-metas]
fonte: fala
faixa: "00:04:31–00:05:16"
perecivel: true
confianca: alta
versao: 1
```
Se uma campanha de vendas usar o site como localização, escolha entre maximizar conversões para buscar mais clientes novos ou maximizar o valor da conversão para focar em quem gasta mais.

### U:7c86762dc9b85fdf:009 — Catálogo limita a meta à quantidade de conversões
```yaml
tipo: regra
plataforma: [meta]
tema: objetivos
tarefas: [criar-campanha-de-catalogo, definir-conversoes-e-metas]
fonte: fala
faixa: "00:04:38–00:05:16"
perecivel: true
confianca: media
versao: 1
nota: "O professor consulta a tela para confirmar a opção e afirma que catálogo permite maximizar o número de conversões."
```
Com catálogo selecionado em campanha de vendas, use maximizar o número de conversões; a tela não permite maximizar o valor da conversão.

### U:7c86762dc9b85fdf:010 — Priorizar a métrica principal antes de testes terciários
```yaml
tipo: regra
plataforma: [meta]
tema: testes-e-experimentos
tarefas: [rodar-testes-e-experimentos]
fonte: fala
faixa: "00:05:16–00:05:51"
perecivel: false
confianca: alta
versao: 1
```
Foque primeiro na métrica principal da campanha.
Testar cliques ou impressões como meta é válido, mas o professor o trata como teste terciário ou posterior, parecido com testar estratégia de lance.

### U:7c86762dc9b85fdf:011 — Selecionar o evento que representa a ação buscada
```yaml
tipo: procedimento
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [definir-conversoes-e-metas, instalar-pixel-e-eventos]
fonte: fala
faixa: "00:05:52–00:07:11"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: pixel e evento de conversão instalados no site.
1. Selecione o pixel da conta; normalmente há um único pixel.
2. Escolha o evento que corresponde ao resultado buscado, como compra ou cadastro.
3. Para cadastro, confirme que o evento Lead/Cadastro dispara na página de obrigado após o envio.

### U:7c86762dc9b85fdf:012 — Eventos podem ser padrão, personalizados ou conversões personalizadas
```yaml
tipo: conceito
plataforma: [meta]
tema: pixel-e-eventos
tarefas: []
fonte: fala
faixa: "00:06:31–00:07:11"
perecivel: false
confianca: alta
versao: 2
nota: "Correção mecânica por gpt-5.6-sol: título reduzido ao limite de 80 caracteres."
```
Há três tipos de eventos de conversão: evento padrão, evento personalizado e conversão personalizada.
O professor cita o Google Tag Manager para instalar esses eventos no site.

### U:7c86762dc9b85fdf:013 — Janela de atribuição define até quando crédito vai ao anúncio
```yaml
tipo: conceito
plataforma: [meta]
tema: atribuicao
tarefas: []
fonte: fala
faixa: "00:07:11–00:08:43"
perecivel: false
confianca: alta
versao: 1
```
A janela de atribuição determina por quanto tempo uma conversão pode ser atribuída a um clique ou visualização de anúncio.
No exemplo, um clique recebe crédito se a pessoa converter 5 dias depois sem interagir com outro anúncio; uma visualização pode receber crédito se a conversão ocorrer 13 horas depois sem nova interação.

### U:7c86762dc9b85fdf:014 — Iniciante não deve mexer na configuração de atribuição
```yaml
tipo: decisao
plataforma: [meta]
tema: atribuicao
tarefas: [configurar-janela-de-atribuicao]
fonte: fala
faixa: "00:08:00–00:08:52"
perecivel: true
confianca: alta
versao: 1
```
Se você é muito iniciante e tem dúvida sobre janela de atribuição, não mexa na configuração.
Para quem já é mais avançado, o professor menciona janela de clique de 1 dia e janela de visualização de nenhum dia.

### U:7c86762dc9b85fdf:015 — Ajustar a janela ao padrão de conversão do usuário
```yaml
tipo: decisao
plataforma: [meta]
tema: atribuicao
tarefas: [configurar-janela-de-atribuicao]
fonte: fala
faixa: "00:08:54–00:10:07"
perecivel: true
confianca: alta
versao: 1
```
Se a decisão de compra costuma levar mais tempo, como na compra de uma geladeira, prefira 7 dias em vez de 1 dia.
Se a ação costuma ocorrer no mesmo dia, como baixar um livro gratuito, 1 dia pode funcionar.
A recomendação do Meta, citada pelo professor, é usar a janela mais adequada ao comportamento do usuário.

### U:7c86762dc9b85fdf:016 — Preferência do professor por janela de 7 dias
```yaml
tipo: regua
plataforma: [meta]
tema: atribuicao
tarefas: [configurar-janela-de-atribuicao]
fonte: fala
faixa: "00:09:34–00:10:45"
condicoes: "preferência pessoal do professor; testar o que funciona para a campanha"
perecivel: true
confianca: alta
versao: 1
```
O professor prefere manter 7 dias nas campanhas porque, na opinião dele, isso traz mais dados.
A janela escolhida orienta o Meta a procurar pessoas com tendência de converter dentro daquele prazo.

### U:7c86762dc9b85fdf:017 — Janela de engajamento considera 10 segundos de vídeo
```yaml
tipo: regua
plataforma: [meta]
tema: atribuicao
tarefas: [configurar-janela-de-atribuicao]
fonte: fala
faixa: "00:10:45–00:11:22"
perecivel: true
confianca: alta
versao: 1
```
A janela de engajamento considera quem assistiu pelo menos 10 segundos do vídeo.
O professor não vê sentido em mantê-la em 1 dia porque ela conta junto com a janela de visualização.

### U:7c86762dc9b85fdf:018 — Google tem janela padrão de visualização de vídeo de 3 dias
```yaml
tipo: regua
plataforma: [google]
tema: atribuicao
tarefas: [configurar-janela-de-atribuicao]
fonte: fala
faixa: "00:10:45–00:11:22"
perecivel: false
confianca: alta
versao: 1
nota: "O professor afirma que, no Google, a janela de visualização de vídeo é de 3 dias por padrão e informa que o tema será tratado no módulo de Google Ads."
```
No Google, a janela de visualização de vídeo é de 3 dias por padrão e pode ser configurada para um prazo maior.

### U:7c86762dc9b85fdf:019 — Pixel é selecionado para conversões no site
```yaml
tipo: regra
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos, definir-conversoes-e-metas]
fonte: fala
faixa: "00:11:22–00:14:26"
perecivel: true
confianca: media
versao: 1
nota: "Durante a demonstração, o professor corrige a própria afirmação sobre tráfego e verifica que engajamento com conversão no site permite selecionar pixel."
```
Selecione pixel quando a campanha levar a pessoa ao site e precisar medir ações feitas ali.
Em vendas e cadastros, a configuração usa pixel; para engajamento no anúncio, selecione o tipo de engajamento, sem pixel.

### U:7c86762dc9b85fdf:020 — Não usar engajamento para buscar conversão como regra
```yaml
tipo: regra
plataforma: [meta]
tema: objetivos
tarefas: [escolher-objetivo-de-campanha]
fonte: fala
faixa: "00:13:02–00:14:26"
perecivel: false
confianca: alta
versao: 1
```
Não use campanha de engajamento para fazer conversão, salvo se quiser realizar um teste muito específico.
O professor relata que já testou e não deu certo para ele, mas orienta cada pessoa a testar por si.
