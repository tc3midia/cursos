---
type: unidades-aula
status: rascunho
title: "2.0 - Criando campanhas na Rede de Pesquisa na prática"
modulo: "004"
ordem: 63
aula_id: ce348cdaad0663cc
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - cst_m04_a02_criando_campanhas_na_rede_de_pesquisa_na_pratica.pdf
  - transcricao.md
extraido_em: 2026-09-16
gerado_por: gpt-5.6-terra
retiradas: []
divisoes: []
fusoes: []
---

# 2.0 - Criando campanhas na Rede de Pesquisa na prática

## Contexto da aula

A aula demonstra a criação de uma primeira campanha de Rede de Pesquisa no Google Ads.
Parte de uma planilha já preparada com palavras-chave e usa como exemplo uma campanha de leads.
Mostra configurações de campanha, grupo de anúncios, anúncio e publicação.
Também apresenta extensões de anúncio e formas de configurá-las.
Segmentos de público, grupos dinâmicos, landing pages, otimização e cópias de anúncios ficam para aulas posteriores.

## Unidades

### U:ce348cdaad0663cc:001 — Prepare a lista de palavras-chave antes da campanha
```yaml
tipo: regra
plataforma: [google-search]
tema: palavras-chave
tarefas: [montar-lista-de-palavras-chave]
fonte: fala+pdf:cst_m04_a02_criando_campanhas_na_rede_de_pesquisa_na_pratica.pdf
faixa: 00:00:00–00:02:27
perecivel: false
confianca: alta
versao: 1
```
Antes de iniciar a criação, monte uma planilha com as palavras-chave que serão usadas na campanha.

### U:ce348cdaad0663cc:002 — Use ampla, frase e exata conforme o controle desejado
```yaml
tipo: decisao
plataforma: [google-search]
tema: palavras-chave
tarefas: [montar-lista-de-palavras-chave]
fonte: fala+pdf:cst_m04_a02_criando_campanhas_na_rede_de_pesquisa_na_pratica.pdf
faixa: 00:00:00–00:02:27
perecivel: false
confianca: alta
versao: 1
```
Se quiser aparecer para buscas relacionadas dentro do nicho, use palavras mais amplas; aspas servem para segmentação de frase.
Quando quiser limitar a palavra-chave ou focar uma pesquisa, use colchetes.

### U:ce348cdaad0663cc:003 — Acentos não alteram a palavra-chave
```yaml
tipo: regra
plataforma: [google-search]
tema: palavras-chave
tarefas: [montar-lista-de-palavras-chave]
fonte: fala
faixa: 00:00:34–00:01:13
perecivel: false
confianca: alta
versao: 1
```
Não se preocupe com o acento ao preparar as palavras-chave.

### U:ce348cdaad0663cc:004 — Escolha vendas ou leads como meta de Pesquisa
```yaml
tipo: decisao
plataforma: [google-search]
tema: objetivos
tarefas: [escolher-objetivo-de-campanha]
fonte: fala+pdf:cst_m04_a02_criando_campanhas_na_rede_de_pesquisa_na_pratica.pdf
faixa: 00:02:27–00:03:40
perecivel: true
confianca: alta
versao: 1
```
Se a campanha busca vendas, escolha a meta de vendas; quando busca cadastros no site, escolha leads.

### U:ce348cdaad0663cc:005 — Comece por visitas ao site
```yaml
tipo: regra
plataforma: [google-search]
tema: objetivos
tarefas: [escolher-objetivo-de-campanha]
fonte: fala+pdf:cst_m04_a02_criando_campanhas_na_rede_de_pesquisa_na_pratica.pdf
faixa: 00:03:05–00:04:17
perecivel: true
confianca: alta
versao: 1
```
Ao começar, selecione “visitas ao site” como forma de alcançar a meta; formulário de lead tem detalhes que a aula não aprofunda.

### U:ce348cdaad0663cc:006 — Leia cada etapa da configuração
```yaml
tipo: regra
plataforma: [google-search]
tema: conta-e-configuracao
tarefas: [criar-campanha]
fonte: fala+pdf:cst_m04_a02_criando_campanhas_na_rede_de_pesquisa_na_pratica.pdf
faixa: 00:04:17–00:05:01
perecivel: true
confianca: alta
versao: 1
```
Leia o conteúdo de cada página antes de preencher para entender o que está sendo configurado.

