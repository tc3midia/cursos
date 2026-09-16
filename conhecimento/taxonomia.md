---
type: taxonomia
status: proposta
title: Taxonomia — Curso Subido de Tráfego v2
account_id: account.86ajrj8n9
promoted_by: human.will
versao: 1
---

# Taxonomia

Enums fechados que `ferramentas/curso-subido/validate_unidades.py` lê. Um valor fora destas listas é **erro
duro**. Tag nova entra só por `proposta_tag` na unidade, triagem no fim de cada módulo e edição deste
arquivo (com `versao` incrementada). Formato de cada entrada: `` - `slug` — definição ``. Em Tarefas,
a tabela tem a coluna de plataformas cobertas esperadas; ela vira teste na etapa 3.

## Plataformas

- `geral` — vale para qualquer plataforma; princípios do módulo 001 e regras que o professor aplica a Meta e Google igualmente
- `meta` — Meta Ads (Facebook/Instagram), Gerenciador de Anúncios e de Negócios
- `google` — Google Ads como conta e produto, quando a orientação vale para todas as redes do Google
- `google-search` — Rede de Pesquisa do Google
- `youtube` — campanhas de vídeo no YouTube
- `google-display` — Rede de Display do Google
- `ads-editor` — Google Ads Editor (aplicativo desktop)
- `tiktok` — TikTok Ads

## Temas

- `fundamentos-e-carreira` — o que é tráfego, papel do gestor, hábitos, como estudar, relação com o cliente
- `conta-e-configuracao` — criação e configuração de contas, BM, perfis, acessos, fuso, moeda, pagamento
- `pixel-e-eventos` — pixel, API de conversões, eventos padrão e personalizados, aquecimento
- `atribuicao` — janelas e modelos de atribuição, comparação entre plataformas e relatórios
- `leilao-e-lances` — funcionamento do leilão, fatores, estratégias e ajustes de lance
- `orcamento` — definição, distribuição e alteração de orçamento; CBO/ABO
- `objetivos` — objetivos de campanha e metas de desempenho por tipo de negócio
- `estrutura-de-campanha` — hierarquia campanha/conjunto/anúncio, número de conjuntos, organização
- `nomenclatura` — padrões de nome de campanha, conjunto, anúncio e público
- `publicos` — públicos personalizados, semelhantes, demografia, interesses, sobreposição e exclusão
- `palavras-chave` — pesquisa, lista, tipos de correspondência e negativas
- `posicionamentos-e-formatos` — canais, posicionamentos, formatos de anúncio e dimensões
- `criativo` — qualidade do anúncio, referências, imagem, vídeo, estrutura de criativo
- `copy-e-roteiro` — texto, título, descrição, roteiro de vídeo, ganchos e uso de IA
- `destino-e-landing-page` — página de destino, coerência anúncio-página, formulários e mensagens
- `metricas-e-relatorios` — métricas principais e secundárias, relatórios, leitura de painel
- `otimizacao` — diagnóstico e ajuste de campanhas em andamento
- `testes-e-experimentos` — hipóteses, testes A/B, princípios de teste
- `escala` — como aumentar resultado: verba, públicos, canais, teto de leilão

## Tarefas

