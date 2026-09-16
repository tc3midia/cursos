---
type: unidades-aula
status: validado
title: "13.Usando os relatórios do excel para otimizar campanhas"
modulo: "008"
ordem: 132
aula_id: 0a2da16b5c02f4d6
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - transcricao.md
extraido_em: 2026-09-16
gerado_por: gpt-5.6-terra
retiradas: []
divisoes: []
fusoes: []
---

# 13.Usando os relatórios do excel para otimizar campanhas

## Contexto da aula

A aula demonstra uma limitação operacional do TikTok para analisar anúncios dentro de uma campanha.
O professor usa uma campanha de distribuição de conteúdo como exemplo e exporta seus dados para o Excel.
Mostra como excluir anúncios inativos, agrupar resultados pelo nome do anúncio e criar linhas de soma.
A leitura numérica é complementada por análise qualitativa para verificar se o conteúdo atrai o público certo.

## Unidades

### U:0a2da16b5c02f4d6:001 — Visualização de anúncios ao abrir uma campanha
```yaml
tipo: alerta-ui
plataforma: [tiktok]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: fala
faixa: "00:00:00–00:01:16"
perecivel: true
confianca: alta
versao: 1
```
Ao selecionar uma campanha e abrir os grupos de anúncios, clicar em anúncios sem selecionar um grupo exibe os anúncios de todos os grupos daquela campanha.

### U:0a2da16b5c02f4d6:002 — Escolher colunas para análise de campanha de vídeo
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: fala
faixa: "00:01:16–00:02:33"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: estar na visualização de anúncios de uma campanha de distribuição de conteúdo.
1. Abra Colunas e Custom Columns.
2. Remova campos que não são métricas desejadas, como Ad Group ID, Delivery Suggestions, Budget e BID; mantenha Ad Group Name e custo.
3. Para essa análise de vídeo, mantenha CPM e remova CPC, cliques, CTR, conversão, CPA, CVR, custo por resultado e result rate.
4. Em engajamento, adicione seguidores vindos das campanhas, Video Views, visualizações de 25%, 70% e 100% e tempo médio assistido por vídeo.

### U:0a2da16b5c02f4d6:003 — Salvar uma predefinição de colunas de vídeo
```yaml
tipo: alerta-ui
plataforma: [tiktok]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: fala
faixa: "00:02:35–00:03:16"
perecivel: true
confianca: alta
versao: 1
```
Depois de atualizar as métricas, salve a configuração como uma coluna de Video Views para reutilizar a predefinição.

### U:0a2da16b5c02f4d6:004 — Filtro por nome remove o escopo da campanha
```yaml
tipo: alerta-ui
plataforma: [tiktok]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: fala
faixa: "00:03:16–00:06:57"
perecivel: true
confianca: alta
versao: 1
```
Ao pesquisar pelo nome de um anúncio no filtro, o TikTok desfaz a seleção da campanha e passa a mostrar anúncios com aquele nome em toda a conta, não apenas na campanha analisada.

### U:0a2da16b5c02f4d6:005 — Exportar o relatório da campanha para analisar anúncios
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: fala
faixa: "00:06:16–00:07:36"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: selecionar a campanha que será analisada.
1. Entre na área de anúncios da campanha.
2. Use o botão Export Report para baixar o relatório da campanha em Excel.
3. Abra a planilha exportada para trabalhar os resultados de cada anúncio.

### U:0a2da16b5c02f4d6:006 — Excluir anúncios inativos da planilha exportada
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: fala
faixa: "00:07:36–00:08:10"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: abrir no Excel o relatório de uma campanha com anúncios ativos e inativos.
1. Selecione a coluna Primary Stats, usada como status.
2. Em Data, ordene de A a Z ou de Z a A.
3. Selecione e delete todas as linhas com status inativo.

### U:0a2da16b5c02f4d6:007 — Ordenar os anúncios pelo nome no Excel
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: fala
faixa: "00:08:12–00:09:35"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: remover os anúncios inativos da planilha exportada.
1. Selecione a coluna do nome do anúncio.
2. Em Data, ordene pelo nome do anúncio.
3. Use o Excel porque, na demonstração, o TikTok não permitiu ordenar o nome do anúncio diretamente na campanha.

### U:0a2da16b5c02f4d6:008 — Inserir linhas de soma para cada anúncio
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: fala
faixa: "00:09:35–00:11:45"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: ordenar a planilha pelo nome do anúncio.
1. Insira uma linha após cada bloco que tenha o mesmo nome de anúncio.
2. Selecione as linhas inseridas com Ctrl ou Command e dê uma cor de destaque.
3. Em cada linha, some custo, Video Views e visualizações de 25%, 50%, 75% e 100%.
4. Copie as fórmulas para as demais linhas de soma.

### U:0a2da16b5c02f4d6:009 — Linhas de soma mostram o resultado por anúncio
```yaml
tipo: conceito
plataforma: [tiktok]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: fala
faixa: "00:09:36–00:12:34"
perecivel: true
confianca: alta
versao: 1
```
A linha geral do relatório soma a campanha inteira; as linhas inseridas agrupam e somam os resultados de cada anúncio distribuído em vários grupos de anúncios.