### U:ce348cdaad0663cc:007 — Nomeie a campanha com rede e tags identificadoras
```yaml
tipo: procedimento
plataforma: [google-search]
tema: nomenclatura
tarefas: [nomear-campanhas]
fonte: fala+pdf:cst_m04_a02_criando_campanhas_na_rede_de_pesquisa_na_pratica.pdf
faixa: 00:04:17–00:05:38
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: estar na etapa de configurações da campanha.
1. Comece o nome pela rede anunciada, como Search, Pesquisa ou Rede de Pesquisa.
2. Acrescente tags que identifiquem a campanha, o público e o tipo da campanha.
3. Deixe espaço entre os colchetes para facilitar a leitura diária.

### U:ce348cdaad0663cc:008 — Exiba a campanha somente na Rede de Pesquisa
```yaml
tipo: decisao
plataforma: [google-search]
tema: posicionamentos-e-formatos
tarefas: [escolher-canais-e-posicionamentos]
fonte: fala+pdf:cst_m04_a02_criando_campanhas_na_rede_de_pesquisa_na_pratica.pdf
faixa: 00:05:38–00:06:10
perecivel: true
confianca: alta
versao: 1
```
Quando criar uma campanha de Pesquisa, selecione a Rede de Pesquisa e não o Display.

### U:ce348cdaad0663cc:009 — Evite data de término em campanhas de Pesquisa
```yaml
tipo: regra
plataforma: [google-search]
tema: estrutura-de-campanha
tarefas: [criar-campanha]
fonte: fala+pdf:cst_m04_a02_criando_campanhas_na_rede_de_pesquisa_na_pratica.pdf
faixa: 00:05:38–00:06:10
perecivel: true
confianca: alta
versao: 1
```
Evite definir data de término: para o professor, quanto mais tempo a campanha de Pesquisa permanece ligada, melhor.

### U:ce348cdaad0663cc:010 — Separe cada dia na programação de anúncios
```yaml
tipo: procedimento
plataforma: [google-search]
tema: estrutura-de-campanha
tarefas: [criar-campanha]
fonte: fala+pdf:cst_m04_a02_criando_campanhas_na_rede_de_pesquisa_na_pratica.pdf
faixa: 00:06:11–00:07:22
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: querer anunciar todos os dias.
1. Adicione a programação de anúncios 7 vezes.
2. Troque “todos os dias” por cada dia da semana, de domingo a sábado.
3. Defina os horários de exibição.
Isso permite observar depois o resultado dos anúncios por dia.

### U:ce348cdaad0663cc:011 — Use cinco dígitos para inserir CEP
```yaml
tipo: regua
plataforma: [google-search]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala+pdf:cst_m04_a02_criando_campanhas_na_rede_de_pesquisa_na_pratica.pdf
faixa: 00:07:24–00:08:04
perecivel: true
confianca: alta
versao: 1
```
Para inserir uma localização por CEP, informe apenas os 5 primeiros números e selecione a opção correspondente.

### U:ce348cdaad0663cc:012 — Use português, inglês e espanhol como idiomas padrão
```yaml
tipo: decisao
plataforma: [google-search]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala+pdf:cst_m04_a02_criando_campanhas_na_rede_de_pesquisa_na_pratica.pdf
faixa: 00:07:24–00:08:39
perecivel: true
confianca: alta
versao: 1
```
Quando o produto não exigir idioma específico, anuncie para português, inglês e espanhol; inclua outro idioma se o produto ou público for específico.

### U:ce348cdaad0663cc:013 — Deixe segmentos de público para a aula específica
```yaml
tipo: limite
plataforma: [google-search]
tema: publicos
tarefas: []
fonte: fala
faixa: 00:08:05–00:08:39
perecivel: true
confianca: alta
versao: 1
```
A aula não configura segmentos de público-alvo; esse assunto será tratado em aula específica.

### U:ce348cdaad0663cc:014 — Defina orçamento que possa ser investido diariamente
```yaml
tipo: decisao
plataforma: [google-search]
tema: orcamento
tarefas: [definir-orcamento]
fonte: fala
faixa: 00:08:39–00:09:21
perecivel: true
confianca: alta
versao: 1
```
Quando definir o orçamento diário, use o valor que consegue investir todos os dias sem prejudicar a empresa.

