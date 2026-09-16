# Curso Subido: base atômica no Jarvis 4, plano de sessões

> **Para agentes executores:** use superpowers:executing-plans (ou subagent-driven-development) para executar este plano sessão por sessão. Os passos usam checkbox (`- [ ]`). Cada sessão termina com os gates verdes e um commit; a próxima começa lendo `tarefas.md` da frente.

**Objetivo:** transformar as 133 aulas do Curso Subido de Tráfego em uma base atômica de unidades por aula, com consolidação por tema e visões geradas (playbooks por tarefa, checklists por plataforma, glossário), vivendo em `biblioteca/curso-subido-trafego/` do Jarvis 4, com ferramentas e testes em `ferramentas/curso-subido/`.

**Arquitetura:** camada 1 são unidades pequenas por aula (verdade e auditoria, com ID fixo, hash e versão). Camada 2 são visões que só existem por citação de unidades; toda frase termina com `U:…`. Um `insumos_hash` em cada derivado e o arquivo `_gerado/desatualizadas.md` garantem que unidade editada invalida quem a cita. A revisão usa inspetor (lê fonte) e juiz (nunca lê fonte) com cinco vetos e sem nota numérica.

**Stack:** Python 3 stdlib (sem PyYAML), `pdftotext` em `/opt/homebrew/bin`, `unittest`, git. Subagentes via ferramenta Agent do Claude Code (`model: sonnet | opus | fable`).

**Spec:** [2026-09-13-spec-base-atomica.md](../specs/2026-09-13-spec-base-atomica.md) (plano original, revisão 2, com os caminhos do Jarvis 3.0). Os contratos vivos são `FORMATO.md`, `taxonomia.md` e `revisao/RUBRICA.md` na biblioteca, depois da Sessão 1.

**Estado de partida (2026-09-14):** Etapa 0 do spec concluída no Jarvis 3.0, branch `task/curso-subido-v2-etapa-0`, commit `719408a`. CP1 aprovado por Will em 2026-09-14 com as decisões registradas em 2026-09-14-curso-subido-base-atomica.md (registro no Jarvis 4: `projetos/tc3/decisoes/2026-09-14-curso-subido-base-atomica.md`). Dois ouros extraídos (001-8-3 com 43 unidades, 005-4-0 com 17), playbook piloto, 4 fixtures, avaliação de uso piloto, 58 testes v2 verdes.

## Restrições globais

**Rota Codex aprovada para piloto em 14/09/2026:** seguir a [proposta de adaptação, revisão 2](../specs/2026-09-14-spec-tecnica-processamento-codex.md). Comparar Sol e Terra como extratores nas duas aulas escolhidas; Terra inspeciona, Astra julga, Sol corrige. Esforço médio em Sol/Terra e alto no juiz. Essa matriz substitui as referências Claude abaixo somente no piloto Codex, em cópias temporárias. A sessão 5 e a escolha definitiva continuam dependentes do resultado registrado em `tarefas.md`. Cada subagente começa sem histórico herdado e escreve somente na saída atribuída.

**Decisão posterior ao piloto, 14/09/2026:** Will confirmou o uso de três modelos com funções diferentes. Para o próximo módulo, 002, a rota Codex passa a ser Terra na extração/reextração e inspeção (contextos separados), Sol na correção de conteúdo e Astra no julgamento da amostra; scripts nas verificações mecânicas. Esforço médio em Terra/Sol e alto em Astra. Esta decisão substitui a restrição ao piloto do parágrafo anterior e os modelos Claude dos prompts abaixo para a execução Codex do módulo 002. A inspeção deve cobrir números, condições e preferências com evidências suficientes. Permanecem a divisão em sessões 5 e 6, os critérios do Procedimento E e suas regras de amostragem e parada. Resultado e prontidão em tarefas.md (registro no Jarvis 4: `projetos/tc3/frentes/curso-subido-base-atomica/tarefas.md`).

**Fechamento antecipado em 15/09/2026:** depois da sessão 5, Will pediu fechar correções e pendências antes da próxima etapa. Antecipar a triagem e a revisão amostral de E6/E7 sobre as 18 aulas já existentes do módulo 002, usando a rota Codex acima. A sessão 5b registra esse trabalho. Preservar critérios, evidências e expansão da amostra; corrigir apenas os arquivos existentes. A segunda metade fica para depois. Essa revisão parcial não aciona E8 nem marca o módulo como fechado.

**Sessão 5b concluída em 15/09/2026:** quatro candidatos corrigidos e aprovados, 5.0/6.0 passaram na única expansão focal. Will autorizou uma conferência adicional de dois ajustes da 6.1 após a parada; passou, sem reiniciar contador. Quatro laudos selados, zero erros, 80 testes. O 002 tem 18 aulas/431 unidades; as outras 18 são a sessão 6, liberada. Nenhuma reextração nesta retomada. [Resultado e limites](../2026-09-15-fechamento-primeiras-18.md). Preservar a revisão realizada; não repetir chamadas por mudança de sessão sem alteração de insumos ou motivo material.

**Histórico da sessão 5b, antes da decisão abaixo:** quatro aulas reprovaram na revisão inicial; duas foram reextraídas e corrigidas e chegaram à terceira reprovação. Candidatos de 54 e 32 unidades ficaram temporários, sem promoção. A regra então vigente exigia reextração do lote e bloqueio por rodada. Essa obrigação foi revogada por Will; o [relatório anterior](../2026-09-15-fechamento-pendencias-sessao-05.md) preserva os resultados e o consumo.

**Decisão vigente de Will, 15/09/2026:** qualidade com correção localizada e retrabalho proporcional, conforme a [regra de qualidade e retrabalho](../2026-09-15-regra-qualidade-e-retrabalho.md). Cancelada a obrigação de reextrair as outras 16 aulas. Aplicar E7 e RUBRICA atualizados: falhas materiais recebem correção pontual; detalhes complementares ficam registrados; divergências de avaliação são resolvidas com evidência e impacto. Reaproveitar candidatos e provas existentes na triagem das quatro aulas apontadas. Laudos anteriores permanecem históricos, sem aprovação automática. As outras 18 aulas do módulo continuam sendo a segunda metade ainda não extraída.
- Nenhum `.pdf`, `.srt` ou `transcricao.md` entra na biblioteca. Fonte bruta é o clone `~/curso-subido-trafego-transcricoes` no commit `f188775`, somente leitura. Variável `CURSO_SUBIDO_CLONE` sobrescreve o caminho.
- Timestamps só em `faixa` nos metadados. Corpo sem timestamp, sem `[[`, sem "hoje/atualmente/neste momento", sem 25 palavras copiadas da fonte.
- IDs `U:<aula_id>:<nnn>` nunca renumerados nem reutilizados. Retiradas, divisões e fusões vão no front matter. Presentes ∪ retirados = `001..max`.
- `versao` sobe toda vez que o hash da unidade muda. `desatualizadas.md` vazio é gate de toda sessão.
- Enums fechados em `taxonomia.md`. Tag nova só por `proposta_tag`.
- Haiku em nenhum papel. `gerado_por` em todo artefato gerado por modelo.
- Juiz nunca lê transcrição, PDF, clone, memos ou outros laudos. Se leu, o laudo é inválido.
- Pacotes de subagente nunca entram no git: vão para `_saida/tc3/2026-09-14-curso-subido-base-atomica/temporarios/`, que o `.gitignore` do Jarvis 4 exclui.
- Sem `skipUnless` nos testes. Ausência de artefato obrigatório falha.
- Memos v1 ficam no Jarvis 3.0. Nenhum papel lê memos. Só a avaliação de uso lê memos, e só no lado v1.
- Sem travessões e sem diminutivos nos textos novos (voz do Will).
- Nunca atravessar um checkpoint (CP) sem a decisão do Will registrada em `tarefas.md`.

## Como usar este plano

**Início de toda sessão:**

```bash
J4="/Users/wilianrafaelribeiro/Jarvis 4"; cd "$J4"
git status --short -- biblioteca/curso-subido-trafego ferramentas/curso-subido projetos/tc3/frentes/curso-subido-base-atomica
git -C ~/curso-subido-trafego-transcricoes rev-parse --short=7 HEAD     # f188775
python3 ferramentas/curso-subido/build_indices.py --check
python3 ferramentas/curso-subido/validate_visoes.py --desatualizadas
python3 -m unittest discover -s ferramentas/curso-subido/tests -p 'test_curso_subido_*.py'
```

Os quatro comandos precisam estar limpos (a partir da Sessão 1). Ler `tarefas.md` da frente para saber qual sessão é a próxima e se há decisão de checkpoint pendente. Outras alterações não commitadas no Jarvis 4 (trabalho de outras frentes) não são desta frente: não tocar, não commitar.

**Fim de toda sessão:**

1. Gates da sessão verdes (validador, `--check`, `desatualizadas.md` vazio, testes).
2. Commit só dos caminhos desta frente, mensagem indicada na sessão, terminando com `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>` (ou o modelo real da conversa, ver "Modelos por papel").
3. Atualizar `tarefas.md` (linha da sessão: feita, data, commit, pendências) e `biblioteca/curso-subido-trafego/historico.md` (uma entrada por sessão: data, operação, arquivos, lacunas).
4. Se a sessão termina num checkpoint, escrever em `tarefas.md` o que Will precisa decidir e parar.

**Se sobrar contexto numa sessão:** encadear a próxima sessão até o checkpoint seguinte. Nunca pular um checkpoint.

**Subagentes:** ferramenta Agent, `subagent_type: general-purpose`, `run_in_background: true`, vários na mesma mensagem quando são independentes. O prompt de cada papel está neste plano; o papel completo está em `biblioteca/curso-subido-trafego/revisao/papeis/`.

**Modelos por papel:**

| Papel | Quem executa | Modelo | Esforço de raciocínio |
|---|---|---|---|
| Sessão (orquestra agentes, roda gates, triagem de `proposta_tag`, correção manual depois de 2 reexecuções, avaliador da Sessão 15) | a própria conversa | Fable 5.1 | o da conversa |
| Extrator e reextração | Agent | `opus` em todas as aulas até o CP2 (decisão de Will, 2026-09-14); no CP2 Will decide se passa a `sonnet` com a regra das 8.000 palavras | padrão do agente |
| Inspetor | Agent | `sonnet` | padrão do agente |
| Juiz | Agent, contexto fresco | `fable` | padrão do agente |
| Redator, consolidador, sintetizador (playbooks, checklists, glossário, órfãs) | Agent | `opus` | padrão do agente |
| Respondentes da avaliação de uso (v1 e v2) | Agent | `sonnet` | padrão do agente |

Regras:

