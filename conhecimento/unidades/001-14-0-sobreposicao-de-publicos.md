---
type: unidades-aula
status: validado
title: "14.0 - Sobreposição de públicos"
modulo: "001"
ordem: 18
aula_id: 518268cbf4025351
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - cst_m01_a14_sobreposicao_de_publicos.pdf
  - transcricao.md
extraido_em: 2026-09-14
gerado_por: opus-5
retiradas: []
divisoes: []
fusoes: []
---

# 14.0 - Sobreposição de públicos

## Contexto da aula

Aula de princípios do módulo de fundamentos: apresenta o conceito de sobreposição de públicos, por que
ela atrapalha, quando ela não é problema e as três formas de evitá-la.
Assume que o aluno já conhece a estrutura campanha / conjunto de anúncios / anúncio e a divisão entre
públicos quentes e frios.
O professor apresenta o sistema de exclusão hierárquica como organização criada por ele e mostra de
relance uma campanha própria só para ilustrar a ordem dos conjuntos.
A configuração da exclusão dentro do gerenciador de anúncios fica para os módulos práticos e para os de
e-commerce, lançamento e negócio local; ele pede que o aluno entenda o conceito e não aplique ainda.

## Unidades

### U:518268cbf4025351:001 — Onde o público mora na estrutura da campanha
```yaml
tipo: conceito
plataforma: [meta, google]
tema: estrutura-de-campanha
tarefas: []
fonte: "fala+pdf:cst_m01_a14_sobreposicao_de_publicos.pdf"
faixa: "00:00:00–00:01:42"
perecivel: false
confianca: alta
versao: 1
```
Na campanha ficam o objetivo, o orçamento e as configurações gerais; em cada conjunto (ou grupo) de anúncios fica normalmente um público; no anúncio fica o que está sendo anunciado.
O público é, portanto, um atributo do conjunto, não da campanha: uma campanha com vários conjuntos é uma campanha com vários públicos diferentes rodando ao mesmo tempo.
Essa mesma divisão vale tanto dentro do Facebook quanto dentro do Google.

### U:518268cbf4025351:002 — O que é sobreposição de públicos
```yaml
tipo: conceito
plataforma: [geral]
tema: publicos
tarefas: []
fonte: "fala+pdf:cst_m01_a14_sobreposicao_de_publicos.pdf"
faixa: "00:00:33–00:02:11"
perecivel: false
confianca: alta
versao: 1
```
Sobreposição de públicos é a mesma pessoa pertencer a mais de um dos públicos que você está usando em conjuntos de anúncios diferentes.
Como cada conjunto tem seu próprio público e eles não se conhecem, essa pessoa pode ser alcançada uma vez por cada conjunto em que ela se encaixa.
Isso vale em qualquer fonte de tráfego onde você monte vários conjuntos com públicos distintos.

### U:518268cbf4025351:003 — O Joaquim que cabe em três públicos ao mesmo tempo
```yaml
tipo: exemplo
plataforma: [geral]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos]
fonte: "fala+pdf:cst_m01_a14_sobreposicao_de_publicos.pdf"
faixa: "00:01:43–00:03:34"
perecivel: false
confianca: alta
versao: 1
```
Situação: uma campanha com três conjuntos, cada um com um público — interesse em empreendedorismo, donos de restaurante e quem quer aprender idiomas.
O que aconteceu: Joaquim é dono de restaurante, empreendeu e estuda inglês, então ele está dentro dos três públicos e o anunciante paga três vezes para aparecer para ele.
Lógica: públicos montados por critérios diferentes podem descrever a mesma pessoa; some os critérios antes de assumir que cada conjunto fala com gente nova.

### U:518268cbf4025351:004 — Sobreposição proposital é boa; desproposital é ruim
```yaml
tipo: decisao
plataforma: [geral]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos]
fonte: "fala+pdf:cst_m01_a14_sobreposicao_de_publicos.pdf"
faixa: "00:02:55–00:03:34"
perecivel: false
confianca: alta
versao: 1
```
Quando você sabe o que está fazendo e escolheu ter sobreposição, ela pode ser boa.
Quando ela aparece sem você ter decidido, é ruim, porque você perdeu o controle de para onde o investimento está indo.
O critério não é a sobreposição em si: é saber que ela existe e ter escolhido conviver com ela.

