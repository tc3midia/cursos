---
type: unidades-aula
status: validado
title: "6.0 - Otimização de canais e públicos"
modulo: "006"
ordem: 110
aula_id: 1c2f010a1aecd776
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - cst_m06_a06_otimizacao_de_canais_e_publicos.pdf
  - transcricao.md
extraido_em: 2026-09-16
gerado_por: gpt-5.6-terra
retiradas: []
divisoes: []
fusoes: []
---

# 6.0 - Otimização de canais e públicos

## Contexto da aula

A aula continua a otimização de campanhas da Rede de Display do Google.
Ela pressupõe a aula anterior sobre momento de otimizar, relevância estatística e métrica principal.
O professor demonstra como analisar canais exibidos, pausar canais e extrair informações sobre o público.
Também apresenta a otimização de públicos por grupo de anúncios e distingue estruturas de atenção, recordação e intenção.
A próxima aula tratará da otimização de criativos no Display.

## Unidades

### U:1c2f010a1aecd776:001 — Baseie a otimização na métrica principal da campanha
```yaml
tipo: decisao
plataforma: [google-display]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: fala
faixa: 00:00:37–00:02:14
perecivel: false
confianca: alta
versao: 1
```
Se for otimizar uma campanha, olhe sempre para a métrica principal, definida pelo objetivo de atenção, intenção ou recordação.

### U:1c2f010a1aecd776:002 — Relevância estatística depende do volume de dados
```yaml
tipo: regua
plataforma: [google-display]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: fala
faixa: 00:00:37–00:01:37
perecivel: false
confianca: alta
versao: 1
```
Considere relevância estatística como boa quantidade de dados: o professor usa 1.000 impressões como referência e uma quantidade de resultados adequada ao tamanho do tráfego e do nicho.
100 conversões podem ser pouco para uma pessoa e muito para outra.

### U:1c2f010a1aecd776:003 — Otimização de canais lê o resultado por site da GDN
```yaml
tipo: conceito
plataforma: [google-display]
tema: posicionamentos-e-formatos
tarefas: []
fonte: fala
faixa: 00:02:14–00:03:30
perecivel: false
confianca: alta
versao: 1
```
A otimização de canais mostra o resultado dos anúncios em cada site parceiro do Google na GDN.
Ela permite pausar sites sem resultado satisfatório.

### U:1c2f010a1aecd776:004 — Use canais bons para conhecer o público
```yaml
tipo: regra
plataforma: [google-display]
tema: publicos
tarefas: [otimizar-publicos-e-segmentacoes]
fonte: fala
faixa: 00:03:30–00:04:39
perecivel: false
confianca: alta
versao: 1
```
Além de pausar canais ruins, identifique os bons para aprender quais sites o usuário e as pessoas segmentadas costumam acessar.
Extraia essa informação das campanhas.

### U:1c2f010a1aecd776:005 — Analise canais em períodos de 14, 21 ou 30 dias
```yaml
tipo: decisao
plataforma: [google-display]
tema: otimizacao
tarefas: [otimizar-publicos-e-segmentacoes]
fonte: fala
faixa: 00:04:39–00:06:30
condicoes: "quando 14 dias não derem relevância estatística"
perecivel: false
confianca: alta
versao: 1
```
Se 14 dias não derem relevância estatística, analise 21 dias; se ainda não der, analise 30 dias.
Os períodos sugeridos são 14 em 14, 21 em 21 ou 30 em 30 dias e variam conforme o tráfego e o investimento.

### U:1c2f010a1aecd776:006 — Avalie escala, custo e qualidade do canal
```yaml
tipo: regra
plataforma: [google-display]
tema: otimizacao
tarefas: [otimizar-publicos-e-segmentacoes]
fonte: fala
faixa: 00:06:30–00:08:20
perecivel: false
confianca: alta
versao: 1
```
Avalie escala, custo por resultado e qualidade do site ao decidir sobre um canal.
Escala é o resultado gerado; qualidade inclui a reputação do site, seus materiais e sua relação com o assunto anunciado.

### U:1c2f010a1aecd776:007 — Limite os critérios de decisão a três pontos
```yaml
tipo: regra
plataforma: [google-display]
tema: otimizacao
tarefas: [otimizar-publicos-e-segmentacoes]
fonte: fala
faixa: 00:07:45–00:09:30
perecivel: false
confianca: alta
versao: 1
```
Tente não passar de 3 pontos para tomar uma decisão de otimização.
Analise a métrica principal, pois analisar muitas métricas pode impedir a decisão.

