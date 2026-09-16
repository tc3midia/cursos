---
type: unidades-aula
status: validado
title: "6.6 - Criativo dinâmico"
modulo: "002"
ordem: 36
aula_id: ba4ba6bb97808a45
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

# 6.6 - Criativo dinâmico

## Contexto da aula

A aula apresenta o criativo dinâmico na configuração de anúncios da Meta.
Explica em quais testes o recurso pode entrar e por que ele não é prioridade para iniciantes.
Também diferencia regras de data final conforme o tipo de orçamento.
Limite de gasto, CBO, ABO e a programação ligada ao orçamento são assuntos já tratados em outras aulas.

## Unidades

### U:ba4ba6bb97808a45:001 — Criativo dinâmico não é usado na maioria das campanhas
```yaml
tipo: regra
plataforma: [meta]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:00:00–00:01:11
perecivel: true
confianca: alta
versao: 1
```
Na maioria das campanhas, não utilize criativo dinâmico.

### U:ba4ba6bb97808a45:002 — Use criativo dinâmico para testes específicos
```yaml
tipo: decisao
plataforma: [meta]
tema: testes-e-experimentos
tarefas: [rodar-testes-e-experimentos]
fonte: fala
faixa: 00:00:00–00:01:11
perecivel: false
confianca: alta
versao: 1
```
Se quiser testar rapidamente muitas variações ou verificar se o criativo dinâmico funciona na campanha, use-o como teste de anúncios.

### U:ba4ba6bb97808a45:003 — Adicione múltiplos recursos ao anúncio dinâmico
```yaml
tipo: procedimento
plataforma: [meta]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:01:11–00:02:12
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: criativo dinâmico selecionado e anúncio aberto.
1. Selecione mais de uma imagem ou vídeo como recurso do anúncio.
2. Adicione várias versões do texto e dos títulos.
3. Respeite o limite de 5 sugestões de texto mostrado na interface.

### U:ba4ba6bb97808a45:004 — Criativo dinâmico combina recursos e separa seus resultados
```yaml
tipo: conceito
plataforma: [meta]
tema: criativo
tarefas: []
fonte: fala
faixa: 00:02:12–00:02:55
perecivel: false
confianca: alta
versao: 1
```
O recurso pode reunir imagens e vídeos no mesmo anúncio; a Meta combina os elementos para identificar o que funciona melhor.
Depois da veiculação, é possível consultar separadamente o desempenho de vídeos, imagens, textos e títulos.

### U:ba4ba6bb97808a45:005 — Compare criativo dinâmico com variações em anúncios separados
```yaml
tipo: decisao
plataforma: [meta]
tema: testes-e-experimentos
tarefas: [rodar-testes-e-experimentos]
fonte: fala
faixa: 00:02:55–00:03:31
perecivel: false
confianca: alta
versao: 1
```
Se quiser avaliar a abordagem, teste 10 imagens em anúncios separados contra essas mesmas imagens reunidas em um anúncio com criativo dinâmico.

### U:ba4ba6bb97808a45:006 — Iniciante deve deixar o criativo dinâmico desativado
```yaml
tipo: decisao
plataforma: [meta]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:03:31–00:04:06
perecivel: true
confianca: alta
versao: 1
```
Quando estiver começando, desative o criativo dinâmico e registre esse teste para realizar depois.
O professor orienta testar futuramente, perguntar a alguém que já testou ou levar a dúvida à Comunidade Sobral.

### U:ba4ba6bb97808a45:007 — Orçamento diário permite data final opcional
```yaml
tipo: decisao
plataforma: [meta]
tema: orcamento
tarefas: [definir-orcamento]
fonte: fala
faixa: 00:04:06–00:04:47
perecivel: true
confianca: alta
versao: 1
```
Se o orçamento for diário, defina ou não uma data de término; a campanha pode continuar rodando até ser pausada.

### U:ba4ba6bb97808a45:008 — Orçamento total exige data de término
```yaml
tipo: decisao
plataforma: [meta]
tema: orcamento
tarefas: [definir-orcamento]
fonte: fala
faixa: 00:04:06–00:05:20
condicoes: "orçamento total"
perecivel: true
confianca: alta
versao: 1
```
Se o orçamento for total, defina obrigatoriamente a data de término, pois ele corresponde ao gasto entre uma data inicial e uma final.

### U:ba4ba6bb97808a45:009 — A aula não aprofunda limite de gasto e programação
```yaml
tipo: limite
plataforma: [meta]
tema: orcamento
tarefas: []
fonte: fala
faixa: 00:04:48–00:05:20
perecivel: false
confianca: alta
versao: 1
```
A aula não retoma limite de gasto, CBO, ABO nem a programação associada aos tipos de orçamento; esses tópicos foram tratados em aulas anteriores.