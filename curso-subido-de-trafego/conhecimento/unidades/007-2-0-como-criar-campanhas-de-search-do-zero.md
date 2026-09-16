---
type: unidades-aula
status: validado
title: "2.0 - Como criar campanhas de Search do zero"
modulo: "007"
ordem: 114
aula_id: fa80cd201007f33e
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - cst_m07_a02_como_criar_campanhas_de _search_do_zero.pdf
  - transcricao.md
extraido_em: 2026-09-16
gerado_por: gpt-5.6-terra
retiradas: []
divisoes: []
fusoes: []
---

# 2.0 - Como criar campanhas de Search do zero

## Contexto da aula

A aula demonstra a criação de uma campanha de Rede de Pesquisa no Google Ads Editor.
O professor apresenta o processo como menos intuitivo que criar no Google Ads online.
A configuração do zero serve para entender as opções, mas a recomendação recorrente é duplicar uma campanha semelhante.
Também são mostrados grupo de anúncios, segmentações, palavras-chave, anúncios e extensões.

## Unidades

### U:fa80cd201007f33e:001 — Prefira duplicar uma campanha semelhante
```yaml
tipo: decisao
plataforma: [ads-editor]
tema: estrutura-de-campanha
tarefas: [replicar-campanhas-e-grupos]
fonte: fala+pdf:cst_m07_a02_como_criar_campanhas_de _search_do_zero.pdf
faixa: 00:00:00–00:03:51
condicoes: "ao criar uma nova campanha de Search"
perecivel: false
confianca: alta
versao: 1
```
Se for criar uma nova campanha de Search, normalmente duplique uma campanha já existente em vez de iniciar do zero.
Selecione como origem uma campanha do mesmo tipo e objetivo, para reduzir as alterações até a campanha nova.

### U:fa80cd201007f33e:002 — Criar campanha não exige seleção prévia
```yaml
tipo: alerta-ui
plataforma: [ads-editor]
tema: estrutura-de-campanha
tarefas: [criar-campanha]
fonte: fala+pdf:cst_m07_a02_como_criar_campanhas_de _search_do_zero.pdf
faixa: 00:03:51–00:04:29
perecivel: true
confianca: alta
versao: 1
```
Para criar uma campanha do zero, deixe a conta inteira selecionada e use “adicionar uma nova campanha”; não é preciso selecionar campanhas de Search antes.

