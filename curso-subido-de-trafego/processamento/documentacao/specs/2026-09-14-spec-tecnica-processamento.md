# Spec técnica: processamento das aulas do Curso Subido

Data: 2026-09-14. Autor: Claude (Fable 5.1), a pedido do Will. Status: descrição do processo vigente, escrita para permitir a execução de sessões de extração no Codex. Não altera contratos nem decisões da frente.

Leitor: quem vai rodar sessões do [plano](../planos/2026-09-14-plano-de-sessoes.md) em outro runtime e com outros modelos. Esta spec explica o que o processo exige de cada peça, para que a adaptação preserve as garantias. O plano continua sendo a sequência oficial; os contratos vivos são `FORMATO.md`, `taxonomia.md` e `revisao/RUBRICA.md` na biblioteca.

## 1. O que o processo produz

Objetivo: transformar as 133 aulas do curso em conhecimento operável por agente, em duas camadas.

- **Camada 1, unidades.** Um arquivo Markdown por aula em `biblioteca/curso-subido-trafego/unidades/<slug>.md`. Cada arquivo tem front matter YAML, uma seção de contexto e blocos de unidades. Cada unidade é uma orientação distinta do professor, com ID fixo `U:<aula_id>:<nnn>`, metadados fechados e corpo de 1 a 8 linhas. É a verdade auditável.
- **Camada 2, visões.** Playbooks por tarefa, checklists por plataforma, glossário, páginas de tema e consolidação. Só existem por citação: toda frase termina com um `U:…` que a sustenta. Sem citação, não é conhecimento do curso.

Duas garantias amarram as camadas. Cada unidade tem um hash do conteúdo semântico e uma `versao` que sobe a cada mudança. Cada derivado guarda um `insumos_hash` das unidades que cita; o arquivo `_gerado/desatualizadas.md` lista os derivados cujo hash não bate mais. Ele vazio é gate de qualquer commit.

Estado em 14/09/2026: módulos 001 e 003 extraídos, validados e commitados, mais o ouro do módulo 005. Faltam 107 aulas. Próxima sessão é a 5, módulo 002, aulas 1 a 18. Ordem restante: 002, 004, 006, 007, 005, 008. Estado por sessão em tarefas.md (registro no Jarvis 4: `projetos/tc3/frentes/curso-subido-base-atomica/tarefas.md`).

## 2. Fontes

Clone local somente leitura: `~/curso-subido-trafego-transcricoes`, repo `tc3midia/curso-subido-trafego-transcricoes`, commit `f188775`. A variável de ambiente `CURSO_SUBIDO_CLONE` sobrescreve o caminho. Nenhuma fonte bruta é copiada para a biblioteca.

- `manifest.jsonl`: uma linha por aula. Campos usados: `id` (16 hex, o `aula_id`), `ordem`, `modulo`, `aula` (título), `duracao_segundos`, `saida_relativa` (pasta da aula).
- Pasta da aula: `transcricao.md` (front matter com título, módulo, duração e modelo de transcrição; corpo em segmentos `**[hh:mm:ss–hh:mm:ss]**` seguidos do texto), `legenda.srt`, `segmentos.json` e, quando existem, PDFs e txt do material da aula.
- PDFs viram texto por `pdftotext -layout`, esperado em `/opt/homebrew/bin` ou no PATH.

O `slug` do arquivo de unidades é `<modulo 3 dígitos>-<slug do título>`, derivado do manifest pela biblioteca `unidades.py`, com tabela de exceções para títulos encurtados.

## 3. Ferramentas

Tudo em `ferramentas/curso-subido/`, Python 3 e biblioteca padrão, sem dependências. Todos os scripts aceitam `--root` (padrão: a biblioteca) e `--revisao` (padrão `revisao`). Detalhe de uso no [README da ferramenta](../../README.md).

