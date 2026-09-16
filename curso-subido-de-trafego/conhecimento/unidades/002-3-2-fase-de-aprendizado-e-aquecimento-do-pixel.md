---
type: unidades-aula
status: validado
title: "3.2 - Fase de aprendizado e aquecimento do pixel"
modulo: "002"
ordem: 23
aula_id: 13b2d9f52cf439b3
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - transcricao.md
extraido_em: 2026-09-15
gerado_por: gpt-5.6-terra
retiradas: ["U:13b2d9f52cf439b3:003", "U:13b2d9f52cf439b3:004", "U:13b2d9f52cf439b3:009", "U:13b2d9f52cf439b3:018"]
divisoes: ["U:13b2d9f52cf439b3:009 → U:13b2d9f52cf439b3:024, U:13b2d9f52cf439b3:025", "U:13b2d9f52cf439b3:018 → U:13b2d9f52cf439b3:028, U:13b2d9f52cf439b3:029"]
fusoes: ["U:13b2d9f52cf439b3:003, U:13b2d9f52cf439b3:004 → U:13b2d9f52cf439b3:021"]
---

# 3.2 - Fase de aprendizado e aquecimento do pixel

## Contexto da aula

A aula explica os estados de veiculação de conjuntos de anúncios Meta em campanhas de conversão.
Ela relaciona a fase de aprendizado ao evento de conversão escolhido e à quantidade de pessoas que o ativam.
Mostra opções para lidar com aprendizado limitado e quando não alterar o conjunto.
Também define aquecimento do pixel, critica o funil de pixel como primeira escolha e aponta o processo de conversão como parte do diagnóstico.

## Unidades

### U:13b2d9f52cf439b3:001 — Escolher o evento pelo resultado buscado
```yaml
tipo: decisao
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [definir-conversoes-e-metas]
fonte: fala
faixa: "00:00:00–00:00:53"
perecivel: false
confianca: alta
versao: 2
```
Se a campanha busca compras, leads, cadastros ou registro em uma página, selecione esse resultado como evento de conversão por evento padrão, evento personalizado ou conversão personalizada.

### U:13b2d9f52cf439b3:002 — Conjunto de anúncios tem três estados de veiculação
```yaml
tipo: conceito
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [ler-metricas-e-relatorios]
fonte: fala
faixa: "00:00:53–00:01:33"
perecivel: true
confianca: media
versao: 2
nota: A transcrição chama o status de conjunto pausado de “nativo”; o nome foi preservado sem normalização.
```
Um conjunto de anúncios em veiculação pode aparecer como em aprendizado, ativo ou aprendizado limitado. Se estiver pausado, a fala diz que o status é “nativo”.

### U:13b2d9f52cf439b3:005 — Resultados podem ficar instáveis por sete dias
```yaml
tipo: regua
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [ler-metricas-e-relatorios]
fonte: fala
faixa: "00:02:15–00:03:48"
perecivel: false
confianca: alta
versao: 2
```
Durante a fase de aprendizado, os resultados podem ser mais instáveis por um período de 7 dias.

### U:13b2d9f52cf439b3:006 — Mais de 50 conversões em sete dias é a base indicada
```yaml
tipo: regua
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [ler-metricas-e-relatorios]
fonte: fala
faixa: "00:03:00–00:05:13"
condicoes: A referência varia de conta para conta e é apresentada como base do Meta.
perecivel: false
confianca: alta
versao: 2
```
Se, ao longo de 7 dias, a campanha não fizer mais de 50 conversões, ela pode ficar com aprendizado limitado. O número 50 é uma base para orientação, não uma regra constante.

### U:13b2d9f52cf439b3:007 — Aprendizado limitado pode ocorrer por restrições do conjunto
```yaml
tipo: conceito
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [diagnosticar-campanha-sem-gasto]
fonte: fala
faixa: "00:03:48–00:04:30"
perecivel: true
confianca: alta
versao: 2
```
O aviso de aprendizado limitado informa que o conjunto não gera conversões suficientes para sair da fase; tamanho de público, controle de custo, orçamento ou outras configurações podem limitá-lo.

