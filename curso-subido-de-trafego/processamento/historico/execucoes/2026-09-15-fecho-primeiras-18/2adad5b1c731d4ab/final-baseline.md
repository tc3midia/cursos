---
type: unidades-aula
status: rascunho
title: "5.1 - Públicos Personalizados"
modulo: "002"
ordem: 26
aula_id: 2adad5b1c731d4ab
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

# 5.1 - Públicos Personalizados

## Contexto da aula
A aula apresenta os públicos personalizados no Meta Ads e suas fontes de criação.
Mostra a lógica dos públicos de site, aplicativo, catálogo, listas, vídeo, formulário e envolvimento.
A explicação assume familiaridade prévia com pixel, eventos e estrutura de campanha.
Públicos semelhantes ficam para a próxima aula, embora sejam classificados pelo Meta como personalizados.
Algumas fontes menos usuais são citadas sem demonstração detalhada.

## Unidades

### U:2adad5b1c731d4ab:001 — Caminhos para criar um público personalizado
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: "00:00:00–00:01:13"
perecivel: true
confianca: alta
versao: 1
```
O público personalizado pode ser criado durante a criação da campanha, na área de públicos pelo botão de criar, ou em “todas as ferramentas” e “anunciar públicos”.
Conheça mais de um caminho, pois menus podem mudar de lugar.

### U:2adad5b1c731d4ab:002 — Público personalizado reúne quem já teve contato
```yaml
tipo: conceito
plataforma: [meta]
tema: publicos
tarefas: []
fonte: fala
faixa: "00:01:49–00:02:31"
perecivel: false
confianca: alta
versao: 1
```
Públicos personalizados são formados por pessoas que já tiveram algum contato com você.
O curso separa públicos personalizados e semelhantes para facilitar a explicação, embora o Meta trate o semelhante como personalizado.

### U:2adad5b1c731d4ab:003 — Tipos visíveis de fonte podem mudar
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: "00:02:31–00:03:55"
perecivel: true
confianca: alta
versao: 1
```
A quantidade e os tipos mostrados em “suas fontes” e “fontes da Meta” podem mudar na interface.
Entenda o princípio da criação para replicá-lo quando surgir uma fonte nova.

### U:2adad5b1c731d4ab:004 — Pixel é necessário para público de site
```yaml
tipo: regra
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos, montar-publicos-personalizados]
fonte: fala
faixa: "00:03:11–00:04:36"
perecivel: false
confianca: alta
versao: 1
```
Instale o pixel no site antes de criar públicos de pessoas que o visitaram.
Sem pixel instalado, não é possível criar público de site.

### U:2adad5b1c731d4ab:005 — Retenção de todos os visitantes do site
```yaml
tipo: regua
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: "00:03:55–00:04:36"
perecivel: false
confianca: alta
versao: 1
```
O público de todos os visitantes do site aceita retenção de 1 até 180 dias.
A interface não aceita valor maior que 180 dias.

### U:2adad5b1c731d4ab:006 — Padrão de nome para visitantes do site
```yaml
tipo: procedimento
plataforma: [meta]
tema: nomenclatura
tarefas: [nomear-campanhas, montar-publicos-personalizados]
fonte: fala
faixa: "00:04:36–00:05:19"
perecivel: false
confianca: alta
versao: 1
```
Pré-condição: público criado para todas as pessoas que visitaram o site.
1. Comece o nome pelo tipo “site”.
2. Use “visitantes do site - ”.
3. Acrescente o período em dias, como “1D”.