### U:1c2f010a1aecd776:008 — Abra “Onde os anúncios foram exibidos” para otimizar canais
```yaml
tipo: procedimento
plataforma: [google-display]
tema: posicionamentos-e-formatos
tarefas: [otimizar-publicos-e-segmentacoes]
fonte: fala
faixa: 00:09:30–00:10:46
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: campanha de Display com dados para análise.
1. Abra “Canais”; essa tela mostra os canais escolhidos ativamente para segmentação.
2. Abra “Onde os anúncios foram exibidos” para analisar os locais em que os anúncios apareceram.
3. Otimize a tela “Canais” apenas se a campanha for de intenção.

### U:1c2f010a1aecd776:009 — Filtre os canais relevantes pela métrica principal
```yaml
tipo: procedimento
plataforma: [google-display]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios, otimizar-publicos-e-segmentacoes]
fonte: fala
faixa: 00:10:42–00:12:41
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: período de análise definido e métrica principal identificada.
1. Abra “Filtros” em “Onde os anúncios foram exibidos”.
2. Escolha “Impressões” e defina valores maiores que 1.000.
3. Ajuste o limiar conforme a métrica principal: conversões ou cliques exigem uma referência relevante para o caso.

### U:1c2f010a1aecd776:010 — Impressão visível exige área e tempo de exibição
```yaml
tipo: regua
plataforma: [google-display]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: fala
faixa: 00:12:41–00:13:24
perecivel: true
confianca: alta
versao: 1
```
Uma impressão é considerada visível quando pelo menos 50% da área do anúncio fica visível por 1 segundo.
Passe o mouse sobre a métrica no gerenciador para ler sua explicação.

### U:1c2f010a1aecd776:011 — Pause canais relevantes caros e ruins
```yaml
tipo: decisao
plataforma: [google-display]
tema: otimizacao
tarefas: [otimizar-publicos-e-segmentacoes]
fonte: fala
faixa: 00:13:24–00:16:49
condicoes: "canais com mais de 1.000 impressões na demonstração"
perecivel: false
confianca: alta
versao: 1
```
Se um canal relevante tiver custo por resultado acima da régua e for ruim ou não tiver relação com o anunciado, pause-o.
Na demonstração, a régua é CPM visível médio de R$ 1,50; canais muito relacionados ao que anuncia ou como YouTube podem ser mantidos.

### U:1c2f010a1aecd776:012 — Revise as impressões antes de excluir canais selecionados
```yaml
tipo: regra
plataforma: [google-display]
tema: otimizacao
tarefas: [otimizar-publicos-e-segmentacoes]
fonte: fala
faixa: 00:15:24–00:16:49
perecivel: false
confianca: alta
versao: 1
```
Antes de excluir os canais selecionados, revise o número de impressões visíveis e verifique se algum canal se destaca muito.
Se o filtro retornar somente 3 sites, o professor considera que não há relevância estatística adequada.

