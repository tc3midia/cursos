---
type: unidades-aula
status: rascunho
title: "9.4 - Otimizar onde os anúncios são exibidos"
modulo: "005"
ordem: 102
aula_id: c86ce4cf35ef8d0b
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - cst_m05_a94_otimizar_onde_os_anuncios_sao_exibidos.pdf
  - transcricao.md
extraido_em: 2026-09-16
gerado_por: gpt-5.6-terra
retiradas: []
divisoes: []
fusoes: []
---

# 9.4 - Otimizar onde os anúncios são exibidos

## Contexto da aula

A aula mostra como otimizar os locais de exibição de uma campanha In-Stream com botão no YouTube.
Parte da visualização de canais e vídeos onde o anúncio apareceu e dos resultados atribuídos a eles.
A otimização reúne exclusão de canais ou vídeos ruins e aproveitamento dos canais bons em novos testes.
O professor demonstra filtros, ordenações, análise de detalhes e exclusão no grupo de anúncios.
A aula seguinte fica reservada para alterar a estrutura organizacional de campanhas e grupos de anúncios.

## Unidades

### U:c86ce4cf35ef8d0b:001 — Campanha analisada é In-Stream com botão
```yaml
tipo: conceito
plataforma: [youtube]
tema: posicionamentos-e-formatos
tarefas: []
fonte: "fala+pdf:cst_m05_a94_otimizar_onde_os_anuncios_sao_exibidos.pdf"
faixa: "00:00:37–00:02:27"
perecivel: false
confianca: alta
versao: 1
nota: "A fala nomeia a campanha como TrueViewForAction; o PDF usa In-Stream com botão e a recomenda para gerar mais conversões."
```
A otimização demonstrada é de campanha In-Stream com botão, cujo anúncio aparece antes de um vídeo.
O YouTube informa os vídeos em que o anúncio apareceu e os resultados obtidos nesses locais.

### U:c86ce4cf35ef8d0b:002 — Otimização combina exclusão e aproveitamento de canais bons
```yaml
tipo: regra
plataforma: [youtube]
tema: otimizacao
tarefas: [otimizar-publicos-e-segmentacoes]
fonte: "fala+pdf:cst_m05_a94_otimizar_onde_os_anuncios_sao_exibidos.pdf"
faixa: "00:02:27–00:03:11"
perecivel: false
confianca: alta
versao: 1
```
Pause canais ou vídeos ruins e salve os canais bons em uma planilha para anunciar neles.
Otimizar também inclui encontrar o que está bom e tentar ampliar sua entrega.

### U:c86ce4cf35ef8d0b:003 — Abrir os locais onde os anúncios foram exibidos
```yaml
tipo: procedimento
plataforma: [youtube]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: "fala+pdf:cst_m05_a94_otimizar_onde_os_anuncios_sao_exibidos.pdf"
faixa: "00:03:11–00:04:12"
perecivel: true
confianca: alta
versao: 1
nota: "O PDF orienta abrir Grupos de anúncios no menu lateral; na fala, o professor abre Conteúdo na lateral. Ambos levam à visão de onde os anúncios foram exibidos."
```
Pré-condição: campanha de vídeo com dados de locais em que o anúncio apareceu.
1. Na campanha, abra a área de conteúdo ou grupos de anúncios no menu lateral.
2. Acesse “onde os anúncios foram exibidos” para ver a lista de lugares em que o anúncio apareceu.
3. Ordene a lista por conversões para identificar os locais com volume de resultados.

### U:c86ce4cf35ef8d0b:004 — Investigar detalhes apenas dos canais com mais conversões
```yaml
tipo: decisao
plataforma: [youtube]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: "fala+pdf:cst_m05_a94_otimizar_onde_os_anuncios_sao_exibidos.pdf"
faixa: "00:04:12–00:06:31"
condicoes: "canais com maior volume de conversões"
perecivel: true
confianca: alta
versao: 1
```
Quando um canal traz mais conversões, selecione-o e use “ver detalhes” para examinar os vídeos do canal.
Pare essa análise quando o volume cair; o professor deixa de aprofundar abaixo de 10 conversões.

### U:c86ce4cf35ef8d0b:005 — Vídeo sem conversão e pouco gasto não deve ser pausado
```yaml
tipo: decisao
plataforma: [youtube]
tema: otimizacao
tarefas: [otimizar-publicos-e-segmentacoes]
fonte: fala
faixa: "00:06:31–00:07:54"
condicoes: "vídeo com poucos dados ou cerca de R$ 1 gasto"
perecivel: false
confianca: alta
versao: 1
```
Se um vídeo não converteu, mas quase não teve dados ou gastou R$ 1, não o exclua só por isso.
Deixe o Google gastar mais para verificar se surge uma conversão.

