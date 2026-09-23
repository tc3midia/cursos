# Aula 6 — Pixel eventos e dominios

Transcrição automática pelo Whisper `large-v3-turbo` em português. Não revisada contra o áudio.
Módulo: Módulo 09 - Facebook e Instagram Ads.

## Parte 1 — m9_a6_p1_pixel_eventos_e_dominios.mp4

Origem: https://drive.google.com/drive/folders/1IscwBtiyGPNNtEAq6NV2CWASDx-7SGSB?hl=pt-br
SHA-256: `3a0b2c08405f8ebad30401e4d5c222d7095fd0c72e99ceebb553da1414400238`. Duração: 00:27:26.061.

[00:00:00–00:00:13] Nessa aula você vai saber todas as características possíveis, como utilizar, o que é, o que não é.

[00:00:13–00:00:17] E eu estou falando de pixel, de eventos e de domínios.

[00:00:19–00:00:27] Recentemente, num passado também não tão distante, a Apple lançou uma política de privacidade

[00:00:27–00:00:34] que permite que o usuário escolha ou não escolha ser rastreados por aplicativos, tá?

[00:00:35–00:00:36] E por que eu estou falando isso?

[00:00:36–00:00:45] Porque algumas regras entraram depois dessa lei, vamos dizer assim, que eles estabeleceram, né?

[00:00:45–00:00:52] E não se preocupe que eu vou deixar uma aula aqui nesse módulo também falando apenas das boas práticas do S14, tá?

[00:00:52–00:00:58] Eu não quis misturar aqui, porque você vai ver o que é um pixel, o que é um API de conversão,

[00:00:58–00:01:05] o que é um evento, o que é uma conversão personalizada, e também a parte de domínio.

[00:01:05–00:01:11] Se você, por exemplo, anunciava há mais de um ano e meio atrás,

[00:01:11–00:01:14] essas características que eu vou explicar nessa aula não tinha.

[00:01:15–00:01:19] Mas, de novo, como a gente tem que se adequar, tem que jogar as regras do jogo,

[00:01:19–00:01:25] É algo de extrema importância e a gente vai ver tudo sobre pixel, eventos e domínios.

[00:01:26–00:01:32] O que é, como visualizar, como pegar, como saber se está funcionando, enfim.

[00:01:33–00:01:35] Nós vamos ver tudo nessa aula aqui.

[00:01:35–00:01:38] Então, iniciando aqui, pixel, eventos e domínios.

[00:01:39–00:01:42] O que é um pixel? Características principais.

[00:01:42–00:01:44] Deve ser instalado em todas as páginas do seu site.

[00:01:44–00:01:52] Ele envia parâmetros, por exemplo, da web pelos navegadores usados pelos usuários

[00:01:52–00:01:55] direto para os servidores do Facebook, tá?

[00:01:56–00:02:01] Tem duas grandes diferenças e você vai acompanhar aqui.

[00:02:01–00:02:03] Depois eu vou colocar o resumo aqui, tá?

[00:02:04–00:02:05] Pixel

[00:02:05–00:02:09] e

[00:02:09–00:02:11] API.

[00:02:11–00:02:28] Ou seja, aqui está o seu site, aqui está o seu site, e aqui está o servidor do Facebook, certo?

[00:02:29–00:02:30] E aqui está o servidor do Facebook.

[00:02:31–00:02:36] E aqui estão as pessoas que ainda não entraram no seu site.

[00:02:37–00:02:39] Essa é a função do Pixel, tá?

[00:02:39–00:03:08] A função do Pixel é o seguinte, você vai fazer uma campanha e vai colocar pessoas dentro do seu site, pessoas dentro do seu site, pessoas dentro do seu site, e aí nesse seu site aqui tem um botão, né, um botão de compra, um botão de cadastro, enfim, e o Facebook vai identificar todas as ações que essas pessoas fazem aqui dentro da sua página, tá?

[00:03:08–00:03:16] Então, essas informações aqui, elas serão enviadas direto para o servidor do Facebook, beleza?

[00:03:17–00:03:18] Para o servidor do Facebook.

[00:03:19–00:03:24] E em paralelo, tem o seu servidor também, que fica ali só recebendo os dados, né?

[00:03:24–00:03:29] Aqui ele não tem nenhuma influência direta, tá?

[00:03:29–00:03:33] Então, a função do Pixel, né? A característica principal do Pixel

[00:03:33–00:03:39] é você poder rastrear todos os movimentos que os usuários fazem no seu site, beleza?

[00:03:41–00:03:45] Tenha certeza de que os seus anúncios serão mostrados às pessoas certas,

[00:03:45–00:03:49] gere mais vendas com pixel inteligente e mensure os resultados, né?

[00:03:49–00:03:55] Uma característica importante também é, quanto mais pessoas você envia para o seu site,

[00:03:55–00:04:02] quanto mais pessoas compram de você, o Facebook consegue identificar pessoas parecidas, né?

[00:04:02–00:04:08] Pessoas semelhantes com essas que você acaba atingindo de primeiro momento, né?

[00:04:08–00:04:13] Então, ele pega mais ou menos um perfil de usuário e começa a distribuir os seus anúncios

[00:04:13–00:04:17] para outras pessoas parecidas com essas que entram no seu site, né?

[00:04:17–00:04:20] Por isso que o Pixel, ele fica inteligente, tá?

[00:04:21–00:04:26] Então, basicamente, essas são as características do Pixel.

[00:04:27–00:04:29] Lucas, como pegar, enfim, como instalar?

[00:04:29–00:04:34] Essa aula aqui eu reservei apenas para ser uma aula teórica, tá?

[00:04:34–00:04:37] Para você entender toda a questão de pixel, eventos e domínios.

[00:04:38–00:04:44] Aqui embaixo vai ter uma parte de número 2 e aí é onde vai ser a instalação prática, tá?

[00:04:44–00:04:49] Ou seja, nós vamos ver onde pega, eu posso até dar um pequeno spoiler aqui depois na minha conta,

[00:04:49–00:04:53] onde pega, como pega e como instala, tá?

[00:04:53–00:04:57] Do zero, o passo a passo, vai estar na parte 2 aqui embaixo, beleza?

[00:04:59–00:05:15] Formas de adicionar, você pode fazer isso manualmente, você pode fazer isso usando uma integração de parceiro que o próprio Facebook fornece para você na hora da configuração do pixel, ou você pode também enviar as instruções de instalação para o seu programador, tá?

[00:05:15–00:05:25] Ou seja, lá no gerenciador de eventos, no Facebook, a gente vai ver aqui depois, existem essas três formas de você adicionar, tá?

[00:05:25–00:05:34] Manual, usar uma integração que tem lá pronta, que daí é automático, com alguns cliques, por exemplo, você consegue colocar o seu pixel, tá?

[00:05:35–00:05:38] E, ou, né, enviar as instruções para o seu programador.

[00:05:38–00:06:07] É importante o seguinte, o pixel precisa estar em todas as suas páginas, todas, desde a home até a página de finalização, tem que estar em todas as páginas, o pixel é instalado no seu domínio inteiro, legal?

[00:06:08–00:06:29] Agora, vou falar um pouco sobre API de conversões, que justamente é algo do Facebook, isso aqui já existe há um tempo, só que até eu não dava devida atenção, porque na minha visão isso não era necessário antes, mas, de novo, a gente precisa se adaptar à ferramenta.

