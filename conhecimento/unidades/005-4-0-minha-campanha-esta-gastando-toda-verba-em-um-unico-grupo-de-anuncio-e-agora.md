---
type: unidades-aula
status: ouro
title: "4.0 - Minha campanha está gastando toda verba em um único grupo de anúncio - e agora"
modulo: "005"
ordem: 84
aula_id: 869445a4c64befbf
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - transcricao.md
extraido_em: 2026-09-13
gerado_por: fable-5.1
retiradas: []
divisoes: []
fusoes: []
---

# 4.0 - Minha campanha está gastando toda verba em um único grupo de anúncio - e agora

## Contexto da aula
Aula de diagnóstico do módulo de YouTube: a campanha de vídeo concentra todo o gasto em um único grupo de anúncio (no exemplo, o público frio "sites e plataformas") e os públicos quentes não gastam.
O professor apresenta três diagnósticos possíveis e três soluções em escalada, aplicadas ao vivo numa campanha com lance manual de CPV máximo.
A mensagem central é que concentração de verba não é necessariamente um problema; é problema quando o gestor não decidiu conscientemente que está tudo bem.
Sem PDF; toda a aula é fala sobre a tela do Google Ads.

## Unidades

### U:869445a4c64befbf:001 — O Google concentra gasto onde a ação valorizada sai mais barata
```yaml
tipo: conceito
plataforma: [youtube, google]
tema: leilao-e-lances
tarefas: [diagnosticar-concentracao-de-verba]
fonte: fala
faixa: 00:00:38–00:01:19
perecivel: false
confianca: alta
versao: 1
```
O Google é treinado para achar oportunidades baratas da ação que o lance pede (com CPV máximo, visualizações).
Num público de milhões de pessoas é muito mais fácil achar visualização barata do que num público restrito de canais, por isso a verba escorre para o grupo mais amplo.

### U:869445a4c64befbf:002 — Se há público quente e frio na mesma campanha, o frio come a verba
```yaml
tipo: decisao
plataforma: [youtube]
tema: otimizacao
tarefas: [diagnosticar-concentracao-de-verba]
fonte: fala
faixa: "00:01:30–00:02:19"
perecivel: false
confianca: alta
versao: 2
```
Se o grupo que concentra o gasto tem audiência muito maior que os outros, o diagnóstico é público amplo demais (diagnóstico 1).
Quando isso acontece, quase sempre é porque públicos quentes e frios estão na mesma campanha: o gasto vai todo para o frio e os quentes ficam sem verba.

### U:869445a4c64befbf:003 — Se todos os públicos são quentes e um menor concentra, ele entrega a ação
```yaml
tipo: decisao
plataforma: [youtube]
tema: otimizacao
tarefas: [diagnosticar-concentracao-de-verba]
fonte: fala
faixa: "00:02:19–00:03:27"
perecivel: false
confianca: alta
versao: 2
```
Se a campanha só tem públicos quentes e o gasto se concentra num grupo até menor que os outros (ex.: "envolvimento completo 60 dias" gastando tudo enquanto "canais" e "cadastrados nas aulas ao vivo" não gastam), o diagnóstico é resultado (diagnóstico 2).
O Google encontrou ali muita gente completando a ação que a estratégia de lance valoriza; o lance diz ao Google qual resultado você quer, e ele gasta tudo onde o encontra.

### U:869445a4c64befbf:004 — Não pause o grupo que concentra o gasto e traz o resultado
```yaml
tipo: regra
plataforma: [youtube]
tema: otimizacao
tarefas: [diagnosticar-concentracao-de-verba, otimizar-publicos-e-segmentacoes]
fonte: fala
faixa: "00:03:27–00:04:01"
perecivel: false
confianca: alta
versao: 2
```
Pausar o conjunto que gasta tudo e traz todo o resultado é pausar o público que sustenta a campanha; a campanha piora.
Concentração com resultado não é motivo para pausa.

### U:869445a4c64befbf:005 — Se as metas diárias estão sendo atingidas, a concentração não é o problema
```yaml
tipo: decisao
plataforma: [youtube]
tema: otimizacao
tarefas: [diagnosticar-concentracao-de-verba]
fonte: fala
faixa: "00:04:01–00:04:36"
perecivel: false
confianca: alta
versao: 2
```
Se a campanha entrega a quantidade de visualizações ou de conversões por dia que você queria, não se preocupe com o grupo que não gasta; não é o maior problema.
Se não entrega, aí vale aplicar as soluções.