### U:518268cbf4025351:005 — Motivo 1: perda de controle da frequência
```yaml
tipo: conceito
plataforma: [meta, google]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos]
fonte: "fala+pdf:cst_m01_a14_sobreposicao_de_publicos.pdf"
faixa: "00:03:35–00:04:08"
perecivel: false
confianca: alta
versao: 1
```
O primeiro motivo para evitar sobreposição é não perder o controle de quantas vezes a mesma pessoa vê seu anúncio.
Quando alguém é impactado por um conjunto e não converte, a plataforma tende a parar de mostrar o anúncio para essa pessoa naquele conjunto — mas o conjunto seguinte não tem essa informação e mostra de novo, e o terceiro repete.
O resultado é uma frequência que você não definiu e não consegue ler.

### U:518268cbf4025351:006 — Motivo 2: você concorre com você mesmo no leilão
```yaml
tipo: conceito
plataforma: [meta, google]
tema: leilao-e-lances
tarefas: [organizar-hierarquia-e-exclusao-de-publicos]
fonte: "fala+pdf:cst_m01_a14_sobreposicao_de_publicos.pdf"
faixa: "00:04:08–00:04:38"
perecivel: false
confianca: alta
versao: 1
```
Com a mesma pessoa em conjuntos diferentes, cada conjunto entra em um leilão próprio para alcançá-la, e você acaba disputando contra si mesmo.
O professor classifica esse motivo como menor que a perda de controle da frequência, mas ainda assim como razão para evitar a sobreposição.
Vale mesmo quando o anúncio dos dois conjuntos é o mesmo.

### U:518268cbf4025351:007 — A aula não explica a janela de aparição
```yaml
tipo: limite
plataforma: [meta]
tema: publicos
tarefas: []
fonte: fala
faixa: "00:04:38–00:06:04"
perecivel: true
confianca: alta
versao: 1
```
Em aulas antigas o professor ensinava uma "janela de aparição" — intervalo mínimo entre duas aparições do mesmo anunciante para a mesma pessoa, com valores diferentes para Facebook, Instagram e Stories.
Nesta aula ele declara que não vai explicar esse mecanismo: reviu a documentação oficial das ferramentas e não reencontrou a informação, e o suporte respondeu que isso não acontece mais e que o mesmo anúncio pode aparecer várias vezes para a mesma pessoa.
Os motivos que ficam de pé para evitar sobreposição são o controle da frequência e a concorrência no leilão.

### U:518268cbf4025351:008 — Motivo 3: anúncio de etapa específica exige exclusão
```yaml
tipo: regra
plataforma: [meta, google]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos, montar-publicos-personalizados]
fonte: "fala+pdf:cst_m01_a14_sobreposicao_de_publicos.pdf"
faixa: "00:06:04–00:07:16"
perecivel: false
confianca: alta
versao: 1
```
Quando o anúncio fala com uma etapa específica da jornada, exclua as etapas seguintes do público.
No anúncio que lembra o item deixado no carrinho, exclua quem já comprou: quem comprou também adicionou ao carrinho e cairia no mesmo público.
Sem essa exclusão a mensagem chega errada para quem já avançou.

### U:518268cbf4025351:009 — A conta dos 120 carrinhos e das 50 compras
```yaml
tipo: exemplo
plataforma: [meta]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos]
fonte: fala
faixa: "00:06:51–00:07:57"
perecivel: false
confianca: alta
versao: 1
```
Situação: uma loja quer anunciar só para quem deixou produto no carrinho e não comprou.
O que aconteceu: o painel mostra 120 adições ao carrinho e 50 compras; as 50 compras estão dentro das 120 adições, então o público útil é o resto, 70 pessoas.
Lógica: faça essa subtração antes de montar o público, porque o público de etapa anterior sempre contém o da etapa seguinte.

### U:518268cbf4025351:010 — Públicos muito pequenos: não evite a sobreposição
```yaml
tipo: decisao
plataforma: [meta, google]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos]
fonte: "fala+pdf:cst_m01_a14_sobreposicao_de_publicos.pdf"
faixa: "00:07:58–00:08:38"
perecivel: false
confianca: alta
versao: 1
```
Quando suas segmentações já são muito pequenas, não se preocupe com a sobreposição.
Exemplos citados: uma lista de clientes curta, ou envolvimento de um dia com um perfil de Instagram recém-começado.
O risco é a exclusão deixar o público tão reduzido que não dê mais para anunciar para ele.

