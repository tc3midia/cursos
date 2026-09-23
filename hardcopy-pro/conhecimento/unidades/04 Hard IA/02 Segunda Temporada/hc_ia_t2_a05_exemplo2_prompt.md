---
type: unidades-aula
status: revisado
title: "Aula 05 - Exemplo 2 - Prompt"
curso: hardcopy-pro
trilha: "04 Hard IA"
grupo: "04 Hard IA/02 Segunda Temporada"
modulo: "12"
ordem: 5
aula: G12_A05
aula_id: b337ecb123c0045d
account_id: account.86ajrj8n9
fonte_repo: tc3midia/cursos
fonte_commit: 42c88f6
fontes:
  - 04 Hard IA/02 Segunda Temporada/hc_ia_t2_a05_exemplo2_prompt.md
extraido_em: 2026-09-22
gerado_por: sonnet-5
retiradas: []
---

# Aula 05 - Exemplo 2 - Prompt

## Contexto da aula

Esta é a segunda aula de uma sequência sobre um anúncio para o nicho de insônia, dentro da trilha Hard IA (Segunda Temporada) do curso Hardcopy Pro.
A aula assume que a copy completa desse anúncio já foi escrita numa aula anterior e que quem assiste já sabe abrir e operar o gerador de vídeo por IA chamado Veo 3 (identificado na tabela de grafias do curso como Veo 3), o CapCut e o Voice Changer do ElevenLabs.
O professor demonstra, cena por cena, como transformar a copy em prompts de vídeo, gerar cada clipe, baixar e organizar as partes, manter o mesmo personagem visualmente consistente entre clipes diferentes e depois montar a trilha de voz do anúncio, parte gravada manualmente e parte convertida com o Voice Changer do ElevenLabs.
Boa parte da aula é edição de tela (cliques em CapCut e nas plataformas de IA) narrada de forma solta, então o conteúdo capturável pela transcrição está mais nas decisões de fluxo de trabalho do que nos cliques exatos.
A aula termina com as partes de vídeo e voz geradas por IA prontas, deixando para a aula seguinte a montagem com elementos do Canva e com a trilha sonora final.
Não há material de apoio escrito para esta aula.

## Unidades

<a id="u-b337ecb123c0045d-001"></a>

### U:b337ecb123c0045d:001 — Veo 3 no modo quality custa 100 créditos por geração
```yaml
tipo: "regua"
plataforma: [ia-de-video]
tema: "video-e-avatar-com-ia"
tarefas: [gerar-video-com-ia]
fonte: fala
faixa: 00:00:48–00:00:57
perecivel: true
confianca: "media"
versao: 2
evidencia: "vamos pegar um VO3 quality 100 créditos"
nota: "VO3 grafado como transcrito; identificado como hipótese com Veo 3, conforme tabela de grafias do curso. Custo de créditos é específico do plano/versão da ferramenta na época da gravação e pode mudar."
```
No início da aula, ao abrir um novo projeto de texto para vídeo no Veo 3, o modo 'quality' custa 100 créditos por geração.

<a id="u-b337ecb123c0045d-002"></a>

### U:b337ecb123c0045d:002 — Peça só o prompt à IA, não peça para ela criar o anúncio
```yaml
tipo: "regra"
plataforma: [geral]
tema: "ia-para-copy-e-prompts"
tarefas: [criar-prompt-ou-agente]
fonte: fala
faixa: 00:01:22–00:01:38
perecivel: true
confianca: "alta"
versao: 1
evidencia: "porque senão ele vai criar um anúncio junto com o prompt"
nota: "A transcrição não deixa claro qual ferramenta de IA de texto foi usada nessa etapa (soa como 'Google Prompt', termo não identificável com segurança); a orientação não depende de qual ferramenta é."
```
Ao usar uma IA de texto para transformar a copy do anúncio em um prompt de vídeo, não peça diretamente para ela 'criar um anúncio diferente': pedido assim faz a IA criar um anúncio novo junto com o prompt, misturando as duas coisas. Peça de forma mais restrita, focada só em gerar o prompt de vídeo a partir da copy que você já escreveu, sem deixar a IA reescrever o anúncio.

<a id="u-b337ecb123c0045d-003"></a>

