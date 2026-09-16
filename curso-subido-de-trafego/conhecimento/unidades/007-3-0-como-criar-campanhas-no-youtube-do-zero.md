---
type: unidades-aula
status: validado
title: "3.0 - Como criar campanhas no YouTube do zero"
modulo: "007"
ordem: 115
aula_id: 126ac7a4360a6a85
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - cst_m07_a03_como_criar_campanhas_no_youtube_do_zero.pdf
  - transcricao.md
extraido_em: 2026-09-16
gerado_por: gpt-5.6-terra
retiradas: []
divisoes: []
fusoes: []
---

# 3.0 - Como criar campanhas no YouTube do zero

## Contexto da aula

A aula demonstra a criação de uma campanha de YouTube no Google Ads Editor.
Ela pressupõe que o aluno já viu as aulas de Google Ads e as anteriores do módulo de Ads Editor.
O exemplo é uma campanha TrueView for Action voltada à captação para aulas.
A demonstração cobre campanha, grupos de anúncios, audiências, exclusões, anúncios e replicação.
O professor recomenda praticar a criação do zero, mas publicar a campanha pausada por haver chance de erro.
A próxima aula criará uma campanha de Display do zero.

## Unidades

### U:126ac7a4360a6a85:001 — Criar e isolar a nova campanha no Editor
```yaml
tipo: procedimento
plataforma: [youtube, ads-editor]
tema: estrutura-de-campanha
tarefas: [criar-campanha]
fonte: fala
faixa: "00:00:35–00:01:12"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: estar no Google Ads Editor e ter acesso à ramificação de campanhas.
1. Selecione Campanhas no menu de ramificações e clique em adicionar campanha.
2. Na aba de seleção, clique na nova campanha para visualizar e configurar somente ela.

### U:126ac7a4360a6a85:002 — Nomear a campanha e definir orçamento inicial
```yaml
tipo: procedimento
plataforma: [youtube, ads-editor]
tema: orcamento
tarefas: [criar-campanha, nomear-campanhas, definir-orcamento]
fonte: fala
faixa: "00:00:35–00:02:25"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: a nova campanha estar selecionada no Editor.
1. Dê à campanha um nome que identifique a campanha de YouTube TrueView for Action.
2. Defina o orçamento de R$ 50 por dia.

### U:126ac7a4360a6a85:003 — Target CPA exige lance diferente de zero
```yaml
tipo: regua
plataforma: [youtube, ads-editor]
tema: leilao-e-lances
tarefas: [escolher-estrategia-de-lance]
fonte: fala
faixa: "00:01:49–00:02:25"
condicoes: "ao usar a estratégia Target CPA"
perecivel: true
confianca: alta
versao: 1
```
A estratégia Target CPA precisa de um bid diferente de zero; no exemplo, edite o lance e informe R$ 5.

### U:126ac7a4360a6a85:004 — Selecionar Vídeo — Drive Conversions para TrueView for Action
```yaml
tipo: decisao
plataforma: [youtube, ads-editor]
tema: objetivos
tarefas: [escolher-objetivo-de-campanha, criar-campanha]
fonte: fala
faixa: "00:02:26–00:03:16"
perecivel: true
confianca: alta
versao: 1
```
Se a campanha for TrueView for Action, selecione o tipo Vídeo — Drive Conversions.
Se não souber o tipo, procure uma campanha anterior com o mesmo objetivo e confira sua configuração.

