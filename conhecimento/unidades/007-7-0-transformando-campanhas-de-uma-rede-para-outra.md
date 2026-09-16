---
type: unidades-aula
status: validado
title: "7.0 - Transformando campanhas de uma rede para outra"
modulo: "007"
ordem: 119
aula_id: fa1b6ce75df3beb4
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - cst_m07_a07_transformando_campanhas_de_uma_rede_para_outra.pdf
  - transcricao.md
extraido_em: 2026-09-16
gerado_por: gpt-5.6-terra
retiradas: []
divisoes: []
fusoes: []
---

# 7.0 - Transformando campanhas de uma rede para outra

## Contexto da aula

A aula demonstra no Google Ads Editor como copiar uma campanha e adaptar sua estrutura para outra rede.
Parte de campanhas de vídeo, display e pesquisa já existentes, com públicos e grupos configurados.
Mostra quais erros surgem após a troca de tipo e como ajustar campanha, grupos, lances e anúncios.
Também apresenta a exceção de transformar Search em vídeo para a pesquisa do YouTube.

## Unidades

### U:fa1b6ce75df3beb4:001 — Replicar preserva a estrutura ao mudar de rede
```yaml
tipo: conceito
plataforma: [ads-editor]
tema: estrutura-de-campanha
tarefas: []
fonte: fala
faixa: 00:00:27–00:00:56
perecivel: false
confianca: alta
versao: 1
```
Replicar uma campanha entre redes é aproveitar uma campanha existente, como uma de vídeo, para criar outra de display com a mesma estrutura.

### U:fa1b6ce75df3beb4:002 — Duplicar e renomear a campanha no Ads Editor
```yaml
tipo: procedimento
plataforma: [ads-editor]
tema: estrutura-de-campanha
tarefas: [converter-campanha-entre-redes, replicar-campanhas-e-grupos]
fonte: fala
faixa: 00:00:56–00:01:29
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: uma campanha existente no Google Ads Editor.
1. Selecione a campanha e use Ctrl C, depois Ctrl V.
2. Se surgir erro por já haver campanha com o mesmo nome, altere o nome da cópia, por exemplo para indicar Display.

### U:fa1b6ce75df3beb4:003 — Trabalhar somente na cópia criada
```yaml
tipo: alerta-ui
plataforma: [ads-editor]
tema: estrutura-de-campanha
tarefas: [converter-campanha-entre-redes]
fonte: fala
faixa: 00:01:29–00:02:04
perecivel: true
confianca: alta
versao: 1
```
Ao haver duas campanhas selecionadas, selecione apenas a cópia que está sendo criada para não editar as duas.

### U:fa1b6ce75df3beb4:004 — Converter vídeo Drive Conversions para Display
```yaml
tipo: procedimento
plataforma: [ads-editor]
tema: estrutura-de-campanha
tarefas: [converter-campanha-entre-redes]
fonte: fala
faixa: 00:01:29–00:02:41
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: a cópia da campanha de vídeo está selecionada.
1. No tipo de campanha, troque Video Drive Conversions por Display; o professor cita Display Smart e Display Gmail como opções que não escolheu no exemplo.
2. Verifique os erros da campanha, dos grupos de anúncio e dos anúncios após a mudança.

### U:fa1b6ce75df3beb4:005 — Remover a rede de vídeo da campanha Display
```yaml
tipo: decisao
plataforma: [ads-editor, google-display]
tema: posicionamentos-e-formatos
tarefas: [converter-campanha-entre-redes]
fonte: fala
faixa: 00:02:05–00:02:41
perecivel: true
confianca: alta
versao: 1
```
Se a campanha foi convertida para Display, desabilite a rede de vídeo: ela é específica de campanhas de vídeo e impede publicar a campanha Display.

