---
type: unidades-aula
status: validado
title: "5.0 - Replicando grupos de anúncios"
modulo: "004"
ordem: 66
aula_id: 5c9362f19f198b61
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - cst_m04_a05_replicando_grupos_de_anuncio.pdf
  - transcricao.md
extraido_em: 2026-09-16
gerado_por: gpt-5.6-terra
retiradas: []
divisoes: []
fusoes: []
---

# 5.0 - Replicando grupos de anúncios

## Contexto da aula

A aula demonstra como replicar grupos de anúncios em uma campanha da Rede de Pesquisa.
Parte de uma campanha que já contém palavras-chave, anúncios, extensões e públicos-alvo.
O objetivo é criar novas segmentações sem refazer toda a configuração do grupo e dos anúncios.
A otimização das segmentações e o diagnóstico de campanha sem gasto ficam para aulas posteriores.

## Unidades

### U:5c9362f19f198b61:001 — Copiar um grupo preserva estruturas já configuradas
```yaml
tipo: conceito
plataforma: [google-search]
tema: estrutura-de-campanha
tarefas: [replicar-campanhas-e-grupos]
fonte: fala
faixa: 00:01:12–00:04:26
perecivel: false
confianca: alta
versao: 1
```
Ao copiar um grupo de anúncios, o novo grupo começa com as palavras-chave, anúncios, extensões, públicos-alvo e outras estruturas do grupo original.
A cópia evita configurar novamente essas partes antes de adaptá-las para a nova segmentação.

### U:5c9362f19f198b61:002 — Replicar grupo por copiar, colar e adaptar
```yaml
tipo: procedimento
plataforma: [google-search]
tema: estrutura-de-campanha
tarefas: [replicar-campanhas-e-grupos]
fonte: fala
faixa: 00:01:56–00:07:12
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: existir um grupo de anúncios já configurado e uma planilha com as novas palavras-chave.
1. Selecione o grupo que será replicado, copie com Ctrl C e cole com Ctrl V.
2. Na tela que pergunta a campanha de destino, mantenha a campanha já selecionada, clique em concluído e depois em colar sem pausar o novo grupo.
3. Renomeie o grupo de acordo com a nova lista de palavras-chave.
4. Entre no grupo, selecione as palavras-chave existentes em editar e remova-as.
5. Copie as novas palavras-chave da planilha, adicione-as pelo ícone “+” e salve.
6. Altere os anúncios para se adequarem às novas palavras-chave.

### U:5c9362f19f198b61:003 — Escolher entre substituir textos ou recriar palavras-chave
```yaml
tipo: decisao
plataforma: [google-search]
tema: palavras-chave
tarefas: [montar-lista-de-palavras-chave]
fonte: fala
faixa: 00:04:26–00:05:56
perecivel: true
confianca: alta
versao: 1
```
Se a troca de termos mantiver o sentido das palavras-chave, use em editar a opção de alterar texto, localizar e substituir.
Se a substituição gerar frases sem sentido, remova as palavras-chave antigas e adicione a nova segmentação do zero.
O professor cita trocar “Facebook Ads” por “Google Ads” como mudança simples, mas alerta que trocar “gestão de tráfego” por “tráfego pago” pode produzir termos inadequados.

### U:5c9362f19f198b61:004 — Status de baixo volume pode indicar restrição excessiva
```yaml
tipo: alerta-ui
plataforma: [google-search]
tema: palavras-chave
tarefas: [diagnosticar-campanha-sem-gasto]
fonte: fala
faixa: 00:06:39–00:07:34
perecivel: true
confianca: alta
versao: 1
```
A indicação “Não qualificada, baixo volume de pesquisas” pode aparecer em uma palavra-chave.
Quando a campanha não gasta, isso pode indicar que todas as palavras-chave estão muito restritas ou específicas; mesmo com essa indicação, uma palavra-chave pode gastar.

### U:5c9362f19f198b61:005 — Adequar anúncios às palavras-chave do novo grupo
```yaml
tipo: procedimento
plataforma: [google-search]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:07:36–00:10:21
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: a nova segmentação já foi adicionada ao grupo replicado.
1. Abra “anúncios e extensões”, entre em “anúncios” e escolha editar no anúncio desejado.
2. Ajuste títulos e descrições para usar termos relacionados às novas palavras-chave.
3. Alinhe o texto do anúncio à intenção de buscas incluídas na segmentação.
4. Salve o anúncio e repita o processo nos demais anúncios do grupo.