### U:fa80cd201007f33e:003 — Nomear e isolar a campanha em edição
```yaml
tipo: procedimento
plataforma: [ads-editor]
tema: nomenclatura
tarefas: [criar-campanha, nomear-campanhas]
fonte: fala+pdf:cst_m07_a02_como_criar_campanhas_de _search_do_zero.pdf
faixa: 00:03:51–00:06:22
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: uma nova campanha foi adicionada no Google Ads Editor.
1. Dê nome à campanha criada.
2. Clique no nome da própria campanha para exibir somente os itens dela, em vez de toda a conta.
3. Use as marcações de erro como guia dos campos que ainda precisam ser configurados.

### U:fa80cd201007f33e:004 — Campanha exige orçamento
```yaml
tipo: regua
plataforma: [ads-editor]
tema: orcamento
tarefas: [criar-campanha, definir-orcamento]
fonte: fala
faixa: 00:05:46–00:06:22
perecivel: true
confianca: alta
versao: 1
```
Uma campanha sem orçamento aparece com erro. No exemplo, o professor preenche R$50,00 para resolver essa pendência.

### U:fa80cd201007f33e:005 — Target CPA requer CPA desejado diferente de zero
```yaml
tipo: decisao
plataforma: [ads-editor]
tema: leilao-e-lances
tarefas: [criar-campanha, escolher-estrategia-de-lance]
fonte: fala
faixa: 00:06:27–00:07:06
condicoes: "estratégia de lance target CPA"
perecivel: true
confianca: alta
versao: 1
```
Se usar target CPA, informe um CPA desejado diferente de zero; no exemplo, o valor 1 remove o erro.

### U:fa80cd201007f33e:006 — Iniciar Search com CPC manual
```yaml
tipo: decisao
plataforma: [ads-editor]
tema: leilao-e-lances
tarefas: [criar-campanha, escolher-estrategia-de-lance]
fonte: fala+pdf:cst_m07_a02_como_criar_campanhas_de _search_do_zero.pdf
faixa: 00:07:07–00:07:48
condicoes: "campanha de Rede de Pesquisa do exemplo"
perecivel: true
confianca: alta
versao: 1
```
Se a campanha for de Search como a demonstrada, comece com Manual CPC e mantenha CPC otimizado selecionado.

### U:fa80cd201007f33e:007 — Manter Search Network e excluir parceiros e Display
```yaml
tipo: decisao
plataforma: [ads-editor]
tema: posicionamentos-e-formatos
tarefas: [criar-campanha, escolher-canais-e-posicionamentos]
fonte: fala+pdf:cst_m07_a02_como_criar_campanhas_de _search_do_zero.pdf
faixa: 00:07:48–00:09:51
condicoes: "campanha de Rede de Pesquisa do exemplo"
perecivel: true
confianca: alta
versao: 1
nota: "O PDF orienta desabilitar também a opção Search; na demonstração, o professor revisa campanhas existentes e conclui que Search Network deve permanecer ativado."
```
Se configurar uma campanha apenas de Search, mantenha Search Network ativado e desative parceiros da Rede de Pesquisa e Rede de Display.

### U:fa80cd201007f33e:008 — Agenda por dia é configurada no Google Ads online
```yaml
tipo: limite
plataforma: [ads-editor, google]
tema: estrutura-de-campanha
tarefas: []
fonte: fala+pdf:cst_m07_a02_como_criar_campanhas_de _search_do_zero.pdf
faixa: 00:09:15–00:10:28
perecivel: true
confianca: alta
versao: 1
```
O Google Ads Editor não permite editar os dias da semana em que a campanha roda. Para veicular apenas em dias definidos, envie a campanha e faça essa edição no Google Ads online.

### U:fa80cd201007f33e:009 — Usar todos os dispositivos e rotação padrão
```yaml
tipo: decisao
plataforma: [ads-editor]
tema: posicionamentos-e-formatos
tarefas: [criar-campanha, escolher-canais-e-posicionamentos]
fonte: fala
faixa: 00:09:52–00:10:28
condicoes: "campanha de Search do exemplo"
perecivel: true
confianca: alta
versao: 1
```
Se não houver uma necessidade específica de dispositivo, anuncie em todos e mantenha a rotação padrão, que direciona mais verba aos melhores anúncios.

### U:fa80cd201007f33e:010 — Idiomas do exemplo: inglês e português
```yaml
tipo: regra
plataforma: [ads-editor]
tema: estrutura-de-campanha
tarefas: [criar-campanha]
fonte: fala+pdf:cst_m07_a02_como_criar_campanhas_de _search_do_zero.pdf
faixa: 00:10:29–00:10:46
perecivel: true
confianca: alta
versao: 1
```
Na campanha demonstrada, altere o idioma para inglês e português.

### U:fa80cd201007f33e:011 — Não selecionar metas de conversão do exemplo
```yaml
tipo: decisao
plataforma: [ads-editor]
tema: objetivos
tarefas: [criar-campanha, definir-conversoes-e-metas]
fonte: fala+pdf:cst_m07_a02_como_criar_campanhas_de _search_do_zero.pdf
faixa: 00:10:48–00:11:30
condicoes: "campanha do exemplo não possui visitas à loja, cliques para ligações, direções, vendas ou novos clientes como objetivo"
perecivel: true
confianca: alta
versao: 1
```
Se a campanha não tiver os objetivos listados nas metas de conversão, não selecione nenhuma dessas opções.

### U:fa80cd201007f33e:012 — Consultar campanha pronta diante de dúvida
```yaml
tipo: procedimento
plataforma: [ads-editor]
tema: estrutura-de-campanha
tarefas: [criar-campanha]
fonte: fala
faixa: 00:07:48–00:12:51
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: existe uma campanha pronta do mesmo tipo na conta.
1. Abra a configuração equivalente em uma campanha de Search já criada.
2. Compare a opção com a campanha nova.
3. Replique a configuração que as campanhas prontas usam quando ela fizer sentido para a nova.

