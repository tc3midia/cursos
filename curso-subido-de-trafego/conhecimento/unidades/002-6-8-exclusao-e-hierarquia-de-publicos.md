---
type: unidades-aula
status: validado
title: "6.8 - Exclusão e hierarquia de públicos"
modulo: "002"
ordem: 38
aula_id: c8b6931bb5d322bc
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

# 6.8 - Exclusão e hierarquia de públicos

## Contexto da aula
A aula organiza públicos de conjuntos de anúncios em uma hierarquia de exclusões.
Ela parte de campanhas Meta com públicos personalizados, semelhantes, interesses e públicos frios.
Explica quando preservar ou evitar a interseção, como usar o fator de exclusão no nome e como planejar a estrutura antes da criação.
A aula não apresenta uma hierarquia perfeita ou fórmula única; orienta testar e ajustar a lógica.

## Unidades

### U:c8b6931bb5d322bc:001 — Públicos podem ter pessoas em comum
```yaml
tipo: conceito
plataforma: [meta]
tema: publicos
tarefas: []
fonte: fala
faixa: 00:02:19–00:04:21
perecivel: false
confianca: alta
versao: 1
```
Um público de envolvimento e uma lista completa podem conter a mesma pessoa; essa coincidência entre públicos é uma interseção.

### U:c8b6931bb5d322bc:002 — Conjuntos de anúncios têm inteligências separadas
```yaml
tipo: conceito
plataforma: [meta]
tema: estrutura-de-campanha
tarefas: []
fonte: fala
faixa: 00:04:57–00:06:17
perecivel: false
confianca: alta
versao: 1
```
Mesmo dentro da mesma campanha, cada conjunto de anúncios tem uma inteligência separada e não considera automaticamente a decisão tomada pelo outro conjunto sobre uma pessoa.

### U:c8b6931bb5d322bc:003 — Interseção sem controle pode repetir entrega
```yaml
tipo: decisao
plataforma: [meta]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos]
fonte: fala
faixa: 00:04:21–00:06:59
perecivel: false
confianca: alta
versao: 1
```
Se a mesma pessoa estiver em conjuntos diferentes sem exclusão, ela pode receber anúncios mais de uma vez sem que os conjuntos controlem isso entre si.
Repetir a entrega pode ser bom quando há controle; o problema é a repetição descontrolada.

### U:c8b6931bb5d322bc:004 — Hierarquia busca evitar interseção entre conjuntos
```yaml
tipo: conceito
plataforma: [meta]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos]
fonte: fala
faixa: 00:06:59–00:08:17
perecivel: false
confianca: alta
versao: 1
```
Hierarquia de públicos é uma escadinha de exclusões entre conjuntos para tentar impedir que a mesma pessoa receba anúncio em mais de um deles.
Ela busca garantir a separação, mas não garante 100%.

### U:c8b6931bb5d322bc:005 — Exclua os públicos anteriores do público seguinte
```yaml
tipo: procedimento
plataforma: [meta]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos]
fonte: fala
faixa: 00:08:51–00:10:57
perecivel: false
confianca: alta
versao: 1
```
Pré-condição: os públicos estão ordenados como A, B, C, D e E para a explicação.
1. Anuncie primeiro para o público A.
2. Ao criar o público B, exclua dele o público A.
3. Ao criar o público C, exclua dele B e A.
4. Repita a escadinha: cada novo público exclui todos os públicos anteriores.