### U:ce348cdaad0663cc:015 — Comece o lance focando em cliques
```yaml
tipo: decisao
plataforma: [google-search]
tema: leilao-e-lances
tarefas: [escolher-estrategia-de-lance]
fonte: fala+pdf:cst_m04_a02_criando_campanhas_na_rede_de_pesquisa_na_pratica.pdf
faixa: 00:09:22–00:10:38
perecivel: true
confianca: alta
versao: 1
```
Se esta for a primeira campanha, comece com foco em cliques e mude para conversão depois de a campanha acumular dados.
Quando a conta já tiver muitas conversões, histórico e campanhas rodando, você pode iniciar direto com conversão.

### U:ce348cdaad0663cc:016 — Contextualize o valor máximo por clique
```yaml
tipo: decisao
plataforma: [google-search]
tema: leilao-e-lances
tarefas: [escolher-estrategia-de-lance]
fonte: fala+pdf:cst_m04_a02_criando_campanhas_na_rede_de_pesquisa_na_pratica.pdf
faixa: 00:10:38–00:12:09
perecivel: true
confianca: alta
versao: 1
```
Quando definir o limite máximo de custo por clique, considere o produto e a concorrência do nicho.
R$ 10 por clique pode fazer sentido para um produto de R$ 10 mil, mas não para um produto de R$ 5,99.

### U:ce348cdaad0663cc:017 — Comece com lance entre R$ 0,30 e R$ 1
```yaml
tipo: regua
plataforma: [google-search]
tema: leilao-e-lances
tarefas: [escolher-estrategia-de-lance]
fonte: fala
faixa: 00:11:49–00:12:09
perecivel: true
confianca: alta
versao: 1
```
Para iniciar, varie o custo por clique entre R$ 0,30 e R$ 1; o professor prefere começar com R$ 1,00 para a maioria dos anunciantes.

### U:ce348cdaad0663cc:018 — Use grupo de anúncios padrão nesta primeira campanha
```yaml
tipo: decisao
plataforma: [google-search]
tema: estrutura-de-campanha
tarefas: [definir-estrutura-de-campanha]
fonte: fala
faixa: 00:12:50–00:14:02
perecivel: true
confianca: alta
versao: 1
```
Quando criar o primeiro grupo de anúncios, escolha o tipo padrão; grupos dinâmicos serão abordados depois.

### U:ce348cdaad0663cc:019 — Trate o grupo de anúncios como grupo de palavras-chave
```yaml
tipo: conceito
plataforma: [google-search]
tema: estrutura-de-campanha
tarefas: []
fonte: fala
faixa: 00:13:25–00:14:40
perecivel: true
confianca: alta
versao: 1
```
O grupo de anúncios é o grupo de palavras-chave; use um nome ligado à terminologia pesquisada e cole nele a lista preparada.

### U:ce348cdaad0663cc:020 — Crie um grupo antes de replicar outros
```yaml
tipo: regra
plataforma: [google-search]
tema: estrutura-de-campanha
tarefas: [definir-estrutura-de-campanha]
fonte: fala
faixa: 00:14:40–00:15:14
perecivel: true
confianca: alta
versao: 1
```
Crie primeiro um grupo de anúncios e depois replique-o para outros, em vez de criar vários grupos nesta etapa.