### U:b337ecb123c0045d:003 — Partes de um prompt de cena para o gerador de vídeo por IA
```yaml
tipo: "estrutura"
plataforma: [ia-de-video]
tema: "video-e-avatar-com-ia"
tarefas: [criar-prompt-ou-agente, gerar-video-com-ia]
fonte: fala
faixa: 00:01:46–00:04:22
perecivel: true
confianca: "media"
versao: 2
evidencia: "então você tem que dar bastante bastante detalhe como que vai ser"
nota: "VO3 identificado como hipótese com Veo 3, conforme tabela de grafias do curso. Estrutura reconstruída a partir de falas fragmentadas enquanto o professor ditava e corrigia o prompt na tela; o texto exato do prompt não é reproduzido aqui."
```
Partes usadas para montar, num só prompt, a descrição de uma cena para o gerador de vídeo por IA (Veo 3):
1. Descrição física do personagem: idade, cor e comprimento do cabelo, cor dos olhos.
2. Cenário: local (ex.: quarto escuro), objeto de apoio (ex.: travesseiro branco), posição do corpo.
3. Tom emocional e referência de gênero (ex.: comparar com filme de terror), para guiar a atuação gerada.
4. Direção de tempo e de atuação: pausa antes da fala e como ela deve ser entregue (ex.: 'desesperada olhando para trás').
5. A fala do personagem na cena.
Quanto mais detalhe nessas partes, melhor o resultado; se a IA devolver a cena incompleta, peça para refazer explicando o que faltou.

<a id="u-b337ecb123c0045d-004"></a>

### U:b337ecb123c0045d:004 — Escreva o prompt em inglês mas peça fala em português do Brasil
```yaml
tipo: "regra"
plataforma: [ia-de-video]
tema: "video-e-avatar-com-ia"
tarefas: [gerar-video-com-ia, criar-prompt-ou-agente]
fonte: fala
faixa: 00:04:22–00:04:56
perecivel: true
confianca: "media"
versao: 2
evidencia: "passa o promo ultra realista com o máximo de informações possíveis em inglês, porém a mulher falando em português, português Brasil"
nota: "VO3 identificado como hipótese com Veo 3, conforme tabela de grafias do curso."
```
Ao escrever o prompt para o gerador de vídeo por IA (Veo 3), escreva-o em inglês, com o máximo de detalhe possível, buscando um resultado ultrarrealista. Mesmo com o prompt em inglês, informe explicitamente que a fala do personagem deve ser em português do Brasil.

<a id="u-b337ecb123c0045d-005"></a>

### U:b337ecb123c0045d:005 — Baixe em 720p e nomeie os clipes em sequência de partes
```yaml
tipo: "procedimento"
plataforma: [ia-de-video]
tema: "edicao-de-video"
tarefas: [gerar-video-com-ia, editar-video]
fonte: fala
faixa: 00:06:08–00:06:31
perecivel: true
confianca: "media"
versao: 2
evidencia: "vamos baixar ele aqui 720p tá bom ele vai fazer o download"
nota: "VO3 identificado como hipótese com Veo 3, conforme tabela de grafias do curso."
```
Pré-condição: um clipe de vídeo já foi gerado e aprovado no Veo 3.
1. Baixe o vídeo na resolução 720p.
2. Nomeie o arquivo salvo com um identificador sequencial de parte (parte 1, parte 2, parte 3...) que corresponda à ordem da cena dentro do anúncio.
Essa numeração mantém a ordem das cenas geradas separadamente para a montagem final do anúncio.

<a id="u-b337ecb123c0045d-006"></a>

### U:b337ecb123c0045d:006 — Prompt de vídeo não se generaliza entre copys diferentes
```yaml
tipo: "regra"
plataforma: [geral]
tema: "ia-para-copy-e-prompts"
tarefas: [criar-prompt-ou-agente]
fonte: fala
faixa: 00:09:02–00:09:29
perecivel: true
confianca: "alta"
versao: 1
evidencia: "prompt é a mesma coisa que copy, é muito, muito parte de uma só coisa que você está criando"
```
O professor evita entregar listas prontas de prompts para gerar vídeo por IA, porque, na visão dele, o prompt é tão parte da criação quanto a própria copy do anúncio: não dá para generalizar um prompt pronto para qualquer copy, já que cada anúncio tem a sua. Ele critica cursos e vendedores que prometem 'mil prompts prontos para a sua copy', dizendo que a promessa não corresponde a como o processo funciona de fato.

<a id="u-b337ecb123c0045d-007"></a>

