---
type: unidades-aula
status: validado
title: "6.1 - Configurando sua campanha"
modulo: "005"
ordem: 92
aula_id: ce8fcab6ad6a538a
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - cst_m05_a61_configurando_sua_campanha.pdf
  - transcricao.md
extraido_em: 2026-09-16
gerado_por: gpt-5.6-terra
retiradas: []
divisoes: []
fusoes: []
---

# 6.1 - Configurando sua campanha

## Contexto da aula

A aula demonstra a configuração de uma campanha de conversão em vídeo no Google, após a hierarquia de públicos já estar definida.
O exemplo usa geração de cadastros, público quente e campanha no YouTube, mas diferencia objetivo de leads e de vendas.
Também registra mudanças de interface e de opções de segmentação ocorridas durante a gravação.
A replicação de anúncios e grupos é anunciada como próximo conteúdo, sem ser ensinada aqui.

## Unidades

### U:ce8fcab6ad6a538a:001 — Criar campanha de vídeo para conversão
```yaml
tipo: procedimento
plataforma: [youtube]
tema: estrutura-de-campanha
tarefas: [criar-campanha]
fonte: fala
faixa: 00:00:00–00:00:50
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: a hierarquia da campanha já foi definida.
1. Clique no botão de mais, escolha criar nova campanha e selecione o objetivo.
2. Para conversão, escolha leads ou vendas conforme a ação desejada.
3. Mantenha as metas exibidas sem alteração, avance e escolha campanha de vídeo.

### U:ce8fcab6ad6a538a:002 — Escolher leads ou vendas pelo objetivo da conversão
```yaml
tipo: decisao
plataforma: [youtube]
tema: objetivos
tarefas: [escolher-objetivo-de-campanha]
fonte: fala
faixa: 00:00:00–00:00:34
perecivel: true
confianca: alta
versao: 1
```
Se a conversão buscada for cadastro em uma página, escolha leads; se for venda, escolha vendas.

### U:ce8fcab6ad6a538a:003 — Nomear e separar campanhas de público quente e frio
```yaml
tipo: regra
plataforma: [youtube]
tema: nomenclatura
tarefas: [nomear-campanhas, definir-estrutura-de-campanha]
fonte: fala
faixa: 00:00:52–00:01:25
perecivel: true
confianca: alta
versao: 1
```
Dê nome à campanha antes de começar e separe público quente de público frio para controlar quanto é gasto por dia em cada um.

### U:ce8fcab6ad6a538a:004 — Começar conversão com CPA desejado de R$5
```yaml
tipo: procedimento
plataforma: [youtube]
tema: leilao-e-lances
tarefas: [escolher-estrategia-de-lance]
fonte: fala+pdf:cst_m05_a61_configurando_sua_campanha.pdf
faixa: 00:01:25–00:02:01
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: a campanha de conversão está na etapa de estratégia de lance.
1. Selecione CPA desejado.
2. Informe R$5 como valor inicial, inclusive quando não souber quanto pagar por conversão.
3. Diminua o valor depois, caso queira pagar menos.

### U:ce8fcab6ad6a538a:005 — Preferir orçamento diário e definir verba pela hierarquia
```yaml
tipo: regra
plataforma: [youtube]
tema: orcamento
tarefas: [definir-orcamento]
fonte: fala+pdf:cst_m05_a61_configurando_sua_campanha.pdf
faixa: 00:02:01–00:03:18
perecivel: true
confianca: alta
versao: 1
```
Prefira orçamento diário; a diferença entre gastar R$3.000 ou R$30 por dia está na hierarquia e na quantidade e qualificação dos públicos, não no procedimento de configuração.
Não defina data de término se pretende pausar a campanha manualmente.

### U:ce8fcab6ad6a538a:006 — Evitar todos os países ao preparar duplicação para público frio
```yaml
tipo: decisao
plataforma: [youtube]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses, replicar-campanhas-e-grupos]
fonte: fala+pdf:cst_m05_a61_configurando_sua_campanha.pdf
faixa: 00:02:41–00:03:54
perecivel: true
confianca: alta
versao: 1
```
Se a campanha será duplicada para público frio, selecione Brasil em locais em vez de todos os países e territórios, para não esquecer essa segmentação na cópia.

### U:ce8fcab6ad6a538a:007 — Manter espanhol, inglês e português nos idiomas
```yaml
tipo: regra
plataforma: [youtube]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala+pdf:cst_m05_a61_configurando_sua_campanha.pdf
faixa: 00:03:18–00:03:54
perecivel: true
confianca: alta
versao: 1
```
Mantenha selecionados os idiomas espanhol, inglês e português.

### U:ce8fcab6ad6a538a:008 — Usar inventário padrão; expandido só sem gasto
```yaml
tipo: decisao
plataforma: [youtube]
tema: posicionamentos-e-formatos
tarefas: [escolher-canais-e-posicionamentos, diagnosticar-campanha-sem-gasto]
fonte: fala+pdf:cst_m05_a61_configurando_sua_campanha.pdf
faixa: 00:03:55–00:04:29
perecivel: true
confianca: alta
versao: 1
```
Se a campanha não estiver gastando dinheiro, use inventário expandido como uma das últimas opções para fazê-la gastar; fora disso, mantenha inventário padrão e não use o limitado.