[00:06:29–00:06:36] Então, na metade do ano de 2020, a Apple lançou essa parada aí do iOS 14,

[00:06:36–00:06:39] das políticas de privacidade que protegem o usuário.

[00:06:39–00:06:44] Você não consegue hoje, por exemplo, fazer anúncios tão personalizados como antes,

[00:06:45–00:06:53] porque os usuários de iOS 14 para cima, eles têm a opção de querer ser rastreado ou não

[00:06:53–00:06:55] por esses aplicativos de Instagram, Facebook,

[00:06:55–00:06:59] ou até quando você for instalar qualquer aplicativo no seu celular,

[00:07:00–00:07:03] isso é uma regra, uma lei da Apple, né?

[00:07:03–00:07:06] Que, por exemplo, assim, ah, baixei um aplicativo de conversa.

[00:07:06–00:07:09] Quando você baixar um aplicativo de conversa, assim que você abrir,

[00:07:09–00:07:11] vai aparecer um pop-up na tela do seu celular,

[00:07:11–00:07:15] perguntando se você permite o rastreio desse aplicativo ou não, tá?

[00:07:16–00:07:18] E depois também a gente vai ver todas as diferenças,

[00:07:18–00:07:21] se você aceita, o que acontece com você ou com o seu usuário,

[00:07:21–00:07:23] e se você também não aceita, tá?

[00:07:23–00:07:48] API de conversão, características principais, deve ser instalado no servidor do seu site, tá, envia parâmetros da web diretamente do seu servidor para o Facebook utilizando uma API, precisa ser instalada apenas uma única vez, olha só a diferença do pixel para o API, tá, aqui você tem a mesma página, que eu desenhei aqui em cima,

[00:07:48–00:07:53] A mesma página, o mesmo botão, tudo igualzinho.

[00:07:54–00:08:02] E aqui, de novo, os usuários que estão sendo atingidos pelo seu anúncio.

[00:08:03–00:08:07] Aqui você tem o servidor do Facebook.

[00:08:09–00:08:14] E aqui você tem o seu servidor próprio do seu site.

[00:08:14–00:08:17] Seu servidor próprio

[00:08:17–00:08:18] Servidor, vou botar aqui

[00:08:18–00:08:21] Servidor, tá?

[00:08:21–00:08:23] Então, servidor do Facebook

[00:08:23–00:08:25] E seu servidor próprio

[00:08:25–00:08:26] Olha só que legal

[00:08:26–00:08:30] Os usuários, eles estão entrando na sua página

[00:08:30–00:08:31] Entrando na sua página

[00:08:31–00:08:33] Entrando na sua página

[00:08:33–00:08:34] Só que, opa

[00:08:34–00:08:36] Um desses usuários aqui

[00:08:36–00:08:38] Utiliza

[00:08:38–00:08:41] O iOS 14

[00:08:41–00:08:43] O que que acontece, tá?

[00:08:43–00:08:48] O que que acontece? Qual é a principal função dessa API aqui?

[00:08:49–00:08:54] Se esse cara do S14 clicou em não permitir o rastreio, o que que vai acontecer?

[00:08:55–00:09:00] Ele vai ser rastreado da mesma forma, só que pelo seu servidor, certo?

[00:09:01–00:09:04] Pelo seu servidor, beleza? E não direto pelo Facebook.

[00:09:04–00:09:09] Vocês estão conseguindo entender a diferença? Sim? Sim? Então, beleza.

[00:09:09–00:09:16] Quando o usuário cai no seu servidor, o seu servidor manda os dados para o Facebook

[00:09:16–00:09:20] Que é o contrário daqui de cima

[00:09:20–00:09:26] Aqui de cima o usuário entra e cai direto no servidor do Facebook, certo?

[00:09:27–00:09:31] No caso da API de conversão, que ela precisa ser instalada apenas uma única vez também

[00:09:31–00:09:34] O cara que tem o S14 está sendo rastreado

[00:09:34–00:09:37] Na verdade é assim, não só do S14, tá?

[00:09:37–00:09:51] mas todos esses usuários aqui, eles estão caindo tudo no seu servidor, todos no seu servidor, e os usuários que não são de OS14, eles caem direto no Facebook, por quê?

[00:09:52–00:09:59] Porque eu tenho a minha API instalada e o meu Pixel instalado, então você precisa ter os dois.

[00:09:59–00:10:01] Lucas, eu vou deixar só a API

[00:10:01–00:10:03] Tem os dois

[00:10:03–00:10:05] Formas de adicionar, você pode adicionar manualmente

[00:10:05–00:10:08] Usando uma integração de parceiro também

[00:10:08–00:10:09] Lá direto do próprio Facebook

[00:10:09–00:10:14] E você vai ver também outras formas de adicionar na aula prática

[00:10:14–00:10:17] Que deve existir aí já

[00:10:17–00:10:19] E o El já está ligado e você já está ligado

[00:10:19–00:10:20] Que o El é o cara das programações aí

[00:10:20–00:10:23] E ele vai resolver essa parada aí pra gente, beleza?

[00:10:25–00:10:26] Eventos, eventos, eventos

[00:10:26–00:10:28] Características principais

[00:10:28–00:10:32] deve ser instalado em páginas específicas do seu site.

[00:10:32–00:10:36] Mensurações valiosas, precisa ser instalado apenas uma única vez

[00:10:36–00:10:40] e você também precisa ter no máximo oito eventos.

[00:10:40–00:10:42] Caraca, quanta regrinha, né?

[00:10:43–00:10:44] Quanta regrinha.

[00:10:44–00:10:47] Aqui ficou claro, pixel e API, ficou 100% claro.

[00:10:47–00:10:48] Então beleza.

[00:10:49–00:10:50] Então beleza.

[00:10:52–00:10:55] Os eventos personalizados é o seguinte, tá?

[00:10:55–00:10:58] Aqui você vai ter a sua página

[00:10:58–00:11:01] Sua página

[00:11:01–00:11:04] E aqui você vai ter

[00:11:04–00:11:06] Uma outra página

[00:11:06–00:11:08] E essa página aqui

[00:11:08–00:11:11] É uma página de obrigado

[00:11:11–00:11:14] Obrigado pelo que, Lucas?

[00:11:14–00:11:17] Pela compra, obrigado pelo cadastro

[00:11:17–00:11:18] Obrigado pelo contato

[00:11:18–00:11:20] Uma página final, né?

[00:11:20–00:11:22] E essa página final aqui

[00:11:22–00:11:24] Você precisa ter ela, né?

[00:11:24–00:11:25] O que que acontece?

[00:11:25–00:11:33] muitas pessoas, elas não, você tem o seu site, você tem um formulário lá para cadastro, por exemplo,

[00:11:33–00:11:38] só que nem você testou esse formulário de cadastro, você não sabe para onde o lead vai,

[00:11:38–00:11:44] você não sabe para onde o lead cai, se cai num CRM, CRM, para quem não sabe,

[00:11:44–00:11:53] é como se fosse um gerenciador de clientes, de uma empresa, enfim, o seu CRM, a sua carteira de clientes.

[00:11:53–00:11:55] Então aqui é o seguinte

[00:11:55–00:11:58] Você vai ter o seu site principal

[00:11:58–00:11:59] Onde você vende

[00:11:59–00:12:02] Onde você vende

[00:12:02–00:12:04] Onde você captura

[00:12:04–00:12:06] Onde você liga