### U:869445a4c64befbf:006 — Se um grupo tem lance muito maior, ele ganha mais leilões e concentra
```yaml
tipo: decisao
plataforma: [youtube]
tema: leilao-e-lances
tarefas: [diagnosticar-concentracao-de-verba, otimizar-lances]
fonte: fala
faixa: "00:04:36–00:05:39"
perecivel: false
confianca: alta
versao: 2
```
Se um grupo de anúncio tem lance muito acima dos demais (ex.: R$ 3 contra R$ 0,30 nos outros), é natural que ele gaste tudo: lance maior diz ao Google que você aceita pagar mais caro por aquelas pessoas, ganha mais leilões e gasta mais (diagnóstico 3).
Compare os lances entre grupos antes de qualquer outra ação; no exemplo da aula todos estavam iguais em R$ 0,30, então esse diagnóstico não se aplicava.

### U:869445a4c64befbf:007 — Solução 1: regular os lances entre os grupos
```yaml
tipo: procedimento
plataforma: [youtube]
tema: leilao-e-lances
tarefas: [diagnosticar-concentracao-de-verba, otimizar-lances]
fonte: fala
faixa: "00:05:47–00:08:16"
perecivel: false
confianca: alta
versao: 2
```
Pré-condição: campanha com lance manual por grupo de anúncio (CPV máximo) e leitura do gasto e do custo real por grupo.
1. No grupo que concentra o gasto, reduza o lance; o quanto (metade, 30%, alguns centavos) vem do feeling, a lógica é que lance menor tende a gastar menos e a baratear o custo por visualização.
2. No grupo qualificado que gastou zero, aumente o lance com mais força (no exemplo, de R$ 0,30 para R$ 0,45).
3. Nos grupos qualificados que gastaram pouco, aumente um pouco (no exemplo, R$ 0,05 em cada), sinalizando ao Google que gaste neles.
4. Espere alguns dias e observe; só depois passe à solução 2.

### U:869445a4c64befbf:008 — Lance é sinal de quanto você aceita pagar; o custo real pode ser bem menor
```yaml
tipo: regua
plataforma: [youtube]
tema: leilao-e-lances
tarefas: [otimizar-lances]
fonte: fala
faixa: "00:06:24–00:07:34"
perecivel: false
confianca: alta
versao: 2
```
No exemplo, o lance era R$ 0,30 e o custo pago por visualização era R$ 0,05.
Baixar o lance até o custo real (R$ 0,05) é possível, mas provavelmente fica tão baixo que o Google não consegue gastar; ninguém tem certeza, então o professor testa R$ 0,05 em vez dos R$ 0,15 que ia colocar.

### U:869445a4c64befbf:009 — Ajuste de lances feito ao vivo na campanha de lives
```yaml
tipo: exemplo
plataforma: [youtube]
tema: leilao-e-lances
tarefas: [diagnosticar-concentracao-de-verba, otimizar-lances]
fonte: fala
faixa: 00:07:02–00:08:16
perecivel: false
confianca: alta
versao: 1
```
Situação: campanha de distribuição de lives com público frio "sites e plataformas" (lance R$ 0,30, pagando R$ 0,05 por view) gastando tudo, "cadastrados nas aulas ao vivo" zerado e outros públicos quentes gastando pouco.
O que aconteceu: o professor derrubou o lance do frio para R$ 0,05, subiu o do público zerado e muito qualificado para R$ 0,45 e deu R$ 0,05 a mais em cada um dos que gastaram pouco.
Lógica: reduzir onde concentra, aumentar mais onde não gastou nada e é qualificado, aumentar menos onde já gastou algo; depois esperar.

### U:869445a4c64befbf:010 — Solução 2: retirar as exclusões de público do grupo que não gasta
```yaml
tipo: procedimento
plataforma: [youtube]
tema: publicos
tarefas: [diagnosticar-concentracao-de-verba, organizar-hierarquia-e-exclusao-de-publicos]
fonte: fala
faixa: "00:08:16–00:08:53"
perecivel: true
confianca: alta
versao: 2
```
Pré-condição: a solução 1 já foi aplicada e o grupo seguiu sem gastar; o grupo usa as exclusões de público da hierarquia ensinada nas aulas anteriores.
1. Entre no grupo de anúncio que não gasta (ex.: "cadastrados nas aulas ao vivo").
2. Abra públicos-alvo e depois exclusões.
3. Remova a exclusão inserida ali, transformando o grupo num "00" (sem exclusões).
4. Deixe rodar e observe se o Google passa a gastar nele.

### U:869445a4c64befbf:011 — Uma solução por vez, com espera entre elas
```yaml
tipo: regra
plataforma: [youtube]
tema: otimizacao
tarefas: [diagnosticar-concentracao-de-verba, rodar-testes-e-experimentos]
fonte: fala
faixa: "00:08:53–00:09:35"
perecivel: false
confianca: alta
versao: 2
```
Aplique a solução 1, espere alguns dias e veja; se não resolver, aplique a 2; se ainda não resolver, a 3.
Tomar as três de uma vez impede saber qual funcionou.

