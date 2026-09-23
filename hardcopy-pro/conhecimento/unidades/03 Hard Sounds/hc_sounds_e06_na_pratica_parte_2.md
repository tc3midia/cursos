---
type: unidades-aula
status: revisado
title: "Episódio 6 - Na prática (Parte 2)"
curso: hardcopy-pro
trilha: "03 Hard Sounds"
grupo: "03 Hard Sounds"
modulo: "10"
ordem: 6
aula: G10_A06
aula_id: dc249ec660e8014d
account_id: account.86ajrj8n9
fonte_repo: tc3midia/cursos
fonte_commit: 42c88f6
fontes:
  - 03 Hard Sounds/hc_sounds_e06_na_pratica_parte_2.md
extraido_em: 2026-09-22
gerado_por: sonnet-5
retiradas: []
---

# Episódio 6 - Na prática (Parte 2)

## Contexto da aula

Esta aula é a segunda parte prática de uma sequência do módulo Hard Sounds do curso Hardcopy Pro, dedicada à sonorização de um anúncio ou VSL dentro de um editor de vídeo.
O professor demonstra ao vivo como extrair a trilha original de um vídeo, encontrar o trecho mais importante da música (o plot da música) e usá-lo estrategicamente ao longo da peça.
A aula pressupõe que quem assiste já viu a parte teórica sobre sentimentalismo, trilha e efeitos sonoros dada em aulas anteriores, e foca só na execução prática dentro da ferramenta de edição.
Boa parte do conteúdo é mostrado só na tela, com o professor cortando, arrastando e posicionando clipes enquanto aponta com termos como 'aqui' e 'bem aqui', então a transcrição captura sobretudo os princípios por trás de cada ação, não cada clique.
O professor reforça técnicas de retenção com efeitos sonoros no início e ao longo do vídeo, o uso de calar a boca para dar destaque a falas importantes, e uma orientação para não copiar literalmente os efeitos que ele usa como exemplo.
A aula não nomeia o software de edição usado, não fornece os arquivos de música e efeitos citados, e adia para a aula seguinte a repetição do mesmo exercício com outra música.

## Unidades

<a id="u-dc249ec660e8014d-001"></a>

### U:dc249ec660e8014d:001 — Extrair a trilha do vídeo e usar o plot da música no final
```yaml
tipo: "procedimento"
plataforma: [geral]
tema: "som-e-sentimentalismo"
tarefas: [sonorizar-video, editar-video]
fonte: fala
faixa: 00:00:00–00:02:02
perecivel: true
confianca: "alta"
versao: 1
evidencia: "Vamos clicar com o botão do mouse e extrair áudio."
```
Pré-condição: o vídeo com a música original já está importado na timeline do editor.
1. Clique com o botão do mouse sobre o clipe de vídeo e escolha a opção de extrair o áudio dele.
2. Delete a faixa de vídeo; a música extraída fica isolada na faixa de baixo da timeline.
3. Ouça a música inteira e localize o trecho mais impactante dela, o plot da música (a parte mais importante da música); ele costuma aparecer logo depois de um trecho com pouco ou nenhum som.
4. Corte fora o restante da música e mantenha só esse trecho do plot, aplicando um fade nele para suavizar a entrada.
5. Arraste esse trecho para o final do vídeo, no ponto em que o vídeo termina.
6. Se quiser esse trecho final mais longo e não conseguir esticar arrastando, reduza a velocidade do áudio para 0.4 para aumentar sua duração sem cortar mais nada.

<a id="u-dc249ec660e8014d-002"></a>

### U:dc249ec660e8014d:002 — Recortar só o trecho da música pra dificultar detecção do Facebook e TikTok
```yaml
tipo: "regra"
plataforma: [meta-ads, tiktok]
tema: "politicas-e-bloqueios"
tarefas: [revisar-risco-de-bloqueio, sonorizar-video]
fonte: fala
faixa: 00:02:02–00:02:17
condicoes: "Vale para o uso de música comercial protegida por direitos autorais no anúncio."
perecivel: true
confianca: "alta"
versao: 1
evidencia: "Com essa parte aqui, o Facebook, TikTok não vai conseguir identificar essa música"
nota: "Contorna política de plataforma ou direito de terceiros: o professor ensina a manter só um trecho curto da música comercial (o plot) em vez da faixa completa, para reduzir a chance de o Facebook e o TikTok identificarem a música e bloquearem o anúncio por direito autoral."
```
Ao usar uma música comercial protegida, mantenha na peça só o trecho pequeno que interessa (o plot da música) e apague o restante da faixa. Segundo o professor, usar somente esse trecho reduz a chance de o Facebook e o TikTok identificarem a música por direito autoral, permitindo anunciar sem bloqueio.

