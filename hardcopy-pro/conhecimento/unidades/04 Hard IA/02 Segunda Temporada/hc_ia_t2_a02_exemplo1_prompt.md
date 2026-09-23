---
type: unidades-aula
status: revisado
title: "Aula 02 - Exemplo 1 - Prompt"
curso: hardcopy-pro
trilha: "04 Hard IA"
grupo: "04 Hard IA/02 Segunda Temporada"
modulo: "12"
ordem: 2
aula: G12_A02
aula_id: fcb539fa4b836e38
account_id: account.86ajrj8n9
fonte_repo: tc3midia/cursos
fonte_commit: 7470ca0
fontes:
  - transcricao.md
extraido_em: 2026-09-22
gerado_por: sonnet-5
retiradas: []
---

# Aula 02 - Exemplo 1 - Prompt

## Contexto da aula

Esta aula faz parte da trilha Hard IA, segunda temporada, como a segunda de uma sequência de exemplos práticos de uso de inteligência artificial na produção de anúncios.
O professor demonstra, na tela, o fluxo de montar um anúncio: refinar um texto já escrito com um assistente de IA em chat, escrever um prompt detalhado para gerar em uma ferramenta de vídeo por IA uma personagem falando o roteiro, extrair o áudio dos clipes gerados no CapCut e clonar vozes no ElevenLabs, inclusive a voz de uma pessoa pública real usada como exemplo de anúncio político.
A aula pressupõe que quem assiste já tem um roteiro de anúncio pronto de aulas anteriores do curso e já conhece conceitos de copy de outros módulos, que não são reexplicados aqui.
Boa parte do conteúdo é gravação de tela, com cliques em menus de diferentes ferramentas, o que deixa vários passos pouco descritos pela fala e não reconstituíveis só pela transcrição.
A aula termina depois de preparar as peças separadas do anúncio de exemplo (vídeos gerados por IA e vozes clonadas), deixando a montagem final da edição para a aula seguinte.
Não fazem parte desta aula etapas de veiculação, compra de domínio ou configuração de conta de anúncios: o foco é só a geração de vídeo e voz por IA para compor as peças do anúncio.

## Unidades

<a id="u-fcb539fa4b836e38-001"></a>

### U:fcb539fa4b836e38:001 — Pedir à IA só ajuste de encaixe narrativo, mantendo a ideia do anúncio
```yaml
tipo: "regra"
plataforma: [geral]
tema: "ia-para-copy-e-prompts"
tarefas: [refinar-saida-de-ia, criar-prompt-ou-agente]
fonte: fala
faixa: 00:00:24–00:01:30
perecivel: true
confianca: "alta"
versao: 1
evidencia: "o encaixe narrativo junto com vírgulas, pontos, etc"
```
Depois de já ter um texto de anúncio escrito, peça a um assistente de IA em chat que corrija só o encaixe narrativo do texto (pontuação como vírgulas e pontos, e a escolha de palavras para deixar mais fluido), mantendo a mesma ideia do anúncio original. A instrução deve deixar claro que a IA só ajusta a forma do texto, sem mudar o conceito por trás dele.

<a id="u-fcb539fa4b836e38-002"></a>

### U:fcb539fa4b836e38:002 — Nunca gerar copy 100% por IA; ela é extensão do trabalho do copywriter
```yaml
tipo: "regra"
plataforma: [geral]
tema: "ia-para-copy-e-prompts"
tarefas: [refinar-saida-de-ia]
fonte: fala
faixa: 00:03:30–00:04:15
perecivel: true
confianca: "alta"
versao: 1
evidencia: "nunca faça uma copy 100% criada por IA, não adianta, não presta."
```
Nunca produza uma copy 100% criada por IA: segundo o professor, não funciona bem. A IA deve ser tratada como extensão do trabalho do copywriter — em certos trechos ela pode escrever melhor do que o próprio redator, como aconteceu com uma frase do anúncio de exemplo, mas a ideia e o ângulo continuam sendo do redator. A regra é sempre juntar a IA com o próprio conhecimento, nunca depender só dela.

