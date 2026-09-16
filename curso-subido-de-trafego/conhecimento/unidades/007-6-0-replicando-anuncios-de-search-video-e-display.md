---
type: unidades-aula
status: validado
title: "6.0 - Replicando anúncios de search, vídeo e display"
modulo: "007"
ordem: 118
aula_id: 41d06b9cb3ee79cd
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - cst_m07_a06_replicando_anuncios_de_search_video_e_display.pdf
  - transcricao.md
extraido_em: 2026-09-16
gerado_por: gpt-5.6-terra
retiradas: []
divisoes: []
fusoes: []
nota: "O PDF demonstra conversão de campanhas entre redes; a transcrição demonstra replicação de anúncios. As unidades preservam os dois recortes."
---

# 6.0 - Replicando anúncios de search, vídeo e display

## Contexto da aula

A aula mostra como replicar anúncios de search, vídeo e display no Google Ads Editor.
O professor usa cópias de anúncios existentes para criar variações, alterar campos e escolher os grupos que receberão a cópia.
Também explica que anúncios de imagem de display precisam ser enviados pelo Google Ads antes de poderem ser replicados no Editor.
O PDF complementar demonstra conversões de estrutura de campanha entre vídeo, display e pesquisa do YouTube.

## Unidades

### U:41d06b9cb3ee79cd:001 — Replicar anúncio responsivo de pesquisa para criar variação
```yaml
tipo: procedimento
plataforma: [google-search, ads-editor]
tema: criativo
tarefas: [configurar-anuncio, otimizar-anuncios]
fonte: fala
faixa: 00:00:58–00:03:41
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: um anúncio responsivo de pesquisa existente no grupo de anúncios.
1. Copie e cole o anúncio para criar uma nova versão.
2. Altere títulos e descrições da cópia, respeitando o espaço disponível nos campos.
3. Mantenha um título na posição 1 quando essa for a intenção do anúncio.
4. Use a nova versão como anúncio adicional no grupo.

### U:41d06b9cb3ee79cd:002 — Manter ao menos três anúncios de texto expandido
```yaml
tipo: regua
plataforma: [google-search]
tema: criativo
tarefas: [configurar-anuncio, otimizar-anuncios]
fonte: fala
faixa: 00:03:41–00:04:29
perecivel: false
confianca: alta
versao: 1
```
Tenha no mínimo três anúncios de texto expandido rodando no grupo de anúncios.
O professor replica um anúncio responsivo e aproveita uma descrição nova para compor outro anúncio de texto expandido.

### U:41d06b9cb3ee79cd:003 — Pausar anúncio que não está bom antes de criar variação
```yaml
tipo: decisao
plataforma: [google-search, ads-editor]
tema: otimizacao
tarefas: [otimizar-anuncios]
fonte: fala
faixa: 00:04:29–00:06:40
perecivel: true
confianca: alta
versao: 1
```
Se um anúncio não está bom, pause-o na própria ferramenta antes de ir ao Google Ads Editor.
Depois use um anúncio que está bom como base para criar uma variação.

### U:41d06b9cb3ee79cd:004 — Alterações aparecem em roxo no Google Ads Editor
```yaml
tipo: alerta-ui
plataforma: [ads-editor]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:06:40–00:07:34
perecivel: true
confianca: alta
versao: 1
```
No Editor, o conteúdo em roxo indica o que está sendo alterado no anúncio.
Use essa marcação para identificar qual versão está em edição.

### U:41d06b9cb3ee79cd:005 — Publicar alterações do Editor na conta
```yaml
tipo: procedimento
plataforma: [ads-editor]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:07:37–00:08:30
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: alterações de anúncio concluídas no Google Ads Editor.
1. Selecione a conta no Editor.
2. Acione a opção de publicar.
3. Aguarde a publicação das alterações na conta.

### U:41d06b9cb3ee79cd:006 — Trocar anúncio fraco por variação de anúncio que funciona
```yaml
tipo: decisao
plataforma: [google-search]
tema: otimizacao
tarefas: [otimizar-anuncios]
fonte: fala
faixa: 00:08:30–00:09:55
condicoes: "ao analisar anúncios de um grupo de anúncios"
perecivel: true
confianca: alta
versao: 1
```
Se um anúncio tem pouca conversão e preço caro, pause-o e crie uma versão dos anúncios que estão funcionando.
O professor exemplifica a leitura de um anúncio com 7 conversões e outro com 5 conversões a R$ 6.