### U:b337ecb123c0045d:007 — Use print do personagem como referência para manter consistência visual
```yaml
tipo: "regra"
plataforma: [ia-de-video]
tema: "video-e-avatar-com-ia"
tarefas: [gerar-video-com-ia]
fonte: fala
faixa: 00:10:20–00:12:30
perecivel: true
confianca: "media"
versao: 2
evidencia: "agora o médico que ela criou está na foto na cima de todos os detalhes possíveis para ela fazer o mesmo médico"
nota: "VO3 identificado como hipótese com Veo 3, conforme tabela de grafias do curso."
```
Para manter a aparência do mesmo personagem em cenas geradas separadamente no gerador de vídeo por IA (Veo 3), tire uma captura de tela do personagem já criado numa cena anterior e envie essa imagem como referência junto com o novo prompt, que descreve só a nova ação ou fala da cena. Também é possível enviar essa mesma captura para a conversa de texto usada para montar os prompts, pedindo que ela mantenha aquele personagem nas próximas descrições. Se você esquecer de anexar a imagem de referência, ainda há chance de a IA gerar um personagem parecido, porque a mesma sessão já havia criado aquele personagem antes.

<a id="u-b337ecb123c0045d-008"></a>

### U:b337ecb123c0045d:008 — Grave manualmente as vozes de barulho em poucas tomadas contínuas
```yaml
tipo: "procedimento"
plataforma: [capcut]
tema: "som-e-sentimentalismo"
tarefas: [sonorizar-video, produzir-locucao]
fonte: fala
faixa: 00:14:07–00:18:38
condicoes: "Demonstração do professor no anúncio de insônia, para produzir o áudio dos barulhos e vozes que a personagem escuta à noite; ele grava com a própria voz."
perecivel: true
confianca: "media"
versao: 2
evidencia: "vamos pegar as 3 vozes aqui"
nota: "O professor faz três tomadas nesta demonstração; os ajustes de cada faixa ele executa na tela e a fala só nomeia volume, velocidade, efeito de voz e duplicação."
```
Pré-condição: as cenas geradas por IA já estão no projeto e falta o áudio das vozes e barulhos que o personagem escuta; essa parte é feita de forma manual, não pela IA.
1. Abra o gravador de voz do CapCut e grave você mesmo poucas tomadas; o professor fez três.
2. Em cada tomada, encadeie numa gravação contínua várias frases curtas seguidas, que representem cobranças e pensamentos diferentes do dia a dia do personagem, no formato "amanhã você tem que...", fechando com as perguntas de angústia sobre não conseguir dormir.
3. Trate cada gravação separadamente na linha do tempo: deixe uma mais baixa, divida outra e mexa na velocidade, e aplique um efeito de voz na que for reconhecível.
4. Duplique as faixas para somar as vozes e salve o conjunto como um arquivo de áudio único, que o professor nomeia voz de barulho.

<a id="u-b337ecb123c0045d-009"></a>

### U:b337ecb123c0045d:009 — Nem toda tarefa simples precisa ser feita pela IA
```yaml
tipo: "regra"
plataforma: [geral]
tema: "locucao-e-voz"
tarefas: [produzir-locucao]
fonte: fala
faixa: 00:15:33–00:16:17
perecivel: true
confianca: "alta"
versao: 1
evidencia: "dá pra IA fazer isso? Dá, mas cara, olha o tanto que isso ia demandar trabalho, token"
```
Nem toda etapa da produção precisa ser feita por inteligência artificial. Mesmo quando a IA seria capaz de executar uma tarefa simples, como gravar várias falas curtas, o professor recomenda avaliar o trabalho e o gasto de token envolvidos: em tarefas assim, o próprio produtor pode gravar a fala manualmente em vez de acionar a IA.

<a id="u-b337ecb123c0045d-010"></a>

### U:b337ecb123c0045d:010 — Distorça a própria voz gravada quando ela for reconhecível
```yaml
tipo: "regra"
plataforma: [capcut]
tema: "locucao-e-voz"
tarefas: [produzir-locucao]
fonte: fala
faixa: 00:17:01–00:17:20
condicoes: "Relevante para quem tem voz reconhecível pelo público e não quer se identificar numa gravação específica do anúncio."
perecivel: true
confianca: "alta"
versao: 1
evidencia: "que é algo que não dá pra lembrar, que é a minha voz, né? Porque muita gente conhece ela"
```
Ao usar a própria voz gravada como uma das camadas de áudio do anúncio, aplique um efeito de distorção nela no CapCut quando a voz for reconhecível por muitas pessoas, para que essa gravação específica não seja identificada como sendo sua.

<a id="u-b337ecb123c0045d-011"></a>