[00:12:06–00:12:08] E depois vai ter a sua página de obrigado

[00:12:08–00:12:11] Então, de novo, aqui ó

[00:12:11–00:12:11] Os usuários

[00:12:11–00:12:14] Tudo querendo entrar no seu site

[00:12:14–00:12:15] Tudo querendo atacar você aqui

[00:12:15–00:12:19] Esses usuários vão cair no seu site

[00:12:19–00:12:23] A partir do momento que eles caem no seu site

[00:12:23–00:12:29] eles vão ser automaticamente atingidos pelo Pixel e pela API,

[00:12:29–00:12:31] que está instalado em todo o seu site.

[00:12:32–00:12:34] E aí, navegando ali, ele pega e decide assim,

[00:12:35–00:12:38] vou comprar desse cara, esse cara aí é interessante para mim,

[00:12:38–00:12:39] eu vou deixar o contato.

[00:12:40–00:12:43] Ele vai deixar o contato aqui e vai apertar no botão enviar dados.

[00:12:43–00:12:46] Enviou os dados de contato, por exemplo, de orçamento,

[00:12:47–00:12:49] e ele vai cair nessa página de obrigado aqui.

[00:12:50–00:12:52] Fulano, muito obrigado pelo seu cadastro, viu?

[00:12:52–00:12:54] mais ou menos umas 24 horas

[00:12:54–00:12:56] nossa equipe comercial, nosso time

[00:12:56–00:12:58] nós vamos entrar em contato, enfim

[00:12:58–00:13:00] a mensagem que você quiser passar para o cara

[00:13:00–00:13:03] nessa página de obrigado aqui

[00:13:03–00:13:05] vai ter um evento

[00:13:05–00:13:06] personalizado

[00:13:06–00:13:09] de lead, compra

[00:13:09–00:13:11] registro concluído

[00:13:11–00:13:13] ou o que você quiser mensurar

[00:13:13–00:13:15] então eventos

[00:13:15–00:13:17] personalizados é para você mensurar ações

[00:13:17–00:13:19] valiosas, compra, cliques em

[00:13:19–00:13:21] botões, aquela coisa

[00:13:21–00:13:26] toda, enfim, o que você quiser mensurar de forma específica, tá?

[00:13:26–00:13:33] E aí é o seguinte, com essas novas regras, né, com essa lei aí do S14 implementada

[00:13:33–00:13:39] pela Apple, hoje o Facebook permite que você tenha apenas oito eventos, tá?

[00:13:39–00:13:43] Eu não tenho aqui no meu slide, mas eu vou mostrar aqui pra vocês que existem dois tipos

[00:13:43–00:13:52] de eventos, tá? Existem os eventos padrão, padrões, né? Mas eu vou escrever aqui padrão

[00:13:52–00:14:02] e existem os eventos personalizados. Palavra grande, né? Personalizados. Lucas, quais

[00:14:02–00:14:08] são os eventos padrões? Depois eu vou exemplificar ali na prática, mas os eventos padrões

[00:14:08–00:14:10] já são eventos prontos pelo Facebook, tá?

[00:14:11–00:14:16] Que são lead, purchase, que é no caso de compra, né?

[00:14:17–00:14:21] Que lá vai ser em inglês, vai ter adição ao carrinho

[00:14:21–00:14:25] e vai ter lá mais uma série de eventos padrões que eu vou mostrar ali, tá?

[00:14:26–00:14:31] E os eventos personalizados são eventos que você pode personalizar o nome, por exemplo.

[00:14:32–00:14:36] Eu quero um evento personalizado de um clique num botão de WhatsApp.

[00:14:36–00:14:43] Você vai pegar e vai escrever, botão Watts, por exemplo.

[00:14:44–00:14:46] Então tem esses dois tipos de evento.

[00:14:47–00:14:54] Lembrando, você vai aprender como você instala eventos padrões e como você instala os eventos personalizados.

[00:14:55–00:15:01] E aí uma coisa é muito importante, existe algo lá dentro do seu gerenciador de negócios,

[00:15:01–00:15:04] seu gerenciador de eventos, chamado mensuração de eventos agregados.

[00:15:04–00:15:09] Você não pode ter mais do que oito eventos instalados no seu site, tá?

[00:15:09–00:15:12] Isso não é possível.

[00:15:12–00:15:13] Lucas, mas eu tenho um nono aqui.

[00:15:14–00:15:15] Esquece, tá?

[00:15:15–00:15:18] Oito eventos é o máximo permitido pelo Facebook

[00:15:18–00:15:24] para cumprir aí as regras de privacidade dos usuários da Apple, tá?

[00:15:24–00:15:25] E eu vou falar com toda certeza.

[00:15:26–00:15:28] Oito eventos, bastante evento, tá?

[00:15:28–00:15:32] Principalmente no caso aí de quem usa mais de três, quatro eventos.

[00:15:32–00:15:34] Acredito que é apenas e-commerce, né?

[00:15:34–00:15:40] Então, dificilmente você vai precisar de mais de oito eventos padrões ou personalizados, tá?

[00:15:41–00:15:44] E aqui eu até botei como que é o código desse evento, né?

[00:15:44–00:15:52] Tudo que for relacionado a pixel, evento e domínio, é meio que fala uma linguagem aí de programação, né?

[00:15:52–00:15:55] Mas é bem simples, ó, eu separei aqui pra você.

[00:15:55–00:15:59] Onde os seus eventos devem ser instalados, né?

[00:15:59–00:16:06] Pode ver, ó, aqui tem uma palavra HEAD e aqui tem uma palavra HEAD com fechamento, né?

[00:16:06–00:16:10] Então ele tem que estar instalado dentro aqui do corpo do seu site, tá?

[00:16:10–00:16:15] Dentro do cabeçalho, né? Aliás, do seu site, tá bom?

[00:16:16–00:16:20] Aqui, esse número 2 é a parte do pixel, ó, parte do pixel, tá?

[00:16:21–00:16:28] E o número 3, que tá aqui, ó, pequenininho, ó, ele é o meu evento personalizado, tá?

[00:16:28–00:16:32] Aqui, no caso, é um evento padrão de adição ao carrinho, tá?

[00:16:33–00:16:36] Um evento padrão do Facebook, beleza?

[00:16:37–00:16:43] Então, de novo, aqui é o início do código, aqui é o fim do código.

[00:16:44–00:16:48] E dentro desse código aqui, eu tenho, por exemplo, na minha página de obrigado, né?

[00:16:49–00:16:54] Ou na minha página, enfim, independente da página que você queira mensurar alguma ação valiosa,

[00:16:54–00:17:00] você vai ter o seu evento personalizado aqui, representado pelo número 3, legal?

[00:17:03–00:17:11] Domínios, verificação de domínio, características principais, segurança da sua marca, obrigatório após as políticas do ES14,

[00:17:11–00:17:21] você precisa fazer apenas uma vez, tá? E aí você precisa também ter no máximo 8 eventos por domínio, tá?

[00:17:21–00:17:43] A parte do domínio é a seguinte, a parte do domínio é a seguinte, você tem o seu site, www, e aqui você tem o seu gerenciador do Facebook, tá?

[00:17:43–00:17:51] Aqui dentro do Facebook, você vai pegar o seu domínio e vai adicioná-lo aqui dentro.

[00:17:52–00:17:52] Eu já vou te mostrar onde.

