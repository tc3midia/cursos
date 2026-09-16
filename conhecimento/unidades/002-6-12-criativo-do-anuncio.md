---
type: unidades-aula
status: validado
title: "6.12 - Criativo do anúncio"
modulo: "002"
ordem: 42
aula_id: 367e808623ec5fe5
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

# 6.12 - Criativo do anúncio

## Contexto da aula

A aula mostra a configuração operacional do criativo de anúncio no Meta Ads.
Parte da escolha e substituição de mídias conforme os principais formatos e posicionamentos.
Também cobre otimizações automáticas, textos, títulos, descrição e chamada para ação.
A parte de copy para criar bons anúncios não é aprofundada nesta aula.
Destino e rastreamento ficam para a próxima aula.

## Unidades

### U:367e808623ec5fe5:001 — Teste todas as possibilidades de formato
```yaml
tipo: regra
plataforma: [meta]
tema: criativo
tarefas: [configurar-anuncio, rodar-testes-e-experimentos]
fonte: fala
faixa: 00:00:00–00:00:32
perecivel: false
confianca: alta
versao: 1
```
Não procure um formato supremo entre imagem, vídeo ou carrossel; teste todas as possibilidades e use o que foi testado e deu mais resultado.

### U:367e808623ec5fe5:002 — Mantenha seis anúncios por grupo
```yaml
tipo: regua
plataforma: [meta]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:00:00–00:01:07
perecivel: false
confianca: alta
versao: 1
```
Mantenha seis anúncios rodando em cada grupo de anúncio.

### U:367e808623ec5fe5:003 — Varie anúncios e substitua os que não performam
```yaml
tipo: decisao
plataforma: [meta]
tema: criativo
tarefas: [configurar-anuncio, otimizar-anuncios]
fonte: fala
faixa: 00:00:32–00:01:07
condicoes: "verba alta para usar até cerca de oito anúncios"
perecivel: false
confianca: alta
versao: 1
```
Se um anúncio não estiver performando depois de alguns dias, pause-o e crie outro; o foco é variar e testar constantemente.

### U:367e808623ec5fe5:004 — Mantenha ativos os anúncios com vários anunciantes
```yaml
tipo: decisao
plataforma: [meta]
tema: posicionamentos-e-formatos
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:01:07–00:02:09
perecivel: true
confianca: alta
versao: 1
```
Quando encontrar a opção de exibir seu anúncio ao lado de anúncios de outros anunciantes, o professor prefere deixá-la ativa.

### U:367e808623ec5fe5:005 — Organize mídias em pastas da empresa antes da campanha
```yaml
tipo: procedimento
plataforma: [meta]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:02:09–00:04:33
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: acesso à Biblioteca de Mídia da empresa no Gerenciador de Negócios.
1. Abra Todas as ferramentas e acesse Gerenciador de negócios > Biblioteca de mídia.
2. Crie pastas, dê nome e descrição, e adicione os anúncios nelas; é possível criar pasta dentro de pasta.
3. Suba os anúncios na biblioteca antes de ir para a campanha.

### U:367e808623ec5fe5:006 — Envie várias mídias diretamente pela biblioteca
```yaml
tipo: procedimento
plataforma: [meta]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:04:33–00:05:49
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: arquivos de imagem ou vídeo já disponíveis no computador.
1. Prefira enviar os arquivos pela Biblioteca de Mídia, pois o professor relata que é mais rápido que enviá-los na criação da campanha.
2. Se precisar enviar no anúncio, clique em carregar, selecione os arquivos com Ctrl ou Command, ou clique no primeiro e use Shift no último.
3. Clique em abrir e escolha a mídia que será usada no anúncio.

### U:367e808623ec5fe5:007 — Use versões adequadas aos três grupos de formatos
```yaml
tipo: decisao
plataforma: [meta]
tema: posicionamentos-e-formatos
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:05:49–00:07:13
perecivel: true
confianca: alta
versao: 1
```
Quando a mídia de Stories estiver inadequada, substitua-a por uma versão verticalizada do mesmo anúncio.
Priorize Feed, anúncios em stream para vídeos e Reels, e Stories, Reels, apps e sites; coluna da direita e resultados da pesquisa são secundários.
Se tiver a versão retangular para o posicionamento secundário, inclua-a; o professor prefere pedir nova imagem de Feed para testar a adequar a imagem existente.

### U:367e808623ec5fe5:008 — Teste as otimizações automáticas do Meta
```yaml
tipo: decisao
plataforma: [meta]
tema: criativo
tarefas: [configurar-anuncio, rodar-testes-e-experimentos]
fonte: fala
faixa: 00:07:13–00:08:34
perecivel: true
confianca: alta
versao: 1
```
Quando quiser evitar otimizações automáticas, abra Todas as otimizações, desative todas e conclua.
O professor não gosta dessas alterações, mas relata que em alguns casos seu time as usa e os resultados melhoram; trate-as como teste.

