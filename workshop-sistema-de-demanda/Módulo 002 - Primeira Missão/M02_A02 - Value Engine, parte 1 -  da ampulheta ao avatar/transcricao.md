# Value Engine, parte 1: da ampulheta ao avatar

> Transcrição automática com revisão textual. Dúvidas e limitações estão em [relatório de revisão](https://github.com/tc3midia/workshop-sistema-de-demanda-transcricoes/blob/ffe55d56029a698db7d27045e014927577c8515c/REVISAO.md). Timestamps relativos ao MKV capturado em 2×.

**[00:00:00–00:00:27]**

Então vamos lá. Quatro pilares. O sistema de demanda que a gente vai aprender a desenvolver hoje, ele é baseado nesses quatro pilares, tá? Então, basicamente, o que a gente tem? Primeiro, a arquitetura de receita. Isso aqui são fundamentos que mudam completamente aquilo que a gente entende como um processo comercial, um processo de venda, um processo de entrega. A vida inteira a gente olhou para a venda como isso aqui. Então eu tinha lead, eu tinha frio, morno, quente. E o processo de venda hoje, ele está mais parecido com isso aqui. E aí a gente separa em várias etapas, depois eu mostro melhor para vocês, mas basicamente é o famoso funil ampulheta.

**[00:00:28–00:00:47]**

E o funil ampuleta, ele faz o quê? Eu tenho uma entrada, onde eu tenho o lead chegando, eu faço uma qualificação desse lead, um agendamento, um processo de venda, um processo de entrega. A partir do momento do processo de entrega, deixa eu desenhar de novo, senão eu não consigo explicar para vocês. Isso aqui é muito importante vocês entenderem, porque isso aqui faz vocês ganharem muito dinheiro, tá? Então vem para cá, vem para cá. Aqui, aqui, aqui e aqui. Então eu tenho o quê? Eu tenho primeiro a captação, a aquisição de leads, então eu vou adquirir leads, eu vou qualificar os leads.

**[00:00:48–00:01:07]**

Aqui eu vou vender, aqui eu vou entregar, eu sei que não dá para entender, mas escuta o que eu estou falando, tá? O que eu vou fazer aqui, gente? Eu vou fazer a adoção. É o famoso onboarding, mas não é um onboarding, é um onboarding onde eu faço uma entrega para esse cliente, eu mostro para ele dando de um kick-off, qual é o plano de ação que eu vou fazer para ele, em quanto tempo eu vou entregar, e eu projeto qual que vai ser o primeiro ganho dele, o primeiro impacto. A gente já falou aqui, pô, mas o cliente não fica 45 dias na minha carteira, por que isso aqui não aconteceu certo?

**[00:01:07–00:01:26]**

Se isso aqui acontece certo, e ele entende que o primeiro impacto é com 60 dias, é essa a expectativa dele. E depois que eu faço isso, eu tenho a ascensão. O que é a ascensão? É eu jogar o cliente para cá de novo, para ele fazer uma nova compra. E isso acontece no mínimo três vezes, dentro da tua agência, e no teu cliente vai acontecer no mínimo uma vez por ano para o cliente que ele tem. Quando você joga esse sistema de aquisição, uma arquitetura de receita, para a tua operação, você traz o cliente por três, daqui a três meses ele sobe para cinco, daqui a três meses ele sobe para sete mil por mês, te pagando.

**[00:01:26–00:01:41]**

A gente vai mostrar, isso chama escada de valor. E escada, porque são degraus conectados. Eu tenho um first value, que é o primeiro impacto, e eu tenho um rise value, que é o motivo que faz o cliente contar de novo de mim. Isso estando bem montado, o cliente entra por um preço e continua pagando mais, a cada três, quatro meses ele sobe e não. Quando você faz isso para o cliente que você tem, a mesma coisa acontece. E isso faz com que o cliente nunca mais cancele com você. Então basicamente é isso aqui. A gente vai falar bastante sobre essa arquitetura, mas a gente vai falar sobre isso aqui na prática.

**[00:01:41–00:01:58]**

Aqui é o fundamento, mas eu vou mostrar para vocês na prática como isso é montado, na escada de valor, validation, todas as técnicas mais absurdas que tem de negócio, marketing, aquisição, venda, que estão sendo utilizados hoje aqui nos Estados Unidos. Caras como Alex Hormozi, Russell Brunson, esses caras que vocês deveriam pagar milhares de dólares para conhecer, vão ter, pelos R$29,00 hoje aqui, grande parte dessa implementação feita. A gente tem aqui o quê? Primeiro, diagnóstico da operação. Então toda vez que eu vou fazer uma arquitetura de receita sem implementar, eu tenho que fazer um diagnóstico operacional.

**[00:01:58–00:02:12]**

Vocês vão aprender a fazer o próprio diagnóstico aqui e como arremontar e escrever para fazer o diagnóstico para o cliente de vocês. Nada de ficar fazendo o diagnóstico na mão, que eu sou. Lembra do Bia? First, hoje a gente fala diagnóstico com IA. Aqui, descoberta do nicho. Pô, qual que é o nicho que eu opero? Ah, mas eu não quero operar com o nicho. Beleza, deixa ele aberto, mas vai ser muito mais difícil de você trabalhar, de você esconder e tudo mais. Agora, e para o meu cliente também tem? Óbvio que tem. O teu cliente trabalha dentro do nicho.

**[00:02:12–00:02:32]**

A Apple não vende para qualquer um. A Volkswagen não vende para qualquer um. A BMW não vende para qualquer um. São clientes de nichos diferentes. E o produto é desenvolvido para aquele nicho. Eu gosto muito do exemplo da Volkswagen. Quem conhece Volkswagen? Quem não conhece Volkswagen? Lá dentro da Volkswagen eu tenho o quê? Eu tenho um Gol, eu tenho uma Amarok, e eu tenho uma Tiguan. Eu não faço esse produto para o meu cliente. Como a gente é uma agência, o cliente chega, eu faço um briefing e monto o produto para ele. Não! Isso está errado.

**[00:02:32–00:02:47]**

Por isso que vocês não conseguem estar lá e ganhar dinheiro de verdade. Por quê? Porque produto que não existe é difícil de explicar. É difícil de vender, é difícil de entregar. Se o produto já existe, o que eu tenho que entender? O Gol é para um cara que está dentro do primeiro carro, que vai comprar ali para bater na empresa. O cara que vai comprar... Que hoje o Gol, eu achei que está far rico aí no Brasil também, né? Mas antigamente o Gol era para o quê? O cara ia comprar para botar na empresa, para fazer um escorre dele, ou estava começando a vida agora e vai comprar um Golzinho ali para ter um carro.

**[00:02:47–00:03:07]**

Já o Amarok, ela está focando em um cara que gosta de off-road, que tem chacra, tem fazenda, ou carrega carga, ou quer ir para fora. Ele não é feito para o cliente que chega lá e diz, olha, estou pensando em... Eu tenho uma fazenda, vocês constroem um carro para mim? Não, o carro está pronto. E a Tiguan? O cara de família, ou que já está melhor na vida, o cara foi lá e aconteceu e pegou uma Tiguan. Pô, vamos lá. BMW, esportividade, o cara que gosta de esportividade. Pô, Mercedes, luxo. Apple, você não pede para o cara botar três câmeras.

**[00:03:07–00:03:23]**

Já tem três câmeras nesse aqui, ele é maior, é um Apple Nexa. E tem esse aqui também, que é o Pro, que é menorzinho. O cara não fez para mim. Ele fez pensando em um cara que já existe no mercado, que tem essa preferência, ou o problema que esse produto resolve. Quando a gente pensa em descoberta de nicho, pesquisa de mercado, escada de valor, a gente chega num roteiro de venda entendendo quem é o nosso cliente, qual é o problema que ele tem, o que a gente entrega para ele, não muda. E é isso que faz você começar a escalar.

**[00:03:23–00:03:39]**

É isso que faz você começar a construir um produto de verdade. Tá? Beleza. Entre outras, 12 fases de implementação, a gente vai falar sobre essas, então, o processo que eu vou passar para vocês são 12 fases, a gente vai montar junto. O objetivo aqui, rodar a estrutura estratégica, gerando o manual operacional e o treinamento de IA que você vai utilizar para tudo na sua operação. Então, essa primeira esquina vai liberar isso para vocês. O visual do que é a agência de vocês de verdade e os dois arquivinhos mágicos que vocês jogam em qualquer IA e a IA começa a entender o que é a agência de vocês para tudo.

**[00:03:40–00:03:54]**

Então, vocês conversam com a IA e a IA sabe qual é a precificação, qual é o plano, o serviço, como é que ela vai fazer um carrossel, como é que ela vai ajudar vocês a produzir conteúdos para vocês poderem para criar isso e tudo mais. Depois que a gente tem isso montado, e só depois, que a polícia explica as grandes operações da mão para frente, a gente fala sobre o comercial inteligente. Gente, comercial inteligente é o quê? É um comercial simples, fácil de tocar, organizado em um CRM e você não precisa estar inventando a moda.

**[00:03:55–00:04:13]**

Eu só mexo em comercial se eu preciso melhorar ele, se eu não estou tendo o resultado que eu quero. E, obviamente, você vai ter aquelas calibragens para aumentar a porcentagem da conversão. Mas um comercial inteligente, ele não é um comercial absurdamente automatizado, nada disso. Às vezes, é um CRM com três fases montado num Kanban de uma planilha que você não entende para o WhatsApp e faz o fechamento. Se isso funciona para você, não serve. A gente já fez mais de um milhão em vendas utilizando o Trello como CRM, com o processo de venda do Trello e jogou os vídeos lá dentro e rodou num Kanban.

**[00:04:13–00:04:35]**

Por quê? Porque mais importante é o processo do que a ferramenta. Quando que você vai trocar de CRM? Quando o processo não acolpa mais nessa ferramenta. A gente trabalhou com o Kommo CRM por muito tempo, ainda uso na operação da agência de valor como CRM, porque ele ainda comporta a minha operação, mas, por exemplo, por outro motivo, a gente mudou. Porque o Kommo CRM não me dá a possibilidade de ter um agente de IA ali operando, vendo os vídeos e fazendo de uma forma mais barata. Ele me dá essa possibilidade, a gente fez isso por ele, mas fica muito maçante porque é um processo de integração externa, não é internalizado.

**[00:04:35–00:04:50]**

Então a gente desenvolveu o próprio CRM com IA por isso. Mas eu só vou fazer isso quando o processo não for comportado pela ferramenta. Se não, eu vou utilizar a mesma ferramenta para sempre. Tá? Mais uma coisa que a gente entendeu aqui sobre o Kommo. ele é muito bom para a agência, uma operação de quem sabe lidar com o como, mas, às vezes, ele não é tão bom para o cliente que o cliente não tem capacidade tecnológica para isso. Então tem que tomar cuidado, tá? Às vezes a gente fala, não, como é massa, mas é massa para a gente saber lidar.

**[00:04:50–00:05:09]**

Para quem não sabe lidar, é uma folia, uma bagunça, é nome do 4 errada, é uma desgraça. Folio de venda, etapas e fundamentos. A gente vai falar sobre fluxo de fechamento do lead à venda, a gente vai falar sobre a implementação de inteligências comerciais, a gente vai falar sobre geração de script e modelo de cadência, a gente vai falar sobre automação e gestão inteligente, tá? Objetivo, estruturar o processo comercial na prática, implementar modelo operacional, estratégia de venda e fluxo de cadência. Engenharia de demanda, agora o que a gente está fazendo? A gente posicionou o negócio, a gente montou a estrutura comercial, agora a gente está pronto para começar a receber leads.

**[00:05:09–00:05:28]**

Para começar a receber leads, não é fazer tráfego, se eu saio do lead para o tráfego, se eu saio do comercial para o tráfego, vou pagar caro no lead, eu vou ter leads qualificado, eu vou ter resultados que fazem eu ser demitido. É simples, é isso. Agora, se eu começo pelo posicionamento digital, eu construo a famosa camada que separa o curioso e traz o lead bom. E a gente está olhando para o retorno do tráfego orgânico. Prestem atenção nisso. O tráfego pago está trazendo do teu lado. O tráfego pago está na boca da grande maioria, só traz tudo do teu lado.

**[00:05:28–00:05:45]**

Antes a gente falava de 30% de conversão no tráfego, a gente estava falando de 5%, 7% de conversão no tráfego. Então a eficiência está lá embaixo, está caindo. Enquanto isso, enquanto a gente está falando do PP descendo, a gente está falando do tráfego orgânico subindo. YAP content, olha quanta gente está fazendo YAP content, gente, a gente tem um case dentro do nosso Mastermind que faz venda só com isso aqui. Ela vai lá e documenta o dia dela, ela grava reunião, depois ela faz cores, ela faz videozinho de dica para o nicho dela todo dia e ela fecha contrato caro nesses leads.

**[00:05:46–00:06:05]**

O tráfego pago ela não fecha. O cara vem, é curioso e tal. Qual que é a grande diferença? O tráfego orgânico, ele tem uma estrutura natural de aquecimento e envolvimento com o lead, onde o lead assiste o seu conteúdo, confia em você, entende o que você fala, abriu a autoridade e fecha. O tráfego pago não traz o cara no impacto. Aqui é esse lead, olha aqui essa lista, olha aqui esse produto, olha aqui essa isca. O cara vem nessa e ele não tem o fator de confiança ainda. Tá? A gente já falou dos sonhos de marketing que fazem esse posicionamento ser legal, óbvio que não adianta só gerar engajamento, você tem que transformar engajamento e venda.

**[00:06:05–00:06:24]**

Vamos falar de conteúdo estratégico, iscas digitais, pra mim, isso aqui é um jogo que todo mundo deveria estar jogando. A gente tem hoje mais de 30 iscas rodando, planilha, matéria de mídia, PDF, vai testando várias coisas, agora a gente vai botar uma mão de IA também, uma de skill de IA também pra rodar. Então, isso aí, e o tráfego orgânico e pago, tá? Objetivo, implementar a engenharia que traz isso verificado, os calls de vendas pra você fechar a conta todos os meses. E por fim, como é que funciona o nosso sistema de venda? Então, a reunião estratégica, a condução, a consultoria gratuita, como é que você faz?

**[00:06:24–00:06:42]**

Tem que ser consultiva, tem que ser consultiva, não adianta tentar entrar vendendo. Muita gente falha aqui, a gente já corrige um muito processo de venda. O cara fazia três, quatro reuniões por semana, e eu acho isso pouco, mas, pra uma operação pequena, é suficiente, três, quatro reuniões, se você fechar dois clientes por mês, de 2,500, então, de 5 mil a mais de NRR, 10 meses e 50 mil por mês. Então, é uma operação que cresceu saudável. Mas aí, fazia as reuniões e não fechava. Não fechava, não fechava. Aí, a gente vai ver a reunião, o que que estava acontecendo.

**[00:06:42–00:06:56]**

O cara entrava na reunião e já começava a falar do software, e não sei o que lá, e abria a tela e começava a vender. Reunião de venda, a gente só mostra a tela e depois o cliente comprou. O cliente comprou. Como que ele comprou? Tá, quanto é que é o teu serviço? O que que você me entrega? Pera aí que eu vou te mostrar. Enquanto o cliente não perguntou isso, é rapport, é bater objeção, é mostrar pra ele como é que tá a empresa dele na internet, tudo isso a gente vai falar também. E, por fim, a virada de oferta, que é exatamente o que eu falei.

**[00:06:56–00:07:12]**

O cliente tá pronto, aí a gente abre a tela, por exemplo, quando eu faço fechamento na call. Por que é na call? Porque se você fechar na call, você não precisa de um segundo coach, de um segundo aquecimento, de um processo comercial mais extenso. Vai fechar 100% na call? Não. Follow-up é infinito. Fala o app é uma coisa que você faz até Jesus voltar. O cara veio pra call, não comprou? Follow-up até Jesus voltar. A gente até tinha uma regra, quando o cliente falava sobre LGTB, a gente parava de chamar o link e dava como perdido e marcava ele lá no CRM pra não chamar mais.

**[00:07:13–00:07:27]**

Aí a gente cometeu um erro. Três meses depois que o cliente falou no LGTB, a gente ficava chamando ele numa automação e o cliente comprou. Aí a regra agora é se fala no LGTB, a gente aguarda três meses pra fazer o que ela falou lá. Tá? Então falou lá até Jesus voltar. Bom, gente, campo de batalha, tá? A gente vai entender também que a quebra de objeções, tava aqui escondidinho, pra gente poder construir esse processo de fechamento. Campo de batalha é basicamente o que a gente vai fazer agora, então. A arquitetura de receita. A primeira coisa, dentro da arquitetura de receita, é a gente estruturar ela.

**[00:07:28–00:07:48]**

A gente vai falar sobre a estruturação básica da operação, os exemplos de branding design que a gente vai fazer aqui também. A gente vai montar um design system e um projeto de IA pra tudo. É isso que eu vou mostrar pra vocês a partir de agora, tá? Então deixa eu fazer o seguinte, eu vou abrir aqui um link pra vocês poderem baixar a skill. Legal? Que naquela hora que eu troquei as telas, ó, já perdi de novo. Cadê vocês agora? Sumiu? Deixa eu fechar aqui essa. A hora que eu troquei as telas, eu perdi, gente.

**[00:07:48–00:08:15]**

O meu... Olha o meu pai. Tá aí. Agora achei que tava aqui. Eu perdi a minha pasta. Tá aqui. Skills. Value Engine, eu não tenho essa skill, vou compartilhar ela aqui. Vou botar ela como pública. vocês vão precisar fazer o download dela. Eu vou mostrar pra vocês como instala. E agora a gente vai ficar com a batalha. Pode ser? Pode ser ou não? Pode. Aí, ó. Bora. Baixem aí. Bora. Demorou, demorou, demorou. Vamos lá. Demorou, demorou. É isso. Bora. Ah, não. Risquei aqui, ó. Deixa eu riscar aqui também. Tem as 12 fases, tá? Gente, mas eu não vou ficar aqui no PDF, mas...

**[00:08:15–00:08:30]**

Eu vou explicar isso aqui no campo de batalha pra vocês pra ser mais prático, tá? A gente vai fazer todas as 12 fases aqui agora. Ô, Roque, esse material aí vai ser disponibilizado? Todo o material vai ser disponibilizado, inclusive a gente faz depois, a gente pega a aula e transforma ela em workbook passo a passo tudo que a gente falou aqui e disponibiliza pra vocês. Isso no final do workshop tem mais uns 5, 7 dias. A gente montar esse workbook todo, né? Pra gente não, pra IA, né? Pra IA monta. Mas aí a gente manda assim que estiver pronto, tá?

**[00:08:30–00:08:52]**

O link tá na onde, Robson? Desculpa. O link tá no chat. Deixa eu fixá-lo aqui pra vocês não perder fixar essa mensagem. Olha só aí. Show. Valeu. Fechou. Beleza. Meu povo, o que vocês vão fazer? Esse arquivo, ele é um arquivo arquivo zip. Um arquivo zipado. dentro desse arquivo zipado, a gente tem, então, eu tô compartilhando aqui, mas vocês não tão vendo, né? Porque eu tô só com com a tela do tablet. Deixa eu alterar pra outra coisa. Janela. Vamos trabalhar com a janela inteira. Vamos trabalhar com a tela inteira, cara. Tela 2. Um. Um pouquinho menor, mas dá pra ver tudo, né?

**[00:08:53–00:09:09]**

Ok. Então, o que a gente tem aqui? Vocês têm esse arquivinho aqui, que é o Value Engine, tá? E, basicamente, ele é chamado assim porque ele vai criar uma endímide de valor na operação de vocês. A dica é, vocês vão usar pra agência de vocês, mas vocês também podem pegar o mesmo chat depois e transformar essa skill no cliente de vocês. Então, pra cada cliente que chegar, vocês vão fazer 12 perguntas pra eles e vai ter a operação inteira do cliente na mão de vocês que vocês utilizarem. como que faz pra isso aqui acontecer? Vamos pegar o Claude.

**[00:09:09–00:09:25]**

Eu vou usar o Claude aqui, tá? Tem algumas aqui que eu já fiz. Depois a gente vai analisar junto, vai olhar junto com esses materiais aqui, tá? Tem uma que já tá mais completa, que é basicamente como que precisa fazer a sua entrega. Deixa eu abrir aqui os projetos só pra vocês entenderem o escopo geral. O que está aqui? Ok. Isso aqui é uma agência montada, tá? É um exemplo de agência montada que é a Acta Emergency. O que eu tenho aqui? Eu tenho um projeto de instrução. É um modelo estratégico de inteligência artificial do meu projeto dentro do Claude.

**[00:09:26–00:09:47]**

Aqui dentro eu tenho o exam, que é um arquivo que vai ser gerado para ser esquivo pra vocês também. Dentro desse exame, a gente tem basicamente as respostas prontas. Então, toda vez que eu precisar remapear a minha agência, eu falo pra ele Rod, vela e guine e responda a partir do exame. Só me pergunte algumas coisas a mais se você precisar. Então, toda vez eu consigo rodar isso aqui, tá? Aumentar o zoom. Muito pequeno, gente. Posso diminuir um pouquinho a tela aqui. Vou tentar 1.900 por 1.80. Melhorou? Está mais embaçado do que melhor, né? 2.48 ou 920?

**[00:09:47–00:10:09]**

Bota aí no chat. Melhor? Como agora? 2.48. Eu achei também embaçou. Beleza. Vamos deixar assim, então, se vocês não podiam mais ver a tela. Ok. Sim, vocês vão ter que instalar e eu já vou mostrar a instalação pra vocês na prática, mas só pra vocês entenderem o escopo final de onde a gente vai chegar, tá? Eu vou compartilhar com vocês também as vozes, que são os livros que eu coloco aqui dentro pra treinar minha IA. E isso aqui é gerado através de vocês. E tem outras coisas que são geradas também. Por exemplo, eu tenho a FN Brands, que é uma skill que carrega todo o padrão visual da minha agência dentro da memória do Claude.

**[00:10:09–00:10:23]**

Então, sempre que eu peço pra ele um PDF, sempre que eu peço pra ele um carrossel ou alguma coisa assim, ele contém aqui dentro todo o meu design system. A gente também vai aprender a desenvolver o design system aqui durante a nossa aula, tá? Então, toda a implementação a gente vai fazer, talvez a gente precise usar um pouco da tarde pra isso, mas eu acho que vale a pena eu deixar vocês com toda a operação certinha antes de ir pro comercial. E isso aqui pode ser feito aqui, e se vocês pegarem, vocês podem fazer isso pro cliente de vocês também.

**[00:10:23–00:10:45]**

Ou seja, montar a operação do cliente de vocês em algumas horas. Isso parece interessante ou não? Tá? Beleza. Como é que eu instala? Aqui em cima, no Claude, é assim, tá? Se você usa outra IA, pergunta pra própria IA que ela vai responder pra você. Mas no Claude, ele tem aqui esse minuzinho chamado personalizar, tá? Você vai fazer o seguinte, se já tiver a skill instalada, por exemplo, eu já tenho ela aqui, você vem aqui e exclui, tá? Eu atualizei ela hoje, então por isso tá há quatro horas, você exclui aqui, vem aqui em cima e adicionar, fazer upload da habilidade, busca aqui, e você vai pegar a skill A, deixa eu vir aqui na minha mesa, eu tenho a setup, skills, vou pegar lá a valentinha e eu subo ela e pronto, ó, clicar aqui na subestima não tem problema.

**[00:10:45–00:11:05]**

Vou salvar, fazer upload mesmo assim, e aí ela já veio estruturada aqui explicando exatamente como é que é o funcionamento dela, as regras, como é que ela funciona, o jogo todo dela, tá? Beleza, é isso, eu tenho o código aqui, se você quiser depois replicar, também funciona. Ok, uma vez que estando instalada a minha skill, tudo que eu preciso fazer agora é responder a ela, tá? Então eu vou pegar um novo chat e vou botar o seguinte, ó, ativar, ativar, além dele. Nossa, a tela não apareceu, cara. O que? Só a tela não apareceu, você tá fazendo aí o processo, procedimento, ou eu não sei, eu não peguei.

**[00:11:05–00:11:28]**

De instalar? É. Tá aparecendo lá? Não, tá aparecendo você, só. Eu acho que você não deve estar bem na tela dele, vai. É, tem alguma caixinha aí que tá na minha tela. Ah, eu acho que eu, eu acho que eu fixei a tela assim que deixou. Ah, você pode só repetir aí novamente esse processo, na instalação do vidão? Já repetiu. Deu certo aí, Thiago? Oi, não, eu não sei onde que tá a tela. Esse Google, esse meeting, ele é meio confuso. é, qual é a anotação? Eu não sei se tem como eu fixar a minha tela, eu acho que ela já vem fixada.

**[00:11:29–00:11:47]**

É, só tá aparecendo você, só, não tá aparecendo a outra tela, não consigo localizar aqui, desculpa, desculpa, não tá aparecendo aí. É, dá, tenta desfixar a tela do, a, a, não, não, não, não, já fixei, não tem nenhuma fixada, só, só tá, tá tudo normal, mas ele não aparece a outra. Thiago, você tá pelo celular ou você tá pelo computador? Não, tô pelo computador. Ó, vou compartilhar a tela de novo, vamos ver se ela vai. Boa. Cholei e botei de novo, vamos ver se parece fazer o mundo agora. Oi? Sim, então, estamos vendo. Aqui apareceu o meu peixe.

**[00:11:48–00:12:10]**

Hã? Aqui apareceu. Ah, beleza aqui. Bom, continuar aí, Robson, eu vou, vou ver aqui, vou localizar aqui, fica tranquilo. Valeu. Eu, Cholei, só uma dúvida rápida aqui, em relação à situação, eu já baixei o arquivo aqui, tá, tá dentro do meu, do meu notebook aqui, ele, tem uma pasta, inicial, quando a gente abre, que é, change.log, skill.md, aí tem... Não, não, você não precisa abrir ela, você vai jogar o arquivo inteiro pra dar um poste. Ah, não precisa abrir, eu jogo o arquivo zipado mesmo pra dentro do código, né? Sim, zipado, meu bem, baixa dois graus do ar lá pra nós, tá bem, gente, obrigado.

**[00:12:10–00:12:37]**

Então, explica novamente aí, só pra gente entender. Tá, então, ó, clico lá no projeto normal, cliquei ali em personalizar, tá? O app, eu venho fazer isso, ele abriu a tela de personalização, eu venho aqui em adicionar, fazer upload de habilidade. Ah, uma coisa legal, tá, gente, que o Claude tem, aqui em navegar, vocês têm muitas habilidades aqui, ó, projeto financeiro, vendas, operações, o Claude tem muita coisa que funciona muito bem, ó, marketing, design, engineer, human resources, que é recursos humanos pra contratação, tudo que vocês precisam pra empresa de vocês tem aqui dentro, tá? Inclusive, se vocês botarem, por exemplo, aqui um app file, vocês vão ter um, e não veio, só que eu falei, Vibe Prospecting, vamos ver se vem, ó, Vibe Prospecting, vai ter uma skill de Vibe, mas depois eu falo sobre isso, mas basicamente são skills de prospecção, eu vou falar sobre elas também.

**[00:12:37–00:12:57]**

Tá compartilhada a sua tela? Tá compartilhada sim. Tá compartilhada. Tá. Vou em adicionar, fazer a produtividade, cliquei ali, eu arrasto pra cá, selecionei a skill no zip mesmo, abrir, dei o zip pra cá, salvei, se tiver a skill vai pedir pra substituir, e substituiu, a skill está instalada. Ok? Beleza. Vou lá no meu novo chat, Ativar Value Engine, e vou dar um, um enter aqui pra entrar na nossa skill. Aqui, gente, tem alguns processos, que eles são mais lentos naturalmente. Por quê? Porque a gente tá falando de mais que o que vai à internet buscar informações.

**[00:12:57–00:13:23]**

Então, ela tem um processo de scrapping, de grab scrapping, e ela vai fazer a pesquisa pra vocês, ela vai encontrar cinco pessoas pra vocês prospectarem já, com base na resposta, então ela já vai entregar essa listinha pra vocês, é bem bacana, tá? Então, o que a gente tem aqui? São 12 fases, né, se a gente for totalizar, são 12 fases de desenvolvimento. Dentro dessas 12 fases de desenvolvimento, ela faz, basicamente, uma análise. Primeiro, diagnóstico da agência, ou da operação de vocês, descoberta do nicho, então vocês vão passar por um processo de escolher um nicho de mercado aqui, e é importante que vocês façam, eu vou explicar o porquê, três perguntas de valor, avatar do cliente, pra vocês poderem entender quais são os dois desejos, objeções do cliente, pra montar o produto, a pesquisa de mercado, que ela pode fazer sozinha pra vocês, inventário de performance barra eficiência, lembra que eu falei?

**[00:13:23–00:13:39]**

70% de eficiência, 30% de performance? Então, com base do que vocês já sabem, ela já monta o inventário pra vocês aqui, três níveis de acesso estratégico, com base nisso, ela vai montar pra vocês a escada de valor, e vai montar todos os cálculos, pra vocês entenderem como cobrar do cliente. A galera da agência de valor, gente, tá usando isso aqui agora, tá fechando contato na call, assim, ó, batata, banana, por quê? Porque isso aqui expõe, na cara do cliente, que se ele contratar vocês por 3 mil reais por mês, ele vai passar a economizar 10 mil reais por mês, em menos de 30 dias.

**[00:13:40–00:14:03]**

E é verdade, se vocês estruturarem o processo, o produto de vocês, com base nessa skill, vocês vão ter isso na mão. Aí vem a escada e a conta, ele faz uma conta de quanto custa demitir vocês da operação, pra deixar na cara do cliente, cara, se você desligar a gente agora, ele tá falando de custo pra você no descrever, tá? O value equation, que é onde a gente monta a narrativa, narrativa de venda, roteiro de vendas, script de apresentação, e as entregas finais que é. Ele vai entregar pra vocês o PDF, um checklist, PDF com toda a estratégia, 22 páginas, um checklist do que vocês têm que fazer agora, que vai ser a missão de vocês a partir disso, é resolver esse checklist, e vai entregar pra vocês os dois MDs, que são treinamentos de IA, com base, rapidamente, na inteligência da agência de vocês.

**[00:14:03–00:14:29]**

Tá? Vamos começar aqui? Ok. Ele vai dizer também aqui, na segunda fase do jogo, você vai responder normal, então ele vai fazer perguntas, você vai responder do fluxo, toda vez que ele terminar o fluxo, ele vai confirmar com vocês, você tem que aprovar, e tá, o outro ali pro próximo, ele não vai ser isso, tá? Aqui então a gente vai ter, nome da agência, eu gosto de fazer o quê? Gosto de pegar isso aqui, copiar, vou abrir aqui um Sublime Text, e só a uma boa bloquinha, tá? Nome da agência, B.O. Vou botar B.O.LC, aí vocês vão preenchendo também, B.O.com, se quiserem ir fazendo junto, tenha vontade, Instagram, B.O.USA, LinkedIn, putz, eu não me lembro do LinkedIn da B.O., gente, LinkedIn B.O., vou responder certinho aqui, pra ficar bonito, tá?

**[00:14:29–00:14:59]**

Ó, LinkedIn B.O., B.O. Tá aqui, B.O.Company, B.O.USA, vou botar até o link aqui, pra não se confundir. Outros canais, não preciso, não tenho, onde ela atua? Hoje atua na Flórida, vou botar aqui, Central Flórida, Central Flórida, B.O.S.A. Tempo de operação, a gente tá com sete meses, de operação, tamanho do time, três, três, quatro, cliente ativo hoje, onze, setor estudante atua, loja de carros, dealers, faturamento mensal atual, 22 mil dólares, principal desafio hoje, fase um, cara, escalar, escalar aqui, tá? Tô usando exemplos, tá, gente? Algumas coisas são reais, outras são fictícias, só pra gente poder acelerar no processo aqui.

**[00:14:59–00:15:19]**

Como que vamos? Voltei com as respostas, mandei pra ela. Não tenho pressa, ou tenho pressa pra fazer agora e acompanhar e ver o processo, mas depois façam de novo com mais calma. Vai gastar um monte de crédito em vocês, tá? Vai gastar o dia, de token, vai gastar. Faltou um R no carro. Não tem problema, Lucas, essa é a mágica da IA, que a gente escreve errado, ela acerta pra nós. Inclusive, você consegue fazer isso com áudio também, ela quer mandar áudio, ela vai fazer. Bom, o que ela vai fazer agora? Já percebe que ela começou a entrar em vários sites aqui, a sunbiz.org, que é o site do CNPJ americano, diz profile, ah, é só pros Estados Unidos?

**[00:15:19–00:15:36]**

Não, ela serve pro Brasil. Todos os outros exemplos que eu vou mostrar pra vocês são agências no Brasil. só a minha execução aqui, tá? Diagnóstico da B.O., olha que bacana. Nicho concentrado na prática. 11 clientes recorrentes, todos em lojas de carros, dealers, talalala. [trecho incerto] Então, eu já calculo lá, 22 mil com 11 clientes, 2 mil pro cliente. Autoridade do fundador como ativo. Ela já me achou e já disse que eu sou uma autoridade. Há mais de 15 anos de mercado, liderança, talalala. Discurso já apontado. Isso aqui não é [termo incerto], tá, gente? Não fiz nada pra alimentar a IA antes disso.

**[00:15:36–00:15:52]**

Ela tá partindo da pesquisa que ela fez. Depois que eu respondi isso, ela pesquisou na internet, tá vendo? Ela pesquisou todos esses sites aqui para poder fazer o diagnóstico. Ok? Ela vai fazer a mesma coisa com vocês. Ela vai trazer a visão da agência de vocês com base nas respostas. Discurso já aponta na direção direta. Comunicação fala em escala de vendas, estrutura, margem para visibilidade e tudo mais. A gente tem um problema muito grande na bio hoje e o perfil da bio não está ainda nichado. A gente decidiu o nicho e não refez o perfil.

**[00:15:52–00:16:10]**

Então ela tem que trazer esse gap aqui. Infradigital básica no lugar. A empresa é registrada e ativa na Flórida, site no ar, com o pixel da meta instalado, link a DIN e Instagram criados. Software próprios na operação. O sistema que seus clientes usam é DABIO. Ó, como é que ela sabe isso? A agência que entrega a ferramenta junto com o serviço tem um pilar de eficiência que concorrente de tráfego não consegue copiar. Eu não faço ideia de como ela encontrou essa informação, tá? Mas está certo. Gap, ó. Posicionamento público não está... Não conta a verdade da carteira, tá vendo?

**[00:16:10–00:16:31]**

No meu site não fala qual é o motivo. Site só em português, mentira. Mentira absurda. A não ser que tenha saído no meu botão de... É, mentira. Mentira. Tá tudo em inglês, já. Ô, Zero prova social visível. Verdade, a gente não tem nenhuma prova social. Promessa centrada em vender mais. Olha que bosta. Desculpa a palavra. Fuguei. Tá ruim. Tem que ser em eficiência. A gente não mudou ainda. Escala travada em gente não em demanda. Tá errado. Redes sociais sem cadência de autoridade ou nicho. Verdade. A gente não começou a operar ainda isso. Reposicionar site Bios para nicho automotivo.

**[00:16:31–00:16:54]**

Ó, minhas prioridades. Melhorias e prioridades que a gente tem que fazer agora. Posicionar. Publicar três case-read cliente. Versão em inglês do site. Transformar a entrega em planos nomeados com preços definidos por conta. E é exatamente o que vamos fazer na fase 7 e 8. Então, vamos ajudar com isso. Levantar os números de economia cliente atuais. Ativar uma cadência mínima de conteúdo de autoridade no nicho. Um, mínimo, dois, três conteúdos para se firmar. Aprovo? Aprovo. Gostei muito desse comentário, inclusive. Foi melhor do que a encomenda. Vocês estão fazendo também aí? Alguém já teve a resposta? Ó, aqui é muito legal porque a gente tem um ponto muito importante dentro da nossa mentoria, que é basicamente o quê, gente?

**[00:16:54–00:17:14]**

A galera não escolhe o nicho. E se você não escolhe o nicho, uma coisa que eu tenho que dizer para você é o seguinte, nicho não é a sua vida que vai mudar. O que acontece? Se eu vou fazer todo um mecanismo, o nicho basicamente é o seguinte. Ele está aqui. Então, aqui eu tenho o produto. Eu tenho o sistema. Eu tenho o preço. Eu tenho a praça. Eu estou escrevendo assim porque é só para pronomear, tá? Não estou tentando escrever, não. Não é tão feia a minha letra. Mas basicamente, tudo que está em volta é o meu ecossistema.

**[00:17:14–00:17:29]**

E ele parte do núcleo que é o nicho. Se eu não sei qual é o meu nicho, eu não sei qual é o problema. Se eu não sei qual é o problema, eu não tenho soluções. Ah, Robson, eu posso ter mais de um nicho? Pode, mas cada nicho dá mais trabalho. Se eu tenho um nicho só, eu tenho um trabalho. Dois nichos é duas vezes o trabalho. De estruturar, de compor, de construir, de melhorar, de otimizar, de fazer o processo de venda e ir para cima. Então, para você que quer ganhar dinheiro e escalar rápido, um nicho só é o melhor caminho.

**[00:17:30–00:17:46]**

Ah, eu quero aproveitar mais oportunidades porque eu ainda não tenho essa informação. Aí você abre dois, três nichos, roda a skill várias vezes, não tem problema nenhum. Inclusive, eu vou mostrar para vocês que dá para rodar a skill no produto automático para fazer suas pesquisas de campo, que é bem legal, tá? O que deu aqui? Ok, voltamos aqui. Ah, meu menu veio para cá, do nada. Ok. Beleza. E quem está me perguntando aqui, qual é o nicho e qual é a descoberta de nicho? Ele vai me guiar aqui no universo macro do nicho para poder fazer uma escolha saudável, uma escolha legal.

**[00:17:46–00:18:05]**

Então, ele fala, você vai trabalhar com saúde, estética e bem-estar? E ele explica o que é esse nicho, quais são os prós e quais são os contras, tá? Primeiro, a gente vai escolher aqui qual é o universo. Negócios locais com ticket alto. Gosto muito. O que é os prós e os contas? Varejo físico, alimentação, hospitalidade, serviços profissionais B2B, educação, produto. Leiam isso. Tenho certeza que vocês vão escolher isso aqui com mais qualidade do que escolheriam de qualquer forma, tá? Olha, eu posso aumentar. Que burro. Desculpa. Vou aumentar bem aqui. Agora fica bem bom pra vocês verem.

**[00:18:06–00:18:23]**

Eu vou escolher negócios locais de alto ticket. Eu gosto. Onde eu gosto de trabalhar, onde eu gosto de atuar. Automotivo. Pegou já de cara. Já mandou. Nicho de dealers independente usados, franchise dealers, revendas de luxo exóticos, buy here, pay here ou motores de power sport. Onde eu tô, já vou direto aqui e nem vou pensar. Mas ele vai te dar mais nichos ali. Tem o nicho de consultório, que é muito bom também. Nicho de consultório é ótimo pra trabalhar eficiência, pra ter recorrência, né? Qualquer coisa que tem a consulta, agendamento é legal. E aí ele vem aqui pro nicho de fato, né?

**[00:18:23–00:18:44]**

Então a gente trabalhou a primeira coisa do universo. Trabalhamos a vertical desse universo. Agora a gente trabalha, obviamente, o nicho em si. Livro independente usados. Stock de 30, 150 carros. Micro revendas, até 30 carros. Revendas de luxo. Fransiders. Eu vou pegar. Em 30, 50, eu vou pegar o micro. Vou montar pro micro aqui. Até 30 carros. Olha como ele muda bastante, né? É outra comunicação, é outro fluxo de caixa. Os problemas são diferentes e tudo mais. Então é importante a gente saber. Agora é atualizado da Biopen. Eu não queria que ele fizesse isso. Eu acho que ele já identificou que eu tô mexendo na bio aqui.

**[00:18:44–00:19:03]**

Mandando a memória nova lá. Fechado. Nicho revendo de carros usados até 30 carros. Risco. Orçamento apertado com churn alto nesse perfil. Agência que vende só mais leads. Morre com um ticket de 500 dólares. Cancelamento em três meses. Olha que louco. O que eu tô escolhendo é certa. Parará, parará. A consequência. Resumo da fase 2. Eu vou aprovar mesmo assim que eu sou louco. É, mano. Um risco de churn em três meses. É que é isso. Quero. Perguntas de valor. Aqui é muito interessante. Por quê? Porque ele vai te orientar sobre aquilo que você quer trabalhar.

**[00:19:03–00:19:17]**

Onde você quer entregar o resultado. Então, sobre dinheiro no final do mês. O que esse cliente quer, né? Ele quer que sobe dinheiro no final do mês. Aí você pode pegar a descrição se tiver dúvida. Ele quer gerar o estoque mais rápido. Ou ele quer parar de vender. Ele quer parar de perder venda por organização. Ele quer gerar estoque rápido. Vai estar na boca de qualquer dealer hoje. Ele precisa gerar o estoque rápido. Porque ele trabalha com o Forplan. O Forplan cobra ele em três meses. Que é o financiamento automotivo. Então, ele precisa gerar o estoque.

**[00:19:18–00:19:36]**

Vender carro a cada 30... Vender cada carro em até 30 dias no lote. Qual que é o resultado que ele quer que converte. Girar o estoque completo 12 vezes ao ano. Comprar melhor porque vende rápido. Um. Vender ele em 30 dias porque ele não paga a taxa de barriga. De Forplan. No controle do negócio. Como é que esse cara quer se sentir? No controle do negócio. Tranquilo com as contas. Orgulhoso da loja de construir. Quer se sentir tranquilo com as contas. Dois. Mais uma vez. Olha como eu estou indo rápido. Não estou nem processando a informação direito.

**[00:19:36–00:19:52]**

Porque eu quero que vocês mostrem. Você vai fazer isso com mais calma. O que ele me trouxe aqui? Resumo três. Necessidade principal. Geral, estoque mais rápido. Carro parado. E juros de... Olha, até ele botou. Forplan. Mais depreciação todo dia. Forplan é o tipo de financiamento que vocês entenderem, gente. Rapidamente. Que é focado em lojas de automóveis. E o que acontece? Quando o cara usa o dinheiro desse financiamento. Ele tem lá 100 mil dólares. Ele usa 20 mil. Nos três primeiros meses. Ele tem os 20 mil parado lá. Que ele pode usar. Que fica parado. Ele pode simplesmente vender o carro.

**[00:19:53–00:20:11]**

Pagar o forplan. Para pagar 200, 300 dólares de taxa. Só porque usou ele certo. Se passar os três meses. Ele tem que pagar o carro para o banco. Aí ele começa a pagar juros e tudo mais. E perde o lucro. Então é isso que ele está falando aqui. Resultado concreto. Vender carro a cada 30 dias. Ou seja, nunca vai usar o forplan. E como quer se sentir? Tranquilo com as contas. O forplan deixa de ser uma bomba relógio. Para cima. Trabalhando nisso. Algumas fases vão demorar um pouquinho mais. Fiquem tranquilos. Enquanto ele estiver se mexendo.

**[00:20:11–00:20:29]**

Tudo certo. Se ele parar de se mexer. Vocês botam três pontinhos. Assim. Às vezes o Claudio vai tomar um café. Se quer de voltar. Vocês ativam ele de volta. Ó. Avatar do cliente. O que a gente fez? A gente construiu a nossa agência já. Tá? Então basicamente o que vocês fizeram aqui foi um processo de 30 dias. De pesquisa de mercado. De entender nicho. De escolher o nicho. Agora eu falo com quem é a cliente de vocês. Perfil. Quem é? É um homem de 35 a 55 anos. Muitas vezes imigrante. Brasileiro latino. Ex-vendedor de concessionária.

**[00:20:29–00:20:48]**

Ex-mecânico. Ou empreendedor. E venceu. Que começou vendendo carro no Facebook do Marketplace. E cresceu até abrir uma loja. O negócio dele é uma revenda independente. Com 10 a 30 carros no pátio. Operando há 2 a 8 anos. Usados. 8 mil a 25 mil dólares. Compre em leilão. Merlin Corporate. Toda semana. Ou quinzena. Faturamento. Vende de 8 a 15 carros por mês. Algo como 128 a 250 mil. Em veículos com margem bruta de 1.500 a 2.500 por carro. A margem é bem maior. Mas tudo bem. O lucro real do mês fica entre 8 e 20 mil.

**[00:20:48–00:21:06]**

Não. 515 e 30 mil. Mas também tá lá. Equipe. Ele mesmo. Mais uma ou duas pessoas. Fecha a localização central fora. Orlando, Kiss, Nissan, Ford. Tampa no raio expandido. Lote em avenida. Difluxo médio ou galpão. Top. Basicamente assim, gente. Ele descreveu quem é meu cliente. E acertou. E isso é muito legal vocês lerem. Cara, tá muito fora. Corrige ele, tá? Não avança sem corrigir. Ele vai pedir aprovação. Leiam tudo. Crescento a 5.2. Tem carro parado a 60 dias. Começa os juros. É 90. Aqui eu tenho que corrigir ele. Chega ali de madrugada de domingo e ninguém responde.

**[00:21:07–00:21:22]**

Bota aí a pra isso. Vendo. Vendo. No final do mês não sobra dinheiro. Não tem controle financeiro. Você vai e bota um softwarezinho financeiro. Que ele vai estar indo nas contas dele. Olha quanto dinheiro eu tô trazendo. Eficiência. Só de olhar isso aqui. Com a ideia já dá pra ter de produto. Sou eu que faço tudo. Compre, anuncio, respondo. Olha só que eu tô anunciando pra ele. Respondendo. Olha aqui também. Vendo carro por volta do banco. Não tenho tempo nem de almoçar. Olha só. Isso aqui é muito importante. Vocês vão entender. Vocês podem ter um...

**[00:21:23–00:21:47]**

Vocês podem ter uma empresa boa. Uma boa empresa. Uma boa empresa. Empresa. Deixa eu pegar outro lado do canto aqui. Aqui já tá indo lá no final. Não vou conseguir desenrolar. Vocês podem ter uma boa empresa. O que é uma boa empresa? Resolve o problema do negócio. Uma boa empresa resolve o problema do negócio. Então ela entrou. Ela entendeu qual é o negócio que ela tá operando. E uma boa empresa resolve o problema do negócio. Agora, o que uma ótima empresa faz? Alguém arrisca? Ela botou no chat. Uma ótima empresa faz? Ela já chegou a roca.

**[00:21:47–00:22:26]**

Aí. Resolve problemas. Não. Já tá resolvendo o problema. Resolve o problema daqui. Gera valor. Não. Gera valor todo mundo. Gera. Tá um livro. Gera valor. Balota. Não. Balota. Entrega tempo. Resolve. O problema. Do. Dono. Do negócio. Vocês já acordaram no meio da noite. ansiosos com o problema da empresa de vocês? Quase todos os dias. Se alguém resolve esse problema de vocês, o que acontece? Quem é que essa pessoa vira na vida de vocês? Salvador. Olha o problema. Olha o problema. O negócio do meu cliente já na vida dele que eu resolvo. é? Quando vocês têm essa resposta, meu irmão.

**[00:22:28–00:22:48]**

Tá pago ou não tá pago? Tem sininho pra mim agora ou não? Pelo amor de Deus. Tá pago. Vou até falar. Pronto. Encontrem esse tipo de problema. Usem a IA pra encontrar esse tipo de problema. Podem ir atrás. Pega aí a facol. É a dor que esse negócio causa no meu cliente. Ajuda a encontrar. Vai no ânago do carro. Se você bota isso num anúncio, tá cansado de perder o tempo por não entender os números da tua empresa e fechar sempre no negativo e não conseguir pagar o boleto, dar uma viagem pra tua família. Tá perdendo o final de semana inteiro em vez de ver os seus filhos crescerem e tá trancado na empresa.

**[00:22:49–00:23:06]**

Você não pode nem ficar... Vou falar uma minha agora. Você não pode nem ficar doente porque a tua agência fecha. Quem já viu esse anúncio meu aí? Sacou? Se vocês encontram isso aqui, velho, isso aqui é ouro. É o melhor anúncio. É o melhor hook. Isso aqui roda infinitamente, tá? Isso é atendor dele. Eu sou o computador. Não confio em agência. Já paguei em uma... Olha, isso aqui é o atendor dele. Uma que mandava lead e tal. Toda empresa que a gente chega aqui tá assim. Onde lead? Lead pra caceta. Não é pouco lead, não.

**[00:23:06–00:23:24]**

400 leads, 500 leads por mês. A gente gera no máximo 200 leads por mês. Os caras geram 400, 500 leads por mês. Mais barato que eu. Bem mais barato que eu. Pega um vende lá. O meu lead de vende. A gente pega o cara só vendendo 2, 3, 4 carros. Os caras mandam 11, 15 carros por mês. Os caras saem de 30, 40 mil de faturamento pra 180, 200 mil de faturamento. Só de ajeitar o funil. Toda agência que entrou aqui nos Estados Unidos entrou por esses temas, alguns gurus aí, né? De agência na gringa, agência em bola e tal.

**[00:23:24–00:23:40]**

E no Brasil que fala, ah, vai lá, a Cobra 750 faz toda a África. Os Estados Unidos tá tudo assim. E a V4. A V4 veio pra cá, que fez uma bagunça. Todo mundo tá falando mal da V4 aqui também. Por quê? Porque os caras entram aqui pra gerar lead. E as operações não estão prontas pra lead. Nem no Brasil, nem nos Estados Unidos fazem. Operação americana também não tá pronta pra lead. Pra volume. Eles estão acostumados a atender os walk-ins. Pessoas que vão até a loja. O comércio aqui é pulsante. Terra do capitalismo. Começou a gerar volume no tráfego.

**[00:23:40–00:24:01]**

Eles se perdem. Não conseguem dar vazão. Não entendem o processo. Dorda, cara. Cinco desejos. Carro entrando e saindo. Vou lá até 30 dias. Posso usar pra anunciar. Todo lead respondido em minutos. Posso. A gente tem uma inteligência que responde seus leads. A qualquer hora. Sem depender. Já me deu até o produto que eu tenho que ter aqui. Saber com um olhar quais carros estão envelhecendo. E o que fazer com cada um. Mas como é que faz isso, Robson? Cara. Faz isso. Desenvolvendo. Uma aplicação. Que tem um nível de inteligência. Que lá no menu de inteligência fala.

**[00:24:01–00:24:21]**

Cara. Aqui, ó. Teus carros encalhados são esses. Teus carros médios são esses. Teus carros que vendem mais rápido são esses. Os carros que mais vendem na tua empresa é esse aqui. Você não tem no estoque. Olha aqui, ó. Os carros que mais vendem em Orlando. Os mais pesquisados no Google. Compra a partir daqui. Eu não vou dizer no estoque. Eu comecei vendendo tráfego para os clientes aqui. Olha o que eu entrego hoje. Comercial, calendário, campanha, aplicação. Controle de clientes, estatístico. Controle de investidores. Menu de inteligência. Estoque. Farplan. Atendimento no WhatsApp. Comercial. Comercial. Channel. Chega a rede do Facebook.

**[00:24:21–00:24:40]**

Do Instagram. Do WhatsApp. Tudo aqui. Eles atendem tudo aqui dentro. Com o IA. Tudo isso que a gente entrega hoje. Esse CRM é meu. Vira aqui que vai do. Está da minha agência. Por quê? Porque a gente foi resolvendo esses micro-problemas. Foi pesquisando. Qual o problema que o meu cliente tem? Foi escutando. Pega o cloud. Vai no cliente. Faz uma reunião. Qual o cliente que o meu cliente tem? Qual o problema ele tem? Deixa eu resolver aqui sem nem me pedir. Qual o problema? Não programei nenhuma linha desse software. Eu entendi o cliente. Muitas vezes eu jogava o cloud do cliente em IA.

**[00:24:40–00:24:58]**

E pedia pra implementar. E aí implementava pra mim. Quem eu fiz dessa merda? Gente. Entende o que eu falei pra vocês agora? Ó. Cloud. Quando você tem o cloud. Eu vou te dar esse arquivo aqui. Aqui você tem as reuniões. Tem a reunião. Muitas vezes eu peguei a reunião do cliente aqui dentro. Tá o áudio. Eu gerei o arquivo. Deixa eu ver. Esse aqui foi o que eu gerei hoje. Eu gerei o arquivo da reunião. Eu venho aqui nesse arquivo. Copio o transcript. Vou lá na minha IA. E jogo no chat da IA. No last code.

**[00:24:58–00:25:20]**

Aqui ó. Vou pegar aqui. A velote. Eu venho aqui e jogo aqui ó. Pum. E peço pra ela. Interprete esse texto. Deja e presta os pedidos do cliente. E liste pra mim. Aí ela liste os pedidos. Eu falo implementa o 1 e 3. Ela faz. Parar de pagar juros. Reduzir. Ó. Três objetivos práticos. Isso aqui tem que virar produto. Reduzir os 10 unlocks. Médio pra 30 dias ou menos. Isso aqui tem que ter uma parada que vocês colocam em aplicativo. A gente colocou também. Quando eu venho aqui pro Melodio Inteligência. Eu tenho aqui ó. Os que mais vendem.

**[00:25:20–00:25:33]**

Até 10 mil dólares. 42 dias de giro. De 10 a 15. 102 dias de giro. De 15 a 20. 68 dias de giro. Tá vendo? Eu mostro pra ele qual é o valor. Qual é o giro que ele tem no pátio. O melhor tá esse. Qual que é a meta agora? Diminuir isso aqui. A gente já tá falando que eu diminuo o giro. Então eu tenho essa meta. Eu mostro pra ele. A gente tem como trabalhar. Nada que não é medido pode ser melhorado. Então você tem que primeiro entender. Mede e vai tá assim. Recuperar as vendas e tal.

**[00:25:34–00:25:37]**

Vamos pro próximo passo aqui. Pra não se estender muito. Vou aprovar aqui. Essa etapa também tá top. Perfeita. Escreve exatamente no cliente.