### U:13b2d9f52cf439b3:008 — Menos de 50 eventos não determina sozinho o status
```yaml
tipo: exemplo
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [ler-metricas-e-relatorios]
fonte: fala
faixa: "00:04:30–00:05:13"
perecivel: true
confianca: alta
versao: 2
```
Situação: um grupo de anúncios teve 13 resultados na última semana.
O que aconteceu: ele aparecia como ativo, embora não tivesse 50 eventos.
Lógica: o limiar de 50 é uma referência, pois o status não depende sempre desse número.

### U:13b2d9f52cf439b3:010 — Manter aprendizado limitado que converte bem
```yaml
tipo: decisao
plataforma: [meta]
tema: otimizacao
tarefas: [ler-metricas-e-relatorios]
fonte: fala
faixa: "00:06:11–00:06:53"
condicoes: O grupo em aprendizado limitado gera conversões a baixo custo e atinge o público-alvo.
perecivel: false
confianca: alta
versao: 2
```
Se o grupo em aprendizado limitado gera bons resultados, conversões a baixo custo e alcança o público-alvo, mantenha-o sem fazer alterações.

### U:13b2d9f52cf439b3:011 — Otimização pode devolver conjunto ativo ao aprendizado
```yaml
tipo: conceito
plataforma: [meta]
tema: otimizacao
tarefas: [otimizar-publicos-e-segmentacoes, otimizar-anuncios]
fonte: fala
faixa: "00:06:54–00:08:13"
perecivel: false
confianca: alta
versao: 2
```
Ao melhorar público ou alterar criativos de um grupo ativo com base em dados, ele pode voltar para em aprendizado e depois retornar ao estado ativo.

### U:13b2d9f52cf439b3:012 — Um ou dois grupos em aprendizado limitado são normais
```yaml
tipo: regua
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [ler-metricas-e-relatorios]
fonte: fala
faixa: "00:08:13–00:08:51"
perecivel: false
confianca: alta
versao: 2
```
Ter 1 ou 2 grupos de anúncios em aprendizado limitado pode ser normal e padrão.

### U:13b2d9f52cf439b3:013 — Aquecer o pixel é gerar informações pelos eventos
```yaml
tipo: conceito
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: "00:09:36–00:10:34"
perecivel: false
confianca: alta
versao: 2
```
Aquecer o pixel é gerar tráfego e informações para o pixel, eventos padrão, eventos personalizados e conversões personalizadas por meio das pessoas que acessam páginas e ativam esses eventos.

### U:13b2d9f52cf439b3:014 — Evento com menos ocorrências está menos aquecido
```yaml
tipo: exemplo
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [ler-metricas-e-relatorios]
fonte: fala
faixa: "00:09:37–00:11:51"
perecivel: false
confianca: alta
versao: 2
```
Situação: um e-commerce registrou 5 mil ViewContent, mil AddToCart, 100 InitiateCheckout e 5 Purchase.
O que aconteceu: Purchase ficou menos aquecido que os demais eventos porque o Meta tinha informação de apenas 5 pessoas que compraram.
Lógica: eventos com mais ativações dão ao pixel mais informação sobre as pessoas que os realizam.

### U:13b2d9f52cf439b3:015 — Aquecer o pixel exige anunciar por longos períodos
```yaml
tipo: regra
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [criar-campanha]
fonte: fala
faixa: "00:11:52–00:12:37"
perecivel: false
confianca: alta
versao: 2
```
Aqueça o pixel anunciando durante longos períodos de tempo.

### U:13b2d9f52cf439b3:016 — Otimizar para o evento final desejado
```yaml
tipo: regra
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [definir-conversoes-e-metas]
fonte: fala
faixa: "00:12:37–00:13:52"
perecivel: false
confianca: alta
versao: 2
```
Otimize a campanha para o evento que você busca, como Purchase quando o objetivo é compra, mesmo que o pixel ainda não tenha muitos dados.

