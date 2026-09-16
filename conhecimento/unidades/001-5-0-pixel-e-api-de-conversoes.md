---
type: unidades-aula
status: validado
title: "5.0 - Pixel e API de Conversões"
modulo: "001"
ordem: 6
aula_id: 54dea110daddeb21
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - cst_m01_a05_pixel_e_api_de_conversoes.pdf
  - transcricao.md
extraido_em: 2026-09-14
gerado_por: opus-5
retiradas: []
divisoes: []
fusoes: []
---

# 5.0 - Pixel e API de Conversões

## Contexto da aula

Aula de princípios: apresenta pixel, API de conversões e traqueamento antes de o aluno entrar em qualquer fonte de tráfego.
O objetivo declarado é conceitual — entender o que cada peça é e para que serve, para que a configuração prática faça sentido quando chegar.
Cobre as três funções do pixel, o que é um pixel sujo, as quatro formas de instalação e em que parte do site o código entra.
Explica a API de conversões como um canal de comunicação mais robusto, que vive no servidor em vez do navegador.
Fecha com traqueamento: ferramentas, técnicas rudimentares para negócio local e a margem de erro esperada na leitura dos dados.
A criação e a instalação passo a passo ficam para as aulas de cada plataforma e para os cursos de Google Tag Manager e de Google Analytics da comunidade.

## Unidades

### U:54dea110daddeb21:001 — Pixel, API de conversões e traqueamento medem o investimento
```yaml
tipo: conceito
plataforma: [geral]
tema: pixel-e-eventos
tarefas: []
fonte: "fala+pdf:cst_m01_a05_pixel_e_api_de_conversoes.pdf"
faixa: "00:00:00–00:00:31"
perecivel: false
confianca: alta
versao: 1
```
As três peças juntas permitem medir o resultado prático de cada centavo investido em tráfego pago e entender o impacto da verba dentro da estratégia.
Sem elas o anunciante não consegue direcionar melhor o investimento nem justificar o aumento da verba ao longo do tempo.

### U:54dea110daddeb21:002 — A aula explica os conceitos; a configuração fica para cada fonte
```yaml
tipo: limite
plataforma: [geral]
tema: pixel-e-eventos
tarefas: []
fonte: "fala+pdf:cst_m01_a05_pixel_e_api_de_conversoes.pdf"
faixa: "00:00:31–00:01:04"
perecivel: false
confianca: alta
versao: 1
```
Esta aula não ensina a criar nem a configurar o pixel em nenhuma plataforma: trata só do que cada ferramenta é e para que serve.
A criação e a configuração específicas de Meta Ads, Google Ads e TikTok Ads aparecem nas aulas de cada fonte de tráfego.

### U:54dea110daddeb21:003 — Primeiro contato com a nomenclatura antes da aula prática
```yaml
tipo: conceito
plataforma: [geral]
tema: fundamentos-e-carreira
tarefas: []
fonte: fala
faixa: "00:01:04–00:01:38"
perecivel: false
confianca: alta
versao: 1
```
Entender o que uma peça é e para que serve antes de configurá-la dá a ela a devida importância e torna a aula de execução mais fácil.
O professor compara com aprender um idioma: são necessários vários contatos com a mesma nomenclatura até ela ficar.

### U:54dea110daddeb21:004 — O pixel é o informante do site
```yaml
tipo: conceito
plataforma: [geral]
tema: pixel-e-eventos
tarefas: []
fonte: "fala+pdf:cst_m01_a05_pixel_e_api_de_conversoes.pdf"
faixa: "00:01:38–00:02:45"
perecivel: false
confianca: alta
versao: 1
```
O pixel fica instalado dentro do site e avisa a fonte de tráfego cada vez que alguém entra e faz alguma coisa ali.
Ele relata entrada na página, produto adicionado ao carrinho, compra iniciada, compra concluída e o valor dessa compra.
O nome vem do pedacinho mínimo da tela: é uma célula do site que ninguém enxerga, mas que está lá.

### U:54dea110daddeb21:005 — O gestor não precisa entender de código
```yaml
tipo: regra
plataforma: [geral]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: "fala+pdf:cst_m01_a05_pixel_e_api_de_conversoes.pdf"
faixa: "00:02:46–00:04:10"
perecivel: false
confianca: alta
versao: 1
```
O pixel é um código, um conjunto de letras, números e símbolos sem sentido para quem não programa.
Quem cuida dos anúncios não precisa entender programação: basta saber onde criar o pixel, onde instalar e como instalar.