<a id="u-fcb539fa4b836e38-003"></a>

### U:fcb539fa4b836e38:003 — IA de vídeo não sustenta o mesmo rosto; descrever a personagem em detalhe
```yaml
tipo: "regra"
plataforma: [ia-de-video]
tema: "video-e-avatar-com-ia"
tarefas: [gerar-video-com-ia, criar-prompt-ou-agente]
fonte: fala
faixa: 00:04:26–00:04:58
perecivel: true
confianca: "media"
versao: 1
evidencia: "Ela não consegue sustentar o mesmo rosto da pessoa."
nota: "A ferramenta de geração de vídeo usada na aula é citada em trechos próximos como 'VO3'/'VL3 da Google'; a grafia adotada 'Veo 3' é hipótese, conforme tabela de grafias do curso."
```
Ferramentas de geração de vídeo por IA têm, segundo o professor, uma deficiência: não conseguem sustentar o mesmo rosto da mesma pessoa entre gerações diferentes. Para contornar isso, escreva no chat um prompt com o máximo de detalhes possível sobre a personagem — cabelo, olho, boca, roupa, cenário etc. — para que toda vez que um novo prompt for criado, ele mire a mesma pessoa descrita.

<a id="u-fcb539fa4b836e38-004"></a>

### U:fcb539fa4b836e38:004 — Estrutura do prompt para avatar falante em anúncio de vídeo por IA
```yaml
tipo: "estrutura"
plataforma: [ia-de-video]
tema: "video-e-avatar-com-ia"
tarefas: [criar-prompt-ou-agente, gerar-video-com-ia]
fonte: fala
faixa: 00:05:01–00:08:33
condicoes: "O exemplo do professor é um anúncio de cunho político, que ele mesmo trata como muito pessoal; cada pessoa deve montar seu próprio prompt a partir do que imagina para o seu próprio anúncio, não copiar o exemplo dele."
perecivel: true
confianca: "media"
versao: 1
evidencia: "uma mulher de branco em um programa de TV estilo morning show"
nota: "Ferramenta citada como 'VO3'/'VL3 da Google'; grafia adotada 'Veo 3' por hipótese, conforme tabela de grafias."
```
Estrutura do prompt para gerar, em ferramenta de vídeo por IA, uma personagem falando em um anúncio:
1. Contexto do anúncio: diga claramente do que se trata (no exemplo, um anúncio que une um tema político a uma copy).
2. Descrição física e de comportamento da personagem: cabelo, olhar, dicção etc.
3. Cenário e vestuário: onde a cena acontece (no exemplo, um estúdio estilo programa matinal de TV) e que roupa a personagem usa (no exemplo, traje social).
4. Idioma do prompt e da fala: escreva o prompt em inglês, mas inclua a instrução de que a personagem deve dizer, em português, uma frase exata definida por quem cria o anúncio.

<a id="u-fcb539fa4b836e38-005"></a>

### U:fcb539fa4b836e38:005 — Não usar prompt pronto da internet; escrever o próprio prompt de vídeo
```yaml
tipo: "regra"
plataforma: [geral]
tema: "ia-para-copy-e-prompts"
tarefas: [criar-prompt-ou-agente]
fonte: fala
faixa: 00:05:35–00:06:00
perecivel: true
confianca: "alta"
versao: 1
evidencia: "não fica com essa conversinha de ficar pegando prompt na internet"
```
Prompt é algo único para cada anúncio: não fique pegando prompt pronto na internet esperando que sirva para o seu caso. Escreva o seu próprio prompt a partir do que você imagina para o seu anúncio — segundo o professor, é assim que se aprende a criar prompts, em vez de ficar dependendo dos prompts de outras pessoas.

<a id="u-fcb539fa4b836e38-006"></a>