### U:2adad5b1c731d4ab:007 — Selecione o pixel correto ao criar público de site
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: "00:05:19–00:05:52"
perecivel: true
confianca: alta
versao: 1
```
Na criação de público de site, confira se o pixel selecionado é o correto.
Contas usadas para demonstrações podem ter vários pixels e confundir a seleção.

### U:2adad5b1c731d4ab:008 — Crie públicos de visitantes em períodos pré-definidos
```yaml
tipo: regua
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: "00:05:52–00:06:33"
perecivel: false
confianca: alta
versao: 1
```
Deixe criados públicos de visitantes do site para 1, 3, 7, 14, 30, 60, 90 e 180 dias.
Outros períodos, como 45 ou 57 dias, podem ser criados, mas esses são os mais impactantes segundo o professor.

### U:2adad5b1c731d4ab:009 — Público de página específica replica uma conversão
```yaml
tipo: conceito
plataforma: [meta]
tema: publicos
tarefas: []
fonte: fala
faixa: "00:06:33–00:07:06"
perecivel: false
confianca: alta
versao: 1
```
Não se cria público a partir de conversão personalizada, mas é possível replicar a mesma lógica com pessoas que visitaram determinada página.
A base é usar a URL da página visitada.

### U:2adad5b1c731d4ab:010 — Informe domínio e caminho na URL do público
```yaml
tipo: procedimento
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: "00:07:06–00:08:30"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: criação de público de visitantes de uma página específica.
1. Remova “http://” ou “https://” da URL.
2. Informe o domínio seguido do caminho, como “pedrosobral.com.br/lives-semanais”.
3. Confirme que o valor inserido aparece com a caixa cinza ao redor.

### U:2adad5b1c731d4ab:011 — Nomeie público de página específica pelo destino
```yaml
tipo: procedimento
plataforma: [meta]
tema: nomenclatura
tarefas: [nomear-campanhas, montar-publicos-personalizados]
fonte: fala
faixa: "00:08:30–00:10:26"
perecivel: false
confianca: alta
versao: 1
```
Pré-condição: público baseado em uma URL ou página específica.
1. Comece por “site visitou”.
2. Adicione um nome compreensível para a página, como “lives semanais”.
3. Termine com “- YD”, substituindo Y pelo número de dias escolhido.

### U:2adad5b1c731d4ab:012 — Defina dias de página específica conforme o uso
```yaml
tipo: decisao
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: "00:09:09–00:10:26"
perecivel: false
confianca: alta
versao: 1
```
Se o público é de uma página muito específica, normalmente crie-o para 180 dias.
Quando a necessidade for recente, como visitantes da última semana, use o período que corresponde ao motivo da criação.

### U:2adad5b1c731d4ab:013 — Página de obrigado identifica cadastrados
```yaml
tipo: exemplo
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: "00:10:26–00:11:07"
perecivel: false
confianca: alta
versao: 1
```
Situação: a URL de agradecimento contém “/obrigado” após cadastro em uma live.
O que aconteceu: foi criado um público de visitantes dessa página nos últimos 180 dias.
Lógica: quem chegou à página de obrigado é tratado como cadastrado na live.

### U:2adad5b1c731d4ab:014 — Percentil de tempo gasto seleciona os mais engajados
```yaml
tipo: conceito
plataforma: [meta]
tema: publicos
tarefas: []
fonte: fala
faixa: "00:11:07–00:12:29"
perecivel: false
confianca: alta
versao: 1
```
O público por tempo gasto reúne o percentil de visitantes que passou mais tempo no site.
Os 10% que mais gastaram tempo são mais restritos que os 25%; também há referência aos 5%.

### U:2adad5b1c731d4ab:015 — Nomeie público por tempo gasto com percentil e dias
```yaml
tipo: procedimento
plataforma: [meta]
tema: nomenclatura
tarefas: [nomear-campanhas, montar-publicos-personalizados]
fonte: fala
faixa: "00:11:49–00:12:29"
perecivel: false
confianca: alta
versao: 1
```
Pré-condição: público de visitantes por tempo gasto no site.
1. Comece por “visitantes do site”.
2. Adicione o percentil, como “5%”.
3. Termine com a retenção, como “180 dias”, separando partes por espaço, hífen e espaço.