### U:ce8fcab6ad6a538a:009 — Criar sitelinks com textos e URLs distintos
```yaml
tipo: procedimento
plataforma: [youtube]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala+pdf:cst_m05_a61_configurando_sua_campanha.pdf
faixa: 00:04:30–00:06:50
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: a seção de extensões de anúncio está disponível.
1. Clique em nova extensão de sitelink e preencha texto, descrições e URL final.
2. Crie cerca de 4 opções com estímulos diferentes.
3. Use texto e URL exclusivos em cada sitelink; extensões duplicadas não aparecem.
4. Se testar duas páginas, direcione os sitelinks para as duas URLs.

### U:ce8fcab6ad6a538a:010 — Começar com todos os dispositivos habilitados
```yaml
tipo: decisao
plataforma: [youtube]
tema: posicionamentos-e-formatos
tarefas: [escolher-canais-e-posicionamentos]
fonte: fala
faixa: 00:06:50–00:07:23
perecivel: true
confianca: alta
versao: 1
```
Quando iniciar a campanha, não exclua TV, tablet, smartphone ou computador; avalie depois os resultados por dispositivo e exclua, por exemplo, TV se ela não converter.

### U:ce8fcab6ad6a538a:011 — Limitar frequência por impressões e visualizações
```yaml
tipo: regua
plataforma: [youtube]
tema: otimizacao
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:07:23–00:08:36
perecivel: true
confianca: alta
versao: 1
```
Use, na maioria das vezes, limite de 3 impressões por pessoa por dia; o professor também usa 2 visualizações por dia e pode aplicar ambos.
Impressão ocorre quando o anúncio aparece; visualização exige pelo menos 30 segundos assistidos.

### U:ce8fcab6ad6a538a:012 — Retirar limite de frequência quando a campanha não gasta
```yaml
tipo: decisao
plataforma: [youtube]
tema: otimizacao
tarefas: [diagnosticar-campanha-sem-gasto]
fonte: fala+pdf:cst_m05_a61_configurando_sua_campanha.pdf
faixa: 00:08:36–00:09:10
perecivel: true
confianca: alta
versao: 1
```
Se a campanha não estiver gastando dinheiro, retire os limites de frequência para deixá-la livre; esses limites travam o gasto após 3 impressões ou 2 visualizações por usuário.
No exemplo, o limite é removido desde o início para a campanha gastar bem a verba.

### U:ce8fcab6ad6a538a:013 — Agendar todos os dias separadamente
```yaml
tipo: procedimento
plataforma: [youtube]
tema: metricas-e-relatorios
tarefas: [criar-campanha, ler-metricas-e-relatorios]
fonte: fala+pdf:cst_m05_a61_configurando_sua_campanha.pdf
faixa: 00:09:10–00:09:30
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: a seção de programação de anúncios está aberta.
1. Adicione todos os dias da semana separadamente.
2. Leia depois os resultados de segunda a domingo para ter a visão detalhada por dia.

### U:ce8fcab6ad6a538a:014 — Configurar público quente sem exclusões demográficas
```yaml
tipo: decisao
plataforma: [youtube]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: 00:09:32–00:10:37
perecivel: true
confianca: alta
versao: 1
```
Se anunciar para público quente, não faça exclusão demográfica; no exemplo, quem já viu os anúncios deve continuar recebendo-os.

### U:ce8fcab6ad6a538a:015 — Excluir quem chegou à página de obrigado
```yaml
tipo: procedimento
plataforma: [youtube]
tema: publicos
tarefas: [organizar-hierarquia-e-exclusao-de-publicos]
fonte: fala
faixa: 00:10:10–00:13:02
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: o segmento de público-alvo do grupo de anúncios está aberto.
1. Adicione, em seus dados, o público que viu o vídeo convite.
2. Em listas de remarketing excluídas, adicione quem visualizou a página de obrigado.
3. Desative a segmentação otimizada para não anunciar a público novo encontrado pelo Google.

### U:ce8fcab6ad6a538a:016 — Não restringir público quente por canais, temas ou palavras
```yaml
tipo: regra
plataforma: [youtube]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: 00:13:03–00:13:37
perecivel: true
confianca: alta
versao: 1
```
Para o público que viu o vídeo convite, não acrescente a exigência de pesquisar palavra-chave, assistir determinado tópico ou canal; anuncie para ele em qualquer contexto no YouTube.

### U:ce8fcab6ad6a538a:017 — Criar ou selecionar público-alvo nos menus atualizados
```yaml
tipo: procedimento
plataforma: [youtube]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: 00:16:25–00:18:07
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: a campanha está na etapa de seleção de público-alvo.
1. Clique em adicionar um público-alvo e escolha um público usado antes ou novo público-alvo.
2. Dê nome ao novo público se quiser reutilizá-lo.
3. Inclua segmentos personalizados, públicos próprios, interesses e dados demográficos pelos menus disponíveis.
4. Em procurar, encontre públicos no mercado, afinidade, dados demográficos detalhados e eventos importantes.
5. Abra informações demográficas adicionais para status parental e renda familiar.

