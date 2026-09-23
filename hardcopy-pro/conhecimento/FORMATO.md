# FORMATO — base Hardcopy Pro

Versão 2 · 21/09/2026 (v1 de 20/09/2026; a v2 muda só a seção 6, o caminho das páginas e os campos `grupo` e `pagina`; nenhuma regra de unidade mudou). Contrato técnico da base. `processamento/base_fcc.py`, com `CURSO=hardcopy-pro`, implementa as regras marcadas **[E]** (erro) e **[W]** (aviso). O hash deste arquivo e o de `taxonomia.md` formam o `contrato_sha256` gravado no manifesto e nos julgamentos: mudar o contrato desatualiza os derivados de propósito.

Referência de origem: FORMATO do Formato Criativo de Conteúdo, que vem do Curso Subido de Tráfego. O desenho é o mesmo (unidades por aula, IDs citáveis, `unidades.jsonl`, `cobertura.jsonl`, índices, laudos). Mudam os enums, o código da aula, o vocabulário e as regras de fidelidade próprias deste curso, registradas no fim.

O leitor final é um agente. Os dados de primeira classe são `unidades.jsonl` e `cobertura.jsonl`. O Markdown é derivado para auditoria humana.

## 1. Fonte editável: `conhecimento/dados/<AULA>.json`

Um arquivo por aula, 139 no total: 138 gravações e 1 material avulso. `<AULA>` = `Gxx_Ayy`, grupo e ordem pela posição no `manifest.jsonl`. É a única fonte editável das unidades. Tudo em `conhecimento/` fora de `dados/`, `FORMATO.md` e `taxonomia.md` é gerado.

| campo | valor | regra |
|---|---|---|
| `curso` | `hardcopy-pro` | [E] |
| `aula` | `Gxx_Ayy` | [E] igual ao inventário |
| `titulo` | título da aula | [E] igual ao manifesto |
| `extraido_em` | `YYYY-MM-DD` | preenchido pelo executor |
| `gerado_por` | `sonnet-5` \| `opus-5` \| `fable-5.1` | preenchido pelo executor |
| `esforco` | `low` … `max` | preenchido pelo executor |
| `retiradas` | lista de números retirados, pode ser `[]` | [E] |
| `correcoes` | histórico de ciclos de correção | opcional, preenchido pelo executor |
| `contexto` | lista de 3–8 frases | [E] o que a aula é, para quem, o que assume, o que deixa para depois; sem timestamp, sem "hoje"/"atualmente" |
| `unidades` | lista de unidades | [E] ≥ 1; [W] fora de 3–60 |

`aula_id` = 16 primeiros hex de sha256(`hardcopy-pro/<pasta da aula>`). A pasta é estável; o código `Gxx_Ayy` muda se o manifesto ganhar aula no meio. ID citável da unidade: `U:<aula_id>:<nnn>`, regex `U:[0-9a-f]{16}:\d{3}`.

O curso tem cinco trilhas (Hard Copy, Hard Ads, Hard Sounds, Hard IA, 0 a 100K) e 18 grupos. A trilha vai no front matter da aula e em cada linha de `unidades.jsonl`, no campo `trilha`.

## 2. Unidade

Uma unidade é uma orientação que se entende e se consulta sozinha, sem a aula ao lado. Nem resumo da aula inteira, nem uma frase solta sem utilidade.