| Script | Função no processo |
|---|---|
| `unidades.py` | Biblioteca: manifest, parser do formato, hash, taxonomia, citações. Importada pelos outros. |
| `pacote.py` | Monta o pacote de contexto de cada papel e lista aulas pendentes. É o único ponto de contato entre a fonte bruta e os modelos. |
| `validate_unidades.py` | Aplica todas as regras marcadas [E] e [W] do `FORMATO.md` §1 a §4 aos arquivos de unidades. Exit 1 com erro. `--json` dá a saída que o juiz recebe. `--sem-fontes` pula a comparação com transcrição e PDF. |
| `build_indices.py` | Gera `_gerado/` (`unidades.jsonl`, `cobertura.jsonl`, `propostas_tags.md`, `desatualizadas.md`), `visoes/temas/` e `indice.md`. `--check` compara com o disco. |
| `validate_visoes.py` | Valida playbooks, checklists, glossário, consolidação e órfãs; `--desatualizadas` recalcula a lista; `--selar ARQ…` grava o `insumos_hash` de laudos e visões. |
| `reconciliar.py` | Junta uma reextração completa ao arquivo existente preservando IDs, registrando retiradas, divisões e fusões. |

Testes: `python3 -m unittest discover -s ferramentas/curso-subido/tests -p 'test_curso_subido_*.py'`. Em 14/09/2026 a suíte tem 74 testes e passa. A pasta `tests/calibracao/` guarda fixtures com defeito plantado e nunca entra em pacote de extração.

## 4. Papéis, isolamento e modelos

O processo separa cinco papéis. O que cada um pode ler é a garantia central; o modelo é escolha por papel.

| Papel | Lê | Não lê | Escreve | Modelo no Claude Code |
|---|---|---|---|---|
| Extrator | Só o pacote de extração | Memos v1, outras aulas, laudos, playbooks, internet | `unidades/<slug>.md` completo | Opus 5 em todas as aulas, decisão do CP2 |
| Inspetor | Só o pacote de inspeção, que inclui a fonte bruta | Laudos anteriores, outras aulas, visões | `revisao/laudos/<aula_id>.evidencia.md` | Sonnet 5 |
| Juiz | Arquivo julgado, RUBRICA, evidência do inspetor, saída do validador | Transcrição, PDF, clone, memos, outros laudos | `revisao/laudos/<aula_id>.md` | Fable 5.1, contexto fresco |
| Redator | Artefato reprovado, seção Falhas do laudo, evidência, fonte no clone | Memos, outras aulas, outras visões | Corrige só o listado, `versao` sobe | Opus 5 |
| Sessão | Tudo | | Orquestra, roda gates, triagem de tags, correções manuais, commit | Fable 5.1, a conversa |

Regras que não dependem do runtime:

- O juiz nunca vê fonte bruta. Se viu, o laudo é inválido e se refaz em outro contexto. É o que impede o juiz de "completar" a aula com o próprio conhecimento.
- Extrator e inspetor recebem um único arquivo, o pacote, e não abrem mais nada. O pacote é montado pelo script, não pela sessão.
- Todo artefato gerado por modelo declara `gerado_por`. O validador aceita apenas `sonnet-5`, `opus-5` e `fable-5.1`, enum em `FORMATO.md` §1 e em `GERADO_POR` de `unidades.py`. Ver a seção 9 sobre outros modelos.
- Haiku em nenhum papel. Nenhum papel lê os memos v1 do Jarvis 3.0.
- O papel completo de cada um está em `biblioteca/curso-subido-trafego/revisao/papeis/`. Os papéis não entram no `insumos_hash`, então podem ganhar lições sem desatualizar derivados.

## 5. Pacotes: o que cada modelo recebe

`pacote.py <modo> <aula_id|slug> --saida DIR` grava o pacote e imprime caminho e contagem de palavras. Pacotes só podem ficar em `_saida/tc3/<trabalho>/temporarios/`, fora do git. Trabalho vigente: `_saida/tc3/2026-09-14-curso-subido-base-atomica/temporarios/`.

**Extração** (`extracao`): papel do extrator; `FORMATO.md` §1 a §4; `taxonomia.md` inteira; 6 unidades do ouro 001-8-3 como âncora de granularidade, uma por tipo; cabeçalho YAML já preenchido a partir do manifest; transcrição sem front matter; PDFs e txt em texto. A parte fixa soma cerca de 3.800 palavras. A parte da aula variou de 1.400 a 10.500 palavras no módulo 001. Estimativa de consumo no Claude, Sessão 3: 72 mil a 152 mil tokens por aula.

