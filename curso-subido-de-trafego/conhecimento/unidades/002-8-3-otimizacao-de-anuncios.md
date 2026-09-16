---
type: unidades-aula
status: validado
title: "8.3 - Otimização de anúncios"
modulo: "002"
ordem: 53
aula_id: 276afb7e27536530
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - transcricao.md
extraido_em: 2026-09-15
gerado_por: gpt-5.6-terra
retiradas: []
divisoes: []
fusoes: []
---

# 8.3 - Otimização de anúncios

## Contexto da aula

A aula apresenta quatro maneiras de otimizar anúncios em campanhas do Meta.
Ela parte de uma campanha de conversão já existente, com anúncios ativos, pausados e ainda não testados.
O foco é decidir quais anúncios pausar e quais ativar conforme custo por resultado e volume de conversões.
Também mostra testes paralelos para quem tem muita verba e anúncios específicos para públicos valorizados.

## Unidades

### U:276afb7e27536530:001 — Quatro formas de otimizar anúncios
```yaml
tipo: conceito
plataforma: [meta]
tema: otimizacao
tarefas: [otimizar-anuncios]
fonte: fala
faixa: "00:00:00–00:00:33"
perecivel: false
confianca: alta
versao: 1
```
A aula organiza a otimização de anúncios em quatro formas: análise grupo por grupo, análise geral da campanha, testes paralelos e criação de anúncios específicos.

### U:276afb7e27536530:002 — Limite de seis anúncios ativos por grupo
```yaml
tipo: regua
plataforma: [meta]
tema: estrutura-de-campanha
tarefas: [definir-estrutura-de-campanha, otimizar-anuncios]
fonte: fala
faixa: "00:00:34–00:01:03"
condicoes: "no grupo de anúncios em otimização"
perecivel: false
confianca: alta
versao: 1
```
Busque não ter mais de seis anúncios ativos no grupo de anúncios.
Sempre que pausar um anúncio, ative outro para substituí-lo.

### U:276afb7e27536530:003 — Ordenar anúncios para analisar o grupo
```yaml
tipo: procedimento
plataforma: [meta]
tema: otimizacao
tarefas: [otimizar-anuncios, ler-metricas-e-relatorios]
fonte: fala
faixa: "00:00:00–00:01:38"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: campanha aberta e período de análise pré-definido, como os últimos 7 dias.
1. Entre em cada grupo de anúncios da campanha.
2. Filtre a veiculação para exibir somente anúncios ativos.
3. Ordene pelos resultados e pelo custo por resultado buscado.
4. Use a ordenação para separar anúncios de alto volume dos anúncios caros.

### U:276afb7e27536530:004 — Filtrar apenas os anúncios que serão trabalhados
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: otimizacao
tarefas: [otimizar-anuncios]
fonte: fala
faixa: "00:01:39–00:02:12"
perecivel: true
confianca: alta
versao: 1
```
Filtre a visualização para mostrar somente o que será trabalhado na otimização; isso dá uma visão clara da análise.

### U:276afb7e27536530:005 — Cuidado ao pausar anúncios de alto volume
```yaml
tipo: decisao
plataforma: [meta]
tema: otimizacao
tarefas: [otimizar-anuncios]
fonte: fala
faixa: "00:01:03–00:03:34"
condicoes: "o anúncio está entre os que mais geram resultados"
perecivel: false
confianca: alta
versao: 1
```
Quando um anúncio está no topo pelo número de resultados, tenha mais delicadeza para pausá-lo; com os três primeiros, o cuidado deve ser maior, principalmente com o primeiro.
O anúncio pode ter custo maior que outro, mas ainda ser uma fonte importante das oportunidades que a campanha encontra.

### U:276afb7e27536530:006 — Pausar só o anúncio muito fora do custo desejado
```yaml
tipo: decisao
plataforma: [meta]
tema: otimizacao
tarefas: [otimizar-anuncios]
fonte: fala
faixa: "00:03:34–00:04:12"
condicoes: "o anúncio também gera volume relevante"
perecivel: false
confianca: alta
versao: 1
```
Se um anúncio de alto volume não estiver muito fora do valor que você quer pagar, não o pause.
No exemplo, a meta era R$ 5, o anúncio custava R$ 6,36 e o custo geral era R$ 5,25.

### U:276afb7e27536530:007 — Pausar os piores por custo e volume
```yaml
tipo: decisao
plataforma: [meta]
tema: otimizacao
tarefas: [otimizar-anuncios]
fonte: fala
faixa: "00:03:34–00:04:12"
condicoes: "o anúncio tem custo caro e baixo número de conversões"
perecivel: false
confianca: alta
versao: 1
```
Quando o anúncio tem custo caro e não gera um volume legal de conversões, pause-o e ative novos anúncios em seu lugar.

### U:276afb7e27536530:008 — Deixar anúncios prontos antes da otimização
```yaml
tipo: regra
plataforma: [meta]
tema: otimizacao
tarefas: [otimizar-anuncios, configurar-anuncio]
fonte: fala
faixa: "00:04:12–00:05:31"
perecivel: false
confianca: alta
versao: 1
```
Crie anúncios de reposição antes da sessão de otimização.
Na hora de criar, apenas crie; na hora de otimizar, apenas otimize, para não perder produtividade.

