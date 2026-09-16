---
type: unidades-aula
status: validado
title: "3.1 - Eventos padrão, personalizados e conversões personalizadas"
modulo: "002"
ordem: 22
aula_id: f94349a07934812a
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - transcricao.md
extraido_em: 2026-09-14
gerado_por: gpt-5.6-terra
retiradas: []
divisoes: []
fusoes: []
---

# 3.1 - Eventos padrão, personalizados e conversões personalizadas

## Contexto da aula
A aula parte de um pixel Meta já criado e instalado no site.
Explica eventos como ações de usuários e apresenta eventos padrão, personalizados e conversões personalizadas.
Mostra caminhos de interface, configurações e exemplos de código para rastrear essas ações.
A criação de campanhas é usada apenas como exemplo; a aula seguinte trata da fase de aprendizado.

## Unidades

### U:f94349a07934812a:001 — Pixel também aparece como fonte ou conjunto de dados
```yaml
tipo: conceito
plataforma: [meta]
tema: pixel-e-eventos
tarefas: []
fonte: fala
faixa: "00:00:00–00:00:40"
perecivel: true
confianca: alta
versao: 1
```
Na interface, o pixel pode receber os nomes de fonte de dados ou conjunto de dados.
Ele pode ser criado ao conectar uma fonte de dados e configurado por API de conversões, código manual ou integração de parceiros.

### U:f94349a07934812a:002 — Criar e conceder acesso ao pixel pela BM
```yaml
tipo: procedimento
plataforma: [meta]
tema: conta-e-configuracao
tarefas: [configurar-conta, instalar-pixel-e-eventos]
fonte: fala
faixa: "00:00:41–00:01:20"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: acesso ao Gerenciador de Negócios.
1. Em fontes de dados, abra pixel e crie o pixel.
2. Dê acesso ao pixel às pessoas e às contas de anúncio necessárias.
3. Configure o pixel no site; depois disso a tela passa a mostrar atividades.

### U:f94349a07934812a:003 — Conferir pixel e eventos com Meta Pixel Helper
```yaml
tipo: procedimento
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: "00:01:20–00:02:03"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: extensão Meta Pixel Helper instalada no navegador.
1. Pesquise “Meta Pixel Helper” no Google e abra o primeiro link exibido.
2. Instale a extensão no navegador.
3. Ao entrar em um site, abra a extensão para ver qual pixel e quais eventos estão instalados.

### U:f94349a07934812a:004 — Evento é uma ação feita pelo usuário no site
```yaml
tipo: conceito
plataforma: [meta]
tema: pixel-e-eventos
tarefas: []
fonte: fala
faixa: "00:02:03–00:03:33"
perecivel: false
confianca: alta
versao: 1
```
Evento é qualquer ação realizada por uma pessoa no site.
Cadastro, visita a produto, adição ao carrinho e início de compra são exemplos de eventos.
O anunciante pede à Meta que rastreie as ações que importam para ele.

### U:f94349a07934812a:005 — Ações rastreáveis podem ser específicas
```yaml
tipo: conceito
plataforma: [meta]
tema: pixel-e-eventos
tarefas: []
fonte: fala
faixa: "00:03:33–00:04:20"
perecivel: false
confianca: alta
versao: 1
```
É possível pedir o mapeamento de compra, cadastro, clique em botão, pesquisa, inscrição em aula ou visita a páginas e produtos específicos.
A aula apresenta três formas de solicitar esse mapeamento: evento padrão, evento personalizado e conversão personalizada.

### U:f94349a07934812a:006 — Conversão é a ação escolhida como resultado da campanha
```yaml
tipo: conceito
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [definir-conversoes-e-metas]
fonte: fala
faixa: "00:04:24–00:06:20"
perecivel: true
confianca: alta
versao: 1
```
Em campanhas de vendas ou cadastros, a localização da conversão pode ser o site.
O evento de conversão é a ação que se quer que as pessoas executem após ver os anúncios.
Esse evento pode ser padrão, personalizado ou uma conversão personalizada.

