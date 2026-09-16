> Cópia preservada do plano original (revisão 2, 2026-09-13), escrito para o Jarvis 3.0. Os caminhos
> citados (`Conhecimento/Tráfego Pago/...`, `tools/curso_subido/`, `revisao-v2/`) são os da época.
> A execução vigente segue [o plano de sessões](../planos/2026-09-14-plano-de-sessoes.md); o mapa de
> caminhos está lá. A Etapa 0 deste spec foi concluída no Jarvis 3.0 (commit 719408a) e o CP1 foi
> aprovado em 2026-09-14. Origem: `~/.claude/plans/d-uma-olhada-no-bubbly-goose.md`.

# Curso Subido de Tráfego — reprocessamento como base atômica + visões geradas

Revisão 2 (2026-09-13): incorpora os cinco ajustes do feedback de revisão. O tratamento dado a cada
ponto está na seção final **Tratamento do feedback**.

## Contexto

O acervo atual em `Conhecimento/Tráfego Pago/Curso Subido de Tráfego/` (etapa 1, commits de 2026-09-09) tem
133 memos, um por aula, ~120k palavras, com 8 seções fixas e revisão inspetor/juiz em amostra de 8. Será
substituído porque espelha a ordem do curso, não a tarefa do gestor: um agente que vai montar uma campanha de
conversão no Meta precisa abrir ~10 memos; pixel aparece em 4 aulas sem fusão; metade do volume é walkthrough
narrativo; não há como carregar só o pedaço certo nem auditar uma conta contra as réguas. Os memos também não
têm `account_id`/responsável, como `Conhecimento/README.md` exige. Os prompts que geraram os módulos 4–8 nunca
foram commitados (só o `LEIA-ME.md`), então não há pipeline reproduzível para reaproveitar.

Fonte bruta: clone `/Users/wilianrafaelribeiro/curso-subido-trafego-transcricoes` (commit `f188775`,
somente leitura): 133 aulas em 8 módulos, ~490k palavras, 44h25, `transcricao.md` com parágrafos
`**[hh:mm:ss–hh:mm:ss]**`, 81 PDFs + 4 txt junto de cada aula, `manifest.jsonl` (id 16 hex = `aula_id`,
`duracao_segundos`, `saida_relativa`). `pdftotext` disponível em `/opt/homebrew/bin`.

Consumidor: agente gestor de tráfego que vai (a) operar contas de clientes da TC3, (b) auditar/diagnosticar
contas, (c) ser cérebro de skills/agentes futuros. Skill e agente ficam FORA deste trabalho.

## Decisões do Will (fechadas em 2026-09-13, não reabrir)

1. Forma: **base atômica + visões geradas**. Camada 1 = unidades pequenas por aula; camada 2 = páginas de
   tema (wiki), playbooks por tarefa, checklists de auditoria por plataforma, glossário.
2. Local: mesma pasta; memos e kit v1 vão para `historico/etapa-1/`; índice refeito.
3. Timestamp permitido nos metadados da unidade, nunca no texto que o agente lê.
4. Gate de qualidade: inspetor/juiz v2 calibrado em ouro novo, por amostra.
5. Reprocessar do zero a partir de transcrição + PDF; memos servem só como checklist de cobertura no gate.
6. Checkpoint do Will antes da leva: aprova taxonomia, formato, 2 ouros e 1 playbook piloto (CP1).
7. Exemplos do professor entram comprimidos como unidade `exemplo` (situação → o que aconteceu → lógica).
8. Dono: TC3 Media (`account_id: account.86ajrj8n9`, `promoted_by: human.will`).
9. Unidades guardadas **por aula** (verdade e auditoria); página por tema é visão gerada, não armazenamento.

## Layout

Durante a preparação (S0–S8) a v1 fica intacta: `README.md`, `_index.md`, `memos/`, `revisao/` e os 4 testes
v1 não são tocados. A v2 usa só caminhos novos, sem colisão. A troca acontece num único commit em S9.

