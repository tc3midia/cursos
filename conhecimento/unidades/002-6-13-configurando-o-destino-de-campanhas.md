---
type: unidades-aula
status: validado
title: "6.13 - Configurando o Destino de campanhas"
modulo: "002"
ordem: 43
aula_id: 2e7295a14c7a318f
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

# 6.13 - Configurando o Destino de campanhas

## Contexto da aula

A aula configura o destino de campanhas no Meta conforme a localização da conversão.
Ela demonstra destinos para site, experiência instantânea, formulário, mensagens, ligações e aplicativo.
Também diferencia experiência instantânea de formulário instantâneo e mostra opções de rastreamento.
O detalhamento de formulários, automação e parâmetros dinâmicos fica para outros conteúdos.

## Unidades

### U:2e7295a14c7a318f:001 — Destino após o anúncio influencia o resultado
```yaml
tipo: conceito
plataforma: [meta]
tema: destino-e-landing-page
tarefas: []
fonte: fala
faixa: 00:00:00–00:01:01
perecivel: false
confianca: alta
versao: 1
```
O que acontece depois que a pessoa vê, engaja, clica ou entra em contato pelo anúncio é um fator para o sucesso ou fracasso do tráfego pago.
As opções de destino estão ligadas à localização da conversão escolhida.

### U:2e7295a14c7a318f:002 — Destinos disponíveis para conversão no site
```yaml
tipo: conceito
plataforma: [meta]
tema: destino-e-landing-page
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:01:04–00:01:43
condicoes: "quando a localização da conversão é site"
perecivel: false
confianca: alta
versao: 1
```
Com conversão no site, os destinos possíveis são site, experiência instantânea e evento do Facebook.
O destino de site exige uma URL.

### U:2e7295a14c7a318f:003 — Repetir o domínio no título de exibição
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: destino-e-landing-page
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:01:43–00:02:26
perecivel: true
confianca: alta
versao: 1
```
Ao usar um site, o Meta mostra o domínio como prévia; o professor prefere escrever o domínio de novo no título ou link de exibição para evitar uma mudança futura da plataforma.

### U:2e7295a14c7a318f:004 — Uma campanha deve focar uma ação
```yaml
tipo: decisao
plataforma: [meta]
tema: objetivos
tarefas: [criar-campanha]
fonte: fala
faixa: 00:02:26–00:03:04
perecivel: false
confianca: alta
versao: 1
```
Se quiser que a pessoa ligue, crie uma campanha voltada para ligação em vez de combinar ligação com uma campanha de clique no link.
Se precisar de duas ações, faça duas campanhas, cada uma focada em uma ação.

### U:2e7295a14c7a318f:005 — Não usar complementos de navegador em campanha de link
```yaml
tipo: regra
plataforma: [meta]
tema: destino-e-landing-page
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:01:43–00:03:04
perecivel: true
confianca: alta
versao: 1
```
Em campanha para a pessoa clicar no link, o professor prefere selecionar nenhum complemento do navegador.
Pedir clique no link e ligação na mesma campanha não faz sentido para ele.

### U:2e7295a14c7a318f:006 — O destino altera posicionamentos suportados
```yaml
tipo: conceito
plataforma: [meta]
tema: posicionamentos-e-formatos
tarefas: [escolher-canais-e-posicionamentos]
fonte: fala
faixa: 00:03:05–00:04:00
perecivel: true
confianca: alta
versao: 1
```
Ao trocar o destino, ativos personalizados podem precisar ser removidos e alguns posicionamentos deixam de aparecer.
Mesmo com posicionamento automático, o destino pode alterar os posicionamentos suportados.

### U:2e7295a14c7a318f:007 — Experiência instantânea abre dentro do celular
```yaml
tipo: conceito
plataforma: [meta]
tema: destino-e-landing-page
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:04:00–00:05:09
perecivel: false
confianca: alta
versao: 1
```
A experiência instantânea abre em tela cheia no celular após o clique no anúncio, parecendo uma página sem ser um site.
Ela pode conter carrossel, imagem, vídeo, texto e botão clicável.

### U:2e7295a14c7a318f:008 — Testar experiência instantânea com ressalva de resultado
```yaml
tipo: decisao
plataforma: [meta]
tema: destino-e-landing-page
tarefas: [rodar-testes-e-experimentos]
fonte: fala
faixa: 00:05:09–00:05:48
perecivel: false
confianca: alta
versao: 1
```
Se quiser usar experiência instantânea, pode testar, mas o professor relata que uma réplica de sua página não funcionou tão bem.
Ele diz que a minoria tem resultado e que normalmente ela não funciona legal.

### U:2e7295a14c7a318f:009 — Criar experiência instantânea pela campanha
```yaml
tipo: procedimento
plataforma: [meta]
tema: destino-e-landing-page
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:05:48–00:06:35
perecivel: true
confianca: media
versao: 1
nota: "O professor afirma que pode estar errado sobre a existência de um menu específico."
```
Pré-condição: campanha em criação com experiência instantânea como destino.
1. Clique em experiência instantânea.
2. Aperte em criar nova.
3. Escolha um dos modelos oferecidos, como aquisição de cliente, ou inicie uma experiência do zero.

### U:2e7295a14c7a318f:010 — Configurar componentes da experiência instantânea
```yaml
tipo: procedimento
plataforma: [meta]
tema: destino-e-landing-page
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:06:23–00:09:00
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: editor de uma experiência instantânea aberto.
1. Substitua imagens e defina URLs de destino para imagens, botões e itens de carrossel.
2. Adicione componentes como vídeo e bloco de texto.
3. Ajuste texto, cores, tamanho de letra, espaçamento e preenchimento do componente.
4. Nos três pontinhos, abra configurações avançadas para alterar, por exemplo, o preenchimento superior.