### U:13b2d9f52cf439b3:017 — Mais checkout iniciado pode não gerar mais compras
```yaml
tipo: exemplo
plataforma: [meta]
tema: destino-e-landing-page
tarefas: [otimizar-landing-page]
fonte: fala
faixa: "00:13:53–00:15:10"
perecivel: false
confianca: alta
versao: 2
```
Situação: 100 pessoas iniciam checkout e 1 compra é concluída, com conversão de 1%.
O que aconteceu: ao levar mil pessoas ao checkout, haveria 10 compras se a conversão continuasse em 1%; ao corrigir o checkout, 100 visitantes poderiam gerar 10 compras.
Lógica: baixa compra após checkout pode indicar problema no checkout, como falta de confiança ou ausência de tamanhos, e não falta de aquecimento do pixel.

### U:13b2d9f52cf439b3:019 — Avaliar o processo de conversão além do pixel
```yaml
tipo: conceito
plataforma: [meta]
tema: destino-e-landing-page
tarefas: [otimizar-landing-page]
fonte: fala
faixa: "00:15:10–00:16:19"
perecivel: false
confianca: alta
versao: 3
nota: "Correção manual de C02: preservar a ressalva de que a falta de aquecimento do pixel pode explicar a ausência de compras em alguns casos, mas não na maioria."
```
O processo de conversão é o caminho percorrido após o clique no anúncio. A falta de aquecimento do pixel pode explicar a ausência de compras em alguns casos, mas não na maioria. Investigue também problemas no checkout, na headline, na oferta ou no público.

### U:13b2d9f52cf439b3:020 — Alternância entre aprendizado e ativo é constante
```yaml
tipo: conceito
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [ler-metricas-e-relatorios, otimizar-publicos-e-segmentacoes, otimizar-anuncios]
fonte: fala
faixa: "00:16:25–00:17:43"
perecivel: false
confianca: alta
versao: 2
nota: "Classificação por gpt-5.6-sol: tarefa genérica inexistente substituída pelas tarefas específicas atuais."
```
A campanha pode passar repetidamente de em aprendizado para ativo e de ativo para em aprendizado; otimizações conscientes fazem parte desse processo.

### U:13b2d9f52cf439b3:021 — Campanha de conversão entra em aprendizado
```yaml
tipo: regra
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [criar-campanha]
fonte: fala
faixa: "00:01:33–00:02:14"
perecivel: true
confianca: alta
versao: 1
```
Toda campanha de venda ou conversão criada entra na fase em aprendizado; passe o mouse sobre o status e leia a explicação exibida.

### U:13b2d9f52cf439b3:022 — Meta busca identificar quem realiza o evento
```yaml
tipo: conceito
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [definir-conversoes-e-metas]
fonte: fala
faixa: "00:02:15–00:03:00"
perecivel: false
confianca: alta
versao: 1
```
Na fase de aprendizado, o Meta tenta identificar quais pessoas do público realizam o evento de conversão definido, como comprar.

### U:13b2d9f52cf439b3:023 — Buscar campanhas ativas sem tratar aprendizado limitado como desastre
```yaml
tipo: decisao
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [ler-metricas-e-relatorios]
fonte: fala
faixa: "00:05:31–00:06:11"
perecivel: false
confianca: alta
versao: 2
nota: "Classificação por gpt-5.6-sol: tarefa genérica inexistente substituída pelas tarefas específicas atuais. Correção manual de C01: explicitar a preferência por todas as campanhas ativas, preservando a ressalva contra sair do aprendizado limitado a qualquer custo."
```
Quando um conjunto estiver em aprendizado limitado, busque sair dessa fase: o ideal é que todas as suas campanhas fiquem ativas. Não trate esse estado como fim do mundo nem tente evitá-lo a qualquer custo.