```
BASE = Conhecimento/Tráfego Pago/Curso Subido de Tráfego/
  # v1 (intacta até S9)
  README.md  _index.md  memos/ (133)  revisao/ (rubrica, schema, amostra, papéis, 16 laudos)
  # v2 (caminhos novos durante a preparação)
  README-v2.md         contrato v2; vira README.md em S9
  FORMATO.md           schema do arquivo de unidades, do bloco, IDs, versão/hash, formato das visões
  taxonomia.md         ## Plataformas / ## Temas / ## Tarefas / ## Tipos — enums que o validador lê
  _index-v2.md         GERADO; vira _index.md em S9
  unidades/<slug>.md   1 por aula (133), mesmo slug dos memos atuais
  consolidacao/<tema>.md          grupos duplicata/conflito/complemento/condicional por tema
  visoes/temas/<tema>.md          GERADO por script (wiki de navegação; NÃO conta como citação para órfãs)
  visoes/playbooks/<tarefa>.md    1 por tarefa (subagente)
  visoes/checklists/<plataforma>.md
  visoes/glossario.md
  visoes/orfas.md                 unidades não citadas por playbook/checklist/glossário + motivo (lista fechada)
  _gerado/unidades.jsonl, cobertura.jsonl, desatualizadas.md, propostas_tags.md   GERADOS, commitados, --check
  revisao-v2/RUBRICA.md, amostra.md, papeis/{extrator,sintetizador,inspetor,juiz,redator}.md, laudos/
  revisao-v2/calibracao/          fixtures com defeitos conhecidos + vereditos esperados (nunca vão ao extrator)
  revisao-v2/avaliacao/casos.md, resultados-v1.md, resultados-v2.md   avaliação registrada de uso
  # depois de S9
  historico/etapa-1/   memos/, revisao/ v1, README.md, _index.md, MANIFEST.sha256
  revisao/             = revisao-v2 promovida
tools/curso_subido/    unidades.py (lib), validate_unidades.py, build_indices.py, pacote.py,
                       candidatos_consolidacao.py, validate_visoes.py, reconciliar.py   (stdlib only)
tests/                 test_curso_subido_v2_{taxonomia,unidades,indices,visoes,revisao,historico}.py
                       (v1: test_curso_subido_{modulo_005_memos,modulo_007_memos,revisao_laudos,revisao_kit}.py intactos até S9)
```

Scripts recebem `--root` (default: caminho final) e `--revisao` (default `revisao/`; durante a preparação
`revisao-v2/`). Rollback de S9: `git revert` do commit de migração (um commit, sem efeito fora do repo).

## Formato da unidade (resumo; detalhe completo vai em FORMATO.md)

Front matter do arquivo por aula: `type: unidades-aula`, `status: rascunho|validado|revisado|ouro`, `title`,
`modulo`, `ordem`, `aula_id`, `account_id: account.86ajrj8n9`, `promoted_by: human.will`, `fonte_repo`,
`fonte_commit: f188775`, `fontes: [transcricao.md, <pdf exatos>]`, `extraido_em`, `retiradas: []`,
`divisoes: []`, `fusoes: []` (registro de reconciliação, ver etapa 1).
Corpo: `## Contexto da aula` (3–8 linhas, prosa) e `## Unidades`.

Bloco:

```
### U:<aula_id>:<nnn> — <título ≤ 80>
```yaml
tipo: regra|regua|procedimento|decisao|conceito|exemplo|alerta-ui|fato-material|limite
plataforma: [meta, google]      # enum da taxonomia, ≥1
tema: criativo                  # 1
tarefas: [coletar-referencias-de-anuncio]   # vazio só se tipo ∈ {conceito, limite}
fonte: fala | pdf:<nome> | txt:<nome> | fala+pdf:<nome>
faixa: 00:11:52–00:13:10        # obrigatória se fonte inclui fala; dentro da duração do manifest
condicoes: "verba < R$ 50/dia"  # opcional; quando a orientação só vale sob condição
perecivel: false
confianca: alta|media|baixa     # baixa exige nota:
versao: 1                       # incrementa em toda edição de corpo ou metadado semântico
proposta_tag: "..."             # opcional, único caminho para tag nova
```
<corpo 1–8 linhas; procedimento/exemplo até 15; sem timestamp, sem [[ ]], sem "hoje/atualmente">
```

Regras por tipo: `alerta-ui` ⇒ `perecivel: true`; `fato-material` ⇒ fonte pdf/txt; `procedimento` ⇒
`Pré-condição:` + lista numerada ≥2; `decisao` ⇒ "Se "/"Quando "; `regua` ⇒ número ou unidade.