### U:518268cbf4025351:011 — Entre públicos frios, deixe a sobreposição existir
```yaml
tipo: regra
plataforma: [meta, google]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos, definir-segmentacao-demografica-e-interesses]
fonte: "fala+pdf:cst_m01_a14_sobreposicao_de_publicos.pdf"
faixa: "00:08:39–00:09:49"
perecivel: false
confianca: media
nota: "O professor se atrapalha na formulação e se corrige em seguida ('aliás, não evitando'); o sentido que fica é deixar a sobreposição entre frios."
versao: 1
```
Entre públicos frios não faça exclusão: deixe a sobreposição correr, porque o objetivo ali é que essas pessoas conheçam você e interajam.
O professor cita como frios os semelhantes, o direcionamento detalhado, os segmentos personalizados e o público-alvo de mercado.
Ele apresenta isso como direcionamento de resultado melhor para praticamente todo mundo, e diz que tirar a sobreposição entre frios é algo a testar só mais para frente.

### U:518268cbf4025351:012 — Campanha que não gasta: suspeite das exclusões
```yaml
tipo: decisao
plataforma: [meta, google]
tema: otimizacao
tarefas: [diagnosticar-campanha-sem-gasto, otimizar-publicos-e-segmentacoes]
fonte: "fala+pdf:cst_m01_a14_sobreposicao_de_publicos.pdf"
faixa: "00:09:49–00:11:02"
perecivel: false
confianca: alta
versao: 1
```
Se a campanha não está gastando dinheiro, não exclua público nenhum: evitar a sobreposição encolhe cada público, porque as pessoas que estavam em vários deles saem de todos menos um.
Encolhidos demais, os conjuntos param de entregar, e a própria exclusão vira a causa do não gasto.
A saída apontada é retirar o sistema de exclusões dessa campanha.

### U:518268cbf4025351:013 — Faixa de verba em que a sobreposição não importa
```yaml
tipo: regua
plataforma: [meta, google]
tema: orcamento
tarefas: [organizar-hierarquia-e-exclusao-de-publicos, definir-orcamento]
fonte: "fala+pdf:cst_m01_a14_sobreposicao_de_publicos.pdf"
faixa: "00:11:03–00:11:55"
condicoes: "verba diária entre R$ 5 e R$ 200"
perecivel: false
confianca: alta
versao: 1
```
Com verba entre R$ 5 e R$ 200 por dia, o professor não se preocuparia com sobreposição de públicos — e diz que essa é a situação da maioria das pessoas.
Acima de R$ 200 por dia, ou anunciando para públicos quentes, aí sim vale evitar.

### U:518268cbf4025351:014 — Com verba pequena, mantenha só a exclusão de etapa
```yaml
tipo: decisao
plataforma: [meta, google]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos]
fonte: fala
faixa: "00:11:09–00:11:55"
condicoes: "verba diária entre R$ 5 e R$ 200"
perecivel: false
confianca: alta
versao: 1
```
Se a verba é pequena, a única sobreposição que ainda vale tratar é a de anúncio feito para uma etapa específica.
Exemplo dado: um anúncio que você não quer que seus clientes vejam — nesse caso exclua os clientes das campanhas, mesmo sem montar hierarquia nenhuma.

### U:518268cbf4025351:015 — Sobreposição como teste deliberado
```yaml
tipo: regra
plataforma: [meta, google]
tema: testes-e-experimentos
tarefas: [rodar-testes-e-experimentos, otimizar-publicos-e-segmentacoes]
fonte: "fala+pdf:cst_m01_a14_sobreposicao_de_publicos.pdf"
faixa: "00:11:56–00:12:39"
perecivel: false
confianca: alta
versao: 1
```
Quando a intenção é testar a sobreposição, use-a à vontade: é um dos casos em que não se preocupar com ela é a decisão certa.
Sobreposição proposital aparece aqui como estratégia disponível, não como erro.

### U:518268cbf4025351:016 — O professor voltou a permitir sobreposição e melhorou
```yaml
tipo: exemplo
plataforma: [meta]
tema: testes-e-experimentos
tarefas: [rodar-testes-e-experimentos, otimizar-publicos-e-segmentacoes]
fonte: fala
faixa: "00:11:56–00:12:39"
perecivel: false
confianca: alta
versao: 1
```
Situação: campanhas do professor rodando com a sobreposição já eliminada entre os públicos.
O que aconteceu: ele reinseriu a sobreposição, deixou as campanhas voltarem a compartilhar pessoas entre os públicos e relata melhora nos resultados.
Lógica: eliminar sobreposição não é sempre ganho; testar o cenário oposto é um movimento válido de otimização.

