## Escopo e rastreabilidade

Reinspeção focal de U026 e U035, com dependências U023, U027, U034 e U037 para regressões materiais. Fonte: `transcricao.md`, SHA-256 `11c558…602083`; rubrica SHA-256 `cb66…09f47`. Validador informado: zero erros; 55 unidades. Não há evidência anterior preservada no pacote para compor cobertura integral.

| id | veredito | evidência |
|---|---|---|
| U023 | lastreada | Fala 00:22:01–00:23:26: “comparar uma campanha focada em engajamento… com outra campanha idêntica… visualização de vídeo”. |
| U026 | lastreada | Fala 00:23:40–00:24:31: “Vale o teste, mas eu sempre teria as duas rodando em paralelo.” A preferência aparece com referente/nomenclatura ambíguos. |
| U027 | lastreada | Fala 00:27:15–00:27:54: “Google Play, App Store… app ou URL exato… maximizar… instalação… ou eventos”. |
| U034 | lastreada | Fala 00:33:49–00:35:03: no Instagram, “ferramenta que pegue esses dados e envia… CRM”; contatos também “no Instagram e no Messenger”. |
| U035 | lastreada | Fala 00:35:03–00:36:16: “quando você sabe operar… nível altíssimo, você vai fazer… vendas manual”; “ter as duas rodando para testar”. |
| U037 | lastreada | Fala 00:36:56–00:37:42: “tem que ter pixel quando eu quero mapear uma ação… no site”; Instagram e Messenger “não precisa de pixel”. |

## Omissões

- Resolução U026: a transcrição recomenda rodar ambas em paralelo, mas a escolha singular usa “essa daqui” e alterna “anúncios do WhatsApp”/“anúncios do aplicativo”. A unidade preserva a incerteza; sem omissão material focal. Fonte: fala 00:23:40–00:24:31.
- Resolução U035: a condição para campanha manual está presente — domínio operacional em nível alto — e o teste das duas opções também. Sem omissão material focal. Fonte: fala 00:35:03–00:36:16.
- Detalhe complementar fora do escopo focal: catálogo exige e-commerce/produtos do site conectados à Meta, mas isso pertence à continuação sobre catálogo, não altera o teste Advantage Plus/manual. Fonte: fala 00:36:16–00:36:56.
- Não foi comprovada regressão material nas dependências conferidas.

## Contrato

- Não há sequência bruta identificável de 25 palavras nas seis unidades apresentadas; comparação limitada aos blocos e janelas fornecidos.
- Não há timestamp no corpo, `[[` ou “hoje” no corpo dos blocos apresentados.
- O validador informado declara `erros: []`, `fontes_disco: ["transcricao.md"]` e `fontes_declaradas: ["transcricao.md"]`.
- A presença física no disco e eventual PDF/txt não utilizado não foram verificáveis sem ferramentas; o pacote só informa `transcricao.md`.

## Material

- Material informado: `transcricao.md`; contém as janelas de fala que sustentam as seis unidades.
- Nenhum PDF ou TXT adicional é declarado pelo validador fornecido.
- Não há `fato-material` entre os blocos apresentados; cobertura de materiais adicionais não se aplica ao escopo focal.

## Perecível

- U026, U027, U034 e U035 descrevem opções, metas ou fluxos de interface e possuem `perecivel: true`.
- U023 descreve comparação de campanhas, sem caminho/tela específico; `perecivel: false`.
- U037 estabelece regra de mensuração/conversão, sem descrição de tela; `perecivel: false`.