### U:276afb7e27536530:009 — Substituir pausados por anúncios ainda não testados
```yaml
tipo: procedimento
plataforma: [meta]
tema: otimizacao
tarefas: [otimizar-anuncios]
fonte: fala
faixa: "00:04:12–00:05:31"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: anúncios de reposição já criados na campanha.
1. Pause os anúncios que não estão funcionando legal no grupo.
2. Ative a mesma quantidade dos próximos anúncios preparados.
3. Mantenha os substitutos disponíveis na campanha antes de precisar deles.

### U:276afb7e27536530:010 — Otimização geral da campanha economiza tempo
```yaml
tipo: conceito
plataforma: [meta]
tema: otimizacao
tarefas: [otimizar-anuncios]
fonte: fala
faixa: "00:05:31–00:06:14"
perecivel: false
confianca: alta
versao: 1
```
A otimização geral analisa todos os anúncios da campanha de uma vez, em vez de otimizar grupo por grupo.
Ela é indicada quando há menos tempo e o professor diz que normalmente pode ter resultado pior do que a análise por grupo.

### U:276afb7e27536530:011 — Analisar a campanha inteira pelos anúncios ativos
```yaml
tipo: procedimento
plataforma: [meta]
tema: otimizacao
tarefas: [otimizar-anuncios, ler-metricas-e-relatorios]
fonte: fala
faixa: "00:06:07–00:10:45"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: todos os grupos de anúncios da campanha estão abertos para análise conjunta.
1. Exiba todos os anúncios e filtre somente os ativos.
2. Anote o resultado médio e o total de conversões da campanha.
3. Ordene por resultados para identificar anúncios com maior volume e evite pausá-los sem cuidado.
4. Ordene por custo por resultado para encontrar anúncios caros que não aparecem entre os de bom volume.
5. Pause os anúncios ruins e substitua-os por anúncios ainda não testados.
6. Confira o gasto do substituto no período máximo e publique após a conferência.

### U:276afb7e27536530:012 — Análise geral considera o desempenho total do anúncio
```yaml
tipo: regra
plataforma: [meta]
tema: otimizacao
tarefas: [otimizar-anuncios]
fonte: fala
faixa: "00:07:45–00:09:52"
perecivel: false
confianca: alta
versao: 1
```
Na otimização geral, analise o custo por resultado do anúncio no conjunto da campanha, não CPM ou CTR.
Um anúncio pode ter custo alto em um grupo e ainda assim não estar ruim na análise geral.

### U:276afb7e27536530:013 — A otimização geral é usada em 70% das vezes
```yaml
tipo: regua
plataforma: [meta]
tema: otimizacao
tarefas: [otimizar-anuncios]
fonte: fala
faixa: "00:10:45–00:11:26"
perecivel: false
confianca: alta
versao: 1
```
O professor diz que, na maioria das vezes, a otimização geral funciona tão bem quanto a análise grupo por grupo e que ela é feita em 70% das vezes.

### U:276afb7e27536530:014 — Testar criativos em campanha paralela
```yaml
tipo: procedimento
plataforma: [meta]
tema: testes-e-experimentos
tarefas: [rodar-testes-e-experimentos, otimizar-anuncios]
fonte: fala
faixa: "00:11:26–00:12:44"
condicoes: "quando há muita verba e pouco tempo para descobrir o melhor anúncio na campanha principal"
perecivel: true
confianca: media
nota: "O professor diz 'BO' ao configurar o orçamento; o nome da configuração não está claro na fala."
versao: 1
```
Pré-condição: campanha paralela criada para testar criativos e público frio que já se sabe ser bom.
1. Coloque os anúncios em concorrência na campanha paralela.
2. Configure para todos gastarem o mesmo orçamento.
3. Observe quais anúncios apresentam melhor custo por conversão.
4. Ao pausar um anúncio da campanha principal, ative um anúncio que já funcionou no teste paralelo.

### U:276afb7e27536530:015 — Priorizar na campanha principal o criativo já testado
```yaml
tipo: decisao
plataforma: [meta]
tema: otimizacao
tarefas: [otimizar-anuncios, rodar-testes-e-experimentos]
fonte: fala
faixa: "00:12:05–00:13:22"
condicoes: "há uma campanha paralela com resultado dos criativos"
perecivel: false
confianca: alta
versao: 1
```
Quando precisar ativar um anúncio na campanha principal, prefira o criativo que a campanha paralela já mostrou ser bom, em vez de ativar um anúncio ainda não testado.

### U:276afb7e27536530:016 — Criar anúncio específico para público valioso
```yaml
tipo: decisao
plataforma: [meta]
tema: criativo
tarefas: [otimizar-anuncios, configurar-anuncio]
fonte: fala
faixa: "00:13:22–00:14:28"
condicoes: "o público é valioso e não está funcionando legal"
perecivel: false
confianca: alta
versao: 1
```
Quando não quiser abrir mão de um público, grave e suba um anúncio que fale somente com aquelas pessoas.
Essa abordagem é especialmente fácil em campanhas de público quente e ajuda a ressuscitar públicos que não estão funcionando legal.

### U:276afb7e27536530:017 — Público misturado dificulta anúncio específico
```yaml
tipo: decisao
plataforma: [meta]
tema: publicos
tarefas: [otimizar-publicos-e-segmentacoes, otimizar-anuncios]
fonte: fala
faixa: "00:13:55–00:14:28"
condicoes: "há dois públicos misturados no mesmo conjunto de anúncios"
perecivel: false
confianca: alta
versao: 1
```
Se dois públicos estiverem misturados no mesmo conjunto de anúncios, criar uma mensagem específica para eles fica menos fácil.

### U:276afb7e27536530:018 — Lógica central da otimização de anúncios
```yaml
tipo: regra
plataforma: [meta]
tema: otimizacao
tarefas: [otimizar-anuncios]
fonte: fala
faixa: "00:14:28–00:15:09"
perecivel: false
confianca: alta
versao: 1
```
Pause o que não funciona e suba o que funciona.
Em testes paralelos, não substitua um anúncio ruim por algo desconhecido: use um anúncio já testado que você sabe que funciona.