### U:54dea110daddeb21:006 — As três funções do pixel
```yaml
tipo: conceito
plataforma: [geral]
tema: pixel-e-eventos
tarefas: []
fonte: "fala+pdf:cst_m01_a05_pixel_e_api_de_conversoes.pdf"
faixa: "00:04:11–00:04:50"
perecivel: false
confianca: alta
versao: 1
```
O pixel faz três coisas: leva para a fonte de tráfego as informações do que acontece no site, funciona como cérebro da conta de anúncios e cria audiências.
O professor pede que essa lista de três seja memorizada, porque ela volta quando ele explica a API de conversões.

### U:54dea110daddeb21:007 — Cada fonte de tráfego fornece um pixel próprio
```yaml
tipo: regra
plataforma: [geral]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: "fala+pdf:cst_m01_a05_pixel_e_api_de_conversoes.pdf"
faixa: "00:04:50–00:05:25"
perecivel: false
confianca: alta
versao: 1
```
Não existe um código único que sirva para todas as plataformas: Meta Ads, Google Ads, TikTok Ads, LinkedIn Ads e as demais entregam cada uma o seu pixel.
Trate o pixel como impressão digital ou DNA do anunciante naquela plataforma: ele é exclusivo e só serve ali.

### U:54dea110daddeb21:008 — O pixel é o cérebro que decide para quem mostrar primeiro
```yaml
tipo: conceito
plataforma: [geral]
tema: pixel-e-eventos
tarefas: []
fonte: "fala+pdf:cst_m01_a05_pixel_e_api_de_conversoes.pdf"
faixa: "00:05:25–00:06:39"
perecivel: false
confianca: alta
versao: 1
```
Diante de um público de um milhão de pessoas, alguém precisa decidir para quem o anúncio aparece primeiro e para quem aparece depois.
Quem faz essa escolha é o pixel: ele é a inteligência da conta e direciona a entrega para quem tem mais chance de gerar resultado.

### U:54dea110daddeb21:009 — Pixel novo não impede resultado
```yaml
tipo: conceito
plataforma: [geral]
tema: pixel-e-eventos
tarefas: []
fonte: fala
faixa: "00:06:39–00:07:54"
perecivel: false
confianca: alta
versao: 1
```
Com um pixel recém-criado a fonte de tráfego começa por aproximação: lê o público selecionado, o texto do anúncio e o conteúdo do site e entrega para quem ela acha mais provável.
Conforme as campanhas geram venda, cadastro, mensagem ou engajamento, a conta sai do achismo e passa a reconhecer o público-alvo real.
O pixel não é a única fonte de inteligência que a plataforma tem.

### U:54dea110daddeb21:010 — Conta herdada com o pixel treinado errado
```yaml
tipo: exemplo
plataforma: [geral]
tema: pixel-e-eventos
tarefas: [otimizar-publicos-e-segmentacoes, otimizar-anuncios]
fonte: fala
faixa: "00:07:54–00:08:28"
perecivel: false
confianca: alta
versao: 1
```
Situação: o professor assume um cliente que já anunciava com outro gestor de tráfego.
O que aconteceu: o gestor anterior escolhia mal as segmentações e publicava anúncios genéricos, atraindo as pessoas erradas e alimentando o pixel com elas.
Lógica: o pixel aprende com quem ele atrai, e um pixel treinado errado é como um cachorro que não foi adestrado no começo — reeducar depois é difícil.

### U:54dea110daddeb21:011 — Quando o pixel foi treinado errado, criar um novo costuma ser o caminho
```yaml
tipo: decisao
plataforma: [geral]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: "00:08:12–00:08:28"
condicoes: "pixel já alimentado com o público errado por gestão anterior"
perecivel: false
confianca: alta
versao: 1
```
Quando o pixel foi treinado com o público errado e reeducá-lo se mostra difícil, muitas vezes o melhor caminho é criar um pixel novo.