Identidade: `U:<aula_id>:<nnn>`. O número é atribuído na primeira extração pela ordem de aparição e **nunca
muda**; depois de correções, ordem de apresentação e identidade deixam de coincidir (o arquivo pode ter
`:031` antes de `:012`). Nunca renumerar; nunca reutilizar número retirado. `build_indices` grava no JSONL
`hash` = sha256 do corpo + metadados semânticos; `versao` muda junto com o hash (teste). Citação nas
visões: `` `U:<16hex>:<nnn>` `` (regex `U:[0-9a-f]{16}:\d{3}`).

## Taxonomia inicial (a aprovar no CP1)

- Plataformas (8): `geral, meta, google, google-search, youtube, google-display, ads-editor, tiktok`.
- Temas (19): fundamentos-e-carreira, conta-e-configuracao, pixel-e-eventos, atribuicao, leilao-e-lances,
  orcamento, objetivos, estrutura-de-campanha, nomenclatura, publicos, palavras-chave,
  posicionamentos-e-formatos, criativo, copy-e-roteiro, destino-e-landing-page, metricas-e-relatorios,
  otimizacao, testes-e-experimentos, escala.
- Tarefas (40), com plataformas cobertas pelo curso (matriz vira teste na etapa 3):
  - Fundação: configurar-conta; instalar-pixel-e-eventos; definir-conversoes-e-metas; configurar-janela-de-atribuicao
  - Planejamento: escolher-objetivo-de-campanha; definir-estrutura-de-campanha; nomear-campanhas; definir-orcamento; escolher-estrategia-de-lance
  - Segmentação: montar-publicos-personalizados; montar-publicos-semelhantes; definir-segmentacao-demografica-e-interesses; montar-lista-de-palavras-chave; definir-palavras-chave-negativas; organizar-hierarquia-e-exclusao-de-publicos; escolher-canais-e-posicionamentos
  - Criativo: coletar-referencias-de-anuncio; escrever-copy-e-roteiro; fazer-briefing-de-criativo; configurar-anuncio; usar-ia-para-anuncios
  - Execução: criar-campanha; replicar-campanhas-e-grupos; converter-campanha-entre-redes; operar-ads-editor; criar-campanha-de-catalogo; criar-campanha-de-formulario; criar-campanha-de-mensagem; criar-campanha-de-reconhecimento-ou-seguidores
  - Diagnóstico/otimização: diagnosticar-campanha-sem-gasto; diagnosticar-concentracao-de-verba; ler-metricas-e-relatorios; otimizar-lances; otimizar-publicos-e-segmentacoes; otimizar-anuncios; otimizar-estruturas; otimizar-palavras-chave; otimizar-landing-page; rodar-testes-e-experimentos; escalar-campanha
- Sem tarefa "auditar-conta": auditoria é visão (checklist) montada de regua/regra/decisao/alerta-ui.
- Tag nova: extrator usa a mais próxima + `proposta_tag`; `build_indices` agrega em `_gerado/propostas_tags.md`;
  triagem no fim de cada módulo; zero `proposta_tag` restante é condição para a etapa 3.

## Ciclo de correção (vale para todas as etapas a partir da 1)

1. Registrar a alteração: editar a unidade, incrementar `versao`; retirada = remover bloco + `retiradas:`.
2. `build_indices.py` recalcula hashes; `validate_visoes.py --desatualizadas` compara o `insumos_hash` de
   cada consolidação, visão e laudo com os hashes atuais das unidades/grupos que eles citam e escreve
   `_gerado/desatualizadas.md` (artefato, insumo mudado, tipo de mudança). Citação a ID retirado = **erro**.
3. Derivado desatualizado é regenerado (páginas de tema, índices) ou revisto por subagente (consolidação,
   playbook, checklist, glossário), que grava novo `insumos_hash`. Laudo desatualizado é refeito só quando o
   insumo mudou de conteúdo (não só de metadado de ordem).
4. Gate de qualquer etapa e aceite final: `desatualizadas.md` vazio; teste falha se não estiver.

`insumos_hash` = sha256 ordenado dos pares (id, hash) das unidades citadas + grupos citados + hash de
`FORMATO.md`/`taxonomia.md`. Gravado no front matter de consolidações, visões e laudos.

## Pipeline

### Etapa 0 — contrato, ferramentas, ouro, calibração (S0) → CP1
1. Escrever `taxonomia.md`, `FORMATO.md`, `README-v2.md`, `revisao-v2/RUBRICA.md`, 5 papéis v2.
2. Escrever `tools/curso_subido/{unidades,validate_unidades,build_indices,pacote}.py` e
   `tests/test_curso_subido_v2_{taxonomia,unidades,indices}.py` (TDD: fixture inline com bloco válido + 5
   inválidos; teste de hash/versão). Preflight: `pdftotext` presente; clone em `f188775`.