- **Contagem das 8.000 palavras** (vale só se o CP2 trouxer o Sonnet de volta; até lá o extrator é Opus em todas as aulas e a contagem fica anotada como informação): conta só a parte da aula no pacote (transcrição e PDFs em texto), não o pacote inteiro. A parte fixa (papel, FORMATO, taxonomia, âncora do ouro) soma cerca de 3.800 palavras e é igual para todas. Medição de 2026-09-14 sobre as 133 aulas: pelo pacote inteiro, 60 aulas iriam para Opus; pela parte da aula, 11. `pacote.py extracao` imprime as duas contagens a partir da Sessão 2.
- **Sessão fora do Fable:** se a conversa rodar em outro modelo, registrar em `tarefas.md` na linha da sessão, usar esse modelo no `gerado_por` das correções manuais e no `Co-Authored-By` do commit. O papel do juiz continua `fable` de qualquer forma.
- **Correção manual** feita pela sessão (depois de 2 reexecuções) leva `nota:` explicando e mantém o `gerado_por` do extrator no front matter; a unidade corrigida sobe `versao`.
- **Esforço de raciocínio:** a ferramenta Agent não recebe esforço por chamada; ele só pode ser fixado numa definição de agente (`.claude/agents/<papel>.md`, frontmatter). Até o CP2 todos os papéis usam o padrão. No CP2, se as falhas amostrais forem de fidelidade ou cobertura e vierem do modelo, Will escolhe entre subir o extrator para Opus ou criar definições de agente com esforço alto para extrator e juiz.
- Haiku em nenhum papel.

**Caminhos usados nas sessões:**

```bash
J3="/Users/wilianrafaelribeiro/Jarvis 3.0"
J4="/Users/wilianrafaelribeiro/Jarvis 4"
B3="$J3/Conhecimento/Tráfego Pago/Curso Subido de Tráfego"      # v1 + v2 no Jarvis 3.0 (só leitura depois da Sessão 1)
B4="$J4/biblioteca/curso-subido-trafego"                          # biblioteca no Jarvis 4
T4="$J4/ferramentas/curso-subido"                                 # ferramenta + testes
S4="$J4/_saida/tc3/2026-09-14-curso-subido-base-atomica/temporarios"   # pacotes e rascunhos, fora do git
FR="$J4/projetos/tc3/frentes/curso-subido-base-atomica"           # esta frente
```

## Mapa de caminhos (Jarvis 3.0 para Jarvis 4)

| Jarvis 3.0 | Jarvis 4 |
|---|---|
| `$B3/taxonomia.md`, `FORMATO.md` | `$B4/taxonomia.md`, `FORMATO.md` |
| `$B3/README-v2.md` | `$B4/README.md` (reescrito como índice) |
| `$B3/_index-v2.md` | `$B4/indice.md` (gerado) |
| `$B3/unidades/`, `visoes/`, `_gerado/` | `$B4/unidades/`, `visoes/`, `_gerado/` |
| `$B3/consolidacao/` (vazia) | `$B4/consolidacao/` (criada na sessão de consolidação) |
| `$B3/revisao-v2/{README,RUBRICA,amostra}.md`, `papeis/`, `avaliacao/` | `$B4/revisao/…` |
| `$B3/revisao-v2/laudos/<vivos>` | `$B4/revisao/laudos/` |
| `$B3/revisao-v2/laudos/*.rodada-N.md` | não vai; fica na branch do 3.0 |
| `$B3/revisao-v2/calibracao/` e `laudos/fixture-*` | `$T4/tests/calibracao/` e `tests/calibracao/laudos/` |
| `$J3/tools/curso_subido/*.py` | `$T4/*.py` |
| `$J3/tests/test_curso_subido_v2_*.py` | `$T4/tests/` |
| `$B3/memos/`, `revisao/`, `README.md`, `_index.md` (v1) | ficam no 3.0; `$B4/fontes.md` aponta |
| scratchpad de pacotes | `$S4` |

Sessões: 1 promoção, 2 ferramentas da leva, 3 a 11 extração (com CP2 e CP3), 12 consolidação (CP4), 13 e 14 visões, 15 avaliação de uso (CP5), 16 revisão final (CP6), 17 fecho (CP7).

---

### Sessão 1: promoção para o Jarvis 4

**Arquivos:**
- Criar: `$B4/{README.md,fontes.md,historico.md,taxonomia.md,FORMATO.md,indice.md}`, `$B4/unidades/`, `$B4/visoes/`, `$B4/_gerado/`, `$B4/revisao/`
- Criar: `$T4/README.md`, `$T4/{unidades,validate_unidades,build_indices,validate_visoes,pacote}.py`, `$T4/tests/test_curso_subido_v2_*.py`, `$T4/tests/slugs-v1.txt`, `$T4/tests/calibracao/`
- Modificar: `$J4/biblioteca/README.md`, `$J4/ferramentas/README.md`, `$FR/tarefas.md`

**Interfaces:**
- Produz: `unidades.BASE_DEFAULT = ROOT / "biblioteca" / "curso-subido-trafego"`, `ROOT` = raiz do Jarvis 4, `build_indices.INDICE_NOME = "indice.md"`, default `--revisao revisao` em todos os scripts, `pacote.py --saida` aceitando `_saida/**/temporarios/`. Tudo que vem depois usa isso.

- [ ] **Passo 1: preflight nos dois repos**

```bash
git -C "$J3" status --short -- Conhecimento tools tests        # vazio
git -C "$J3" log --oneline -1 task/curso-subido-v2-etapa-0      # 719408a
cd "$J4" && git checkout -b task/curso-subido-base-atomica
```

- [ ] **Passo 2: copiar conhecimento, ferramenta e testes**

```bash
mkdir -p "$B4/revisao/laudos" "$T4/tests/calibracao/laudos" "$S4"
cp "$B3/FORMATO.md" "$B3/taxonomia.md" "$B4/"
cp -R "$B3/unidades" "$B3/visoes" "$B3/_gerado" "$B4/"
cp "$B3/revisao-v2/README.md" "$B3/revisao-v2/RUBRICA.md" "$B3/revisao-v2/amostra.md" "$B4/revisao/"
cp -R "$B3/revisao-v2/papeis" "$B3/revisao-v2/avaliacao" "$B4/revisao/"
for f in "$B3"/revisao-v2/laudos/*.md; do case "$(basename "$f")" in *.rodada-*|fixture-*) ;; *) cp "$f" "$B4/revisao/laudos/";; esac; done
cp "$B3"/revisao-v2/calibracao/README.md "$B3"/revisao-v2/calibracao/esperado.jsonl "$B3"/revisao-v2/calibracao/f?.md "$T4/tests/calibracao/"
cp "$B3"/revisao-v2/laudos/fixture-* "$T4/tests/calibracao/laudos/"
cp "$J3"/tools/curso_subido/unidades.py "$J3"/tools/curso_subido/validate_unidades.py "$J3"/tools/curso_subido/build_indices.py "$J3"/tools/curso_subido/validate_visoes.py "$J3"/tools/curso_subido/pacote.py "$T4/"
cp "$J3"/tests/test_curso_subido_v2_*.py "$T4/tests/"
ls "$B3/memos" | sed 's/\.md$//' | sort > "$T4/tests/slugs-v1.txt"      # 133 linhas
rm -f "$B4/_gerado/selos.jsonl"      # será refeito pelo --selar com os caminhos novos
ls "$B4/revisao/laudos"              # 5 arquivos: 2 laudos + 2 evidências dos ouros, 1 laudo do playbook
```

Não copiar `README-v2.md`, `_index-v2.md` (gerado), `memos/`, `revisao/` v1, `README.md` v1, `_index.md` v1, rodadas arquivadas.

- [ ] **Passo 3: adaptar imports e caminhos nos scripts**

Nos cinco `.py` de `$T4`:

```bash
cd "$T4"
sed -i '' 's|sys.path.insert(0, str(Path(__file__).resolve().parents\[2\]))|sys.path.insert(0, str(Path(__file__).resolve().parent))|' *.py
sed -i '' -E 's|from tools\.curso_subido import ([a-z_]+) as ([a-z_]+)|import \1 as \2|; s|from tools\.curso_subido import ([a-z_]+)$|import \1|' *.py
sed -i '' 's|BASE_DEFAULT = ROOT / "Conhecimento" / "Tráfego Pago" / "Curso Subido de Tráfego"|BASE_DEFAULT = ROOT / "biblioteca" / "curso-subido-trafego"|' unidades.py
sed -i '' 's|default="revisao-v2"|default="revisao"|; s|revisao: str = "revisao-v2"|revisao: str = "revisao"|' *.py
sed -i '' 's|INDICE_NOME = "_index-v2.md"|INDICE_NOME = "indice.md"|; s|Contrato: `README-v2.md`|Contrato: `README.md`|' build_indices.py
sed -i '' 's|tools/curso_subido/|ferramentas/curso-subido/|g' *.py
grep -n 'tools.curso_subido\|revisao-v2\|Conhecimento' *.py      # nada
```

`ROOT = Path(__file__).resolve().parents[2]` em `unidades.py` continua certo: `ferramentas/curso-subido/unidades.py` sobe para a raiz do Jarvis 4.

Em `pacote.py`, trocar a recusa de `--saida` dentro do repo por esta regra (pacote pode ir para `_saida/**/temporarios/`):

```python
    if args.saida:
        saida = Path(args.saida).resolve()
        dentro = lib.ROOT.resolve() in saida.parents or saida == lib.ROOT.resolve()
        if dentro and "temporarios" not in saida.relative_to(lib.ROOT.resolve()).parts:
            raise SystemExit("pacote dentro do repositório só em _saida/<negocio>/<trabalho>/temporarios/")
        saida.mkdir(parents=True, exist_ok=True)
```

- [ ] **Passo 4: adaptar os testes**

Em todos os `$T4/tests/test_curso_subido_v2_*.py`, o cabeçalho passa a ser:

```python
ROOT = Path(__file__).resolve().parents[3]          # raiz do Jarvis 4
FERRAMENTA = Path(__file__).resolve().parents[1]    # ferramentas/curso-subido
sys.path.insert(0, str(FERRAMENTA))
```

```bash
cd "$T4/tests"
sed -i '' 's|ROOT = Path(__file__).resolve().parents\[1\]|ROOT = Path(__file__).resolve().parents[3]\nFERRAMENTA = Path(__file__).resolve().parents[1]|' test_curso_subido_v2_*.py
sed -i '' 's|sys.path.insert(0, str(ROOT))|sys.path.insert(0, str(FERRAMENTA))|' test_curso_subido_v2_*.py
sed -i '' -E 's|from tools\.curso_subido import ([a-z_]+) as ([a-z_]+)|import \1 as \2|' test_curso_subido_v2_*.py
sed -i '' 's|BASE = ROOT / "Conhecimento" / "Tráfego Pago" / "Curso Subido de Tráfego"|BASE = ROOT / "biblioteca" / "curso-subido-trafego"|' test_curso_subido_v2_*.py
sed -i '' 's|REV = BASE / "revisao-v2"|REV = BASE / "revisao"\nCALIB = FERRAMENTA / "tests" / "calibracao"|' test_curso_subido_v2_revisao.py
sed -i '' 's|revisao="revisao-v2"|revisao="revisao"|g' test_curso_subido_v2_*.py
sed -i '' 's|"README-v2.md"|"README.md"|' test_curso_subido_v2_revisao.py
```

