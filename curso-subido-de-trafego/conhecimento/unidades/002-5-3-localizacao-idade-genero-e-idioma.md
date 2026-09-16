---
type: unidades-aula
status: validado
title: "5.3 - Localização, idade, gênero e idioma"
modulo: "002"
ordem: 28
aula_id: fd00fa74026cdd49
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

# 5.3 - Localização, idade, gênero e idioma

## Contexto da aula
A aula demonstra no Meta Ads a segmentação por localização, idade, gênero e idioma.
Explica como públicos em campos diferentes se combinam e como isso pode reduzir o alcance.
Mostra cidades, CEPs, pinos, exclusões, listas de localizações e segmentação por idioma.
O direcionamento detalhado fica para a próxima aula.

## Unidades

### U:fd00fa74026cdd49:001 — Públicos no mesmo campo se somam; campos diferentes restringem
```yaml
tipo: conceito
plataforma: [meta]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses, montar-publicos-personalizados]
fonte: fala
faixa: "00:00:00–00:01:29"
perecivel: false
confianca: alta
versao: 1
```
Públicos personalizados colocados no mesmo campo funcionam como um ou outro: envolvimento no Instagram ou visita ao site, inclusive quem fez os dois.
Ao combinar público, país, idade e gênero em campos diferentes, a pessoa precisa atender a todas essas condições.

### U:fd00fa74026cdd49:002 — Evite resegmentar até deixar o público pequeno
```yaml
tipo: regra
plataforma: [meta]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses, montar-publicos-personalizados]
fonte: fala
faixa: "00:00:59–00:01:29"
perecivel: false
confianca: alta
versao: 1
```
Cuidado com a resegmentação: somar público personalizado, localização, idade e gênero pode deixar o público muito pequeno.

### U:fd00fa74026cdd49:003 — Escolher estado ou cidade na localização
```yaml
tipo: procedimento
plataforma: [meta]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: "00:01:29–00:02:11"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: campo de localização aberto no conjunto de anúncios.
1. Digite o local desejado, como Paraná ou Londrina.
2. Leia a identificação exibida ao lado do resultado para confirmar se é estado, cidade ou outra localização.
3. Ao selecionar uma cidade, confira o raio aplicado, pois ele pode incluir cidades ao redor.

### U:fd00fa74026cdd49:004 — Raio mínimo ao redor de uma cidade
```yaml
tipo: regua
plataforma: [meta]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: "00:02:00–00:02:53"
condicoes: "ao usar raio em volta de uma cidade"
perecivel: true
confianca: alta
versao: 1
```
Uma cidade pode vir com raio de 40 quilômetros; é possível escolher apenas a cidade ou usar raio ao redor dela.
O menor raio que a tela permite é 17 quilômetros; 1 quilômetro não é aceito nessa opção.

### U:fd00fa74026cdd49:005 — Segmentar um CEP pelos cinco primeiros dígitos
```yaml
tipo: procedimento
plataforma: [meta]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: "00:02:13–00:03:32"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: campo de localização aberto e CEP da área desejada disponível.
1. Digite apenas os cinco primeiros dígitos do CEP, como 86015.
2. Selecione o resultado identificado como CEP, cidade, estado e país.
3. Use essa seleção para anunciar somente naquele CEP.

### U:fd00fa74026cdd49:006 — Expandir o pino quando os resultados saturarem
```yaml
tipo: exemplo
plataforma: [meta]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: "00:03:32–00:04:10"
perecivel: true
confianca: alta
versao: 1
```
Situação: um negócio anuncia em torno do próprio endereço.
O que aconteceu: o professor adiciona um pino sobre o negócio com 1 quilômetro; quando os resultados começam a saturar após aparecer para todos, adiciona outro pino de 2 quilômetros.
Lógica: ampliar os pinos progressivamente permite anunciar para públicos territoriais cada vez maiores; ele chama isso de estratégia war.