### U:54dea110daddeb21:012 — O material afirma que o pixel sujo é reversível com o tempo
```yaml
tipo: fato-material
plataforma: [geral]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: "pdf:cst_m01_a05_pixel_e_api_de_conversoes.pdf"
perecivel: false
confianca: alta
versao: 1
nota: "O PDF diz que a situação do pixel sujo pode ser revertida com o tempo; na fala o professor enfatiza a dificuldade de reeducar e sugere criar um pixel novo."
```
O material escrito registra que um pixel sujo prejudica os resultados das campanhas, mas que dá para reverter esse quadro com o tempo.

### U:54dea110daddeb21:013 — Não culpe o pixel pelo resultado ruim
```yaml
tipo: regra
plataforma: [geral]
tema: otimizacao
tarefas: [ler-metricas-e-relatorios]
fonte: "fala+pdf:cst_m01_a05_pixel_e_api_de_conversoes.pdf"
faixa: "00:08:29–00:10:09"
perecivel: false
confianca: alta
versao: 1
```
Se os anúncios apontam para o público-alvo e as segmentações são as óbvias, sem reinventar a roda, o problema provavelmente não está no pixel.
Resultado ruim depende de muitos fatores — preço do produto, engajamento da marca, percepção de valor da audiência — e culpar o pixel é o atalho fácil.
O professor pede que acenda uma luz vermelha sempre que alguém, cliente ou gestor, atribuir tudo ao pixel.

### U:54dea110daddeb21:014 — Público qualificado é quem vê valor, não quem tem dinheiro
```yaml
tipo: conceito
plataforma: [geral]
tema: publicos
tarefas: []
fonte: fala
faixa: "00:09:01–00:09:38"
perecivel: false
confianca: alta
versao: 1
```
Não é o saldo bancário que define se alguém é público qualificado: quem tem dinheiro não compra o que não faz sentido para ele.
O que qualifica é a pessoa enxergar valor no produto, e isso vem da narrativa construída em volta da marca, como no caso das canetas de luxo citadas na aula.

### U:54dea110daddeb21:015 — Anúncio é filtro, não isca para todo mundo
```yaml
tipo: regra
plataforma: [geral]
tema: criativo
tarefas: [otimizar-anuncios]
fonte: fala
faixa: "00:10:09–00:10:41"
perecivel: false
confianca: alta
versao: 1
```
O problema aparece quando se mistura tudo para atrair o maior número possível de públicos com o mesmo anúncio.
Faça o anúncio funcionar como filtro que puxa as pessoas certas, porque é ele que decide quem alimenta o pixel.

### U:54dea110daddeb21:016 — Conta com mais dados deixa o pixel mais inteligente
```yaml
tipo: conceito
plataforma: [geral]
tema: pixel-e-eventos
tarefas: []
fonte: fala
faixa: "00:10:41–00:11:20"
perecivel: false
confianca: alta
versao: 1
```
Quanto mais antiga é a conta de anúncios e quanto mais dados ela produz, mais inteligente fica o pixel e melhor ele direciona a entrega.

### U:54dea110daddeb21:017 — Terceira função: criar públicos de quem visitou ou agiu no site
```yaml
tipo: conceito
plataforma: [geral]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: "fala+pdf:cst_m01_a05_pixel_e_api_de_conversoes.pdf"
faixa: "00:11:00–00:11:55"
perecivel: false
confianca: alta
versao: 1
```
Pelo pixel dá para montar públicos e segmentações de quem visitou o site ou realizou alguma ação dentro dele.
Entram nessa lista quem se cadastrou, quem clicou em um botão, quem chegou a uma página determinada, quem adicionou produto ao carrinho e quem comprou.

### U:54dea110daddeb21:018 — Onde o pixel aparece em cada plataforma
```yaml
tipo: alerta-ui
plataforma: [meta, google]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: "00:11:20–00:12:10"
perecivel: true
confianca: media
versao: 1
nota: "O professor cita a localização no Google Ads de passagem, durante a demonstração de tela, sem abrir o painel."
```
No Meta Ads o pixel fica no gerenciador de eventos; no Google Ads ele aparece na parte de metas, no resumo.
O pixel vive dentro da conta de anúncios da fonte de tráfego, não no site nem em uma ferramenta separada.

