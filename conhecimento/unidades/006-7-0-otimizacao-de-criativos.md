---
type: unidades-aula
status: validado
title: "7.0 - Otimização de criativos"
modulo: "006"
ordem: 111
aula_id: 6bb448cdbb00ccb4
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - cst_m06_a07_otimizacao_de_criativos.pdf
  - transcricao.md
extraido_em: 2026-09-16
gerado_por: gpt-5.6-terra
retiradas: []
divisoes: []
fusoes: []
---

# 7.0 - Otimização de criativos

## Contexto da aula

A aula encerra o ciclo de otimizações para campanhas da Rede de Display do Google.
Ela contrasta a prioridade de criativos com a de estrutura especificamente no Display.
Mostra como analisar anúncios por conjunto, decidir entre pausar ou manter e criar uma variação responsiva.
A demonstração pressupõe uma campanha com dados suficientes e anúncios já publicados.
A otimização de estrutura para Pesquisa, YouTube, Facebook e Instagram fica para depois.

## Unidades

### U:6bb448cdbb00ccb4:001 — Priorize criativos em vez de variar estrutura no Display
```yaml
tipo: decisao
plataforma: [google-display]
tema: estrutura-de-campanha
tarefas: [otimizar-estruturas, otimizar-anuncios]
fonte: fala+pdf:cst_m06_a07_otimizacao_de_criativos.pdf
faixa: 00:00:00–00:01:14
perecivel: false
confianca: alta
versao: 1
```
Quando a campanha for de Display, mantenha a estrutura de atenção, intenção ou recordação e concentre o esforço em lances, canais, públicos e criativos.
Separar Display por mobile, desktop ou vários conjuntos de canais normalmente não funcionou bem nos muitos testes relatados.

### U:6bb448cdbb00ccb4:002 — Estrutura importa em outras redes
```yaml
tipo: limite
plataforma: [google-search, youtube, meta]
tema: estrutura-de-campanha
tarefas: []
fonte: fala+pdf:cst_m06_a07_otimizacao_de_criativos.pdf
faixa: 00:00:38–00:01:14
perecivel: false
confianca: alta
versao: 1
```
A aula não detalha otimização de estrutura para Pesquisa, YouTube, Facebook ou Instagram; o professor afirma que nessas redes esse esforço faz muita diferença e será tratado depois.

### U:6bb448cdbb00ccb4:003 — Use pelo menos 14 dias para otimizar criativos
```yaml
tipo: regua
plataforma: [google-display]
tema: otimizacao
tarefas: [otimizar-anuncios]
fonte: fala+pdf:cst_m06_a07_otimizacao_de_criativos.pdf
faixa: 00:01:14–00:02:27
condicoes: "a campanha precisa ter volume de dados relevante"
perecivel: false
confianca: alta
versao: 1
```
Analise no mínimo 14 dias para otimizar criativos na Rede de Display.
No exemplo, 14 dias e cerca de R$ 2 mil gastos davam dados suficientes; para alguns clientes, use 21 ou até 30 dias para obter volume relevante.