### U:2adad5b1c731d4ab:016 — Refine visitantes por frequência e dispositivo
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: "00:12:29–00:13:11"
perecivel: true
confianca: alta
versao: 1
```
Públicos de visitantes podem ser refinados pela frequência de visita e pelo dispositivo, como computador, iOS, Android ou qualquer dispositivo.
O professor apresenta esses refinadores como recursos que não serão usados com frequência.

### U:2adad5b1c731d4ab:017 — “Qualquer um dos” cria condição OU
```yaml
tipo: conceito
plataforma: [meta]
tema: publicos
tarefas: []
fonte: fala
faixa: "00:13:11–00:14:25"
perecivel: true
confianca: alta
versao: 1
```
Ao incluir mais pessoas com “qualquer um dos”, basta a pessoa cumprir uma das condições.
Exemplo: visitar lives semanais em 180 dias ou o blog em 30 dias.

### U:2adad5b1c731d4ab:018 — “Todos os” cria condição E
```yaml
tipo: conceito
plataforma: [meta]
tema: publicos
tarefas: []
fonte: fala
faixa: "00:14:25–00:15:05"
perecivel: true
confianca: alta
versao: 1
```
Ao trocar para “todos os”, a pessoa precisa cumprir todas as condições do público.
No exemplo, ela precisa ter visitado lives semanais em 180 dias e o blog em 30 dias.

### U:2adad5b1c731d4ab:019 — Domine os quatro tipos principais de público de site
```yaml
tipo: regra
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: "00:15:05–00:16:20"
perecivel: false
confianca: alta
versao: 1
```
Priorize dominar todos os visitantes do site, visitantes de páginas específicas, visitantes por tempo gasto e públicos baseados em evento.
Combinações de condições são apresentadas como testes avançados e pouco usados.

### U:2adad5b1c731d4ab:020 — Eventos padrão e personalizados podem formar públicos
```yaml
tipo: conceito
plataforma: [meta]
tema: pixel-e-eventos
tarefas: []
fonte: fala
faixa: "00:15:05–00:16:57"
perecivel: false
confianca: alta
versao: 1
```
Eventos padrão e personalizados servem para criar públicos de pessoas que ativaram determinado evento no site.
Conversões personalizadas aparecem para otimização e análise, mas não são apresentadas como base direta para esse público.

### U:2adad5b1c731d4ab:021 — Público de evento pode ser refinado
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: "00:16:20–00:16:57"
perecivel: true
confianca: alta
versao: 1
```
Ao criar público por evento, a interface permite refinamento por dispositivo e por valor agregado.
O professor orienta deixar o detalhe de valor agregado para depois.

### U:2adad5b1c731d4ab:022 — Padronize nome de público baseado em evento
```yaml
tipo: procedimento
plataforma: [meta]
tema: nomenclatura
tarefas: [nomear-campanhas, montar-publicos-personalizados]
fonte: fala
faixa: "00:16:57–00:17:40"
perecivel: false
confianca: alta
versao: 1
```
Pré-condição: público criado a partir de um evento instalado no site.
1. Use “site visitou” como início do padrão.
2. Inclua o nome do evento, como “lead”.
3. Acrescente o número de dias, como “180 dias”.

### U:2adad5b1c731d4ab:023 — Público de aplicativo só se aplica a quem tem app
```yaml
tipo: decisao
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: "00:17:40–00:18:41"
perecivel: false
confianca: alta
versao: 1
```
Se o negócio tiver aplicativo, crie públicos de quem abriu, usuários mais ativos e usuários por valor de compra.
A criação usa percentis de 5%, 10% e 25% para atividade e valor de compra.

### U:2adad5b1c731d4ab:024 — Crie variações completas de público de aplicativo
```yaml
tipo: regua
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: "00:18:44–00:19:29"
perecivel: false
confianca: alta
versao: 1
```
Para aplicativo, crie retenções de 1 até 180 dias para abertura, atividade e valor de compra.
Nos públicos percentuais, o professor orienta criar todos os períodos para 5%, 10% e 25%.

### U:2adad5b1c731d4ab:025 — Público de catálogo exige catálogo e conjuntos de produtos
```yaml
tipo: decisao
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: "00:19:29–00:20:12"
perecivel: false
confianca: alta
versao: 1
```
Se o negócio tiver e-commerce com catálogo e conjuntos de produtos, crie públicos de quem viu, adicionou ao carrinho ou comprou produtos do conjunto selecionado.
A retenção de catálogo vai até 180 dias.