3. Ouros extraídos pelo modelo forte da sessão: `001-8-3` (regra/régua/PDF pesado) e
   `005-4-0-minha-campanha-esta-gastando-toda-verba...` (diagnóstico procedimental, sem PDF). `status: ouro`.
4. Playbook piloto `visoes/playbooks/diagnosticar-concentracao-de-verba.md` (marcado parcial até o módulo 005).
5. **Calibração negativa** em `revisao-v2/calibracao/`: 4 cópias do ouro 8.3 com defeito conhecido e
   veredito esperado (`número alterado` → falha fidelidade; `condição omitida` → falha fidelidade;
   `citação que não sustenta` no playbook piloto → falha aplicabilidade; `instrução perecível sem
   ressalva` → falha perecibilidade). Ficam fora de `unidades/` e nunca entram no pacote do extrator.
6. Inspetor v2 + juiz v2 nos 2 ouros, no piloto e nas 4 fixtures. Aceite: ouros e piloto `passa`; as 4
   fixtures reprovadas pelo veto certo. Reprovação de ouro: investigar se o erro está na extração, na
   evidência, no formato ou na rubrica; corrigir a causa, não afrouxar a régua.
7. **Avaliação de uso, recorte piloto**: escrever `revisao-v2/avaliacao/casos.md` (6 casos, ver etapa 3b)
   e rodar os 2 casos cobertos pelos ouros (diagnosticar concentração de verba; coletar referências) contra
   v1 (memos) e v2 (ouros + piloto), em contextos separados.
8. Gate 0: testes v1 e v2 verdes; laudos e fixtures conforme o esperado; piloto de avaliação registrado.
   **CP1 (Will): taxonomia, FORMATO, ouro 8.3, playbook piloto, resultado do piloto de avaliação.**
   Commit `conhecimento: contrato v2, taxonomia, ouros e calibração do Curso Subido`.

### Etapa 1 — extração por módulo (S1–S4)
- 1 subagente por aula, contexto fresco, pacote via `pacote.py extracao <aula_id>` (cabeçalho YAML
  pré-preenchido do manifest, transcrição, PDFs em texto, txt, taxonomia, FORMATO, papel do extrator,
  6 unidades do ouro como âncora de granularidade). Pacote vai para o scratchpad, nunca para o repo.
- Lotes de 6–8 em paralelo; após cada lote `validate_unidades.py --modulo`; erro ⇒ reexecuta a aula com a
  lista de erros (máx. 2), depois correção manual anotada em `nota:`.
- Fim de módulo: validador + `build_indices` + testes; triagem de `propostas_tags.md`; **revisão amostral
  do módulo**: inspetor + juiz em 1 aula escolhida por hash (2 no módulo 001). Regra de parada: qualquer
  `falha` em fidelidade ou cobertura ⇒ amostrar +2 aulas do módulo; 2 de 4 falhando ⇒ reextrair o módulo
  com o papel do extrator corrigido; caso contrário redator só nas falhas. `status: validado`; commit
  `conhecimento: unidades do módulo 00X do Curso Subido`.
- Reextração de módulo ou aula já extraída usa `reconciliar.py`: o extrator recebe a lista (ID, título,
  corpo) existente; preserva o ID quando é a mesma unidade, mesmo com texto corrigido (`versao`+1); novas
  unidades recebem números novos após o maior existente; unidades que somem vão para `retiradas`; divisão
  e fusão são registradas em `divisoes`/`fusoes` (`[U:..:012 → U:..:040, U:..:041]`). O validador exige
  que o conjunto presente ∪ retirados seja `001..max` sem furos.
- Ordem: 001 → **CP2 (Will: granularidade em 2 arquivos + os 2 laudos do módulo 001)** → 003 → 002 → 004
  → 006 → 007 → 005 → 008 → **CP3 (estatísticas por tipo/plataforma/tarefa, tarefas vazias, tags
  aceitas/recusadas, laudos amostrais por módulo).**