Edições manuais:

1. `test_curso_subido_v2_revisao.py`: em `CalibracaoTest`, trocar `REV / "calibracao"` por `CALIB` (três ocorrências) e `REV / "laudos" / f"fixture-{f}.md"` por `CALIB / "laudos" / f"fixture-{f}.md"`.
2. `test_curso_subido_v2_unidades.py`: substituir `test_slug_de_todas_as_aulas_bate_com_memos_v1` por:

```python
    def test_slug_de_todas_as_aulas_bate_com_a_lista_v1(self):
        manifest = lib.load_manifest()
        self.assertEqual(len(manifest), 133)
        esperados = set((FERRAMENTA / "tests" / "slugs-v1.txt").read_text(encoding="utf-8").split())
        self.assertEqual({row["slug"] for row in manifest.values()}, esperados)
```

3. `test_curso_subido_v2_indices.py`: onde o teste abre `_index-v2.md`, trocar por `indice.md`.
4. `test_curso_subido_v2_visoes.py`: o `copytree` ignora `("memos", "revisao", "historico")`; trocar por `("historico",)` para a cópia temporária levar `revisao/` (os laudos vivos entram no ciclo de desatualização).

- [ ] **Passo 5: adaptar os textos**

```bash
cd "$B4"
grep -rl -E 'revisao-v2|tools/curso_subido|README-v2|_index-v2|Conhecimento/Tráfego' --include='*.md' . "$T4/tests/calibracao"
sed -i '' 's|revisao-v2/|revisao/|g; s|`revisao-v2`|`revisao`|g; s|tools/curso_subido/|ferramentas/curso-subido/|g; s|README-v2\.md|README.md|g; s|_index-v2\.md|indice.md|g' FORMATO.md taxonomia.md revisao/*.md revisao/papeis/*.md revisao/avaliacao/*.md revisao/laudos/*.md "$T4"/tests/calibracao/*.md "$T4"/tests/calibracao/laudos/*.md
sed -i '' "s|python3 -m unittest discover -s tests -p 'test_curso_subido_\*.py'|python3 -m unittest discover -s ferramentas/curso-subido/tests -p 'test_curso_subido_*.py'|" FORMATO.md
```

Depois, à mão:

1. `revisao/papeis/juiz.md`, seção Escreve: laudo de fixture vai em `ferramentas/curso-subido/tests/calibracao/laudos/fixture-<nome>.md`.
2. `revisao/amostra.md`: caminhos `calibracao/fN.md` viram `ferramentas/curso-subido/tests/calibracao/fN.md`; laudos `laudos/fixture-fN.md` viram `ferramentas/curso-subido/tests/calibracao/laudos/fixture-fN.md`. Acrescentar a linha: "CP1 aprovado por Will em 2026-09-14; o tratamento da rodada 3 do piloto foi ratificado."
3. `$T4/tests/calibracao/README.md`: "Laudo em `laudos/fixture-fN.md` (nesta pasta)"; "Ficam fora de `biblioteca/`".
4. `FORMATO.md` §5 e §7: onde citar `_index-v2.md` ou `revisao-v2`, o sed já trocou; conferir com `grep -n 'v2' FORMATO.md` e deixar só as menções à "v2" como nome da geração, não como caminho.

- [ ] **Passo 6: escrever o README da biblioteca, fontes.md e historico.md**

`$B4/README.md` (substitui o antigo `README-v2.md`; front matter mantido):

```markdown
---
type: conhecimento
status: em-construcao
title: Curso Subido de Tráfego
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
---

# Curso Subido de Tráfego

Conhecimento do curso como unidades atômicas por aula (camada 1, verdade e auditoria) e visões geradas por tarefa, plataforma e tema (camada 2, o que o agente lê). Consumidor: agente gestor de tráfego que opera contas da TC3, audita contas e alimenta skills futuras. Skill e agente ficam fora desta pasta.

Situação: em construção. Frente e sessões em projetos/tc3/frentes/curso-subido-base-atomica (registro no Jarvis 4: `projetos/tc3/frentes/curso-subido-base-atomica/projetos/tc3/frentes/curso-subido-base-atomica/README.md`). Aulas cobertas: ver indice.md (registro no Jarvis 4: `projetos/tc3/frentes/curso-subido-base-atomica/documentos/planos/indice.md`) (gerado).

## O que ler, por necessidade

| Preciso de… | Abro |
|---|---|
| executar uma tarefa (criar campanha, diagnosticar verba…) | `visoes/playbooks/<tarefa>.md` |
| auditar uma conta numa plataforma | `visoes/checklists/<plataforma>.md` |
| entender um termo | `visoes/glossario.md` |
| navegar por assunto | `visoes/temas/<tema>.md` (gerada; não é fonte) |
| conferir a origem de uma afirmação | `unidades/<slug>.md`, bloco `U:<aula_id>:<nnn>` |
| saber o que o curso não resolve | seção "Sem resolução no curso" do playbook e `consolidacao/` |

Toda frase de playbook, checklist e glossário termina com citação `U:…`. Sem citação, não é conhecimento do curso.

## Contratos e revisão

- taxonomia.md (registro no Jarvis 4: `projetos/tc3/frentes/curso-subido-base-atomica/documentos/planos/taxonomia.md`): enums fechados de plataformas, temas, tarefas e tipos.
- FORMATO.md (registro no Jarvis 4: `projetos/tc3/frentes/curso-subido-base-atomica/documentos/planos/FORMATO.md`): schema da unidade, IDs, versão e hash, `insumos_hash`, visões e laudos.
- revisao/ (registro no Jarvis 4: `projetos/tc3/frentes/curso-subido-base-atomica/documentos/planos/revisao/README.md`): rubrica com cinco vetos, papéis, amostra, laudos e avaliação de uso.
- fontes.md (registro no Jarvis 4: `projetos/tc3/frentes/curso-subido-base-atomica/documentos/planos/fontes.md`): onde está a fonte bruta e o que não entra aqui.
- historico.md (registro no Jarvis 4: `projetos/tc3/frentes/curso-subido-base-atomica/documentos/planos/historico.md`): incorporações e correções por sessão.

## Ferramentas

Em ferramentas/curso-subido (registro no Jarvis 4: `projetos/tc3/frentes/curso-subido-base-atomica/ferramentas/curso-subido/README.md`). Gates de qualquer commit nesta pasta:

```bash
python3 ferramentas/curso-subido/validate_unidades.py
python3 ferramentas/curso-subido/build_indices.py --check
python3 ferramentas/curso-subido/validate_visoes.py --playbooks --desatualizadas
python3 -m unittest discover -s ferramentas/curso-subido/tests -p 'test_curso_subido_*.py'
```

`_gerado/desatualizadas.md` vazio é gate: unidade editada invalida quem a cita até o derivado ser revisto e selado.
```

`$B4/fontes.md`:

```markdown
# Fontes do Curso Subido

- Transcrições, PDFs e txt: clone local `~/curso-subido-trafego-transcricoes` do repo `tc3midia/curso-subido-trafego-transcricoes`, commit `f188775`, somente leitura. 133 aulas em 8 módulos, `manifest.jsonl` com `aula_id` (16 hex), duração e caminho. `pdftotext` em `/opt/homebrew/bin`.
- Nenhum `.pdf`, `.srt` ou `transcricao.md` é copiado para esta pasta. Cada unidade guarda `fonte` e `faixa` para localizar o trecho no clone.
- Síntese anterior (v1, memos por aula, 2026-09-09): `Jarvis 3.0/Conhecimento/Tráfego Pago/Curso Subido de Tráfego/memos/`. Histórico, não estado vigente; nenhum papel desta base lê memos. Só a avaliação de uso compara v1 com v2.
- Etapa 0 (contratos, ouros, calibração): Jarvis 3.0, branch `task/curso-subido-v2-etapa-0`, commit `719408a`. As rodadas arquivadas dos laudos de calibração ficaram lá.
```

`$B4/historico.md`:

```markdown
# Histórico editorial

| Data | Operação | Fontes | Alterado | Lacunas |
|---|---|---|---|---|
| 2026-09-14 | Promoção da Etapa 0 do Jarvis 3.0 (commit 719408a) para esta pasta. Fixtures de calibração foram para a ferramenta; rodadas arquivadas e memos v1 ficaram no 3.0. FORMATO.md e taxonomia.md só mudaram caminhos; derivados vivos foram selados de novo sem nova revisão. | Sessão 1 do plano da frente | tudo nesta pasta | 131 aulas por extrair |
```

- [ ] **Passo 7: README da ferramenta e índices do Jarvis 4**

`$T4/README.md`:

```markdown
# Curso Subido: ferramentas da base atômica

Scripts e testes da biblioteca do Curso Subido (registro no Jarvis 4: `projetos/tc3/frentes/curso-subido-base-atomica/biblioteca/curso-subido-trafego/README.md`). Stdlib only. Contrato em `FORMATO.md` da biblioteca.

| Script | Faz | Uso |
|---|---|---|
| `unidades.py` | biblioteca: manifest, parser, hash, taxonomia, citações | importado pelos outros |
| `validate_unidades.py` | valida arquivos de unidades (FORMATO §1 a §4) | `[--modulo 001 \| --arquivo slug] [--json] [--sem-fontes]`; exit 1 se erro |
| `build_indices.py` | gera `_gerado/`, `visoes/temas/`, `indice.md` | `--check` compara com o disco |
| `validate_visoes.py` | playbooks, checklists, glossário, consolidação, órfãs, desatualizadas | `--playbooks --consolidacao --orfas --desatualizadas`; `--selar ARQ…` grava `insumos_hash` |
| `pacote.py` | monta o pacote de um subagente | `extracao\|reextracao\|tarefa\|plataforma\|tema\|orfas <chave> --saida DIR` |

Todos aceitam `--root` (default: a biblioteca) e `--revisao` (default `revisao`). Pacotes vão para `_saida/tc3/<trabalho>/temporarios/`, nunca para o git.

Testes: `python3 -m unittest discover -s ferramentas/curso-subido/tests -p 'test_curso_subido_*.py'`. `tests/calibracao/` guarda fixtures com defeito plantado e seus laudos; expectativas só em `esperado.jsonl`. Elas nunca entram em pacote de extrator nem na biblioteca.

Clone das fontes: `~/curso-subido-trafego-transcricoes` em `f188775`; `CURSO_SUBIDO_CLONE` sobrescreve.
```

