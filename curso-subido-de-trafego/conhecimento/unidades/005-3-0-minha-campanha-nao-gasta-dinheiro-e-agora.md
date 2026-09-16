---
type: unidades-aula
status: validado
title: "3.0 - Minha campanha não gasta dinheiro - e agora"
modulo: "005"
ordem: 83
aula_id: eeeff0901543d710
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - cst_m05_a03_minha_campanha_nao_gasta_dinheiro_e_agora_.pdf
  - transcricao.md
extraido_em: 2026-09-16
gerado_por: gpt-5.6-terra
retiradas: []
divisoes: []
fusoes: []
---

# 3.0 - Minha campanha não gasta dinheiro - e agora

## Contexto da aula

A aula apresenta uma sequência de diagnóstico para uma campanha de vídeo In-Feed que não consumiu verba.
Parte de uma campanha que parece zerada no gerenciador e verifica data, aprovação, lance e tamanho dos públicos.
A demonstração ocorre no Google Ads e usa grupos de anúncios, CPV máximo e públicos do YouTube.
Também mostra como reenviar anúncios reprovados para revisão e pausar suas versões não qualificadas.
O caso de verba concentrada em um grupo é introduzido, mas a solução fica para a aula seguinte.

## Unidades

### U:eeeff0901543d710:001 — Confira o filtro de datas antes de diagnosticar gasto
```yaml
tipo: alerta-ui
plataforma: [google]
tema: metricas-e-relatorios
tarefas: [diagnosticar-campanha-sem-gasto, ler-metricas-e-relatorios]
fonte: "fala+pdf:cst_m05_a03_minha_campanha_nao_gasta_dinheiro_e_agora_.pdf"
faixa: "00:00:29–00:01:37"
perecivel: true
confianca: alta
versao: 1
```
Confira o filtro de datas no canto superior direito antes de concluir que a campanha não gastou.
Uma data vista uma semana à frente pode mostrar gasto e encerrar o diagnóstico.

### U:eeeff0901543d710:002 — Verifique a aprovação dos anúncios
```yaml
tipo: procedimento
plataforma: [youtube]
tema: criativo
tarefas: [diagnosticar-campanha-sem-gasto, configurar-anuncio]
fonte: "fala+pdf:cst_m05_a03_minha_campanha_nao_gasta_dinheiro_e_agora_.pdf"
faixa: "00:01:37–00:03:53"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: a data correta está selecionada e a campanha continua sem gasto.
1. Entre na campanha e depois no grupo de anúncios; confira a coluna de status dos anúncios.
2. Se o anúncio está correto, passe o mouse sobre “não qualificado”, escolha editar, faça uma alteração mínima e salve para submetê-lo outra vez.
3. Se houver dúvida sobre a reprovação, consulte as políticas para identificar o motivo.
Anúncio não aprovado não faz a campanha gastar dinheiro.

### U:eeeff0901543d710:003 — Reenvie anúncios reprovados para todos os grupos
```yaml
tipo: procedimento
plataforma: [youtube]
tema: criativo
tarefas: [diagnosticar-campanha-sem-gasto, replicar-campanhas-e-grupos]
fonte: "fala+pdf:cst_m05_a03_minha_campanha_nao_gasta_dinheiro_e_agora_.pdf"
faixa: "00:03:13–00:06:02"
condicoes: "os mesmos anúncios foram reprovados em vários grupos da mesma campanha"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: os anúncios reprovados precisam ser reenviados à revisão em mais de um grupo de anúncios.
1. Copie os anúncios reprovados e cole-os; pesquise e selecione a campanha de destino.
2. Selecione todos os grupos de anúncios e confirme a opção para criar anúncio duplicado quando já houver anúncio no destino.
3. Clique em colar para submeter as cópias a nova revisão.
As cópias ficam pendentes de análise enquanto os anúncios anteriores ainda podem aparecer como não qualificados.

