---
type: unidades-aula
status: validado
title: "5.4 - Otimização de estruturas"
modulo: "005"
ordem: 90
aula_id: cd10f367f1715299
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - cst_m05_a54_otimizacao_de_estruturas.pdf
  - transcricao.md
extraido_em: 2026-09-16
gerado_por: gpt-5.6-terra
retiradas: []
divisoes: []
fusoes: []
---

# 5.4 - Otimização de estruturas

## Contexto da aula

A aula mostra ajustes de estrutura em campanhas de distribuição de conteúdo no YouTube.
Compara campanhas de vídeo In-Feed e In-Stream, apresentando estrutura igual e diferença na configuração do anúncio.
O foco é redistribuir grupos quando a verba se concentra e os lances não recuperam o controle desejado.
A demonstração separa públicos quentes e frios em campanhas distintas e reorganiza grupos de anúncios.

## Unidades

### U:cd10f367f1715299:001 — Estrutura de campanhas In-Feed e In-Stream
```yaml
tipo: conceito
plataforma: [youtube]
tema: estrutura-de-campanha
tarefas: []
fonte: "fala+pdf:cst_m05_a54_otimizacao_de_estruturas.pdf"
faixa: "00:00:00–00:00:38"
perecivel: false
confianca: alta
versao: 1
nota: "A fala situa as campanhas no YouTube; o PDF chama In-Feed de campanha que aparece em pesquisas e relacionados."
```

As campanhas In-Feed e In-Stream têm a mesma estrutura e o mesmo processo de criação no gerenciador.
A diferença indicada é o tipo e a configuração do anúncio.

### U:cd10f367f1715299:002 — Concentração de verba indica ajuste estrutural
```yaml
tipo: exemplo
plataforma: [youtube]
tema: estrutura-de-campanha
tarefas: [otimizar-estruturas, diagnosticar-concentracao-de-verba]
fonte: "fala+pdf:cst_m05_a54_otimizacao_de_estruturas.pdf"
faixa: "00:00:38–00:01:18"
perecivel: false
confianca: alta
versao: 1
nota: "O PDF usa o exemplo de R$ 200 gastos em um conjunto; a fala demonstra R$ 216, dos quais R$ 214 foram para um único conjunto."
```

Situação: na última semana, uma campanha gastou R$ 216, sendo R$ 214 em um único conjunto de anúncios.
O que aconteceu: reduzir o lance desse conjunto e elevar os lances dos demais não fez o Google distribuir a entrega.
Lógica: quando o investimento não é usado de modo uniforme e o ajuste de lances não muda isso, a campanha precisa de otimização de estrutura.

### U:cd10f367f1715299:003 — Formas de alterar a estrutura
```yaml
tipo: regra
plataforma: [youtube]
tema: estrutura-de-campanha
tarefas: [otimizar-estruturas]
fonte: "fala+pdf:cst_m05_a54_otimizacao_de_estruturas.pdf"
faixa: "00:01:18–00:01:54"
perecivel: false
confianca: alta
versao: 1
```

Altere a estrutura mexendo nos grupos de anúncios: pause ou adicione grupos, una grupos de campanhas distintas ou separe os grupos de uma campanha em mais campanhas.

### U:cd10f367f1715299:004 — Não alterar por falta de dados é normal
```yaml
tipo: decisao
plataforma: [youtube]
tema: otimizacao
tarefas: [otimizar-estruturas]
fonte: "fala+pdf:cst_m05_a54_otimizacao_de_estruturas.pdf"
faixa: "00:02:59–00:04:11"
condicoes: "campanhas com verba pequena e poucos dados acumulados"
perecivel: false
confianca: alta
versao: 1
```

Se os grupos ainda têm poucos dados, não se sinta mal por não alterar a campanha.
Campanhas de R$ 10, R$ 20 ou R$ 30 por dia podem não acumular dados suficientes em uma semana para todos os tipos de otimização.

### U:cd10f367f1715299:005 — Pausar grupos e renomear a campanha de público quente
```yaml
tipo: procedimento
plataforma: [youtube]
tema: estrutura-de-campanha
tarefas: [otimizar-estruturas]
fonte: "fala+pdf:cst_m05_a54_otimizacao_de_estruturas.pdf"
faixa: "00:01:54–00:04:11"
perecivel: true
confianca: alta
versao: 1
```

Pré-condição: os grupos que recebem a verba não resolvem a distribuição mesmo após ajustes de lance.
1. Selecione os grupos que serão interrompidos, como afinidade personalizada, segmento de mercado e keywords, e pause-os.
2. Entre em campanhas e altere o nome da campanha restante para sinalizar que ela atende apenas público quente.
3. Salve a alteração de nome.

### U:cd10f367f1715299:006 — Criar campanha separada para público frio
```yaml
tipo: procedimento
plataforma: [youtube]
tema: estrutura-de-campanha
tarefas: [otimizar-estruturas, definir-orcamento]
fonte: fala
faixa: "00:02:29–00:04:52"
perecivel: true
confianca: alta
versao: 1
```