Acrescentar uma linha em `$J4/biblioteca/README.md`, depois do item Three Ms:

```markdown
- Curso Subido de Tráfego (registro no Jarvis 4: `projetos/tc3/frentes/curso-subido-base-atomica/documentos/planos/curso-subido-trafego/README.md`): base atômica do curso de tráfego pago, em construção por sessões; contratos, unidades por aula e visões por tarefa.
```

E em `$J4/ferramentas/README.md`, depois do item Kie.ai:

```markdown
- Curso Subido (registro no Jarvis 4: `projetos/tc3/frentes/curso-subido-base-atomica/documentos/planos/curso-subido/README.md`): validadores, geradores de índice e montador de pacotes da base atômica do curso, com testes e fixtures de calibração.
```

- [ ] **Passo 8: regenerar, selar e rodar os gates**

```bash
cd "$J4"
: > "$B4/_gerado/selos.jsonl"
python3 ferramentas/curso-subido/validate_visoes.py --selar \
  "$B4/visoes/playbooks/diagnosticar-concentracao-de-verba.md" \
  "$B4/revisao/laudos/1674fc3d8d94c601.md" \
  "$B4/revisao/laudos/869445a4c64befbf.md" \
  "$B4/revisao/laudos/playbook-diagnosticar-concentracao-de-verba.md"
python3 ferramentas/curso-subido/build_indices.py
python3 ferramentas/curso-subido/build_indices.py --check
python3 ferramentas/curso-subido/validate_unidades.py
python3 ferramentas/curso-subido/validate_visoes.py --playbooks --desatualizadas
cat "$B4/_gerado/desatualizadas.md"
python3 -m unittest discover -s ferramentas/curso-subido/tests -p 'test_curso_subido_*.py'
```

Esperado: `--check` limpo, validador 0 erros, `desatualizadas.md` sem linhas de artefato, 58 testes OK. O `--selar` é necessário porque `FORMATO.md` e `taxonomia.md` mudaram de texto (caminhos) e o hash deles entra no `insumos_hash`; a entrada em `historico.md` registra que não houve nova revisão. Se `--selar` falhar por `selos.jsonl` inexistente, o `: >` acima já o criou vazio.

Conferir que nada bruto entrou: `find "$B4" -name '*.pdf' -o -name '*.srt' -o -name 'transcricao.md'` retorna vazio. Conferir que `indice.md` não linka `memos` nem `historico/etapa-1`.

- [ ] **Passo 9: commit e fechamento**

```bash
cd "$J4"
git add biblioteca/curso-subido-trafego biblioteca/README.md ferramentas/curso-subido ferramentas/README.md projetos/tc3
git status --short      # só os caminhos acima em verde; o resto do working tree fica como estava
git commit -m "conhecimento: promove a base atômica do Curso Subido para o Jarvis 4

Etapa 0 vinda do Jarvis 3.0 (719408a): contratos, 2 ouros, playbook piloto,
revisão v2 e avaliação de uso na biblioteca; scripts, testes e fixtures de
calibração em ferramentas/curso-subido. Memos v1 e rodadas arquivadas ficam no 3.0.

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

Atualizar `$FR/tarefas.md` (Sessão 1 feita, hash do commit). Push para `origin` só se Will já tiver dito sim em `tarefas.md`; senão anotar como pendência. No Jarvis 3.0 nada muda nesta sessão.

---

### Sessão 2: ferramentas da leva

**Arquivos:**
- Criar: `$T4/reconciliar.py`, `$T4/tests/test_curso_subido_v2_reconciliar.py`
- Modificar: `$T4/pacote.py` (modo `pendentes`), `$T4/tests/test_curso_subido_v2_unidades.py`, `$B4/revisao/papeis/{extrator,sintetizador,juiz}.md`

**Interfaces:**
- Produz: `reconciliar.reconciliar(texto_antigo: str, texto_novo: str) -> tuple[str, dict]` (texto reconciliado e relatório `{"preservadas": [...], "novas": [...], "retiradas": [...], "divisoes": [...], "fusoes": [...]}`), CLI `python3 ferramentas/curso-subido/reconciliar.py <antigo.md> <novo.md> [--saida ARQ]`; `pacote.py pendentes [--modulo 00X]` imprimindo `modulo<TAB>aula_id<TAB>slug<TAB>palavras` das aulas sem arquivo em `unidades/`.

- [ ] **Passo 1: teste de reconciliação (falha primeiro)**

`$T4/tests/test_curso_subido_v2_reconciliar.py`:

```python
"""Reconciliação de reextração: IDs preservados, novos no fim, retiradas, divisões e fusões."""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FERRAMENTA = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FERRAMENTA))

import reconciliar  # noqa: E402
import unidades as lib  # noqa: E402

AULA = "0123456789abcdef"
FRONT = f"""---
type: unidades-aula
status: rascunho
title: "Teste"
modulo: "001"
ordem: 1
aula_id: {AULA}
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - transcricao.md
extraido_em: 2026-09-14
gerado_por: sonnet-5
retiradas: []
divisoes: []
fusoes: []
---

# Teste

## Contexto da aula
Aula de teste.

## Unidades
"""


def bloco(n: int, titulo: str, corpo: str, versao: int = 1) -> str:
    return f"""### U:{AULA}:{n:03d} — {titulo}
```yaml
tipo: regra
plataforma: [meta]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:01:00–00:02:00
perecivel: false
confianca: alta
versao: {versao}
```
{corpo}

"""


ANTIGO = FRONT + bloco(1, "Um anúncio por ideia", "Cada anúncio testa uma ideia só.") + bloco(2, "Cinco ou seis anúncios por conjunto", "Subir cinco ou seis anúncios por conjunto para o leilão escolher.") + bloco(3, "Trocar criativo cansado", "Trocar o criativo quando a frequência passa de três.")


class ReconciliarTest(unittest.TestCase):
    def test_mesma_unidade_com_texto_corrigido_preserva_id_e_sobe_versao(self):
        novo = FRONT + bloco(1, "Um anúncio por ideia", "Cada anúncio testa uma única ideia.") + bloco(2, "Cinco ou seis anúncios por conjunto", "Subir cinco ou seis anúncios por conjunto para o leilão escolher.") + bloco(3, "Trocar criativo cansado", "Trocar o criativo quando a frequência passa de três.")
        texto, rel = reconciliar.reconciliar(ANTIGO, novo)
        arq = lib.parse_arquivo_unidades(texto)
        ids = [u.id for u in arq.unidades]
        self.assertEqual(ids, [f"U:{AULA}:001", f"U:{AULA}:002", f"U:{AULA}:003"])
        self.assertEqual(arq.unidades[0].meta["versao"], 2)
        self.assertEqual(arq.unidades[1].meta["versao"], 1)
        self.assertEqual(rel["novas"], [])

    def test_divisao_retira_a_antiga_e_numera_as_novas_no_fim(self):
        novo = FRONT + bloco(1, "Um anúncio por ideia", "Cada anúncio testa uma ideia só.") + bloco(2, "Cinco anúncios no mínimo", "Subir pelo menos cinco anúncios por conjunto.") + bloco(3, "Seis anúncios no máximo", "Não passar de seis anúncios por conjunto.") + bloco(4, "Trocar criativo cansado", "Trocar o criativo quando a frequência passa de três.")
        texto, rel = reconciliar.reconciliar(ANTIGO, novo, divisoes=[(f"U:{AULA}:002", [2, 3])])
        arq = lib.parse_arquivo_unidades(texto)
        ids = [u.id for u in arq.unidades]
        self.assertEqual(ids, [f"U:{AULA}:001", f"U:{AULA}:003", f"U:{AULA}:004", f"U:{AULA}:005"])
        self.assertEqual(arq.front["retiradas"], [f"U:{AULA}:002"])
        self.assertEqual(arq.front["divisoes"], [f"U:{AULA}:002 → U:{AULA}:004, U:{AULA}:005"])

    def test_unidade_que_some_vai_para_retiradas(self):
        novo = FRONT + bloco(1, "Um anúncio por ideia", "Cada anúncio testa uma ideia só.") + bloco(2, "Cinco ou seis anúncios por conjunto", "Subir cinco ou seis anúncios por conjunto para o leilão escolher.")
        texto, rel = reconciliar.reconciliar(ANTIGO, novo)
        arq = lib.parse_arquivo_unidades(texto)
        self.assertEqual(arq.front["retiradas"], [f"U:{AULA}:003"])
        self.assertEqual(rel["retiradas"], [f"U:{AULA}:003"])

    def test_numero_retirado_nao_volta(self):
        antigo = ANTIGO.replace("retiradas: []", f"retiradas: [U:{AULA}:004]")
        novo = FRONT + bloco(1, "Um anúncio por ideia", "Cada anúncio testa uma ideia só.") + bloco(2, "Cinco ou seis anúncios por conjunto", "Subir cinco ou seis anúncios por conjunto para o leilão escolher.") + bloco(3, "Trocar criativo cansado", "Trocar o criativo quando a frequência passa de três.") + bloco(4, "Nova orientação", "Regra nova que não existia.")
        texto, rel = reconciliar.reconciliar(antigo, novo)
        arq = lib.parse_arquivo_unidades(texto)
        self.assertEqual([u.id for u in arq.unidades][-1], f"U:{AULA}:005")
        self.assertEqual(rel["novas"], [f"U:{AULA}:005"])


if __name__ == "__main__":
    unittest.main()