| campo | regra |
|---|---|
| `numero` | [E] inteiro; atribuído na primeira extração pela ordem de aparição na fonte e nunca muda; único no arquivo |
| `titulo` | [E] 1–80 caracteres |
| `tipo` | [E] enum `## Tipos` |
| `tema` | [E] exatamente 1 valor do enum `## Temas`. Tema de ato (`abertura-e-gancho`, `desenvolvimento-e-conexao`, `plot-twist`, `pitch-e-cta`) vence `kishotenketsu` quando a orientação é de um ato só. Tema de nicho de anúncio (`anuncio-*`) vence quando a orientação só vale para aquele tipo de negócio |
| `tarefas` | [E] lista do enum `## Tarefas`; vazia só em `conceito` e `limite` |
| `plataformas` | [E] lista com ≥1 valor do enum `## Plataformas`; `geral` quando a orientação não depende de rede nem ferramenta |
| `fonte` | [E] `fala` \| `material` \| `fala+material`. `material` só em aula com material utilizável, que neste curso é só `G02_A12` |
| `inicio`, `fim` | [E] segundos como na transcrição. Obrigatórios se `fonte` inclui `fala`; `0 ≤ inicio < fim ≤ fim da transcrição + 2`. `null` se `fonte` é só `material` |
| `condicoes` | texto ou `null`. Preenchido quando a orientação só vale sob condição, exceção, nicho ou perfil |
| `perecivel` | [E] booleano. `true` para tela, menu, configuração, prompt, recurso e política de plataforma, recurso e estrutura do curso (documento, mapa mental, produto irmão, temporada, suporte), preço, plano pago, data, oferta e número de mercado. [E] `ferramenta` ⇒ `true`. [E] qualquer plataforma além de `geral` ⇒ `true`. [E] tema `curso-e-recursos` ou tarefa `usar-recursos-do-curso` ⇒ `true` |
| `confianca` | [E] `alta` \| `media` \| `baixa`. Mede fidelidade da interpretação, não eficácia do método. `baixa` ⇒ `nota` obrigatória |
| `nota` | texto ou `null`. Dúvida de transcrição, termo identificado por hipótese, nome da ferramenta quando a plataforma é genérica, aviso de contorno de política |
| `proposta_tag` | texto ou `null`. Único caminho para tag nova: `tema: <slug> — motivo`, `tarefa: <slug> — motivo` ou `plataforma: <slug> — motivo` [E] |
| `corpo` | paráfrase fiel; regras abaixo |
| `evidencia` | [E] trecho literal de 1–24 palavras, existente na fonte, **com a grafia da transcrição, mesmo quando ela está errada**. A comparação é por sequência de palavras: ignora caixa, pontuação e as marcações de tempo, então a âncora pode atravessar marcações vizinhas. Se `fonte` inclui `fala`, está na transcrição e dentro da faixa `inicio`–`fim`; se `fonte` é `material`, está no material. É âncora para inspeção, não prova suficiente da unidade inteira |
| `versao` | [E] inteiro ≥ 1; incrementa em toda correção de corpo ou metadado semântico |

### Corpo

- [E] 1–8 linhas não vazias; `procedimento`, `exemplo` e `estrutura` até 15.
- [E] sem timestamp, sem `[[`, sem `**[`.
- [E] sem "hoje", "atualmente", "neste momento".
- [E] sem cópia bruta: nenhuma sequência de 25 palavras idêntica à transcrição ou ao material. Vale também para copy, roteiro e prompt ditados na aula: a unidade descreve as partes e o que cada uma faz, não transcreve o texto.
- [E] sem grafia deformada conhecida: o corpo, o título, as condições e o contexto usam a grafia adotada da tabela da seção 3.
- Prosa direta, no imperativo ou indicativo. Uma frase de razão é permitida ("porque…").
- Números como o professor diz. Jargão do curso é explicado na primeira ocorrência dentro da unidade, só com o que a fonte diz dele (ver o vocabulário na seção 3). Nunca desdobrar sigla nem inventar definição.

### Regras por tipo [E]

| tipo | regra |
|---|---|
| `regra` | frase categórica; sem número obrigatório |
| `regua` | corpo contém número, em algarismo ou por extenso, ou unidade |
| `procedimento` | corpo começa com `Pré-condição:` e tem lista numerada com ≥2 passos |
| `estrutura` | corpo tem lista numerada com ≥2 partes, na ordem da fonte |
| `decisao` | corpo começa com `Se ` ou `Quando ` |
| `exemplo` | corpo tem `Situação:`, `O que aconteceu:`, `Lógica:` |
| `ferramenta` | `perecivel: true` |
| `fato-material` | `fonte: material` |
| `conceito`, `limite` | `tarefas` pode ser `[]` |

## 3. Fidelidade: o que o extrator preserva