### U:869445a4c64befbf:012 — Solução 3: isolar o grupo que concentra em campanha própria
```yaml
tipo: procedimento
plataforma: [youtube]
tema: estrutura-de-campanha
tarefas: [diagnosticar-concentracao-de-verba, otimizar-estruturas, definir-orcamento]
fonte: fala
faixa: "00:09:35–00:11:22"
perecivel: false
confianca: alta
versao: 2
```
Pré-condição: soluções 1 e 2 aplicadas sem efeito, ou pressa em resolver; normalmente o caso é quente e frio na mesma campanha.
1. Crie uma segunda campanha com o mesmo nome e o sufixo do tipo de público (ex.: "conteúdo em feed quente distribuição das lives" e "conteúdo em feed frio distribuição das lives").
2. Mova o grupo que concentra (o frio, "sites e plataformas") para a campanha fria; deixe os quentes ("canais", "envolvimento completo 60D", "cadastrados nas lives") na quente.
3. Defina orçamento por campanha (no exemplo, R$ 10 por dia em cada), garantindo o gasto nos dois blocos.
4. Adicione pelo menos mais um público frio na campanha fria (palavras-chave, interesses ou afinidade) para o Google dividir a verba e você comparar.

### U:869445a4c64befbf:013 — Nunca deixe uma campanha com um único público
```yaml
tipo: regra
plataforma: [youtube]
tema: estrutura-de-campanha
tarefas: [definir-estrutura-de-campanha, otimizar-estruturas]
fonte: fala
faixa: "00:11:22–00:11:56"
perecivel: false
confianca: alta
versao: 2
```
Campanha com um só grupo de anúncio não permite comparar qual público funciona melhor.
Ao criar campanha nova, coloque pelo menos dois públicos para o Google dividir a verba entre eles.

### U:869445a4c64befbf:014 — Concentração só é problema quando você não decidiu que está tudo bem
```yaml
tipo: regra
plataforma: [youtube]
tema: otimizacao
tarefas: [diagnosticar-concentracao-de-verba]
fonte: fala
faixa: "00:11:57–00:13:07"
perecivel: false
confianca: alta
versao: 2
```
Gastar tudo num público frio não é, por si, um problema; o problema é não ter consciência disso nem ter decidido que está tudo bem.
Se a concentração trouxesse as visualizações ou conversões desejadas (ex.: tudo no "envolvimento completo 60 dias"), o professor não tomaria medida drástica; cabe ao gestor dizer quando é problema, saber diagnosticar e ter as soluções à mão.

### U:869445a4c64befbf:015 — Se há pressa, vá direto à solução 3
```yaml
tipo: decisao
plataforma: [youtube]
tema: otimizacao
tarefas: [diagnosticar-concentracao-de-verba, otimizar-estruturas]
fonte: fala
faixa: "00:13:07–00:13:51"
perecivel: false
confianca: alta
versao: 2
```
Se você tem pressa para resolver, pule a escalada: isole os grupos em campanha de público quente e campanha de público frio e o problema acaba.
Se não tem pressa, tente manter tudo numa campanha só: regule lances, depois retire exclusões, e só então isole.

### U:869445a4c64befbf:016 — Nomenclatura dos grupos por temperatura (00, 01, 02)
```yaml
tipo: regra
plataforma: [youtube]
tema: nomenclatura
tarefas: [nomear-campanhas]
fonte: fala
faixa: "00:10:24–00:11:22"
perecivel: false
confianca: media
versao: 2
nota: A aula só cita os prefixos ao ler a tela; a regra completa vem das aulas anteriores do módulo. Confirmar na consolidação do tema nomenclatura.
```
Os grupos aparecem com prefixo numérico por temperatura e hierarquia de exclusão: "00" para públicos quentes sem exclusão (canais, envolvimento completo 60D), "01" para o quente seguinte (cadastrados nas lives) e "02" para o frio de segmento personalizado (sites e plataformas).
O prefixo se mantém mesmo quando o grupo muda de campanha.

### U:869445a4c64befbf:017 — O que esta aula não define
```yaml
tipo: limite
plataforma: [youtube]
tema: otimizacao
tarefas: []
fonte: fala
faixa: "00:05:47–00:13:51"
perecivel: false
confianca: alta
versao: 2
```
A aula não fixa quanto reduzir ou aumentar o lance ("você vai pegar o feeling") nem quantos dias esperar entre soluções ("uns dias").
Demonstra numa campanha de YouTube com lance manual de CPV máximo; outras redes do Google, lances automáticos e Meta Ads não aparecem.