### U:fcb539fa4b836e38:006 — Gerar um resultado por vez no Veo 3 para não gastar 400 créditos à toa
```yaml
tipo: "regua"
plataforma: [ia-de-video]
tema: "video-e-avatar-com-ia"
tarefas: [gerar-video-com-ia]
fonte: fala
faixa: 00:09:17–00:09:44
condicoes: "Refere-se à configuração do Veo 3 (ferramenta de vídeo por IA) no momento da aula; o número de créditos e a opção de gerar quatro variações de uma vez podem mudar."
perecivel: true
confianca: "media"
versao: 2
evidencia: "se você colocar a quadra vai gastar 400 créditos"
nota: "Ferramenta citada como 'VO3'; grafia adotada 'Veo 3' por hipótese, conforme tabela de grafias."
```
Depois de colar o prompt no campo de texto-para-vídeo e conferir se está correto, gere apenas um resultado por vez. Pedir a geração em lote de quatro variações de uma só vez (o professor chama isso de 'uma quadra') consome 400 créditos.

<a id="u-fcb539fa4b836e38-007"></a>

### U:fcb539fa4b836e38:007 — Usar print do avatar gerado para manter a mesma personagem no próximo clipe
```yaml
tipo: "procedimento"
plataforma: [ia-de-video]
tema: "video-e-avatar-com-ia"
tarefas: [gerar-video-com-ia, criar-prompt-ou-agente]
fonte: fala
faixa: 00:09:57–00:11:11
perecivel: true
confianca: "baixa"
versao: 2
evidencia: "a mesma mulher é cenário e porém agora ela dizendo e agora colocamos aqui mais uma parte do vídeo"
nota: "Ferramenta de vídeo citada como 'VO3'/'VL3 da Google' (Veo 3, grafia adotada por hipótese). A fala menciona levar o print para o 'Google Chat', mas não fica claro se esse é o nome real da interface onde o próximo prompt é escrito; a transcrição não permite confirmar o destino exato da captura de tela."
```
Pré-condição: já existe um primeiro clipe de vídeo, gerado por IA, com a personagem/avatar falando a primeira parte do anúncio.
1. Tire um print (captura de tela) do quadro do vídeo já gerado, mostrando a aparência da personagem.
2. Leve essa captura para a ferramenta onde o próximo prompt será escrito.
3. Escreva a instrução pedindo a mesma mulher e o mesmo cenário, porém agora dizendo o próximo trecho do texto do anúncio.
4. Gere o clipe seguinte com esse prompt.

<a id="u-fcb539fa4b836e38-008"></a>

### U:fcb539fa4b836e38:008 — Limite: navegação de tela na continuidade de personagem no gerador de vídeo
```yaml
tipo: "limite"
plataforma: [ia-de-video]
tema: "video-e-avatar-com-ia"
tarefas: []
fonte: fala
faixa: 00:09:57–00:10:46
perecivel: true
confianca: "alta"
versao: 1
evidencia: "vamos printar aqui, aperta link no seu teclado"
nota: "Ferramenta citada como 'VO3'/'VL3 da Google'; grafia adotada 'Veo 3' por hipótese."
```
Na sequência em que o professor reaproveita o print do avatar já gerado para pedir a continuação do vídeo com a mesma personagem, parte da navegação fica só na tela: não é possível reconstituir, só pela fala, onde exatamente a captura é colada nem qual campo da ferramenta recebe a instrução seguinte. O procedimento registrado nesta base cobre apenas o que a fala nomeia com clareza.

<a id="u-fcb539fa4b836e38-009"></a>