### U:fa80cd201007f33e:013 — Criar grupo de anúncios dentro da campanha
```yaml
tipo: procedimento
plataforma: [ads-editor]
tema: estrutura-de-campanha
tarefas: [criar-campanha, definir-estrutura-de-campanha]
fonte: fala+pdf:cst_m07_a02_como_criar_campanhas_de _search_do_zero.pdf
faixa: 00:12:51–00:14:03
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: a campanha nova está selecionada sozinha.
1. Abra “grupos de anúncio”.
2. Use “adicionar um novo grupo de anúncio”.
3. Dê um nome ao grupo conforme o agrupamento de palavras-chave que ele receberá.

### U:fa80cd201007f33e:014 — CPC inicial de 30 centavos no grupo
```yaml
tipo: regua
plataforma: [ads-editor]
tema: leilao-e-lances
tarefas: [criar-campanha, escolher-estrategia-de-lance]
fonte: fala
faixa: 00:14:03–00:14:40
condicoes: "campanha configurada com estratégia de CPC"
perecivel: true
confianca: alta
versao: 1
nota: "O professor declara que não sabe a origem desse valor; é o ponto de partida que ele costuma usar."
```
Com estratégia de CPC, defina o CPC do grupo. O professor normalmente começa campanhas de Search com 30 centavos.

### U:fa80cd201007f33e:015 — Desativar Target Expansion no exemplo
```yaml
tipo: decisao
plataforma: [ads-editor]
tema: publicos
tarefas: [criar-campanha, definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: 00:14:40–00:16:05
condicoes: "grupo de anúncios de Search demonstrado"
perecivel: true
confianca: alta
versao: 1
```
Se o grupo for de Search como no exemplo, deixe Target Expansion desativado.

### U:fa80cd201007f33e:016 — Criar palavras-chave e definir correspondência
```yaml
tipo: procedimento
plataforma: [ads-editor]
tema: palavras-chave
tarefas: [montar-lista-de-palavras-chave]
fonte: fala+pdf:cst_m07_a02_como_criar_campanhas_de _search_do_zero.pdf
faixa: 00:17:53–00:20:25
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: o grupo de anúncios de Search está criado.
1. Abra “segmentações” do grupo e adicione as palavras-chave.
2. Selecione cada palavra-chave e altere seu tipo de correspondência no campo próprio, como frase ou exata.
3. Copie e cole palavras já inseridas para criar variações, em vez de adicionar cada uma do zero.

### U:fa80cd201007f33e:017 — Aspas digitadas não definem correspondência de frase
```yaml
tipo: alerta-ui
plataforma: [ads-editor]
tema: palavras-chave
tarefas: [montar-lista-de-palavras-chave]
fonte: fala
faixa: 00:18:19–00:19:35
perecivel: true
confianca: alta
versao: 1
```
No Editor, colocar aspas no texto da palavra-chave não a torna de frase. Selecione a palavra e altere o match type para “frase”.

### U:fa80cd201007f33e:018 — Conferir localização e segmentações existentes
```yaml
tipo: procedimento
plataforma: [ads-editor]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: 00:21:04–00:24:38
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: palavras-chave do grupo foram inseridas.
1. Abra localização e confira se a localização padrão está correta.
2. Compare palavras-chave negativas, localizações, públicos, gênero e idade com um grupo pronto semelhante.
3. Copie as configurações necessárias; se os campos equivalentes estiverem zerados na campanha pronta, mantenha-os zerados na nova.

### U:fa80cd201007f33e:019 — Excluir idades negativas no grupo ou campanha
```yaml
tipo: procedimento
plataforma: [ads-editor]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: 00:24:00–00:25:20
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: é necessário impedir a veiculação para uma faixa etária.
1. Abra “idades negativas” e adicione a idade negativa no grupo de anúncio ou na campanha.
2. Selecione a faixa desejada, como 65 anos ou desconhecido.
3. Remova as exclusões se não quiser negativar nenhuma idade.

### U:fa80cd201007f33e:020 — Criar anúncio responsivo com títulos, descrições e URL
```yaml
tipo: procedimento
plataforma: [ads-editor]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala+pdf:cst_m07_a02_como_criar_campanhas_de _search_do_zero.pdf
faixa: 00:25:20–00:28:41
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: grupo de anúncios de Search está configurado.
1. Abra anúncios e escolha adicionar um novo anúncio responsivo.
2. Preencha os títulos e as descrições.
3. Informe a URL de destino do anúncio.

### U:fa80cd201007f33e:021 — Estrutura de anúncios: um responsivo e três expandidos
```yaml
tipo: regua
plataforma: [ads-editor]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:28:04–00:30:35
perecivel: true
confianca: alta
versao: 1
```
O professor roda 1 anúncio responsivo e 3 anúncios de texto expandido na campanha de Search.

### U:fa80cd201007f33e:022 — Copiar conteúdo para anúncios de texto expandido
```yaml
tipo: procedimento
plataforma: [ads-editor]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala+pdf:cst_m07_a02_como_criar_campanhas_de _search_do_zero.pdf
faixa: 00:28:04–00:30:35
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: existe um anúncio responsivo ou texto expandido com conteúdo aproveitável.
1. Abra “texto expandido” e adicione um novo anúncio.
2. Copie títulos, descrições e URL do anúncio anterior.
3. Duplique o anúncio de texto expandido e altere os textos para formar os 3 anúncios.

### U:fa80cd201007f33e:023 — Adicionar extensões já existentes ao grupo
```yaml
tipo: procedimento
plataforma: [ads-editor]
tema: posicionamentos-e-formatos
tarefas: [configurar-anuncio]
fonte: fala
faixa: "00:30:35–00:31:35"
perecivel: true
confianca: media
versao: 2
nota: "Proposta recusada: erro de grafia no slug; tema existente posicionamentos-e-formatos atende a unidade. Corpo preservado."
```
Pré-condição: anúncios do grupo estão configurados e existem extensões disponíveis na conta.
1. Abra extensões e escolha adicionar extensões ao grupo de anúncios.
2. Selecione extensões existentes, como callout e sitelink.
3. Associe as extensões ao grupo de anúncios.

### U:fa80cd201007f33e:024 — Replicar grupo pronto para criar outros grupos
```yaml
tipo: decisao
plataforma: [ads-editor]
tema: estrutura-de-campanha
tarefas: [replicar-campanhas-e-grupos]
fonte: fala+pdf:cst_m07_a02_como_criar_campanhas_de _search_do_zero.pdf
faixa: 00:31:36–00:32:09
perecivel: true
confianca: alta
versao: 1
```
Quando já houver um grupo de anúncios pronto, duplique-o para criar os demais e altere palavras-chave, anúncios e informações específicas.

### U:fa80cd201007f33e:025 — Usar localizar e substituir nas palavras-chave
```yaml
tipo: procedimento
plataforma: [ads-editor]
tema: palavras-chave
tarefas: [replicar-campanhas-e-grupos, montar-lista-de-palavras-chave]
fonte: fala
faixa: 00:31:36–00:32:42
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: um grupo duplicado contém palavras-chave que precisam de troca recorrente.
1. Selecione as palavras-chave do grupo.
2. Abra “encontrar e substituir” e limite a substituição às palavras-chave.
3. Informe o termo a encontrar e o termo de substituição, depois aplique a alteração.

### U:fa80cd201007f33e:026 — Revisar todas as substituições, especialmente URLs
```yaml
tipo: regra
plataforma: [ads-editor]
tema: otimizacao
tarefas: [replicar-campanhas-e-grupos]
fonte: fala
faixa: 00:33:21–00:36:36
perecivel: true
confianca: alta
versao: 1
```
Revise tudo depois de usar localizar e substituir. A ferramenta acelera alterações, mas pode modificar URLs ou deixar termos sem substituir por diferenças como espaço ou abreviação.