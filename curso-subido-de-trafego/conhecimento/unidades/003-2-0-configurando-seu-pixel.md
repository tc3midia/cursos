---
type: unidades-aula
status: validado
title: "2.0 - Configurando seu Pixel"
modulo: "003"
ordem: 56
aula_id: c27d506b3f3b9659
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - cst_m03_a02_configurando_seu_pixel.pdf
  - transcricao.md
extraido_em: 2026-09-14
gerado_por: opus-5
retiradas: []
divisoes: []
fusoes: []
---

# 2.0 - Configurando seu Pixel

## Contexto da aula

Aula de configuração do rastreamento do Google Ads, feita logo depois que a conta de anúncios já está criada.
O professor percorre a criação de uma ação de conversão manual do início ao fim dentro do Google Ads, campo por campo: categoria, nome, valor, contagem, janelas e modelo de atribuição.
Explica antes a diferença entre os dois códigos do Google — a tag global do site e o código de conversão — e onde cada um precisa ficar no site.
No fim mostra onde recuperar os códigos, como conferir a instalação com uma extensão do Chrome e qual parte do código as plataformas de site costumam pedir.
Assume que o aluno já tem conta configurada e um site com página de captura e página de confirmação.
Não ensina a instalar o código no site: manda usar o Google Tag Manager (curso próprio na comunidade), a plataforma do site ou alguém de programação.

## Unidades

### U:c27d506b3f3b9659:001 — Caminho até conversões no Google Ads
```yaml
tipo: alerta-ui
plataforma: [google]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: "fala+pdf:cst_m03_a02_configurando_seu_pixel.pdf"
faixa: "00:00:00–00:00:25"
perecivel: true
confianca: alta
versao: 1
```
O pixel do Google Ads fica na aba superior, em "ferramentas e configurações"; é por esse menu que se acessa praticamente tudo na conta.
Dentro dele, a seção de medição traz "conversões" e "Google Analytics"; entre em conversões, porque a marcação do Analytics já vem da criação da conta.

### U:c27d506b3f3b9659:002 — Os dois códigos principais do Google
```yaml
tipo: conceito
plataforma: [google]
tema: pixel-e-eventos
tarefas: []
fonte: "fala+pdf:cst_m03_a02_configurando_seu_pixel.pdf"
faixa: "00:00:25–00:01:04"
perecivel: false
confianca: alta
versao: 1
```
O Google trabalha com dois códigos: a tag global do site (global site tag) e o código de conversão.
A tag global é o código que habilita o público de quem acessou as páginas do site.
O código de conversão é o que marca a ação que você quer contar como resultado.

### U:c27d506b3f3b9659:003 — Onde cada código entra no site
```yaml
tipo: regra
plataforma: [google]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: "fala+pdf:cst_m03_a02_configurando_seu_pixel.pdf"
faixa: "00:01:04–00:01:39"
perecivel: false
confianca: alta
versao: 1
```
Coloque a tag global em todas as páginas do site, sem exceção.
Coloque o código de conversão apenas nas páginas que confirmam que a pessoa converteu, como a página de agradecimento depois da compra.
Nessa página de confirmação convivem os dois códigos: a tag global mais o código de conversão.