### U:ce348cdaad0663cc:021 — Configure URL final e títulos relacionados à busca
```yaml
tipo: procedimento
plataforma: [google-search]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala+pdf:cst_m04_a02_criando_campanhas_na_rede_de_pesquisa_na_pratica.pdf
faixa: 00:15:14–00:19:58
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: estar na etapa de criação do anúncio.
1. Informe na URL final a página para a qual as pessoas serão enviadas.
2. Crie vários títulos relacionados às palavras-chave e ao que é oferecido.
3. Respeite o limite mostrado de 30 caracteres por título.
4. Abra “visualizar ideias” e use as sugestões do Google como inspiração.

### U:ce348cdaad0663cc:022 — Faça anúncio correspondente às palavras-chave
```yaml
tipo: regra
plataforma: [google-search]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala+pdf:cst_m04_a02_criando_campanhas_na_rede_de_pesquisa_na_pratica.pdf
faixa: 00:19:14–00:20:29
perecivel: false
confianca: alta
versao: 1
```
Faça o anúncio corresponder às palavras-chave, produza muitas variações de títulos e inclua call to action.

### U:ce348cdaad0663cc:023 — Pesquise referências no Google e no YouTube
```yaml
tipo: procedimento
plataforma: [google-search, youtube]
tema: criativo
tarefas: [coletar-referencias-de-anuncio]
fonte: fala+pdf:cst_m04_a02_criando_campanhas_na_rede_de_pesquisa_na_pratica.pdf
faixa: 00:19:58–00:22:02
perecivel: false
confianca: alta
versao: 1
nota: "A fala afirma que Google e YouTube são as duas maiores redes de pesquisa."
```
Pré-condição: ter definido o termo principal da campanha.
1. Pesquise o termo no Google e observe anúncios e resultados orgânicos da concorrência.
2. Pesquise o termo no YouTube e observe os títulos dos vídeos.
3. Use os achados como ideias para fazer um anúncio melhor que o da concorrência.

### U:ce348cdaad0663cc:024 — Use quatro descrições e repita palavras-chave
```yaml
tipo: regua
plataforma: [google-search]
tema: copy-e-roteiro
tarefas: [escrever-copy-e-roteiro]
fonte: fala+pdf:cst_m04_a02_criando_campanhas_na_rede_de_pesquisa_na_pratica.pdf
faixa: 00:22:02–00:24:07
perecivel: true
confianca: alta
versao: 1
```
Use as 4 descrições, repita nelas as palavras-chave e use “visualizar ideias” para receber sugestões baseadas na URL.

### U:ce348cdaad0663cc:025 — Otimize o primeiro anúncio depois
```yaml
tipo: regra
plataforma: [google-search]
tema: otimizacao
tarefas: [otimizar-anuncios]
fonte: fala
faixa: 00:23:28–00:24:07
perecivel: false
confianca: alta
versao: 1
```
Não espere que o primeiro anúncio seja o melhor; aprenda com o tempo, otimize-o depois e crie outros anúncios.

### U:ce348cdaad0663cc:026 — Revise e publique a campanha
```yaml
tipo: procedimento
plataforma: [google-search]
tema: estrutura-de-campanha
tarefas: [criar-campanha]
fonte: fala+pdf:cst_m04_a02_criando_campanhas_na_rede_de_pesquisa_na_pratica.pdf
faixa: 00:24:07–00:25:05
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: campanha, grupo de anúncios e primeiro anúncio configurados.
1. Clique em “concluído” e depois em “salvar e continuar”.
2. Revise o que foi configurado.
3. Clique em “publicar”.
As extensões podem ser configuradas após a publicação.

### U:ce348cdaad0663cc:027 — Use a aba selecionada e o topo para se localizar
```yaml
tipo: alerta-ui
plataforma: [google]
tema: conta-e-configuracao
tarefas: [criar-campanha]
fonte: fala+pdf:cst_m04_a02_criando_campanhas_na_rede_de_pesquisa_na_pratica.pdf
faixa: 00:25:05–00:26:53
perecivel: true
confianca: alta
versao: 1
```
No menu lateral, a aba aberta fica selecionada. No topo, o caminho mostra a conta de campanhas, a campanha e, quando aplicável, o grupo de anúncios em que você está.

### U:ce348cdaad0663cc:028 — Acesse extensões a partir do grupo de anúncios
```yaml
tipo: procedimento
plataforma: [google-search]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala+pdf:cst_m04_a02_criando_campanhas_na_rede_de_pesquisa_na_pratica.pdf
faixa: 00:26:18–00:27:43
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: estar dentro do grupo de anúncios da campanha.
1. Clique em “anúncios e extensões”.
2. Abra “extensões”.
3. Clique no botão “+” para adicionar uma extensão.

### U:ce348cdaad0663cc:029 — Comece pelas extensões de sitelink
```yaml
tipo: procedimento
plataforma: [google-search]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala+pdf:cst_m04_a02_criando_campanhas_na_rede_de_pesquisa_na_pratica.pdf
faixa: 00:27:43–00:29:58
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: estar no menu de criação de extensões.
1. Selecione “extensão de sitelink”.
2. Escolha aplicá-la à conta, campanha ou grupo de anúncios.
3. Escreva texto e descrição; o texto tem limite de 25 caracteres.
4. Crie de 2 a 4 sitelinks e clique em “salvar”.

