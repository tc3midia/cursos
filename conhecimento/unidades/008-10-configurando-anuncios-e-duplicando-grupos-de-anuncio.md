---
type: unidades-aula
status: validado
title: "10.Configurando anúncios e duplicando grupos de anúncio"
modulo: "008"
ordem: 129
aula_id: 699c37b5bbda68c6
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

# 10.Configurando anúncios e duplicando grupos de anúncio

## Contexto da aula

A aula demonstra a montagem de anúncios no TikTok Ads após a configuração dos níveis anteriores da campanha.
Explica as opções de identidade, a seleção de vídeos e os campos finais do anúncio.
Também mostra como duplicar anúncios e grupos de anúncio para formar uma hierarquia de públicos.
Catálogo e Instant Pages são citados, mas ficam para aulas posteriores.
A aula encerra a parte de criação de campanhas e anuncia que as próximas aulas abordarão otimização.

## Unidades

### U:699c37b5bbda68c6:001 — Nomear anúncios com o padrão AD
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: nomenclatura
tarefas: [nomear-campanhas]
fonte: fala
faixa: "00:00:00–00:00:40"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: estar na configuração de um anúncio no TikTok Ads.
1. Dê um nome ao anúncio antes de configurá-lo.
2. Use o padrão AD01 e acrescente uma descrição, como “Convite Aulas”.

### U:699c37b5bbda68c6:002 — TikTok oferece identidade customizada e Spark Ads
```yaml
tipo: conceito
plataforma: [tiktok]
tema: criativo
tarefas: []
fonte: fala
faixa: "00:00:00–00:01:30"
perecivel: true
confianca: media
versao: 1
nota: "O professor hesita ao pronunciar o nome em inglês e o apresenta como “identidade customizada” ou “custom identity”."
```
No TikTok, o anúncio pode usar identidade customizada ou Spark Ads.
Spark Ads anuncia por meio de um perfil Business do TikTok; a identidade customizada veicula sem perfil vinculado.

### U:699c37b5bbda68c6:003 — Vincular conta do TikTok ao Ads Manager
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala
faixa: "00:00:41–00:01:30"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: usar Spark Ads e ter uma conta Business do TikTok.
1. Clique no ícone de User no topo.
2. Abra User Settings.
3. Use o botão para associar a conta do TikTok ao Ads Manager e à business account.

### U:699c37b5bbda68c6:004 — Criar identidade customizada sem perfil clicável
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: "00:01:30–00:02:04"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: escolher anunciar sem usar um perfil do TikTok.
1. Clique no botão azul para criar uma nova identidade customizada.
2. Defina um arroba não clicável e escolha a foto de perfil.
3. Configure a foto, pois o professor destaca que ela é importante.

### U:699c37b5bbda68c6:005 — Usar Spark Ads com conta própria ou post autorizado
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: "00:02:04–00:03:52"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: Spark Ads selecionado e acesso ao perfil ou ao post que será anunciado.
1. Escolha uma conta própria ou uma conta/post autorizado.
2. No perfil, abra os três traços, entre em Creator Tools e ative Add Settings.
3. Abra o post, use os três pontos, localize Add Settings e Add Authorization.
4. Gere o código, use Manage e Copy Code.
5. Cole o código no campo solicitado pelo Ads Manager.

### U:699c37b5bbda68c6:006 — Escolher formato conforme catálogo e e-commerce
```yaml
tipo: decisao
plataforma: [tiktok]
tema: posicionamentos-e-formatos
tarefas: [configurar-anuncio]
fonte: fala
faixa: "00:03:52–00:04:30"
condicoes: "Collection Ads exige e-commerce e catálogo configurado nos ativos."
perecivel: true
confianca: alta
versao: 1
```
Quando o negócio for e-commerce com catálogo configurado, use Collection Ads.
Quando não for o caso, selecione TikTok post ou single vídeo.

### U:699c37b5bbda68c6:007 — Selecionar vídeo publicado, enviar arquivo ou usar biblioteca
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: "00:04:30–00:05:14"
condicoes: "O vídeo precisa ter entre 5 e 60 segundos."
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: TikTok post ou single vídeo selecionado.
1. Escolha um post já publicado no perfil para patrociná-lo, ou envie um vídeo pelo Upload.
2. Como alternativa, use Add from your library para selecionar um vídeo enviado anteriormente.
3. Confirme que o vídeo está entre 5 e 60 segundos.

### U:699c37b5bbda68c6:008 — Enviar criativos em massa para a biblioteca
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: "00:05:14–00:06:28"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: ter os vídeos que serão usados nos anúncios.
1. Em Ativos, abra Creatives e depois Vídeos.
2. Clique em Upload para enviar vários vídeos.
3. No anúncio, abra Vídeo e Adicionar da sua biblioteca.
4. Selecione o criativo e confirme.

### U:699c37b5bbda68c6:009 — Impedir publicação do vídeo no perfil
```yaml
tipo: alerta-ui
plataforma: [tiktok]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: "00:05:49–00:06:28"
perecivel: true
confianca: alta
versao: 2
nota: " Faixa mecânica de duração zero corrigida após confronto com a transcrição: o bloco 00:05:49–00:06:28 contém a seleção Apenas mostrar esse vídeo como um anúncio e a consequência de publicar no perfil. Corpo preservado."
```
Marque “apenas mostrar este vídeo como um anúncio”; sem essa seleção, o TikTok publica o vídeo no perfil.

### U:699c37b5bbda68c6:010 — Instant Pages e catálogo ficam para depois
```yaml
tipo: limite
plataforma: [tiktok]
tema: destino-e-landing-page
tarefas: []
fonte: fala
faixa: "00:06:53–00:07:35"
perecivel: true
confianca: alta
versao: 1
```
A aula não aprofunda Instant Pages nem catálogo; o professor diz que revisará ambos nas aulas finais.
No exemplo, a pessoa será enviada para o site em vez de uma experiência instantânea.

