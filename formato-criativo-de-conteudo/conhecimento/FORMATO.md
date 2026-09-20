# FORMATO — base Formato Criativo de Conteúdo

Versão 1 · 19/09/2026. Contrato técnico da base. `processamento/base_fcc.py` implementa as regras marcadas **[E]** (erro) e **[W]** (aviso). O hash deste arquivo e o de `taxonomia.md` formam o `contrato_sha256` gravado no manifesto e nos julgamentos: mudar o contrato desatualiza os derivados de propósito.

Referência de origem: FORMATO do Curso Subido de Tráfego. O desenho é o mesmo (unidades por aula, IDs citáveis, `unidades.jsonl`, `cobertura.jsonl`, índices, laudos). Mudam os enums, que são deste curso, e três adaptações registradas no fim.

O leitor final é um agente. Os dados de primeira classe são `unidades.jsonl` e `cobertura.jsonl`. O Markdown é derivado para auditoria humana.

## 1. Fonte editável: `conhecimento/dados/<AULA>.json`

Um arquivo por aula, 54 no total. `<AULA>` = `Mxx_Axx` (módulo e ordem do `manifest.jsonl`). É a única fonte editável das unidades. Tudo em `conhecimento/` fora de `dados/`, `FORMATO.md` e `taxonomia.md` é gerado.

| campo | valor | regra |
|---|---|---|
| `curso` | `formato-criativo-de-conteudo` | [E] |
| `aula` | `Mxx_Axx` | [E] igual ao inventário |
| `titulo` | título da aula | [E] igual ao manifesto |
| `extraido_em` | `YYYY-MM-DD` | preenchido pelo executor |
| `gerado_por` | `sonnet-5` \| `opus-5` \| `fable-5.1` | preenchido pelo executor |
| `esforco` | `low` … `max` | preenchido pelo executor |
| `retiradas` | lista de números retirados, pode ser `[]` | [E] |
| `correcoes` | histórico de ciclos de correção | opcional, preenchido pelo executor |
| `contexto` | lista de 3–8 frases | [E] o que a aula é, para quem, o que assume, o que deixa para depois; sem timestamp, sem "hoje"/"atualmente" |
| `unidades` | lista de unidades | [E] ≥ 1; [W] fora de 3–60 |

`aula_id` = 16 primeiros hex de sha256(`formato-criativo-de-conteudo/Mxx_Axx`). ID citável da unidade: `U:<aula_id>:<nnn>`, regex `U:[0-9a-f]{16}:\d{3}`.

## 2. Unidade

Uma unidade é uma orientação que se entende e se consulta sozinha, sem a aula ao lado. Nem resumo da aula inteira, nem uma frase solta sem utilidade.

| campo | regra |
|---|---|
| `numero` | [E] inteiro; atribuído na primeira extração pela ordem de aparição na fonte e nunca muda; único no arquivo |
| `titulo` | [E] 1–80 caracteres. Unidade específica de um formato começa com o nome do formato e dois-pontos (`Narrado: trocar a imagem a cada ~3 s`) |
| `tipo` | [E] enum `## Tipos` |
| `tema` | [E] exatamente 1 valor do enum `## Temas`. Em aula de formato, o tema `formato-*` vence quando a orientação é específica daquele formato; tema geral quando vale para vários |
| `tarefas` | [E] lista do enum `## Tarefas`; vazia só em `conceito` e `limite` |
| `plataformas` | [E] lista com ≥1 valor do enum `## Plataformas`; `geral` quando a orientação não depende de rede nem ferramenta |
| `fonte` | [E] `fala` \| `material` \| `fala+material`. `material` só em aula com material utilizável |
| `inicio`, `fim` | [E] segundos na escala da aula original, como na transcrição. Obrigatórios se `fonte` inclui `fala`; `0 ≤ inicio < fim ≤ fim da transcrição + 2`. `null` se `fonte` é só `material` |
| `condicoes` | texto ou `null`. Preenchido quando a orientação só vale sob condição, exceção ou para um perfil |
| `perecivel` | [E] booleano. `true` para tela, menu, configuração, prompt, recurso de plataforma, recurso e estrutura do curso (link, documento-modelo, quadro, comunidade, lista de módulos, ordem das aulas), preço, data, oferta e número de mercado. [E] `ferramenta` ⇒ `true`. [E] qualquer plataforma além de `geral` ⇒ `true`, porque depender de rede ou ferramenta é depender de algo que muda. [E] tema `curso-e-recursos` ou tarefa `usar-recursos-do-curso` ⇒ `true` (decisão de Will em 19/09/2026: estrutura do curso é perecível) |
| `confianca` | [E] `alta` \| `media` \| `baixa`. Mede fidelidade da interpretação, não eficácia do método. `baixa` ⇒ `nota` obrigatória |
| `nota` | texto ou `null`. Dúvida de transcrição, nome próprio incerto, divergência fala × material, nome da ferramenta quando `plataformas` tem `outra` |
| `proposta_tag` | texto ou `null`. Único caminho para tag nova: `tema: <slug> — motivo`, `tarefa: <slug> — motivo` ou `plataforma: <slug> — motivo` [E] |
| `corpo` | paráfrase fiel; regras abaixo |
| `evidencia` | [E] trecho literal de 1–24 palavras, existente na fonte. A comparação é por sequência de palavras: ignora caixa, pontuação e as marcações de tempo, então a âncora pode atravessar marcações vizinhas. Se `fonte` inclui `fala`, está na transcrição e dentro da faixa `inicio`–`fim`; se `fonte` é `material`, está no material. É âncora para inspeção, não prova suficiente da unidade inteira |
| `versao` | [E] inteiro ≥ 1; incrementa em toda correção de corpo ou metadado semântico |