### U:c27d506b3f3b9659:004 — Criar uma ação de conversão manual
```yaml
tipo: procedimento
plataforma: [google]
tema: pixel-e-eventos
tarefas: [definir-conversoes-e-metas, instalar-pixel-e-eventos]
fonte: "fala+pdf:cst_m03_a02_configurando_seu_pixel.pdf"
faixa: "00:01:39–00:02:33"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: estar na seção de conversões da conta do Google Ads, com o endereço do site em mãos.
1. Clique em "nova ação de conversão".
2. Escolha a origem "site" e informe o endereço para verificação.
3. Mande verificar e aguarde o retorno da ferramenta.
4. Ignore a sugestão automática de usar um carregamento de página como conversão.
5. Desça até o fim da página e escolha adicionar uma conversão manual utilizando o código.
6. A tela seguinte avisa que conversões criadas manualmente precisam ser incluídas no código do site e que as instruções vêm depois de concluir a criação.

### U:c27d506b3f3b9659:005 — Quem instala o código no site
```yaml
tipo: regra
plataforma: [google]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: "fala+pdf:cst_m03_a02_configurando_seu_pixel.pdf"
faixa: "00:02:33–00:03:08"
perecivel: false
confianca: alta
versao: 1
```
O caminho mais fácil de instalação é o Google Tag Manager, seguindo as aulas próprias da comunidade.
A alternativa é pedir a alguém que trabalhe com programação e instalação de códigos.
A operação em si é copiar e colar o código no site.

### U:c27d506b3f3b9659:006 — Categoria da conversão sai do objetivo
```yaml
tipo: decisao
plataforma: [google]
tema: pixel-e-eventos
tarefas: [definir-conversoes-e-metas]
fonte: "fala+pdf:cst_m03_a02_configurando_seu_pixel.pdf"
faixa: "00:02:33–00:03:08"
perecivel: false
confianca: alta
versao: 1
```
Se o que você quer é que a pessoa se cadastre em uma página para uma aula ao vivo, escolha na seção de otimização e meta a categoria de envio de formulário de lead ou de inscrição.
Defina o objetivo antes de abrir a lista de categorias, porque é ele que manda na escolha.
As demais opções de otimização dessa seção não precisam ser mexidas nessa primeira configuração.

### U:c27d506b3f3b9659:007 — Nome da conversão: objetivo mais identificador
```yaml
tipo: regra
plataforma: [google]
tema: nomenclatura
tarefas: [definir-conversoes-e-metas]
fonte: "fala+pdf:cst_m03_a02_configurando_seu_pixel.pdf"
faixa: "00:03:08–00:03:43"
perecivel: false
confianca: alta
versao: 2
nota: "triagem 003: nomenclatura de público e conversão coberta pela definição ampliada de nomear-campanhas"
```
No campo de nome da conversão, mantenha o objetivo e acrescente um identificador do que está sendo medido.
Exemplo do professor: "Inscrição - aula ao vivo".

### U:c27d506b3f3b9659:008 — Valor da conversão
```yaml
tipo: decisao
plataforma: [google]
tema: pixel-e-eventos
tarefas: [definir-conversoes-e-metas]
fonte: "fala+pdf:cst_m03_a02_configurando_seu_pixel.pdf"
faixa: "00:03:08–00:04:23"
perecivel: false
confianca: alta
versao: 1
```
Se todas as conversões valem o mesmo para o negócio, informe esse valor único; por exemplo, cada uma representando R$ 100,00 na conta.
Se cada conversão vale um valor diferente, informe pelo menos um valor padrão.
Quando a conversão é uma inscrição em aula ao vivo, o professor não atribui valor nenhum, mesmo a ferramenta sinalizando que não é o recomendado.

### U:c27d506b3f3b9659:009 — Valores dinâmicos ficam fora da aula
```yaml
tipo: limite
plataforma: [google]
tema: pixel-e-eventos
tarefas: []
fonte: "fala+pdf:cst_m03_a02_configurando_seu_pixel.pdf"
faixa: "00:03:44–00:04:23"
perecivel: false
confianca: alta
versao: 1
```
A aula não mostra como inserir valores diferentes por conversão no código de acompanhamento.
O professor aponta que a própria tela seguinte do Google traz essas orientações e que o assunto interessa a quem vai trabalhar com e-commerce.

### U:c27d506b3f3b9659:010 — O que é a contagem de conversões
```yaml
tipo: conceito
plataforma: [google]
tema: pixel-e-eventos
tarefas: []
fonte: "fala+pdf:cst_m03_a02_configurando_seu_pixel.pdf"
faixa: "00:04:23–00:04:59"
perecivel: false
confianca: alta
versao: 1
```
A contagem decide se as ações repetidas da mesma pessoa viram uma conversão ou várias.
Alguém que se cadastra cinco vezes no site pode ser contado como cinco conversões ou como uma; quem compra dez vezes no e-commerce, como dez compras ou como uma.

### U:c27d506b3f3b9659:011 — Escolher entre contar uma ou todas
```yaml
tipo: decisao
plataforma: [google]
tema: pixel-e-eventos
tarefas: [definir-conversoes-e-metas]
fonte: "fala+pdf:cst_m03_a02_configurando_seu_pixel.pdf"
faixa: "00:04:25–00:05:39"
perecivel: false
confianca: alta
versao: 1
```
Se você quer o dado batendo com as outras ferramentas, escolha contar uma; muita gente faz assim em cadastro de aula ao vivo.
O professor prefere contar todas, mesmo sabendo que isso gera discrepância: o mesmo cadastro repetido aparece uma vez só na ferramenta de e-mail e várias no Google Ads.

### U:c27d506b3f3b9659:012 — O que é a janela de conversão
```yaml
tipo: conceito
plataforma: [google]
tema: atribuicao
tarefas: []
fonte: "fala+pdf:cst_m03_a02_configurando_seu_pixel.pdf"
faixa: "00:04:59–00:06:19"
perecivel: false
confianca: media
versao: 1
nota: "Ao contar o exemplo o professor troca o prazo no meio da fala (começa em dez dias e segue com vinte); o PDF fixa o exemplo em dez dias. O período exato do exemplo não altera o conceito."
```
A janela de conversão é por quanto tempo a ferramenta continua lembrando que a pessoa clicou no anúncio.
A analogia do professor: o anúncio é um tapa na cara e a janela é o tempo que você leva para esquecer que levou o tapa.
Exemplo do prazo: alguém clica no anúncio em primeiro de janeiro, encontra o site por outro caminho dias depois e se cadastra; a janela decide se aquele clique leva o crédito.

### U:c27d506b3f3b9659:013 — Deixe a janela de conversão como veio
```yaml
tipo: regua
plataforma: [google]
tema: atribuicao
tarefas: [configurar-janela-de-atribuicao]
fonte: "fala+pdf:cst_m03_a02_configurando_seu_pixel.pdf"
faixa: "00:06:19–00:06:59"
condicoes: "primeiras configurações de conta"
perecivel: false
confianca: alta
versao: 1
```
Não mexa na janela de conversão no começo: mantenha os 30 dias que já vêm marcados.
É possível personalizar o prazo, por exemplo 20 dias, mas isso encurta o tempo em que os anúncios se lembram de quem clicou.
Só alongue quando o ciclo do negócio pedir: em venda de imóvel, em que o fechamento costuma levar 90 dias, faz sentido configurar esse prazo.

### U:c27d506b3f3b9659:014 — Janela de conversão de visualização engajada
```yaml
tipo: conceito
plataforma: [google]
tema: atribuicao
tarefas: []
fonte: "fala+pdf:cst_m03_a02_configurando_seu_pixel.pdf"
faixa: "00:06:59–00:07:38"
perecivel: false
confianca: alta
versao: 1
```
Funciona como a janela de conversão, só que a partir do engajamento com o vídeo: a pessoa assistiu inteiro, curtiu ou interagiu de alguma forma.
O prazo diz por quanto tempo depois desse engajamento a conversão ainda pode ser creditada ao anúncio; o professor mantém 30 dias.

### U:c27d506b3f3b9659:015 — Janela de conversão de visualização
```yaml
tipo: conceito
plataforma: [google]
tema: atribuicao
tarefas: []
fonte: "fala+pdf:cst_m03_a02_configurando_seu_pixel.pdf"
faixa: "00:06:59–00:07:38"
perecivel: false
confianca: alta
versao: 1
```
Aqui a pessoa não clicou: ela apenas viu o anúncio.
Se a conversão acontecer em até 24 horas depois dessa visualização — cadastro, compra ou o que for a conversão do negócio — o Google credita o resultado àquele anúncio.

### U:c27d506b3f3b9659:016 — O que o modelo de atribuição decide
```yaml
tipo: conceito
plataforma: [google]
tema: atribuicao
tarefas: []
fonte: "fala+pdf:cst_m03_a02_configurando_seu_pixel.pdf"
faixa: "00:07:38–00:08:19"
perecivel: false
confianca: media
versao: 1
nota: "O professor fala em 0,33 de conversão por anúncio no modelo linear; o PDF escreve 0,33%. A fala é o número coerente com a divisão de crédito entre três anúncios."
```
Quando a pessoa clica em vários anúncios antes de converter, o modelo de atribuição decide qual deles leva o crédito.
No último clique, o crédito é do último anúncio clicado; há também primeiro clique e linear, entre vários que o Google oferece.
No linear o crédito se reparte: com três anúncios no caminho, cada um fica responsável por 0,33 daquela conversão.

### U:c27d506b3f3b9659:017 — Último clique ou baseado em dados
```yaml
tipo: decisao
plataforma: [google]
tema: atribuicao
tarefas: [configurar-janela-de-atribuicao, definir-conversoes-e-metas]
fonte: "fala+pdf:cst_m03_a02_configurando_seu_pixel.pdf"
faixa: "00:08:19–00:09:17"
condicoes: "o modelo baseado em dados só fica disponível em conta com histórico suficiente"
perecivel: false
confianca: alta
versao: 1
```
Se for escolher modelo de atribuição, fique entre último clique e baseado em dados: para o professor são os dois que fazem sentido.
O modelo baseado em dados distribui o crédito pelo histórico da conta e só abre quando há dados suficientes, então entra no futuro, com a conta mais rodada.
Consultores e funcionários do Google recomendam muito o baseado em dados; o professor usa último clique e sugere testar o outro depois para ver se melhora os anúncios.

### U:c27d506b3f3b9659:018 — Primeira configuração vai de último clique
```yaml
tipo: regra
plataforma: [google]
tema: atribuicao
tarefas: [configurar-janela-de-atribuicao]
fonte: fala
faixa: "00:08:59–00:09:17"
condicoes: "conta nova, sem histórico de campanhas"
perecivel: false
confianca: alta
versao: 1
```
Na primeira configuração da conta, use o último clique: sem histórico, o modelo baseado em dados não está disponível.

### U:c27d506b3f3b9659:019 — Concluir a conversão e chegar às instruções
```yaml
tipo: procedimento
plataforma: [google]
tema: pixel-e-eventos
tarefas: [definir-conversoes-e-metas, instalar-pixel-e-eventos]
fonte: "fala+pdf:cst_m03_a02_configurando_seu_pixel.pdf"
faixa: "00:09:17–00:10:02"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: todos os campos da ação de conversão preenchidos.
1. Clique em "concluído" para fechar a configuração.
2. Confira a conversão que aparece listada.
3. Clique em "salvar e continuar" no fim da página.
4. A ferramenta leva para "ver instruções", onde dá para enviar as instruções por e-mail a outra pessoa ou editar o código do site.