- Números, denominadores, condições, exceções, preferências e limites expressos. Condição que a fonte impõe e a unidade omite é desvio. Ressalva do professor sobre a própria técnica ("eu não usaria", "não indico") faz parte da orientação.
- Preferência do professor não vira regra universal. Número de caso (venda de um dia, conversão de uma campanha, preço que alguém cobrou) é `exemplo`, perecível, nunca `regua`. Faixa de preço dada para um nicho fica com o nicho em `condicoes`.
- **Copy de exemplo não é fato.** O professor escreve e lê na aula VSLs e anúncios de produtos inventados (CTRL Z, Menticaps, Touro Hair e outros). Percentuais, depoimentos, preços e alegações de saúde ditos dentro dessas copys pertencem ao texto de venda fictício. Entram, quando entram, como `exemplo`, com `condicoes` dizendo que é copy de exemplo. Nunca viram `regua`, `regra` nem estatística de mercado.
- Afirmações de resultado e de originalidade são atribuídas ao professor. A base documenta o que o curso ensina; não confirma eficácia.
- **Aula de tela.** Boa parte do curso é edição e configuração com o professor apontando ("clica aqui", "olha isso", "essa cor aqui"). Extrair só o que a fala descreve de modo que se entenda sem a imagem. Passo que a fala não nomeia não entra no procedimento. Se o essencial ficou na tela, registrar um `limite` dizendo o que a transcrição não captura. Aula de tela com pouca unidade é resultado esperado, não falha.
- **Resíduo de silêncio e laço de repetição não são fonte.** A transcrição automática deixou frases sem relação com a aula em aberturas, fechos e pausas: "Legenda Adriana Zanotto", "Copyright Australian Broadcasting Corporation", "Amém.", "Tchau, tchau.", "E aí" repetido, "Obrigado." solto, nome de outra trilha no começo, e blocos da mesma palavra repetida dezenas de vezes. Não extrair, não citar como evidência, não mencionar no contexto.
- **Técnica que contorna política ou direito de terceiros.** O curso ensina, por exemplo, a fatiar música comercial para escapar da detecção de direito autoral, a camuflar antes e depois para passar na moderação e a esconder que um vídeo é sintético. A base registra com fidelidade, como o que o professor ensina, com `perecivel: true`, tema `politicas-e-bloqueios` quando esse for o assunto, e `nota` começando por "Contorna política de plataforma ou direito de terceiros:". A decisão de aplicar é de quem consulta.
- Testemunho pessoal, motivação e construção de autoridade do professor não viram unidade, salvo quando carregam uma orientação. Não contam como omissão.
- Oferta comercial (outro produto do professor, temporada futura, preço, bônus, suporte pago): não extrair como orientação. Registrar um `limite` por aula dizendo que o trecho é oferta e o que ela promete cobrir.
- Aula sem conteúdo didático (abertura, recado, convite) rende uma unidade `limite` dizendo o que a aula é.
- Material avulso e fala divergem: registrar as duas versões em `nota`, baixar `confianca` se a divergência afeta a orientação, e não escolher um lado por conhecimento externo. Regras que **não** existem: "material vence fala", "aula posterior vence anterior".
- Nada de completar com conhecimento externo: estado atual de plataforma, definição de livro, prática de mercado, o que é Kishotenketsu fora do curso. Completar é sem-lastro.

### Grafias da transcrição

A transcrição automática deforma siglas, o nome do método e nomes de ferramenta. Esta tabela fixa a grafia adotada. No corpo, título, condições e contexto, usar a grafia adotada. Em `evidencia`, copiar como está na fonte. Identificação marcada como hipótese exige `nota` dizendo como a fonte grafou; se a orientação depende de qual ferramenta é, `confianca` no máximo `media`. Termo que não está na tabela e não é reconhecível fica como transcrito, entre aspas, com `nota` e `confianca: baixa`.