### U:13b2d9f52cf439b3:024 — Aumentar orçamento pode ajudar a sair do aprendizado limitado
```yaml
tipo: decisao
plataforma: [meta]
tema: orcamento
tarefas: [definir-orcamento]
fonte: fala
faixa: "00:05:31–00:06:53"
condicoes: Conjunto de anúncios em aprendizado limitado.
perecivel: false
confianca: alta
versao: 1
```
Se o conjunto estiver em aprendizado limitado, você pode aumentar seu orçamento.

### U:13b2d9f52cf439b3:025 — Otimizar público e criativos em aprendizado limitado
```yaml
tipo: procedimento
plataforma: [meta]
tema: otimizacao
tarefas: [otimizar-publicos-e-segmentacoes, otimizar-anuncios]
fonte: fala
faixa: "00:05:31–00:06:53"
condicoes: Conjunto de anúncios em aprendizado limitado.
perecivel: false
confianca: alta
versao: 1
```
Pré-condição: o conjunto está em aprendizado limitado.
1. Amplie o público se ele estiver muito pequeno.
2. Melhore os criativos se o grupo não estiver gerando resultado.

### U:13b2d9f52cf439b3:026 — Não deixar de otimizar por receio do aprendizado
```yaml
tipo: regra
plataforma: [meta]
tema: otimizacao
tarefas: [otimizar-publicos-e-segmentacoes, otimizar-anuncios]
fonte: fala
faixa: "00:07:35–00:08:51"
perecivel: false
confianca: alta
versao: 1
nota: "Classificação por gpt-5.6-sol: tarefa genérica inexistente substituída pelas tarefas específicas atuais."
```
Não abandone melhorias de campanha apenas porque um conjunto ativo pode retornar ao estado em aprendizado.

### U:13b2d9f52cf439b3:027 — Muitos conjuntos em aprendizado limitado são mau sinal
```yaml
tipo: decisao
plataforma: [meta]
tema: otimizacao
tarefas: [diagnosticar-campanha-sem-gasto, definir-orcamento, otimizar-publicos-e-segmentacoes, otimizar-anuncios]
fonte: fala
faixa: "00:07:35–00:08:13"
condicoes: Todos os conjuntos estão em aprendizado limitado.
perecivel: false
confianca: alta
versao: 1
nota: "Classificação por gpt-5.6-sol: tarefa genérica inexistente substituída pelas tarefas específicas atuais."
```
Se tudo estiver em aprendizado limitado, trate como sinal de pouca verba ou de campanhas que não estão gerando resultado e otimize as campanhas.

### U:13b2d9f52cf439b3:028 — Testar passo anterior não é a primeira opção
```yaml
tipo: decisao
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [definir-conversoes-e-metas, rodar-testes-e-experimentos]
fonte: fala
faixa: "00:12:37–00:14:30"
condicoes: A otimização para o evento final não funciona.
perecivel: false
confianca: alta
versao: 1
```
Se otimizar para o evento final não funcionar, teste a otimização para uma etapa anterior, como InitiateCheckout, para verificar se ela gera compras; não use isso como primeira opção.

### U:13b2d9f52cf439b3:029 — Funil de pixel pode funcionar, mas não é a primeira escolha
```yaml
tipo: decisao
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [definir-conversoes-e-metas]
fonte: fala
faixa: "00:14:30–00:15:45"
perecivel: false
confianca: alta
versao: 1
```
Quando considerar o funil de pixel, reconheça que ele pode funcionar, mas prefira primeiro anunciar e gastar dinheiro durante o tempo necessário.

### U:13b2d9f52cf439b3:030 — Aqueça pixel anunciando e melhorando a conversão
```yaml
tipo: procedimento
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [criar-campanha, otimizar-landing-page]
fonte: fala
faixa: "00:15:45–00:17:07"
perecivel: false
confianca: alta
versao: 1
```
Pré-condição: pixel e eventos recebem ativações pelo site.
1. Anuncie durante um bom tempo para fornecer informações ao pixel e aos eventos.
2. Melhore o processo de conversão depois do clique no anúncio.