### U:ce8fcab6ad6a538a:018 — Segmentação otimizada permanece ativa sem público
```yaml
tipo: decisao
plataforma: [youtube]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: 00:16:25–00:19:21
perecivel: true
confianca: alta
versao: 1
```
Se não adicionar público à campanha, a segmentação otimizada fica ativada e, segundo o professor, normalmente consome a verba; adicione ou crie um público para desativá-la.

### U:ce8fcab6ad6a538a:019 — Canais, palavras-chave e tópicos não servem a conversão
```yaml
tipo: regra
plataforma: [youtube]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala+pdf:cst_m05_a61_configurando_sua_campanha.pdf
faixa: 00:18:07–00:19:21
perecivel: true
confianca: alta
versao: 1
```
Não use públicos de canais, palavras-chave ou tópicos em campanhas de conversão: o Google os retirou dessas opções por dizer que atrapalhavam as conversões.

### U:ce8fcab6ad6a538a:020 — Formulário de lead exige enviar contatos ao e-mail
```yaml
tipo: procedimento
plataforma: [youtube]
tema: destino-e-landing-page
tarefas: [criar-campanha-de-formulario]
fonte: fala+pdf:cst_m05_a61_configurando_sua_campanha.pdf
faixa: 00:14:06–00:15:13
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: a opção de formulário de lead está disponível na conta.
1. Ative o formulário para solicitar dados como nome, e-mail e telefone dentro do anúncio.
2. Envie os contatos armazenados no Google para a ferramenta de e-mail por webhook.
3. Use uma ferramenta de integração; o professor cita Peble, Integromat e Zapier, e prefere Integromat.

### U:ce8fcab6ad6a538a:021 — Usar vídeo público ou não listado no anúncio
```yaml
tipo: decisao
plataforma: [youtube]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala+pdf:cst_m05_a61_configurando_sua_campanha.pdf
faixa: 00:19:21–00:22:53
perecivel: true
confianca: alta
versao: 1
```
Se o vídeo do YouTube estiver privado, não será possível anunciá-lo; deixe-o público ou não listado.
Para criar o anúncio, informe a URL completa do vídeo e não pule a etapa de criação.

### U:ce8fcab6ad6a538a:022 — Preencher destino, chamada e textos do anúncio
```yaml
tipo: procedimento
plataforma: [youtube]
tema: copy-e-roteiro
tarefas: [configurar-anuncio, escrever-copy-e-roteiro]
fonte: fala+pdf:cst_m05_a61_configurando_sua_campanha.pdf
faixa: 00:22:09–00:24:51
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: o vídeo foi aceito para a criação do anúncio.
1. Preencha a URL final e escolha a chamada à ação mais alinhada ao objetivo; o professor costuma usar “saiba mais”.
2. Preencha título, título longo e descrição.
3. Use no título longo uma linha próxima à headline da página e aproveite o que funciona na rede de pesquisa.
4. Mantenha a descrição enxuta, resumindo o que a pessoa encontrará.

### U:ce8fcab6ad6a538a:023 — Nomear anúncio para identificá-lo visualmente
```yaml
tipo: regra
plataforma: [youtube]
tema: nomenclatura
tarefas: [nomear-campanhas, configurar-anuncio]
fonte: fala+pdf:cst_m05_a61_configurando_sua_campanha.pdf
faixa: 00:24:13–00:25:31
perecivel: true
confianca: alta
versao: 1
```
Nomeie o anúncio com um termo que permita reconhecer sua proposta ao bater o olho; no exemplo, use AD01 em vez de AD1 e acrescente “dez reais por dia”.

### U:ce8fcab6ad6a538a:024 — Replicação fica para o próximo conteúdo
```yaml
tipo: limite
plataforma: [youtube]
tema: estrutura-de-campanha
tarefas: []
fonte: fala+pdf:cst_m05_a61_configurando_sua_campanha.pdf
faixa: 00:25:31–00:25:42
perecivel: false
confianca: alta
versao: 1
```
A aula termina após salvar a campanha; a replicação de um anúncio em seis e a criação dos demais grupos de anúncios ficam para o próximo conteúdo.

### U:ce8fcab6ad6a538a:025 — Divergência do PDF sobre impressão após pulo do anúncio
```yaml
tipo: fato-material
plataforma: [youtube]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios]
fonte: pdf:cst_m05_a61_configurando_sua_campanha.pdf
perecivel: false
confianca: media
versao: 1
nota: "Há divergência: a fala afirma que o anúncio pulado após 5 segundos conta como impressão; o PDF afirma que não é contabilizado como impressão nem visualização."
```
O PDF diz que, se a pessoa pular o anúncio depois de 5 segundos, a ação não conta como impressão nem como visualização; assistir 30 segundos conta como visualização. Fonte: p. 12.