[00:17:53–00:17:56] Você vai botar o seu www aqui. Por quê?

[00:17:56–00:17:58] Para provar que você é o dono desse site.

[00:17:59–00:18:04] Para você provar para o Facebook que você tem todos os acessos possíveis ao seu site.

[00:18:05–00:18:10] Colocando aqui, vai ser gerado um código e você vai ter que instalar no seu site também, tá?

[00:18:10–00:18:14] E aí, a gente vai ver aqui na parte de número 2 como faz toda a instalação.

[00:18:14–00:18:19] Lembrando, isso aqui é só aula teórica para você entender o que acontece com esses elementos, tá?

[00:18:20–00:18:23] Fazendo a instalação, vai estar verificado.

[00:18:23–00:18:31] O seu domínio, de novo, não pode passar de 8 eventos personalizados ou 8 eventos padrões, tá?

[00:18:32–00:18:37] E a partir do momento que você colocar um domínio dentro de um gerenciador,

[00:18:37–00:18:41] você não consegue anunciar esse domínio em outro gerenciador.

[00:18:41–00:18:46] Então, o caso, por exemplo, de agências, né?

[00:18:46–00:18:49] Agências ou pessoas que cuidam demais de um cliente.

[00:18:50–00:18:54] Você vai ter o gerenciador do seu cliente com o domínio verificado, beleza?

[00:18:54–00:18:58] Ah, Lucas, o cliente contratou, não fechou mais a parceria comigo,

[00:18:58–00:19:00] contratou uma outra agência e a outra agência quer anunciar.

[00:19:00–00:19:01] O que eu faço?

[00:19:01–00:19:03] Olha só a importância da organização, né?

[00:19:03–00:19:05] Desde lá do início eu falei.

[00:19:05–00:19:32] Se você tiver um gerenciador para cada cliente seu, vai ser muito mais fácil, você vai trabalhar de forma muito mais organizada, porque se você quiser tirar esse domínio daqui e passar, por exemplo, para o gerenciador do Lucas, você vai ter que ir lá, vai ter que remover, vai ter que remover o script de instalação da verificação do domínio, e aí começa a ficar uma bola de neve, e aí você começa a encher o campo de comentário de dúvida, e aí fica difícil para você entender e dar sequência, tá?

[00:19:33–00:19:39] Então, essa parte de verificação de domínio que eu queria falar é isso, tá?

[00:19:39–00:19:42] E lá no seu gerenciador, né, que a gente criou já o gerenciador,

[00:19:43–00:19:45] para quem não tem, quem já tem também está ok,

[00:19:46–00:19:49] vai ter essa opção aqui, ó, segurança de marca e domínio, tá?

[00:19:49–00:19:52] E de novo, na aula técnica, na parte 2,

[00:19:53–00:19:55] a gente vai mostrar exatamente o caminho para você chegar

[00:19:55–00:19:59] até aqui na verificação de domínio e também para fazer a instalação do script lá,

[00:19:59–00:20:01] que ele vai mandar você instalar

[00:20:01–00:20:03] para verificar o seu domínio. Resumo

[00:20:03–00:20:05] Pixel, instale em todo o seu

[00:20:05–00:20:07] site uma única vez, envia

[00:20:07–00:20:09] parâmetros da web direto para os

[00:20:09–00:20:11] servidores do Facebook. API

[00:20:11–00:20:13] instale em todo o seu site

[00:20:13–00:20:15] também e envia parâmetros

[00:20:15–00:20:17] diretamente do seu servidor

[00:20:17–00:20:19] para os servidores do Facebook

[00:20:19–00:20:21] Eventos, mensurações valiosas

[00:20:21–00:20:23] compra o lead e deve ser instalado

[00:20:23–00:20:25] em páginas específicas, tá?

[00:20:25–00:20:27] E o domínio, instale uma única

[00:20:27–00:20:28] vez

[00:20:28–00:20:32] verifique uma única vez, né, para proteger sua marca

[00:20:32–00:20:35] e garantir também que ninguém utilize esse domínio.

[00:20:35–00:20:37] Cara, esse domínio aqui, a verificação desse domínio é algo genial

[00:20:37–00:20:42] porque ninguém pode fazer nada contra você, assim.

[00:20:42–00:20:46] Por exemplo, você tem um site www.exemplo.com

[00:20:46–00:20:49] já verificado no seu gerenciador, você já anuncia nele

[00:20:49–00:20:53] e por um motivo qualquer, sei lá, comigo já aconteceu isso, tá?

[00:20:53–00:20:59] Uma vez eu estava anunciando para, tinha dois clientes, cliente A e o cliente B,

[00:20:59–00:21:02] era do mesmo nicho, só que eram em contas diferentes.

[00:21:03–00:21:08] Resumo da ópera, eu peguei o URL do cliente A e anunciei para o cliente B o mesmo domínio,

[00:21:08–00:21:10] ou seja, um concorrente estava anunciando para o outro,

[00:21:11–00:21:14] e hoje graças a essa verificação de domínio aqui,

[00:21:14–00:21:20] eu não consigo, e ninguém consegue, anunciar o mesmo domínio em outro gerenciador

[00:21:20–00:21:23] ou em outra conta de anúncio, então você não corre esse risco.

[00:21:24–00:21:30] E por isso que é muito importante você ter pixel, API, seus eventos de conversão,

[00:21:31–00:21:37] seu domínio verificado, tudo 100%, e eu acredito que na próxima aula

[00:21:37–00:21:42] nós vamos começar a falar mais de parte estratégica, de público,

[00:21:42–00:21:46] de criação de campanha, de otimização de campanha, então é isso,

[00:21:46–00:21:48] Revise essa aula novamente

[00:21:48–00:21:50] E assista a parte 1

[00:21:50–00:21:51] A parte 2 que vai estar aqui embaixo

[00:21:51–00:21:53] E a gente se vê no próximo vídeo

[00:21:53–00:21:59] A dúvida é sobre a questão dos eventos

[00:21:59–00:22:01] Tu falou muito sobre ter no máximo 8 eventos

[00:22:01–00:22:03] Mas uma dúvida que acontece é

[00:22:03–00:22:05] Eu posso criar mais do que 8 eventos

[00:22:05–00:22:06] E usar só 8?

[00:22:07–00:22:08] Ou 8 é o máximo que eu posso criar?

[00:22:09–00:22:10] Você pode criar mais de 8

[00:22:10–00:22:12] Você pode criar mais de 8

[00:22:12–00:22:14] Só que aí é o seguinte

[00:22:14–00:22:16] Você vai ter oito eventos aqui

[00:22:16–00:22:20] Um, dois, três, quatro

[00:22:20–00:22:20] E assim vai

[00:22:20–00:22:22] Cinco, seis, sete, oito

[00:22:22–00:22:24] Esses oito eventos aqui

[00:22:24–00:22:27] Eles são definidos por você

[00:22:27–00:22:32] Por ordem de prioridade, tá?

[00:22:32–00:22:36] Ou seja, qual evento é mais importante pra você?

[00:22:36–00:22:38] Provavelmente ou é um lead

[00:22:38–00:22:42] Ou é uma compra, tá?

[00:22:42–00:22:43] Ou é uma compra

[00:22:43–00:22:52] E aqui embaixo você coloca eventos secundários, visualização de página, clique de botão, enfim, o que você quiser mensurar, tá?