| tarefa | grupo | plataformas cobertas (esperado) | definição |
|---|---|---|---|
| `configurar-conta` | fundacao | meta, google, tiktok | criar e configurar conta de anúncios, BM, acessos, fuso, moeda e pagamento |
| `instalar-pixel-e-eventos` | fundacao | meta, google, tiktok | instalar pixel/tag, API de conversões e eventos |
| `definir-conversoes-e-metas` | fundacao | meta, google | escolher e configurar conversões e metas que a campanha vai otimizar |
| `configurar-janela-de-atribuicao` | fundacao | meta, google | definir janela e modelo de atribuição |
| `escolher-objetivo-de-campanha` | planejamento | meta, google, tiktok | escolher objetivo de campanha pelo tipo de negócio |
| `definir-estrutura-de-campanha` | planejamento | meta, google-search, youtube, google-display, tiktok | decidir quantas campanhas, conjuntos/grupos e anúncios, e como se organizam |
| `nomear-campanhas` | planejamento | meta, google | aplicar padrão de nomenclatura a campanhas, conjuntos, anúncios, públicos e conversões |
| `definir-orcamento` | planejamento | meta, google | definir e distribuir orçamento inicial |
| `escolher-estrategia-de-lance` | planejamento | meta, google, tiktok | escolher estratégia de lance e valores iniciais |
| `montar-publicos-personalizados` | segmentacao | meta, google, tiktok | criar públicos personalizados (site, lista, vídeo, engajamento) |
| `montar-publicos-semelhantes` | segmentacao | meta, google, tiktok | criar públicos semelhantes a partir de origem |
| `definir-segmentacao-demografica-e-interesses` | segmentacao | meta, google-search, youtube, google-display, tiktok | localização, idade, gênero, idioma, interesses e comportamentos |
| `montar-lista-de-palavras-chave` | segmentacao | google-search | pesquisar e montar lista com tipos de correspondência |
| `definir-palavras-chave-negativas` | segmentacao | google-search | listar e aplicar negativas |
| `organizar-hierarquia-e-exclusao-de-publicos` | segmentacao | meta, google | evitar sobreposição; excluir públicos entre conjuntos |
| `escolher-canais-e-posicionamentos` | segmentacao | meta, youtube, google-display, tiktok | escolher canais, posicionamentos e dispositivos |
| `coletar-referencias-de-anuncio` | criativo | geral, meta, google, tiktok | reunir referências de anúncios para inspirar criativos |
| `escrever-copy-e-roteiro` | criativo | geral, meta, google-search, youtube, tiktok | escrever texto, título, descrição e roteiro |
| `fazer-briefing-de-criativo` | criativo | geral, meta, youtube, google-display | pedir criativo a designer/editor com especificações |
| `configurar-anuncio` | criativo | meta, google-search, youtube, google-display, tiktok | montar o anúncio na plataforma: formato, mídia, campos, destino |
| `usar-ia-para-anuncios` | criativo | geral | usar ChatGPT e afins para gerar copy e ideias |
| `criar-campanha` | execucao | meta, google-search, youtube, google-display, tiktok | criar campanha do zero na interface |
| `replicar-campanhas-e-grupos` | execucao | meta, ads-editor | duplicar campanhas, conjuntos e anúncios |
| `converter-campanha-entre-redes` | execucao | ads-editor | transformar campanha de uma rede em outra |
| `operar-ads-editor` | execucao | ads-editor | instalar, baixar, editar em massa e publicar pelo Ads Editor |
| `criar-campanha-de-catalogo` | execucao | meta | campanhas de catálogo/produto |
| `criar-campanha-de-formulario` | execucao | meta, tiktok | campanhas de geração de cadastros com formulário nativo |
| `criar-campanha-de-mensagem` | execucao | meta | campanhas de mensagem (WhatsApp/Direct/Messenger) |
| `criar-campanha-de-reconhecimento-ou-seguidores` | execucao | meta, tiktok | campanhas de alcance, reconhecimento ou seguidores |
| `diagnosticar-campanha-sem-gasto` | diagnostico | meta, google | campanha aprovada que não gasta ou não entrega |
| `diagnosticar-concentracao-de-verba` | diagnostico | meta, youtube, google-display | verba concentrada em um conjunto/grupo/anúncio |
| `ler-metricas-e-relatorios` | diagnostico | geral, meta, google, tiktok | ler painel, montar e interpretar relatórios |
| `otimizar-lances` | diagnostico | meta, google | ajustar lance de campanha em andamento |
| `otimizar-publicos-e-segmentacoes` | diagnostico | meta, google-search, youtube, google-display | ajustar públicos e segmentações em andamento |
| `otimizar-anuncios` | diagnostico | meta, google-search, youtube, google-display | trocar, pausar e melhorar anúncios em andamento |
| `otimizar-estruturas` | diagnostico | meta, google | reorganizar campanhas e conjuntos em andamento |
| `otimizar-palavras-chave` | diagnostico | google-search | ajustar lista, correspondência e negativas em andamento |
| `otimizar-landing-page` | diagnostico | geral, google-search | melhorar página de destino a partir das métricas |
| `rodar-testes-e-experimentos` | diagnostico | geral, meta, google | planejar, rodar e ler testes |
| `escalar-campanha` | diagnostico | geral, meta, google | aumentar resultado de campanha que já funciona |
| `formar-se-como-gestor` | fundacao | geral | estudar o curso e a ferramenta, desenvolver hábitos do gestor, escolher modelo de atuação e crescer a operação de gestão |
| `produzir-conteudo-organico` | criativo | geral | planejar e produzir conteúdo orgânico (linha editorial, distribuição) que complementa o tráfego pago |

Sem tarefa `auditar-conta`: auditoria é visão (`visoes/checklists/<plataforma>.md`) montada de unidades
`regua`, `regra`, `decisao` e `alerta-ui`.

## Tipos

- `regra` — orientação categórica do professor (faça/não faça), sem número
- `regua` — critério numérico ou unidade observável (limite, faixa, quantidade, prazo)
- `procedimento` — sequência de passos com pré-condição
- `decisao` — escolha condicional: "Se X, então Y" / "Quando X, prefira Y"
- `conceito` — definição ou explicação de mecanismo; sem ação direta
- `exemplo` — caso do professor comprimido: situação → o que aconteceu → lógica copiável
- `alerta-ui` — descrição de tela, botão ou caminho de menu; perecível por natureza
- `fato-material` — dado que só existe no PDF/txt (lista, tabela, template)
- `limite` — o que a aula declara não cobrir ou deixar para depois