### U:518268cbf4025351:017 — Sistema de exclusão (exclusão hierárquica)
```yaml
tipo: conceito
plataforma: [meta, google]
tema: publicos
tarefas: []
fonte: "fala+pdf:cst_m01_a14_sobreposicao_de_publicos.pdf"
faixa: "00:12:39–00:13:31"
perecivel: false
confianca: alta
versao: 1
```
Sistema de exclusão, também chamado de exclusão hierárquica ou hierarquia dos conjuntos de anúncios, é a primeira e principal forma de evitar sobreposição.
A regra que o define é simples: a cada novo público que entra na campanha, exclua dele os públicos anteriores.
O professor esclarece que não inventou a exclusão de públicos, e sim essa forma de organizá-la em hierarquia.

### U:518268cbf4025351:018 — Montar a escada de exclusões
```yaml
tipo: procedimento
plataforma: [meta, google]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos, definir-estrutura-de-campanha]
fonte: "fala+pdf:cst_m01_a14_sobreposicao_de_publicos.pdf"
faixa: "00:13:31–00:14:22"
perecivel: false
confianca: alta
versao: 1
```
Pré-condição: os públicos quentes da campanha já escolhidos e ordenados do melhor para o pior.
1. Coloque o melhor público no primeiro conjunto e não exclua nada dele.
2. No segundo conjunto, anuncie para o segundo público e exclua dele o primeiro.
3. No terceiro conjunto, exclua o segundo e o primeiro.
4. No quarto, exclua o terceiro, o segundo e o primeiro — e siga assim a cada público novo.
5. Repita até o último público quente da campanha.

### U:518268cbf4025351:019 — A notação da escada no material
```yaml
tipo: fato-material
plataforma: [meta, google]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos]
fonte: "pdf:cst_m01_a14_sobreposicao_de_publicos.pdf"
perecivel: false
confianca: alta
versao: 1
```
O material escreve a hierarquia em sete linhas, uma por conjunto: A; B menos A; C menos B e A; D menos C, B e A; e assim por diante até G, que exclui os seis anteriores.
Cada linha é um conjunto de anúncios, a letra da frente é o público daquele conjunto e as letras subtraídas são as exclusões aplicadas nele.
O material registra que essa escada é inteira de públicos quentes.

### U:518268cbf4025351:020 — Frios não se excluem entre si, mas excluem todos os quentes
```yaml
tipo: regra
plataforma: [meta, google]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos]
fonte: "fala+pdf:cst_m01_a14_sobreposicao_de_publicos.pdf"
faixa: "00:14:24–00:16:22"
perecivel: false
confianca: alta
versao: 1
```
A escada só vale entre os públicos quentes; quando a lista chega aos públicos frios, ela para de crescer.
Em cada conjunto de público frio, exclua todos os públicos quentes da campanha — e só eles — para garantir que ali você fale apenas com quem ainda não conhece o negócio.
Entre um público frio e outro não há exclusão nenhuma.

### U:518268cbf4025351:021 — Melhores e menores no topo, piores e maiores embaixo
```yaml
tipo: regra
plataforma: [meta, google]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos]
fonte: "fala+pdf:cst_m01_a14_sobreposicao_de_publicos.pdf"
faixa: "00:16:03–00:18:04"
perecivel: false
confianca: alta
versao: 1
```
O que define a ordem da hierarquia é a qualidade do público: os melhores ficam no topo e os piores embaixo.
Na prática, os melhores tendem a ser também os menores, e os piores os maiores.
Quem está mais abaixo é menos favorecido, porque chega ao conjunto já sem todas as pessoas retiradas pelos conjuntos acima.

### U:518268cbf4025351:022 — Nunca exclua um público maior de um menor
```yaml
tipo: regra
plataforma: [meta, google]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos]
fonte: "fala+pdf:cst_m01_a14_sobreposicao_de_publicos.pdf"
faixa: "00:16:24–00:17:19"
perecivel: false
confianca: alta
versao: 1
```
Um público que contém outro nunca pode ser excluído de dentro dele: isso zera o conjunto.
Por isso o público mais amplo jamais fica acima do mais restrito na hierarquia quando os dois vêm da mesma origem e mudam só a janela de dias.
Confira a relação de contenção entre dois públicos antes de decidir qual vem primeiro.