### U:c27d506b3f3b9659:020 — A tag global tem um identificador único
```yaml
tipo: conceito
plataforma: [google]
tema: pixel-e-eventos
tarefas: []
fonte: "fala+pdf:cst_m03_a02_configurando_seu_pixel.pdf"
faixa: "00:09:20–00:10:39"
perecivel: false
confianca: alta
versao: 1
```
Ao escolher editar o código do site, o Google entrega a tag global com um identificador exclusivo daquela conta, começando por AW e seguido de uma sequência numérica.
Cada conta tem o seu; é esse número que aparece repetido também dentro do código de conversão.

### U:c27d506b3f3b9659:021 — Instalar a tag global em todas as páginas
```yaml
tipo: regra
plataforma: [google]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: "fala+pdf:cst_m03_a02_configurando_seu_pixel.pdf"
faixa: "00:10:02–00:10:39"
perecivel: false
confianca: alta
versao: 1
```
A tag global precisa estar em todas as páginas do site, sem deixar nenhuma de fora.
Em plataforma de e-commerce ou site com plugin de pixel, basta colar esse código no campo indicado e ele se espalha por todas as páginas.
Copie ou baixe o código para guardar nos seus arquivos; o Google Tag Manager também serve para distribuí-lo pelo site.

### U:c27d506b3f3b9659:022 — Onde pegar a tag do evento de conversão
```yaml
tipo: alerta-ui
plataforma: [google]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: "fala+pdf:cst_m03_a02_configurando_seu_pixel.pdf"
faixa: "00:10:39–00:11:21"
perecivel: true
confianca: alta
versao: 1
```
Na mesma tela de instruções, role até o fim e clique em "ver tag do evento" para abrir o código do evento de conversão.
Esse código vai apenas na página em que a pessoa completa a ação, como a página que confirma a inscrição.