### U:6bb448cdbb00ccb4:004 — Otimize criativos por conjunto de anúncios
```yaml
tipo: procedimento
plataforma: [google-display]
tema: otimizacao
tarefas: [otimizar-anuncios]
fonte: fala+pdf:cst_m06_a07_otimizacao_de_criativos.pdf
faixa: 00:01:51–00:02:27
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: campanha de Display aberta com período de análise definido.
1. Entre em um conjunto de anúncios.
2. Abra a tela que lista os anúncios desse conjunto.
3. Analise cada anúncio antes de passar ao próximo conjunto.

### U:6bb448cdbb00ccb4:005 — Escolha entre pausar ou manter cada anúncio
```yaml
tipo: regra
plataforma: [google-display]
tema: otimizacao
tarefas: [otimizar-anuncios]
fonte: fala+pdf:cst_m06_a07_otimizacao_de_criativos.pdf
faixa: 00:01:51–00:03:03
perecivel: false
confianca: alta
versao: 1
```
Para cada anúncio, a decisão de otimização é binária: pausar ou manter.

### U:6bb448cdbb00ccb4:006 — Não pause formato sem substituto do mesmo tamanho
```yaml
tipo: decisao
plataforma: [google-display]
tema: posicionamentos-e-formatos
tarefas: [otimizar-anuncios]
fonte: fala+pdf:cst_m06_a07_otimizacao_de_criativos.pdf
faixa: 00:03:03–00:04:33
condicoes: "o anúncio ocupa um tamanho que pode ser exclusivo em determinados sites"
perecivel: false
confianca: alta
versao: 1
```
Se for pausar um anúncio de tamanho específico, só faça isso quando houver outro anúncio do mesmo tamanho para substituí-lo.
Pausar o único anúncio de 600x1200, por exemplo, impede a exibição em sites que só oferecem esse espaço e pode reduzir a escala.

### U:6bb448cdbb00ccb4:007 — Compare criativos apenas com o mesmo tamanho
```yaml
tipo: regra
plataforma: [google-display]
tema: criativo
tarefas: [otimizar-anuncios]
fonte: fala+pdf:cst_m06_a07_otimizacao_de_criativos.pdf
faixa: 00:04:33–00:05:15
perecivel: false
confianca: alta
versao: 1
```
Compare um criativo somente com outro do mesmo tamanho; 320x50 não deve ser comparado com 300x600.

### U:6bb448cdbb00ccb4:008 — Peça novas versões de formatos específicos
```yaml
tipo: regua
plataforma: [google-display]
tema: criativo
tarefas: [fazer-briefing-de-criativo, otimizar-anuncios]
fonte: fala+pdf:cst_m06_a07_otimizacao_de_criativos.pdf
faixa: 00:04:33–00:05:15
perecivel: false
confianca: alta
versao: 1
```
Peça ao designer novos anúncios de tamanhos específicos uma vez a cada 30 ou 45 dias, com novas fotos, layout, cor ou outra variação.
Use as novas peças para comparar formato com formato e decidir qual pausar.

### U:6bb448cdbb00ccb4:009 — Dê prioridade aos anúncios responsivos
```yaml
tipo: conceito
plataforma: [google-display]
tema: criativo
tarefas: []
fonte: fala+pdf:cst_m06_a07_otimizacao_de_criativos.pdf
faixa: 00:05:15–00:06:34
perecivel: false
confianca: alta
versao: 1
```
Os anúncios responsivos aparecem mais na campanha demonstrada: em 14 dias, contribuíam com mais da metade das 335 mil impressões visíveis.
Eles permitem novas variações de texto e copy sem depender de novas fotos do designer.

### U:6bb448cdbb00ccb4:010 — Avalie escala e custo por resultado
```yaml
tipo: regra
plataforma: [google-display]
tema: metricas-e-relatorios
tarefas: [otimizar-anuncios]
fonte: fala+pdf:cst_m06_a07_otimizacao_de_criativos.pdf
faixa: 00:06:34–00:07:18
perecivel: false
confianca: alta
versao: 1
```
Ao comparar anúncios responsivos, observe escala e custo por resultado.
O anúncio com custo mais caro e sem a maior quantidade de impressões visíveis foi escolhido para pausa.

### U:6bb448cdbb00ccb4:011 — Prefira escala entre custos próximos
```yaml
tipo: exemplo
plataforma: [google-display]
tema: otimizacao
tarefas: [otimizar-anuncios]
fonte: fala+pdf:cst_m06_a07_otimizacao_de_criativos.pdf
faixa: 00:06:34–00:07:18
perecivel: false
confianca: alta
versao: 1
```
Situação: havia um anúncio a R$ 1,82 com 10 mil impressões visíveis e outro a R$ 1,97.
O que aconteceu: o professor duplicou o de R$ 1,97, que tinha o segundo menor custo e maior escala.
Lógica: entre custos próximos, ele ordenou a escolha pela combinação de custo por resultado e escala.

### U:6bb448cdbb00ccb4:012 — Duplique o anúncio escolhido antes de variar
```yaml
tipo: procedimento
plataforma: [google-display]
tema: criativo
tarefas: [otimizar-anuncios]
fonte: fala+pdf:cst_m06_a07_otimizacao_de_criativos.pdf
faixa: 00:07:18–00:08:03
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: anúncio responsivo escolhido como base para uma nova variação.
1. Selecione o anúncio e use “Editar” e “Copiar”.
2. Feche a barra exibida e use CTRL+V no grupo de anúncios.
3. Confirme que a cópia será colada no grupo.
4. Selecione “Se já existe um anúncio no destino, crie um anúncio duplicado” e clique em “Colar”.

