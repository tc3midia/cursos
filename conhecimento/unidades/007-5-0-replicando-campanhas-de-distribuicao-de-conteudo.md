---
type: unidades-aula
status: validado
title: "5.0 - Replicando campanhas de distribuição de conteúdo"
modulo: "007"
ordem: 117
aula_id: 0473805f43ec7b28
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - cst_m07_a05_replicando_campanhas_de_distribuicao_de_conteudo.pdf
  - transcricao.md
extraido_em: 2026-09-16
gerado_por: gpt-5.6-terra
retiradas: []
divisoes: []
fusoes: []
---

# 5.0 - Replicando campanhas de distribuição de conteúdo

## Contexto da aula

A aula demonstra, no Google Ads Editor, como reaproveitar a estrutura de campanhas de distribuição de conteúdo.
O professor trabalha com campanhas de vídeo e anúncios TrueView, usando cópia e edição de campanhas ou anúncios.
A decisão entre distribuir um vídeo por campanha ou vários na mesma campanha é tratada nas aulas do módulo de YouTube.
A demonstração cobre a alteração de vídeo, nome, textos e publicação das mudanças na conta.

## Unidades

### U:0473805f43ec7b28:001 — Estrutura de distribuição pode ser reutilizada em nova campanha
```yaml
tipo: conceito
plataforma: [youtube, ads-editor]
tema: estrutura-de-campanha
tarefas: [definir-estrutura-de-campanha, replicar-campanhas-e-grupos]
fonte: fala
faixa: 00:00:00–00:01:54
perecivel: false
confianca: alta
versao: 1
```
Uma campanha de distribuição pode reunir vários vídeos ou ser criada para um único vídeo; a escolha é explicada no módulo de YouTube.
O professor usa estruturas com públicos de cadastrados, espectadores de vídeos, palavras-chave, custom intent e canais para montar novas campanhas.

### U:0473805f43ec7b28:002 — Campanha individual força gasto em um conteúdo
```yaml
tipo: decisao
plataforma: [youtube, ads-editor]
tema: orcamento
tarefas: [definir-estrutura-de-campanha, replicar-campanhas-e-grupos]
fonte: fala
faixa: 00:00:38–00:01:54
perecivel: false
confianca: alta
versao: 1
```
Se quiser forçar o YouTube a gastar dinheiro em uma live ou conteúdo específico, distribua-o em uma campanha própria.

### U:0473805f43ec7b28:003 — Duplicar e ajustar a campanha para um novo conteúdo
```yaml
tipo: procedimento
plataforma: [youtube, ads-editor]
tema: estrutura-de-campanha
tarefas: [replicar-campanhas-e-grupos]
fonte: fala
faixa: 00:01:54–00:03:38
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: uma campanha existente com a estrutura de públicos que será reutilizada.
1. Duplique a campanha com Ctrl+C e Ctrl+V e altere o nome para o novo conteúdo.
2. Defina as datas de início e término da nova campanha.
3. Confira a quantidade de campanhas selecionadas e selecione apenas a cópia antes de editá-la.
4. Nos anúncios TrueView Video Discovery, selecione todos e substitua o código do vídeo pelo trecho da URL após `v=`, sem incluir o parâmetro de tempo.

### U:0473805f43ec7b28:004 — Alterar título, descrição e destino do anúncio replicado
```yaml
tipo: procedimento
plataforma: [youtube, ads-editor]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:03:40–00:04:33
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: anúncios da campanha duplicada selecionados no Google Ads Editor.
1. Informe o título do anúncio correspondente ao novo conteúdo.
2. Atualize a descrição do anúncio.
3. Defina como destino o vídeo no YouTube.