### U:41d06b9cb3ee79cd:007 — Copiar anúncio de vídeo para todos os grupos
```yaml
tipo: procedimento
plataforma: [youtube, ads-editor]
tema: criativo
tarefas: [configurar-anuncio, otimizar-anuncios]
fonte: fala
faixa: 00:09:55–00:10:42
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: um anúncio TrueView in-stream pronto em uma campanha de conversão.
1. Copie o anúncio existente e cole a cópia.
2. Escolha todos os grupos de anúncios que receberão o novo anúncio.
3. Altere o nome, informe o novo Video ID e ative o anúncio.
4. Publique a alteração.

### U:41d06b9cb3ee79cd:008 — Pausar anúncios de vídeo ruins em massa
```yaml
tipo: decisao
plataforma: [youtube, ads-editor]
tema: otimizacao
tarefas: [otimizar-anuncios]
fonte: fala
faixa: 00:09:55–00:10:42
perecivel: true
confianca: alta
versao: 1
```
Se vários anúncios de vídeo estão ruins, selecione todos e pause-os no Editor.
A lógica de replicar e editar anúncios vale para qualquer campanha de vídeo mostrada.

### U:41d06b9cb3ee79cd:009 — Replicar anúncio responsivo de display
```yaml
tipo: procedimento
plataforma: [google-display, ads-editor]
tema: criativo
tarefas: [configurar-anuncio, otimizar-anuncios]
fonte: fala
faixa: 00:10:42–00:12:13
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: anúncio responsivo de display disponível na campanha.
1. Copie e cole o anúncio responsivo.
2. Escolha os grupos de anúncios que receberão a cópia.
3. Altere a imagem, o headline e os demais campos necessários no anúncio novo.

### U:41d06b9cb3ee79cd:010 — Enviar anúncios de imagem pelo Google Ads
```yaml
tipo: procedimento
plataforma: [google-display, google]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:11:28–00:13:10
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: arquivos dos anúncios de imagem e acesso à campanha de display no Google Ads.
1. Abra o grupo de anúncios da campanha.
2. Crie um novo anúncio de display para upload.
3. Informe a URL e escolha os arquivos para envio.
4. Salve os formatos de imagem enviados.

### U:41d06b9cb3ee79cd:011 — Baixar mais dados para trazer anúncios de imagem ao Editor
```yaml
tipo: procedimento
plataforma: [google-display, ads-editor]
tema: criativo
tarefas: [operar-ads-editor]
fonte: fala
faixa: 00:13:10–00:14:32
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: anúncios de imagem enviados pelo Google Ads.
1. Baixe no Editor as informações da campanha onde os anúncios foram enviados.
2. Se o download básico não trouxer os anúncios de imagem, escolha baixar mais dados.
3. Restrinja o download à campanha necessária para deixar a área de trabalho mais limpa.
4. Confirme a quantidade de anúncios após o download.

### U:41d06b9cb3ee79cd:012 — Copiar anúncios de imagem entre grupos de display
```yaml
tipo: procedimento
plataforma: [google-display, ads-editor]
tema: criativo
tarefas: [configurar-anuncio, otimizar-anuncios]
fonte: fala
faixa: 00:14:34–00:16:15
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: anúncios de imagem já baixados no Google Ads Editor.
1. Selecione todos os anúncios de imagem no grupo de origem.
2. Copie os anúncios.
3. Abra o outro grupo de anúncios e cole a seleção.
4. Revise e publique as alterações.

### U:41d06b9cb3ee79cd:013 — Remover anúncios de teste antes de publicar
```yaml
tipo: alerta-ui
plataforma: [ads-editor]
tema: criativo
tarefas: [otimizar-anuncios]
fonte: fala
faixa: 00:14:34–00:16:15
perecivel: true
confianca: alta
versao: 1
```
O professor removeu anúncios usados apenas como exemplo antes de publicar, para evitar que rodassem na conta.
A opção mostrada para a remoção foi “Remove”.

### U:41d06b9cb3ee79cd:014 — Distribuição de ferramentas entre Google Ads e Editor
```yaml
tipo: regra
plataforma: [google, ads-editor]
tema: otimizacao
tarefas: [operar-ads-editor, ler-metricas-e-relatorios, configurar-anuncio]
fonte: fala
faixa: 00:16:15–00:16:33
perecivel: false
confianca: alta
versao: 1
```
Use o Google Ads para analisar dados e enviar anúncios de imagem de display.
Use o Google Ads Editor para criar, replicar e editar anúncios.

### U:41d06b9cb3ee79cd:015 — Trabalhar com Google Ads e Editor em dois monitores
```yaml
tipo: regra
plataforma: [google, ads-editor]
tema: fundamentos-e-carreira
tarefas: [operar-ads-editor]
fonte: fala
faixa: 00:16:15–00:16:33
perecivel: false
confianca: alta
versao: 1
```
O professor recomenda dois monitores: Google Ads em um e Google Ads Editor no outro.
Assim, ele trabalha alternando entre as duas ferramentas.

### U:41d06b9cb3ee79cd:016 — Ajustes ao converter vídeo em display
```yaml
tipo: procedimento
plataforma: [youtube, google-display, ads-editor]
tema: estrutura-de-campanha
tarefas: [converter-campanha-entre-redes]
fonte: pdf:cst_m07_a06_replicando_anuncios_de_search_video_e_display.pdf
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: cópia de uma campanha de vídeo no Google Ads Editor.
1. Altere o tipo da campanha para Display e desmarque YouTube Vídeos em Video Settings.
2. Mude o tipo dos grupos para Default e remova o lance de CPV.
3. Troque a estratégia Target CPA por Manual CPC e defina CPC nos grupos.
4. Apague anúncios TrueView in-stream e inclua anúncios responsivos ou de imagem.