### U:1c2f010a1aecd776:013 — Exclua canais pelo menu de edição do grupo de anúncios
```yaml
tipo: procedimento
plataforma: [google-display]
tema: posicionamentos-e-formatos
tarefas: [otimizar-publicos-e-segmentacoes]
fonte: fala
faixa: 00:16:13–00:17:34
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: canais já selecionados para remoção na tela “Onde os anúncios foram exibidos”.
1. Clique em “Editar”.
2. Clique em “Excluir do grupo de anúncios”.
3. Confirme a mensagem de canais excluídos; eles podem continuar aparecendo na listagem após a atualização.

### U:1c2f010a1aecd776:014 — Registre canais relevantes e baratos para usos futuros
```yaml
tipo: regra
plataforma: [google-display, youtube]
tema: publicos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: 00:17:34–00:19:11
perecivel: false
confianca: alta
versao: 1
nota: "O professor diz que a lista de sites e aplicativos pode servir no futuro para criar público de Intenção Personalizada no YouTube."
```
Ordene os canais relevantes do mais barato para o mais caro e anote sites ou aplicativos interessantes.
Use a lista futuramente para criar um público de Intenção Personalizada no YouTube.

### U:1c2f010a1aecd776:015 — Amplie o período antes de agir sobre canais pouco relevantes
```yaml
tipo: decisao
plataforma: [google-display]
tema: otimizacao
tarefas: [otimizar-publicos-e-segmentacoes]
fonte: fala
faixa: 00:19:15–00:21:16
condicoes: "canais com menos de 1.000 impressões e custo alto"
perecivel: false
confianca: alta
versao: 1
```
Se canais pouco relevantes tiverem custo alto com poucas impressões, aumente o período de 14 para 21 dias antes de pausar.
CPM de R$ 3.000,00 com 1, 2 ou 3 impressões não é custo confiável; pause se o custo continuar alto com mais impressões.

### U:1c2f010a1aecd776:016 — Use 400 a menos de 1.000 impressões no ajuste fino
```yaml
tipo: regua
plataforma: [google-display]
tema: otimizacao
tarefas: [otimizar-publicos-e-segmentacoes]
fonte: fala
faixa: 00:20:35–00:26:40
perecivel: false
confianca: alta
versao: 1
```
Para a otimização dos menos relevantes, use canais com menos de 1.000 e mais de 400 impressões.
O professor primeiro usou mais de 100 impressões, mas recomenda 400 porque o CPM fica menos distorcido; essa é uma otimização secundária.

### U:1c2f010a1aecd776:017 — Trate a otimização dos menos relevantes como ajuste fino
```yaml
tipo: decisao
plataforma: [google-display]
tema: otimizacao
tarefas: [otimizar-publicos-e-segmentacoes]
fonte: fala
faixa: 00:21:16–00:25:47
condicoes: "canais abaixo de 1.000 impressões"
perecivel: false
confianca: alta
versao: 1
```
Se analisar canais menos relevantes, pause com mais cautela, pois os dados podem estar distorcidos e a ação é ajuste fino.
Na demonstração, o professor pausa canais caros até CPM de R$ 10,00, preservando canais considerados bons.

### U:1c2f010a1aecd776:018 — Canal de aplicativo inválido não pode ser excluído
```yaml
tipo: alerta-ui
plataforma: [google-display]
tema: posicionamentos-e-formatos
tarefas: [otimizar-publicos-e-segmentacoes]
fonte: fala
faixa: 00:23:13–00:23:49
perecivel: true
confianca: alta
versao: 1
```
Se a exclusão informar que um site não foi excluído, abra “Ver Detalhes” e consulte “Erros”.
Um canal de aplicativo para dispositivos móveis inválido não pode ser excluído porque já não é possível anunciar nele.

### U:1c2f010a1aecd776:019 — Otimize públicos dentro de cada grupo de anúncios
```yaml
tipo: procedimento
plataforma: [google-display]
tema: publicos
tarefas: [otimizar-publicos-e-segmentacoes]
fonte: fala
faixa: 00:26:40–00:28:27
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: campanha de Display com grupos de anúncios e públicos configurados.
1. Abra “Grupos de anúncio” e entre em cada grupo, um por vez.
2. Abra “Públicos-alvo” e avalie se algum público deve ser pausado.
3. Se o grupo tiver apenas um público, não há o que otimizar nele.

### U:1c2f010a1aecd776:020 — Preserve público caro quando sua qualidade for muito boa
```yaml
tipo: decisao
plataforma: [google-display]
tema: publicos
tarefas: [otimizar-publicos-e-segmentacoes]
fonte: fala
faixa: 00:27:50–00:29:01
condicoes: "público com custo alto em estrutura de atenção ou recordação"
perecivel: false
confianca: alta
versao: 1
```
Se um público estiver caro, avalie também sua qualidade antes de pausá-lo.
O professor manteria o público de quem curtiu seus vídeos nos últimos 14 dias mesmo com CPM de R$ 1,50, se sua qualidade fosse muito boa.

### U:1c2f010a1aecd776:021 — Estruturas de intenção exigem otimização de públicos em “Canais”
```yaml
tipo: decisao
plataforma: [google-display]
tema: publicos
tarefas: [otimizar-publicos-e-segmentacoes]
fonte: fala
faixa: 00:28:27–00:29:01
perecivel: true
confianca: alta
versao: 1
```
Se a campanha tiver objetivo de intenção, entre na aba “Canais”, onde está a segmentação, para escolher pausar ou manter públicos.
Em estruturas de atenção ou recordação, a otimização de públicos normalmente exige pouca intervenção.

### U:1c2f010a1aecd776:022 — Crie uma régua própria e analise canal por canal
```yaml
tipo: regra
plataforma: [google-display]
tema: otimizacao
tarefas: [otimizar-publicos-e-segmentacoes]
fonte: fala
faixa: 00:29:01–00:30:11
perecivel: false
confianca: alta
versao: 1
```
Não trave: crie uma lógica e uma régua para a própria conta.
Analise os canais com calma, um por um e site por site; o professor diz que o feeling vem da repetição dessas otimizações.