[00:22:53–00:23:05] Só que aqui, nesses eventos agregados, que surgiu depois das políticas do ES14, eu vou explicar isso lá na aula de boas práticas também, mas é o seguinte.

[00:23:06–00:23:11] Você lembra que eu falei que o usuário tem a opção de ser rastreado e não ser rastreado, né?

[00:23:11–00:23:21] Olha só que interessante, esse evento aqui, que é o seu principal, ele consegue rastrear o seu usuário com a API de conversão,

[00:23:21–00:23:27] mesmo ele falando para não ser rastreado, porque ele está caindo direto no seu servidor, tá?

[00:23:27–00:23:36] Então assim, você consegue até criar mais de 8 eventos, só que você não consegue adicionar mais de 8 eventos

[00:23:36–00:23:42] aqui na sua lista de mensuração de eventos agregados, tá?

[00:23:42–00:23:46] Então até você pode criar muito, enfim, quanto você quiser,

[00:23:47–00:23:49] mas o que vai ser mensurável é o que está aqui, tá?

[00:23:50–00:23:54] Se ele não achar nenhum evento de lead ou venda, que é o principal,

[00:23:54–00:23:57] ele vai para o 2, que é, por exemplo, adição ao carrinho.

[00:23:57–00:24:00] Se ele não achar o adição ao carrinho, ele vai para o de baixo,

[00:24:00–00:24:04] que é visualização de produto, tá?

[00:24:04–00:24:10] Uma coisa que pode acontecer é que às vezes o pessoal vai lá e instala o pixel

[00:24:10–00:24:14] e às vezes conta duplicado, ou até às vezes não conta.

[00:24:14–00:24:20] O que tu recomenda de ações que a gente pode ver para solucionar esse problema?

[00:24:21–00:24:27] Então, a primeira coisa de todas é você instalar uma única vez, certo?

[00:24:27–00:24:32] Tanto o pixel geral, que é o page view que vai ser em todo o seu site,

[00:24:32–00:24:35] quando os seus eventos, as suas conversões personalizadas.

[00:24:35–00:24:36] O que acontece?

[00:24:36–00:24:38] Se você está instalando de forma manual,

[00:24:39–00:24:42] você pode até instalar duas vezes por engano,

[00:24:42–00:24:46] mas, por exemplo, existe uma função que tem ali no gerenciador,

[00:24:46–00:24:47] a gente vai ver aqui na aula prática,

[00:24:48–00:24:51] que é a instalação utilizando o próprio Facebook ali.

[00:24:51–00:24:55] Você cai na sua página e o Facebook já identifica onde tem os botões,

[00:24:55–00:24:57] se você quiser instalar algum evento personalizado nos botões,

[00:24:58–00:25:01] ou até na própria página, você vai lá e bota, por exemplo, assim,

[00:25:01–00:25:05] ah, quero instalar com a ferramenta de instalação de eventos do Facebook.

[00:25:05–00:25:09] Ele vai abrir a sua página e ele vai te dar as opções lá de eventos, beleza?

[00:25:10–00:25:13] Então, por exemplo, você colocou o lead, tá, nessa forma de instalação.

[00:25:14–00:25:19] Você nem tem a opção de colocá-lo novamente porque, ah, não lembro se eu coloquei.

[00:25:19–00:25:22] Porque se tu abrir de novo essa página, vou mostrar aqui, tá,

[00:25:22–00:25:26] se você abrir de novo essa página, ele já vai acusar que você tem um evento personalizado ali,

[00:25:26–00:25:33] Ou seja, essa margem de duplicação, ela diminuiu bastante com essa ferramenta nova do Facebook, entendeu?

[00:25:33–00:25:35] Vou mostrar aqui na tela rapidamente.

[00:25:35–00:25:40] Por exemplo, aqui eu tenho um site, conversãoextrema.com.br, Telegram.

[00:25:40–00:25:43] É um site que eu envio pessoas aí para o Telegram, tá?

[00:25:44–00:25:52] Vou pegar essa URL aqui e eu vou colocar, por exemplo, em adicionar eventos do Pixel

[00:25:52–00:25:56] e, ó, abrir a ferramenta de configuração de eventos.

[00:25:56–00:25:59] De novo, tá gente, isso aqui a gente vai ver com detalhes na aula prática

[00:25:59–00:26:02] Aqui eu vou inserir a minha URL

[00:26:02–00:26:06] É a forma mais fácil de você instalar

[00:26:06–00:26:07] É usando essa forma aqui

[00:26:07–00:26:10] Pode ver que ele já abre uma caixa de ferramentas

[00:26:10–00:26:12] Ou seja, automaticamente

[00:26:12–00:26:13] Ele já identificou que eu tenho

[00:26:13–00:26:15] Um botão nessa página

[00:26:15–00:26:18] E eu já instalei um evento personalizado

[00:26:18–00:26:19] De registro concluído aqui nesse botão

[00:26:19–00:26:22] Tá vendo? Não sei se você tá vendo aí na tela

[00:26:22–00:26:24] Mas aqui no meu computador

[00:26:24–00:26:25] Tá aparecendo o botão

[00:26:25–00:26:30] Eu não consigo, por exemplo, fazer a instalação de outro registro concluído

[00:26:30–00:26:31] Porque já tem, tá?

[00:26:31–00:26:34] Com isso, evita erros de duplicação de evento

[00:26:34–00:26:36] Agora, se eu quiser rastrear, por exemplo, um novo botão

[00:26:36–00:26:39] Deixa eu ver se eu tenho outro botão

[00:26:39–00:26:43] Se eu quiser rastrear esses dois aqui, ele mesmo já identifica

[00:26:43–00:26:45] E ele mesmo fala aqui o seguinte

[00:26:45–00:26:47] Clique no botão em destaque para configurar seu evento

[00:26:47–00:26:50] Vamos supor que eu queira configurar aqui nesse aqui da Apple Store

[00:26:50–00:26:52] Ele vai pedir para eu selecionar um evento

[00:26:52–00:26:54] Eu vou selecionar um evento

[00:26:54–00:26:57] botar, por exemplo, sei lá, entrar em contato

[00:26:57–00:26:58] e vou botar

[00:26:58–00:26:59] confirmar

[00:26:59–00:27:03] você tem o evento personalizado

[00:27:03–00:27:05] no seu botão, certo?

[00:27:05–00:27:07] isso aqui eu passei rapidamente, tá?

[00:27:07–00:27:09] eu não vou salvar, porque

[00:27:09–00:27:11] não quero que atrapalhe

[00:27:11–00:27:13] aqui, né? não vou misturar, enfim

[00:27:13–00:27:15] e aí depois se você terminar, você vem aqui

[00:27:15–00:27:17] e clica em terminar configuração

[00:27:17–00:27:19] dá um feedback aqui pros caras, deixa os meninos

[00:27:19–00:27:21] felizes e clica em

[00:27:21–00:27:23] enviar, tá? então é isso

[00:27:23–00:27:24] Tchau.

## Parte 2 — m9_a6_p2_pixel_eventos_e_dominios.mp4

Origem: https://drive.google.com/drive/folders/1IscwBtiyGPNNtEAq6NV2CWASDx-7SGSB?hl=pt-br
SHA-256: `4a6f8ecc3a913dd5a237b3bc282a58022a760b81da26c3a415e7fdfbbffdcf0f`. Duração: 00:07:58.167.

[00:00:00–00:00:05] Fala aí gente, tudo bem com vocês? Bom, vamos entrar agora na parte de Facebook.

