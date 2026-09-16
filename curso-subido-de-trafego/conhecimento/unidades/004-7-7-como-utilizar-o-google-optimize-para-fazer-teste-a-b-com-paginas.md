---
type: unidades-aula
status: validado
title: "7.7 - Como utilizar o Google Optimize para fazer teste A-B com páginas"
modulo: "004"
ordem: 75
aula_id: 1c750220ccdd4d82
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - cst_m04_a77_como_utilizar_o_google_optimize.pdf
  - transcricao.md
extraido_em: 2026-09-16
gerado_por: gpt-5.6-terra
retiradas: []
divisoes: []
fusoes: []
---

# 7.7 - Como utilizar o Google Optimize para fazer teste A-B com páginas

## Contexto da aula

A aula demonstra o Google Optimize para testar páginas de captura e páginas de vendas.
Mostra a criação de conta, o teste A/B e o teste de redirecionamento.
O teste A/B altera elementos dentro de uma página; o redirecionamento distribui tráfego entre URLs.
A medição apresentada depende da vinculação com Google Analytics e de uma meta de destino.
A demonstração usa Google Analytics Universal, não GA4.
O material orienta acompanhar o teste logo após seu início para identificar erros de configuração.

## Unidades

### U:1c750220ccdd4d82:001 — Separe contas e contêineres para organizar experiências
```yaml
tipo: conceito
plataforma: [google]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala+pdf:cst_m04_a77_como_utilizar_o_google_optimize.pdf
faixa: 00:00:29–00:02:04
perecivel: true
confianca: alta
versao: 1
```
No Optimize, use uma conta diferente para cada cliente.
Uma conta pode ter vários contêineres, usados para organizar produtos diferentes.

### U:1c750220ccdd4d82:002 — Criar conta e contêiner no Optimize
```yaml
tipo: procedimento
plataforma: [google]
tema: conta-e-configuracao
tarefas: [configurar-conta]
fonte: fala+pdf:cst_m04_a77_como_utilizar_o_google_optimize.pdf
faixa: 00:00:00–00:02:04
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: estar logado em uma conta Gmail e acessar o endereço do Optimize.
1. Clique em “criar conta”, preencha o nome da conta e confirme os termos.
2. Informe o nome do contêiner e clique em “criar”.
3. No menu principal, clique em “criar experiência”.

### U:1c750220ccdd4d82:003 — Diferença entre teste A/B e teste de redirecionamento
```yaml
tipo: conceito
plataforma: [google]
tema: testes-e-experimentos
tarefas: [rodar-testes-e-experimentos]
fonte: fala+pdf:cst_m04_a77_como_utilizar_o_google_optimize.pdf
faixa: 00:01:11–00:02:51
perecivel: false
confianca: alta
versao: 1
```
Teste A/B parte de uma página e cria variantes com alterações em seus elementos.
Teste de redirecionamento envia parcelas do tráfego para páginas com URLs diferentes.
O professor usa principalmente teste A/B e teste de redirecionamento; usa pouco o teste multivariável.

### U:1c750220ccdd4d82:004 — Distribuir tráfego entre URLs no teste de redirecionamento
```yaml
tipo: exemplo
plataforma: [google]
tema: testes-e-experimentos
tarefas: [rodar-testes-e-experimentos]
fonte: fala
faixa: 00:01:11–00:02:04
perecivel: false
confianca: alta
versao: 1
```
Situação: há várias páginas web com URLs diferentes.
O que aconteceu: o teste enviou 25% do tráfego para a URL X, 25% para a URL Y e 50% para a URL Z.
Lógica: as URLs e suas parcelas definidas no teste determinam o redirecionamento.

### U:1c750220ccdd4d82:005 — Criar teste A/B e suas variantes
```yaml
tipo: procedimento
plataforma: [google]
tema: testes-e-experimentos
tarefas: [rodar-testes-e-experimentos]
fonte: fala+pdf:cst_m04_a77_como_utilizar_o_google_optimize.pdf
faixa: 00:02:51–00:04:16
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: ter a URL da página que será usada como página do editor.
1. Em “criar experiência”, selecione “teste A/B”, dê um nome e informe a URL da página.
2. Clique em “criar” e use “adicionar variante” para nomear cada variante.
3. Mantenha a página original e as variantes para compor o teste.