### U:518268cbf4025351:023 — Envolvimento 7 dias com o 365 dias excluído zera
```yaml
tipo: exemplo
plataforma: [meta]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos]
fonte: "fala+pdf:cst_m01_a14_sobreposicao_de_publicos.pdf"
faixa: "00:16:24–00:17:19"
perecivel: false
confianca: alta
versao: 1
```
Situação: a hierarquia coloca o envolvimento de 365 dias acima do envolvimento de 7 dias, e o conjunto de 7 dias exclui o de 365.
O que aconteceu: o conjunto fica com zero pessoas e não gasta, porque quem se envolveu na última semana também se envolveu no último ano.
Lógica: janelas maiores da mesma origem contêm as menores; a janela curta tem de vir antes da longa na hierarquia.

### U:518268cbf4025351:024 — Prefixo numérico nos nomes dos conjuntos marca a hierarquia
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: nomenclatura
tarefas: [nomear-campanhas, organizar-hierarquia-e-exclusao-de-publicos]
fonte: fala
faixa: "00:18:24–00:20:19"
perecivel: true
confianca: baixa
nota: "O professor perde a campanha no meio da demonstração e a explicação de qual público exclui qual fica truncada; só a existência do prefixo numérico está clara. Ele pede explicitamente que a campanha não seja copiada."
versao: 1
```
Na campanha que o professor abre, cada conjunto começa com um número de dois dígitos no nome: 00 para o melhor público, depois 01, 02, 03, 04.
O número indica a posição na hierarquia, então ao abrir a edição do conjunto 02 espera-se ver o conjunto 01 na lista de exclusões.
Ele avisa que a campanha aparece apenas para ilustrar a ordem e não deve ser copiada.

### U:518268cbf4025351:025 — Segunda forma: juntar os públicos no mesmo conjunto
```yaml
tipo: regra
plataforma: [meta, google]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos, definir-estrutura-de-campanha]
fonte: "fala+pdf:cst_m01_a14_sobreposicao_de_publicos.pdf"
faixa: "00:20:19–00:21:47"
perecivel: false
confianca: alta
versao: 1
```
Em vez de manter dois públicos que se sobrepõem em conjuntos separados, junte os dois em um único conjunto.
No exemplo da aula, interesse em empreendedorismo e donos de restaurante viram um só conjunto que alcança quem atende a qualquer um dos dois critérios.
Quem cabe nos dois entra uma vez só, porque a plataforma trata aquilo como um público único.

### U:518268cbf4025351:026 — Terceira forma: refinar o direcionamento por dados demográficos
```yaml
tipo: regra
plataforma: [meta, google]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses, organizar-hierarquia-e-exclusao-de-publicos]
fonte: "fala+pdf:cst_m01_a14_sobreposicao_de_publicos.pdf"
faixa: "00:21:03–00:22:41"
perecivel: false
confianca: alta
versao: 1
```
A terceira forma é usar refinadores demográficos que tornem impossível a mesma pessoa cair em dois conjuntos.
Exemplos da aula: um conjunto só para homens e outro só para mulheres; ou um conjunto com mais de 40 anos e outro de 20 a 39 anos.
Os refinadores citados são idade, gênero e localização, apontados como os mais precisos; o professor classifica essa forma como a menos utilizada das três.

### U:518268cbf4025351:027 — A configuração no gerenciador fica para outros módulos
```yaml
tipo: limite
plataforma: [meta, google]
tema: publicos
tarefas: []
fonte: "fala+pdf:cst_m01_a14_sobreposicao_de_publicos.pdf"
faixa: "00:23:15–00:24:28"
perecivel: false
confianca: alta
versao: 1
```
A aula cobre apenas o conceito de sobreposição e de exclusão de públicos; como aplicar a exclusão dentro do gerenciador de anúncios não é ensinado aqui.
O professor remete essa parte prática para as aulas de criação de campanha e para os módulos de e-commerce, rota dos lançamentos e tráfego para negócio local.
Ele pede que o aluno entenda o conceito agora e não tente executar ainda.