### U:0473805f43ec7b28:005 — Criar segunda variação em todos os conjuntos
```yaml
tipo: procedimento
plataforma: [youtube, ads-editor]
tema: criativo
tarefas: [replicar-campanhas-e-grupos, configurar-anuncio]
fonte: fala
faixa: 00:03:51–00:05:10
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: um anúncio da nova campanha pronto para servir de base.
1. Copie um anúncio e cole a cópia em todos os conjuntos de anúncios da campanha.
2. Renomeie a cópia como uma segunda variação, como AD2.
3. Altere o texto da variação, como trocar “Facebook” por “Instagram”.
4. Selecione a campanha e use Publicar para enviar as alterações.

### U:0473805f43ec7b28:006 — Uso de Facebook ou Instagram pode gerar erro
```yaml
tipo: alerta-ui
plataforma: [youtube, ads-editor]
tema: copy-e-roteiro
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:04:33–00:05:54
perecivel: true
confianca: media
versao: 1
nota: "O professor relata que o erro pode aparecer, mas não ocorreu na demonstração."
```
Ao publicar texto que contém o nome Facebook ou Instagram, o Editor pode exibir um erro e o anúncio pode ser rejeitado.
No exemplo, o professor confirma conformidade por se tratar de live informativa, sem venda associada ao nome da plataforma.

### U:0473805f43ec7b28:007 — Substituir anúncios que apontam para conteúdo desatualizado
```yaml
tipo: procedimento
plataforma: [youtube, ads-editor]
tema: criativo
tarefas: [replicar-campanhas-e-grupos, configurar-anuncio]
fonte: fala
faixa: 00:05:54–00:07:16
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: uma live nova substitui ou atualiza uma live presente em campanhas existentes.
1. Entre em cada campanha e localize os conjuntos cujos anúncios apontam para a live anterior.
2. Troque o Video ID pelo ID do vídeo novo.
3. Renomeie os anúncios para refletir o conteúdo atualizado.
4. Se necessário, filtre os anúncios pelo número ou nome do conteúdo antigo para localizá-los.

### U:0473805f43ec7b28:008 — Acrescentar nova variação após atualizar anúncios antigos
```yaml
tipo: procedimento
plataforma: [youtube, ads-editor]
tema: criativo
tarefas: [replicar-campanhas-e-grupos, configurar-anuncio]
fonte: fala
faixa: 00:07:18–00:08:11
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: anúncios antigos já foram atualizados para apontar ao vídeo novo.
1. Identifique o último número de anúncio existente, como AD9.
2. Cole uma cópia do anúncio em todos os conjuntos da campanha.
3. Crie o próximo anúncio, como AD10, com o novo conteúdo e uma variação de texto.
4. Clique na conta e publique para enviar todas as alterações pendentes dela.

### U:0473805f43ec7b28:009 — Baixar campanhas antes de editá-las no Editor
```yaml
tipo: procedimento
plataforma: [ads-editor]
tema: conta-e-configuracao
tarefas: [operar-ads-editor]
fonte: fala
faixa: 00:08:16–00:11:57
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: a campanha foi ativada ou alterada no Google Ads e precisa aparecer no Google Ads Editor.
1. No Google Ads Editor, abra Basic e faça o download das campanhas.
2. Localize a campanha baixada.
3. Selecione somente essa campanha e confira a indicação de uma campanha selecionada.
4. Abra os anúncios TrueView InStream Ads da campanha.