### Corpo

- [E] 1–8 linhas não vazias; `procedimento`, `exemplo` e `estrutura` até 15.
- [E] sem timestamp, sem `[[`, sem `**[`.
- [E] sem "hoje", "atualmente", "neste momento".
- [E] sem cópia bruta: nenhuma sequência de 25 palavras idêntica à transcrição ou ao material.
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

- Números, denominadores, condições, exceções, preferências e limites expressos. Condição que a fonte impõe e a unidade omite é desvio.
- Preferência do professor não vira regra universal. Número de caso (seguidores ganhos, faturamento de aluno, preço que alguém cobrou) é `exemplo`, perecível, nunca `regua`.
- Afirmações de resultado são atribuídas ao professor. A base documenta o que o curso ensina; não confirma eficácia.
- Fala e material divergem: registrar as duas versões em `nota`, baixar `confianca` se a divergência afeta a orientação, e não escolher um lado por conhecimento externo. Regras que **não** existem: "material vence fala", "aula posterior vence anterior".
- Nomes de criadores e perfis variam entre fala e material e dentro da mesma transcrição. Usar a grafia do material quando ele cita o nome; se só a fala cita, manter como transcrito e registrar a incerteza em `nota`. Não corrigir por conhecimento externo.
- Trecho degradado de transcrição (repetição em laço, legenda fantasma no fim do áudio) não é fonte. Não extrair dele.
- Conteúdo visual que a fala só aponta ("olha isso aqui", gesto, marcação no chão): extrair apenas o que a fala ou o material descrevem. Se o essencial ficou só na imagem, registrar um `limite` dizendo o que a transcrição não captura.
- Oferta comercial dos professores (comunidade paga, formação futura, preço, bônus, data): não extrair como orientação. Registrar um `limite` por aula dizendo que o trecho é oferta e o que ela promete cobrir.
- Q&A: extrair o padrão que a resposta ensina, como `decisao` ou `regra`, com a situação de quem perguntou em `condicoes`. Resposta que só serve àquele aluno fica de fora.
- Nada de completar com conhecimento externo: estado atual de plataforma, definição de livro, prática de mercado. Completar é sem-lastro.

### Vocabulário recorrente do curso

Termos que aparecem em muitas aulas e são definidos em uma só. As definições abaixo são as da fonte, com a aula de origem. Ao explicar um desses termos numa unidade, use esta definição ou a que a própria aula der. Termo que não está aqui e que a aula não define fica como está, sem explicação inventada.

- **CDF** — como os professores chamam os alunos. `M01_A01`: "a pessoa que é nerd por opção". `M01_A05`: os CDFs "alcançam o que eles querem". A fonte não desdobra a sigla.
- **figurante** — o oposto do CDF. `M01_A05`: quem está "só fazendo volume no sonho dos outros".
- **SOFIA** — `M01_A01`: "a nossa IA roteirista", a IA do curso para escrever roteiros.
- **Tutor CDF** — a outra IA do curso, que fica na plataforma das aulas (`M01_A01`).

## 4. Identidade e reconciliação

- `numero` nunca é renumerado nem reutilizado. [E] {presentes} ∪ {`retiradas`} = `1..max`, sem furo e sem repetição.
- Retirar = remover a unidade e listar o número em `retiradas`.
- Dividir ou fundir = retirar as originais e criar novas com números após o maior existente; a correspondência fica em `correcoes`.
- A ordem de apresentação é independente da identidade.

## 5. Hash e versão