### U:54dea110daddeb21:019 — Um pixel por conta de anúncios
```yaml
tipo: regra
plataforma: [geral]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos, configurar-conta]
fonte: fala
faixa: "00:12:10–00:12:36"
perecivel: false
confianca: alta
versao: 1
```
Cada conta de anúncios tem o seu próprio pixel, e é assim que o professor recomenda trabalhar.
Compartilhar um mesmo pixel entre contas diferentes é possível, mas não é o normal.

### U:54dea110daddeb21:020 — Copiar o código base do pixel no gerenciador
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: "fala+pdf:cst_m01_a05_pixel_e_api_de_conversoes.pdf"
faixa: "00:12:36–00:13:44"
perecivel: true
confianca: media
versao: 1
nota: "A transcrição embaralha os nomes das opções do menu durante a demonstração; o ponto firme é onde o código base é copiado."
```
No gerenciador, o caminho passa por fontes de dados, o pixel da Meta e a opção de configurar, onde existe a alternativa de adicionar o código manualmente.
Ali aparece um botão de copiar código e a tela mostra apenas o código base, não o código inteiro — para a instalação isso basta.

### U:54dea110daddeb21:021 — O pixel vai no head do site
```yaml
tipo: regra
plataforma: [geral]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: "fala+pdf:cst_m01_a05_pixel_e_api_de_conversoes.pdf"
faixa: "00:13:45–00:15:01"
perecivel: false
confianca: alta
versao: 1
```
Todo site é dividido em duas partes: head, a cabeça, e body, o corpo.
Instale o pixel no head, porque o pixel é o cérebro da conta de anúncios e cérebro vai na cabeça.
Onde exatamente fica o head não é assunto desta aula: basta guardar a regra.

### U:54dea110daddeb21:022 — Quatro formas de instalar o pixel
```yaml
tipo: conceito
plataforma: [meta, google]
tema: pixel-e-eventos
tarefas: []
fonte: "fala+pdf:cst_m01_a05_pixel_e_api_de_conversoes.pdf"
faixa: "00:15:01–00:18:06"
perecivel: true
confianca: baixa
versao: 1
nota: "O professor começa dizendo três maneiras, se corrige para quatro e depois observa que o Google Tag Manager está listado dentro da integração de parceiros, o que deixa a contagem ambígua. Ele demonstra no Meta e afirma que a mesma configuração aparece no pixel do Google Ads."
```
A aula descreve quatro caminhos: colar o código manualmente, usar a integração de parceiros, enviar instruções por e-mail e usar o gerenciador de tags do Google.
O gerenciador de tags aparece dentro da própria lista de parceiros, então a fronteira entre o segundo e o quarto caminho não é limpa.

### U:54dea110daddeb21:023 — Integração de parceiros no gerenciador
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: "fala+pdf:cst_m01_a05_pixel_e_api_de_conversoes.pdf"
faixa: "00:15:50–00:16:32"
perecivel: true
confianca: alta
versao: 1
```
Em adicionar eventos, nova integração, pixel da Meta, existe a opção de usar a integração de parceiros, que abre uma lista de plataformas de criação de site.
Ao escolher um parceiro, a tela entrega as instruções para conectar a conta daquela plataforma à conta de anúncios.
Antes de decidir o método, verifique se a ferramenta que construiu o site está nessa lista — Shopify, Magento, Shopline, WooCommerce, WordPress, Wix e Webflow são citadas.

### U:54dea110daddeb21:024 — Quando existe programador responsável, envie as instruções por e-mail
```yaml
tipo: decisao
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: "fala+pdf:cst_m01_a05_pixel_e_api_de_conversoes.pdf"
faixa: "00:16:32–00:17:16"
condicoes: "há webmaster, equipe de TI ou programador responsável pelo site"
perecivel: true
confianca: alta
versao: 1
```
Quando a instalação vai ser delegada a um webmaster, a alguém de TI ou ao responsável pelo site, use a opção de enviar instruções por e-mail.

### U:54dea110daddeb21:025 — Prefira sempre o Google Tag Manager
```yaml
tipo: regra
plataforma: [geral]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: "fala+pdf:cst_m01_a05_pixel_e_api_de_conversoes.pdf"
faixa: "00:17:16–00:18:07"
perecivel: false
confianca: alta
versao: 1
```
A recomendação do professor é instalar o pixel pelo Google Tag Manager; a instalação direta pelo parceiro, quando ele está na lista, é a outra boa opção.
O método manual às vezes é mais rápido, mas as duas alternativas acima deixam a instalação muito mais organizada.