### U:f94349a07934812a:007 — Eventos e conversões servem para otimizar e ler dados
```yaml
tipo: conceito
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [definir-conversoes-e-metas, ler-metricas-e-relatorios]
fonte: fala
faixa: "00:06:20–00:09:21"
perecivel: true
confianca: alta
versao: 1
```
Eventos padrão, personalizados e conversões personalizadas indicam à Meta o resultado buscado pela campanha.
Eles também tornam os dados dessas ações disponíveis para leitura nas campanhas e nas colunas do gerenciador.
Na fala, evento, ação e conversão são tratados como a mesma coisa.

### U:f94349a07934812a:008 — Conversão personalizada não gera público diretamente
```yaml
tipo: regra
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: "00:09:21–00:10:11"
perecivel: false
confianca: alta
versao: 1
```
Crie públicos a partir de eventos padrão ou eventos personalizados, mas não diretamente de conversões personalizadas.
A aula afirma que há uma forma de resolver isso, sem explicar como neste trecho.

### U:f94349a07934812a:009 — Mantenha correspondência avançada e rastreamento automático ativos
```yaml
tipo: regra
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: "00:10:11–00:11:28"
perecivel: true
confianca: alta
versao: 1
```
Nas configurações do pixel, mantenha ativados correspondência avançada e rastreamento automático de eventos sem código.

### U:f94349a07934812a:010 — Caminhos para recuperar o código do pixel
```yaml
tipo: procedimento
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: "00:10:46–00:12:07"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: pixel aberto na interface Meta.
1. Use “adicionar eventos” e “adicionar uma nova integração”.
2. Escolha Pixel da Meta e abra “configurar”.
3. Selecione código manual, integração de parceiros ou envio de instruções por e-mail.
4. Copie o código do pixel e retorne à visão geral dos eventos.

### U:f94349a07934812a:011 — Criar conversão personalizada por regra de URL
```yaml
tipo: procedimento
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [definir-conversoes-e-metas]
fonte: fala
faixa: "00:12:07–00:14:17"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: pixel instalado e página cuja URL identifica a conversão.
1. Em “adicionar eventos”, escolha conversão personalizada.
2. Dê um nome identificável, escolha o pixel como fonte de dados e site como fonte da ação.
3. Defina uma regra de URL contendo o trecho que identifica a ação.
4. Crie a conversão; a aula orienta remover o prefixo `https://` ao preencher a URL.

### U:f94349a07934812a:012 — Página com “/obrigado” pode identificar cadastro
```yaml
tipo: exemplo
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [definir-conversoes-e-metas]
fonte: fala
faixa: "00:12:48–00:14:17"
perecivel: false
confianca: alta
versao: 1
```
Situação: quem se cadastra em uma aula chega a uma URL terminada em `/obrigado`.
O que aconteceu: foi criada uma conversão personalizada para identificar a visita a essa página.
Lógica: se várias páginas de cadastro terminam em `/obrigado`, esse trecho pode sinalizar que a pessoa se cadastrou em algo.

### U:f94349a07934812a:013 — Conversão personalizada criada fica disponível na campanha
```yaml
tipo: conceito
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [definir-conversoes-e-metas]
fonte: fala
faixa: "00:14:17–00:15:11"
perecivel: true
confianca: alta
versao: 1
```
Depois de criada, a conversão personalizada pode ser escolhida como conversão na configuração da campanha.
Se ela não aparecer logo após a criação, o professor atualiza a tela no exemplo.

### U:f94349a07934812a:014 — Eventos padrão e personalizados exigem edição do código
```yaml
tipo: conceito
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: "00:15:11–00:16:24"
perecivel: false
confianca: alta
versao: 1
```
Conversões personalizadas são criadas por URL.
Eventos padrão e personalizados são criados por edição do código do pixel.
O código base contém a identificação numérica do pixel e o evento `PageView`.

### U:f94349a07934812a:015 — Evento padrão Lead registra envio de informações
```yaml
tipo: conceito
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: "00:16:24–00:17:55"
perecivel: false
confianca: alta
versao: 1
```
Lead é um evento padrão ligado ao envio de informações pelo cliente.
Quando o código com esse evento está em uma página, sua visita dispara o evento.
No exemplo, o evento Lead fica na página posterior ao envio do cadastro, não na página do formulário.