<a id="u-dc249ec660e8014d-003"></a>

### U:dc249ec660e8014d:003 — Música sozinha não gera vontade de clicar; precisa de efeito sonoro
```yaml
tipo: "regra"
plataforma: [geral]
tema: "som-e-sentimentalismo"
tarefas: [sonorizar-video]
fonte: fala
faixa: 00:02:17–00:02:35
perecivel: false
confianca: "alta"
versao: 1
evidencia: "Não dá aquele tesão, não dá aquela vontade de clicar, não dá ainda, ainda não dá."
```
Colocar apenas a música de fundo, sem nenhum efeito sonoro adicional, deixa a peça sem graça. Segundo o professor, isso não gera vontade de clicar no anúncio; é preciso somar efeitos sonoros à música para dar ênfase e criar o impacto que faz a pessoa querer continuar assistindo.

<a id="u-dc249ec660e8014d-004"></a>

### U:dc249ec660e8014d:004 — Sempre abrir o anúncio com um efeito de impacto no início
```yaml
tipo: "regra"
plataforma: [geral]
tema: "som-e-sentimentalismo"
tarefas: [sonorizar-video]
fonte: fala
faixa: 00:03:05–00:04:53
perecivel: false
confianca: "alta"
versao: 1
evidencia: "O início, sempre você tem que dar um boom."
```
No início de qualquer anúncio, insira um efeito sonoro de impacto forte (um 'boom') para prender a atenção da pessoa antes mesmo de ela processar a música. Não importa qual seja a música escolhida, desde que ela também tenha esse impacto forte de abertura e depois vá se acalmando; sem esse efeito de entrada, o professor descreve o resultado como sem graça e sem sal.

<a id="u-dc249ec660e8014d-005"></a>

### U:dc249ec660e8014d:005 — Usar quadro-chave pra destacar o volume do efeito só no boom inicial
```yaml
tipo: "procedimento"
plataforma: [geral]
tema: "som-e-sentimentalismo"
tarefas: [sonorizar-video]
fonte: fala
faixa: 00:03:48–00:04:09
perecivel: true
confianca: "alta"
versao: 1
evidencia: "a gente clica em cima dele clica aqui adicionar quadro chave"
```
Pré-condição: o efeito sonoro de abertura já está posicionado na timeline com o volume geral baixo.
1. Clique sobre o efeito sonoro selecionado.
2. Adicione um quadro-chave (keyframe) de volume no ponto inicial dele.
3. Aumente o volume só nesse ponto, no momento do impacto.
4. Avance um pouco na timeline e adicione outro quadro-chave reduzindo o volume de volta ao nível baixo.
Isso cria um pico de volume só no momento do boom inicial, sem deixar o efeito alto durante todo o restante da faixa.

<a id="u-dc249ec660e8014d-006"></a>

### U:dc249ec660e8014d:006 — Efeitos favoritados também aparecem buscando o mesmo termo na busca
```yaml
tipo: "ferramenta"
plataforma: [geral]
tema: "som-e-sentimentalismo"
tarefas: [sonorizar-video]
fonte: fala
faixa: 00:07:33–00:07:46
perecivel: true
confianca: "alta"
versao: 1
evidencia: "É só você escrever aqui nessa barra de pesquisa que você vai achar do mesmo jeito que tá aqui."
```
Os efeitos sonoros que o professor guarda como favoritos na ferramenta de edição não são exclusivos dele: qualquer pessoa consegue achar o mesmo efeito digitando o mesmo termo de busca na barra de pesquisa de efeitos, sem precisar ter esse efeito salvo como favorito antes.

<a id="u-dc249ec660e8014d-007"></a>