[00:00:06–00:00:09] E antes de a gente falar sobre instalação de Pixel, instalação de API, enfim,

[00:00:10–00:00:13] a gente tem um passo anterior que a gente precisa realizar, que é a verificação de domínio.

[00:00:14–00:00:18] Então dentro do seu gerenciador de negócios, você vai ter que vir aqui em configurações do negócio,

[00:00:19–00:00:23] e você vai ter que provar para o Facebook que você é dono do seu domínio.

[00:00:23–00:00:27] Então, segurança da marca, domínios, você vai ter que clicar aqui em adicionar,

[00:00:27–00:00:29] para adicionar um novo domínio aqui.

[00:00:30–00:00:32] No caso, o domínio do seu site.

[00:00:32–00:00:35] Então, eu vou colocar um domínio meu aqui e vou clicar em adicionar.

[00:00:36–00:00:40] Quando eu clicar em adicionar, ele vai me dar três opções de verificação desse domínio.

[00:00:41–00:00:45] Basicamente, três maneiras de eu provar para o Facebook que esse site é meu.

[00:00:46–00:00:49] Você só precisa selecionar uma dessas opções.

[00:00:49–00:00:51] Então, clicando aqui, eu tenho três opções.

[00:00:51–00:00:56] Eu tenho a opção de colocar uma meta tag no HTML do meu site.

[00:00:56–00:01:00] Tem a opção de subir um HTML, um arquivo, na raiz do meu site.

[00:01:00–00:01:05] E tem a opção de atualizar o registro TXT do DNS domínio, tá?

[00:01:05–00:01:08] Parece complicado, mas eu já vou mostrar as três maneiras pra vocês, tá?

[00:01:08–00:01:10] Eu vou mostrar as três formas aqui pra vocês.

[00:01:10–00:01:15] Depois vocês escolham aquela que mais fizer sentido pra você,

[00:01:15–00:01:17] que você achar mais fácil, que você tiver acesso, enfim.

[00:01:17–00:01:19] Qualquer uma das três funciona, tá?

[00:01:19–00:01:20] Então, vamos começar com a primeira aqui.

[00:01:21–00:01:24] Adicione uma metatag ao seu código fonte HTML.

[00:01:25–00:01:26] Metatag é isso aqui, ó.

[00:01:26–00:01:28] Então, se eu clicar aqui, ele vai copiar.

[00:01:28–00:01:33] E ele pede para eu adicionar essa metatag no head do meu site

[00:01:33–00:01:34] No cabeçalho do meu site

[00:01:34–00:01:37] Então, no meu caso aqui eu uso o WordPress e uso o Elementor

[00:01:37–00:01:40] Para quem usa o Elementor, vai ter a parte aqui de custom code

[00:01:40–00:01:42] Basta adicionar novo

[00:01:42–00:01:45] E aqui vamos botar aqui, Facebook verificação

[00:01:45–00:01:46] Qualquer nome que quiser

[00:01:46–00:01:52] No head, que ele disse para adicionar no head mesmo

[00:01:52–00:01:55] Colou o código aqui, publicou

[00:01:55–00:01:57] Em todo o site

[00:01:57–00:01:59] Tá feito, tá

[00:01:59–00:02:00] E aí se eu clicar em verificar aqui

[00:02:00–00:02:02] Já vai verificar o domínio

[00:02:02–00:02:04] Não vou clicar em verificar porque eu ainda quero mostrar mais

[00:02:04–00:02:06] Mais opções pra vocês, mas

[00:02:06–00:02:09] Já serviria dessa maneira, tá

[00:02:09–00:02:10] Se você tiver como fazer assim

[00:02:10–00:02:12] Ainda no WordPress

[00:02:12–00:02:15] Eu poderia usar algum outro plugin

[00:02:15–00:02:17] Ou poderia vir, por exemplo

[00:02:17–00:02:18] Na parte de aparência, editor de temas

[00:02:18–00:02:21] Que eu também consigo ter acesso ao código aqui

[00:02:21–00:02:22] Então se eu vir no cabeçalho do tema

[00:02:22–00:02:24] Achar o head aqui, ó, dar um enter

[00:02:24–00:02:25] E colar

[00:02:25–00:02:28] Aqui também funcionaria

[00:02:28–00:02:30] Estou fazendo a mesma coisa que eu fiz anteriormente

[00:02:30–00:02:32] Só que aqui mexendo direto no código

[00:02:32–00:02:34] Então se você tem acesso ao código do seu site

[00:02:34–00:02:36] Ao HTML do seu site de alguma maneira

[00:02:36–00:02:38] Sendo de maneira direta ou por plugin

[00:02:38–00:02:39] Basta você encontrar a tag red

[00:02:39–00:02:41] Dar um enter depois dela

[00:02:41–00:02:43] E colar esse código de verificação

[00:02:43–00:02:46] E aí já vai funcionar a verificação

[00:02:46–00:02:48] Então essa é a primeira forma de fazer

[00:02:48–00:02:50] Colocando essa meta tag

[00:02:50–00:02:52] No red, no cabeçalho do seu site

[00:02:52–00:02:57] A segunda maneira

[00:02:57–00:02:59] Carregue um arquivo HTML no diretório raiz

[00:02:59–00:03:00] Isso aqui é o seguinte

[00:03:00–00:03:03] Isso aqui você vai ter que ter acesso a hospedagem no seu site

[00:03:03–00:03:05] Então se você usa Kinghost

[00:03:05–00:03:07] Se você usa LocalWeb

[00:03:07–00:03:09] Se você usa HostGator

[00:03:09–00:03:11] Enfim, qualquer hospedagem

[00:03:11–00:03:13] Que vai te dar um painel

[00:03:13–00:03:13] Como esse aqui

[00:03:13–00:03:17] Um cpn, um painel onde vai ter um gerenciador de arquivos

[00:03:17–00:03:19] Funciona

[00:03:19–00:03:21] E aí essa segunda opção aqui

[00:03:21–00:03:21] É bem válida

[00:03:21–00:03:24] O que consiste nessa segunda opção?

[00:03:25–00:03:27] Ele te dá um código HTML, tá vendo?

[00:03:27–00:03:28] Que você baixa.

[00:03:28–00:03:33] E aí ele pede para você colocar esse código lá nos arquivos do seu site.

[00:03:33–00:03:37] Então, se eu vim no cPanel aqui, que é um painel bem padrão de quem tem site,

[00:03:37–00:03:38] e vim no gerenciador de arquivos,

[00:03:40–00:03:42] todo o meu site, a raiz é a pasta pública HTML.

[00:03:43–00:03:46] Então, abre essa pasta e aqui estão todos os arquivos do meu site.

[00:03:46–00:03:49] Essa forma de verificação consiste, né?

[00:03:49–00:03:50] Deixa eu fechar outra página aí.

[00:03:50–00:03:54] E justamente você pegar esse arquivo e colar na raiz do seu site.

[00:03:54–00:03:59] Para basicamente falar para o seu Facebook assim, olha, se eu consigo botar um arquivo na raiz do meu site,

[00:03:59–00:04:02] é porque eu sou dono do meu site, porque só eu tenho acesso para isso.

[00:04:02–00:04:07] Então, basicamente, é você carregar, pegar o arquivo que você baixou e enviar para a raiz do seu site.

[00:04:08–00:04:11] E aí, está feito, tá?