### Etapa 2 — consolidação (S5) → CP4
- `candidatos_consolidacao.py`: pares mesmo tema + mesmo tipo (ou regua×regra), Jaccard ≥ 0,45 ou mesmos números.
- 1 subagente por tema (19) escreve `consolidacao/<tema>.md` com grupos `G:<tema>:<nnn>`
  (`tipo: duplicata|conflito|complemento|condicional`, `unidades`, `canonica` (opcional), `resolucao`,
  `evidencia: [U:...]`, `insumos_hash`).
- Resolução apoiada em evidência, não em precedência automática. Antes de classificar como conflito,
  comparar plataforma, objetivo, `condicoes` e se há na fonte evidência explícita de correção ou atualização
  (ex.: o professor diz "o PDF está desatualizado" ou "mudei de opinião"). Casos:
  - mesma orientação em fontes diferentes → `duplicata`, canônica = a mais completa;
  - orientações que valem sob condições distintas → `condicional`, sem canônica, `resolucao` descreve as
    condições e cita as unidades;
  - correção explícita na fonte → `conflito` com canônica e `evidencia` apontando a unidade que corrige;
  - divergência sem evidência → `conflito` **sem canônica**; `resolucao` registra a divergência e o que
    se sabe; o playbook expõe as duas com fonte e marca `sem resolução no curso`.
  - Regras que NÃO existem: "PDF vence fala", "aula posterior vence anterior", "específica vence geral".
  - Nunca editar unidade na consolidação. Conflito que muda decisão operacional (lance, orçamento,
    estrutura) vai para **CP4** com as duas unidades e a evidência.
- Casos de calibração da consolidação (em `revisao-v2/calibracao/consolidacao.md`, com resultado
  esperado): fala corrige PDF; ordem das aulas não prova atualidade; duas recomendações válidas sob
  condições distintas.
- `validate_visoes.py --consolidacao`; `build_indices` preenche `grupo` no JSONL. Commit.

### Etapa 3 — visões (S6–S7) → CP5
- Playbooks: 1 subagente por tarefa (40), pacote = unidades da tarefa + grupos + `limite`s + playbook ouro.
  Seções fixas: Quando usar; Pré-condições; Passos por plataforma; Réguas e critérios de pronto; Decisões;
  Não fazer; O que o curso não cobre; Sem resolução no curso (conflitos abertos); Perecível. Cada bullet
  termina com ≥1 citação `U:`. Front matter com `insumos_hash`.
- Checklists: 1 subagente por plataforma (7; `geral` entra em todas): perguntas de auditoria citando IDs.
- Glossário: 1 subagente com todas as `conceito`.
- Páginas de tema: geradas por `build_indices.py` (título, definição da taxonomia, unidades agrupadas
  por tipo com corpo, temas relacionados por coocorrência, playbooks que citam). Zero prosa nova.
  **Não contam como citação** na análise de órfãs.
- `orfas.md`: `validate_visoes.py --orfas` lista unidades não citadas por playbook, checklist ou
  glossário; subagente escreve motivo da lista fechada (redundante com U:… | anedota sem ação | perecível
  sem valor | fora do escopo do gestor). Meta explícita: órfãs ≤ 15% das unidades com `tarefas` não vazia;
  acima disso, revisar playbooks antes de aceitar motivos.
- Gate 3: toda unidade citada ≥1 ou órfã com motivo; toda citação resolve para ID vivo; matriz
  tarefa×plataforma tem passos; `desatualizadas.md` vazio; `_index-v2.md` regenerado. Commit.

### Etapa 3b — avaliação de uso registrada (S7) → CP5
- `revisao-v2/avaliacao/casos.md`, escrito **antes** de rodar, com 6 casos simulados (sem conta real, sem
  skill): criar campanha de conversão no Meta; criar campanha na Rede de Pesquisa; diagnosticar
  concentração de verba no YouTube; auditar configuração de conjunto no Meta; conflito entre aulas
  (ex.: cota de referências); ausência de cobertura (ex.: Performance Max ou Advantage+ Shopping, que o
  curso não ensina; resposta correta = declarar insuficiência).
- Por caso: entrada; resultado esperado apoiado nas fontes (com IDs ou aulas); condições que precisam
  aparecer; recomendações indevidas que não podem aparecer; critério de aprovação (qualitativo, fechado
  antes da execução; sem meta percentual inventada).