### U:2adad5b1c731d4ab:026 — Conjunto de produtos pode agrupar itens caros
```yaml
tipo: exemplo
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: "00:20:15–00:21:35"
perecivel: false
confianca: alta
versao: 1
```
Situação: um e-commerce precisa separar produtos acima de R$ 500.
O que aconteceu: foi definido um conjunto de produtos chamado “mais de 500 reais”.
Lógica: o conjunto reúne produtos escolhidos para servir de base aos públicos de catálogo.

### U:2adad5b1c731d4ab:027 — Lista de clientes é enviada por contatos
```yaml
tipo: conceito
plataforma: [meta]
tema: publicos
tarefas: []
fonte: fala
faixa: "00:21:35–00:22:28"
perecivel: false
confianca: alta
versao: 1
```
Lista de clientes é uma lista de e-mails ou telefones enviada ao Meta Ads.
A informação base indicada pelo professor é o e-mail; quanto mais informações houver, melhor.

### U:2adad5b1c731d4ab:028 — Coluna de contatos não exige cabeçalho
```yaml
tipo: regra
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: "00:21:35–00:23:14"
perecivel: false
confianca: alta
versao: 1
```
A coluna com e-mails ou contatos da lista não precisa ter identificação no topo.
Ela pode ter ou não um cabeçalho, pois o Meta entende a lista como contatos das pessoas.

### U:2adad5b1c731d4ab:029 — Informe valor do cliente quando a lista o tiver
```yaml
tipo: decisao
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: "00:22:28–00:23:53"
perecivel: true
confianca: alta
versao: 1
```
Se a lista tiver quanto cada pessoa gastou, marque que ela inclui valor para cliente e envie esse valor.
Se os contatos forem apenas cadastrados sem gasto, marque que não há valor.

### U:2adad5b1c731d4ab:030 — Valor de cliente orienta pessoas semelhantes mais valiosas
```yaml
tipo: conceito
plataforma: [meta]
tema: publicos
tarefas: []
fonte: fala
faixa: "00:23:14–00:23:53"
perecivel: false
confianca: alta
versao: 1
```
Quando a lista inclui valor gasto, o Meta entende que clientes com gasto maior são mais valiosos.
O professor afirma que a ferramenta tentará encontrar mais pessoas parecidas com o cliente de maior valor.

### U:2adad5b1c731d4ab:031 — Nome de lista usa M de mutável e data
```yaml
tipo: procedimento
plataforma: [meta]
tema: nomenclatura
tarefas: [nomear-campanhas, montar-publicos-personalizados]
fonte: fala
faixa: "00:23:53–00:25:42"
perecivel: false
confianca: alta
versao: 1
```
Pré-condição: arquivo de lista de clientes ou cadastrados pronto para envio.
1. Comece por “lista M”, usando M para “mutável”.
2. Inclua dia e mês da atualização, como “27/03”.
3. Acrescente o nome da lista, como “lista de cadastrados na aula”.

### U:2adad5b1c731d4ab:032 — Atualize lista mutável e sua data
```yaml
tipo: regra
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: "00:25:03–00:25:42"
perecivel: false
confianca: alta
versao: 1
```
Atualize periodicamente a lista mutável existente quando houver novos cadastrados ou clientes.
Ao atualizar, altere a data presente no nome do público.

### U:2adad5b1c731d4ab:033 — Marque LTV no nome quando a lista contém valor
```yaml
tipo: decisao
plataforma: [meta]
tema: nomenclatura
tarefas: [nomear-campanhas, montar-publicos-personalizados]
fonte: fala
faixa: "00:25:42–00:26:24"
perecivel: false
confianca: alta
versao: 1
```
Se a lista contiver LTV ou o valor gasto pela pessoa, adicione “- LTV” ao fim do nome.
Se ela não contiver valor, não use essa marca.

### U:2adad5b1c731d4ab:034 — Atividade offline fica para negócio local
```yaml
tipo: limite
plataforma: [meta]
tema: publicos
tarefas: []
fonte: fala
faixa: "00:26:24–00:27:04"
perecivel: false
confianca: alta
versao: 1
```
A aula não explica como criar públicos de atividade offline.
O professor direciona esse assunto, como pessoas que visitaram loja física, para o curso de tráfego para negócio local.