[00:04:11–00:04:13] Então, essa é a segunda maneira de verificação.

[00:04:14–00:04:17] Caso a primeira não tenha dado certo, você não consiga, tem essa segunda aqui,

[00:04:17–00:04:20] Mas que você precisa ter acesso aos arquivos do seu site

[00:04:20–00:04:23] E por último

[00:04:23–00:04:24] Nós temos uma terceira

[00:04:24–00:04:25] Um método de verificação

[00:04:25–00:04:28] Então se você não tem acesso

[00:04:28–00:04:29] A raiz do seu site

[00:04:29–00:04:32] Se você não tem acesso ao reader

[00:04:32–00:04:33] Para colocar ao head

[00:04:33–00:04:35] Para colocar a meta tag

[00:04:35–00:04:37] Só te sobra essa última opção

[00:04:37–00:04:40] Que é mexendo nos registros de DNS do seu site

[00:04:40–00:04:40] Então é o seguinte

[00:04:40–00:04:44] A maioria das plataformas

[00:04:44–00:04:46] Onde você compra um domínio

[00:04:46–00:04:48] Ela tem a opção aqui de você mudar

[00:04:48–00:04:49] Os DNS

[00:04:49–00:04:51] Os registros de DNS

[00:04:51–00:04:54] Eu como eu uso o Cloudflare, no meu fica tudo dentro do Cloudflare

[00:04:54–00:04:57] Então aqui, o que o Facebook pede?

[00:04:57–00:04:59] Para você ir na plataforma onde está o seu domínio

[00:04:59–00:05:01] Seu domínio está apontado

[00:05:01–00:05:03] E para você criar um registro

[00:05:03–00:05:04] TXT de DNS

[00:05:04–00:05:07] E colar essas informações aqui

[00:05:07–00:05:08] Facebook, Domain, Verification

[00:05:08–00:05:11] E aqui ele diz também

[00:05:11–00:05:13] Que alguns registradores de domínio exigem um símbolo

[00:05:13–00:05:15] Arroba no campo de host, que é o campo de nome

[00:05:15–00:05:17] Então aqui ó, eu adicionaria um novo

[00:05:17–00:05:18] Registro, no tipo

[00:05:18–00:05:19] TXT

[00:05:19–00:05:24] Aqui, eu usaria

[00:05:24–00:05:27] O arroba, né, que ele lembra

[00:05:27–00:05:29] Que ele falou aqui ó, use arroba

[00:05:29–00:05:31] No campo de host, e aqui no conteúdo eu colocaria

[00:05:31–00:05:33] Essa parte, esse código

[00:05:33–00:05:34] De verificação e salvaria

[00:05:34–00:05:36] Funcionaria perfeitamente também, tá?

[00:05:36–00:05:39] Como eu já fiz, botei nos outros, eu não vou fazer novamente

[00:05:39–00:05:40] Aqui, mas é assim que se faz, tá?

[00:05:41–00:05:43] É, ué, mas eu não uso o Cloudflare

[00:05:43–00:05:44] Né, ó, na local web também tem

[00:05:44–00:05:48] Então, na local web deve ter a parte de zona de DNS

[00:05:48–00:05:50] E a servidora de DNS

[00:05:50–00:05:51] Então, aqui

[00:05:51–00:05:54] Em alguns lugares você também vai conseguir

[00:05:54–00:05:55] Alterar isso, tá?

[00:05:56–00:05:58] No registro BR também

[00:05:58–00:05:59] Se o seu site tiver

[00:05:59–00:06:01] Com DNS no registro BR

[00:06:01–00:06:04] Às vezes você consegue editar todas as zonas

[00:06:04–00:06:05] Daí você vai clicar em nova entrada

[00:06:05–00:06:07] Vai ter lá a entrada do tipo TXT

[00:06:07–00:06:09] Funciona também

[00:06:09–00:06:12] Dentro da HostGator

[00:06:12–00:06:13] Também tem aqui o editar zonas de DNS

[00:06:13–00:06:16] Dentro da parte de domínio

[00:06:16–00:06:18] E aqui no gerenciário eu consigo

[00:06:18–00:06:20] Adicionar vários registros

[00:06:20–00:06:22] Por exemplo, registro do tipo

[00:06:22–00:06:23] TXT também

[00:06:23–00:06:25] E aqui o nome eu botaria

[00:06:25–00:06:26] Domínio

[00:06:26–00:06:31] Então

[00:06:31–00:06:36] Praticamente toda plataforma de

[00:06:36–00:06:37] Compra de domínio vai te dar essa opção

[00:06:37–00:06:40] Vai ficar no local diferente

[00:06:40–00:06:42] Mas existe essa possibilidade

[00:06:42–00:06:45] E aí, feito uma dessas três

[00:06:45–00:06:47] Formas aqui de verificação

[00:06:47–00:06:49] Você só precisa de uma delas

[00:06:49–00:06:51] Eu mostrei as três porque eu mostrei as possibilidades

[00:06:51–00:06:53] Mas você só precisa de uma única

[00:06:53–00:06:54] Delas

[00:06:54–00:06:56] Feito isso, você vai clicar em verificar domínio

[00:06:56–00:06:59] E aí, no meu caso aqui aconteceu de maneira

[00:06:59–00:07:01] Bem instantânea e foi verificado

[00:07:01–00:07:02] Caso não aconteça com você

[00:07:02–00:07:05] Pode ser porque demore, dependendo da maneira de verificação

[00:07:05–00:07:06] Pode demorar um pouco

[00:07:06–00:07:08] Principalmente essa parte de DNS

[00:07:08–00:07:12] Porque pode levar até 72 horas

[00:07:12–00:07:14] Agora, quando é tag HTML

[00:07:14–00:07:15] Geralmente é instantâneo

[00:07:15–00:07:16] Então, depende

[00:07:16–00:07:19] Às vezes pode ser pelo tempo

[00:07:19–00:07:21] Que ainda não propagou

[00:07:21–00:07:24] E às vezes pode ser porque você fez a verificação errada

[00:07:24–00:07:26] Então assim, se não der certo

[00:07:26–00:07:27] Verifique o passo a passo

[00:07:27–00:07:28] Tente de outra maneira

[00:07:28–00:07:32] E mesmo assim não der, espere até 72 horas

[00:07:32–00:07:33] Para ver se a verificação acontece

[00:07:33–00:07:36] Se ainda assim não acontecer, é porque você errou em alguma parte

[00:07:36–00:07:37] Da verificação

[00:07:37–00:07:39] E aí você vai ter que ver onde você errou

[00:07:39–00:07:40] Para ajustar

[00:07:40–00:07:46] Mas em resumo, verificação de domínio é esse o passo a passo e essas são as três maneiras de você verificar um domínio.

[00:07:47–00:07:53] Depois de verificar um domínio, a gente vai partir lá para a parte de instalação de pixel e de API de conversões do Facebook.

## Parte 3 — m9_a6_p3_pixel_eventos_e_dominios.mp4

Origem: https://drive.google.com/drive/folders/1IscwBtiyGPNNtEAq6NV2CWASDx-7SGSB?hl=pt-br
SHA-256: `a8945705e52b60094ca063d199f13fb920cbf62dfa52663b2ec46bccf4d86746`. Duração: 00:04:12.300.

[00:00:00–00:00:07] Falei gente, vamos então para a aula de instalar Pixel e AP de conversões.