### U:ce348cdaad0663cc:030 — Aplique frases de destaque na campanha inteira
```yaml
tipo: regra
plataforma: [google-search]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala+pdf:cst_m04_a02_criando_campanhas_na_rede_de_pesquisa_na_pratica.pdf
faixa: 00:29:58–00:32:00
perecivel: true
confianca: alta
versao: 1
```
Use frases pequenas ligadas à marca ou negócio como extensões de frase de destaque; o professor prefere adicioná-las à campanha inteira, pois normalmente são as mesmas para todos os grupos.

### U:ce348cdaad0663cc:031 — Use snippet estruturado para tipos do que é vendido
```yaml
tipo: decisao
plataforma: [google-search]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala+pdf:cst_m04_a02_criando_campanhas_na_rede_de_pesquisa_na_pratica.pdf
faixa: 00:31:20–00:32:38
perecivel: true
confianca: alta
versao: 1
```
Quando fizer sentido para o negócio, use snippet estruturado para apresentar modelo, tipo, programa, marca, serviço ou outra categoria disponível do que é vendido.

### U:ce348cdaad0663cc:032 — Use extensão de chamada para receber contatos por telefone
```yaml
tipo: decisao
plataforma: [google-search]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala+pdf:cst_m04_a02_criando_campanhas_na_rede_de_pesquisa_na_pratica.pdf
faixa: 00:32:39–00:33:17
perecivel: true
confianca: alta
versao: 1
```
Se quiser que pessoas entrem em contato por telefone, configure a extensão de chamada com o número da empresa.

### U:ce348cdaad0663cc:033 — Formulário de lead pode reduzir custo, mas tem desvantagem
```yaml
tipo: decisao
plataforma: [google-search]
tema: destino-e-landing-page
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:32:39–00:33:55
perecivel: true
confianca: alta
versao: 1
```
Quando testar extensão de formulário de lead, considere que ela pode deixar o custo por conversão mais barato, mas o contato não recebe a mensagem automática logo após o cadastro como receberia em um site conectado à ferramenta de e-mail.
Não é recomendada pelo professor para quem está começando.

### U:ce348cdaad0663cc:034 — Extensão de local exige Google Meu Negócio configurado
```yaml
tipo: decisao
plataforma: [google-search]
tema: conta-e-configuracao
tarefas: [configurar-anuncio]
fonte: fala+pdf:cst_m04_a02_criando_campanhas_na_rede_de_pesquisa_na_pratica.pdf
faixa: 00:33:55–00:34:33
perecivel: true
confianca: alta
versao: 1
```
Se usar extensão de local, tenha o Google Meu Negócio configurado corretamente.

### U:ce348cdaad0663cc:035 — Teste extensão de preço em e-commerce
```yaml
tipo: decisao
plataforma: [google-search]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:34:33–00:35:07
perecivel: true
confianca: alta
versao: 1
```
Se tiver um e-commerce, vale a pena testar extensão de preço para mostrar itens ou marcas com preço especial.

### U:ce348cdaad0663cc:036 — Configure o maior número possível de extensões
```yaml
tipo: regra
plataforma: [google-search]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala+pdf:cst_m04_a02_criando_campanhas_na_rede_de_pesquisa_na_pratica.pdf
faixa: 00:26:53–00:35:07
perecivel: false
confianca: alta
versao: 1
```
A orientação geral para extensões é: quanto mais extensões, melhor; configure cada uma que fizer sentido para o tráfego.

### U:ce348cdaad0663cc:037 — Crie variações do anúncio na próxima aula
```yaml
tipo: limite
plataforma: [google-search]
tema: testes-e-experimentos
tarefas: []
fonte: fala
faixa: 00:35:07–00:35:55
perecivel: true
confianca: alta
versao: 1
```
A aula não mostra como copiar o anúncio para gerar 3 variações; essa etapa fica para a próxima aula.