**Reextração** (`reextracao`): o mesmo, mais a lista das unidades existentes com ID e corpo, para preservar IDs.

**Correção pontual** (`correcao --unidades U:x:007,U:x:021 --erros "<saída do validador>"`): papel, `FORMATO.md` §1 a §4, front matter atual, só os blocos apontados, janela da transcrição de cada faixa com 60 segundos de folga (unidade sem faixa usa as vizinhas), PDFs citados na `fonte`, e os erros. Muito menor que o pacote de extração.

**Inspeção** (`inspecao`): papel do inspetor, `RUBRICA.md`, `FORMATO.md` §8, o arquivo de unidades sob inspeção, transcrição e PDFs em texto.

O juiz não tem pacote. Recebe caminhos: papel, rubrica, arquivo julgado, evidência do inspetor, e a saída de `validate_unidades.py --arquivo <slug> --json` colada no prompt.

`pacote.py pendentes [--modulo 00X]` lista as aulas sem arquivo em `unidades/`, com contagem de palavras.

## 6. Contrato de saída do extrator

O que o validador cobra, resumido. A regra completa está em `FORMATO.md` §1 a §4.

- Front matter com `type: unidades-aula`, `status: rascunho`, título, módulo, ordem e `aula_id` iguais ao manifest, `fontes` com `transcricao.md` e os nomes exatos dos PDFs usados, `extraido_em`, `gerado_por`, e as listas `retiradas`, `divisoes`, `fusoes`.
- Corpo com `## Contexto da aula` em 3 a 8 linhas e `## Unidades`.
- Cada unidade: cabeçalho `### U:<aula_id>:<nnn> — <título até 80 caracteres>`, bloco YAML com `tipo`, `plataforma`, `tema`, `tarefas`, `fonte`, `faixa`, `perecivel`, `confianca`, `versao`, e corpo de 1 a 8 linhas (15 para procedimento e exemplo).
- Enums fechados de `taxonomia.md`. Tag nova só por `proposta_tag`.
- `faixa` obrigatória quando a fonte inclui fala, dentro da duração da aula, cobrindo o trecho inteiro que sustenta a unidade.
- Corpo sem timestamp, sem `[[`, sem "hoje" ou "atualmente", sem 25 palavras seguidas copiadas da fonte.
- Regras por tipo: régua tem número; procedimento começa com `Pré-condição:` e lista numerada; decisão começa com `Se` ou `Quando`; exemplo tem `Situação:`, `O que aconteceu:`, `Lógica:`; descrição de tela em qualquer tipo exige `perecivel: true`.
- IDs sequenciais pela ordem de aparição. Nunca renumerar nem reutilizar número. Presentes mais retiradas formam `001..max` sem furo.
- Faixa esperada de 3 a 60 unidades por aula. Fora disso é aviso, não erro.

## 7. Procedimento por módulo

É o Procedimento E do plano, resumido. Cada passo tem comando ou prompt no plano.