### U:fd00fa74026cdd49:007 — Excluir CEP ou área atendida pelo pino
```yaml
tipo: procedimento
plataforma: [meta]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: "00:04:10–00:05:24"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: uma localização ou pino já selecionado e uma área onde o negócio não atende.
1. Adicione o CEP da área que não deve receber o anúncio.
2. Use a seta da localização e escolha excluir essa localização.
3. Para excluir uma região maior, adicione um pino nela, reduza-o até 1 quilômetro e exclua-o.
4. Confira o mapa: azul indica onde aparece; vermelho indica onde não aparece.

### U:fd00fa74026cdd49:008 — Adicionar localizações em massa
```yaml
tipo: procedimento
plataforma: [meta]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: "00:04:45–00:06:02"
perecivel: true
confianca: alta
versao: 1
```
Pré-condição: opções de localização abertas no conjunto de anúncios.
1. Use adicionar localizações em massa.
2. Informe país, região ou estado, cidade, código postal ou endereço.
3. Adicione vários endereços ou cidades quando isso for mais fácil do que inseri-los individualmente.

### U:fd00fa74026cdd49:009 — Faixas de idade e opções de gênero
```yaml
tipo: regua
plataforma: [meta]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: "00:05:24–00:06:02"
perecivel: true
confianca: alta
versao: 1
```
A segmentação de idade permite anunciar de 18 até 65 mais; ao inserir 65, a opção fica como 65 mais.
As opções de gênero mostradas são todos, homens e mulheres.

### U:fd00fa74026cdd49:010 — Salvar lista de localizações recorrentes
```yaml
tipo: alerta-ui
plataforma: [meta]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: "00:06:03–00:06:39"
perecivel: true
confianca: alta
versao: 1
```
Na opção procurar é possível criar uma lista de localização salva para uso recorrente.
A tela também apresenta regiões como zona do euro, mercados emergentes, áreas com App Store, áreas de livre comércio e Mercosul.

### U:fd00fa74026cdd49:011 — Usar idioma para alcançar brasileiros fora do Brasil
```yaml
tipo: exemplo
plataforma: [meta]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: "00:05:24–00:07:42"
perecivel: true
confianca: alta
versao: 1
```
Situação: anunciar para brasileiros que moram nos Estados Unidos.
O que aconteceu: o professor seleciona Estados Unidos da América como localização, português Brasil como idioma, todos os gêneros e idade de 18 a 65; a estimativa exibida fica entre 1,3 e 1,6 milhões de pessoas.
Lógica: a segmentação de idioma alcança pessoas nos Estados Unidos que usam Instagram e Facebook em português.

### U:fd00fa74026cdd49:012 — Testar inglês como idioma no Brasil
```yaml
tipo: exemplo
plataforma: [meta]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: "00:07:42–00:09:09"
perecivel: true
confianca: media
versao: 1
nota: "O professor associa o idioma inglês no Instagram e Facebook a possível nível cultural maior, sem apresentar evidência ou regra geral."
```
Situação: testar uma fatia menor de público dentro do Brasil.
O que aconteceu: com inglês, a tela mostra 23 milhões de pessoas; com português Brasil, a estimativa exibida é de 149 a 175 milhões.
Lógica: o professor apresenta o idioma inglês como teste possível para qualificar o público e diz que, muitas vezes, não se segmenta idioma algum.

### U:fd00fa74026cdd49:013 — Anunciar para um CEP sem público personalizado
```yaml
tipo: regra
plataforma: [meta]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses]
fonte: fala
faixa: "00:09:09–00:09:42"
perecivel: false
confianca: alta
versao: 1
```
Não é obrigatório incluir público personalizado: é possível anunciar para todas as pessoas de um CEP com idade de 18 a 65 e todos os gêneros.

### U:fd00fa74026cdd49:014 — Público semelhante fica mais específico dentro de uma localização
```yaml
tipo: decisao
plataforma: [meta]
tema: publicos
tarefas: [definir-segmentacao-demografica-e-interesses, montar-publicos-semelhantes]
fonte: fala
faixa: "00:09:09–00:09:57"
perecivel: false
confianca: alta
versao: 1
```
Se adicionar um público semelhante a uma localização específica, considere que o público pode ficar muito pequeno.
Os 1,7 milhões citados para o público semelhante correspondem ao Brasil inteiro, não necessariamente à localização selecionada.

### U:fd00fa74026cdd49:015 — Direcionamento detalhado fica para outra aula
```yaml
tipo: limite
plataforma: [meta]
tema: publicos
tarefas: []
fonte: fala
faixa: "00:09:43–00:09:57"
perecivel: false
confianca: alta
versao: 1
```
A aula encerra localização, idade, gênero e idioma; os direcionamentos detalhados são apresentados na próxima aula.