### U:41d06b9cb3ee79cd:017 — Usar CPC de R$ 0,30 na cópia de display demonstrada
```yaml
tipo: regua
plataforma: [google-display, ads-editor]
tema: leilao-e-lances
tarefas: [converter-campanha-entre-redes, escolher-estrategia-de-lance]
fonte: pdf:cst_m07_a06_replicando_anuncios_de_search_video_e_display.pdf
perecivel: true
confianca: alta
versao: 1
```
Na demonstração de conversão de vídeo para display, o professor define CPC de R$ 0,30 para os grupos de anúncios.
A campanha é configurada com a estratégia Manual CPC.

### U:41d06b9cb3ee79cd:018 — Escolher tipo de vídeo conforme o objetivo da cópia
```yaml
tipo: decisao
plataforma: [youtube, ads-editor]
tema: estrutura-de-campanha
tarefas: [converter-campanha-entre-redes]
fonte: pdf:cst_m07_a06_replicando_anuncios_de_search_video_e_display.pdf
perecivel: true
confianca: alta
versao: 1
```
Se a cópia de display virar campanha de distribuição de conteúdo, escolha o tipo Vídeo.
Se for uma campanha TrueView for Action, escolha Vídeo – Drive conversions.

### U:41d06b9cb3ee79cd:019 — Ajustar lances e grupos ao converter display em vídeo
```yaml
tipo: procedimento
plataforma: [google-display, youtube, ads-editor]
tema: estrutura-de-campanha
tarefas: [converter-campanha-entre-redes, escolher-estrategia-de-lance]
fonte: pdf:cst_m07_a06_replicando_anuncios_de_search_video_e_display.pdf
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: cópia de uma campanha de display destinada a vídeo.
1. Troque Manual CPC por Manual CPV e marque YouTube Vídeos em Video Settings.
2. Mude o tipo dos grupos de Default para Vídeo Discovery.
3. Apague o lance de CPC e informe lance de CPV individualmente em cada grupo.
4. Remova anúncios responsivos de display e inclua TrueView Video Discovery Ads.

### U:41d06b9cb3ee79cd:020 — Criar campanha de conversão a partir de vídeo discovery
```yaml
tipo: procedimento
plataforma: [youtube, ads-editor]
tema: estrutura-de-campanha
tarefas: [converter-campanha-entre-redes, configurar-anuncio]
fonte: pdf:cst_m07_a06_replicando_anuncios_de_search_video_e_display.pdf
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: cópia de uma campanha de distribuição de conteúdo em vídeo.
1. Troque o tipo para Vídeo – Drive Conversions e escolha Target CPA.
2. Na demonstração, informe CPA de R$ 5,00.
3. Mude os grupos de Vídeo Discovery para In-Stream e apague anúncios Video Discovery.
4. Adicione TrueView in-stream ads e preencha Video ID, nome, chamada para ação, Display URL e Final URL.

### U:41d06b9cb3ee79cd:021 — Converter search em pesquisa do YouTube somente para reaproveitar estrutura
```yaml
tipo: decisao
plataforma: [google-search, youtube, ads-editor]
tema: estrutura-de-campanha
tarefas: [converter-campanha-entre-redes]
fonte: pdf:cst_m07_a06_replicando_anuncios_de_search_video_e_display.pdf
perecivel: true
confianca: alta
versao: 1
```
Se precisar anunciar apenas na pesquisa do YouTube, copie uma campanha de search para reaproveitar sua estrutura de pesquisa.
Altere o tipo para Vídeo, use Manual CPV, selecione pesquisa do YouTube, mude os grupos para Vídeo Discovery e remova lances CPC das palavras-chave.

### U:41d06b9cb3ee79cd:022 — Remover anúncios e extensões incompatíveis da pesquisa do YouTube
```yaml
tipo: procedimento
plataforma: [google-search, youtube, ads-editor]
tema: criativo
tarefas: [converter-campanha-entre-redes, configurar-anuncio]
fonte: pdf:cst_m07_a06_replicando_anuncios_de_search_video_e_display.pdf
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: campanha de search convertida para pesquisa do YouTube.
1. Apague anúncios responsivos de pesquisa e anúncios de texto estendidos.
2. Adicione ou copie TrueView Discovery Ads para os grupos compatíveis.
3. Remova callout extensions e structured snippet extensions, que geram erro nessa campanha.