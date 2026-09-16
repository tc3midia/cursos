---
type: unidades-aula
status: validado
title: "8.0 - Minha campanha está gastando toda verba em um único grupo de anúncio, e agora"
modulo: "005"
ordem: 97
aula_id: e8a4deaa9c490d33
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - cst_m05_a08_minha_campanha_esta_ gastando_toda_ve.pdf
  - transcricao.md
extraido_em: 2026-09-16
gerado_por: gpt-5.6-terra
retiradas: []
divisoes: []
fusoes: []
---

# 8.0 - Minha campanha está gastando toda verba em um único grupo de anúncio, e agora

## Contexto da aula

A aula trata da concentração de verba em um ou poucos grupos de anúncios.
O professor separa o assunto entre diagnósticos e possíveis soluções.
A demonstração usa uma campanha do YouTube, embora a explicação também atribua os comportamentos ao Google.
As alternativas propostas envolvem lances, exclusões de públicos e separação de grupos em campanhas.
A próxima parte do curso aborda otimização, mas não usa a campanha demonstrada por ela ainda ter poucos dados.

## Unidades

### U:e8a4deaa9c490d33:001 — Público muito amplo pode concentrar a verba
```yaml
tipo: decisao
plataforma: [google, youtube]
tema: orcamento
tarefas: [diagnosticar-concentracao-de-verba]
fonte: "fala+pdf:cst_m05_a08_minha_campanha_esta_ gastando_toda_ve.pdf"
faixa: "00:00:00–00:01:47"
condicoes: "quando um público é muito maior que os demais grupos da campanha"
perecivel: false
confianca: alta
versao: 1
nota: "A fala demonstra uma campanha do YouTube e atribui o comportamento ao Google."
```
Se um público for muito mais amplo que os outros, considere que o Google pode concentrar nele todo o dinheiro.
O professor contrasta público frio, normalmente maior, com público quente e diz que o sistema busca onde encontra pessoas e resultados com mais facilidade.

### U:e8a4deaa9c490d33:002 — Público que traz mais resultados pode receber prioridade
```yaml
tipo: decisao
plataforma: [google, youtube]
tema: otimizacao
tarefas: [diagnosticar-concentracao-de-verba]
fonte: "fala+pdf:cst_m05_a08_minha_campanha_esta_ gastando_toda_ve.pdf"
faixa: "00:01:47–00:03:26"
condicoes: "quando um público recebe mais verba que os demais, inclusive antes de os outros consumirem verba relevante"
perecivel: false
confianca: alta
versao: 1
nota: "A fala demonstra uma campanha do YouTube e atribui o comportamento ao Google."
```
Se um público estiver trazendo muito mais resultado que os outros, o Google pode priorizá-lo mesmo que os demais grupos quase não tenham gasto.
O professor diz que o sistema usa parâmetros e perfis dos públicos para buscar resultado.

### U:e8a4deaa9c490d33:003 — Lance muito maior favorece um grupo de anúncios
```yaml
tipo: decisao
plataforma: [google, youtube]
tema: leilao-e-lances
tarefas: [diagnosticar-concentracao-de-verba, otimizar-lances]
fonte: "fala+pdf:cst_m05_a08_minha_campanha_esta_ gastando_toda_ve.pdf"
faixa: "00:03:27–00:05:17"
condicoes: "quando um grupo tem lance muito maior que os outros"
perecivel: false
confianca: alta
versao: 1
nota: "A fala demonstra uma campanha do YouTube e atribui o comportamento ao Google."
```
Se um grupo tiver lance muito maior, o Google entende que se aceita pagar mais caro para alcançar aquele público e pode priorizá-lo em detrimento dos outros.
No exemplo, um lance de R$ 15 no grupo que recebe toda a verba é apresentado como coerente com essa concentração.

### U:e8a4deaa9c490d33:004 — Ajuste lances conforme onde se quer gastar
```yaml
tipo: decisao
plataforma: [google, youtube]
tema: leilao-e-lances
tarefas: [otimizar-lances, diagnosticar-concentracao-de-verba]
fonte: "fala+pdf:cst_m05_a08_minha_campanha_esta_ gastando_toda_ve.pdf"
faixa: "00:05:17–00:06:26"
condicoes: "quando houver confiança de que o grupo que não gasta pode funcionar bem, ou quando um grupo recebe verba demais"
perecivel: false
confianca: alta
versao: 1
nota: "A fala demonstra uma campanha do YouTube e atribui o comportamento ao Google."
```
Se quiser mais gasto em um grupo, aumente seu lance; se quiser menos gasto em outro, diminua o lance dele.
Reduzir o lance pode fazer o grupo parar totalmente de gastar e deixar o custo por conversão mais caro.