### U:c86ce4cf35ef8d0b:006 — Anunciar diretamente em um vídeo que converte bem
```yaml
tipo: decisao
plataforma: [youtube]
tema: posicionamentos-e-formatos
tarefas: [escolher-canais-e-posicionamentos]
fonte: fala
faixa: "00:06:31–00:08:34"
condicoes: "vídeo específico já mostrou conversão boa"
perecivel: false
confianca: alta
versao: 1
```
Quando houver um vídeo específico que converte bem, anuncie diretamente nele, em vez de anunciar no canal inteiro.
O professor diz que pode usar lance alto para tentar aparecer nesse vídeo.

### U:c86ce4cf35ef8d0b:007 — Avaliar canais que convertem caro antes de excluir
```yaml
tipo: procedimento
plataforma: [youtube]
tema: otimizacao
tarefas: [otimizar-publicos-e-segmentacoes]
fonte: "fala+pdf:cst_m05_a94_otimizar_onde_os_anuncios_sao_exibidos.pdf"
faixa: "00:08:34–00:11:39"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: locais com pelo menos 1 conversão; a fala usa filtro de conversões maior ou igual a 1.
1. Ordene os locais por custo por conversão.
2. Analise os canais com conversão cara e mantenha os que são muito interessantes para o nicho.
3. Selecione os canais a excluir, clique em “editar” e em “excluir do grupo de anúncios”.

### U:c86ce4cf35ef8d0b:008 — Dar nova chance até o dobro do custo por lead desejado
```yaml
tipo: regua
plataforma: [youtube]
tema: otimizacao
tarefas: [otimizar-publicos-e-segmentacoes]
fonte: fala
faixa: "00:10:23–00:11:39"
condicoes: "canais sem relevância excepcional para o nicho"
perecivel: false
confianca: alta
versao: 1
```
Use até o dobro do custo por lead que está disposto a pagar como margem antes de excluir um canal.
No exemplo, querendo pagar R$ 5 por conversão, o professor dá mais uma chance para quem está abaixo de R$ 10.

### U:c86ce4cf35ef8d0b:009 — Encontrar locais sem conversão que consumiram verba
```yaml
tipo: procedimento
plataforma: [youtube]
tema: otimizacao
tarefas: [otimizar-publicos-e-segmentacoes]
fonte: "fala+pdf:cst_m05_a94_otimizar_onde_os_anuncios_sao_exibidos.pdf"
faixa: "00:11:00–00:13:10"
perecivel: true
confianca: alta
versao: 1
nota: "O PDF chama esta de terceira otimização e indica filtro conversões < 1; a fala também usa esse filtro."
```
Pré-condição: análise dos locais que não geraram conversão.
1. Crie o filtro “conversões menor do que 1”.
2. Ordene por custo para encontrar quem gastou sem converter.
3. Exclua do grupo de anúncios os canais que ultrapassaram o limite aceito, preservando os canais relevantes.

### U:c86ce4cf35ef8d0b:010 — Anunciar no canal inteiro sem vídeo mágico
```yaml
tipo: decisao
plataforma: [youtube]
tema: posicionamentos-e-formatos
tarefas: [escolher-canais-e-posicionamentos]
fonte: "fala+pdf:cst_m05_a94_otimizar_onde_os_anuncios_sao_exibidos.pdf"
faixa: "00:13:10–00:15:02"
condicoes: "canal tem volume de conversões, mas não há vídeo específico com maior chance de converter"
perecivel: false
confianca: alta
versao: 1
```
Se não houver um vídeo mágico no canal, anuncie no canal inteiro que apresenta maior volume de conversões.

### U:c86ce4cf35ef8d0b:011 — Registrar e testar canais que já converteram
```yaml
tipo: procedimento
plataforma: [youtube]
tema: posicionamentos-e-formatos
tarefas: [escolher-canais-e-posicionamentos]
fonte: fala
faixa: "00:14:22–00:16:50"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: canais com volume de conversões identificado na análise de locais de exibição.
1. Ordene por conversões, salve os canais que converteram bem em uma planilha e adicione-os ao grupo de anúncios de canais.
2. Teste os canais adicionados.
3. Pause o canal se ele não converter bem no teste.

### U:c86ce4cf35ef8d0b:012 — Teste de canais pode não funcionar
```yaml
tipo: exemplo
plataforma: [youtube]
tema: testes-e-experimentos
tarefas: [rodar-testes-e-experimentos]
fonte: fala
faixa: "00:15:02–00:16:50"
perecivel: false
confianca: alta
versao: 1
```
Situação: canais que tiveram conversões em uma campanha são adicionados a um grupo de anúncios de canais.
O que aconteceu: o professor afirma que o teste muitas vezes pode dar errado.
Lógica: se o canal não funcionar bem após ser adicionado, ele é pausado.