`hash` da unidade = sha256 da serialização canônica de: `id`, `tipo`, `plataformas` (ordenadas), `tema`, `tarefas` (ordenadas), `fonte`, `inicio`, `fim`, `condicoes`, `perecivel`, `confianca`, corpo (linhas `strip`, espaços colapsados). `versao`, `nota`, `proposta_tag`, `titulo` e `evidencia` não entram.

A inspeção guarda o hash de cada unidade conferida. Unidade cujo hash mudou perde a evidência anterior; as intactas a preservam.

## 6. Derivados (`base_fcc.py --write`, conferidos por `--check`)

- `unidades/<AULA>.md` — uma página por aula: front matter (`type: unidades-aula`, `status`, `title`, `curso`, `modulo`, `ordem`, `aula`, `aula_id`, `account_id`, `fonte_repo`, `fonte_commit`, `fontes`, `fontes_ignoradas`, `extraido_em`, `gerado_por`, `retiradas`), `## Contexto da aula`, `## Unidades` com um bloco `### U:<aula_id>:<nnn> — <título>` + YAML + corpo por unidade. `fonte` aparece como `fala`, `txt:<arquivo>` ou `fala+txt:<arquivo>`; `faixa` como `hh:mm:ss–hh:mm:ss`.
- `status` da aula: `rascunho` (extraída e validada por script), `validado` (inspecionada com fonte), `revisado` (julgada e aprovada), `ouro` (referência do piloto aprovada).
- `unidades.jsonl` — uma linha por unidade viva: todos os campos da unidade + `id`, `aula`, `aula_id`, `modulo`, `ordem`, `aula_titulo`, `status_aula`, `hash`.
- `cobertura.jsonl` — uma linha por tarefa × plataforma da taxonomia, **inclusive as vazias**: `tarefa`, `plataforma`, `n_unidades`, `cobertura` (`presente` \| `ausente`), `aulas`, `ids`. `ausente` significa que o curso, no alcance extraído, não cobre aquela tarefa naquela plataforma. O agente consulta isso antes de responder; não preenche a lacuna sozinho. Presença em uma plataforma não prova cobertura nas outras.
- `temas/<tema>.md` e `tarefas/<tarefa>.md` — índices sem prosa nova, unidades agrupadas por tipo. Item sem unidade gera página dizendo "Nada nas fontes processadas".
- `README.md` — índice de aulas, temas e tarefas. `manifest.json` — inventário com hashes das fontes, commit de referência e `contrato_sha256`. `propostas_tags.md` — propostas agregadas.

## 7. Revisão (`processamento/base-consulta/revisao/`)

- `inspecao/<AULA>.json` (inspetor, com fonte): `arquivo_sha256` do JSON inspecionado, `alcance`, `unidades_verificadas`, `hashes_unidades`, veredito por unidade (`lastreada` \| `desvio` \| `sem-lastro` \| `faixa-errada`) com `gravidade`, `trecho_fonte` literal e explicação; `omissoes`; `perecibilidade`; `contrato`; `material`. O executor confere se cada `trecho_fonte` existe na fonte e lista os que não existem em `citacoes_nao_literais`.
- `julgamento/<AULA>.json` (juiz, sem fonte): `arquivo_sha256`, `inspecao_sha256`, `rodada`, `veredito` (`passa` \| `falha` \| `bloqueado`), `vetos`, parecer por área da rubrica, `falhas` consolidadas (ID, unidades, veto, evidência, impacto, mudança mínima, critério de aceite), `ajustes_menores`, `proximo`.
- `--reviews` rejeita inspeção ou julgamento cujo hash não bate com o JSON atual da aula.
- Cada chamada de modelo grava um `.execucao.json`: papel, modelo, esforço, via, início e fim, os quatro contadores de token, `stop_reason`, hash do pacote e do resultado. Execução registra a chamada; laudo registra o julgamento. Um não substitui o outro.

## 8. Adaptações em relação ao FORMATO do Curso Subido

1. **Fonte editável em JSON.** No Subido o Markdown era editado; aqui o JSON por aula é a fonte e o Markdown é derivado, como no adaptador `base_consulta.py`. Motivo: a saída do extrator é estruturada e o leitor é um agente.
2. **Âncora literal `evidencia`**, herdada do adaptador. Permite ao script provar que a faixa aponta para o trecho certo.
3. **Tipo `estrutura`** e troca de `alerta-ui` por `ferramenta`. O curso ensina moldes com partes fixas (AIDA, IHC, fichas de formato) que não são procedimento nem conceito; e o conteúdo perecível dele é ferramenta e equipamento, não interface de anúncio.
4. **Mínimo de 1 unidade por aula**, com aviso abaixo de 3. Há aula que é quase toda oferta comercial.
5. Playbooks, checklists, glossário, consolidação e voz ficam fora desta etapa.