### U:fa1b6ce75df3beb4:006 — Ajustar grupo e lance ao converter para Display
```yaml
tipo: procedimento
plataforma: [ads-editor, google-display]
tema: leilao-e-lances
tarefas: [converter-campanha-entre-redes, escolher-estrategia-de-lance]
fonte: fala
faixa: 00:02:42–00:03:59
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: a campanha já está como Display e os grupos de anúncio apresentam erros.
1. Selecione todos os grupos, troque o tipo In-stream por Default e apague o lance de CPV.
2. Na campanha, troque Target CPA por CPC ou CPM; o professor diz que normalmente não usa Target CPA em Display.
3. Nos grupos, informe o CPC de cada um; no exemplo, usa R$ 0,30.

### U:fa1b6ce75df3beb4:007 — Quatro ajustes na mudança de rede
```yaml
tipo: regra
plataforma: [ads-editor]
tema: estrutura-de-campanha
tarefas: [converter-campanha-entre-redes]
fonte: fala
faixa: 00:03:23–00:03:59
perecivel: false
confianca: alta
versao: 1
```
Ao transformar campanhas entre redes, ajuste tipo de campanha, tipo de grupo de anúncio, estratégia de lance e o valor do lance.

### U:fa1b6ce75df3beb4:008 — Substituir anúncios In-stream em campanha Display
```yaml
tipo: procedimento
plataforma: [ads-editor, google-display]
tema: criativo
tarefas: [converter-campanha-entre-redes, configurar-anuncio]
fonte: fala
faixa: 00:03:59–00:05:54
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: a campanha foi convertida para Display.
1. Apague os anúncios TrueView In-stream, pois não podem permanecer numa campanha Display.
2. Adicione anúncios responsivos ou anúncios de imagem.
3. Para reutilizar anúncios responsivos, copie-os de um grupo da campanha antiga e cole-os nos grupos da nova campanha.
4. Para anúncios de imagem, copie-os da seção Image Ads de um grupo e cole-os nos grupos da nova campanha.

### U:fa1b6ce75df3beb4:009 — Escolher o tipo de campanha de vídeo pela finalidade
```yaml
tipo: decisao
plataforma: [ads-editor, youtube]
tema: objetivos
tarefas: [converter-campanha-entre-redes, escolher-objetivo-de-campanha]
fonte: fala
faixa: 00:06:10–00:06:47
perecivel: true
confianca: alta
versao: 1
```
Se a campanha de vídeo for para distribuição de conteúdo, escolha o tipo Vídeo; se for TrueView for Action, escolha Video Drive Conversions.