### U:fcb539fa4b836e38:009 — Descrever o sentimento desejado no prompt de vídeo por IA
```yaml
tipo: "regra"
plataforma: [ia-de-video]
tema: "video-e-avatar-com-ia"
tarefas: [criar-prompt-ou-agente, gerar-video-com-ia]
fonte: fala
faixa: 00:11:11–00:11:47
perecivel: true
confianca: "media"
versao: 1
evidencia: "um sentimento de esperança que ele vai criar agora"
nota: "Ferramenta citada como 'VO3'; grafia adotada 'Veo 3' por hipótese, conforme tabela de grafias."
```
Ao escrever o prompt para o vídeo gerado por IA, diga explicitamente qual sentimento a personagem deve transmitir ao falar — no exemplo, um sentimento de esperança. Sem essa instrução, segundo o professor, a ferramenta não entrega a sensação pretendida na entonação. É assim que ele diz conseguir constância no que a ferramenta cria a cada novo trecho gerado.

<a id="u-fcb539fa4b836e38-010"></a>

### U:fcb539fa4b836e38:010 — Extrair áudio dos clipes gerados e juntar no CapCut antes de clonar a voz
```yaml
tipo: "procedimento"
plataforma: [capcut]
tema: "locucao-e-voz"
tarefas: [editar-video, produzir-locucao]
fonte: fala
faixa: 00:14:27–00:15:31
perecivel: true
confianca: "alta"
versao: 1
evidencia: "selecionamos todos eles, botão esquerdo do mouse, extrair áudio"
```
Pré-condição: todos os clipes de vídeo gerados por IA para o anúncio já estão importados e unidos em sequência no CapCut.
1. Selecione todos os clipes de vídeo.
2. Clique com o botão do mouse sobre a seleção e escolha a opção de extrair áudio.
3. Apague a faixa de vídeo, mantendo só o áudio extraído.
4. Duplique esse áudio até atingir a duração total desejada (no exemplo, cerca de dois minutos).
5. Exporte só o áudio e salve o arquivo.

<a id="u-fcb539fa4b836e38-011"></a>

### U:fcb539fa4b836e38:011 — Passo a passo do Instant Voice Clone do ElevenLabs
```yaml
tipo: "procedimento"
plataforma: [elevenlabs]
tema: "locucao-e-voz"
tarefas: [produzir-locucao]
fonte: fala
faixa: 00:15:38–00:16:56
perecivel: true
confianca: "media"
versao: 1
evidencia: "a gente vem em, no mais em, tá, é instant voice clone"
nota: "A fala menciona 'faz o download, desce aqui, faz o upload' de forma um pouco confusa quanto à ordem das ações; o passo que fica claro é o upload do áudio de referência. ElevenLabs aparece na transcrição como 'LevelLabs' e 'Eleven Lex'."
```
Pré-condição: há um arquivo de áudio de referência com a voz que se quer clonar (por exemplo, extraído de um clipe gerado por IA) e a ferramenta ElevenLabs está aberta.
1. Acesse a seção de clonagem instantânea de voz (Instant Voice Clone).
2. Faça o upload do arquivo de áudio de referência e avance.
3. Dê um nome para a voz clonada.
4. Selecione o idioma da voz (no exemplo, português).
5. Selecione o gênero (no exemplo, feminino) e uma idade aproximada (no exemplo, por volta de 30 anos).
6. Salve para concluir a clonagem.

<a id="u-fcb539fa4b836e38-012"></a>

### U:fcb539fa4b836e38:012 — Verificar o modelo Eleven 3 Alpha para mais humanidade na voz gerada
```yaml
tipo: "regra"
plataforma: [elevenlabs]
tema: "locucao-e-voz"
tarefas: [produzir-locucao]
fonte: fala
faixa: 00:17:36–00:17:56
condicoes: "Refere-se à disponibilidade do modelo/versão 'Eleven 3 Alpha' no ElevenLabs no momento da aula."
perecivel: true
confianca: "media"
versao: 1
evidencia: "confere se está no Eleven 3 aqui, Alfa"
nota: "Identificação de 'Eleven 3 Alfa' como um modelo/versão do ElevenLabs é interpretação a partir do contexto da fala; o nome exato e sua disponibilidade podem ter mudado."
```
No ElevenLabs, ao gerar a fala com a voz clonada, confira se está usando o modelo 'Eleven 3 Alpha' e se há uma atualização dele disponível. Segundo o professor, essa versão entrega mais efeito e mais 'humanidade' na fala gerada.

