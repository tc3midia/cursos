---
type: formato
status: proposta
title: FORMATO — base atômica do Curso Subido de Tráfego v2
account_id: account.86ajrj8n9
promoted_by: human.will
versao: 1
---

# FORMATO

Contrato técnico da base atômica. `ferramentas/curso-subido/validate_unidades.py` implementa cada regra
marcada com **[E]** (erro) ou **[W]** (warning). O hash deste arquivo entra no `insumos_hash` de toda
visão, consolidação e laudo: mudar o FORMATO desatualiza os derivados de propósito.

## 1. Arquivo de unidades (`unidades/<slug>.md`)

Um arquivo por aula, 133 no total. `slug` = `<modulo 3 dígitos>-<slug do título da aula>`, igual ao
nome do memo v1 (a lib `unidades.py` deriva do `manifest.jsonl`; há uma tabela de exceções para os
slugs que a v1 encurtou).

### Front matter (YAML plano, `---` na primeira linha)

| campo | valor | regra |
|---|---|---|
| `type` | `unidades-aula` | [E] |
| `status` | `rascunho` \| `validado` \| `revisado` \| `ouro` | [E] |
| `title` | título da aula entre aspas, igual ao manifest | [E] |
| `modulo` | `"001"`…`"008"` | [E] igual ao manifest |
| `ordem` | inteiro do manifest | [E] |
| `aula_id` | 16 hex do manifest | [E] igual ao slug do arquivo |
| `account_id` | `account.86ajrj8n9` | [E] |
| `promoted_by` | `human.will` | [E] |
| `fonte_repo` | `tc3midia/curso-subido-trafego-transcricoes` | [E] |
| `fonte_commit` | `f188775` | [E] |
| `fontes` | lista: `transcricao.md` + nomes exatos de PDF/txt usados | [E] cada nome existe no disco da aula; todo PDF/txt no disco aparece (ou em `fontes_ignoradas` com motivo) |
| `fontes_ignoradas` | lista opcional `- nome.pdf: motivo` | [W] |
| `extraido_em` | `YYYY-MM-DD` | [E] |
| `gerado_por` | `sonnet-5` \| `opus-5` \| `fable-5.1` \| `gpt-5.6-sol` \| `gpt-5.6-terra` \| `gpt-6-astra` | [E] |
| `retiradas` | lista de `U:` retirados, pode ser `[]` | [E] |
| `divisoes` | lista `- "U:..:012 -> U:..:040, U:..:041"`, pode ser `[]` | [E] |
| `fusoes` | lista `- "U:..:007, U:..:009 -> U:..:041"`, pode ser `[]` | [E] |
| `nota` | texto livre opcional (correções manuais, ausência de PDF) | — |

### Corpo

```
# <título da aula>

## Contexto da aula
<3–8 linhas de prosa: o que a aula é, para quem, o que assume, o que deixa para depois>

## Unidades
<blocos>
```

[E] as duas seções existem nesta ordem; `Contexto da aula` tem 3–8 linhas não vazias; sem timestamp,
sem `[[`, sem "hoje"/"atualmente".

## 2. Bloco de unidade

````
### U:<aula_id>:<nnn> — <título ≤ 80 caracteres>
```yaml
tipo: regra
plataforma: [meta, google]
tema: criativo
tarefas: [coletar-referencias-de-anuncio]
fonte: fala
faixa: 00:11:52–00:13:10
condicoes: "verba < R$ 50/dia"
perecivel: false
confianca: alta
versao: 1
nota: "..."
proposta_tag: "..."
```
<corpo>
````

| campo | regra |
|---|---|
| ID | [E] `U:<16hex>:<3 dígitos>`; hex = `aula_id` do arquivo; único no arquivo e na base |
| título | [E] 1–80 caracteres após ` — ` (travessão com espaços) |
| `tipo` | [E] enum de `taxonomia.md ## Tipos` |
| `plataforma` | [E] lista com ≥1 valor do enum Plataformas |
| `tema` | [E] exatamente 1 valor do enum Temas |
| `tarefas` | [E] lista de valores do enum Tarefas; vazia `[]` só se `tipo` ∈ {`conceito`, `limite`} |
| `fonte` | [E] `fala` \| `pdf:<nome exato>` \| `txt:<nome exato>` \| `fala+pdf:<nome>` \| `fala+txt:<nome>`; o nome está em `fontes` |
| `faixa` | [E] obrigatória se `fonte` inclui `fala`; `hh:mm:ss–hh:mm:ss` (travessão `–` ou hífen); início < fim; fim ≤ `duracao_segundos` do manifest + 2 s; proibida se `fonte` é só pdf/txt |
| `condicoes` | opcional, string entre aspas; quando a orientação só vale sob condição |
| `perecivel` | [E] `true` \| `false`; `alerta-ui` ⇒ `true` |
| `confianca` | [E] `alta` \| `media` \| `baixa`; `baixa` ⇒ `nota` obrigatória |
| `versao` | [E] inteiro ≥ 1; incrementa em toda edição do corpo ou de metadado semântico (ver §4) |
| `nota` | opcional; obrigatória com `confianca: baixa` ou correção manual |
| `proposta_tag` | opcional; único caminho para tag nova: `"tema: <slug> — motivo"` ou `"tarefa: <slug> — motivo"` ou `"plataforma: ..."` |