```

Rodar: `python3 -m unittest ferramentas/curso-subido/tests/test_curso_subido_v2_reconciliar.py`. Esperado: `ModuleNotFoundError: reconciliar`.

- [ ] **Passo 2: implementar `reconciliar.py`**

Regras (a numeração do arquivo novo vindo do extrator é descartada; só o conteúdo importa):

1. Parsear os dois textos com `lib.parse_arquivo_unidades`.
2. Casar cada unidade nova com uma antiga viva: título igual (normalizado por `lib.slugify`) ou Jaccard de palavras do corpo ≥ 0,6. Uma antiga casa no máximo uma vez, exceto quando listada em `divisoes` (parâmetro `divisoes: list[tuple[str, list[int]]]`, ID antigo e posições 1-based das novas que saíram dela).
3. Casada: mantém o ID antigo; se `lib.hash_unidade` mudou, `versao` = versão antiga + 1, senão mantém.
4. Não casada: recebe o próximo número depois de `max(presentes ∪ retiradas)`, na ordem em que aparece no novo.
5. Antiga sem par: vai para `retiradas` (bloco removido).
6. Divisão: a antiga vai para `retiradas` e as novas recebem números novos; `divisoes` recebe `"U:x:002 → U:x:004, U:x:005"`. Fusão (parâmetro `fusoes: list[tuple[list[str], int]]`): as antigas vão para `retiradas`, a nova recebe número novo, `fusoes` recebe `"U:x:002, U:x:003 → U:x:006"`.
7. Serializar com `lib.serializar_unidade` e `lib.substituir_campo_front` para `retiradas`, `divisoes`, `fusoes`; ordem dos blocos = ordem do arquivo novo.
8. Relatório: `{"preservadas", "novas", "retiradas", "divisoes", "fusoes"}` com IDs.
9. CLI: `reconciliar.py <antigo> <novo> [--saida ARQ] [--divisao U:x:002=2,3 ...] [--fusao U:x:002+U:x:003=4 ...]`; sem `--saida` imprime o texto; imprime o relatório em stderr como JSON.

Rodar os 4 testes: verdes. Rodar `validate_unidades.py` sobre a saída de um caso (gravar no `$S4`) para confirmar que o validador aceita presentes ∪ retiradas = `001..max`.

- [ ] **Passo 3: `pacote.py pendentes` com teste**

Acrescentar em `test_curso_subido_v2_unidades.py`, classe `ArquivosReaisTest`:

```python
    def test_pendentes_lista_so_aulas_sem_arquivo(self):
        import pacote
        pend = pacote.pendentes(BASE)
        slugs_extraidos = {p.stem for p in (BASE / "unidades").glob("*.md")}
        self.assertEqual(len(pend) + len(slugs_extraidos), 133)
        self.assertTrue(all(r["slug"] not in slugs_extraidos for r in pend))
        self.assertEqual(len(pacote.pendentes(BASE, modulo="003")), 7)
```

Implementar em `pacote.py`:

```python
def pendentes(root: Path, modulo: str | None = None) -> list[dict]:
    """Aulas do manifest sem arquivo em unidades/, com contagem de palavras da transcrição."""
    root = Path(root)
    feitos = {p.stem for p in (root / "unidades").glob("*.md")}
    out = []
    for row in sorted(lib.load_manifest().values(), key=lambda r: (r["modulo3"], r["ordem"])):
        if modulo and row["modulo3"] != modulo:
            continue
        if row["slug"] in feitos:
            continue
        palavras = len(lib.texto_fonte(row, "transcricao.md").split())
        out.append({"modulo": row["modulo3"], "aula_id": row["id"], "slug": row["slug"], "palavras": palavras})
    return out
```

Registrar `pendentes` nos `choices` do argparse (chave opcional) e imprimir `modulo\taula_id\tslug\tpalavras`, com `--modulo` como filtro. Se `lib.texto_fonte` tiver outra assinatura, adaptar aqui e não na lib. Testes verdes.

No mesmo passo, a saída de `pacote.py extracao|reextracao` passa a imprimir `<caminho> <total> palavras (aula: <n>)`, onde `<n>` conta só transcrição e PDFs em texto, sem papel, FORMATO, taxonomia e âncora do ouro. É esse `<n>` que decide Sonnet ou Opus no Procedimento E. Teste em `test_curso_subido_v2_unidades.py`: para uma aula qualquer, `total - aula` é igual à soma das palavras das partes fixas.

- [ ] **Passo 4: lições da calibração nos papéis**

Em `$B4/revisao/papeis/extrator.md`, seção Escreve, acrescentar:

```markdown
- Desfecho que o professor não conta não existe. Se a história fica em suspense, a unidade para onde a fala para. Nunca escreva "mudou de patamar", "funcionou" ou "resolveu" sem a frase do professor.
- `plataforma` é afirmação de escopo. `google` significa "vale para todas as redes do Google". Se a aula só demonstra YouTube, etiquete `[youtube]`. Se demonstra Meta e diz que vale para Google, etiquete as duas e registre em `nota` a frase que estende.
- `limite` só diz o que a aula mostra ou declara não cobrir. Nada de inferir lacunas.
```

Em `sintetizador.md`, seção Escreve, acrescentar:

```markdown
- "Réguas e critérios de pronto" cita só `regua`. Exemplo numérico do professor sem valor de régua vai em "O que o curso não cobre" como exemplo, citando o `exemplo`.
- Subseção de plataforma com "Nada nas fontes." precisa citar um `limite` compatível ou não afirma nada além de "Nada nas fontes.".
```

Em `juiz.md`, seção Decide, acrescentar:

```markdown
- Em "Nada nas fontes.", confira que o `limite` citado fala daquela plataforma. Etiqueta `plataforma` ampla numa unidade que a aula não demonstra é falha de fidelidade.
```

Papéis não entram no `insumos_hash`; nada a selar.

- [ ] **Passo 5: gates e commit**

```bash
cd "$J4"
python3 ferramentas/curso-subido/build_indices.py --check && python3 ferramentas/curso-subido/validate_visoes.py --desatualizadas
python3 -m unittest discover -s ferramentas/curso-subido/tests -p 'test_curso_subido_*.py'     # 63 testes
git add ferramentas/curso-subido biblioteca/curso-subido-trafego/revisao/papeis projetos/tc3/frentes/curso-subido-base-atomica biblioteca/curso-subido-trafego/historico.md
git commit -m "curso-subido: reconciliar.py, pendentes e lições da calibração nos papéis

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

Atualizar `tarefas.md` e `historico.md`.

---

## Procedimento E: extrair um módulo (usado nas Sessões 3 a 11)

Parâmetros da sessão: `MOD` (módulo, 3 dígitos), lista de aulas (todas do módulo ou uma metade), `AMOSTRA` (quantas aulas passam por inspetor e juiz no fim do módulo), checkpoint, mensagem de commit.

**E1. Levantar o pendente.**

```bash
cd "$J4"; mkdir -p "$S4/pacotes" "$S4/laudos"
python3 ferramentas/curso-subido/pacote.py pendentes --modulo $MOD
```

**E2. Montar os pacotes do lote** (6 a 8 aulas por lote):

```bash
for id in <aula_ids do lote>; do python3 ferramentas/curso-subido/pacote.py extracao $id --saida "$S4/pacotes"; done
```

O comando imprime o caminho, o total de palavras do pacote e as palavras da aula. Extrator: `model: opus` em todas as aulas até o CP2. Se o CP2 trouxer o Sonnet de volta, a regra passa a ser: mais de 8.000 palavras **da aula** (não do pacote) `model: opus`, senão `model: sonnet`. Reextração segue o mesmo modelo. Anotar em `tarefas.md` as palavras da aula de cada extração, para o CP2 decidir.

**E3. Lançar um Agent por aula, todos na mesma mensagem, em background.** Prompt do extrator (substituir os campos):

```text
Você é o extrator da base atômica do Curso Subido de Tráfego. Seu papel completo está dentro do pacote.
Leia o pacote em <caminho do pacote> do início ao fim. Ele contém tudo: cabeçalho YAML já preenchido, transcrição, PDFs em texto, taxonomia, FORMATO §1 a §4, o papel do extrator e 6 unidades do ouro como âncora de granularidade.
Escreva o arquivo <B4>/unidades/<slug>.md completo, conforme FORMATO.md, e não abra nenhum outro arquivo do repositório nem da internet. Não leia memos, outras aulas ou playbooks.
Front matter: gerado_por: <sonnet-5 ou opus-5>, status: rascunho, extraido_em: <data de hoje>.
Ao terminar, responda só com: quantidade de unidades por tipo, quantas proposta_tag, quantas confianca baixa.
```

**E4. Validar o lote e corrigir.**

```bash
python3 ferramentas/curso-subido/validate_unidades.py --modulo $MOD
```

Aula com erro (regra da Sessão 3b, decidida no CP2): separar erro mecânico de erro de conteúdo.

- Erro mecânico (contexto acima de 8 linhas, título acima de 80 caracteres e afins de forma): a sessão corrige direto no arquivo na primeira passada, com `nota:` explicando e `versao` subindo; sem agente.
- Erro de conteúdo (régua sem número, cópia bruta, faixa errada, estrutura do tipo errada): `pacote.py correcao <aula_id> --unidades U:<aula_id>:007,U:<aula_id>:021 --erros "<saída do validador>" --saida "$S4/pacotes"` e um Agent `opus` (o extrator) com o prompt: "Você é o extrator da base atômica do Curso Subido. Leia o pacote <caminho> do início ao fim: ele traz seu papel, FORMATO §1 a §4, o front matter, os blocos a corrigir, o trecho da transcrição de cada faixa e os erros do validador. Corrija em <B4>/unidades/<slug>.md só as unidades listadas, no lugar, mantendo os IDs e subindo `versao`. Não abra nenhum outro arquivo. Responda só com os IDs alterados." No máximo 2 correções por aula; depois, correção manual pela própria sessão (Fable 5.1) com `nota:` explicando.
- Reextração completa (`pacote.py reextracao <aula_id> --saida "$S4/pacotes"`, mesmo modelo da regra de E2, prompt de E3 mais "O validador devolveu os erros abaixo; corrija só o apontado, mantendo os IDs existentes: <lista>") só quando o arquivo inteiro está ruim: cópia bruta generalizada, granularidade errada em muitas unidades, contexto que não descreve a aula. Reextração total de uma aula já commitada passa por `reconciliar.py` (IDs preservados).

Warnings de densidade (fora de 3 a 60 unidades) ou `confianca: baixa` não bloqueiam, mas ficam anotados em `tarefas.md`.

**E5. Repetir E2 a E4 até o módulo (ou a metade prevista) estar sem pendentes.**

**E6. Gate do módulo** (só quando o módulo fecha; sessão de meia leva pula para E9 com `status: rascunho`):

```bash
python3 ferramentas/curso-subido/validate_unidades.py --modulo $MOD
python3 ferramentas/curso-subido/build_indices.py
cat "$B4/_gerado/propostas_tags.md"
```

Triagem de `proposta_tag` na sessão: aceitar = acrescentar a tag em `taxonomia.md` (bullet ou linha da tabela, com definição) e retirar `proposta_tag` das unidades que a usam, trocando a tag; recusar = retirar `proposta_tag` e deixar a tag mais próxima com `nota`. Toda mudança de unidade sobe `versao`. Mudança em `taxonomia.md` exige `--selar` dos derivados vivos (listar com `validate_visoes.py --desatualizadas`). Meta: zero `proposta_tag` no módulo fechado.

**E7. Revisão amostral do módulo.** Escolher `AMOSTRA` aulas pelo `aula_id` ordenado (a menor; no módulo 001 a menor e a maior), pulando ouros.

Inspetor (Agent `sonnet`, um por aula, pacote `pacote.py inspecao <aula_id> --saida "$S4/pacotes"`; desde a Sessão 3b o inspetor não recebe o pacote de extração), prompt:

```text
Você é o inspetor da base atômica do Curso Subido. Leia o pacote <S4>/pacotes/inspecao-<slug>.md do início ao fim: ele traz seu papel, a RUBRICA, FORMATO §8, o artefato sob inspeção (unidades/<slug>.md) e a fonte bruta (transcrição e PDFs em texto).
Escreva <B4>/revisao/laudos/<aula_id>.evidencia.md no formato de FORMATO.md §8: tabela por unidade (lastreada, desvio, sem-lastro, faixa-errada, com a frase da fonte que sustenta ou contradiz), omissões (números e passos da fonte sem unidade), contrato, PDFs. gerado_por: sonnet-5. Não reescreva unidades. Não abra nenhum outro arquivo: nem memos, nem outras aulas, nem o clone.
```

Juiz (Agent `fable`, contexto fresco, um por aula, depois do inspetor), prompt:

```text
Você é o juiz da base atômica do Curso Subido. Leia <B4>/revisao/papeis/juiz.md e <B4>/revisao/RUBRICA.md.
Julgue <B4>/unidades/<slug>.md usando o laudo de evidência <B4>/revisao/laudos/<aula_id>.evidencia.md e a saída do validador abaixo. Não abra transcrição, PDF, clone, memos, outros laudos nem playbooks; se algo assim aparecer no seu contexto, declare isolamento inválido e pare.
Saída do validador: <colar a saída de validate_unidades.py --arquivo <slug> --json>
Escreva <B4>/revisao/laudos/<aula_id>.md no formato de FORMATO.md §8, com veredito passa|falha|bloqueado, vetos, seções Fidelidade, Cobertura, Perecibilidade, Contrato, Falhas (uma linha por item, com ID), Próximo. gerado_por: fable-5.1, isolamento: ok, insumos_hash: PENDENTE.
```

Depois de conferir manualmente a rastreabilidade e a cobertura acumulada conforme a RUBRICA: `python3 ferramentas/curso-subido/validate_visoes.py --selar "$B4/revisao/laudos/<aula_id>.md"`. Parecer focal sem cobertura acumulada completa fica em temporários; não emitir `passa` final nem tratá-lo como revisão integral. O selo atual não verifica escopo nem hashes da evidência.

**Regra vigente de qualidade e retrabalho (decisão de Will, 15/09/2026):** aplicar a gravidade e o tratamento local definidos na RUBRICA. Não reextrair módulo por contagem de reprovações. Consolidar cada falha com ID, evidência, impacto prático, correção mínima e aceite. Erro mecânico é corrigido e checado por script; ajuste menor fica registrado sem nova rodada só por ele. Falha material segue para o redator apenas nas unidades afetadas.

Mesma causa material confirmada em duas aulas exige uma única ampliação da inspeção para duas adicionais ainda não revisadas (próximas no `aula_id` ordenado), buscando essa causa, antes de encerrar a revisão da leva. A ampliação não manda reextrair nem se repete automaticamente. Nova ampliação exige alcance demonstrado e escopo registrado. Reextração de uma aula exige defeito amplo comprovado nela e justificativa para não bastar correção localizada; preservar identidade com `reconciliar.py`.

Redator (Agent `opus` no fluxo Claude; Sol na rota Codex), só na lista consolidada:

```text
Você é o redator da base atômica do Curso Subido. Leia <B4>/revisao/papeis/redator.md.
Corrija em <B4>/unidades/<slug>.md só os itens da seção Falhas do laudo <B4>/revisao/laudos/<aula_id>.md, usando a evidência de <B4>/revisao/laudos/<aula_id>.evidencia.md. Unidade sem lastro é retirada (remover o bloco e registrar em retiradas), não reescrita. Toda unidade alterada sobe versao. Não renumere. Não abra transcrição nem PDF.
```

Depois do redator: validador, `build_indices.py` e verificação dos derivados afetados. Mudança de conteúdo recebe inspeção focal e juiz em contexto fresco, com evidência atualizada dos trechos alterados e evidência preservada do restante somente se hashes/versões continuarem iguais. A coordenação monta o pacote focal temporário; o comando padrão de inspeção não ficou menor por esta mudança de regra. Correção mecânica objetiva se encerra com o script. Ajuste menor não exige outra chamada de modelo por si só.

No máximo dois ciclos automáticos de correção e verificação por artefato na etapa; apontamentos novos, candidatos, mudança da regra ou renomeação da etapa não reiniciam o contador. Depois, apenas uma intervenção residual da coordenação e uma única verificação focal final; persistindo falha material, isolar em rascunho/bloqueado e levar o caso concreto a Will, sem novas chamadas automáticas. Trabalho independente pode continuar. Não bloquear por simples número do julgamento. Divergência recebe prova, efeito prático e decisão independente do juiz na verificação já prevista; a coordenação não rebaixa sozinha sua própria correção. Preservar rodadas anteriores e consumo. Ver [decisão e aplicação à sessão 5b](../2026-09-15-regra-qualidade-e-retrabalho.md), incluindo o teto já consumido nas aulas 6.1 e 3.2.

Pacote focal e evidência composta seguem o contrato dessa decisão: janelas também das omissões, blocos novos/alterados, dependências, validador e hashes; sem contexto suficiente, devolver à coordenação sem aprovação e sem reiniciar o teto. Antes do juiz e do selo, conferir os hashes guardados na inspeção original, fonte, integridade e compatibilidade da evidência preservada. Documentar em `## Rastreabilidade da revisão`; inspecionar partes sem comprovação anterior.

**E8. Fechar o módulo.**

Na expansão única de 5b sobre 5.0 e 6.0, conferir o conjunto de causas do diagnóstico: condições/ressalvas omitidas, limites/números alterados, hipóteses/nomes incertos apresentados como fatos e tela sem `perecivel`. A parte mecânica cobre somente os casos que o validador de fato detecta; conferir focalmente os demais. Não acrescentar aulas por este ajuste de escopo nem declarar inspeção integral.

Executar somente quando todas as aulas previstas existirem, a revisão exigida (inclusive a única expansão por recorrência) estiver concluída e não houver falha material conhecida pendente. No 002, conferir a causa nas aulas 5.0 e 6.0 conforme a decisão da sessão 5b antes de encerrar a revisão da primeira metade. Ajustes menores registrados não impedem o fechamento. Aula com pendência material continua em rascunho; não executar a promoção em lote abaixo nem declarar o módulo fechado enquanto essa pendência existir. Inspeção focal por causa não significa inspeção integral da aula; registrar essa diferença no fechamento amostral.

```bash
for f in "$B4"/unidades/${MOD}-*.md; do grep -q 'status: ouro' "$f" || sed -i '' 's/^status: rascunho$/status: validado/' "$f"; done
```

Acrescentar o módulo em `MODULOS_FECHADOS` no teste (criar na primeira vez, em `test_curso_subido_v2_unidades.py`, classe `ArquivosReaisTest`):

```python
    MODULOS_FECHADOS = {"001": 18}   # módulo: aulas; cresce a cada módulo fechado

    def test_modulos_fechados_completos_e_validados(self):
        for mod, n in self.MODULOS_FECHADOS.items():
            arquivos = sorted((BASE / "unidades").glob(f"{mod}-*.md"))
            self.assertEqual(len(arquivos), n, mod)
            for p in arquivos:
                front, _ = lib.parse_front_matter(p.read_text(encoding="utf-8"))
                self.assertIn(front["status"], {"validado", "revisado", "ouro"}, p.name)
                self.assertNotIn("proposta_tag", p.read_text(encoding="utf-8"), p.name)
```

Aulas por módulo: 001 = 18, 002 = 36, 003 = 7, 004 = 15, 005 = 28, 006 = 8, 007 = 7, 008 = 14.

**E9. Gates e commit da sessão.**

```bash
cd "$J4"
python3 ferramentas/curso-subido/validate_unidades.py
python3 ferramentas/curso-subido/build_indices.py && python3 ferramentas/curso-subido/build_indices.py --check
python3 ferramentas/curso-subido/validate_visoes.py --playbooks --desatualizadas
python3 -m unittest discover -s ferramentas/curso-subido/tests -p 'test_curso_subido_*.py'
git add biblioteca/curso-subido-trafego ferramentas/curso-subido/tests projetos/tc3/frentes/curso-subido-base-atomica
git commit -m "<mensagem da sessão>

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

Se `desatualizadas.md` acusar o playbook piloto (por edição no ouro 005 ou na taxonomia), a sessão revisa o playbook com o sintetizador (Sessão 13, prompt) ou, se a mudança for só de caminho ou de metadado, sela de novo e anota em `historico.md`.

Atualizar `tarefas.md` (aulas feitas, warnings, reexecuções) e `historico.md`.

---

### Sessões 3 a 11: extração por módulo

Ordem do spec: 001, 003, 002, 004, 006, 007, 005, 008. Cada linha é uma sessão com o Procedimento E.

| Sessão | MOD | Aulas | Lotes | Gate do módulo | AMOSTRA | Checkpoint | Commit |
|---|---|---|---|---|---|---|---|
| 3 | 001 | 18 (menos o ouro 8.3 = 17) | 3 | sim | 2 | **CP2** | `conhecimento: unidades do módulo 001 do Curso Subido` |
| 4 | 003 | 7 | 1 | sim | 1 | | `conhecimento: unidades do módulo 003 do Curso Subido` |
| 5 | 002 | aulas 1 a 18 | 3 | não | | | `conhecimento: unidades do módulo 002 (aulas 1 a 18) do Curso Subido` |
| 6 | 002 | aulas 19 a 36 | 3 | sim | 1 | | `conhecimento: unidades do módulo 002 do Curso Subido` |
| 7 | 004 | 15 | 2 | sim | 1 | | `conhecimento: unidades do módulo 004 do Curso Subido` |
| 8 | 006 e 007 | 8 + 7 | 2 | sim, os dois | 1 cada | | `conhecimento: unidades dos módulos 006 e 007 do Curso Subido` |
| 9 | 005 | aulas 1 a 14 (menos o ouro 4.0) | 2 | não | | | `conhecimento: unidades do módulo 005 (aulas 1 a 14) do Curso Subido` |
| 10 | 005 | aulas 15 a 28 | 2 | sim | 1 | | `conhecimento: unidades do módulo 005 do Curso Subido` |
| 11 | 008 | 14 | 2 | sim | 1 | **CP3** | `conhecimento: unidades do módulo 008 do Curso Subido` |

**CP2 (fim da Sessão 3), Will decide:** granularidade em 2 arquivos do módulo 001 escolhidos por ele, os 2 laudos amostrais, e se o extrator segue em Opus em todas as aulas, passa a Sonnet com Opus só acima de 8.000 palavras da aula, ou ganha definição de agente com esforço alto. A sessão leva ao CP2 os laudos, as reexecuções por aula e as palavras da aula de cada extração. Registrar em `tarefas.md`.

**CP3 (fim da Sessão 11), Will decide:** aceita as estatísticas por tipo, plataforma e tarefa (gerar a tabela a partir de `_gerado/cobertura.jsonl`: unidades por tarefa × plataforma, tarefas da matriz sem unidade), as tags aceitas e recusadas, e os laudos amostrais por módulo. Tarefa da matriz sem unidade em nenhuma plataforma vira item do CP3: manter na taxonomia com "Nada nas fontes" ou retirar.

A partir da Sessão 6, sempre que o módulo 002 (Meta) ou 006 (Display) fechar, o playbook piloto perde `parcial_ate` para aquela plataforma: `desatualizadas.md` não acusa (novas unidades não mudam hash de insumo), então anotar em `tarefas.md` que o piloto será refeito na Sessão 13 junto com os demais playbooks.

---

### Sessão 12: consolidação por tema

**Arquivos:**
- Criar: `$T4/candidatos_consolidacao.py`, `$T4/tests/test_curso_subido_v2_consolidacao.py`, `$T4/tests/calibracao/consolidacao.md`, `$B4/consolidacao/<tema>.md` (até 19)
- Modificar: `$T4/pacote.py` (modo `tema` inclui os candidatos), `$B4/revisao/papeis/consolidador.md` (novo papel, curto, no molde dos outros: Lê, Não lê, Escreve)

**Interfaces:**
- Produz: `candidatos_consolidacao.candidatos(root, tema) -> list[dict]` com `{"a": id, "b": id, "motivo": "jaccard|numeros", "score": float}`; pares do mesmo tema e mesmo tipo (ou `regua` × `regra`) com Jaccard de palavras ≥ 0,45 ou o mesmo conjunto de números no corpo. CLI `candidatos_consolidacao.py [--tema T] [--json]`.
- Formato dos grupos: `FORMATO.md` §6 (bloco `### G:<tema>:<nnn> — título` com `tipo: duplicata|conflito|complemento|condicional`, `unidades: [...]`, `canonica:` opcional, `resolucao:`, `evidencia: [U:...]`); front matter do arquivo com `insumos_hash`. `validate_visoes.py --consolidacao` já valida; `build_indices.py` já preenche `grupo` no JSONL.