| Grafia adotada | Como aparece na transcrição | Base da identificação |
|---|---|---|
| Kishotenketsu | Kinshu, Kishu, Kensho, quinchu, Kinshutengetsu, Kinshoten Ketsu, Kenshu Genketsu, Kim Shu Den Kits, quinchotem queijo | Material avulso `G02_A12` escreve Kishotenketsu e os atos Ki, Sho, Ten, Ketsu |
| Ki, Sho, Ten, Ketsu | Kim, o show, plot, Ketsu | Material avulso `G02_A12` |
| VSL | BSL, PSL, DSL | Uso constante de VSL no resto do curso |
| MVE | MVR | `G17_A04` define MVE |
| Hard Copy | Rádio Cop, Rádio Copy, RedCopy, Rádio Clop, Rádio Top | Hipótese: nome do produto irmão citado como pré-requisito |
| ElevenLabs | Eleven Labs, Eleven Lapse, Eleven Eves, Eleven Leves, Eleven Lex, LevelLabs, Level Labs, Eleva | Procedimento descrito bate com a ferramenta |
| ChatGPT | chat GPT, chat de PT, chat EPT, chat IPT, chat APT | Idem |
| Veo 3 | VO3, V3, VL3 da Google | Hipótese |
| HeyGen | Rengen | Hipótese |
| Kiwify | Qify, QI-Fi, Wi-Fi, Wi-Fi Pad | Hipótese; o título da aula `G17_A04` escreve Kiwify |
| GoDaddy | Golderi | Hipótese |
| VTURB | Vetorbi, vetor | Hipótese |
| UTMify | UTM file | Hipótese |
| CapCut | cap cut, TapCut | — |
| Canva | Cava | — |
| Biblioteca de Anúncios | ads librar, Ads Libraria, Ads Librele, Eds Libraria, ads pie | Hipótese |
| ClickBank | clickbait (quando fala de plataforma de afiliação) | Hipótese |
| order bump | Rodem Bump, ordenbump | Hipótese |
| SnapTik | Snap, Tiki | Hipótese |
| SaveFrom | Save from Mad | Hipótese |
| arma de Chekhov | arma de Tchekhov | — |
| ROI | ROD | Hipótese |

Não identificados, ficam como transcritos e com `confianca: baixa`: "Teamify" (`G01_A05`), "Tomicat" ou "tomiquete" (hospedagem de página, trilha 0 a 100K), "Copsonde" ou "copy-som" (`G10_A01`), "Dote com Strickland" (`G06_A02`).

### Vocabulário recorrente do curso

Termos que aparecem em muitas aulas e são definidos em uma só. As definições abaixo são as da fonte, conferidas por script contra a transcrição, com a aula de origem. Ao explicar um desses termos numa unidade, use esta definição ou a que a própria aula der. Termo que não está aqui e que a aula não define fica como está, sem explicação inventada.

- **Kishotenketsu** — a estrutura narrativa do curso. `G02_A06`: "nada mais nada menos que a melhor forma pra reter o público através de um plot twist". `G14_A03`: "basicamente é separada em quatro atos". Os atos, no material `G02_A12`: Ki (introdução), Sho (desenvolvimento), Ten (plot twist), Ketsu (conclusão).
- **mecanismo único** — `G01_A03`: "é basicamente o diferencial que o seu produto tem em relação aos outros produtos do mercado".
- **mecanismo único oculto** — `G08_A01`: algo "que o mercado inteiro não tá vendendo"; "isso eu chamo de mecanismo único oculto".
- **MVE** — `G17_A04`: "o MVE [...] que é o nosso mecanismo único". A fonte não desdobra a sigla fora do roteiro de exemplo.
- **MVP** — `G13_A04`: "você primeiro lança a oferta pra ver se tem demanda". Dentro da copy de exemplo do CTRL Z a sigla é usada com outros desdobramentos, que pertencem à copy.
- **nível de consciência** — `G01_A05`: "o quanto ele sabe sobre aquele assunto que eu estou vendendo para ele".
- **lead** — dois sentidos. O prospect, no uso comum; e, em `G02_A02`, "O lead é o início da VSL". Em `G11_A04`: "quem chama de lead é quem já é mais antigo". Dizer na unidade qual sentido vale.
- **hook** — `G11_A04`: "O hook é o início do anúncio". **gancho** — `G07_A07`: "Aqui chamamos de gancho", a frase de abertura do anúncio.
- **plot twist** — `G02_A06`: "nada mais é do que algo que a pessoa não estava esperando acontecer".
- **pitch** — `G02_A09`: "é quando você fala pela primeira vez o valor do seu produto". Em `G14_A04`: "o pitch que eu falo é explicação do produto".
- **NPC** — `G02_A05`: "são as pessoas que estão ali pra fazer a mudança de roteiro".
- **subtexto** — `G06_A02`: "é aquilo que você coloca [...] no seu texto, no seu anúncio, de uma forma inconsciente".
- **arma de Chekhov** — `G07_A11`: princípio segundo o qual "todos os elementos presentes em uma história devem ser necessários".
- **2 mais 2 é melhor que 4** — `G06_A02`: "Mostra somente o 2 mais 2". Deixar o lead concluir em vez de entregar a resposta.
- **verdade absoluta** — `G08_A07`: "Quando a pessoa escuta uma verdade absoluta" no anúncio, o que vem depois ganha crédito. Em `G14_A04`, dentro do roteiro de exemplo: "pegamos uma verdade desconhecida e conectamos com o nosso produto".
- **elefante na sala** e **modo jacaré** — `G03_A05`: "hoje chamamos no marketing de elefante na sala"; o estado defensivo do lead, "que chamamos o modo jacaré".
- **contexto** — `G10_A02`: "O contexto é quando você é uma autoridade". Opõe-se a texto.
- **VSL Express** — `G06_A01`: "a gente chama ela de VSL Express".
- **PP** — `G12_A04`: "público e problema, é o famoso PP".
- **playrate** — `G11_A05`: "É a porcentagem entre a visualização de página e o clique da VSL".
- **plot da música** — `G09_A06`: "A parte mais importante da música". **calar a boca** — `G09_A06`: tirar a música nas partes que se quer destacar; "Eu chamo isso de calar a boca na hora certa".
- **pilar de três ofertas** — `G14_A03`: "hoje eu trabalho com o pilar de 3 classificações de ofertas".
- **estrutura 1-3-1** — `G18_A04`: "eu sempre utilizo a estrutura 131". **AD** — `G18_A04`: "AD significa anúncio". **Dark Post** — `G18_A07`: "a gente chama de Dark Post".
- **roda de ferro** — `G07_A01`: demora a girar e "depois com impulso ela roda e gira sozinha".
- **incluído, não bônus** — `G02_A09`: na fala de venda, "Você vai falar que isso é incluído". Nas aulas o professor usa "bônus" como termo didático.
- **frufru** — `G06_A09`: "Frufru é quando a pessoa é cheia de mimimi". **fadear** — `G16_A02`: aplicar fade no áudio.
- Usados sem definição na fonte: **X1**, **PLR**, **sentimentalismo**, **subnicho**, **CBO**, **CPA**. Não definir por conta própria.
- **CTRL Z**, **Menticaps**, **Touro Hair** — produtos inventados pelo professor para os exemplos. Não são casos reais.