### U:1c750220ccdd4d82:006 — Personalizar o peso das variantes
```yaml
tipo: procedimento
plataforma: [google]
tema: testes-e-experimentos
tarefas: [rodar-testes-e-experimentos]
fonte: fala+pdf:cst_m04_a77_como_utilizar_o_google_optimize.pdf
faixa: 00:03:39–00:04:16
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: haver página original e variantes no teste.
1. Clique no peso distribuído igualmente e abra a opção de divisão uniforme.
2. Selecione “porcentagens personalizadas”.
3. Informe a porcentagem de cada página e clique em “concluído”.

### U:1c750220ccdd4d82:007 — Exemplo de divisão entre original e variantes
```yaml
tipo: exemplo
plataforma: [google]
tema: testes-e-experimentos
tarefas: [rodar-testes-e-experimentos]
fonte: fala
faixa: 00:03:39–00:04:16
perecivel: false
confianca: alta
versao: 1
```
Situação: há uma página original e duas variantes.
O que aconteceu: a original recebeu 50% do tráfego e cada outra variante recebeu 25%.
Lógica: a divisão pode ser personalizada em vez de permanecer uniforme.

### U:1c750220ccdd4d82:008 — Editar elementos em uma variante A/B
```yaml
tipo: procedimento
plataforma: [google]
tema: testes-e-experimentos
tarefas: [rodar-testes-e-experimentos]
fonte: fala+pdf:cst_m04_a77_como_utilizar_o_google_optimize.pdf
faixa: 00:04:17–00:07:45
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: a variante já foi criada.
1. Clique em “editar” na variante para abrir a página no editor.
2. Altere elementos como botão, chamada, cor, texto, imagem ou headline.
3. Clique em “salvar” e depois em “concluído”.
4. Abra original e variantes para conferir se as alterações ficaram corretas.

### U:1c750220ccdd4d82:009 — Prefira URL diferente se a página impedir a edição
```yaml
tipo: decisao
plataforma: [google]
tema: testes-e-experimentos
tarefas: [rodar-testes-e-experimentos]
fonte: fala
faixa: 00:06:42–00:07:31
perecivel: false
confianca: alta
versao: 1
```
Se não conseguir alterar um elemento porque a página foi formatada de outra maneira, prefira usar uma URL diferente para que quem edita a página possa deixá-la correta.