### U:5c9362f19f198b61:006 — Fixar título determina sua posição no anúncio
```yaml
tipo: alerta-ui
plataforma: [google-search]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:10:21–00:11:27
perecivel: true
confianca: alta
versao: 1
```
No ícone de fixar de um título, escolha a posição para instruir o Google a sempre mostrar aquele título naquele lugar.
O professor demonstra fixar um título para que ele apareça em primeiro lugar.

### U:5c9362f19f198b61:007 — Anúncio mostra dois, no máximo três títulos
```yaml
tipo: regua
plataforma: [google-search]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:13:38–00:14:24
perecivel: false
confianca: alta
versao: 1
```
O anúncio não exibe todos os títulos juntos: mostra 2, no máximo 3.
Ao ajustar títulos, não se apegue a deixá-los repetitivos.

### U:5c9362f19f198b61:008 — Testar alterações e reagir ao desempenho
```yaml
tipo: decisao
plataforma: [google-search]
tema: otimizacao
tarefas: [otimizar-anuncios]
fonte: fala
faixa: 00:15:15–00:15:49
perecivel: false
confianca: alta
versao: 1
```
Quando houver dúvida sobre quais alterações fazer nos anúncios, faça as mudanças e acompanhe qual teve mais e menos resultado.
Mantenha o que teve mais resultado; pause o que teve menos e crie um novo anúncio.

### U:5c9362f19f198b61:009 — Extensões específicas do grupo são opcionais
```yaml
tipo: decisao
plataforma: [google-search]
tema: posicionamentos-e-formatos
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:15:49–00:17:13
perecivel: true
confianca: alta
versao: 1
```
Se quiser usar uma extensão específica para o grupo, entre em “extensões”, clique para adicionar uma extensão e escolha o tipo, como sitelink.
O professor costuma usar o mesmo sitelink e as mesmas frases de destaque em todos os conjuntos, por sentir que esse preciosismo não faz muita diferença.

### U:5c9362f19f198b61:010 — Começar campanha com quatro ou cinco grupos
```yaml
tipo: regua
plataforma: [google-search]
tema: estrutura-de-campanha
tarefas: [definir-estrutura-de-campanha]
fonte: fala
faixa: 00:19:23–00:20:04
condicoes: "no início da campanha"
perecivel: false
confianca: alta
versao: 1
```
Comece a campanha com no mínimo 4 grupos de anúncios, preferencialmente 4 ou 5, e não mais do que isso.
Outros grupos podem ser adicionados depois.

### U:5c9362f19f198b61:011 — Google Ads Editor torna a replicação mais rápida
```yaml
tipo: regua
plataforma: [ads-editor]
tema: estrutura-de-campanha
tarefas: [operar-ads-editor, replicar-campanhas-e-grupos]
fonte: fala
faixa: 00:20:58–00:21:41
perecivel: false
confianca: alta
versao: 1
```
No Google Ads Editor, o professor afirma que esse trabalho pode ser feito 10 vezes mais rápido.

### U:5c9362f19f198b61:012 — Diagnóstico sem gasto e otimizações ficam para depois
```yaml
tipo: limite
plataforma: [google-search]
tema: otimizacao
tarefas: []
fonte: fala
faixa: 00:21:41–00:22:15
perecivel: false
confianca: alta
versao: 1
```
A aula não aborda como otimizar as segmentações após conversões nem o que fazer quando a campanha não gasta dinheiro; esses assuntos ficam para as próximas aulas.