### U:54dea110daddeb21:026 — Instalação de pixel e API fica no curso de Google Tag Manager
```yaml
tipo: limite
plataforma: [geral]
tema: pixel-e-eventos
tarefas: []
fonte: "fala+pdf:cst_m01_a05_pixel_e_api_de_conversoes.pdf"
faixa: "00:18:07–00:18:54"
perecivel: true
confianca: alta
versao: 1
```
Esta aula não ensina a usar o gerenciador de tags: o passo a passo de criação e instalação do pixel está no curso de Google Tag Manager da comunidade.
Esse mesmo curso cobre a instalação e a configuração da API de conversões, inclusive em e-commerce.

### U:54dea110daddeb21:027 — A API de conversões é um canal de comunicação melhor
```yaml
tipo: conceito
plataforma: [geral]
tema: pixel-e-eventos
tarefas: []
fonte: "fala+pdf:cst_m01_a05_pixel_e_api_de_conversoes.pdf"
faixa: "00:18:54–00:20:22"
perecivel: false
confianca: alta
versao: 1
```
O pixel é o informante dentro do site; a API de conversões é um novo canal de comunicação entre esse informante e a fonte de tráfego.
Sem a API, a comunicação funciona como um rádio de militar: dá conta do recado, mas é rudimentar e algumas informações se perdem no caminho.
Com a API, é como entregar ao pixel um celular com uma conexão que nunca cai para falar com a plataforma.

### U:54dea110daddeb21:028 — A API amplia as três funções do pixel
```yaml
tipo: conceito
plataforma: [geral]
tema: pixel-e-eventos
tarefas: []
fonte: "fala+pdf:cst_m01_a05_pixel_e_api_de_conversoes.pdf"
faixa: "00:20:26–00:21:16"
perecivel: false
confianca: alta
versao: 1
```
A API de conversões não substitui o pixel: ela aumenta o potencial das três funções dele.
Na prática, melhora as informações que chegam à fonte de tráfego, melhora o cérebro da conta de anúncios e melhora a criação de audiências.

### U:54dea110daddeb21:029 — Navegador e servidor: onde cada peça roda
```yaml
tipo: conceito
plataforma: [geral]
tema: pixel-e-eventos
tarefas: []
fonte: "fala+pdf:cst_m01_a05_pixel_e_api_de_conversoes.pdf"
faixa: "00:21:16–00:23:46"
perecivel: false
confianca: media
versao: 1
nota: "O professor assume que a explicação é simplificada e desenhada no bloco de notas; ele mesmo diz que um programador descreveria de outro jeito."
```
O usuário chega ao site por um navegador — Chrome, Safari, Edge, Firefox, Opera — e é no navegador que o pixel dispara e manda as informações para a fonte de tráfego.
Quem abastece o navegador de informações é o servidor.
A API de conversões fica no servidor, e não no navegador, e por isso é mais robusta do que o pixel sozinho.

### U:54dea110daddeb21:030 — Quando chegar a hora de instalar, vá ao curso de GTM e volte
```yaml
tipo: decisao
plataforma: [geral]
tema: fundamentos-e-carreira
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: "00:25:00–00:25:41"
perecivel: false
confianca: alta
versao: 1
```
Quando chegar o momento de instalar o pixel e a API de conversões, migre para o curso de Google Tag Manager, domine a habilidade e depois retome as aulas de tráfego pago na ordem.
Não antecipe esse desvio: o professor diz que quem sai da sequência antes da hora se perde, e que ele já viu isso acontecer muitas vezes.

### U:54dea110daddeb21:031 — Traqueamento é rastrear comportamento e origem
```yaml
tipo: conceito
plataforma: [geral]
tema: atribuicao
tarefas: []
fonte: "fala+pdf:cst_m01_a05_pixel_e_api_de_conversoes.pdf"
faixa: "00:25:41–00:26:14"
perecivel: false
confianca: alta
versao: 2
nota: "Triagem do módulo 001 (2026-09-14): proposta de tag recusada (tema: traqueamento); mantida a tag mais próxima."
```
Traquear é rastrear o comportamento do usuário e entender de onde ele veio.
Sem isso, quem recebe uma mensagem no WhatsApp não sabe se aquela pessoa pesquisou a marca no Google, viu um anúncio no Instagram ou no YouTube, nem de qual campanha e público ela saiu.