- [ ] **Passo 1: teste dos candidatos (falha primeiro)**

```python
"""Consolidação: candidatos por tema e validação dos grupos."""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FERRAMENTA = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FERRAMENTA))

import candidatos_consolidacao as cc  # noqa: E402
import unidades as lib  # noqa: E402
import validate_visoes as vv  # noqa: E402

BASE = ROOT / "biblioteca" / "curso-subido-trafego"


class CandidatosTest(unittest.TestCase):
    def test_par_com_mesmos_numeros_e_candidato(self):
        u1 = lib.Unidade(id="U:0000000000000001:001", titulo="Cinco anúncios", meta={"tipo": "regua", "tema": "criativo", "plataforma": ["meta"]}, corpo=["Subir de 5 a 6 anúncios por conjunto."])
        u2 = lib.Unidade(id="U:0000000000000002:001", titulo="Quantidade de anúncios", meta={"tipo": "regra", "tema": "criativo", "plataforma": ["meta"]}, corpo=["O conjunto precisa de 5 ou 6 anúncios diferentes para o leilão escolher."])
        pares = cc.candidatos_de({u1.id: u1, u2.id: u2}, "criativo")
        self.assertEqual(len(pares), 1)
        self.assertIn(pares[0]["motivo"], {"numeros", "jaccard"})

    def test_temas_diferentes_nao_pareiam(self):
        u1 = lib.Unidade(id="U:0000000000000001:001", titulo="A", meta={"tipo": "regra", "tema": "criativo", "plataforma": ["meta"]}, corpo=["Texto igual de teste com várias palavras iguais."])
        u2 = lib.Unidade(id="U:0000000000000002:001", titulo="A", meta={"tipo": "regra", "tema": "publicos", "plataforma": ["meta"]}, corpo=["Texto igual de teste com várias palavras iguais."])
        self.assertEqual(cc.candidatos_de({u1.id: u1, u2.id: u2}, "criativo"), [])


class GruposReaisTest(unittest.TestCase):
    def test_consolidacao_valida_e_selada(self):
        erros = vv.validar_consolidacao(BASE)
        self.assertEqual(erros, [], erros)
        for p in sorted((BASE / "consolidacao").glob("*.md")):
            front, _ = lib.parse_front_matter(p.read_text(encoding="utf-8"))
            self.assertEqual(front["insumos_hash"], vv.calcular_insumos_hash(BASE, p), p.name)

    def test_conflito_sem_canonica_tem_resolucao_aberta(self):
        for gid, g in lib.todos_grupos(BASE).items():
            if g.meta.get("tipo") == "conflito" and not g.meta.get("canonica"):
                self.assertIn("Sem resolução no curso", " ".join(g.corpo) + str(g.meta.get("resolucao", "")), gid)
```

Se `lib.Unidade` tiver campos obrigatórios diferentes, ajustar o construtor no teste, não a lib. Rodar: falha por módulo ausente.

- [ ] **Passo 2: implementar `candidatos_consolidacao.py`**

`candidatos_de(unidades: dict[str, Unidade], tema: str) -> list[dict]`: filtra pelo tema; pares (a < b) com `tipo` igual ou {regua, regra}; Jaccard das palavras do corpo (minúsculas, sem pontuação, sem stopwords de uma lista curta: de, a, o, que, e, do, da, em, um, uma, para, com, não, por, os, as, no, na, se) ≥ 0,45 ⇒ motivo `jaccard`; ou conjunto de números (regex `\d+(?:[.,]\d+)?`) não vazio e igual ⇒ motivo `numeros`. `candidatos(root, tema)` usa `lib.todas_unidades(root)`. CLI imprime `a\tb\tmotivo\tscore`. Testes de candidatos verdes; os de grupos reais falham até o Passo 4 (é o esperado nesta ordem).

- [ ] **Passo 3: calibração e papel**

`$T4/tests/calibracao/consolidacao.md`: três casos com unidades sintéticas (mesmo formato de bloco) e resultado esperado em `esperado.jsonl` (chaves `fixture: c1|c2|c3`, `tipo_esperado`, `canonica_esperada`): c1 fala corrige PDF explicitamente ("o PDF está desatualizado") ⇒ `conflito` com canônica na fala e `evidencia` apontando a unidade que corrige; c2 aula posterior diverge sem evidência ⇒ `conflito` sem canônica, resolução "Sem resolução no curso"; c3 duas recomendações sob `condicoes` diferentes ⇒ `condicional`, sem canônica. Rodar o consolidador (Agent `opus`) nos 3 casos antes da leva; se errar, corrigir o papel, não o caso. Registrar em `amostra.md`.

`$B4/revisao/papeis/consolidador.md`:

```markdown
# Papel: consolidador (v2)

Você escreve `consolidacao/<tema>.md` a partir das unidades de um tema. Modelo: Opus 5. `gerado_por` obrigatório.

## Lê (só o pacote)

Unidades do tema (ID, metadados, corpo), lista de pares candidatos, `FORMATO.md` §6, `taxonomia.md`, este papel.

## Não lê

Transcrição, PDF, memos, outras consolidações, playbooks, laudos.

## Escreve

Grupos `G:<tema>:<nnn>` só onde há relação real; par candidato sem relação é ignorado, sem registro.
- Mesma orientação em fontes diferentes: `duplicata`, canônica = a mais completa.
- Orientações que valem sob condições distintas: `condicional`, sem canônica, `resolucao` descreve as condições citando as unidades.
- Correção explícita na fonte (o professor diz que o PDF está velho, que mudou de opinião): `conflito` com canônica e `evidencia` apontando a unidade que corrige.
- Divergência sem evidência: `conflito` sem canônica; `resolucao` começa com "Sem resolução no curso" e registra as duas orientações com fonte.
- Não existem as regras "PDF vence fala", "aula posterior vence anterior", "específica vence geral".
- Nunca edite unidade. Conflito que muda decisão operacional (lance, orçamento, estrutura) recebe `escalar: true` para o CP4.
- Deixe `insumos_hash: PENDENTE`.
```

- [ ] **Passo 4: leva de 19 temas**

Fazer `pacote.py tema <tema>` incluir a saída de `candidatos(root, tema)` e o papel do consolidador. Para cada tema com unidades (`build_indices` lista em `visoes/temas/`): `pacote.py tema <tema> --saida "$S4/pacotes"` e um Agent `opus`:

```text
Você é o consolidador da base atômica do Curso Subido. Leia o pacote <S4>/pacotes/tema-<tema>.md do início ao fim e escreva <B4>/consolidacao/<tema>.md conforme FORMATO.md §6 e o papel incluído no pacote. Não abra nenhum outro arquivo. gerado_por: opus-5. Responda só com: número de grupos por tipo e a lista dos grupos com escalar: true.
```

Depois de cada lote: `validate_visoes.py --consolidacao`; erros voltam ao mesmo agente com a lista. Ao final: `--selar` de todos os `consolidacao/*.md`, `build_indices.py` (preenche `grupo` no JSONL), testes verdes.

- [ ] **Passo 5: gates, commit e CP4**

Gates E9. Commit `conhecimento: consolidação por tema do Curso Subido`. **CP4, Will decide:** cada grupo com `escalar: true` (as duas unidades e a evidência, listadas em `tarefas.md`); a decisão dele vira `canonica` e `resolucao` com `decidido_por: human.will`, `versao` do grupo sobe, `--selar`.

---

### Sessão 13: playbooks

**Arquivos:**
- Criar: `$B4/visoes/playbooks/<tarefa>.md` para as 40 tarefas (o piloto é refeito e perde `parcial_ate`)
- Modificar: `$T4/tests/test_curso_subido_v2_visoes.py` (contagem: 40 playbooks, matriz coberta)

- [ ] **Passo 1: teste da matriz (falha primeiro)**

```python
    def test_quarenta_playbooks_cobrem_a_matriz(self):
        tax = lib.load_taxonomia(BASE / "taxonomia.md")
        playbooks = {p.stem for p in (BASE / "visoes" / "playbooks").glob("*.md")}
        self.assertEqual(playbooks, set(tax.tarefas))
        for tarefa, info in tax.tarefas.items():
            text = (BASE / "visoes" / "playbooks" / f"{tarefa}.md").read_text(encoding="utf-8")
            for plat in info["plataformas"]:
                self.assertIn(f"### {plat}", text, f"{tarefa}: sem subseção {plat}")
            self.assertNotIn("parcial_ate", text, tarefa)
```

`lib.load_taxonomia` recebe o caminho do `taxonomia.md` e devolve `Taxonomia(plataformas, temas, tarefas, tipos, definicoes)`, com `tarefas[tarefa] = {"grupo": ..., "plataformas": [...]}`.

