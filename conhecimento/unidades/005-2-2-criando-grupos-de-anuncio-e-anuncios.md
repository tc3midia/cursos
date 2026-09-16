---
type: unidades-aula
status: validado
title: "2.2 - Criando grupos de anúncio e anúncios"
modulo: "005"
ordem: 80
aula_id: 769b58cb532b0f84
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - cst_m05_a22_criando_grupos_de_anuncio_e_anuncios.pdf
  - transcricao.md
extraido_em: 2026-09-16
gerado_por: gpt-5.6-terra
retiradas: []
divisoes: []
fusoes: []
---

# 2.2 - Criando grupos de anúncio e anúncios

## Contexto da aula

A aula continua a criação de uma campanha de distribuição de conteúdo no YouTube.
Ela configura o primeiro grupo de anúncios após campanha, orçamento, redes e demais escolhas anteriores.
O exemplo usa uma live longa em formato vídeo In-Feed e segmentação exclusivamente por canais.
Também mostra alternativas de segmentação, lance, formatos de anúncio e campos de criação.
A replicação de anúncios fica anunciada para a próxima aula.

## Unidades

### U:769b58cb532b0f84:001 — Escolher vídeo In-Feed para alcance qualificado
```yaml
tipo: decisao
plataforma: [youtube]
tema: posicionamentos-e-formatos
tarefas: [escolher-canais-e-posicionamentos]
fonte: "fala+pdf:cst_m05_a22_criando_grupos_de_anuncio_e_anuncios.pdf"
faixa: "00:00:00–00:01:05"
condicoes: "campanha de distribuição de conteúdo"
perecivel: false
confianca: alta
versao: 1
nota: "PDF p. 2 também lista visualizações qualificadas, vídeos maiores e engajamento com vídeo/canal."
```
Quando quiser visualizações mais qualificadas, divulgar vídeos maiores ou buscar engajamento, inscritos, curtidas e compartilhamentos, use vídeo In-Feed.
Esse formato aparece nos vídeos relacionados e na pesquisa do YouTube.

### U:769b58cb532b0f84:002 — Escolher In-Stream para volume de visualizações
```yaml
tipo: decisao
plataforma: [youtube]
tema: posicionamentos-e-formatos
tarefas: [escolher-canais-e-posicionamentos]
fonte: "fala+pdf:cst_m05_a22_criando_grupos_de_anuncio_e_anuncios.pdf"
faixa: "00:01:05–00:01:39"
condicoes: "objetivo de distribuição de conteúdo com vídeos entre 1 e 10 minutos no máximo"
perecivel: false
confianca: alta
versao: 1
nota: "PDF p. 2 cita volume de visualizações, visualizações mais baratas e público maior; a fala acrescenta não priorizar inscritos."
```
Quando buscar volume de visualizações, visualizações mais baratas e um público maior, use In-Stream.
A fala associa esse uso a vídeos menores e a casos em que o número de inscritos gerados não importa.

### U:769b58cb532b0f84:003 — Definir CPV máximo e excluir parceiros de vídeo
```yaml
tipo: procedimento
plataforma: [youtube]
tema: leilao-e-lances
tarefas: [criar-campanha, escolher-estrategia-de-lance]
fonte: "fala+pdf:cst_m05_a22_criando_grupos_de_anuncio_e_anuncios.pdf"
faixa: "00:01:39–00:01:53"
perecivel: true
confianca: alta
versao: 1
nota: "PDF p. 3 orienta acessar Campanhas no menu lateral, selecionar CPV máximo em Estratégia de lances e não marcar parceiros de vídeo na Rede de Display."
```
Pré-condição: campanha de vídeo criada no Google Ads e objetivo de obter visualizações.
1. Em estratégia de lance, selecione CPV máximo, porque o objetivo é visualização, não impressão.
2. Em redes, não selecione parceiros de vídeo na rede de display.
3. Mantenha a veiculação pretendida na pesquisa e nos vídeos do YouTube.

### U:769b58cb532b0f84:004 — Criar primeiro o grupo segmentado por canais
```yaml
tipo: regra
plataforma: [youtube]
tema: estrutura-de-campanha
tarefas: [definir-estrutura-de-campanha]
fonte: "fala+pdf:cst_m05_a22_criando_grupos_de_anuncio_e_anuncios.pdf"
faixa: "00:01:55–00:03:05"
perecivel: false
confianca: alta
versao: 1
nota: "PDF p. 4 recomenda começar por público de canais, inclusive em campanhas de conversão ou de visualização."
```
Comece as campanhas de YouTube pelo público de canais e coloque esse grupo como prioridade na hierarquia, usando a ordem do nome como fator de exclusão.
A segmentação por canais é mais restrita; no exemplo, a lista tem 85 canais e muitas exclusões podem impedir a entrega.