### U:54dea110daddeb21:032 — Não existe traqueamento perfeito
```yaml
tipo: regra
plataforma: [geral]
tema: atribuicao
tarefas: [ler-metricas-e-relatorios]
fonte: "fala+pdf:cst_m01_a05_pixel_e_api_de_conversoes.pdf"
faixa: "00:26:14–00:26:51"
perecivel: false
confianca: alta
versao: 1
```
Entre no assunto sabendo que traqueamento perfeito não existe; quem espera rastrear cada pessoa vai se frustrar.
Ainda assim, há maneiras de identificar boa parte das pessoas e do caminho que elas fizeram até a empresa.

### U:54dea110daddeb21:033 — Pixel e API são a base do traqueamento
```yaml
tipo: regra
plataforma: [geral]
tema: atribuicao
tarefas: [instalar-pixel-e-eventos, ler-metricas-e-relatorios]
fonte: "fala+pdf:cst_m01_a05_pixel_e_api_de_conversoes.pdf"
faixa: "00:26:51–00:27:35"
perecivel: false
confianca: alta
versao: 1
```
A primeira ferramenta de traqueamento é o próprio pixel somado à API de conversões, porque são eles que informam à fonte de tráfego o que acontece no site.
Com essa informação chegando, dá para ver qual anúncio, qual público e qual campanha geraram cada compra e medir o retorno do investimento.

### U:54dea110daddeb21:034 — Google Analytics e UTMs completam o traqueamento
```yaml
tipo: regra
plataforma: [geral]
tema: atribuicao
tarefas: [ler-metricas-e-relatorios]
fonte: "fala+pdf:cst_m01_a05_pixel_e_api_de_conversoes.pdf"
faixa: "00:27:35–00:28:58"
perecivel: false
confianca: alta
versao: 1
```
Além do pixel e da API, use o Google Analytics com UTMs, que são os parâmetros de acompanhamento.
O Analytics serve para interpretar e identificar o que o usuário faz dentro do site; a UTM é o recurso que marca de onde ele chegou.
É essa dupla que a empresa do professor usa na operação do dia a dia.

### U:54dea110daddeb21:035 — Analytics e UTMs têm curso próprio na comunidade
```yaml
tipo: limite
plataforma: [geral]
tema: atribuicao
tarefas: []
fonte: "fala+pdf:cst_m01_a05_pixel_e_api_de_conversoes.pdf"
faixa: "00:28:17–00:28:58"
perecivel: true
confianca: alta
versao: 1
```
Esta aula não ensina Google Analytics nem UTMs: existe um curso específico na comunidade que cobre toda essa parte de traqueamento.

### U:54dea110daddeb21:036 — Página isolada por fonte com carimbo no CRM
```yaml
tipo: procedimento
plataforma: [geral]
tema: atribuicao
tarefas: [ler-metricas-e-relatorios]
fonte: "fala+pdf:cst_m01_a05_pixel_e_api_de_conversoes.pdf"
faixa: "00:28:58–00:31:10"
perecivel: false
confianca: alta
versao: 2
nota: "Triagem do módulo 001 (2026-09-14): proposta de tag recusada (tarefa: configurar-traqueamento); mantida a tag mais próxima."
```
Pré-condição: poder criar páginas separadas no site e ter uma ferramenta de e-mail (CRM) recebendo os cadastros.
1. Crie uma página de captura por fonte de tráfego, com o nome da fonte no endereço (por exemplo, aulas-meta e aulas-pesquisa).
2. Divulgue cada endereço apenas nos anúncios da fonte correspondente.
3. Configure a página para aplicar uma etiqueta no contato que se cadastra ali, com o nome da fonte.
4. Leia os cadastros por etiqueta no CRM para saber de onde veio cada pessoa.
O professor classifica o método como rudimentar e diz que funciona muito bem.

### U:54dea110daddeb21:037 — Quando quiser separar por temperatura de público, prefira Analytics e UTMs
```yaml
tipo: decisao
plataforma: [geral]
tema: atribuicao
tarefas: [ler-metricas-e-relatorios]
fonte: fala
faixa: "00:31:10–00:31:50"
perecivel: false
confianca: alta
versao: 1
```
Quando a ideia for desdobrar as páginas isoladas por temperatura de público, criando um endereço para o frio e outro para o quente, saiba que isso dá muito mais trabalho.
O professor diz que o efeito é muito parecido usando Google Analytics e UTMs, que é o caminho adotado na empresa dele.