### U:dc249ec660e8014d:007 — Buscar música ou efeito pelo sentimento desejado, como 'suspense'
```yaml
tipo: "regra"
plataforma: [geral]
tema: "som-e-sentimentalismo"
tarefas: [sonorizar-video]
fonte: fala
faixa: 00:08:09–00:08:37
perecivel: true
confianca: "alta"
versao: 1
evidencia: "Se você vir aqui e escrever suspense em música, olha o que vai acontecer"
```
Para reforçar um sentimento específico do roteiro (por exemplo, arrepio, raiva ou suspense em um trecho que desmistifica o produto), digite diretamente esse sentimento, como 'suspense', na busca de música ou efeitos da ferramenta de edição; a busca retorna opções sonoras compatíveis com a emoção desejada.

<a id="u-dc249ec660e8014d-008"></a>

### U:dc249ec660e8014d:008 — Calar a boca no início de uma transição ou revelação
```yaml
tipo: "regra"
plataforma: [geral]
tema: "som-e-sentimentalismo"
tarefas: [sonorizar-video, escrever-desenvolvimento-e-plot-twist]
fonte: fala
faixa: 00:06:43–00:07:00
perecivel: false
confianca: "alta"
versao: 1
evidencia: "vamos calar a boca No início Da transição, para não ficar"
```
Antes de uma transição de cena ou de um momento de revelação (o plot), silencie completamente a música, técnica que o curso chama de calar a boca. O professor faz isso já no início da transição, para que a mudança não fique estranha e para que a fala ou o efeito daquele momento ganhe destaque sem concorrência do som de fundo.

<a id="u-dc249ec660e8014d-009"></a>

### U:dc249ec660e8014d:009 — Usar o som real do objeto ou da dor mencionada na fala
```yaml
tipo: "regra"
plataforma: [geral]
tema: "som-e-sentimentalismo"
tarefas: [sonorizar-video]
fonte: fala
faixa: 00:11:12–00:12:06
perecivel: false
confianca: "alta"
versao: 1
evidencia: "se você está tocando em uma dor do seu lead e você está falando da geladeira, é importante você colocar o barulho da geladeira."
```
Quando a fala menciona um objeto ou uma dor específica do lead (por exemplo, uma geladeira, ou o momento de uma notificação de venda), insira em volume baixo o efeito sonoro correspondente a esse objeto ou situação (o barulho real da geladeira, o som de uma notificação). Isso ajuda o espectador a lembrar e associar aquele som ao que está sendo vendido ou prometido.

<a id="u-dc249ec660e8014d-010"></a>

### U:dc249ec660e8014d:010 — Faixa específica de transição não pode ser compartilhada por limite de licença
```yaml
tipo: "limite"
plataforma: [outra]
tema: "som-e-sentimentalismo"
tarefas: []
fonte: fala
faixa: 00:12:09–00:12:33
perecivel: true
confianca: "baixa"
versao: 1
evidencia: "Eu não consigo compartilhar nem nada disso"
nota: "Termos 'Epic' e 'Metro W A' ficam como transcritos; a identificação da biblioteca ou faixa de áudio é incerta."
```
O professor cita uma faixa cujo início já funciona como transição, chamada (como transcrito) de 'Epic', com o nome 'Metro W A'. Ele diz não conseguir compartilhar esse arquivo com os alunos porque a fonte dela é limitada para esse tipo de compartilhamento. A aula não indica onde encontrar essa faixa específica.

<a id="u-dc249ec660e8014d-011"></a>

### U:dc249ec660e8014d:011 — Dar pistas da música principal ao longo do vídeo e reservá-la pro final
```yaml
tipo: "regra"
plataforma: [geral]
tema: "som-e-sentimentalismo"
tarefas: [sonorizar-video, estruturar-vsl]
fonte: fala
faixa: 00:14:42–00:16:04
perecivel: true
confianca: "alta"
versao: 1
evidencia: "Eu vou dando pista da música com o decorrer do vídeo"
nota: "O professor atribui a si mesmo um teste A/B que confirmaria a eficácia dessa técnica; a base registra a afirmação, sem confirmar o resultado."
```
Ao longo do vídeo, dê pistas da música de assinatura (trechos curtos, sem entregá-la por completo) e reserve o trecho principal dela para o final. Isso faz a pessoa assistir até o fim esperando ouvir aquele trecho; ao entregá-lo no final, gera-se uma sensação de recompensa que, segundo o professor, aumenta a chance de a pessoa clicar. Ele afirma ter testado essa técnica em teste A/B e diz que funciona.