### U:1c750220ccdd4d82:010 — Delimitar corretamente a URL que aciona a experiência
```yaml
tipo: procedimento
plataforma: [google]
tema: testes-e-experimentos
tarefas: [rodar-testes-e-experimentos]
fonte: fala+pdf:cst_m04_a77_como_utilizar_o_google_optimize.pdf
faixa: 00:08:45–00:10:12
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: as páginas do teste e páginas semelhantes tenham URLs conhecidas.
1. Em “segmentação por página”, clique no ícone de pincel.
2. Informe a URL e verifique a regra antes de salvar.
3. Confira outras páginas com URL semelhante para garantir que a experiência não será acionada nelas.

### U:1c750220ccdd4d82:011 — Evitar loop causado por URL ampla demais
```yaml
tipo: exemplo
plataforma: [google]
tema: testes-e-experimentos
tarefas: [rodar-testes-e-experimentos]
fonte: fala
faixa: 00:08:45–00:10:12
perecivel: false
confianca: alta
versao: 1
```
Situação: a regra usava uma parte ampla da URL da página de captura.
O que aconteceu: a experiência também era acionada na página de obrigado após o cadastro, gerando loop no teste A/B.
Lógica: usar uma parte mais específica da URL impediu que a página de obrigado acionasse o experimento.

### U:1c750220ccdd4d82:012 — Criar meta de destino no Google Analytics Universal
```yaml
tipo: procedimento
plataforma: [google]
tema: atribuicao
tarefas: [definir-conversoes-e-metas]
fonte: fala+pdf:cst_m04_a77_como_utilizar_o_google_optimize.pdf
faixa: 00:10:54–00:12:33
perecivel: true
confianca: alta
versao: 1
nota: "A demonstração declara usar Google Analytics Universal, não GA4."
```
Pré-condição: acesso ao Google Analytics Universal e conhecimento do final da URL de conversão.
1. Em “administrador”, abra “metas” e clique em “nova meta”.
2. Selecione “personalizado”, nomeie a meta e escolha o tipo “destino”.
3. Em detalhes, selecione “começa com”, informe o final da URL e salve.

### U:1c750220ccdd4d82:013 — Vincular o Optimize ao Analytics e selecionar a meta
```yaml
tipo: procedimento
plataforma: [google]
tema: atribuicao
tarefas: [definir-conversoes-e-metas, rodar-testes-e-experimentos]
fonte: fala+pdf:cst_m04_a77_como_utilizar_o_google_optimize.pdf
faixa: 00:10:13–00:13:26
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: existir uma meta de destino no Google Analytics.
1. Em “medição e objetivos” no Optimize, clique no ícone de pincel do campo “Google Analytics”.
2. Verifique a vinculação e deixe selecionado “todos os dados do website”.
3. Em “objetivo principal”, escolha a meta criada na lista.
4. Se a meta recém-criada não aparecer, atualize a página e procure-a novamente.

### U:1c750220ccdd4d82:014 — Medir conversões de cada variante pela meta
```yaml
tipo: conceito
plataforma: [google]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios, rodar-testes-e-experimentos]
fonte: fala
faixa: 00:12:51–00:13:26
perecivel: false
confianca: alta
versao: 1
```
A meta selecionada no Google Analytics mede a conversão do teste.
Quando a pessoa entra na página de obrigado, o acionamento permite identificar quantas conversões cada variante teve.

### U:1c750220ccdd4d82:015 — Instalar e verificar o pixel do Optimize
```yaml
tipo: procedimento
plataforma: [google]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala+pdf:cst_m04_a77_como_utilizar_o_google_optimize.pdf
faixa: 00:13:26–00:15:45
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: ter o ID do contêiner do Optimize.
1. Em “configurações”, abra “ver instruções” para acessar o script de instalação.
2. Instale o script no Head da página ou, no Google Tag Manager, crie a configuração do Optimize com o ID do contêiner e acionamento em todas as páginas.
3. Publique o contêiner do Tag Manager.
4. Use “verificar instalação” para confirmar que o pixel foi instalado corretamente.

### U:1c750220ccdd4d82:016 — Configurar notificações, ativação e período do teste
```yaml
tipo: procedimento
plataforma: [google]
tema: testes-e-experimentos
tarefas: [rodar-testes-e-experimentos]
fonte: fala+pdf:cst_m04_a77_como_utilizar_o_google_optimize.pdf
faixa: 00:15:05–00:16:23
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: medição e instalação do pixel já conferidas.
1. Ative notificações por e-mail se quiser receber avisos sobre começo e encerramento da experiência.
2. Mantenha a ativação no carregamento da página e defina o período se quiser programar início e término.
3. Quando tudo estiver configurado, clique em “iniciar”.

### U:1c750220ccdd4d82:017 — Não editar teste que já está rodando
```yaml
tipo: decisao
plataforma: [google]
tema: testes-e-experimentos
tarefas: [rodar-testes-e-experimentos]
fonte: fala+pdf:cst_m04_a77_como_utilizar_o_google_optimize.pdf
faixa: 00:16:28–00:17:03
perecivel: false
confianca: alta
versao: 1
```
Se o teste já estiver rodando, não edite suas configurações, porque isso faz perder parte do histórico.
Quando o teste ainda não rodou, a professora diz que pode editar.