- [ ] **Passo 2: leva de 40, em dois lotes de 20** (Agent `opus` por tarefa; pacote `pacote.py tarefa <tarefa> --saida "$S4/pacotes"`):

```text
Você é o sintetizador da base atômica do Curso Subido. Leia o pacote <S4>/pacotes/tarefa-<tarefa>.md do início ao fim (unidades da tarefa, grupos da consolidação, limites, matriz, FORMATO §6, papel, playbook ouro). Escreva <B4>/visoes/playbooks/<tarefa>.md com as nove seções fixas na ordem, cada bullet terminando com citação `U:…` que sustenta a frase. Nada do seu conhecimento de Ads. Não abra nenhum outro arquivo. gerado_por: opus-5, insumos_hash: PENDENTE. Responda só com: número de bullets por seção e as plataformas marcadas "Nada nas fontes".
```

Depois de cada lote: `validate_visoes.py --playbooks`; erro volta ao mesmo agente. `--selar` de cada playbook aprovado pelo validador.

- [ ] **Passo 3: gates e commit** (E9). Commit `conhecimento: playbooks por tarefa do Curso Subido`.

---

### Sessão 14: checklists, glossário, órfãs

**Arquivos:**
- Criar: `$B4/visoes/checklists/<plataforma>.md` (7: meta, google, google-search, youtube, google-display, ads-editor, tiktok; `geral` entra em todas), `$B4/visoes/glossario.md`, `$B4/visoes/orfas.md`
- Modificar: `$T4/pacote.py` (modo `glossario`: todas as unidades `conceito`), `$T4/tests/test_curso_subido_v2_visoes.py`

- [ ] **Passo 1: testes (falham primeiro)**

```python
    def test_checklists_glossario_e_orfas_existem_e_validam(self):
        for plat in ("meta", "google", "google-search", "youtube", "google-display", "ads-editor", "tiktok"):
            self.assertTrue((BASE / "visoes" / "checklists" / f"{plat}.md").exists(), plat)
        self.assertTrue((BASE / "visoes" / "glossario.md").exists())
        self.assertTrue((BASE / "visoes" / "orfas.md").exists())
        self.assertEqual(vv.validar_visoes(BASE), [])
        self.assertEqual(vv.validar_orfas(BASE), [], "órfãs acima de 15% ou sem motivo")
```

- [ ] **Passo 2: checklists** (Agent `opus` por plataforma, pacote `pacote.py plataforma <plat>`): perguntas de auditoria montadas de `regua`, `regra`, `decisao` e `alerta-ui`, cada pergunta com citação; formato em FORMATO §6. Prompt no molde do sintetizador, trocando o arquivo de saída por `visoes/checklists/<plat>.md`.

- [ ] **Passo 3: glossário** (um Agent `opus`, pacote `pacote.py glossario`): um verbete por termo, definição citando a unidade `conceito`; formato em FORMATO §6.

- [ ] **Passo 4: órfãs.** `validate_visoes.py --orfas` lista as unidades sem citação em playbook, checklist ou glossário (páginas de tema não contam). Se acima de 15% das unidades com `tarefas` não vazia, primeiro revisar os playbooks das tarefas mais órfãs (voltar ao prompt da Sessão 13 com a lista de unidades não citadas) antes de aceitar motivos. Depois, `pacote.py orfas` e um Agent `opus` escreve `visoes/orfas.md` com motivo da lista fechada por unidade (redundante com U:… | anedota sem ação | perecível sem valor | fora do escopo do gestor).

- [ ] **Passo 5: selar, gates e commit.** `--selar` de checklists, glossário e órfãs; E9. Commit `conhecimento: checklists, glossário e órfãs do Curso Subido`.

---

### Sessão 15: avaliação de uso completa

**Arquivos:**
- Modificar: `$B4/revisao/avaliacao/resultados-v1.md`, `resultados-v2.md` (os 7 casos de `casos.md`)

- [ ] **Passo 1:** conferir que `casos.md` está fechado (7 casos com Entrada, Esperado, Não pode aparecer, Aprovação). Não editar casos depois de começar.

- [ ] **Passo 2:** para cada caso, dois Agents `sonnet` em contextos separados, mesma pergunta:

```text
Você é um gestor de tráfego. Responda à situação abaixo usando SOMENTE os arquivos em <raiz permitida>. Liste no fim: arquivos abertos, e para cada recomendação a citação que a sustenta. Se a base não cobre, diga que não cobre.
Situação: <Entrada do caso>
```

Raiz v1: `$B3/memos/` mais `$B3/_index.md` (Jarvis 3.0, só leitura). Raiz v2: `$B4/visoes/` mais `$B4/unidades/`.

- [ ] **Passo 3:** avaliador na sessão (Fable) confere cada recomendação na fonte citada e preenche por caso: arquivos abertos, palavras lidas, decisões críticas certas e erradas, citações que sustentam, condições preservadas, lacunas reconhecidas, aprovado ou reprovado pelo critério do caso. Registrar nos dois arquivos de resultados.

- [ ] **Passo 4:** aceite: v2 acerta as decisões críticas de todos os casos e reconhece as lacunas dos casos de conflito e de ausência de cobertura. Se um caso reprovar na v2, corrigir o playbook responsável (Sessão 13, prompt, com o motivo) e rerodar só aquele caso. Commit `conhecimento: avaliação de uso completa v1 x v2 do Curso Subido`.

**CP5, Will decide:** 2 playbooks, 1 checklist e 1 página de tema escolhidos por ele, mais a tabela comparativa v1 × v2. Registrar em `tarefas.md`.

---

### Sessão 16: revisão final em amostra

- [ ] **Passo 1:** amostra conforme `revisao/amostra.md`, seção S8: 2 ouros + 2 aulas por módulo escolhidas por hash (menor e maior `aula_id`, pulando as já revisadas nas sessões 3 a 11) = 18 arquivos; 6 playbooks (1 por plataforma real, o de maior número de citações); 2 checklists (`meta`, `google-search`). Escrever a lista em `amostra.md`.

- [ ] **Passo 2:** unidades: inspetor e juiz com os prompts de E7. Playbooks e checklists: juiz direto, com as unidades citadas no contexto (o pacote `pacote.py tarefa`/`plataforma` serve) e a saída de `validate_visoes.py --playbooks`. `--selar` de cada laudo.

- [ ] **Passo 3:** aplicar E7 e a RUBRICA vigente: consolidar falhas materiais, corrigir só os itens afetados, atualizar derivados e conferir a correção. Ajustes menores ficam registrados. Recorrência comprovada pode ampliar a inspeção de forma delimitada; não há gatilho de reextração do módulo. Preservar o histórico e tratar divergências de avaliação antes de repetir trabalho.

- [ ] **Passo 4:** `status: revisado` nas aulas amostradas que passaram. Gates E9 mais `validate_visoes.py --orfas --consolidacao`. Teste em `test_curso_subido_v2_revisao.py`: todo laudo vivo `passa`, selado, e todo artefato da lista em `amostra.md` tem laudo. Commit `conhecimento: revisão final em amostra do Curso Subido`.

**CP6, Will decide:** laudos, mudanças do redator e derivados revistos. Registrar em `tarefas.md`.

---

### Sessão 17: fecho

- [ ] **Passo 1: endurecer os testes.** Em `test_curso_subido_v2_unidades.py`: 133 arquivos em `unidades/`, todos com `status` em {validado, revisado, ouro}, `MODULOS_FECHADOS` com os 8 módulos. Em `test_curso_subido_v2_visoes.py`: 40 playbooks, 7 checklists, glossário, órfãs, `desatualizadas` vazio. Em `test_curso_subido_v2_revisao.py`: amostra S8 completa com laudos `passa`. Sem `skipUnless`. Rodar: verde.

- [ ] **Passo 2: README e índices.** `$B4/README.md`: `status: vigente`, retirar "em construção", apontar para a frente como histórico. `historico.md`: entrada de fecho com contagens (unidades por tipo, órfãs, grupos por tipo). `$J4/biblioteca/README.md`: retirar "em construção por sessões".

- [ ] **Passo 3: Jarvis 3.0.** Na branch `main` do 3.0, um commit só com um arquivo novo `Conhecimento/Tráfego Pago/Curso Subido de Tráfego/SUBSTITUIDO.md` dizendo que a base vigente está no Jarvis 4 (`biblioteca/curso-subido-trafego/`), que os memos v1 são histórico, e citando o commit de fecho do Jarvis 4. Não mover nem apagar memos; os 21 testes v1 continuam verdes. Preflight do Bot Git do 3.0 (`bin/jarvis-git --operation push --effect non-production --json`) antes do push.

- [ ] **Passo 4: commit de fecho no Jarvis 4** `conhecimento: fecha a base atômica do Curso Subido (133 aulas, 40 playbooks)`. Frente: `README.md` com situação "concluída", `tarefas.md` fechado.

**CP7, Will decide:** aceita o fecho; se apaga a branch `task/curso-subido-v2-etapa-0` do 3.0 e se arquiva os memos v1 lá.

---

## Verificação global

- Toda sessão: os 4 comandos de início limpos ao começar e ao terminar.
- Extração: nenhuma aula com mais de 2 reexecuções sem `nota`; `proposta_tag` zero em módulo fechado; laudos amostrais `passa` e selados.
- Consolidação: `validate_visoes.py --consolidacao` limpo; 3 casos de calibração com o resultado esperado; grupos escalados decididos no CP4.
- Visões: 40 playbooks, 7 checklists, glossário, órfãs ≤ 15% com motivo; toda citação resolve para ID vivo; `desatualizadas.md` vazio.
- Avaliação de uso: 7 casos, v2 aprovada em todos, comparação com v1 registrada.
- Fecho: suíte endurecida verde; nada bruto na biblioteca; `indice.md` sem link para memos.

## Auto-revisão contra o spec

- Etapa 0 do spec: feita antes deste plano (estado de partida). Local muda de "mesma pasta no 3.0" para a biblioteca do Jarvis 4 por decisão de 2026-09-14; a substituição da v1 (S9 do spec) vira o `SUBSTITUIDO.md` da Sessão 17, sem mover memos.
- Etapa 1 (extração, CP2, CP3): Sessões 3 a 11 com o Procedimento E, `reconciliar.py` da Sessão 2, regra de parada e triagem de tags.
- Etapa 2 (consolidação, CP4): Sessão 12, incluindo os 3 casos de calibração e o papel do consolidador, que o spec não escrevia.
- Etapa 3 e 3b (visões, órfãs, avaliação, CP5): Sessões 13 a 15. O `pacote.py glossario` é novo.
- Etapa 4 (revisão final, CP6): Sessão 16.
- Etapa 5 (migração, CP7): Sessão 17, adaptada ao Jarvis 4.
- Fixtures fora da biblioteca e memos fora do Jarvis 4: decisão de 2026-09-14, aplicada na Sessão 1.