- Execução: subagente avaliado com leitura restrita à base (v1: `memos/` + `_index.md`; v2: `visoes/` +
  `unidades/`), contextos separados, mesma pergunta. Registro em `resultados-v1.md` e `resultados-v2.md`:
  arquivos abertos, palavras lidas, decisões críticas certas/erradas, citações que sustentam a ação
  (conferidas pelo avaliador na fonte), condições preservadas, lacunas reconhecidas.
- Aceite: v2 acerta as decisões críticas e reconhece as lacunas dos casos 5 e 6; se v2 não demonstrar
  ganho sobre v1 em correção ou esforço de leitura, ajustar formato/playbooks antes de S8.
- **CP5 (Will: 2 playbooks, 1 checklist, 1 página de tema, tabela comparativa v1×v2).**

### Etapa 4 — revisão final em amostra (S8) → CP6
- `revisao-v2/amostra.md`: 2 ouros + 2 aulas por módulo escolhidas por hash (menor e maior `aula_id`),
  excluindo as já revisadas na etapa 1 = 18 arquivos; + 6 playbooks (1 por plataforma real, maior nº de
  citações) + 2 checklists (meta, google-search).
- Unidades: inspetor (contexto fresco, lê transcrição+PDF) → `laudos/<aula_id>.evidencia.md` (tabela por
  unidade: lastreada/desvio/sem-lastro/faixa-errada; omissões; contrato; PDFs) → juiz (outro contexto, sem
  transcrição) → `laudos/<aula_id>.md` com `insumos_hash`. Playbooks: juiz direto → `laudos/playbook-<tarefa>.md`.
- Rubrica v2, 5 vetos: contrato (script), fidelidade (nenhuma sem-lastro; desvio com confiança alta =
  falha; faixa errada > 10% = falha), cobertura (todo número e passo da fonte tem unidade; anedota não
  conta; memo v1 usado como checklist não é fonte de verdade), perecibilidade (tela sem `perecivel` =
  falha), aplicabilidade do playbook (pré-condição, passos por plataforma, ≥1 régua, "não cobre" e "sem
  resolução" preenchidos quando a matriz/consolidação mandam, passo cita tipo compatível e a unidade citada
  sustenta a afirmação). Sem nota numérica. Ouro que falha = `bloqueado`, nunca redator.
- Falha → redator v2 corrige só o listado (unidade sem lastro é retirada, não reescrita), `versao`+1,
  ciclo de correção roda (derivados desatualizados revistos), juiz de novo, máx. 2 rodadas. Regra de
  parada por módulo: 2 falhas de fidelidade/cobertura entre as aulas amostradas do módulo (etapa 1 + etapa
  4) ⇒ amostrar +2; 3 de 6 ⇒ reextrair o módulo.
- Gate 4: todos `passa`; `desatualizadas.md` vazio; `test_curso_subido_v2_revisao.py` verde.
  **CP6 (Will: laudos + mudanças do redator + derivados revistos).**

### Etapa 5 — migração (S9) → CP7
1. Antes de mover: `sha256sum` de todos os arquivos v1 (memos, revisao, README, _index) →
   `historico/etapa-1/MANIFEST.sha256`; suíte v1 verde.
2. `git mv memos revisao README.md _index.md → historico/etapa-1/`; `git mv README-v2.md README.md`;
   `git mv _index-v2.md _index.md`; `git mv revisao-v2 revisao`; `build_indices --check` limpo.
3. Testes: remover os 4 testes v1 e adicionar `test_curso_subido_v2_historico.py` (133 memos + 16 laudos
   no histórico; hashes batem com o MANIFEST; nenhum `transcricao.md`/`.pdf`/`.srt` dentro de BASE).
   Endurecer os testes v2: 133 arquivos em `unidades/`, 40 playbooks, 7 checklists, glossário, amostra e
   laudos presentes — **ausência de artefato obrigatório falha**; sem `skipUnless`.
4. Um único commit `conhecimento: migra Curso Subido para base atômica v2 e arquiva etapa 1`.
   Rollback = `git revert` desse commit. **CP7 (Will aprova o commit de migração).**

Regra de testes durante a preparação: cada teste v2 é adicionado no mesmo commit em que o artefato que ele
verifica passa a existir, com asserções sobre o que existe naquele ponto; as contagens totais entram só em S9.
Não há `skipUnless`.

## Scripts (stdlib, padrão `from tools.curso_subido import unidades`)

- `unidades.py`: `load_manifest`, `load_taxonomia`, `parse_arquivo_unidades`, `parse_bloco_yaml` (parser
  plano ~40 linhas, sem PyYAML), `iter_unidades`, `hash_unidade`, `find_citacoes`, `parse_grupos`,
  `insumos_hash`.