[00:00:08–00:00:14] Inicialmente eu quero falar para vocês da diferença entre as duas coisas, para que vocês entendam se vocês precisam, se não precisam e tudo mais.

[00:00:14–00:00:19] Mas basicamente, tanto o Pixel quanto a AP de conversões, elas têm aí o mesmo objetivo.

[00:00:19–00:00:25] O objetivo de ambos é informar ao Facebook as coisas que usuários fazem no seu site.

[00:00:25–00:00:27] Tanto a visita da página

[00:00:27–00:00:30] Ou comprou, ou adicionou o produto ao carrinho

[00:00:30–00:00:31] Enfim, para que vocês tenham os dados

[00:00:31–00:00:32] Nas campanhas aí

[00:00:32–00:00:36] Para que vocês consigam otimizar, criar públicos e tudo mais

[00:00:36–00:00:37] Então

[00:00:37–00:00:40] Basicamente a diferença do pixel e da page de conversões

[00:00:40–00:00:42] É que uma funciona pelo navegador

[00:00:42–00:00:43] O pixel funciona pelo navegador

[00:00:43–00:00:45] A page de conversões funciona pelo servidor

[00:00:45–00:00:46] Então o seguinte

[00:00:46–00:00:49] Recentemente a Apple colocou lá os seus aplicativos

[00:00:49–00:00:51] Relacionados ao Facebook, a opção do usuário

[00:00:51–00:00:53] Não compartilhar dados com o Facebook

[00:00:53–00:01:02] Isso fez com que muitos usuários que usam o navegador do Facebook, enfim, não compartilhem dados de compra de sites ou coisas com o Facebook.

[00:01:02–00:01:09] Isso faz com que os eventos na sua campanha, eles diminuam em quantidade, drasticamente, né?

[00:01:09–00:01:13] Isso acaba prejudicando aí na hora de você criar um público para remarketing ou coisas do tipo.

[00:01:14–00:01:18] A solução que eles deram foi instalar a API de conversões, que aí como ela não usa o navegador, né?

[00:01:18–00:01:20] Basicamente a pessoa realizou uma compra no seu site.

[00:01:20–00:01:22] Se o site sabe que a pessoa realizou a compra

[00:01:22–00:01:24] Ela informa o Facebook

[00:01:24–00:01:26] Que a compra foi realizada

[00:01:26–00:01:29] Mesmo sem que o usuário compartilhe os dados do navegador

[00:01:29–00:01:31] Porque isso acontece lá mais embaixo

[00:01:31–00:01:32] Lá pelo servidor

[00:01:32–00:01:34] E aí acaba recuperando aí

[00:01:34–00:01:36] Alguns eventos interessantes

[00:01:36–00:01:38] Que você perderia se tivesse só o Pixel

[00:01:38–00:01:40] Aqui em ver conteúdo

[00:01:40–00:01:41] Eu quero mostrar para vocês um exemplo

[00:01:41–00:01:45] Eu tenho um evento de ver conteúdo

[00:01:45–00:01:47] Que é de todo mundo que acessa a página de produto de um e-commerce

[00:01:47–00:01:49] E aqui mostra para mim

[00:01:49–00:01:51] Que nos últimos 28 dias

[00:01:51–00:01:53] No navegador, o pixel do navegador

[00:01:53–00:01:55] Verificou que 1204 pessoas

[00:01:55–00:01:57] Acessaram a página de produto

[00:01:57–00:01:59] E a API de conversões

[00:01:59–00:02:01] Verificou que 1947 pessoas acessaram a página de produto

[00:02:01–00:02:02] Então aqui eu tenho

[00:02:02–00:02:05] 700 pessoas a mais do que aqui

[00:02:05–00:02:07] Isso significa que se eu não tivesse

[00:02:07–00:02:08] A API de conversões instaladas

[00:02:08–00:02:11] Mais de 30% dos eventos

[00:02:11–00:02:12] Que acontecem no meu site

[00:02:12–00:02:15] Eu não teria dados aqui na campanha do Facebook

[00:02:15–00:02:17] Então por isso que a API de conversões

[00:02:17–00:02:18] É muito importante

[00:02:18–00:02:20] Porque ela te dá um número muito mais próximo do real

[00:02:20–00:02:22] Do que realmente acontece

[00:02:22–00:02:25] De pessoas que visitaram o seu site, que compraram um produto

[00:02:25–00:02:25] Ou coisas do tipo

[00:02:25–00:02:28] Só que isso não é igual para todo tipo de negócio

[00:02:28–00:02:31] Alguns tipos de negócio, dependendo do público

[00:02:31–00:02:32] Por exemplo, aqui eu estou pegando

[00:02:32–00:02:35] Um público que usa muito iPhone

[00:02:35–00:02:37] Então essa divergência é bem grande

[00:02:37–00:02:39] Mas se eu pego do conversão extrema, por exemplo

[00:02:39–00:02:41] Aqui a diferença é mínima

[00:02:41–00:02:42] É menos de 2%

[00:02:42–00:02:44] Enquanto nesse aqui dá mais de 30%

[00:02:44–00:02:47] Então em alguns negócios, tipos de negócios

[00:02:47–00:02:50] A P de conversões não vai fazer tanta diferença assim

[00:02:50–00:02:53] Quanto nesse exemplo que eu estou dando para vocês

[00:02:53–00:02:56] Então assim, a P de conversões é obrigatória?

[00:02:56–00:02:58] É recomendada, mas não é obrigatória

[00:02:58–00:02:59] Por quê?

[00:02:59–00:03:02] Primeiro porque nem toda a plataforma ainda está pronta para P de conversões

[00:03:02–00:03:07] Segundo porque se você quiser fazer uma instalação via Tag Manager

[00:03:07–00:03:11] Dependendo da quantidade de requisição que você tem no site

[00:03:11–00:03:13] Você vai gastar mais de R$100 por mês

[00:03:13–00:03:16] Às vezes de servidor Cloud

[00:03:16–00:03:21] Então, eu sei que em muitos casos as pessoas vão acabar só com o pixel do navegador.

[00:03:21–00:03:23] Então, o que eu vou mostrar para vocês aqui?

[00:03:23–00:03:28] Como a gente instala a API de conversões do pixel no WordPress, que é o que a gente usa aqui e funciona muito bem.

[00:03:29–00:03:33] Depois eu vou mostrar para vocês algumas opções de instalação de pixel manuais.

[00:03:34–00:03:42] E aí, por último, se der, eu mostro também para vocês qual que seria a alternativa para quem não tem uma integração de parceiros para API de conversões.

[00:03:42–00:03:44] Caso alguém queira tentar fazer por conta própria

[00:03:44–00:03:46] Uma instalação no Tag Manager Server

[00:03:46–00:03:47] Ou coisa do tipo

[00:03:47–00:03:50] Vou dar aqui mais ou menos o caminho para vocês

[00:03:50–00:03:52] Mas eu não vou entrar tão a fundo nisso

[00:03:52–00:03:56] Porque nem eu cheguei a mexer muito com isso

[00:03:56–00:03:57] Eu sei que existe

[00:03:57–00:04:00] Mas como a gente usa mais aqui a questão do WordPress

[00:04:00–00:04:03] Eu deixo aí para quem realmente precisar

[00:04:03–00:04:06] Bom, concluindo aqui essa explicação

[00:04:06–00:04:08] Vamos para a instalação

[00:04:12–00:04:13] Tchau.
