---
type: unidades-aula
status: validado
title: "6.0 - Minha campanha não gasta dinheiro, e agora"
modulo: "004"
ordem: 67
aula_id: 71509baed10c7402
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - cst_m04_a06_minha_campanha_nao_gasta_dinheiro_e_agora_.pdf
  - transcricao.md
extraido_em: 2026-09-16
gerado_por: gpt-5.6-terra
retiradas: []
divisoes: []
fusoes: []
---

# 6.0 - Minha campanha não gasta dinheiro, e agora

## Contexto da aula

A aula apresenta um diagnóstico para campanhas que não gastam dinheiro.
A demonstração usa uma campanha da Rede de Pesquisa no Google Ads.
Ela percorre filtro de data, aprovação, lance, segmentação, estratégia, programação, orçamento e volume.
O professor afirma que os mesmos problemas normalmente também aparecem em YouTube e Facebook.
Se os testes não resolverem, orienta pedir ajuda na Comunidade Sobral de Tráfego.

## Unidades

### U:71509baed10c7402:001 — Confira se o filtro de data mostra o período certo
```yaml
tipo: decisao
plataforma: [google-search]
tema: metricas-e-relatorios
tarefas: [diagnosticar-campanha-sem-gasto]
fonte: fala+pdf:cst_m04_a06_minha_campanha_nao_gasta_dinheiro_e_agora_.pdf
faixa: 00:00:00–00:01:14
perecivel: true
confianca: alta
versao: 1
```
Se a campanha parece zerada, confira se o filtro de data não está mostrando um período antigo; use os dados dos últimos 7 dias ou do dia em curso.

### U:71509baed10c7402:002 — Anúncio sem status qualificado não roda
```yaml
tipo: alerta-ui
plataforma: [google-search]
tema: estrutura-de-campanha
tarefas: [diagnosticar-campanha-sem-gasto]
fonte: fala+pdf:cst_m04_a06_minha_campanha_nao_gasta_dinheiro_e_agora_.pdf
faixa: 00:01:17–00:01:54
perecivel: true
confianca: alta
versao: 1
```
Abra o conjunto e os anúncios e verifique o status. Se o anúncio não estiver como “qualificado”, ele não está rodando; anúncios pendentes em análise ainda podem ser reprovados.

### U:71509baed10c7402:003 — Lance baixo pode impedir a entrega
```yaml
tipo: conceito
plataforma: [google-search]
tema: leilao-e-lances
tarefas: [diagnosticar-campanha-sem-gasto]
fonte: fala+pdf:cst_m04_a06_minha_campanha_nao_gasta_dinheiro_e_agora_.pdf
faixa: 00:01:54–00:02:36
perecivel: false
confianca: alta
versao: 1
```
O lance influencia o leilão que acontece antes de o anúncio aparecer. Lance muito baixo pode fazer a campanha não gastar.