<a id="u-fcb539fa4b836e38-013"></a>

### U:fcb539fa4b836e38:013 — Clonar a voz de uma pessoa pública real para o anúncio de exemplo
```yaml
tipo: "procedimento"
plataforma: [elevenlabs, youtube]
tema: "politicas-e-bloqueios"
tarefas: [produzir-locucao]
fonte: fala
faixa: 00:18:22–00:20:57
condicoes: "Exemplo do professor usa uma pessoa pública real (chamada na aula de Lula, presidente do Brasil) num anúncio de cunho político que ele descreve como muito pessoal."
perecivel: true
confianca: "baixa"
versao: 1
evidencia: "precisamos aqui da voz de quem é nosso querido presidente"
nota: "Contorna política de plataforma ou direito de terceiros: o professor clona a voz de uma pessoa pública real e identificável (chamada na aula de Lula, presidente do Brasil) para fazê-la 'dizer', no anúncio, uma frase roteirizada que ela nunca disse. A transcrição da busca e triagem dos vídeos no YouTube é confusa nesse trecho; não é possível confirmar com certeza que o áudio finalmente usado é uma fala autêntica dele e não de outra pessoa comentando sobre ele nos resultados de busca."
```
Pré-condição: já se sabe qual pessoa pública real vai 'falar' no anúncio e há acesso à ferramenta de clonagem de voz.
1. Procure no YouTube um vídeo em que essa pessoa fala (no exemplo, um depoimento do presidente) e baixe o áudio.
2. Corte o áudio para manter só o trecho com a voz da pessoa, removendo música e ruído de fundo.
3. Use esse trecho como amostra de referência no mesmo procedimento de clonagem instantânea de voz (Instant Voice Clone), selecionando gênero e faixa etária compatíveis com a pessoa real.
4. Use a voz clonada para gerar, nessa voz, uma frase escrita por quem cria o anúncio — no exemplo, 'eu não tenho nada a ver com isso' — frase que a pessoa real nunca disse.

<a id="u-fcb539fa4b836e38-014"></a>

### U:fcb539fa4b836e38:014 — Quando a voz clonada falha, gravar e imitar a fala com a própria voz
```yaml
tipo: "decisao"
plataforma: [elevenlabs]
tema: "locucao-e-voz"
tarefas: [produzir-locucao]
fonte: fala
faixa: 00:24:00–00:24:20
perecivel: true
confianca: "alta"
versao: 1
evidencia: "como a gente fazia antigamente"
```
Quando a voz clonada por IA não conseguir, mesmo depois de várias tentativas de gerar de novo, produzir a frase exata desejada com naturalidade, grave você mesmo, com a sua própria voz, imitando a fala da pessoa, em vez de insistir na geração por IA. O professor chega a essa alternativa depois de repetidas tentativas malsucedidas de fazer a voz clonada dizer a frase de exemplo.

<a id="u-fcb539fa4b836e38-015"></a>

### U:fcb539fa4b836e38:015 — Limite: aula termina sem montar a edição final do anúncio
```yaml
tipo: "limite"
plataforma: [geral]
tema: "edicao-de-video"
tarefas: []
fonte: fala
faixa: 00:25:00–00:25:24
perecivel: true
confianca: "alta"
versao: 2
evidencia: "vou te mostrar como que você vai fazer para juntar tudo isso e fazer uma edição de foto"
```
Esta aula termina depois de preparar os elementos separados do anúncio de exemplo (vídeos gerados por IA e vozes clonadas), sem montar a edição final. O professor declara que vai mostrar como juntar tudo isso e fazer a edição completa do anúncio na aula seguinte.