### U:f94349a07934812a:016 — Plataformas podem instalar eventos padrão automaticamente
```yaml
tipo: decisao
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: "00:17:55–00:20:22"
perecivel: false
confianca: media
versao: 1
nota: "O professor cita uma plataforma de e-commerce com nome incerto na transcrição: “nuvem shop”, seguido de “acho que é isso”."
```
Se a plataforma de e-commerce, cardápio digital ou venda de infoproduto solicitar o ID do pixel, forneça esse número para que ela instale os eventos.
No exemplo, a integração registra automaticamente PageView, ViewContent, AddToCart e InitiateCheckout.
Se a ferramenta não fizer essa instalação, faça o disparo dos códigos ou contrate um programador.

### U:f94349a07934812a:017 — Evento personalizado recebe um nome definido pelo anunciante
```yaml
tipo: conceito
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: "00:20:22–00:21:02"
perecivel: false
confianca: media
versao: 1
nota: "O nome do exemplo é transcrito como “typ aulas”; o professor o explica como evento de pessoas cadastradas em aulas."
```
Evento personalizado é um evento definido pelo anunciante, fora da lista de eventos padrão da Meta.
Ele permite nomear uma ação específica para o negócio, como pessoas cadastradas em aulas.

### U:f94349a07934812a:018 — Criar evento personalizado a partir de cópia do código
```yaml
tipo: procedimento
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: "00:21:02–00:22:24"
perecivel: false
confianca: media
versao: 1
nota: "O exemplo de nome é transcrito como “typ aulas”."
```
Pré-condição: acesso ao código do pixel e à página onde o evento deve disparar.
1. Copie uma linha `fbq` de rastreamento, mantendo a linha original.
2. Ao lado de `track`, escreva `Custom` com a primeira letra maiúscula.
3. Entre aspas retas, informe o nome do evento personalizado, como `typ aulas`.
4. Instale o código na página em que o evento deve ser disparado.

### U:f94349a07934812a:019 — Use aspas retas no código
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: "00:21:02–00:22:24"
perecivel: true
confianca: alta
versao: 1
```
Ao editar o código, use aspas retas, não aspas curvadas.
O professor recomenda copiar e colar o trecho para não alterar as aspas.

### U:f94349a07934812a:020 — Ordem de preferência entre os três tipos de evento
```yaml
tipo: regra
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [definir-conversoes-e-metas]
fonte: fala
faixa: "00:22:24–00:23:06"
perecivel: false
confianca: alta
versao: 1
```
Dê preferência a eventos padrão, depois a eventos personalizados e, por último, a conversões personalizadas.
O professor afirma que o rastreamento do evento padrão é melhor que o do personalizado, que é melhor que o da conversão personalizada.

### U:f94349a07934812a:021 — Público por visita à página não é público por conversão personalizada
```yaml
tipo: conceito
plataforma: [meta]
tema: pixel-e-eventos
tarefas: [montar-publicos-personalizados]
fonte: fala
faixa: "00:23:06–00:23:44"
perecivel: false
confianca: alta
versao: 1
```
É possível criar um público de pessoas que visitaram páginas determinadas do site.
Isso pode parecer equivalente a usar uma conversão personalizada, mas o público é criado pela visita à página, não pela conversão personalizada.

### U:f94349a07934812a:022 — Google Tag Manager ajuda a instalar códigos no site
```yaml
tipo: conceito
plataforma: [geral]
tema: pixel-e-eventos
tarefas: [instalar-pixel-e-eventos]
fonte: fala
faixa: "00:23:44–00:24:20"
perecivel: false
confianca: alta
versao: 1
```
Google Tag Manager ajuda a instalar no site os códigos de eventos padrão e personalizados.
O professor apresenta instalar códigos no site como a função da ferramenta e recomenda dominá-la.

### U:f94349a07934812a:023 — A fase de aprendizado fica para a próxima aula
```yaml
tipo: limite
plataforma: [meta]
tema: otimizacao
tarefas: []
fonte: fala
faixa: "00:24:20–00:24:24"
perecivel: false
confianca: alta
versao: 1
```
A aula não explica a fase de aprendizado nem como ela afeta as campanhas; esse tema é anunciado para a próxima aula.