### U:eeeff0901543d710:004 — Pause os anúncios não qualificados
```yaml
tipo: procedimento
plataforma: [youtube]
tema: criativo
tarefas: [diagnosticar-campanha-sem-gasto, otimizar-anuncios]
fonte: "fala+pdf:cst_m05_a03_minha_campanha_nao_gasta_dinheiro_e_agora_.pdf"
faixa: "00:06:03–00:08:05"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: existem cópias pendentes de análise e anúncios ainda não qualificados.
1. Na visualização da campanha, abra a aba de anúncios e ordene a coluna de status.
2. Selecione os anúncios não qualificados, escolha editar e pause-os; não é necessário removê-los.
3. Se os pausados não aparecerem, ajuste o filtro de status para incluir ativados e pausados.

### U:eeeff0901543d710:005 — Aumente o CPV quando tudo estiver correto e não houver gasto
```yaml
tipo: regua
plataforma: [youtube]
tema: leilao-e-lances
tarefas: [diagnosticar-campanha-sem-gasto, otimizar-lances]
fonte: "fala+pdf:cst_m05_a03_minha_campanha_nao_gasta_dinheiro_e_agora_.pdf"
faixa: "00:08:05–00:10:40"
condicoes: "a campanha está zerada após uma semana, com data certa e anúncios aprovados"
perecivel: true
confianca: alta
versao: 1
```
Aumente o valor na coluna “CPV máximo” do grupo de anúncios; o professor normalmente eleva de 60% a 100% para forçar gasto.
Depois do aumento, acompanhe a campanha após 1 ou 2 horas e atualize a página; em 10 minutos o Google pode consumir todo o orçamento.
Repita o aumento até cinco vezes; se não gastar depois de literalmente cinco tentativas, o lance não é o problema.

### U:eeeff0901543d710:006 — Públicos de canais podem exigir lance maior e ainda não entregar
```yaml
tipo: decisao
plataforma: [youtube]
tema: publicos
tarefas: [diagnosticar-campanha-sem-gasto, otimizar-publicos-e-segmentacoes, otimizar-lances]
fonte: "fala+pdf:cst_m05_a03_minha_campanha_nao_gasta_dinheiro_e_agora_.pdf"
faixa: "00:10:42–00:12:04"
condicoes: "a segmentação usa canais específicos"
perecivel: false
confianca: alta
versao: 1
```
Se o público de canais não gasta, considere que ele é muito nichado e pode exigir lance maior.
Se os canais selecionados não aceitam anúncios por não terem monetização, aumentar o lance não fará a campanha gastar.

### U:eeeff0901543d710:007 — Teste um público frio para verificar público pequeno
```yaml
tipo: procedimento
plataforma: [youtube]
tema: publicos
tarefas: [diagnosticar-campanha-sem-gasto, otimizar-publicos-e-segmentacoes]
fonte: "fala+pdf:cst_m05_a03_minha_campanha_nao_gasta_dinheiro_e_agora_.pdf"
faixa: "00:12:04–00:14:03"
condicoes: "inscritos do canal e visitantes do site formam públicos muito pequenos"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: anúncios aprovados, data correta e lances aumentados não resolveram o gasto.
1. Crie um novo grupo de anúncios e abra a edição dos segmentos de público-alvo.
2. Em vez de segmento personalizado, procure listas prontas do Google.
3. Selecione um público-alvo de mercado, de eventos importantes ou de afinidade.
Esses públicos frios permitem testar se a falta de gasto vinha de públicos pequenos.

### U:eeeff0901543d710:008 — Compare o gasto total com a concentração por grupo
```yaml
tipo: exemplo
plataforma: [youtube]
tema: orcamento
tarefas: [diagnosticar-concentracao-de-verba, ler-metricas-e-relatorios]
fonte: fala
faixa: "00:14:03–00:15:04"
perecivel: false
confianca: alta
versao: 1
```
Situação: a campanha gastou R$ 130,00 em 7 dias, com orçamento esperado de R$ 20,00 por dia.
O que aconteceu: o total esperado era R$ 140,00 na semana, mas R$ 124,00 — cerca de 95% — foi gasto em um único grupo de anúncios.
Lógica: o gasto total pode estar próximo do previsto mesmo quando quase toda a verba fica concentrada em um público.

### U:eeeff0901543d710:009 — A solução para verba em um grupo fica para a próxima aula
```yaml
tipo: limite
plataforma: [youtube]
tema: orcamento
tarefas: []
fonte: "fala+pdf:cst_m05_a03_minha_campanha_nao_gasta_dinheiro_e_agora_.pdf"
faixa: "00:13:24–00:15:04"
perecivel: false
confianca: alta
versao: 1
```
A aula identifica a situação em que a campanha consome toda a verba em um único grupo de anúncios, mas deixa o que fazer nesse caso para o próximo conteúdo.