### U:1c750220ccdd4d82:018 — Ler relatório após o período do experimento
```yaml
tipo: alerta-ui
plataforma: [google]
tema: metricas-e-relatorios
tarefas: [ler-metricas-e-relatorios, rodar-testes-e-experimentos]
fonte: fala+pdf:cst_m04_a77_como_utilizar_o_google_optimize.pdf
faixa: 00:16:28–00:17:55
perecivel: true
confianca: alta
versao: 1
```
Em “relatórios”, o experimento mostra taxa de conversão das páginas, probabilidade de cada combinação ser a melhor, sessões coletadas, dias entre início e término, meta buscada e linha do tempo.
O relatório fica sem informações enquanto o teste não começou a rodar.

### U:1c750220ccdd4d82:019 — Criar teste de redirecionamento
```yaml
tipo: procedimento
plataforma: [google]
tema: testes-e-experimentos
tarefas: [rodar-testes-e-experimentos]
fonte: fala+pdf:cst_m04_a77_como_utilizar_o_google_optimize.pdf
faixa: 00:17:55–00:20:37
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: ter a página do editor, as URLs das variantes e uma meta já disponível.
1. Em “criar experiência”, dê nome ao teste, selecione “teste de redirecionamento” e clique em “criar”.
2. Em “adicionar variantes”, dê nome à variante, informe sua URL de redirecionamento e clique em “concluído”.
3. Ajuste a segmentação por página, escolhendo “contém” como tipo de correspondência e verificando a regra.
4. Em “medição e objetivos”, escolha uma meta existente, verifique o pixel e clique em “iniciar”.

### U:1c750220ccdd4d82:020 — Acionar o redirecionamento apenas pela URL do anúncio
```yaml
tipo: decisao
plataforma: [google]
tema: testes-e-experimentos
tarefas: [rodar-testes-e-experimentos, configurar-anuncio]
fonte: fala
faixa: 00:18:32–00:19:43
perecivel: false
confianca: alta
versao: 1
```
Quando criar um teste de redirecionamento, configure a URL usada no anúncio como a única página que aciona o teste.
As páginas de destino das variantes não podem acionar novamente a experiência, senão a pessoa entra em loop.

### U:1c750220ccdd4d82:021 — Acompanhar os dados nos primeiros dias do teste
```yaml
tipo: regra
plataforma: [google]
tema: testes-e-experimentos
tarefas: [ler-metricas-e-relatorios, rodar-testes-e-experimentos]
fonte: fala+pdf:cst_m04_a77_como_utilizar_o_google_optimize.pdf
faixa: 00:21:26–00:22:05
perecivel: true
confianca: alta
versao: 1
```
Assim que o teste iniciar, acompanhe os números no Google Analytics e no Optimize.
Fique atento a problemas de configuração e a várias páginas sendo acionadas; pequenos erros podem acontecer nos primeiros dias.

### U:1c750220ccdd4d82:022 — Cancelar ou finalizar uma experiência
```yaml
tipo: procedimento
plataforma: [google]
tema: testes-e-experimentos
tarefas: [rodar-testes-e-experimentos]
fonte: fala
faixa: "00:20:47–00:21:23"
perecivel: true
confianca: alta
versao: 1
nota: Unidade acrescentada para preservar as operações de cancelar e finalizar demonstradas na fala, ausentes das unidades anteriores.
```
Pré-condição: ter acesso à experiência que deseja interromper ou encerrar.
1. Para a experiência apresentada como programada, use a opção de interromper e confirme “Cancelar o experimento”.
2. Para a experiência apresentada como em exibição, use a opção de encerrar e confirme “Finaliza a experiência”.