### U:2adad5b1c731d4ab:035 — Público de vídeo usa marcos mínimos de visualização
```yaml
tipo: conceito
plataforma: [meta]
tema: publicos
tarefas: []
fonte: fala
faixa: "00:27:04–00:29:38"
perecivel: false
confianca: alta
versao: 1
```
Públicos de vídeo podem considerar quem viu pelo menos 3, 10 ou 15 segundos, ou pelo menos 25%, 50%, 75% e 95%.
“Pelo menos” significa que quem alcança uma marca posterior também pertence às marcas anteriores.

### U:2adad5b1c731d4ab:036 — Públicos de vídeo são conjuntos contidos
```yaml
tipo: exemplo
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: "00:29:38–00:32:36"
perecivel: false
confianca: alta
versao: 2
nota: "Correção mecânica por gpt-5.6-sol: tarefa obrigatória associada ao exemplo."
```
Situação: um vídeo de 100 segundos teve 50 pessoas que chegaram a 95% e 150 que chegaram a 75%.
O que aconteceu: as 50 pessoas de 95% também ficaram dentro do público de 75% e dos marcos anteriores.
Lógica: cada marco posterior está contido nos públicos de visualização mínima anteriores.

### U:2adad5b1c731d4ab:037 — Nome de vídeo usa M, data, retenção e marco
```yaml
tipo: procedimento
plataforma: [meta]
tema: nomenclatura
tarefas: [nomear-campanhas, montar-publicos-personalizados]
fonte: fala
faixa: "00:32:36–00:34:38"
perecivel: false
confianca: alta
versao: 1
```
Pré-condição: público criado a partir de vídeos selecionados.
1. Use M e a data, pois novos vídeos exigem atualização do público.
2. Identifique os vídeos selecionados, como “view video” ou equivalente.
3. Acrescente o marco de visualização e o número de dias.
4. Evite acentos no nome, conforme recomendação do professor.

### U:2adad5b1c731d4ab:038 — Retenção de vídeo vai de 180 até 365 dias
```yaml
tipo: regua
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: "00:33:50–00:34:38"
perecivel: false
confianca: alta
versao: 1
```
Públicos de vídeo podem ser criados com retenção de 180 até 365 dias.
O professor recomenda priorizar os marcos de 25%, 50%, 75% e 95%, em vez de 3, 10 e 15 segundos.

### U:2adad5b1c731d4ab:039 — Retargete quem viu anúncio e não chegou à página
```yaml
tipo: exemplo
plataforma: [meta]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos]
fonte: fala
faixa: "00:34:38–00:35:16"
perecivel: false
confianca: alta
versao: 1
```
Situação: uma pessoa viu um anúncio, mas não chegou à página de conversão.
O que aconteceu: o público de quem viu o anúncio foi usado excluindo quem chegou à página.
Lógica: o professor trata esse grupo como pessoas que viram o anúncio, mas não converteram.

### U:2adad5b1c731d4ab:040 — Nome de público de vídeo aceita no máximo 50 caracteres
```yaml
tipo: regua
plataforma: [meta]
tema: nomenclatura
tarefas: [nomear-campanhas, montar-publicos-personalizados]
fonte: fala
faixa: "00:35:16–00:35:59"
perecivel: true
confianca: alta
versao: 1
```
O nome de público de vídeo tem máximo de 50 caracteres.
Quando faltar espaço, o professor sugere remover “viu o vídeo” e deixar apenas a identificação mais curta.