### U:71509baed10c7402:004 — Aumente o lance gradativamente e monitore o gasto
```yaml
tipo: procedimento
plataforma: [google-search]
tema: leilao-e-lances
tarefas: [diagnosticar-campanha-sem-gasto, otimizar-lances]
fonte: fala
faixa: 00:03:02–00:05:20
condicoes: "quando a campanha não gasta por lance baixo"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: identificar que o lance está baixo e manter o orçamento sob controle.
1. Localize o lance no grupo de anúncios ou nas configurações da campanha, conforme o nível em que ele estiver.
2. Aumente o lance gradativamente; quando estiver com pressa, faça aumentos de 1 em 1 hora.
3. Após 1 hora, atualize a tela para conferir se a campanha gastou.
4. Pare de elevar sem controle: o Google pode começar a gastar de uma vez e consumir toda a verba.

### U:71509baed10c7402:005 — Estratégia de lance: comece por cliques antes de conversões
```yaml
tipo: decisao
plataforma: [google-search]
tema: leilao-e-lances
tarefas: [diagnosticar-campanha-sem-gasto, escolher-estrategia-de-lance]
fonte: fala+pdf:cst_m04_a06_minha_campanha_nao_gasta_dinheiro_e_agora_.pdf
faixa: 00:06:57–00:08:35
condicoes: "campanha sem conversões anteriores ou que não gasta com estratégia de conversões"
perecivel: true
confianca: alta
versao: 1
```
Se uma campanha sem conversões começa otimizando para conversões ou valor de conversão e não gasta, mude para cliques.
A sequência apresentada, da mais fácil à mais difícil de gastar, é: parcela de impressões, cliques, conversões e valor de conversão.
Quando a campanha começar a gastar e converter, o professor orienta mudar para conversões.

### U:71509baed10c7402:006 — Amplie palavras-chave quando a segmentação estiver restrita
```yaml
tipo: decisao
plataforma: [google-search]
tema: palavras-chave
tarefas: [diagnosticar-campanha-sem-gasto, otimizar-palavras-chave]
fonte: fala+pdf:cst_m04_a06_minha_campanha_nao_gasta_dinheiro_e_agora_.pdf
faixa: 00:05:20–00:06:56
condicoes: "palavras-chave muito específicas, correspondência restrita ou localização muito limitada"
perecivel: false
confianca: alta
versao: 1
```
Se a segmentação estiver muito restrita, adicione mais palavras-chave ou mude a correspondência de frase ou exata para ampla.
Evite combinar uma localização muito limitada, como CEP ou bairro, com palavras-chave muito específicas.

### U:71509baed10c7402:007 — Confira a programação de anúncios
```yaml
tipo: alerta-ui
plataforma: [google-search]
tema: estrutura-de-campanha
tarefas: [diagnosticar-campanha-sem-gasto]
fonte: fala+pdf:cst_m04_a06_minha_campanha_nao_gasta_dinheiro_e_agora_.pdf
faixa: 00:09:03–00:10:12
perecivel: true
confianca: alta
versao: 1
```
Na lateral, abra “Programação de anúncios” e confira os dias definidos. Uma campanha configurada para rodar apenas na segunda-feira não gastará nos demais dias.

### U:71509baed10c7402:008 — Teste aumento de orçamento só como último caso
```yaml
tipo: decisao
plataforma: [google-search]
tema: orcamento
tarefas: [diagnosticar-campanha-sem-gasto, definir-orcamento]
fonte: fala+pdf:cst_m04_a06_minha_campanha_nao_gasta_dinheiro_e_agora_.pdf
faixa: 00:10:12–00:11:28
condicoes: "depois de conferir os demais pontos do diagnóstico"
perecivel: false
confianca: alta
versao: 1
```
Se tudo já foi conferido, teste elevar um orçamento de R$ 5 para R$ 20 para ver se a campanha começa a gastar.
Quando começar a gastar, reduza para R$ 5 se esse for o valor disponível e acompanhe, pois ela pode gastar muito dinheiro.
O professor diz que orçamento baixo raramente é a causa.

### U:71509baed10c7402:009 — Verifique o volume de pesquisa no Planejador de palavras-chave
```yaml
tipo: procedimento
plataforma: [google-search]
tema: palavras-chave
tarefas: [diagnosticar-campanha-sem-gasto, otimizar-palavras-chave]
fonte: fala+pdf:cst_m04_a06_minha_campanha_nao_gasta_dinheiro_e_agora_.pdf
faixa: 00:10:50–00:12:44
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: a campanha continua sem gastar após ampliar palavras-chave, local e demais configurações.
1. Abra “Ferramentas e configurações” no Google Ads e entre no Planejador de palavras-chave.
2. Selecione “Ver volume de pesquisa e previsões”.
3. Insira as palavras-chave anunciadas e confira a previsão de pesquisas.
4. Se o volume for muito baixo, troque as palavras e pesquise outras opções.

### U:71509baed10c7402:010 — Volume baixo de pesquisa pode explicar a falta de gasto
```yaml
tipo: regua
plataforma: [google-search]
tema: palavras-chave
tarefas: [diagnosticar-campanha-sem-gasto]
fonte: fala
faixa: 00:11:28–00:12:44
perecivel: false
confianca: alta
versao: 1
```
Uma palavra-chave com apenas 50 pesquisas por mês pode indicar que não há procura suficiente para a campanha gastar.

### U:71509baed10c7402:011 — Peça ajuda à comunidade após testar o diagnóstico
```yaml
tipo: decisao
plataforma: [geral]
tema: otimizacao
tarefas: [diagnosticar-campanha-sem-gasto]
fonte: fala+pdf:cst_m04_a06_minha_campanha_nao_gasta_dinheiro_e_agora_.pdf
faixa: 00:12:02–00:13:21
perecivel: false
confianca: alta
versao: 1
nota: "O professor diz que os problemas normalmente também são os mesmos no YouTube e Facebook."
```
Se filtro de data, aprovação, lance, segmentação, estratégia, programação, orçamento e volume já foram testados e a campanha segue sem gastar, publique o caso na Comunidade Sobral de Tráfego informando os testes feitos.