### Corpo do bloco

- [E] 1–8 linhas não vazias; `procedimento` e `exemplo` até 15.
- [E] sem timestamp (`hh:mm`, `mm:ss`, `[00:`), sem `[[`, sem `**[`.
- [E] sem "hoje" / "atualmente" / "neste momento" (case-insensitive, palavra inteira).
- [E] sem cópia bruta: nenhuma sequência de 25 palavras idêntica à transcrição ou ao PDF.
- Prosa direta, no imperativo ou indicativo. Uma frase de razão é permitida ("porque…").
- Números e unidades como o professor diz; conversões entram entre parênteses.

### Regras por tipo

| tipo | regra [E] |
|---|---|
| `regra` | sem número obrigatório; frase categórica |
| `regua` | corpo contém ≥1 número ou unidade (`R$`, `%`, dias, x, vezes) |
| `procedimento` | corpo começa com `Pré-condição:` e tem lista numerada com ≥2 itens |
| `decisao` | corpo começa com `Se ` ou `Quando ` |
| `conceito` | `tarefas` pode ser `[]` |
| `exemplo` | corpo tem as três marcas `Situação:`, `O que aconteceu:`, `Lógica:` |
| `alerta-ui` | `perecivel: true` |
| `fato-material` | `fonte` começa com `pdf:` ou `txt:` |
| `limite` | `tarefas` pode ser `[]`; corpo diz o que a aula não cobre |

### Densidade

- [E] arquivo com < 3 unidades.
- [W] fora da faixa 3–60 unidades por aula; tarefa da taxonomia sem nenhuma unidade na base.

## 3. Identidade e reconciliação

- `nnn` é atribuído na primeira extração pela ordem de aparição na fonte e **nunca muda**.
- Ordem de apresentação e identidade são independentes: após correções o arquivo pode ter `:031`
  antes de `:012`. Nunca renumerar.
- [E] conjunto {presentes} ∪ {`retiradas`} = `001..max`, sem furos e sem repetição.
- Retirar = remover o bloco e listar o ID em `retiradas`. Número retirado nunca é reutilizado [E].
- Divisão: `U:..:012 -> U:..:040, U:..:041` em `divisoes`; o original vai para `retiradas`, os novos
  recebem números após o maior existente.
- Fusão: `U:..:007, U:..:009 -> U:..:041` em `fusoes`; os originais vão para `retiradas`.
- `ferramentas/curso-subido/reconciliar.py` aplica estas regras na reextração (etapa 1).

## 4. Hash e versão

`hash_unidade` = sha256 da serialização canônica de: `id`, `tipo`, `plataforma` (ordenada), `tema`,
`tarefas` (ordenadas), `fonte`, `faixa`, `condicoes`, `perecivel`, `confianca`, corpo (linhas
`strip`, espaços internos colapsados). `versao`, `nota` e `proposta_tag` **não** entram.

`build_indices.py` grava `hash` e `versao` em `_gerado/unidades.jsonl`. [E] se o hash de uma unidade
difere do JSONL commitado e `versao` não é maior que a registrada.

## 5. `_gerado/` (commitado, determinístico, `build_indices.py --check`)

- `unidades.jsonl` — uma linha por bloco vivo: `id, aula_id, slug, modulo, ordem, titulo, tipo,
  plataforma, tema, tarefas, fonte, faixa, condicoes, perecivel, confianca, versao, hash, grupo`
  (`grupo` = `G:` da consolidação ou `null`).
- `cobertura.jsonl` — uma linha por tarefa × plataforma da taxonomia: `n_unidades`, `ids`.
- `propostas_tags.md` — `proposta_tag` agregadas por texto, com IDs.
- `desatualizadas.md` — artefatos cujo `insumos_hash` não bate (ver §7). Vazio = só o cabeçalho.
- `visoes/temas/<tema>.md` — páginas de tema (ver §6.5).
- `indice.md` — índice de navegação.

## 6. Visões e consolidação

Front matter comum: `type`, `status`, `title`, `account_id`, `promoted_by`, `gerado_por`,
`insumos_hash`, `gerado_em`. Citação de unidade: `` `U:<16hex>:<nnn>` `` (regex
`U:[0-9a-f]{16}:\d{3}`). Citação de grupo: `` `G:<tema>:<nnn>` ``.

### 6.1 Playbook (`visoes/playbooks/<tarefa>.md`)

