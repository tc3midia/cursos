---
type: unidades-aula
status: validado
title: "6.4 - Replicando campanhas"
modulo: "005"
ordem: 95
aula_id: ebdc570839d5d761
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - cst_m05_a64_replicando_campanhas.pdf
  - transcricao.md
extraido_em: 2026-09-16
gerado_por: gpt-5.6-terra
retiradas: []
divisoes: []
fusoes: []
---

# 6.4 - Replicando campanhas

## Contexto da aula

A aula mostra como reaproveitar uma campanha de público quente para criar uma de público frio.
A estrutura replicada preserva anúncios e exclusões já configuradas, evitando refazer a campanha do zero.
A demonstração usa grupos de anúncios, palavras-chave e exclusões no Google Ads.
O professor deixa a repetição dos demais grupos para a aula anterior e anuncia que a próxima tratará de diagnóstico.

## Unidades

### U:ebdc570839d5d761:001 — Campanhas fria e quente têm estrutura semelhante
```yaml
tipo: conceito
plataforma: [youtube]
tema: estrutura-de-campanha
tarefas: []
fonte: fala
faixa: "00:00:00–00:01:17"
perecivel: false
confianca: alta
versao: 1
```
Uma campanha de público frio pode reaproveitar a base de uma campanha de público quente, incluindo anúncios e exclusões, embora a hierarquia possa mudar.

### U:ebdc570839d5d761:002 — Replicar evita reconstruir exclusões e estrutura
```yaml
tipo: decisao
plataforma: [youtube]
tema: estrutura-de-campanha
tarefas: [replicar-campanhas-e-grupos]
fonte: fala
faixa: "00:01:17–00:03:37"
perecivel: false
confianca: alta
versao: 1
```
Se for criar uma campanha nova a partir de uma estrutura já existente, copie a campanha em vez de recriar campanha, anúncios, grupos e exclusões do zero.

### U:ebdc570839d5d761:003 — Sequência para replicar uma campanha
```yaml
tipo: procedimento
plataforma: [youtube]
tema: estrutura-de-campanha
tarefas: [replicar-campanhas-e-grupos]
fonte: "fala+pdf:cst_m05_a64_replicando_campanhas.pdf"
faixa: "00:02:23–00:03:44"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: exista uma campanha-base cuja estrutura e exclusões possam ser reaproveitadas.
1. Copie e cole a campanha-base.
2. Altere o nome da campanha nova.
3. Remova a segmentação anterior.
4. Adicione a nova segmentação.
5. Se houver troca de hierarquia, exclua a segmentação anterior.

### U:ebdc570839d5d761:004 — Google Ads Editor acelera cópia e colagem
```yaml
tipo: decisao
plataforma: [ads-editor]
tema: estrutura-de-campanha
tarefas: [operar-ads-editor, replicar-campanhas-e-grupos]
fonte: fala
faixa: "00:03:46–00:04:56"
perecivel: false
confianca: alta
versao: 1
```
Quando passar por esta etapa, aprenda o Google Ads Editor: o professor afirma que Ctrl-C e Ctrl-V nele é muito mais rápido, enquanto no gerenciador a cópia pode levar minutos conforme internet e campanha.

### U:ebdc570839d5d761:005 — Preserve o grupo-base ao limpar a campanha copiada
```yaml
tipo: procedimento
plataforma: [youtube]
tema: estrutura-de-campanha
tarefas: [replicar-campanhas-e-grupos]
fonte: "fala+pdf:cst_m05_a64_replicando_campanhas.pdf"
faixa: "00:04:56–00:05:33"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: a campanha quente foi copiada e o grupo 05 será a base do novo grupo 06.
1. Na campanha nova, selecione os grupos de anúncios que não serão reaproveitados.
2. Clique em “editar” e depois em “remover”.
3. Mantenha o grupo 05 copiado para alterá-lo; a campanha quente original permanece intacta.

### U:ebdc570839d5d761:006 — Renomeie e remova a segmentação do grupo copiado
```yaml
tipo: procedimento
plataforma: [youtube]
tema: estrutura-de-campanha
tarefas: [replicar-campanhas-e-grupos]
fonte: "fala+pdf:cst_m05_a64_replicando_campanhas.pdf"
faixa: "00:05:34–00:06:22"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: o grupo de anúncios copiado será convertido para uma nova segmentação.
1. Altere o nome do grupo conforme a hierarquia e salve.
2. Entre no grupo, abra “público-alvo” e clique em “mostrar tabela”.
3. Selecione a segmentação anterior, clique em “editar” e em “remover”.

### U:ebdc570839d5d761:007 — Adicione palavras-chave pelo menu de conteúdo
```yaml
tipo: procedimento
plataforma: [youtube]
tema: palavras-chave
tarefas: [montar-lista-de-palavras-chave, replicar-campanhas-e-grupos]
fonte: "fala+pdf:cst_m05_a64_replicando_campanhas.pdf"
faixa: "00:06:22–00:07:13"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: a nova segmentação usa palavras-chave, não segmento de público-alvo.
1. No menu lateral esquerdo, abra “conteúdo” e depois “palavras-chave de vídeo/rede de display”.
2. Clique no ícone “+”.
3. Insira as palavras-chave no campo à esquerda e clique em “salvar”.