### U:2e7295a14c7a318f:011 — Duplicar uma experiência instantânea existente
```yaml
tipo: procedimento
plataforma: [meta]
tema: destino-e-landing-page
tarefas: [replicar-campanhas-e-grupos]
fonte: fala
faixa: 00:09:00–00:10:17
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: existir uma experiência instantânea já criada.
1. Selecione a experiência instantânea existente.
2. Abra a prévia.
3. Duplique a experiência.
4. Altere o nome e faça as configurações necessárias na cópia.

### U:2e7295a14c7a318f:012 — Evento do Facebook é destino para ingresso do evento
```yaml
tipo: decisao
plataforma: [meta]
tema: destino-e-landing-page
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:10:17–00:10:31
condicoes: "quando a campanha é para vender ingressos de um evento no Facebook"
perecivel: true
confianca: alta
versao: 1
```
Se a conversão for um evento do Facebook, use o destino de evento e informe o nome ou URL do evento.
O professor diz que normalmente enviaria a pessoa para uma página de venda de ingresso.

### U:2e7295a14c7a318f:013 — Formulário instantâneo é o destino da conversão por formulário
```yaml
tipo: conceito
plataforma: [meta]
tema: destino-e-landing-page
tarefas: [criar-campanha-de-formulario]
fonte: fala
faixa: 00:10:17–00:11:19
condicoes: "quando a localização da conversão é formulário instantâneo"
perecivel: true
confianca: alta
versao: 1
```
Com localização da conversão em formulário instantâneo, o destino é o formulário instantâneo.
Na tela é possível duplicar um formulário existente ou criar um formulário.

### U:2e7295a14c7a318f:014 — Mais perguntas reduzem preenchimentos
```yaml
tipo: regra
plataforma: [meta]
tema: destino-e-landing-page
tarefas: [criar-campanha-de-formulario]
fonte: fala
faixa: 00:11:19–00:11:58
perecivel: false
confianca: alta
versao: 1
```
Quanto mais informações forem pedidas no formulário instantâneo, menos pessoas vão preenchê-lo.
O formulário pode pedir dados como e-mail, nome completo, endereço, cidade, país e perguntas abertas.

### U:2e7295a14c7a318f:015 — Usar formulário para captar cadastros sem site
```yaml
tipo: decisao
plataforma: [meta]
tema: destino-e-landing-page
tarefas: [criar-campanha-de-formulario]
fonte: fala
faixa: 00:11:19–00:12:32
condicoes: "quando não há site e o objetivo é coletar cadastros"
perecivel: false
confianca: alta
versao: 1
```
Se não tiver site e quiser coletar cadastros, use formulário instantâneo.

### U:2e7295a14c7a318f:016 — Caminho alternativo para formulários instantâneos
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: destino-e-landing-page
tarefas: [criar-campanha-de-formulario]
fonte: fala
faixa: 00:11:58–00:13:07
perecivel: true
confianca: alta
versao: 1
```
Além de criar o formulário no anúncio, a alternativa demonstrada é Todas as ferramentas > Meta Business Suite > Todas as ferramentas > Formulários instantâneos.
O professor alerta que o menu é atualizado toda semana; se não estiver disponível, crie pelo anúncio.