- `validate_unidades.py [--root] [--modulo|--arquivo] [--json]`: erros de front matter vs manifest, slug,
  PDFs em `fontes` vs disco, blocos (ID, conjunto presente ∪ retirados = `001..max`, YAML, enums, regras
  por tipo, faixa dentro da duração, corpo sem timestamp/`[[`/"hoje"), mínimo de unidades, IDs únicos,
  `versao` incrementada quando o hash muda vs JSONL commitado, nada bruto copiado. Warnings:
  `proposta_tag`, `confianca: baixa`, densidade fora de 3–60 por aula, tarefa sem unidade.
- `build_indices.py [--root] [--check]`: `_gerado/unidades.jsonl` (com `hash`), `cobertura.jsonl`,
  `propostas_tags.md`, `desatualizadas.md`, `visoes/temas/*.md`, índice; determinístico; `--check`
  compara com o disco (exit 1 se diferente).
- `pacote.py extracao|reextracao|tema|tarefa|plataforma|orfas`: monta contexto para subagente (stdout ou
  scratchpad); `reextracao` inclui IDs/títulos/corpos existentes.
- `reconciliar.py <arquivo antigo> <arquivo novo>`: confere preservação de IDs, numera novos, registra
  retiradas/divisões/fusões, recusa reutilização de número retirado.
- `candidatos_consolidacao.py`; `validate_visoes.py [--consolidacao|--orfas|--playbooks|--desatualizadas]`
  (citação a ID retirado = erro; páginas de tema não contam como citação).

Testes v2 (unittest): taxonomia (headings, slugs, 8 plataformas, 25–45 tarefas); unidades (validador
zero erros; parser round-trip; hash/versão); indices (`--check`; JSONL 1 linha por bloco; índice sem link
para `historico/`); visoes (validador; cobertura; matriz; `desatualizadas` vazio); revisao (papéis v2 com
"Não lê"; rubrica com 5 vetos; fixtures de calibração com veredito esperado; laudos com `veredito:`);
**ciclo de correção com fixtures**: (a) régua alterada mantendo ID ⇒ playbook que a cita aparece em
`desatualizadas`; (b) retirada de unidade citada ⇒ erro no validador de visões; (c) reextração com
divisão ⇒ IDs preservados, novos no fim, `divisoes` registrada, número retirado recusado; historico (S9).

## Modelos por papel (decisão do Will, 2026-09-13)

| Papel | Execuções | Modelo | Observação |
|---|---|---|---|
| Ouros, playbook piloto, fixtures de calibração, avaliador da avaliação de uso | ~10 | Fable 5.1 na sessão | Calibra o padrão |
| Extrator (1 por aula) | ~150 | Sonnet 5 | Opus 5 nas aulas > 8k palavras; se o CP2 mostrar falha de fidelidade causada pelo modelo, Opus em todas |
| Consolidação por tema | 19 | Opus 5 | |
| Sintetizador (playbooks, checklists, glossário, órfãs) | ~56 | Opus 5 | |
| Inspetor | ~30 | Sonnet 5 | |
| Juiz | ~40 | Fable 5.1 em subagente | Contexto fresco obrigatório |
| Redator | ~10 | Opus 5 | |
| Agente avaliado na avaliação de uso | 16 | Sonnet 5, igual para v1 e v2 | Comparação justa |

Haiku em nenhum papel. O modelo usado fica registrado no front matter de cada artefato gerado por
subagente (`gerado_por: sonnet-5 | opus-5 | fable-5.1`) e nos laudos.

## Volume e sessões

Entrada por extração 15–25k tokens (máx ~40k na 006-4.0); saída 3–10k. ~2.200–2.900 unidades esperadas.
Execuções de subagente: 133 extração + ~20 reexecuções + 19 consolidação + 48 visões + ~8 órfãs +
revisão amostral por módulo (9 inspetor + 9 juiz) + calibração (4+3) + avaliação de uso (2×2 piloto + 2×6
completa) + revisão final (18 inspetor + 26 juiz + ~8 redator) + revisão de derivados desatualizados (~10)
≈ 330. Juiz no modelo forte só nas amostras e fixtures. Sessões S0–S9 conforme etapas; cada sessão termina
com validador verde, `desatualizadas.md` vazio e commit; a seguinte começa com `build_indices --check` e
`git status` limpos.