### U:ebdc570839d5d761:008 — Exclua públicos anteriores quando a hierarquia mudar
```yaml
tipo: procedimento
plataforma: [youtube]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos, replicar-campanhas-e-grupos]
fonte: "fala+pdf:cst_m05_a64_replicando_campanhas.pdf"
faixa: "00:06:28–00:07:13"
condicoes: "quando a hierarquia mudar, como do grupo 05 para o 06"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: houve troca de hierarquia entre o grupo original e o novo.
1. Abra “público-alvo” no menu lateral e acesse “exclusões”.
2. Clique em “editar as exclusões”.
3. Escolha “grupo de anúncios”, nunca campanha.
4. Remova as segmentações anteriores e salve.

### U:ebdc570839d5d761:009 — Revise demografia e localização ao mudar de quente para frio
```yaml
tipo: regra
plataforma: [youtube]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: "fala+pdf:cst_m05_a64_replicando_campanhas.pdf"
faixa: "00:07:14–00:08:57"
perecivel: true
confianca: alta
versao: 1
```
Ao mudar uma campanha de público quente para frio, revise informações demográficas e localização; remova a segmentação mundial usada para público quente e anuncie no local mais qualificado, que no exemplo é o Brasil.

### U:ebdc570839d5d761:010 — Ajuste sexo, idade, renda e status parental ao nicho
```yaml
tipo: decisao
plataforma: [youtube]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: "fala+pdf:cst_m05_a64_replicando_campanhas.pdf"
faixa: "00:08:21–00:10:05"
perecivel: true
confianca: alta
versao: 1
```
Se sexo, idade, renda familiar ou status parental fizerem diferença para o nicho, ajuste-os no primeiro grupo de anúncios; nos grupos replicados depois, essas exclusões já estarão aplicadas.

### U:ebdc570839d5d761:011 — Exemplo de exclusão por predominância de vendas masculinas
```yaml
tipo: exemplo
plataforma: [youtube]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: "00:09:31–00:10:05"
perecivel: true
confianca: alta
versao: 1
```
Situação: 99% das vendas de um produto são para homens.
O que aconteceu: o professor orienta excluir feminino e possivelmente “desconhecido” ao anunciar para público frio.
Lógica: se não quer aparecer para mulheres, a categoria “desconhecido” também deve ser considerada na exclusão.

### U:ebdc570839d5d761:012 — Configure o local na campanha, não no grupo
```yaml
tipo: procedimento
plataforma: [youtube]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: "fala+pdf:cst_m05_a64_replicando_campanhas.pdf"
faixa: "00:10:05–00:11:17"
condicoes: "se a campanha quente estiver segmentada para o mundo inteiro"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: é preciso substituir a localização mundial pelo local mais qualificado.
1. Saia do grupo de anúncios e entre na campanha.
2. Abra “configurações”.
3. Em “países” ou “locais”, clique em “inserir outro local”.
4. Selecione o local de veiculação, como Brasil no exemplo.

### U:ebdc570839d5d761:013 — Conjunto aberto mantém apenas filtros demográficos e locais
```yaml
tipo: conceito
plataforma: [youtube]
tema: publicos
tarefas: []
fonte: fala
faixa: "00:11:17–00:13:12"
perecivel: true
confianca: alta
versao: 1
```
Conjunto de anúncios aberto não usa palavras-chave, interesses, público-alvo ou canais; nele permanecem informações demográficas, localização e idioma do navegador. No exemplo, abrange 18 a 44 anos e “desconhecido”, com local Brasil e idiomas espanhol, inglês ou português.

### U:ebdc570839d5d761:014 — Use conjunto aberto para escala bruta ou teste diferente
```yaml
tipo: decisao
plataforma: [youtube]
tema: testes-e-experimentos
tarefas: [rodar-testes-e-experimentos, escalar-campanha]
fonte: fala
faixa: "00:13:12–00:13:46"
perecivel: false
confianca: alta
versao: 1
```
Quando buscar escala bruta ou testar uma alternativa depois de segmentações frias sem resultado, use um conjunto aberto; o professor ressalva que ele muitas vezes começa convertendo caro e pode exigir gasto antes de ser regulado.

### U:ebdc570839d5d761:015 — Entre públicos frios o professor prefere mesma hierarquia
```yaml
tipo: decisao
plataforma: [youtube]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos, replicar-campanhas-e-grupos]
fonte: fala
faixa: "00:13:46–00:14:24"
perecivel: false
confianca: alta
versao: 1
```
Quando replicar grupos dentro da mesma campanha de públicos frios, mantenha todos na hierarquia 06, segundo a preferência do professor; assim não há exclusão entre eles.