### U:367e808623ec5fe5:009 — Use versão menor para Stories quando o vídeo for longo
```yaml
tipo: decisao
plataforma: [meta]
tema: posicionamentos-e-formatos
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:08:46–00:10:40
condicoes: "vídeo excede o limite de 45 segundos para Stories"
perecivel: true
confianca: alta
versao: 1
```
Se o anúncio não puder aparecer em certos posicionamentos por causa da duração, prefira substituir por vídeo equivalente e menor a cortá-lo.
Para Stories, use vídeo de até 45 segundos; acima disso, a pessoa precisa clicar para continuar assistindo. A recomendação automática de até 15 segundos não deve determinar o corte.

### U:367e808623ec5fe5:010 — Confira a prévia e edite o grupo de formato necessário
```yaml
tipo: procedimento
plataforma: [meta]
tema: posicionamentos-e-formatos
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:11:01–00:13:21
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: mídia adicionada ao anúncio.
1. Vá em avançar e verifique como o anúncio aparece nos diferentes posicionamentos.
2. Se algum posicionamento ficar estranho, escolha editar todos os anúncios de Feed e stream para vídeos e Reels, ou edite o grupo de Stories.
3. Faça edição de formato específico apenas quando precisar alterar aquele formato.

### U:367e808623ec5fe5:011 — Altere a miniatura somente se necessário
```yaml
tipo: decisao
plataforma: [meta]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:12:40–00:13:58
perecivel: true
confianca: alta
versao: 1
```
Se quiser mudar a capa do vídeo, selecione manualmente um frame ou carregue uma imagem como miniatura.
O professor não se preocuparia muito com a miniatura porque os vídeos tocam automaticamente.

### U:367e808623ec5fe5:012 — A aula não ensina copy de anúncios
```yaml
tipo: limite
plataforma: [meta]
tema: copy-e-roteiro
tarefas: []
fonte: fala
faixa: 00:13:58–00:14:43
perecivel: false
confianca: alta
versao: 1
```
A aula trata da operação do criativo, não de como criar bons anúncios ou desenvolver copy.

### U:367e808623ec5fe5:013 — Adicione até cinco textos principais e títulos
```yaml
tipo: regua
plataforma: [meta]
tema: copy-e-roteiro
tarefas: [configurar-anuncio, rodar-testes-e-experimentos]
fonte: fala
faixa: 00:13:58–00:16:01
perecivel: true
confianca: alta
versao: 1
```
É possível criar até cinco descrições de texto principal e até cinco títulos em um único anúncio; o Meta testa as variações para identificar a que funciona melhor.
O texto principal fica abaixo no Instagram e acima no Facebook; o título não aparece no Instagram.

### U:367e808623ec5fe5:014 — Use a descrição inferior com cautela
```yaml
tipo: decisao
plataforma: [meta]
tema: copy-e-roteiro
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:16:01–00:17:07
perecivel: true
confianca: alta
versao: 1
```
Quando usar o campo de descrição inferior, considere que o professor não gosta dele por achar que adiciona muita informação e tira foco do botão.
Não simule uma avaliação de 4.9 com estrelas se ela não for verdadeira, mesmo que outras pessoas usem isso e relatem melhora de resultado.

### U:367e808623ec5fe5:015 — Decida se o texto pode ser otimizado por pessoa
```yaml
tipo: decisao
plataforma: [meta]
tema: copy-e-roteiro
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:17:07–00:18:29
perecivel: true
confianca: alta
versao: 1
```
Se o título puder virar descrição sem deixar o anúncio estranho, errado ou esquisito, ative otimizar texto por pessoa.
Se essa troca prejudicar o anúncio, desative a opção.

### U:367e808623ec5fe5:016 — Priorize mídia, títulos e descrições nos testes
```yaml
tipo: regra
plataforma: [meta]
tema: criativo
tarefas: [rodar-testes-e-experimentos]
fonte: fala
faixa: 00:18:29–00:19:08
perecivel: false
confianca: alta
versao: 1
```
Não gaste tempo fazendo 50 testes de chamadas para ação; teste títulos, descrições e, principalmente, a mídia.

### U:367e808623ec5fe5:017 — Saiba Mais é a chamada para ação preferida
```yaml
tipo: regua
plataforma: [meta]
tema: copy-e-roteiro
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:18:29–00:20:13
perecivel: true
confianca: alta
versao: 1
```
O professor diz que 99,9% das pessoas usam Saiba Mais e a considera sua chamada para ação preferida.
Outras opções incluem Assinar, Inscreva-se agora, Agendar, Obter oferta, Ouvir agora, Pedir agora, Ver cardápio, Solicitar hora marcada, Comprar agora e Cadastre-se.

### U:367e808623ec5fe5:018 — Teste o criativo como conjunto completo
```yaml
tipo: conceito
plataforma: [meta]
tema: criativo
tarefas: [rodar-testes-e-experimentos]
fonte: fala
faixa: 00:18:29–00:19:43
perecivel: false
confianca: alta
versao: 1
```
O criativo inclui mídia, texto principal, título, descrição e chamada para ação; é o conjunto inteiro que pode fazer o anúncio funcionar ou não.
Teste vídeos e imagens diferentes mantendo texto e título quando fizer sentido, mas também teste conjuntos completos diferentes.