### U:fa1b6ce75df3beb4:010 — Converter Display em distribuição de conteúdo no YouTube
```yaml
tipo: procedimento
plataforma: [ads-editor, youtube]
tema: leilao-e-lances
tarefas: [converter-campanha-entre-redes, escolher-estrategia-de-lance]
fonte: fala
faixa: 00:05:54–00:07:22
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: uma cópia de campanha Display está selecionada.
1. Renomeie a cópia para YouTube e altere o tipo de campanha para Vídeo.
2. Troque a estratégia de CPC por CPV.
3. Selecione a rede de vídeo e, no exemplo de distribuição de conteúdo, escolha os vídeos do YouTube.
4. Selecione somente a campanha em edição antes de corrigir os grupos.

### U:fa1b6ce75df3beb4:011 — Tipo de grupo depende do tipo de vídeo
```yaml
tipo: decisao
plataforma: [ads-editor, youtube]
tema: estrutura-de-campanha
tarefas: [converter-campanha-entre-redes]
fonte: fala
faixa: 00:07:23–00:08:02
perecivel: true
confianca: alta
versao: 1
```
Se a campanha de vídeo for distribuição de conteúdo, troque os grupos Default por Video Discovery; se for Video Drive Conversions, use In-stream.

### U:fa1b6ce75df3beb4:012 — Corrigir CPV nos grupos de campanhas de vídeo
```yaml
tipo: regra
plataforma: [ads-editor, youtube]
tema: leilao-e-lances
tarefas: [converter-campanha-entre-redes, escolher-estrategia-de-lance]
fonte: fala
faixa: 00:07:23–00:08:02
perecivel: true
confianca: alta
versao: 1
```
Em campanha de vídeo, remova CPC e defina individualmente o lance de CPV em cada grupo de anúncio; corrija os lances sempre que mudar de rede.

### U:fa1b6ce75df3beb4:013 — Usar TrueView Discovery Ads em Video Discovery
```yaml
tipo: decisao
plataforma: [ads-editor, youtube]
tema: criativo
tarefas: [converter-campanha-entre-redes, configurar-anuncio]
fonte: fala
faixa: 00:08:02–00:08:40
perecivel: true
confianca: alta
versao: 1
```
Se a campanha usa Video Discovery, substitua anúncios responsivos por TrueView Discovery Ads.

### U:fa1b6ce75df3beb4:014 — Copiar anúncios preservando a relação com o grupo
```yaml
tipo: regra
plataforma: [ads-editor, youtube]
tema: estrutura-de-campanha
tarefas: [replicar-campanhas-e-grupos, converter-campanha-entre-redes]
fonte: fala
faixa: 00:08:40–00:09:18
perecivel: true
confianca: alta
versao: 1
```
Copie de um grupo de anúncio apenas os anúncios daquele grupo e cole-os no grupo correspondente; copiar todos os anúncios da campanha para cada grupo pode dar errado.

### U:fa1b6ce75df3beb4:015 — Escolher grupos de destino ao colar anúncios
```yaml
tipo: alerta-ui
plataforma: [ads-editor, youtube]
tema: estrutura-de-campanha
tarefas: [replicar-campanhas-e-grupos]
fonte: fala
faixa: 00:09:18–00:10:01
perecivel: true
confianca: alta
versao: 1
```
Ao colar anúncios com a campanha inteira selecionada, o Editor pergunta em quais grupos de anúncio colá-los; o professor seleciona todos no exemplo.

### U:fa1b6ce75df3beb4:016 — Converter distribuição de vídeo em Video Drive Conversions
```yaml
tipo: procedimento
plataforma: [ads-editor, youtube]
tema: leilao-e-lances
tarefas: [converter-campanha-entre-redes, escolher-estrategia-de-lance]
fonte: fala
faixa: 00:10:01–00:10:30
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: uma cópia da campanha de distribuição de vídeo foi criada.
1. Renomeie a cópia para indicar conversão e troque o tipo para Video Drive Conversions.
2. Troque a estratégia de lance para CPA.
3. Informe o CPA; no exemplo, o professor usa 5.

### U:fa1b6ce75df3beb4:017 — Ajustar grupos e anúncios para Drive Conversions
```yaml
tipo: procedimento
plataforma: [ads-editor, youtube]
tema: criativo
tarefas: [converter-campanha-entre-redes, configurar-anuncio]
fonte: fala
faixa: 00:10:30–00:11:09
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: a campanha está como Video Drive Conversions.
1. Selecione apenas a campanha nova e troque os grupos Video Discovery por In-stream.
2. Apague anúncios Video Discovery Ads.
3. Adicione TrueView In-stream Ads para os grupos de anúncio.

### U:fa1b6ce75df3beb4:018 — Campos de um TrueView In-stream criado do zero
```yaml
tipo: alerta-ui
plataforma: [ads-editor, youtube]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:10:30–00:12:05
perecivel: true
confianca: alta
versao: 1
```
Ao criar um TrueView In-stream Ads, o professor preenche ID, nome, call to action, headline, destino, URL final e o ID do vídeo do YouTube.

### U:fa1b6ce75df3beb4:019 — Search só é reaproveitada para vídeo de pesquisa do YouTube
```yaml
tipo: decisao
plataforma: [ads-editor, google-search, youtube]
tema: estrutura-de-campanha
tarefas: [converter-campanha-entre-redes]
fonte: fala
faixa: 00:11:30–00:12:45
perecivel: false
confianca: alta
versao: 1
```
Se for transformar uma campanha de Search, use-a somente para criar uma campanha de vídeo voltada à pesquisa do YouTube e aproveitar grupos organizados por palavras-chave.

### U:fa1b6ce75df3beb4:020 — Converter Search em campanha de pesquisa do YouTube
```yaml
tipo: procedimento
plataforma: [ads-editor, google-search, youtube]
tema: estrutura-de-campanha
tarefas: [converter-campanha-entre-redes]
fonte: fala
faixa: 00:12:45–00:14:00
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: uma cópia de campanha Search foi criada no Ads Editor.
1. Altere o tipo de campanha de Search para Vídeo.
2. Troque Maximizar cliques por CPV.
3. Selecione a rede de vídeo para a campanha aparecer na pesquisa do YouTube, não nos vídeos.
4. Troque o tipo dos grupos Default por Video Discovery.