### U:c27d506b3f3b9659:023 — Conferir as tags com o Tag Assistant
```yaml
tipo: procedimento
plataforma: [google]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: "fala+pdf:cst_m03_a02_configurando_seu_pixel.pdf"
faixa: "00:10:39–00:11:21"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: navegador Chrome e o site já com os códigos instalados.
1. Pesquise no Google por "Google Tag Assistant Legacy".
2. Instale a extensão no Chrome.
3. Abra a página do site que quer conferir e rode a extensão.
4. Leia o que ela lista: é assim que se verifica se as conversões estão instaladas naquela página.

### U:c27d506b3f3b9659:024 — Página de captura e página de confirmação
```yaml
tipo: exemplo
plataforma: [google]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: "fala+pdf:cst_m03_a02_configurando_seu_pixel.pdf"
faixa: "00:11:22–00:12:04"
perecivel: false
confianca: alta
versao: 1
```
Situação: o professor abre a própria página de captura e pergunta se ali precisa da tag de conversão.
O que aconteceu: na página de captura ele confirma que basta a tag global, ao lado de outras tags que tem no site; a tag de conversão não vai ali. Quando a pessoa preenche o e-mail e cai na página seguinte, ele sabe que houve conversão, e é nessa página que estão a tag global e a tag de conversão do Google Ads.
Lógica: a tag de conversão marca a página que prova o resultado, não a que apresenta a oferta.

### U:c27d506b3f3b9659:025 — Procure as instruções da sua plataforma de site
```yaml
tipo: regra
plataforma: [google]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: "fala+pdf:cst_m03_a02_configurando_seu_pixel.pdf"
faixa: "00:12:04–00:12:35"
perecivel: false
confianca: alta
versao: 1
```
Pode instalar direto no código do site, pelo Google Tag Manager ou com ajuda de quem trabalha com programação.
Para qualquer construtor de site ou plataforma de e-commerce, pesquise no Google como instalar a tag naquela ferramenta específica: todas publicam o passo a passo.

### U:c27d506b3f3b9659:026 — O rótulo da conversão é o trecho após a barra
```yaml
tipo: conceito
plataforma: [google]
tema: pixel-e-eventos
tarefas: []
fonte: "fala+pdf:cst_m03_a02_configurando_seu_pixel.pdf"
faixa: "00:12:35–00:13:55"
perecivel: false
confianca: alta
versao: 1
```
O código do evento traz duas informações: o identificador único da conta e o rótulo daquela conversão, que vem depois da barra.
Muitas plataformas de site e de e-commerce não pedem o código inteiro, só esse rótulo, que identifica qual conversão está sendo registrada.

### U:c27d506b3f3b9659:027 — Recuperar o código de uma conversão já criada
```yaml
tipo: procedimento
plataforma: [google]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: "fala+pdf:cst_m03_a02_configurando_seu_pixel.pdf"
faixa: "00:13:55–00:14:30"
perecivel: true
confianca: baixa
versao: 1
nota: "Fala e PDF divergem sobre qual das três opções escolher: o PDF manda escolher a última (gerenciador de tags), enquanto na fala o professor abre o gerenciador e em seguida diz que dá para instalar por conta própria. O caminho de menu é igual nos dois; a escolha final não fica clara."
```
Pré-condição: a ação de conversão já criada e salva na conta.
1. Vá até a página de resumo das conversões.
2. Clique sobre a conversão para abrir suas configurações, onde também dá para editar nome e demais campos.
3. Clique em "configurações da tag".
4. Escolha entre as três opções oferecidas: instalar por conta própria, enviar a tag por e-mail ou usar o gerenciador de tags do Google.
5. Instalando por conta própria, copie a tag global, que vai em todas as páginas, e o evento de conversão, que vai só na página da conversão e traz o rótulo.

### U:c27d506b3f3b9659:028 — Google Tag Manager é o caminho recomendado
```yaml
tipo: regra
plataforma: [google]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: "fala+pdf:cst_m03_a02_configurando_seu_pixel.pdf"
faixa: "00:15:13–00:15:47"
perecivel: false
confianca: alta
versao: 1
```
A recomendação do professor é usar o Google Tag Manager para gerenciar as tags do site.
O começo é um pouco complicado, mas depois de configurado não exige mais atenção.
Existe curso próprio sobre a ferramenta dentro da comunidade, com passo a passo, e dúvidas podem ser levadas para lá.

### U:c27d506b3f3b9659:029 — A instalação no site fica para outro curso
```yaml
tipo: limite
plataforma: [google]
tema: pixel-e-eventos
tarefas: []
fonte: "fala+pdf:cst_m03_a02_configurando_seu_pixel.pdf"
faixa: "00:15:13–00:15:47"
perecivel: false
confianca: alta
versao: 1
```
Esta aula cobre a criação da ação de conversão dentro do Google Ads e mostra onde ficam os códigos, mas não ensina a instalá-los no site.
O professor remete essa parte ao curso de Google Tag Manager da comunidade, à documentação da plataforma do site ou a um profissional de programação.