## Riscos e mitigação

- Perda do "porquê": corpo admite uma frase de razão; `exemplo` comprimido; `Contexto da aula`; playbook cita 2–3 unidades por frase.
- Granularidade errada: âncora do ouro no pacote; warning de densidade; CP2 cedo no módulo 001 com laudos.
- Defeito propagado pela base: revisão amostral por módulo com regra de parada; calibração negativa prova que juiz reprova erro conhecido.
- Derivado velho com citação válida: hash por unidade + `insumos_hash` + `desatualizadas.md` no gate.
- Tags inconsistentes: enum fechado com erro duro; `proposta_tag` único caminho; teste da matriz tarefa×plataforma.
- UI perecível como atual: `alerta-ui` obrigatório em walkthrough; "hoje/atualmente" proibido; seção Perecível no playbook; nunca completar com Ads de 2026.
- Conflito "na canetada": sem precedência automática; evidência registrada; conflito sem evidência fica aberto e visível no playbook; operacional vai ao Will.
- Órfãs trivializadas: páginas de tema não contam; teto de 15% dispara revisão de playbooks.
- Subagente lendo memo antigo por atalho: pacote não contém memo; papel proíbe `memos/` e `historico/`; inspetor sinaliza frases idênticas.
- Quebra da v1 durante a preparação: caminhos v2 sem colisão; testes v1 intactos até S9; hashes no MANIFEST.
- Clone fora de `f188775`: preflight e aviso do validador.

## Verificação

- Preparação (S0–S8): `python3 -m unittest discover -s tests -p 'test_curso_subido_*.py'` (v1 e v2 verdes juntos).
- `python3 tools/curso_subido/validate_unidades.py` (zero erros); `python3 tools/curso_subido/build_indices.py --check`;
  `python3 tools/curso_subido/validate_visoes.py --playbooks --orfas --consolidacao --desatualizadas`.
- Calibração: 2 ouros + piloto `passa`; 4 fixtures reprovadas pelo veto esperado; 3 casos de consolidação com o resultado esperado.
- Avaliação de uso: `revisao-v2/avaliacao/resultados-v2.md` com os 6 casos aprovados pelos critérios fechados antes da execução e comparação com v1.
- Laudos da amostra final todos `veredito: passa`; `desatualizadas.md` vazio.
- S9: MANIFEST.sha256 confere; suíte v2 endurecida verde; `git revert` do commit de migração restaura a v1 (testado uma vez num worktree).
- Baseline hoje: 21 testes v1 passam.

## Tratamento do feedback

1. **Preservar v1**: caminhos v2 sem colisão (`README-v2.md`, `_index-v2.md`, `revisao-v2/`), scripts com
   `--root`/`--revisao`, testes v1 intactos até S9, suíte v2 separada, MANIFEST.sha256, migração + troca de
   testes num commit, rollback por revert, sem `skipUnless`. Seções Layout, Etapa 0, Etapa 5, Scripts, Riscos, Verificação.
2. **Correções invalidam derivados / identidade**: `versao` + hash por unidade, `insumos_hash` em
   consolidações, visões e laudos, `desatualizadas.md` como gate, `reconciliar.py` com
   `retiradas/divisoes/fusoes`, ordem ≠ identidade, citação a retirado = erro, três testes com fixtures.
   Implementado com hash de insumos em vez de grafo de dependências completo (mesmo efeito, menos código).
3. **Precedência**: removidas as regras automáticas; resolução por plataforma, objetivo, `condicoes` e
   evidência explícita; tipo `condicional`; conflito sem evidência fica aberto e o playbook o expõe em
   "Sem resolução no curso"; casos de calibração da consolidação; CP4 mantido.
4. **Calibração negativa e revisão antecipada**: 4 fixtures com veredito esperado; ouro reprovado gera
   investigação de causa; inspetor/juiz em 2 aulas do módulo 001 no CP2 e 1 por módulo depois; regra de
   parada redefinida (2 de 4, depois 3 de 6); estimativas recalculadas (~330 execuções).
5. **Avaliação de uso registrada**: `avaliacao/casos.md` com 6 casos e critérios fechados antes de rodar,
   recorte piloto no CP1 e bateria completa no CP5, comparação v1×v2 em contextos separados, lacunas como
   resposta correta, páginas de tema fora da contagem de órfãs com teto de 15%.