### U:769b58cb532b0f84:005 — Ajustar demografia conforme escala e objetivo
```yaml
tipo: decisao
plataforma: [youtube]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: "fala+pdf:cst_m05_a22_criando_grupos_de_anuncio_e_anuncios.pdf"
faixa: "00:03:05–00:03:41"
perecivel: true
confianca: alta
versao: 1
nota: "PDF p. 4 orienta abrir Informações demográficas; para muita escala, deixar todas as opções selecionadas."
```
Se precisar de muita escala e quiser gastar muito dinheiro, deixe as opções demográficas selecionadas.
Caso contrário, escolha sexo, idade e demais critérios conforme o objetivo; no exemplo, o professor remove desconhecidos por alcançar muitas pessoas menores de 18 anos.

### U:769b58cb532b0f84:006 — Não tratar renda como garantia de valor percebido
```yaml
tipo: regra
plataforma: [youtube]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: "fala+pdf:cst_m05_a22_criando_grupos_de_anuncio_e_anuncios.pdf"
faixa: "00:03:41–00:05:23"
perecivel: false
confianca: alta
versao: 1
nota: "PDF p. 4 faz a mesma ressalva. A fala relata testes no Brasil com os 10% de maior renda, sem apresentá-los como regra geral."
```
Não espere que segmentar pessoas com dinheiro faça com que elas vejam valor no produto.
A segmentação por renda pode fazer sentido conforme nicho e produto, mas renda disponível não determina a compra.

### U:769b58cb532b0f84:007 — Distinguir público-alvo de segmentação de conteúdo
```yaml
tipo: conceito
plataforma: [youtube]
tema: publicos
tarefas: []
fonte: fala
faixa: "00:05:23–00:06:04"
perecivel: false
confianca: alta
versao: 1
```
Segmentos de público-alvo incluem públicos de YouTube, site, lista, aplicativo, personalizados, combinados, de mercado, eventos importantes, afinidade, demográficos e semelhantes.
Canais, palavras-chave e tópicos segmentam o conteúdo e definem onde o anúncio pode aparecer, não o público-alvo.

### U:769b58cb532b0f84:008 — Cautela ao combinar público e canais
```yaml
tipo: decisao
plataforma: [youtube]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses, escolher-canais-e-posicionamentos]
fonte: "fala+pdf:cst_m05_a22_criando_grupos_de_anuncio_e_anuncios.pdf"
faixa: "00:06:05–00:09:21"
condicoes: "combinação de segmento de público-alvo com canais"
perecivel: true
confianca: alta
versao: 1
nota: "PDF p. 6 alerta que público mais canais pode tornar a segmentação muito restrita."
```
Se combinar um segmento de público-alvo com canais, o anúncio aparecerá apenas para aquele público nos canais escolhidos.
Considere que essa combinação pode restringir demais a segmentação.

### U:769b58cb532b0f84:009 — Testar palavras-chave com canais
```yaml
tipo: decisao
plataforma: [youtube]
tema: palavras-chave
tarefas: [montar-lista-de-palavras-chave, escolher-canais-e-posicionamentos]
fonte: "fala+pdf:cst_m05_a22_criando_grupos_de_anuncio_e_anuncios.pdf"
faixa: "00:09:21–00:09:59"
condicoes: "lista de palavras-chave com quantidade suficiente"
perecivel: false
confianca: alta
versao: 1
nota: "PDF p. 6 também recomenda testar palavras-chave com canais. A preferência é relato do professor, não regra universal."
```
Quando testar combinações de segmentação, misture palavras-chave e canais.
O professor diz que, entre as combinações que experimentou, essa foi a que mais viu funcionar, sem afirmar que exista regra geral.

### U:769b58cb532b0f84:010 — Inserir URLs de canais em linhas separadas
```yaml
tipo: procedimento
plataforma: [youtube]
tema: publicos
tarefas: [escolher-canais-e-posicionamentos]
fonte: "fala+pdf:cst_m05_a22_criando_grupos_de_anuncio_e_anuncios.pdf"
faixa: "00:09:59–00:10:37"
perecivel: true
confianca: alta
versao: 1
nota: "PDF p. 6 orienta clicar em Inserir, colar URLs e então clicar em Adicionar."
```
Pré-condição: lista pesquisada de URLs dos canais em que o anúncio deve aparecer.
1. Na segmentação de conteúdo, abra Canais e escolha Inserir.
2. Cole uma URL de canal por linha.
3. Clique em Adicionar para aplicar os canais ao grupo.