### U:2adad5b1c731d4ab:041 — Vídeos podem ser encontrados por página, Instagram ou campanha
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: "00:35:59–00:37:46"
perecivel: true
confianca: alta
versao: 1
```
Na seleção de vídeos, a origem pode ser página do Facebook, perfil empresarial do Instagram ou campanha.
A listagem pode incluir anúncios e vídeos publicados.

### U:2adad5b1c731d4ab:042 — Priorize quatro retenções para público de vídeo
```yaml
tipo: regua
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: "00:37:46–00:38:54"
perecivel: false
confianca: alta
versao: 1
```
Entre 1, 3, 7, 14, 30, 60, 90, 180 e 365 dias, o professor diz usar mais 7, 30, 180 e 365 dias.
O período de 1 dia é apontado como raramente utilizado.

### U:2adad5b1c731d4ab:043 — Criar várias cópias acelera a montagem de vídeo
```yaml
tipo: procedimento
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: "00:38:54–00:40:36"
perecivel: true
confianca: alta
versao: 1
nota: "O professor chama a prática de rataria e demonstra criação repetida por cliques rápidos."
```
Pré-condição: vídeos já selecionados e público de vídeo configurado.
1. Clique rapidamente várias vezes em “criar público” para gerar cópias.
2. Entre em cada cópia e edite a retenção e o nome.
3. Atualize o público após mudar a retenção; mudar apenas o nome não basta.
4. Apague os públicos de exemplo que não devem ser usados.

### U:2adad5b1c731d4ab:044 — Público de formulário tem três estados
```yaml
tipo: conceito
plataforma: [meta]
tema: publicos
tarefas: []
fonte: fala
faixa: "00:40:36–00:42:07"
perecivel: false
confianca: alta
versao: 1
```
Formulário de cadastro é aberto dentro do Facebook ou Instagram após o clique no anúncio, sem exigir envio ao site.
É possível criar público de quem abriu, abriu mas não enviou, e abriu e enviou o formulário.

### U:2adad5b1c731d4ab:045 — Retenção de formulário vai até 90 dias
```yaml
tipo: regua
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: "00:41:14–00:42:07"
perecivel: false
confianca: alta
versao: 1
```
Públicos de formulário aceitam retenção máxima de 90 dias.
O professor lista 1, 7, 14, 30, 60 e 90 dias e aponta 90 dias como o mais utilizado.

### U:2adad5b1c731d4ab:046 — Fontes menos usuais não recebem explicação detalhada
```yaml
tipo: limite
plataforma: [meta]
tema: publicos
tarefas: []
fonte: fala
faixa: "00:42:07–00:44:03"
perecivel: false
confianca: alta
versao: 1
```
A aula não detalha a criação de públicos de experiência instantânea, compras, experiência AR, eventos e classificados do Facebook.
O professor diz que esses tipos normalmente não serão usados e que a lógica de criação é a mesma.

### U:2adad5b1c731d4ab:047 — Envolvimento do Instagram tem tipos específicos
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: "00:44:03–00:46:18"
perecivel: true
confianca: alta
versao: 1
```
No perfil do Instagram, a interface permite públicos de todos, seguidores, visitou o perfil, salvou, enviou mensagem e engajou com publicações.
Seguidores não permite definir número de dias; os demais usam retenção de até 365 dias.

### U:2adad5b1c731d4ab:048 — Padronize nome de envolvimento do Instagram
```yaml
tipo: procedimento
plataforma: [meta]
tema: nomenclatura
tarefas: [nomear-campanhas, montar-publicos-personalizados]
fonte: fala
faixa: "00:44:03–00:47:29"
perecivel: false
confianca: alta
versao: 1
```
Pré-condição: público de envolvimento de uma conta do Instagram.
1. Comece por “IG”.
2. Inclua “envolvimento” e o tipo, como seguidores, visitou, salvou, direct ou engajou.
3. Adicione o arroba da conta e, quando permitido, o número de dias.

### U:2adad5b1c731d4ab:049 — Página do Facebook acrescenta público de clique em botão
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: "00:47:29–00:48:48"
perecivel: true
confianca: alta
versao: 1
```
Na página do Facebook, há públicos de curtem ou seguem, todos que engajaram, visitou a página, engajou com publicações, clicou em botão de chamada para ação, enviou mensagem e salvou.
Curtem ou seguem não permite número de dias; o tipo de clique é apresentado como opção adicional em relação ao Instagram.

### U:2adad5b1c731d4ab:050 — Configurar públicos é parte vendável do serviço do gestor
```yaml
tipo: regra
plataforma: [meta]
tema: fundamentos-e-carreira
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: "00:48:48–00:50:08"
perecivel: false
confianca: alta
versao: 1
```
Ao vender serviço de gestão de tráfego, apresente a configuração e criação dos públicos possíveis na conta do cliente como parte do serviço.
O professor trata essa configuração como trabalho que alguém precisa executar e como ativo da conta.