### U:e8a4deaa9c490d33:005 — Remova exclusões de públicos que não gastam
```yaml
tipo: decisao
plataforma: [google, youtube]
tema: publicos
tarefas: [otimizar-publicos-e-segmentacoes, diagnosticar-concentracao-de-verba]
fonte: "fala+pdf:cst_m05_a08_minha_campanha_esta_ gastando_toda_ve.pdf"
faixa: "00:06:26–00:07:46"
condicoes: "quando as exclusões deixam um público pequeno ou a hierarquia de públicos não funciona bem"
perecivel: false
confianca: alta
versao: 1
nota: "O PDF diz que a correção busca distribuição uniforme da verba; a fala propõe remover a exclusão para testar se o público passa a funcionar."
```
Se um público não estiver gastando, retire sua exclusão para ampliá-lo e verificar se funciona.
O professor apresenta isso como correção possível para uma hierarquia de públicos calculada de forma inadequada.

### U:e8a4deaa9c490d33:006 — Isole grupos para controlar a distribuição de orçamento
```yaml
tipo: procedimento
plataforma: [google, youtube]
tema: estrutura-de-campanha
tarefas: [replicar-campanhas-e-grupos, otimizar-estruturas, diagnosticar-concentracao-de-verba]
fonte: "fala+pdf:cst_m05_a08_minha_campanha_esta_ gastando_toda_ve.pdf"
faixa: "00:07:06–00:08:57"
condicoes: "quando um grupo concentra toda a verba ou quando se quer forçar gasto em um grupo que não recebe verba"
perecivel: true
confianca: alta
versao: 1
nota: "A fala demonstra uma campanha do YouTube e atribui o comportamento ao Google."
```
Pré-condição: campanha com grupos de anúncios cuja distribuição de verba se quer controlar.
1. Pause, na campanha original, o grupo que será isolado.
2. Replique a campanha e deixe o grupo isolado na nova campanha.
3. Defina orçamentos separados para controlar o gasto diário de cada campanha.
4. Para um grupo que não gasta, isole-o em outra campanha como possível forma de fazê-lo receber verba.
No exemplo, R$ 300 por dia viram R$ 100 para o grupo isolado e R$ 200 para os demais grupos.

### U:e8a4deaa9c490d33:007 — Separar públicos quentes e frios é uma alternativa
```yaml
tipo: decisao
plataforma: [google, youtube]
tema: estrutura-de-campanha
tarefas: [definir-estrutura-de-campanha, otimizar-estruturas, diagnosticar-concentracao-de-verba]
fonte: "fala+pdf:cst_m05_a08_minha_campanha_esta_ gastando_toda_ve.pdf"
faixa: "00:09:11–00:10:44"
condicoes: "quando uma campanha reúne públicos quentes e frios e o Google concentra o gasto nos frios"
perecivel: true
confianca: alta
versao: 1
nota: "O professor diz que isso ocorre frequentemente em sua conta, mas reconhece que pode não ocorrer em outras contas."
```
Se uma campanha com público quente e frio gastar toda a verba no frio, replique-a e mantenha público quente em uma campanha e frio em outra.
O professor prefere começar separado em sua própria conta, mas diz que também é possível manter os dois juntos.

### U:e8a4deaa9c490d33:008 — Isolar um grupo não garante gasto
```yaml
tipo: regra
plataforma: [google, youtube]
tema: orcamento
tarefas: [diagnosticar-concentracao-de-verba, otimizar-estruturas]
fonte: fala
faixa: "00:08:18–00:08:57"
condicoes: "após isolar em campanha própria um grupo que não estava gastando"
perecivel: false
confianca: alta
versao: 1
```
Não trate o isolamento de um grupo como garantia de que ele começará a gastar; o professor o apresenta como uma das possíveis soluções.

### U:e8a4deaa9c490d33:009 — A aula não otimiza a campanha demonstrada
```yaml
tipo: limite
plataforma: [youtube]
tema: otimizacao
tarefas: []
fonte: fala
faixa: "00:10:44–00:11:25"
perecivel: false
confianca: alta
versao: 1
```
A aula não otimiza a campanha mostrada porque ela ainda tem poucos dados; o professor cita gasto de R$ 900 e pretende usar uma campanha com mais verba para mostrar otimizações.