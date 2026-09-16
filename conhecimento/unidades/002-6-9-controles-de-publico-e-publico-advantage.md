---
type: unidades-aula
status: validado
title: "6.9 - Controles de público e Público Advantage"
modulo: "002"
ordem: 39
aula_id: 0dceb6b73f3fbe90
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

# 6.9 - Controles de público e Público Advantage

## Contexto da aula

A aula encerra a configuração de públicos no conjunto de anúncios do Meta.
Explica o Público Advantage como seleção automática e seus controles disponíveis.
Mostra como comparar versões com e sem sugestão de público.
A definição da hierarquia e dos públicos adequados continua dependente do tipo de negócio.
A criação completa de campanhas na prática fica para aulas posteriores.

## Unidades

### U:0dceb6b73f3fbe90:001 — Público Advantage encontra o público automaticamente

```yaml
tipo: conceito
plataforma: [meta]
tema: publicos
tarefas: []
fonte: fala
faixa: "00:01:06–00:01:44"
perecivel: false
confianca: alta
versao: 1
```

O Público Advantage é um público automático: a tecnologia do Meta encontra o público.
Ele pode funcionar ou não conforme o tipo de negócio.

### U:0dceb6b73f3fbe90:002 — Teste Advantage junto das segmentações usuais

```yaml
tipo: regra
plataforma: [meta]
tema: publicos
tarefas: [rodar-testes-e-experimentos, definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: "00:01:44–00:02:30"
perecivel: false
confianca: alta
versao: 1
```

Teste o Público Advantage na conta, mas mantenha as outras seleções de público importantes.
Use uma combinação das duas estratégias; não publique só por deixar o Advantage selecionado.

### U:0dceb6b73f3fbe90:003 — Mudar entre Público Advantage e opções originais

```yaml
tipo: procedimento
plataforma: [meta]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: "00:02:33–00:03:06"
perecivel: true
confianca: alta
versao: 1
```

Pré-condição: conjunto de anúncios aberto com o Público Advantage selecionado.
1. Para usar o público manual, clique em “mudar para as opções originais de público”.
2. Para voltar ao Advantage, use a opção de mudar para o Público Advantage.

### U:0dceb6b73f3fbe90:004 — Controles disponíveis no Público Advantage

```yaml
tipo: alerta-ui
plataforma: [meta]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: "00:03:06–00:05:34"
perecivel: true
confianca: alta
versao: 1
```

Em “Mais opções”, os controles de público incluem localização, idade mínima, exclusões e idiomas.
A idade mínima demonstrada vai até 25; não há faixa etária nem seleção de gênero.
Normalmente, mantenha todos os idiomas.

### U:0dceb6b73f3fbe90:005 — Não priorize Advantage para segmentação muito específica

```yaml
tipo: decisao
plataforma: [meta]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: "00:03:42–00:04:17"
condicoes: "necessidade muito específica de segmentação, principalmente de idade e gênero"
perecivel: false
confianca: alta
versao: 1
```

Se precisa segmentar de modo muito específico, o Público Advantage não deve ser o primeiro teste.

### U:0dceb6b73f3fbe90:006 — Exclua públicos personalizados no controle de público

```yaml
tipo: alerta-ui
plataforma: [meta]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos]
fonte: fala
faixa: "00:03:42–00:04:59"
perecivel: true
confianca: alta
versao: 1
```

No controle de público, exclua públicos personalizados como cadastrados, listas e clientes compradores.
A tela permite várias exclusões, mas não permite excluir público semelhante nem público frio.

### U:0dceb6b73f3fbe90:007 — Compare Advantage com e sem sugestão de público

```yaml
tipo: procedimento
plataforma: [meta]
tema: publicos
tarefas: [rodar-testes-e-experimentos, montar-publicos-personalizados]
fonte: fala
faixa: "00:04:59–00:06:15"
perecivel: true
confianca: alta
versao: 1
```

Pré-condição: teste do Público Advantage planejado.
1. Crie pelo menos 2 conjuntos de anúncio.
2. Deixe um sem sugestão de público e outro com sugestão.
3. Na sugestão, informe o perfil que o Meta deve priorizar antes de expandir a pesquisa.

### U:0dceb6b73f3fbe90:008 — Use captura sem cadastro como sugestão e exclua inscritos