1. **Início da sessão.** Working tree limpo nos caminhos da frente, clone em `f188775`, `build_indices.py --check`, `validate_visoes.py --desatualizadas` e testes verdes. Ler `tarefas.md` para saber a sessão e se há checkpoint pendente.
2. **Pendentes.** `pacote.py pendentes --modulo $MOD`.
3. **Pacotes do lote.** 6 a 8 aulas por lote, um pacote de extração por aula.
4. **Extração.** Um agente por aula, contexto próprio, lendo só o pacote e escrevendo `unidades/<slug>.md`. No Claude Code rodam em paralelo em background; rodar em série é válido, só mais lento. Resposta esperada: contagem por tipo, `proposta_tag` e `confianca: baixa`.
5. **Validação e correção.** `validate_unidades.py --modulo $MOD`. Erro mecânico (contexto longo, título longo, forma): a sessão corrige direto, com `nota` e `versao` subindo. Erro de conteúdo (régua sem número, cópia bruta, faixa errada, estrutura do tipo): pacote de correção e agente extrator, no máximo 2 vezes por aula; depois, correção manual da sessão. Reextração completa só quando o arquivo inteiro está ruim, e sobre aula já commitada passa por `reconciliar.py`.
6. **Repetir** até o módulo, ou a metade prevista, ficar sem pendentes.
7. **Gate do módulo.** Validador limpo, `build_indices.py`, triagem de `propostas_tags.md` na sessão: aceitar significa editar `taxonomia.md` e trocar a tag nas unidades; recusar significa manter a tag mais próxima com `nota`. Mudança em `taxonomia.md` desatualiza todos os derivados vivos, que precisam de `--selar`. Meta: zero `proposta_tag` no módulo fechado.
8. **Revisão amostral.** Aulas escolhidas pelo `aula_id` ordenado, pulando ouros; quantidade por sessão na tabela do plano. Para cada aula: inspetor com pacote de inspeção, depois juiz em contexto fresco. Regra de parada: falha de fidelidade ou cobertura amostra mais 2 aulas; 2 de 4 falhando significa corrigir o papel do extrator e reextrair o módulo. Caso contrário, redator só nas falhas listadas, novo validador, `build_indices.py`, novo juiz, no máximo 2 rodadas; laudo anterior renomeado para `<aula_id>.rodada-N.md`. Laudo final selado com `validate_visoes.py --selar`.
9. **Fechar o módulo.** `status: rascunho` vira `validado` nas aulas do módulo, exceto ouro. Acrescentar o módulo em `MODULOS_FECHADOS` no teste `test_curso_subido_v2_unidades.py`. Aulas por módulo: 001 = 18, 002 = 36, 003 = 7, 004 = 15, 005 = 28, 006 = 8, 007 = 7, 008 = 14.
10. **Gates e commit.** Validador, `build_indices.py` e `--check`, `validate_visoes.py --playbooks --desatualizadas`, testes. `git add` só de `biblioteca/curso-subido-trafego`, `ferramentas/curso-subido/tests` e a pasta da frente. Mensagem indicada na tabela de sessões. Atualizar a linha da sessão em `tarefas.md` e uma entrada em `historico.md`. Se a sessão termina em checkpoint, escrever o que Will decide e parar.

Checkpoints pendentes: CP3 no fim da Sessão 11 (estatísticas por tipo, plataforma e tarefa; tags; laudos por módulo). CP2 já foi decidido: extrator segue Opus, Sonnet reavaliado depois.

## 8. Revisão: cinco vetos, sem nota

`RUBRICA.md` define cinco vetos. Um veto é `falha`; ouro reprovado é `bloqueado`.

1. Contrato: validador com zero erros; sem cópia bruta; `fontes` bate com o disco. Quem mede é o script.
2. Fidelidade: cada unidade é `lastreada`, `desvio`, `sem-lastro` ou `faixa-errada` na evidência do inspetor. Qualquer `sem-lastro` reprova. Desvio com `confianca: alta` reprova. Faixa errada em mais de 10% reprova.
3. Cobertura: todo número, régua, passo, decisão condicional e alerta de tela da fonte tem unidade. Omissão de número, passo ou condição reprova.
4. Perecibilidade: tela sem `perecivel: true` reprova.
5. Aplicabilidade: só para playbooks.

O juiz confere no corpo das unidades e na evidência. Por isso a evidência do inspetor precisa citar trecho curto da fonte para cada veredito. O redator só corrige o que a seção Falhas lista; unidade sem lastro é retirada, não reescrita.

## 9. Adaptação ao Codex e a outros modelos

O que precisa existir no runtime, em ordem de importância:

- **Contexto isolado por papel.** Cada extrator, inspetor e juiz precisa de um contexto que só contenha o que o papel pode ler. Se o Codex oferecer subagentes com contexto próprio, usar isso. Se não oferecer, rodar cada papel como invocação separada do CLI, com um prompt que aponta o pacote ou os arquivos permitidos. O juiz nunca pode rodar na mesma conversa em que a transcrição foi aberta.
- **Janela de contexto do extrator.** O pacote de extração vai de cerca de 5 mil a 15 mil palavras, e o modelo escreve de 3 a 60 unidades. Estimativa no Claude de 72 mil a 152 mil tokens por aula, entrada e saída. Modelo com janela menor que isso não serve para as aulas grandes. `pacote.py extracao` imprime as palavras da aula; usar essa contagem para escolher o modelo por aula, como o plano previa com a régua de 8.000 palavras.
- **Escrita em arquivo.** Extrator, inspetor, juiz e redator escrevem um arquivo no caminho indicado. Se o runtime só devolve texto, a sessão grava o texto no caminho e confere que o arquivo começa com `---`.
- **Acesso ao clone e ao pdftotext.** `pacote.py` lê `~/curso-subido-trafego-transcricoes` e chama `pdftotext`. O sandbox precisa permitir leitura fora do repositório e execução do binário. Escrita só dentro do repositório, em `biblioteca/`, `ferramentas/curso-subido/tests`, a pasta da frente e `_saida/`.
- **`gerado_por` com outro modelo.** O enum fechado hoje não aceita nenhum modelo fora da família Claude. Um artefato com outro valor falha no validador. Há dois caminhos, e a escolha é do Will:
  - Ampliar o enum em `FORMATO.md` §1 e em `GERADO_POR` de `unidades.py`, com um teste. Como o hash de `FORMATO.md` entra no `insumos_hash` de todo derivado, isso desatualiza todos os laudos e visões vivos, que precisam de `validate_visoes.py --selar` em um commit próprio de ferramenta, antes de qualquer extração. É o caminho honesto: o metadado diz quem gerou.
  - Manter o enum e registrar o modelo real em `nota` do front matter e em `tarefas.md`. Evita mexer no FORMATO, mas deixa `gerado_por` falso. Não recomendo.
- **Escolha de modelo por papel.** A spec não nomeia modelos do Codex. O critério por papel: extrator precisa de janela longa, obediência estrita a formato e fidelidade sem completar com conhecimento próprio; juiz precisa do modelo mais forte em raciocínio disponível, porque decide sem ver a fonte; inspetor precisa de janela longa e cuidado com números e condições; redator pode ser o mesmo nível do extrator. Registrar a escolha em `tarefas.md` na linha da sessão, como o plano já pede para sessão fora do Fable.
- **Commit.** O plano manda `Co-Authored-By` com o modelo real da conversa. Sessão no Codex usa o autor correspondente.
- **Paralelismo.** Opcional. O que importa é que cada aula tenha seu contexto. Uma sessão do Claude perdeu 10 extrações numa queda com 11 agentes simultâneos; lotes menores são mais seguros.

Prompts de cada papel estão no Procedimento E do plano e servem em qualquer runtime, trocando o caminho do pacote e o valor de `gerado_por`.

## 10. O que não muda ao trocar de runtime

- Os contratos: `FORMATO.md`, `taxonomia.md`, `RUBRICA.md` e os papéis. Mudança neles é decisão registrada, não adaptação.
- Os gates de commit e a regra de `desatualizadas.md` vazio.
- A ordem dos módulos e os checkpoints. Nenhum checkpoint é atravessado sem decisão do Will em `tarefas.md`.
- Uma sessão no Codex e uma no Claude não podem rodar sobre o mesmo módulo ao mesmo tempo. A frente tem uma única branch e um único `tarefas.md`.
- Pacotes e rascunhos ficam fora do git. Fonte bruta não entra na biblioteca.

## 11. Verificação rápida antes de começar uma sessão no Codex

```bash
J4="/Users/wilianrafaelribeiro/Jarvis 4"; cd "$J4"
git status --short -- biblioteca/curso-subido-trafego ferramentas/curso-subido projetos/tc3/frentes/curso-subido-base-atomica
git -C ~/curso-subido-trafego-transcricoes rev-parse --short=7 HEAD
which pdftotext || ls /opt/homebrew/bin/pdftotext
python3 ferramentas/curso-subido/build_indices.py --check
python3 ferramentas/curso-subido/validate_visoes.py --desatualizadas
python3 -m unittest discover -s ferramentas/curso-subido/tests -p 'test_curso_subido_*.py'
python3 ferramentas/curso-subido/pacote.py pendentes --modulo 002
```

Os quatro comandos de gate precisam estar limpos, o clone em `f188775`, e a lista de pendentes precisa bater com a sessão indicada em `tarefas.md`. Só então montar o primeiro pacote.