### U:fa1b6ce75df3beb4:021 — Ajustar targeting e lances na pesquisa do YouTube
```yaml
tipo: procedimento
plataforma: [ads-editor, youtube]
tema: publicos
tarefas: [converter-campanha-entre-redes, definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: 00:14:02–00:15:21
perecivel: true
confianca: media
versao: 1
nota: "A fala alterna entre Flexible Reach e a instrução exibida para usar Targeting em Placements, Topics e Audiences."
```
Pré-condição: os grupos da campanha de pesquisa do YouTube estão selecionados.
1. Defina Targeting para Placements, Topics e Audiences.
2. Corrija o lance da campanha.
3. Selecione todos os grupos antes de aplicar alterações, para não precisar repetir o processo em cada grupo.

### U:fa1b6ce75df3beb4:022 — Remover lances específicos de palavras-chave
```yaml
tipo: decisao
plataforma: [ads-editor, youtube]
tema: leilao-e-lances
tarefas: [converter-campanha-entre-redes, otimizar-palavras-chave]
fonte: fala
faixa: 00:15:28–00:16:10
perecivel: true
confianca: alta
versao: 1
```
Se as palavras-chave da campanha convertida tiverem lances específicos, apague esses lances; o professor diz que não pode mantê-los.

### U:fa1b6ce75df3beb4:023 — Substituir anúncios Search por TrueView Discovery Ads
```yaml
tipo: procedimento
plataforma: [ads-editor, youtube]
tema: criativo
tarefas: [converter-campanha-entre-redes, configurar-anuncio]
fonte: fala
faixa: 00:15:28–00:16:42
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: a campanha Search foi convertida para vídeo.
1. Apague os anúncios de pesquisa.
2. Crie TrueView Discovery Ads.
3. Em cada grupo, use anúncios relacionados às palavras-chave daquele grupo; o exemplo associa anúncios de Facebook Ads ao grupo de Facebook Ads.
4. Os anúncios podem vir de campanha existente ou ser novos.

### U:fa1b6ce75df3beb4:024 — Remover extensões incompatíveis da campanha de vídeo
```yaml
tipo: regra
plataforma: [ads-editor, youtube]
tema: criativo
tarefas: [converter-campanha-entre-redes]
fonte: fala
faixa: 00:16:45–00:17:29
perecivel: true
confianca: alta
versao: 1
```
Na campanha de vídeo derivada de Search, remova extensões de texto, callout e snippet estruturado para eliminar o erro restante.

### U:fa1b6ce75df3beb4:025 — Identificar e apagar campanhas não postadas
```yaml
tipo: procedimento
plataforma: [ads-editor]
tema: estrutura-de-campanha
tarefas: [operar-ads-editor]
fonte: fala
faixa: 00:17:29–00:18:40
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: campanhas de teste foram criadas durante a replicação.
1. Selecione a conta inteira.
2. Identifique em roxo as campanhas não postadas.
3. Apague as campanhas não postadas que foram criadas apenas para o teste, para evitar que rodem por engano.
```