## 4. Identidade e reconciliação

- `numero` nunca é renumerado nem reutilizado. [E] {presentes} ∪ {`retiradas`} = `1..max`, sem furo e sem repetição.
- Retirar = remover a unidade e listar o número em `retiradas`.
- Dividir ou fundir = retirar as originais e criar novas com números após o maior existente; a correspondência fica em `correcoes`.
- A ordem de apresentação é independente da identidade.

## 5. Hash e versão

`hash` da unidade = sha256 da serialização canônica de: `id`, `tipo`, `plataformas` (ordenadas), `tema`, `tarefas` (ordenadas), `fonte`, `inicio`, `fim`, `condicoes`, `perecivel`, `confianca`, corpo (linhas `strip`, espaços colapsados). `versao`, `nota`, `proposta_tag`, `titulo` e `evidencia` não entram.

A inspeção guarda o hash de cada unidade conferida. Unidade cujo hash mudou perde a evidência anterior; as intactas a preservam.

## 6. Derivados (`base_fcc.py --write`, conferidos por `--check`)

- `unidades/<pasta do curso>.md` — uma página por aula, **no mesmo caminho que a aula tem no curso**: `unidades/01 Hard Copy/2a Temporada - Kishotenketsu/hc_t2_e02_parte_04_o_que_nao_pode_faltar.md`. Trilhas, grupos e nomes de pasta são os do criador do curso, sem renomear nem reagrupar; o material avulso fica em `unidades/Materiais/01 Hard Copy/Surpresa.md`, onde o curso o guarda. O código `Gxx_Ayy` continua sendo o nome do arquivo em `dados/` e a chave de ordenação. Front matter (`type: unidades-aula`, `status`, `title`, `curso`, `trilha`, `grupo`, `modulo`, `ordem`, `aula`, `aula_id`, `account_id`, `fonte_repo`, `fonte_commit`, `fontes`, `extraido_em`, `gerado_por`, `retiradas`), `## Contexto da aula`, `## Unidades` com um bloco `### U:<aula_id>:<nnn> — <título>` + YAML + corpo por unidade. `fonte` aparece como `fala`, `txt:<arquivo>` ou `fala+txt:<arquivo>`; `faixa` como `hh:mm:ss–hh:mm:ss`.
- `status` da aula: `rascunho` (extraída e validada por script), `validado` (inspecionada com fonte), `revisado` (julgada e aprovada), `ouro` (referência do piloto aprovada).
- `unidades.jsonl` — arquivo único para o curso inteiro, uma linha por unidade viva: todos os campos da unidade + `id`, `aula`, `aula_id`, `trilha`, `grupo` (pasta do curso, com o nome do criador), `pagina` (caminho da página), `modulo`, `ordem`, `aula_titulo`, `status_aula`, `hash`.
- `cobertura.jsonl` — uma linha por tarefa × plataforma da taxonomia, **inclusive as vazias**: `tarefa`, `plataforma`, `n_unidades`, `cobertura` (`presente` \| `ausente`), `aulas`, `ids`. `ausente` significa que o curso, no alcance extraído, não cobre aquela tarefa naquela plataforma. O agente consulta isso antes de responder; não preenche a lacuna sozinho. Presença em uma plataforma não prova cobertura nas outras.
- `temas/<tema>.md` e `tarefas/<tarefa>.md` — índices sem prosa nova, unidades agrupadas por tipo. Item sem unidade gera página dizendo "Nada nas fontes processadas".
- `README.md` — índice de aulas na ordem e com os nomes de pasta do curso (trilha, grupo, material por último), e índice de temas e tarefas. `manifest.json` — inventário com hashes das fontes, commit de referência e `contrato_sha256`. `propostas_tags.md` — propostas agregadas.