### U:c8b6931bb5d322bc:006 — Duplicar conjunto para montar a escadinha de exclusões
```yaml
tipo: procedimento
plataforma: [meta]
tema: estrutura-de-campanha
tarefas: [replicar-campanhas-e-grupos, organizar-hierarquia-e-exclusao-de-publicos]
fonte: fala
faixa: 00:12:07–00:14:21
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: existe um conjunto de anúncios com o primeiro público já selecionado.
1. Duplique o conjunto existente em vez de criar o próximo do zero.
2. No conjunto copiado, selecione o público adicionado e use a opção de excluir.
3. Inclua o próximo público como público principal.
4. Duplique o último conjunto criado e repita, mantendo excluídos os públicos anteriores.

### U:c8b6931bb5d322bc:007 — Ordem da hierarquia altera as exclusões
```yaml
tipo: regra
plataforma: [meta]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos]
fonte: fala
faixa: 00:14:22–00:15:43
perecivel: false
confianca: alta
versao: 1
```
Defina deliberadamente qual público entra primeiro e qual entra por último: inverter a ordem muda quem cada público posterior exclui.

### U:c8b6931bb5d322bc:008 — Priorize públicos menores e mais qualificados
```yaml
tipo: regra
plataforma: [meta]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos]
fonte: fala
faixa: 00:15:04–00:16:23
perecivel: false
confianca: alta
versao: 1
```
Coloque no topo da hierarquia os públicos menores e mais qualificados; deixe abaixo os públicos maiores e menos qualificados.

### U:c8b6931bb5d322bc:009 — Exemplos de prioridade entre públicos quentes e frios
```yaml
tipo: exemplo
plataforma: [meta]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos]
fonte: fala
faixa: 00:15:43–00:16:23
perecivel: false
confianca: alta
versao: 1
```
Situação: campanha de venda para um e-commerce.
O que aconteceu: entram acima iniciadores de checkout, pessoas que adicionaram ao carrinho, visitantes de produto ou site sem compra e envolvimento recente de 2 ou 3 dias; abaixo ficam envolvimentos de 60 ou 90 dias, visualizadores de vídeo de 365 dias, lookalikes e interesses.
Lógica: a ordem segue tamanho e qualificação do público.

### U:c8b6931bb5d322bc:010 — Use uma lógica mesmo quando a qualidade for incerta
```yaml
tipo: decisao
plataforma: [meta]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos]
fonte: fala
faixa: 00:16:23–00:17:53
perecivel: false
confianca: alta
versao: 1
```
Quando não souber qual público é mais qualificado, use o feeling para ordenar seguindo uma lógica e ajuste depois pelos testes.

### U:c8b6931bb5d322bc:011 — Faça exclusões entre públicos muito diferentes
```yaml
tipo: decisao
plataforma: [meta]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos]
fonte: fala
faixa: 00:18:01–00:19:29
perecivel: false
confianca: alta
versao: 1
```
Se os públicos forem muito diferentes, como um público quente versus um frio, faça exclusões.
Faça também quando quiser garantir que cada conjunto anuncie somente para seu público, sem repetir pessoas.

### U:c8b6931bb5d322bc:012 — Não exclua públicos de qualidade extremamente parecida
```yaml
tipo: decisao
plataforma: [meta]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos]
fonte: fala
faixa: 00:19:29–00:20:09
condicoes: "públicos extremamente parecidos quanto à qualidade"
perecivel: false
confianca: alta
versao: 1
```
Se os públicos tiverem qualidade extremamente parecida, pode não fazer exclusão entre eles e começar as exclusões no público seguinte.

### U:c8b6931bb5d322bc:013 — Não exclua entre públicos muito pequenos
```yaml
tipo: decisao
plataforma: [meta]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos]
fonte: fala
faixa: 00:20:12–00:21:42
condicoes: "audiências muito pequenas"
perecivel: false
confianca: alta
versao: 1
```
Quando os públicos forem muito pequenos, anuncie para eles sem exclusões entre si e passe a excluir esses públicos dos públicos maiores abaixo.

### U:c8b6931bb5d322bc:014 — Não faça exclusões entre públicos frios
```yaml
tipo: regra
plataforma: [meta]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos]
fonte: fala
faixa: 00:20:55–00:23:13
perecivel: false
confianca: alta
versao: 1
```
Entre públicos frios, não faça exclusões; mantenha a exclusão dos públicos quentes nos públicos frios.
O professor afirma, com base nos próprios testes, que entre públicos frios funciona melhor sem exclusão.

### U:c8b6931bb5d322bc:015 — Teste adicionar ou remover exclusões
```yaml
tipo: decisao
plataforma: [meta]
tema: testes-e-experimentos
tarefas: [rodar-testes-e-experimentos, organizar-hierarquia-e-exclusao-de-publicos]
fonte: fala
faixa: 00:22:26–00:23:13
perecivel: false
confianca: alta
versao: 1
```
Quando quiser testar, adicione ou remova exclusões para observar o que acontece na campanha.

### U:c8b6931bb5d322bc:016 — Fator de exclusão indica quantos níveis o público exclui
```yaml
tipo: conceito
plataforma: [meta]
tema: nomenclatura
tarefas: [nomear-campanhas, organizar-hierarquia-e-exclusao-de-publicos]
fonte: fala
faixa: 00:23:13–00:25:20
perecivel: false
confianca: alta
versao: 1
```
O fator de exclusão é o número no início do nome do público que indica quantos níveis anteriores são excluídos.
Um público 0,0 não tem exclusões; um 0,3 exclui os públicos 0,2, 0,1 e 0,0.

### U:c8b6931bb5d322bc:017 — Mantenha o fator de exclusão entre campanhas
```yaml
tipo: regra
plataforma: [meta]
tema: nomenclatura
tarefas: [nomear-campanhas, organizar-hierarquia-e-exclusao-de-publicos]
fonte: fala
faixa: 00:25:21–00:26:32
perecivel: false
confianca: alta
versao: 1
```
Mesmo separando públicos quentes e frios em campanhas diferentes, mantenha o fator de exclusão conforme os públicos excluídos na hierarquia total.

### U:c8b6931bb5d322bc:018 — Públicos no mesmo nível podem repetir o fator
```yaml
tipo: decisao
plataforma: [meta]
tema: nomenclatura
tarefas: [nomear-campanhas, organizar-hierarquia-e-exclusao-de-publicos]
fonte: fala
faixa: 00:26:33–00:27:13
condicoes: "públicos extremamente parecidos quanto à qualidade"
perecivel: false
confianca: alta
versao: 1
```
Se considerar públicos extremamente parecidos em qualidade, mantenha-os no mesmo nível da hierarquia e repita o fator de exclusão.

### U:c8b6931bb5d322bc:019 — Desenhe a hierarquia antes de criar a campanha
```yaml
tipo: regra
plataforma: [meta]
tema: estrutura-de-campanha
tarefas: [definir-estrutura-de-campanha, organizar-hierarquia-e-exclusao-de-publicos]
fonte: fala
faixa: 00:27:14–00:28:31
perecivel: false
confianca: alta
versao: 1
```
Antes de criar a campanha, desenhe os públicos, a estrutura e a hierarquia que serão usados.
O professor afirma que esse planejamento reduz a chance de erro e melhora a eficiência na criação.

### U:c8b6931bb5d322bc:020 — Comece separando quentes e frios na hierarquia
```yaml
tipo: decisao
plataforma: [meta]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos]
fonte: fala
faixa: 00:28:32–00:30:25
condicoes: "início da aplicação da técnica"
perecivel: false
confianca: alta
versao: 1
```
Quando estiver começando, diferencie públicos quentes dos frios na hierarquia, usando uma hierarquia para cada grupo.
Depois, teste alterações, mantenha públicos no mesmo nível quando houver dúvida e mude a hierarquia se não estiver funcionando.