```yaml
tipo: exemplo
plataforma: [meta]
tema: publicos
tarefas: [montar-publicos-personalizados, organizar-hierarquia-e-exclusao-de-publicos]
fonte: fala
faixa: "00:06:15–00:07:49"
perecivel: true
confianca: alta
versao: 1
```

Situação: divulgação de aulas semanais para pessoas que visitaram a página de captura.
O que aconteceu: o professor sugeriu esse público e excluiu, no controle acima, quem chegou à página de obrigado.
Lógica: a sugestão fica para quem visitou a captura, mas não se cadastrou; a exclusão não é feita dentro da sugestão.

### U:0dceb6b73f3fbe90:009 — Quem quase converteu é o público mais qualificado

```yaml
tipo: conceito
plataforma: [meta]
tema: publicos
tarefas: []
fonte: fala
faixa: "00:07:11–00:08:22"
perecivel: false
confianca: alta
versao: 1
```

Em campanha de conversão, o público mais qualificado é quem esteve a um passo de converter, mas não converteu.
No exemplo de cadastro, é quem chegou à página de captura e não enviou o cadastro.

### U:0dceb6b73f3fbe90:010 — Use sugestão para necessidade específica de público

```yaml
tipo: decisao
plataforma: [meta]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses, rodar-testes-e-experimentos]
fonte: fala
faixa: "00:08:57–00:10:17"
condicoes: "teste com necessidade específica de idade ou gênero"
perecivel: true
confianca: alta
versao: 1
```

Se quer especificar o público, dê a sugestão ao Advantage.
Para mulheres com mais de 45 anos, a demonstração usa idade mínima 25 no controle e sugestão de 45 a 65, além de mulheres.
Sem sugestão é indicado para quem não tem tanta necessidade de especificidade.

### U:0dceb6b73f3fbe90:011 — Estruture 4 ou 5 conjuntos para testar sugestões

```yaml
tipo: regua
plataforma: [meta]
tema: testes-e-experimentos
tarefas: [rodar-testes-e-experimentos]
fonte: fala
faixa: "00:10:17–00:10:56"
perecivel: false
confianca: alta
versao: 1
```

Para testar, o professor faria pelo menos 4 ou 5 conjuntos de anúncio.
Use 1 somente com controle de público, sem sugestão, e 4 com sugestões diferentes: público personalizado quente, direcionamento detalhado, público semelhante e segmentação aberta apenas por idade.

### U:0dceb6b73f3fbe90:012 — Combine Advantage e públicos originais conforme a estrutura

```yaml
tipo: regra
plataforma: [meta]
tema: publicos
tarefas: [definir-estrutura-de-campanha, rodar-testes-e-experimentos]
fonte: fala
faixa: "00:10:56–00:11:29"
perecivel: false
confianca: alta
versao: 1
```

Não use apenas o Público Advantage: trabalhe com combinações.
Conforme a estrutura, combine Advantage e público normal na mesma campanha ou separe uma campanha de Advantage e outra com segmentações originais.

### U:0dceb6b73f3fbe90:013 — Retire a sugestão igualando a idade ou duplicando o conjunto

```yaml
tipo: procedimento
plataforma: [meta]
tema: publicos
tarefas: [rodar-testes-e-experimentos, replicar-campanhas-e-grupos]
fonte: fala
faixa: "00:11:30–00:12:40"
perecivel: true
confianca: alta
versao: 1
```

Pré-condição: Público Advantage aberto após a tela ter retornado com sugestão selecionada.
1. Para não sugerir público, iguale a idade da sugestão à idade do controle, como 25 e 25, e deixe todos os gêneros.
2. Ou duplique o conjunto de anúncios para manter a versão anterior sem sugestão pré-selecionada.
3. Depois de clicar para inserir sugestão, não preencher uma sugestão produz o mesmo resultado de não sugerir público.

### U:0dceb6b73f3fbe90:014 — A aula não define a hierarquia ideal por negócio

```yaml
tipo: limite
plataforma: [meta]
tema: publicos
tarefas: []
fonte: fala
faixa: "00:12:40–00:14:21"
perecivel: false
confianca: alta
versao: 1
```

A aula não determina quais públicos ou hierarquia servem para cada tipo de negócio.
As referências dependem de estudo, comunidade, aulas, testes e experiência; a criação completa de campanha fica para depois.