### U:2e7295a14c7a318f:017 — Experiência instantânea e formulário não são iguais
```yaml
tipo: conceito
plataforma: [meta]
tema: destino-e-landing-page
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:12:33–00:13:44
perecivel: false
confianca: alta
versao: 1
```
Experiência instantânea é uma página criada dentro do Meta; formulário instantâneo é um formulário para solicitar informações.
Nos dois casos a pessoa permanece dentro do Facebook ou Instagram e o conteúdo carrega na ferramenta.

### U:2e7295a14c7a318f:018 — Baixar ou enviar cadastros para CRM
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: destino-e-landing-page
tarefas: [criar-campanha-de-formulario]
fonte: fala
faixa: 00:13:08–00:14:19
perecivel: true
confianca: alta
versao: 1
```
Na área de formulários instantâneos, os cadastros podem ser baixados como lista.
Também é possível configurar o envio direto para uma ferramenta de CRM; o professor cita o Make e informa que automação é outro assunto.

### U:2e7295a14c7a318f:019 — Destinos para mensagens, ligação e aplicativo
```yaml
tipo: conceito
plataforma: [meta]
tema: destino-e-landing-page
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:14:19–00:14:53
perecivel: true
confianca: alta
versao: 1
```
Para Messenger ou Instagram, o destino exibido é modelo de mensagem; para ligações, é ligações.
Para aplicativo, o destino pode ser aplicativo ou experiência instantânea, que pode direcionar a pessoa ao aplicativo.

### U:2e7295a14c7a318f:020 — Rastrear eventos do site ao enviar pessoas para o site
```yaml
tipo: regra
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: 00:14:53–00:15:30
condicoes: "quando o anúncio envia pessoas para o site"
perecivel: true
confianca: alta
versao: 1
```
Ao mandar pessoas para o site, mantenha selecionados os eventos do site para rastreamento.
O professor diz que a plataforma os seleciona automaticamente e não permite desmarcá-los.

### U:2e7295a14c7a318f:021 — Parâmetros de URL identificam a origem do clique
```yaml
tipo: conceito
plataforma: [meta]
tema: atribuicao
tarefas: [ler-metricas-e-relatorios]
fonte: fala
faixa: 00:15:30–00:16:50
perecivel: false
confianca: alta
versao: 1
```
Parâmetros de URL adicionam informações à URL do site, como campanha, anúncio, conjunto de anúncios e posicionamento do clique.
Para ler essas informações, o professor diz que é necessário usar Google Analytics.

### U:2e7295a14c7a318f:022 — Google Analytics tende a ser mais confiável para essa leitura
```yaml
tipo: regra
plataforma: [meta]
tema: atribuicao
tarefas: [ler-metricas-e-relatorios]
fonte: fala
faixa: 00:16:50–00:17:33
perecivel: false
confianca: alta
versao: 1
```
Para ler dados trazidos pelos parâmetros de URL, o professor afirma que o Google Analytics tende a ser mais confiável que o Meta.

### U:2e7295a14c7a318f:023 — Parâmetros dinâmicos ficam para o curso de Analytics
```yaml
tipo: limite
plataforma: [meta]
tema: atribuicao
tarefas: []
fonte: fala
faixa: 00:17:33–00:18:17
perecivel: true
confianca: alta
versao: 1
```
A aula não detalha o uso dos parâmetros dinâmicos de rastreamento do Meta.
O professor indica especificações de parâmetros dinâmicos e diz que o uso será aprendido no curso de Google Analytics, com link no material extra da aula.