### U:0a2da16b5c02f4d6:010 — Pausar anúncios sem resultado nas somas
```yaml
tipo: decisao
plataforma: [tiktok]
tema: otimizacao
tarefas: [otimizar-anuncios]
fonte: fala
faixa: "00:11:45–00:12:34"
perecivel: true
confianca: alta
versao: 1
```
Se a soma de um anúncio mostra 0 ou resultados muito baixos nas visualizações, pause-o; no exemplo, AD13 e AD16 foram escolhidos para pausa.

### U:0a2da16b5c02f4d6:011 — Dar mais uma chance a anúncios com pouco gasto
```yaml
tipo: decisao
plataforma: [tiktok]
tema: otimizacao
tarefas: [otimizar-anuncios]
fonte: fala
faixa: "00:12:34–00:13:15"
perecivel: true
confianca: alta
versao: 1
```
Se um anúncio como AD18 ou AD19 gastou pouco, como 13 centavos no exemplo do AD18, você pode escolher pausá-lo ou dar mais uma chance; o professor considera ambas as escolhas aceitáveis.

### U:0a2da16b5c02f4d6:012 — Não pausar o anúncio com maior tração
```yaml
tipo: decisao
plataforma: [tiktok]
tema: otimizacao
tarefas: [otimizar-anuncios]
fonte: fala
faixa: "00:12:34–00:13:15"
perecivel: true
confianca: alta
versao: 1
```
Se o anúncio é o que mais ganha escala e gera tração para a campanha, não o pause; no exemplo, o AD5 gerava 30 mil visualizações, 11 mil visualizações de 25% e 8 mil de 50%.

### U:0a2da16b5c02f4d6:013 — Considerar volume e custo de visualização
```yaml
tipo: exemplo
plataforma: [tiktok]
tema: metricas-e-relatorios
tarefas: [otimizar-anuncios]
fonte: fala
faixa: "00:13:15–00:14:44"
perecivel: true
confianca: alta
versao: 2
nota: "Correção manual: explicitada a divisão usada para calcular o custo por visualização de 100%, sem transformar os valores do exemplo em régua geral."
```
Situação: AD11, AD12 e AD10 gastaram R$1,32, R$5 e R$6, respectivamente, mas geraram muito volume de visualizações.
O que aconteceu: o custo de uma visualização de 100% ficou em R$0,01 ou menos de um centavo em parte dos anúncios; o AD5 custava R$0,01, mas entregou 4 mil visualizações de 100% nos últimos sete dias.
Lógica: calcule o custo por visualização de 100% dividindo o valor gasto pela quantidade de visualizações de 100%. Use a planilha para comparar esse custo com o volume entregue antes de decidir pela pausa.

### U:0a2da16b5c02f4d6:014 — Encontrar anúncios para pausar na campanha
```yaml
tipo: procedimento
plataforma: [tiktok]
tema: otimizacao
tarefas: [otimizar-anuncios]
fonte: fala
faixa: "00:14:44–00:15:29"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: decidir, pela planilha, quais anúncios devem ser pausados.
1. Use Ctrl F para localizar pelo nome o anúncio escolhido, como AD16.
2. Pause as ocorrências desse anúncio.
3. Repita a busca e a pausa para os demais escolhidos, como AD13.

### U:0a2da16b5c02f4d6:015 — Métrica barata não basta para distribuição de conteúdo
```yaml
tipo: regra
plataforma: [tiktok]
tema: otimizacao
tarefas: [otimizar-anuncios]
fonte: fala
faixa: "00:15:29–00:16:44"
condicoes: "campanha de distribuição de conteúdo"
perecivel: true
confianca: alta
versao: 1
```
Não se iluda por custo de visualização barato: busque o menor custo possível dentro de um conteúdo que atraia o público certo.

### U:0a2da16b5c02f4d6:016 — Vídeo barato pode atrair público errado
```yaml
tipo: exemplo
plataforma: [tiktok]
tema: criativo
tarefas: [otimizar-anuncios]
fonte: fala
faixa: "00:15:30–00:16:44"
perecivel: true
confianca: alta
versao: 1
```
Situação: um vídeo humorístico reagindo a anúncios estranhos era o que mais gerava visualizações.
O que aconteceu: ele obtinha visualizações mais baratas que um vídeo sobre tráfego pago.
Lógica: o vídeo podia atrair pessoas interessadas em humor, e não pessoas que querem aprender a anunciar na internet.

### U:0a2da16b5c02f4d6:017 — Custo fora do padrão é sinal para revisar o conteúdo
```yaml
tipo: decisao
plataforma: [tiktok]
tema: otimizacao
tarefas: [otimizar-anuncios]
fonte: fala
faixa: "00:16:44–00:17:57"
condicoes: "custo por visualização ou engajamento muito abaixo do padrão da conta"
perecivel: true
confianca: alta
versao: 1
```
Se um conteúdo tem custo muito barato, revise se ele está genérico demais ou atraindo público não qualificado; a análise do conteúdo, e não apenas as métricas, responde se ele atrai o público certo.

### U:0a2da16b5c02f4d6:018 — Não distribuir conteúdo que atrai o público errado
```yaml
tipo: decisao
plataforma: [tiktok]
tema: otimizacao
tarefas: [otimizar-anuncios]
fonte: fala
faixa: "00:17:22–00:17:57"
condicoes: "a revisão do conteúdo indica que ele atrai o público errado"
perecivel: true
confianca: alta
versao: 1
```
Se a resposta for que o conteúdo pode estar atraindo o público errado, não distribua esse conteúdo.