## 7. Revisão (`processamento/base-consulta/revisao/`)

- `inspecao/<AULA>.json` (inspetor, com fonte): `arquivo_sha256` do JSON inspecionado, `alcance`, `unidades_verificadas`, `hashes_unidades`, veredito por unidade (`lastreada` \| `desvio` \| `sem-lastro` \| `faixa-errada`) com `gravidade`, `trecho_fonte` literal e explicação; `omissoes`; `perecibilidade`; `contrato`; `material`. O executor confere se cada `trecho_fonte` existe na fonte e lista os que não existem em `citacoes_nao_literais`.
- `julgamento/<AULA>.json` (juiz, sem fonte): `arquivo_sha256`, `inspecao_sha256`, `rodada`, `veredito` (`passa` \| `falha` \| `bloqueado`), `vetos`, parecer por área da rubrica, `falhas` consolidadas (ID, unidades, veto, evidência, impacto, mudança mínima, critério de aceite), `ajustes_menores`, `proximo`.
- `--reviews` rejeita inspeção ou julgamento cujo hash não bate com o JSON atual da aula.
- Cada chamada de modelo grava um `.execucao.json`: papel, modelo, esforço, via, início e fim, os quatro contadores de token, `stop_reason`, esperas por limite de sessão, hash do pacote e do resultado. Execução registra a chamada; laudo registra o julgamento. Um não substitui o outro.

## 8. O que muda em relação ao FORMATO do Formato Criativo

1. **Código `Gxx_Ayy` e `aula_id` pela pasta.** O manifesto deste curso não numera aulas; a pasta é o identificador estável.
2. **Campo `trilha`.** Cinco assuntos em uma base só, com um enum só, para a cobertura por tarefa atravessar as trilhas.
3. **Aula só de material** (`G02_A12`): sem transcrição, todas as unidades com `fonte: material` e sem faixa.
4. **Tabela de grafias da transcrição**, com regra de script para grafia deformada no corpo.
5. **Regras de fidelidade próprias:** copy de exemplo não é fato, aula de tela, resíduo de silêncio, técnica que contorna política, testemunho pessoal.
6. **Biblioteca espelhada no curso** (decisão de Will em 21/09/2026, antes do lote 1): páginas de aula e índice seguem as pastas, os nomes e a ordem que o criador deu ao curso. `unidades.jsonl` e `cobertura.jsonl` continuam únicos, com `trilha`, `grupo` e `pagina` por linha, para a consulta atravessar as trilhas.
7. Playbooks, checklists, glossário, consolidação entre aulas e voz ficam fora desta etapa.