### U:54dea110daddeb21:038 — Quando o cliente é negócio local, use um WhatsApp só do tráfego pago
```yaml
tipo: decisao
plataforma: [geral]
tema: atribuicao
tarefas: [ler-metricas-e-relatorios]
fonte: "fala+pdf:cst_m01_a05_pixel_e_api_de_conversoes.pdf"
faixa: "00:31:50–00:33:05"
condicoes: cliente é negócio local com atendimento por WhatsApp
perecivel: false
confianca: alta
versao: 2
nota: "Triagem do módulo 001 (2026-09-14): proposta de tag recusada (tarefa: configurar-traqueamento); mantida a tag mais próxima."
```
Quando o negócio local concentra tudo em um número de WhatsApp, chegam ali cliente de aplicativo de entrega, quem achou a empresa organicamente, cliente antigo e quem veio dos anúncios, sem distinção.
Nesse caso, crie um canal de venda exclusivo do tráfego pago — um WhatsApp separado — para saber que todo contato daquele número veio da campanha.

### U:54dea110daddeb21:039 — Pergunte ao cliente final como ele conheceu a empresa
```yaml
tipo: regra
plataforma: [geral]
tema: atribuicao
tarefas: [ler-metricas-e-relatorios]
fonte: "fala+pdf:cst_m01_a05_pixel_e_api_de_conversoes.pdf"
faixa: "00:33:06–00:33:35"
perecivel: false
confianca: alta
versao: 1
```
O método mais rudimentar de todos continua valendo: pergunte a quem compra onde ele conheceu a empresa.
A resposta costuma vir com a fonte nomeada, como anúncio no Instagram ou anúncio no Google.

### U:54dea110daddeb21:040 — Lista de compradores com nome, e-mail, telefone e valor
```yaml
tipo: regra
plataforma: [geral]
tema: atribuicao
tarefas: [ler-metricas-e-relatorios]
fonte: "fala+pdf:cst_m01_a05_pixel_e_api_de_conversoes.pdf"
faixa: "00:33:35–00:34:13"
perecivel: false
confianca: alta
versao: 2
nota: "Triagem do módulo 001 (2026-09-14): proposta de tag recusada (tarefa: configurar-traqueamento); mantida a tag mais próxima."
```
Monte, principalmente em negócio local, uma lista das pessoas que compraram, com nome, e-mail, telefone e valor da compra.
Ela resolve o caso de quem viu o anúncio pela internet e fechou a compra dentro do estabelecimento.

### U:54dea110daddeb21:041 — Lista enviada ao pixel barateia a aquisição
```yaml
tipo: conceito
plataforma: [geral]
tema: pixel-e-eventos
tarefas: []
fonte: "fala+pdf:cst_m01_a05_pixel_e_api_de_conversoes.pdf"
faixa: "00:34:13–00:34:51"
perecivel: false
confianca: alta
versao: 1
```
A lista de compradores pode ser enviada ao pixel, levando à fonte de tráfego as informações daquelas compras.
Com o cérebro da conta melhor alimentado, o pixel encontra clientes parecidos por um preço mais barato e os anúncios performam melhor.

### U:54dea110daddeb21:042 — Explique ao dono do negócio por que pedir a lista
```yaml
tipo: regra
plataforma: [geral]
tema: fundamentos-e-carreira
tarefas: [ler-metricas-e-relatorios]
fonte: "fala+pdf:cst_m01_a05_pixel_e_api_de_conversoes.pdf"
faixa: "00:34:13–00:34:51"
perecivel: false
confianca: alta
versao: 1
```
O dono do negócio não vai gostar do pedido se ele chegar seco, como mais uma tarefa.
Explique antes o motivo estratégico: a lista alimenta o pixel, os anúncios passam a performar melhor e o esforço volta em venda.

### U:54dea110daddeb21:043 — Conversões offline ficam para outra aula
```yaml
tipo: limite
plataforma: [geral]
tema: pixel-e-eventos
tarefas: []
fonte: fala
faixa: "00:34:13–00:34:51"
perecivel: false
confianca: alta
versao: 1
```
Esta aula não mostra como enviar a lista de compradores para o pixel: o professor remete a uma aula posterior sobre conversões offline e a uma live da comunidade.