`type: playbook`, `tarefa: <slug>`, `plataformas: [...]`, opcional `parcial_ate: "005"` quando ainda
não cobre todos os módulos. Seções fixas, nesta ordem, todas presentes (vazia = "Nada nas fontes."):

1. `## Quando usar`
2. `## Pré-condições`
3. `## Passos por plataforma` (subseção `### <plataforma>` para cada plataforma esperada na matriz)
4. `## Réguas e critérios de pronto`
5. `## Decisões`
6. `## Não fazer`
7. `## O que o curso não cobre`
8. `## Sem resolução no curso`
9. `## Perecível`

[E] cada bullet (`- ` ou `1. `) das seções 1–6 e 9 termina com ≥1 citação `U:`. Zero prosa sem
lastro. Citação a ID retirado = erro. A unidade citada tem de sustentar a afirmação (juiz, veto
aplicabilidade).

### 6.2 Checklist (`visoes/checklists/<plataforma>.md`)

`type: checklist`, `plataforma`. Perguntas de auditoria em bullets; cada bullet cita ≥1 `U:` de tipo
`regua`, `regra`, `decisao` ou `alerta-ui`. `geral` entra em todas as checklists.

### 6.3 Glossário (`visoes/glossario.md`)

`type: glossario`. Um bullet por termo: `- **termo** — definição` + citação de `conceito`.

### 6.4 Órfãs (`visoes/orfas.md`)

`type: orfas`. Tabela `| id | motivo |` com motivo da lista fechada: `redundante com U:…` |
`anedota sem ação` | `perecível sem valor` | `fora do escopo do gestor`. Páginas de tema não contam
como citação. Meta: órfãs ≤ 15% das unidades com `tarefas` não vazia.

### 6.5 Página de tema (`visoes/temas/<tema>.md`)

Gerada por `build_indices.py`. Zero prosa nova. Estrutura: definição da taxonomia; unidades agrupadas
por tipo com corpo; temas relacionados por coocorrência de tarefa; playbooks que citam unidades do tema.

### 6.6 Consolidação (`consolidacao/<tema>.md`)

`type: consolidacao`, `tema`. Grupos:

````
### G:<tema>:<nnn> — <título>
```yaml
tipo: duplicata | conflito | complemento | condicional
unidades: [U:..., U:...]
canonica: U:...        # opcional; proibida em condicional; em conflito só com evidencia
evidencia: [U:...]     # unidades que sustentam a resolução
```
<resolucao: 1–6 linhas>
````

Regras que **não** existem: "PDF vence fala", "aula posterior vence anterior", "específica vence
geral". Conflito sem evidência fica sem canônica e o playbook expõe em "Sem resolução no curso".

## 7. `insumos_hash` e desatualização

`insumos_hash` = sha256 das linhas ordenadas `U:<id>\t<hash>` de cada unidade citada + `G:<id>\t<hash>`
de cada grupo citado + `FORMATO\t<sha256 de FORMATO.md>` + `TAXONOMIA\t<sha256 de taxonomia.md>`.
Laudo de aula (`aula_id` no front matter) cita implicitamente todas as unidades vivas do arquivo.
Só laudos vivos entram na checagem: rodadas arquivadas (`<nome>.rodada-N.md`) e laudos de fixtures
(`fixture-*.md`) são registro histórico e ficam fora de `desatualizadas.md`.

`validate_visoes.py --selar <arquivo>` recalcula e grava o campo. `validate_visoes.py
--desatualizadas` (também chamado por `build_indices.py`) escreve `_gerado/desatualizadas.md` com
`artefato | insumo | tipo de mudança` (`corpo`, `metadado`, `retirado`, `formato`). Gate de qualquer
etapa: `desatualizadas.md` vazio.

## 8. Laudo (`revisao/laudos/`)

- `<aula_id>.evidencia.md` (inspetor): tabela `| id | veredito | evidência |` com veredito
  `lastreada` \| `desvio` \| `sem-lastro` \| `faixa-errada`; seções `## Omissões`, `## Contrato`,
  `## Material`.
- `<aula_id>.md` (juiz): front matter `type: laudo`, `aula_id`, `arquivo`, `rodada`, `veredito:
  passa | falha | bloqueado`, `vetos: [ ... ]` (lista dos vetos que falharam, vazia se passa),
  `gerado_por`, `insumos_hash`; seções `## Fidelidade`, `## Cobertura`, `## Perecibilidade`,
  `## Contrato`, `## Falhas`, `## Próximo`.
- `playbook-<tarefa>.md` (juiz): igual, com `arquivo` e `## Aplicabilidade`.
- Fixture de calibração (`ferramentas/curso-subido/tests/calibracao/`): mesmo formato da unidade/playbook + front matter
  `type: fixture-calibracao`, `defeito`, `veredito_esperado`, `veto_esperado`. Laudo da fixture em
  `ferramentas/curso-subido/tests/calibracao/laudos/fixture-<nome>.md`.