### U:699c37b5bbda68c6:011 — Confirmar direito de uso e controlar exibição no Creative Center
```yaml
tipo: alerta-ui
plataforma: [tiktok]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: "00:06:53–00:08:17"
perecivel: true
confianca: alta
versao: 1
```
O primeiro checkbox confirma que você tem direito de usar o vídeo.
O segundo permite que o anúncio apareça no TikTok Business Creative Center; deixe-o desmarcado se não quiser que outras pessoas o vejam lá.
Segundo o professor, essa escolha não altera o resultado do anúncio.

### U:699c37b5bbda68c6:012 — Criar enquete interativa no anúncio
```yaml
tipo: alerta-ui
plataforma: [tiktok]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: "00:07:35–00:08:18"
perecivel: true
confianca: alta
versao: 1
```
As Interactive Add-ons permitem criar uma enquete interativa no vídeo.
Use o botão de criar nessa área para montar a enquete.

### U:699c37b5bbda68c6:013 — Preferir CTA padrão “saiba mais”
```yaml
tipo: decisao
plataforma: [tiktok]
tema: copy-e-roteiro
tarefas: [configurar-anuncio]
fonte: fala
faixa: "00:08:20–00:09:10"
perecivel: true
confianca: alta
versao: 1
```
Quando definir o Call to Action, o professor prefere o padrão “saiba mais”.
Ele considera que essa opção fica mais bonita e performa melhor.

### U:699c37b5bbda68c6:014 — Duplicar anúncio e trocar apenas o vídeo
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: estrutura-de-campanha
tarefas: [replicar-campanhas-e-grupos]
fonte: fala
faixa: "00:09:10–00:10:24"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: ter um anúncio já configurado e vídeos disponíveis na biblioteca.
1. Duplique o anúncio pelo botão de duplicação.
2. Use Update e escolha outro vídeo na biblioteca, ou envie um novo.
3. Repita para cada variação de vídeo.
4. Renomeie as cópias como AD2, AD3, AD4, AD5 e AD6 para não manter nomes iguais.

### U:699c37b5bbda68c6:015 — Preferir Spark Ads quando houver perfil configurado
```yaml
tipo: decisao
plataforma: [tiktok]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: "00:10:28–00:11:11"
condicoes: "Ter uma conta do TikTok configurada para anunciar."
perecivel: true
confianca: alta
versao: 1
```
Quando houver uma conta do TikTok configurada, o professor recomenda Spark Ads porque relata resultados melhores na maioria das vezes.
Com Spark Ads, a pessoa pode clicar no arroba e abrir o perfil; sem ele, clicar no nome não leva a lugar algum.

### U:699c37b5bbda68c6:016 — Enviar anúncio e aguardar revisão
```yaml
tipo: alerta-ui
plataforma: [tiktok]
tema: estrutura-de-campanha
tarefas: [criar-campanha]
fonte: fala
faixa: "00:11:11–00:11:56"
perecivel: true
confianca: alta
versao: 1
```
Depois de conferir legenda, link e a opção de não publicar no perfil, clique em Submit.
Anúncios podem aparecer como “not delivering” enquanto estão em revisão; o professor diz que isso é normal e que a revisão demora algum tempo.

### U:699c37b5bbda68c6:017 — Duplicar grupo e substituir o público
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: estrutura-de-campanha
tarefas: [replicar-campanhas-e-grupos, definir-estrutura-de-campanha]
fonte: fala
faixa: "00:11:58–00:13:55"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: ter campanha, grupo de anúncio e anúncios configurados.
1. Abra a campanha, entre no grupo de anúncio e crie uma cópia dele.
2. Remova o público incluído antes de excluí-lo.
3. Exclua os públicos anteriores e inclua o novo público pela busca.
4. Avance em Next, confira os anúncios duplicados e envie em Submit.

### U:699c37b5bbda68c6:018 — Corrigir falha de duplicação revisando vídeos
```yaml
tipo: decisao
plataforma: [tiktok]
tema: estrutura-de-campanha
tarefas: [replicar-campanhas-e-grupos]
fonte: fala
faixa: "00:13:55–00:15:12"
perecivel: true
confianca: alta
versao: 1
```
Se a duplicação pedir para selecionar os vídeos novamente, adicione os mesmos vídeos pela biblioteca.
Depois, revise cada anúncio e marque “somente mostrar como anúncio”, pois sem isso os vídeos podem ser publicados no TikTok.
O professor afirma que esse bug ocorre poucas vezes e que, na maioria das duplicações, tudo funciona corretamente.

### U:699c37b5bbda68c6:019 — Repetir duplicações para montar a hierarquia de públicos
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: estrutura-de-campanha
tarefas: [replicar-campanhas-e-grupos, definir-estrutura-de-campanha]
fonte: fala
faixa: "00:15:12–00:16:28"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: ter um novo grupo de anúncio pronto após a duplicação.
1. Copie novamente o grupo de anúncio.
2. Altere o público de cada cópia até montar a hierarquia de públicos.
3. Teste públicos semelhantes e públicos de interesse conforme o objetivo escolhido.

### U:699c37b5bbda68c6:020 — Definir campanhas e públicos conforme o objetivo
```yaml
tipo: decisao
plataforma: [tiktok]
tema: objetivos
tarefas: [escolher-objetivo-de-campanha, definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: "00:15:54–00:16:28"
perecivel: false
confianca: alta
versao: 1
```
Quando decidir qual campanha criar, escolha conforme o objetivo.
Defina também quais públicos testar; o professor caracteriza essa exploração como muito teste em uma ferramenta nova.