Pré-condição: a campanha original foi convertida em campanha de público quente.
1. Copie e cole a campanha no gerenciador usando Ctrl C e Ctrl V.
2. Renomeie a cópia como campanha de público frio e salve.
3. Ajuste as verbas para dividir o investimento entre público quente e público frio.
4. Na demonstração, destine metade da verba a cada público.

### U:cd10f367f1715299:007 — Remover público quente da campanha fria
```yaml
tipo: procedimento
plataforma: [youtube]
tema: publicos
tarefas: [otimizar-publicos-e-segmentacoes, otimizar-estruturas]
fonte: "fala+pdf:cst_m05_a54_otimizacao_de_estruturas.pdf"
faixa: "00:04:11–00:05:29"
perecivel: true
confianca: alta
versao: 1
```

Pré-condição: existe uma campanha separada destinada somente a públicos frios.
1. Entre na campanha de públicos frios e selecione os públicos quentes.
2. Clique em editar e remova os públicos selecionados.
3. Confirme a remoção e ative os públicos frios que devem permanecer.
4. Remova em vez de apenas pausar quando não houver intenção de reativar aqueles públicos nessa campanha.

### U:cd10f367f1715299:008 — Limitar conjuntos em campanha de verba pequena
```yaml
tipo: regua
plataforma: [youtube]
tema: estrutura-de-campanha
tarefas: [otimizar-estruturas]
fonte: fala
faixa: "00:05:31–00:05:58"
condicoes: "campanha de R$ 15 por dia"
perecivel: false
confianca: alta
versao: 1
```

Em campanha de R$ 15 por dia, 3 ou 4 conjuntos de anúncios já são suficientes; mais do que isso vira exagero.
O professor considera 4 conjuntos meio exagerado, mas adiciona outro conjunto porque ele funciona bem em outras campanhas.

### U:cd10f367f1715299:009 — Reorganizar segmentos personalizados em grupos distintos
```yaml
tipo: procedimento
plataforma: [youtube]
tema: estrutura-de-campanha
tarefas: [otimizar-publicos-e-segmentacoes, otimizar-estruturas]
fonte: fala
faixa: "00:06:01–00:08:11"
perecivel: true
confianca: media
versao: 1
nota: "A fala contém correções durante a seleção e exclusão dos públicos; a orientação final é deixar Top Apps e plataforma de venda separados do restante."
```

Pré-condição: um grupo de anúncios contém vários segmentos personalizados.
1. Duplique o grupo, altere o nome e entre no público-alvo do novo grupo.
2. Separe Top Apps e site/plataforma de venda dos demais segmentos, removendo os públicos que não devem ficar em cada grupo.
3. Renomeie os grupos para identificar os segmentos mantidos.
4. Use grupos distintos para que cada segmento personalizado tenha sua própria organização.

### U:cd10f367f1715299:010 — Acompanhar a estrutura após os ajustes
```yaml
tipo: decisao
plataforma: [youtube]
tema: otimizacao
tarefas: [otimizar-estruturas, ler-metricas-e-relatorios]
fonte: "fala+pdf:cst_m05_a54_otimizacao_de_estruturas.pdf"
faixa: "00:08:11–00:08:48"
perecivel: false
confianca: alta
versao: 1
```

Quando terminar de ajustar valores e estrutura, deixe a campanha rodar por alguns dias e analise se houve melhora.
Na demonstração, a expectativa é que os outros grupos da campanha de público quente passem a gastar R$ 15 por dia.

### U:cd10f367f1715299:011 — Opções de otimização estrutural
```yaml
tipo: regra
plataforma: [youtube]
tema: estrutura-de-campanha
tarefas: [otimizar-estruturas]
fonte: "fala+pdf:cst_m05_a54_otimizacao_de_estruturas.pdf"
faixa: "00:08:48–00:09:23"
perecivel: false
confianca: alta
versao: 1
```

Isole públicos quentes e frios, divida uma campanha em três campanhas, pause um grupo que não funciona e adicione outro, ou separe segmentos personalizados em grupos diferentes.

### U:cd10f367f1715299:012 — Alterar estrutura com motivo definido
```yaml
tipo: decisao
plataforma: [youtube]
tema: estrutura-de-campanha
tarefas: [otimizar-estruturas]
fonte: "fala+pdf:cst_m05_a54_otimizacao_de_estruturas.pdf"
faixa: "00:09:23–00:10:00"
perecivel: false
confianca: alta
versao: 1
```

Se um grupo está puxando toda a verba e os lances não dão controle, separe campanhas para controlar quanto será gasto em cada público.
Não crie ou troque campanhas sem entender o motivo da alteração; na maioria das vezes, fazer isso apenas por achar que dará resultado não dá certo.