### U:769b58cb532b0f84:011 — Começar o lance com trinta centavos
```yaml
tipo: regua
plataforma: [youtube]
tema: leilao-e-lances
tarefas: [escolher-estrategia-de-lance]
fonte: "fala+pdf:cst_m05_a22_criando_grupos_de_anuncio_e_anuncios.pdf"
faixa: "00:10:37–00:11:20"
perecivel: true
confianca: alta
versao: 1
nota: "PDF p. 7 recomenda começar com trinta centavos, reconhece que é um lance alto e orienta otimizar após alguns dias."
```
Comece com lance de 30 centavos por visualização, especialmente em contas que você ainda não conhece.
É um lance alto, mas o professor diz que ajuda a campanha a começar a gastar; depois, otimize para reduzir ou explorar o valor.

### U:769b58cb532b0f84:012 — Manter um único formato na campanha
```yaml
tipo: regra
plataforma: [youtube]
tema: estrutura-de-campanha
tarefas: [definir-estrutura-de-campanha, configurar-anuncio]
fonte: "fala+pdf:cst_m05_a22_criando_grupos_de_anuncio_e_anuncios.pdf"
faixa: "00:11:20–00:12:03"
perecivel: false
confianca: alta
versao: 1
nota: "PDF p. 8 declara que todo o grupo será do mesmo tipo após a definição."
```
A definição entre In-Feed e In-Stream define o tipo da campanha a partir do primeiro grupo de anúncios.
Não é possível ter um grupo In-Feed e outro In-Stream na mesma campanha.

### U:769b58cb532b0f84:013 — Usar o próprio vídeo como destino do In-Stream
```yaml
tipo: decisao
plataforma: [youtube]
tema: destino-e-landing-page
tarefas: [configurar-anuncio]
fonte: "fala+pdf:cst_m05_a22_criando_grupos_de_anuncio_e_anuncios.pdf"
faixa: "00:12:03–00:12:39"
condicoes: "anúncio In-Stream pulável usado para distribuir conteúdo"
perecivel: true
confianca: alta
versao: 1
nota: "PDF p. 8 instrui preencher URL final para o destino; p. 9 registra a preferência do professor por não usar call to action nesse caso."
```
Se usar In-Stream pulável para distribuir conteúdo, coloque na URL final o próprio vídeo do anúncio.
O professor prefere não inserir call to action quando quer que a pessoa assista ao vídeo completo.

### U:769b58cb532b0f84:014 — Preencher campos e nomear o anúncio In-Feed
```yaml
tipo: procedimento
plataforma: [youtube]
tema: criativo
tarefas: [configurar-anuncio, nomear-campanhas]
fonte: "fala+pdf:cst_m05_a22_criando_grupos_de_anuncio_e_anuncios.pdf"
faixa: "00:12:39–00:14:20"
perecivel: true
confianca: alta
versao: 1
nota: "PDF p. 10 manda preencher título, descrição 1, descrição 2 e nome do anúncio. Na fala, o professor mostra título, uma descrição e nome; a divergência é preservada."
```
Pré-condição: vídeo selecionado e formato In-Feed definido.
1. Preencha o título e a descrição; no exemplo, o professor repete no título o tema do vídeo.
2. Dê um nome identificável ao anúncio, como AD1, anúncio 1 e a referência do vídeo.
3. Clique em Criar campanha quando os campos estiverem preenchidos.

### U:769b58cb532b0f84:015 — Bumper exige CPM máximo
```yaml
tipo: decisao
plataforma: [youtube]
tema: leilao-e-lances
tarefas: [escolher-estrategia-de-lance, configurar-anuncio]
fonte: fala
faixa: "00:14:56–00:16:06"
perecivel: true
confianca: alta
versao: 1
```
Se quiser selecionar o formato bumper, escolha CPM máximo como estratégia de lance.
Com CPV, o formato bumper não fica disponível; no exemplo, o professor mantém CPV porque busca visualizações.

### U:769b58cb532b0f84:016 — Replicação de anúncios fica para a próxima aula
```yaml
tipo: limite
plataforma: [youtube]
tema: estrutura-de-campanha
tarefas: []
fonte: fala
faixa: "00:16:06–00:16:36"
perecivel: false
confianca: alta
versao: 1
```
A aula mostra a criação do primeiro grupo e de um anúncio.
A replicação para incluir cinco, dez ou outros anúncios no grupo será ensinada na aula seguinte.