### U:54dea110daddeb21:044 — Importa saber o tamanho da imperfeição
```yaml
tipo: regra
plataforma: [geral]
tema: atribuicao
tarefas: [ler-metricas-e-relatorios]
fonte: "fala+pdf:cst_m01_a05_pixel_e_api_de_conversoes.pdf"
faixa: "00:34:51–00:35:37"
perecivel: false
confianca: alta
versao: 1
```
Parte dos dados vai se perder no mapeamento, e isso é esperado.
O objetivo não é ter o traqueamento perfeito, e sim saber o quanto ele é imperfeito naquele negócio.

### U:54dea110daddeb21:045 — Espere uma quebra de 20% entre o painel e o real
```yaml
tipo: regua
plataforma: [geral]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: "fala+pdf:cst_m01_a05_pixel_e_api_de_conversoes.pdf"
faixa: "00:35:37–00:36:17"
perecivel: false
confianca: alta
versao: 1
nota: "Na fala a quebra pode ser para mais ou para menos; o PDF descreve apenas uma queda de 20% em relação ao valor real."
```
Ao analisar os dados, conte com uma quebra de cerca de 20% em relação ao valor real.
Se a plataforma informa R$ 100 mil faturados, o real pode ser R$ 80 mil; se informa R$ 80 mil, o real pode ser R$ 96 mil.
O tamanho e o sentido dessa quebra mudam de negócio para negócio.

### U:54dea110daddeb21:046 — Descobrir a quebra comparando com a ferramenta de recebimento
```yaml
tipo: procedimento
plataforma: [geral]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: "fala+pdf:cst_m01_a05_pixel_e_api_de_conversoes.pdf"
faixa: "00:36:17–00:36:52"
perecivel: false
confianca: alta
versao: 1
```
Pré-condição: acesso à ferramenta que recebe o dinheiro do cliente, seja a plataforma do e-commerce ou a de infoproduto.
1. Anote o resultado que cada fonte de tráfego informa no período (Meta Ads, Google Ads, TikTok Ads).
2. Levante o faturamento na ferramenta de recebimento, que é o dado final: o dinheiro que entrou na conta.
3. Compare os dois números e registre a diferença como a quebra daquele negócio.
4. Repita a conta por cliente, porque a quebra varia de negócio para negócio.

### U:54dea110daddeb21:047 — O conjunto que o professor considera suficiente
```yaml
tipo: regra
plataforma: [geral]
tema: atribuicao
tarefas: [instalar-pixel-e-eventos, ler-metricas-e-relatorios]
fonte: fala
faixa: "00:36:52–00:37:27"
perecivel: false
confianca: alta
versao: 1
```
Com pixel e API de conversões bem instalados via Google Tag Manager, mais Google Analytics e UTMs configuradas, o traqueamento já está resolvido para a maioria dos casos.
Para situações específicas, acrescente página isolada por fonte, canal de venda exclusivo, a pergunta ao cliente e a lista de compradores.
O professor afirma que esse conjunto é mais do que o bastante.

### U:54dea110daddeb21:048 — Não existe ferramenta de traqueamento perfeito
```yaml
tipo: regra
plataforma: [geral]
tema: atribuicao
tarefas: [ler-metricas-e-relatorios]
fonte: "fala+pdf:cst_m01_a05_pixel_e_api_de_conversoes.pdf"
faixa: "00:37:27–00:37:51"
perecivel: false
confianca: alta
versao: 1
```
Desconfie de qualquer ferramenta vendida como solução de traqueamento perfeito, porque ela não existe.
O argumento do professor é que nenhuma empresa faz esse trabalho melhor que o Google, então confie nos dados do Google Analytics.

### U:54dea110daddeb21:049 — Métricas ficam para a próxima aula
```yaml
tipo: limite
plataforma: [geral]
tema: metricas-e-relatorios
tarefas: []
fonte: fala
faixa: "00:37:27–00:37:51"
perecivel: false
confianca: alta
versao: 1
```
A aula fecha em pixel, API de conversões e traqueamento; quais métricas rastrear e como lê-las é assunto da aula seguinte.