### U:126ac7a4360a6a85:005 — Desabilitar redes de pesquisa e Display no exemplo
```yaml
tipo: procedimento
plataforma: [youtube, ads-editor]
tema: posicionamentos-e-formatos
tarefas: [criar-campanha, escolher-canais-e-posicionamentos]
fonte: fala
faixa: "00:03:18–00:04:37"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: uma campanha Vídeo — Drive Conversions estar em configuração.
1. Deixe desabilitadas a rede de pesquisa, os parceiros da pesquisa e a rede de Display.
2. Defina data de início e data de término da campanha.

### U:126ac7a4360a6a85:006 — Erro de campanha de vídeo pede uma rede selecionada
```yaml
tipo: alerta-ui
plataforma: [youtube, ads-editor]
tema: posicionamentos-e-formatos
tarefas: [criar-campanha]
fonte: fala
faixa: "00:03:53–00:04:37"
perecivel: true
confianca: alta
versao: 1
```
O Editor mostra erro enquanto uma campanha de vídeo não tiver pelo menos uma rede de vídeos selecionada; essa escolha é feita nas configurações de vídeo.

### U:126ac7a4360a6a85:007 — Manter preferência por melhores anúncios e configurar idioma e país
```yaml
tipo: procedimento
plataforma: [youtube, ads-editor]
tema: estrutura-de-campanha
tarefas: [criar-campanha, definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: "00:03:53–00:04:37"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: estar nas configurações da campanha.
1. Mantenha a otimização com preferência pelos anúncios que performam melhor e não deixe a frequência em No Cap.
2. Adicione Inglês e Português como idiomas e selecione Brasil para localização.

### U:126ac7a4360a6a85:008 — TrueView for Action aparece antes dos vídeos
```yaml
tipo: conceito
plataforma: [youtube]
tema: posicionamentos-e-formatos
tarefas: []
fonte: fala
faixa: "00:04:37–00:05:17"
perecivel: false
confianca: alta
versao: 1
```
Campanhas TrueView for Action aparecem antes dos vídeos; mesmo selecionando YouTube Search, esse formato não aparece nos resultados de pesquisa do YouTube.

### U:126ac7a4360a6a85:009 — Escolher rede de vídeos e parceiros conforme escala e custo
```yaml
tipo: decisao
plataforma: [youtube, ads-editor]
tema: posicionamentos-e-formatos
tarefas: [escolher-canais-e-posicionamentos]
fonte: fala
faixa: "00:04:37–00:05:58"
perecivel: true
confianca: alta
versao: 1
```
Se a campanha for TrueView for Action, selecione YouTube Vídeos para veicular antes dos vídeos.
Quando incluir parceiros de vídeo, espere mais escala e custo mais caro; sem parceiros, espere menos escala e custo mais barato.

### U:126ac7a4360a6a85:010 — Usar Targeting para anunciar às audiências
```yaml
tipo: decisao
plataforma: [youtube, ads-editor]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: "00:05:18–00:06:37"
perecivel: true
confianca: alta
versao: 1
```
Quando quiser veicular para as audiências incluídas, escolha Targeting no Flexible Reach.
Observation serve apenas para o Google fornecer dados sobre essas audiências.

### U:126ac7a4360a6a85:011 — Criar o primeiro grupo para visitantes da página de captura
```yaml
tipo: procedimento
plataforma: [youtube, ads-editor]
tema: estrutura-de-campanha
tarefas: [definir-estrutura-de-campanha]
fonte: fala
faixa: "00:06:38–00:07:22"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: a campanha estar selecionada no Editor.
1. Abra a ramificação de grupos de anúncios e adicione o primeiro grupo.
2. Para a campanha de lead do exemplo, nomeie-o como o grupo 00 de quem caiu na página de captura.
3. Mantenha o tipo In-Stream, que aparece antes dos vídeos, e o status Enabled.

### U:126ac7a4360a6a85:012 — Grupo de anúncios precisa de pelo menos um lance
```yaml
tipo: regua
plataforma: [youtube, ads-editor]
tema: leilao-e-lances
tarefas: [escolher-estrategia-de-lance]
fonte: fala
faixa: "00:07:23–00:08:08"
perecivel: true
confianca: alta
versao: 1
```
Para o grupo de anúncios ficar apto a rodar, defina pelo menos um lance; no exemplo TrueView for Action, use CPA de R$ 5.
Deixe Targeting Expansion desabilitado.

### U:126ac7a4360a6a85:013 — Configurar Flexible Reach do grupo como Targeting
```yaml
tipo: decisao
plataforma: [youtube, ads-editor]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: "00:08:03–00:08:43"
perecivel: true
confianca: alta
versao: 1
```
Quando incluir local, tópico, audiência, gênero, idade, status parental ou renda para receber anúncios, configure cada segmentação como Targeting.
Observation é a opção para apenas colher dados.

### U:126ac7a4360a6a85:014 — Incluir audiência de remarketing no nível do grupo
```yaml
tipo: procedimento
plataforma: [youtube, ads-editor]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: "00:08:44–00:09:17"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: o grupo de anúncios que receberá a audiência estar selecionado.
1. Abra Audiences e adicione uma audiência no nível do grupo de anúncios.
2. Abra a lista de remarketing, pesquise o público desejado e selecione-o.
3. Confirme a inclusão.

### U:126ac7a4360a6a85:015 — Excluir convertidos da audiência de captação
```yaml
tipo: procedimento
plataforma: [youtube, ads-editor]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos]
fonte: fala
faixa: "00:09:19–00:09:52"
condicoes: "em uma campanha de conversão para captação"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: o grupo incluir a audiência de pessoas que caíram na página de captura.
1. Abra Audiences, Negative e escolha exclusão no nível do grupo de anúncios.
2. Localize e inclua como negativa a audiência de quem já se cadastrou para a aula ao vivo.
3. Mantenha a audiência da página de captura como positiva.

### U:126ac7a4360a6a85:016 — Negativar faixas etárias demonstradas
```yaml
tipo: procedimento
plataforma: [youtube, ads-editor]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: "00:09:53–00:10:34"
perecivel: true
confianca: media
versao: 1
nota: "A fala diz inicialmente 'mais de 45 anos', mas demonstra excluir 55–64, 65+ e desconhecido; o PDF descreve mais de 55 anos."
```
Pré-condição: o grupo de anúncios correto estar selecionado.
1. Abra Ages, Negative e adicione exclusão de idade no nível do grupo.
2. Selecione 55–64, adicione 65 anos ou mais e inclua também idade desconhecida.
3. Não adicione essas idades positivas no exemplo.

### U:126ac7a4360a6a85:017 — Criar anúncio TrueView In-Stream com vídeo e URLs
```yaml
tipo: procedimento
plataforma: [youtube, ads-editor]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: "00:10:35–00:12:40"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: o grupo de anúncios da campanha de conversão estar selecionado.
1. Abra TrueView In-Stream Ads, adicione um anúncio e cole o ID que aparece no fim da URL do vídeo no YouTube.
2. Defina nome, chamada para ação, headline, Display URL, Final URL e um banner quadrado.
3. Não escreva a chamada para ação inteiramente em maiúsculas, pois o Google não permite.

### U:126ac7a4360a6a85:018 — Replicar anúncio e trocar apenas o ID de vídeo
```yaml
tipo: procedimento
plataforma: [youtube, ads-editor]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: "00:12:03–00:12:59"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: existir um anúncio TrueView In-Stream já configurado.
1. Copie e cole o anúncio tantas vezes quanto precisar.
2. Troque o Video ID em cada cópia.
3. Renomeie as cópias para identificá-las como AD2, AD3 ou AD4.

### U:126ac7a4360a6a85:019 — Não adicionar gênero positivo em campanhas novas
```yaml
tipo: alerta-ui
plataforma: [youtube, ads-editor]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: "00:14:03–00:15:26"
perecivel: true
confianca: alta
versao: 1
```
Em campanhas novas no Google Ads Editor, adicionar gênero gera erro.
Para anunciar apenas para homens, negativar Unknown e Females na ramificação de gênero negativo.

### U:126ac7a4360a6a85:020 — Replicar grupos e selecionar só o grupo a editar
```yaml
tipo: procedimento
plataforma: [youtube, ads-editor]
tema: estrutura-de-campanha
tarefas: [replicar-campanhas-e-grupos]
fonte: fala
faixa: "00:16:05–00:17:08"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: o primeiro grupo de anúncios estar configurado.
1. Copie e cole o grupo para criar o próximo e altere seu nome conforme a hierarquia, como Inscritos 60 dias.
2. Antes de editar audiências, selecione somente esse novo grupo no menu de seleção.
3. Não edite audiências com a campanha inteira selecionada, pois a alteração alcança os grupos selecionados.

### U:126ac7a4360a6a85:021 — Trocar inclusão e exclusão ao replicar grupo de remarketing
```yaml
tipo: procedimento
plataforma: [youtube, ads-editor]
tema: publicos
tarefas: [montar-publicos-personalizados, organizar-hierarquia-e-exclusao-de-publicos]
fonte: fala
faixa: "00:16:57–00:18:55"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: apenas o grupo replicado estar selecionado.
1. Remova a audiência positiva herdada e inclua a audiência correspondente ao novo grupo, como inscritos em 60 dias ou quem viu vídeo em 540 dias.
2. Nas audiências negativas, exclua o público do grupo anterior.
3. Confirme que a alteração é feita no nível do grupo de anúncios.

### U:126ac7a4360a6a85:022 — Montar grupo frio com palavras-chave da campanha de Pesquisa
```yaml
tipo: procedimento
plataforma: [youtube, ads-editor]
tema: palavras-chave
tarefas: [montar-lista-de-palavras-chave, replicar-campanhas-e-grupos]
fonte: fala
faixa: "00:18:59–00:20:37"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: o grupo de palavras-chave estar selecionado sozinho.
1. Remova a audiência herdada e abra Keywords.
2. Adicione palavras uma a uma ou selecione todas as palavras-chave de uma campanha de Pesquisa, copie e cole no grupo.
3. Apague as palavras duplicadas que o Editor marcar como erro.

### U:126ac7a4360a6a85:023 — Excluir a audiência anterior no grupo de palavras-chave
```yaml
tipo: procedimento
plataforma: [youtube, ads-editor]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos]
fonte: fala
faixa: "00:20:46–00:21:08"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: as palavras-chave já terem sido adicionadas ao grupo frio.
1. Abra a exclusão de audiências do grupo de palavras-chave.
2. Exclua a audiência do grupo anterior, no exemplo a de quem viu vídeo em 540 dias.

### U:126ac7a4360a6a85:024 — Praticar do zero e subir a campanha pausada
```yaml
tipo: regra
plataforma: [youtube, ads-editor]
tema: fundamentos-e-carreira
tarefas: [criar-campanha, formar-se-como-gestor]
fonte: fala
faixa: "00:21:08–00:22:24"
perecivel: false
confianca: alta
versao: 1
```
Normalmente replique uma campanha pronta, mas faça o processo do zero para ganhar experiência no Editor.
Suba a campanha pausada, porque o professor afirma que erros são esperados mesmo após ele já ter feito isso 500 vezes.
Depois de assistir, tente criar sem rever a aula; volte a ela apenas se travar completamente.