### U:b337ecb123c0045d:011 — Sussurro emotivo pede Voice Changer, não texto-para-fala
```yaml
tipo: "decisao"
plataforma: [elevenlabs]
tema: "locucao-e-voz"
tarefas: [produzir-locucao]
fonte: fala
faixa: 00:21:38–00:22:06
perecivel: true
confianca: "alta"
versao: 1
evidencia: "ela tá falando muito baixo, ela tá dando muita emoção, então temos que continuar essa emoção"
```
Quando a fala original de um personagem for muito baixa (sussurrada) e carregada de emoção, o texto-para-fala do ElevenLabs não reproduz bem esse resultado. Nesse caso, continue usando a função de troca de voz (Voice Changer) sobre uma gravação da própria voz do produtor, em vez de gerar a fala a partir de texto digitado, para preservar a emoção da interpretação original.

<a id="u-b337ecb123c0045d-012"></a>

### U:b337ecb123c0045d:012 — Montagem fina no CapCut ficou só na tela
```yaml
tipo: "limite"
plataforma: [capcut]
tema: "edicao-de-video"
tarefas: []
fonte: fala
faixa: 00:24:00–00:30:33
perecivel: true
confianca: "alta"
versao: 1
evidencia: "então aqui a gente vai dar um CTRL B e a gente vai criar Clip Composta agora"
```
Boa parte da montagem final do anúncio (agrupar clipes como 'clipe composto', cortar trechos exatos da linha do tempo, posicionar e sincronizar camadas de áudio no CapCut) é demonstrada apontando diretamente na tela, sem que a fala nomeie cada clique com precisão suficiente para reconstruir os passos exatos a partir da transcrição.

<a id="u-b337ecb123c0045d-013"></a>

### U:b337ecb123c0045d:013 — Fluxo para dublar personagens gerados por IA com ElevenLabs
```yaml
tipo: "procedimento"
plataforma: [elevenlabs, capcut]
tema: "locucao-e-voz"
tarefas: [produzir-locucao, editar-video]
fonte: fala
faixa: 00:24:37–00:30:24
perecivel: true
confianca: "media"
versao: 1
evidencia: "Confere se a voz casou com o rosto dele"
nota: "Reconstruído a partir de falas fragmentadas sobre uma sequência de edição feita majoritariamente apontando na tela; os cliques exatos de organização dos clipes não são descritos em detalhe pela transcrição."
```
Pré-condição: as falas de cada personagem já foram gravadas com a voz do produtor e o vídeo gerado por IA já está no editor.
1. Separe e exporte, do editor de vídeo, apenas o trecho de áudio correspondente a um personagem por vez.
2. Leve esse áudio ao Voice Changer do ElevenLabs e aplique a voz escolhida para aquele personagem.
3. Traga o áudio convertido de volta para o editor de vídeo e sincronize com o movimento da boca do personagem na cena.
4. Confira se a voz combina com o rosto/movimento labial; se estiver fora do tempo, desloque o áudio um pouco para frente ou para trás até encaixar.

<a id="u-b337ecb123c0045d-014"></a>

### U:b337ecb123c0045d:014 — Escolha preset de voz do ElevenLabs conforme o personagem
```yaml
tipo: "regra"
plataforma: [elevenlabs]
tema: "locucao-e-voz"
tarefas: [produzir-locucao]
fonte: fala
faixa: 00:27:36–00:28:05
perecivel: true
confianca: "alta"
versao: 1
evidencia: "vamos procurar uma voz aqui legal para ele no Eleven Labs"
nota: "Preset de voz citado como 'grandpa' na biblioteca do ElevenLabs."
```
Ao trocar a voz de um personagem no Voice Changer do ElevenLabs, escolha, na biblioteca de vozes, um preset que combine com o tipo do personagem (por exemplo, uma voz predefinida de idoso, citada como 'grandpa', usada para dublar um personagem médico mais velho), em vez de usar sempre a mesma voz para todos os personagens.

<a id="u-b337ecb123c0045d-015"></a>

### U:b337ecb123c0045d:015 — Aula deixa Canva e trilha sonora para a próxima aula
```yaml
tipo: "limite"
plataforma: [canva, geral]
tema: "edicao-de-video"
tarefas: []
fonte: fala
faixa: 00:35:02–00:35:30
perecivel: true
confianca: "alta"
versao: 1
evidencia: "na próxima aula a gente vai juntar todas essas peças aqui junto com o Canva"
```
A aula termina com as partes geradas por IA (vídeo e voz) prontas, mas deixa para a próxima aula juntar essas peças com os elementos do Canva (pequenas partes gráficas do anúncio) e com a trilha sonora, que serve para reforçar emocionalmente a dor do público sobre a insônia.