### U:0473805f43ec7b28:010 — Replicar anúncio de vídeo para todos os conjuntos
```yaml
tipo: procedimento
plataforma: [youtube, ads-editor]
tema: criativo
tarefas: [replicar-campanhas-e-grupos, configurar-anuncio]
fonte: fala
faixa: 00:11:57–00:13:02
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: um anúncio existente serve de estrutura para uma nova peça de vídeo.
1. Copie o anúncio com Ctrl+C.
2. Cole com Ctrl+V e escolha todos os conjuntos de anúncios como destino da cópia.
3. Dê o próximo nome de anúncio, como AD10, e informe o ID do vídeo.
4. Ative o novo anúncio.
5. Se a cópia foi criada por engano, selecione as cópias e use Delete.

### U:0473805f43ec7b28:011 — Replicação de anúncio de vídeo exige poucas alterações
```yaml
tipo: regra
plataforma: [youtube, ads-editor]
tema: criativo
tarefas: [replicar-campanhas-e-grupos, configurar-anuncio]
fonte: fala
faixa: 00:13:02–00:13:39
perecivel: false
confianca: alta
versao: 1
```
Para replicar um anúncio de vídeo, copie e cole, altere o Video ID e altere o nome do anúncio.

### U:0473805f43ec7b28:012 — Aprender o Editor requer prática na própria conta
```yaml
tipo: regra
plataforma: [ads-editor]
tema: fundamentos-e-carreira
tarefas: [operar-ads-editor, formar-se-como-gestor]
fonte: fala
faixa: 00:13:02–00:13:47
perecivel: false
confianca: alta
versao: 1
```
Use a aula para entender possibilidades, mas pratique o Google Ads Editor na própria conta para aprender a operar a ferramenta.
O professor afirma que dominar o Editor torna o gestor, no mínimo, 10 vezes mais rápido no Google.

### U:0473805f43ec7b28:013 — Replicar anúncios responsivos de pesquisa
```yaml
tipo: procedimento
plataforma: [ads-editor]
tema: criativo
tarefas: [configurar-anuncio, operar-ads-editor]
fonte: "pdf:cst_m07_a05_replicando_campanhas_de_distribuicao_de_conteudo.pdf"
perecivel: true
confianca: alta
versao: 2
nota: "Unidade acrescentada para cobrir o procedimento do PDF, pp. 1–3 e 7; os números de headline pertencem à demonstração. Ajuste mecânico da coordenação: removida faixa:null proibida em fonte exclusivamente PDF. Corpo preservado."
```
Pré-condição: há um anúncio-base na campanha e no grupo desejados.
1. Selecione a campanha, o grupo e o tipo Responsive search ads; duplique o anúncio-base.
2. Edite headlines e descrições da cópia. Na demonstração, Headline1 e Headline4 são fixadas alternadamente na posição 1, Headline2 é alterada e Headline6 é testada.
3. Selecione a conta, escolha Post e confirme Post para publicar.

### U:0473805f43ec7b28:014 — Replicar anúncios de texto expandido
```yaml
tipo: procedimento
plataforma: [ads-editor]
tema: criativo
tarefas: [configurar-anuncio, operar-ads-editor]
fonte: "pdf:cst_m07_a05_replicando_campanhas_de_distribuicao_de_conteudo.pdf"
perecivel: true
confianca: alta
versao: 2
nota: "Unidade acrescentada para cobrir o procedimento do PDF, pp. 3 e 6–7. Ajuste mecânico da coordenação: removida faixa:null proibida em fonte exclusivamente PDF. Corpo preservado."
```
Pré-condição: há um anúncio existente no grupo desejado.
1. Selecione o grupo e o tipo Expanded Text Ads; duplique o anúncio existente.
2. Varie headlines e descrições na cópia.
3. Selecione a conta, escolha Post e confirme Post para publicar.

### U:0473805f43ec7b28:015 — Manter ao menos três criativos de texto expandido
```yaml
tipo: regua
plataforma: [ads-editor]
tema: criativo
tarefas: [operar-ads-editor]
fonte: "pdf:cst_m07_a05_replicando_campanhas_de_distribuicao_de_conteudo.pdf"
condicoes: No contexto dos anúncios de texto expandido apresentados no PDF.
perecivel: false
confianca: alta
versao: 2
nota: "Unidade acrescentada para preservar a recomendação histórica do professor no PDF, p. 3. Ajuste mecânico da coordenação: removida faixa:null proibida em fonte exclusivamente PDF; tag inexistente substituída por tarefa existente de operação no Editor. Corpo preservado."
```
Trabalhe com no mínimo 3 criativos de texto expandido, conforme a recomendação apresentada pelo professor.

### U:0473805f43ec7b28:016 — Pausar anúncio de Search com desempenho ruim
```yaml
tipo: decisao
plataforma: [google, ads-editor]
tema: otimizacao
tarefas: [operar-ads-editor]
fonte: "pdf:cst_m07_a05_replicando_campanhas_de_distribuicao_de_conteudo.pdf"
perecivel: true
confianca: alta
versao: 2
nota: "Unidade acrescentada para cobrir a decisão do PDF, pp. 4–8; valores ilustrativos de conversões e custo não são critérios gerais. Ajuste mecânico da coordenação: removida faixa:null proibida em fonte exclusivamente PDF; tag inexistente substituída por tarefa existente de operação no Editor. Corpo preservado."
```
Se a análise no Google Ads indicar desempenho considerado ruim para um anúncio de Search, localize no Editor o grupo, o tipo e o anúncio correspondente e pause-o pelo botão direito. Crie uma variação de um anúncio que funciona ou teste uma ideia nova.

### U:0473805f43ec7b28:017 — Pausar vídeo de conversão com desempenho ruim
```yaml
tipo: decisao
plataforma: [google, ads-editor]
tema: otimizacao
tarefas: [operar-ads-editor]
fonte: "pdf:cst_m07_a05_replicando_campanhas_de_distribuicao_de_conteudo.pdf"
perecivel: true
confianca: alta
versao: 2
nota: "Unidade acrescentada para cobrir a pausa no vídeo de conversão do PDF, pp. 9–10; AD5 é apenas o exemplo mostrado. Ajuste mecânico da coordenação: removida faixa:null proibida em fonte exclusivamente PDF. Corpo preservado."
```
Se a análise no Google Ads apontar desempenho ruim de um anúncio de vídeo de conversão, selecione no Editor as ocorrências desse anúncio e use o botão direito para escolher Pause. O anúncio chamado AD5 no PDF é um exemplo, não um critério para escolher qual peça pausar.

### U:0473805f43ec7b28:018 — Distribuir cópia de anúncio responsivo de Display
```yaml
tipo: procedimento
plataforma: [ads-editor]
tema: criativo
tarefas: [configurar-anuncio, operar-ads-editor]
fonte: "pdf:cst_m07_a05_replicando_campanhas_de_distribuicao_de_conteudo.pdf"
perecivel: true
confianca: alta
versao: 2
nota: "Unidade acrescentada para cobrir a replicação de Responsive Display Ads do PDF, pp. 11–13. Ajuste mecânico da coordenação: removida faixa:null proibida em fonte exclusivamente PDF. Corpo preservado."
```
Pré-condição: há um anúncio-base na campanha de Display desejada.
1. Selecione a campanha e o tipo Responsive display Ads; copie e cole o anúncio-base.
2. Marque a campanha para distribuir a cópia em todos os grupos e confirme em OK.
3. Edite as headlines, descrições, logos e imagens necessários nas cópias.

### U:0473805f43ec7b28:019 — Enviar e replicar anúncios de imagem de Display
```yaml
tipo: procedimento
plataforma: [google, ads-editor]
tema: posicionamentos-e-formatos
tarefas: [configurar-anuncio, operar-ads-editor]
fonte: "pdf:cst_m07_a05_replicando_campanhas_de_distribuicao_de_conteudo.pdf"
perecivel: true
confianca: alta
versao: 2
nota: "Unidade acrescentada para cobrir o fluxo do PDF, pp. 13–19. A preferência pelo upload no Google Ads reflete a limitação do Editor usado pelo professor na demonstração. Ajuste mecânico da coordenação: removida faixa:null proibida em fonte exclusivamente PDF. Corpo preservado."
```
Pré-condição: os arquivos de imagem estão prontos e há grupos de origem e destino definidos na campanha de Display.
1. No Google Ads, abra a campanha de Display e o grupo desejado; escolha criar anúncio e Fazer upload de anúncios de display.
2. Informe a URL, escolha os arquivos e selecione as imagens em conjunto; aguarde o upload e salve.
3. No Editor, baixe as alterações por Get recent changes, More Data, All Campaigns e OK.
4. Após o download, selecione o grupo de origem e Image Ads; selecione e copie os anúncios.
5. Selecione outro grupo e cole os anúncios.

### U:0473805f43ec7b28:020 — Escolher a ferramenta conforme a atividade
```yaml
tipo: regra
plataforma: [google, ads-editor]
tema: conta-e-configuracao
tarefas: [operar-ads-editor]
fonte: "pdf:cst_m07_a05_replicando_campanhas_de_distribuicao_de_conteudo.pdf"
perecivel: false
confianca: alta
versao: 2
nota: "Unidade acrescentada para preservar a divisão de trabalho proposta no PDF, p. 19, sem tratá-la como exclusividade. Ajuste mecânico da coordenação: removida faixa:null proibida em fonte exclusivamente PDF. Corpo preservado."
```
Na divisão de trabalho proposta, use o Google Ads para otimização, análise de dados e upload de imagens de Display; use o Editor para criar e replicar anúncios.