### U:6bb448cdbb00ccb4:013 — Nova imagem é a variação de maior impacto
```yaml
tipo: regra
plataforma: [google-display]
tema: criativo
tarefas: [fazer-briefing-de-criativo, otimizar-anuncios]
fonte: fala+pdf:cst_m06_a07_otimizacao_de_criativos.pdf
faixa: 00:08:03–00:09:10
perecivel: false
confianca: alta
versao: 1
```
Para uma variação com mudança maior de resultado, peça uma nova imagem ao designer.
Se não houver imagens novas, altere títulos e descrições, que são a copy disponível para edição.

### U:6bb448cdbb00ccb4:014 — Pequenas mudanças de copy são testes
```yaml
tipo: conceito
plataforma: [google-display]
tema: testes-e-experimentos
tarefas: [otimizar-anuncios, rodar-testes-e-experimentos]
fonte: fala+pdf:cst_m06_a07_otimizacao_de_criativos.pdf
faixa: 00:09:18–00:11:14
perecivel: false
confianca: alta
versao: 1
```
Pequenas alterações de títulos e descrições são testes em busca de melhora de resultado.
O professor não garante que essas variações melhorem nem revolucionem a campanha; ele as trata como trabalho semanal, quinzenal ou a cada 21 dias.

### U:6bb448cdbb00ccb4:015 — Ajuste a copy ao público já cadastrado
```yaml
tipo: decisao
plataforma: [google-display]
tema: copy-e-roteiro
tarefas: [escrever-copy-e-roteiro, otimizar-anuncios]
fonte: fala+pdf:cst_m06_a07_otimizacao_de_criativos.pdf
faixa: 00:10:02–00:11:12
condicoes: "o anúncio é exibido para pessoas que já se cadastraram"
perecivel: false
confianca: alta
versao: 1
```
Se o anúncio for para pessoas já cadastradas, não repita que a aula é sobre tráfego; use uma mensagem de lembrete com dia e horário.

### U:6bb448cdbb00ccb4:016 — Aguarde cerca de 15 dias após a alteração
```yaml
tipo: regua
plataforma: [google-display]
tema: otimizacao
tarefas: [otimizar-anuncios]
fonte: fala+pdf:cst_m06_a07_otimizacao_de_criativos.pdf
faixa: 00:11:06–00:11:56
perecivel: false
confianca: alta
versao: 1
```
Depois de salvar as alterações, deixe os anúncios rodarem por mais cerca de 15 dias antes de uma nova otimização.

### U:6bb448cdbb00ccb4:017 — Solicite 3 ou 4 imagens responsivas
```yaml
tipo: regua
plataforma: [google-display]
tema: criativo
tarefas: [fazer-briefing-de-criativo]
fonte: fala+pdf:cst_m06_a07_otimizacao_de_criativos.pdf
faixa: 00:11:14–00:11:56
perecivel: false
confianca: alta
versao: 1
```
Se precisar pedir imagens ao designer, solicite 3 ou 4 imagens de anúncios responsivos.
Segundo o professor, essa quantidade dá cerca de 2 meses de otimizações; depois de uns 30 dias, pode pedir um pacote dos outros tamanhos.

### U:6bb448cdbb00ccb4:018 — Repita o processo em todos os conjuntos
```yaml
tipo: procedimento
plataforma: [google-display]
tema: otimizacao
tarefas: [otimizar-anuncios]
fonte: fala+pdf:cst_m06_a07_otimizacao_de_criativos.pdf
faixa: 00:11:56–00:12:36
perecivel: false
confianca: alta
versao: 1
```
Pré-condição: um conjunto de anúncios já foi otimizado.
1. Entre em cada conjunto restante.
2. Analise os anúncios.
3. Pause o anúncio com pior resultado.
4. Suba novos anúncios com modificações, preservando pelo menos uma peça de cada formato necessário.

### U:6bb448cdbb00ccb4:019 — Produção de criativos sustenta a otimização
```yaml
tipo: regra
plataforma: [google-display]
tema: criativo
tarefas: [fazer-briefing-de-criativo, otimizar-anuncios]
fonte: fala+pdf:cst_m06_a07_otimizacao_de_criativos.pdf
faixa: 00:11:14–00:12:52
perecivel: false
confianca: alta
versao: 1
```
Solicite artes ao designer de forma recorrente; a otimização de criativos depende da capacidade de produzir novas peças.