<a id="u-dc249ec660e8014d-012"></a>

### U:dc249ec660e8014d:012 — Modificar a voz do efeito ao repetir a mesma peça sonora
```yaml
tipo: "regra"
plataforma: [geral]
tema: "som-e-sentimentalismo"
tarefas: [sonorizar-video]
fonte: fala
faixa: 00:17:25–00:17:43
condicoes: "Vale quando o mesmo efeito sonoro de voz ou chamada é reaproveitado mais de uma vez no mesmo vídeo."
perecivel: true
confianca: "alta"
versao: 1
evidencia: "vamos modificar a voz para não ficar repetido"
```
Ao copiar e colar o mesmo efeito sonoro de voz ou chamada em outro ponto do vídeo, modifique a voz desse efeito (aplicando um modificador diferente) para que ele não pareça repetido para quem está assistindo.

<a id="u-dc249ec660e8014d-013"></a>

### U:dc249ec660e8014d:013 — Não copiar o material do professor; usar o ensinamento com a própria essência
```yaml
tipo: "regra"
plataforma: [geral]
tema: "criatividade-e-angulo"
tarefas: [gerar-variacoes-de-criativo]
fonte: fala
faixa: 00:18:36–00:19:48
perecivel: false
confianca: "alta"
versao: 2
evidencia: "hoje tem muito anúncio e muita BSL baseada na minha"
nota: "A transcrição grafa 'BSL' para VSL, 'chat EPT' para ChatGPT, 'ROD' para ROI e 'RedCop' para Hard Copy. Na parte final do trecho o professor ilustra o resultado de quem copia com 'ROD 1 ROD 0.8', dito como resultado normal e como ilustração dele, não como parâmetro de decisão."
```
O professor diz que vê muitos anúncios e VSLs baseados nos dele e pede que ninguém se apegue a copiar o que ele mostra: nem os efeitos sonoros e as músicas escolhidos na aula, nem o anúncio ou a VSL inteira.
A orientação dele é pegar o ensinamento e a própria essência e aplicar no projeto de cada um, em vez de fazer mais do mesmo só para copiar.
Ele afirma que copiar ficou no passado e que agora é a época de criar.
Como argumento, lembra que copiar é fácil — jogar o texto no ChatGPT, pedir que ele refaça um resumo e editar — e que isso entrega só o resultado normal, sem nada próprio.
A recomendação e o julgamento de resultado são do professor.

<a id="u-dc249ec660e8014d-014"></a>

### U:dc249ec660e8014d:014 — Centralizar o efeito de transição entre duas camadas de áudio
```yaml
tipo: "regra"
plataforma: [geral]
tema: "som-e-sentimentalismo"
tarefas: [sonorizar-video]
fonte: fala
faixa: 00:23:06–00:23:22
condicoes: "Vale quando o efeito de transição está sendo usado para ligar duas camadas de áudio diferentes, como a música principal e um efeito modificado."
perecivel: true
confianca: "media"
versao: 1
evidencia: "na parte laranja ela está centralizada entre a música do Pink Floyd"
```
Ao usar um efeito sonoro de transição para ligar duas camadas de áudio diferentes (por exemplo, a música principal e um efeito de voz modificado), posicione esse efeito de transição centralizado exatamente entre essas duas camadas, para que ele funcione como ponte entre elas.

<a id="u-dc249ec660e8014d-015"></a>

### U:dc249ec660e8014d:015 — Muitos cortes e posicionamentos exatos na timeline ficaram só na tela
```yaml
tipo: "limite"
plataforma: [geral]
tema: "edicao-de-video"
tarefas: []
fonte: fala
faixa: 00:00:00–00:25:24
perecivel: false
confianca: "alta"
versao: 1
evidencia: "Vamos arrastar e vamos colocar ela"
```
Grande parte desta aula mostra o professor arrastando, cortando e posicionando clipes de música e efeitos sonoros na timeline de um editor de vídeo, apontando com termos como 'aqui' e 'bem aqui'. A transcrição não nomeia a ferramenta usada nem dá os valores exatos de cada corte ou posição na timeline; esses detalhes ficaram só na imagem e não entram nos procedimentos desta base.