### U:13b2d9f52cf439b3:031 — Mais ativações ajudam a ter conjuntos ativos
```yaml
tipo: conceito
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos, criar-campanha, otimizar-landing-page]
fonte: fala
faixa: "00:16:25–00:17:52"
perecivel: false
confianca: alta
versao: 2
nota: "Classificação por gpt-5.6-sol: tarefa genérica inexistente substituída pelas tarefas específicas atuais. Correção manual residual: ampliar a faixa para incluir o trecho de alternância entre estados e orientações de melhoria, preservando a janela anterior."
```
A quantidade de pessoas que ativa o pixel influencia o aquecimento e a transição do conjunto entre em aprendizado, aprendizado limitado e ativo; anuncie, melhore a conversão e otimize campanhas.

### U:13b2d9f52cf439b3:032 — Pré-condição para criar a campanha de conversão
```yaml
tipo: regra
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos, criar-campanha]
fonte: fala
faixa: "00:00:00–00:00:29"
perecivel: false
confianca: alta
versao: 1
nota: "Autoria: gpt-5.6-sol. Adição manual para cobrir F01: explicitar a pré-condição de pixel instalado e evento ou conversão criados."
```
Antes de criar a campanha de conversão, tenha o pixel instalado e um evento padrão, evento personalizado ou conversão personalizada criado.

### U:13b2d9f52cf439b3:033 — Solicitar um evento não garante o resultado
```yaml
tipo: conceito
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [definir-conversoes-e-metas]
fonte: fala
faixa: "00:00:53–00:01:33"
perecivel: false
confianca: alta
versao: 1
nota: "Autoria: gpt-5.6-sol. Adição manual para cobrir F03: preservar a ressalva de que solicitar o evento não garante os resultados."
```
Selecionar um evento de conversão informa ao Meta o resultado buscado, mas não garante que ele consiga entregar esses resultados.

### U:13b2d9f52cf439b3:034 — Painel mostra 20 eventos desde a última edição
```yaml
tipo: exemplo
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [ler-metricas-e-relatorios]
fonte: fala
faixa: "00:03:00–00:03:48"
perecivel: true
confianca: alta
versao: 1
nota: "Autoria: gpt-5.6-sol. Adição manual para cobrir F04: preservar o número 20 e a referência desde a última edição no exemplo do painel."
```
Situação: o professor consulta no painel a contagem de eventos de otimização.
O que aconteceu: o painel mostrava 20 eventos de otimização desde a última edição.
Lógica: leia essa contagem considerando sua referência à última edição.

### U:13b2d9f52cf439b3:035 — Critério de conversões suficientes para o estado ativo
```yaml
tipo: conceito
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [ler-metricas-e-relatorios]
fonte: fala
faixa: "00:03:48–00:04:30"
perecivel: true
confianca: alta
versao: 1
nota: "Autoria: gpt-5.6-sol. Adição manual para cobrir C01 r2: registrar o critério operacional do estado ativo, conforme evidência Terra."
```
O estado ativo indica que o conjunto gerou conversões suficientes para identificar o público ao qual deve direcionar a verba.

### U:13b2d9f52cf439b3:036 — Verificações do processo de conversão após o clique
```yaml
tipo: procedimento
plataforma: [meta]
tema: destino-e-landing-page
tarefas: [otimizar-landing-page, ler-metricas-e-relatorios]
fonte: fala
faixa: "00:15:10–00:15:45"
perecivel: false
confianca: alta
versao: 1
nota: "Autoria: gpt-5.6-sol. Adição manual para cobrir C02 r2: registrar a lista de verificações do diagnóstico após o clique, conforme evidência Terra."
```
Pré-condição: é necessário diagnosticar o processo de conversão após o clique no anúncio.
1. Verifique o site e a página de destino.
2. Examine as métricas do processo de conversão.
3. Confira quantas pessoas chegam ao checkout.
4. Investigue os motivos pelos quais essas pessoas não compram.
