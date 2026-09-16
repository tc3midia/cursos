---
type: laudo
aula_id: 1674fc3d8d94c601
arquivo: revisao/calibracao/f3.md
rodada: 0
veredito: falha
vetos: [fidelidade, perecibilidade]
isolamento: ok
gerado_por: fable-5.1
insumos_hash: b8ee235a685567dcb9bf499d1fe633ae2f932013a0a0242069fd559af6b4a44b
---

# Laudo — fixture f3

Julgado como arquivo real de unidades da aula 8.3 (43 unidades). Insumos: `papeis/juiz.md`,
`RUBRICA.md`, `FORMATO.md` §1–§2 e §8, o artefato e o pacote `fixture-f3.evidencia.md`. Nenhum
arquivo do pacote continha fonte bruta colada; transcrição, PDFs, memos, histórico e outros laudos
não foram abertos. Isolamento válido.

## Contrato

Validador não roda fora de `unidades/`; contrato conferido por leitura do FORMATO §1–§2 mais uma
checagem mecânica local (só violações impressas; retornou vazio).

- Front matter: todos os campos obrigatórios presentes (`status: rascunho`, `modulo "001"`,
  `ordem 12`, `aula_id` 16 hex igual ao arquivo, `fonte_commit f188775`, `fontes` com
  `transcricao.md` + dois PDFs, `retiradas/divisoes/fusoes` = `[]`). Campo `type` ignorado por
  instrução.
- Corpo: `# título`, `## Contexto da aula` com 5 linhas (faixa 3–8), `## Unidades`; sem timestamp,
  `[[`, "hoje"/"atualmente".
- Blocos: IDs `U:1674fc3d8d94c601:001..043` sem furo nem repetição; títulos ≤ 80 caracteres;
  `tipo`, `plataforma`, `tema`, `tarefas` dentro dos enums de `taxonomia.md`; `tarefas: []` só em
  `conceito` (001) e `limite` (043); `faixa` presente em todas as 37 unidades com `fala` e ausente
  nas 6 só-PDF (012–017); início < fim em todas; `fonte` no formato exigido e nomes de PDF
  presentes em `fontes`; `confianca: alta` em todas (nenhuma `baixa` sem nota).
- Regras por tipo: `procedimento` (006, 039) começam com `Pré-condição:` e têm lista numerada ≥ 2;
  `decisao` (022, 031) começam com `Se `/`Quando `; `exemplo` (004, 021, 029, 038, 041) têm as três
  marcas; `regua` (008, 014, 040) têm número; `fato-material` (012, 013, 016, 017) têm `fonte:
  pdf:`; corpo dentro do limite de linhas; nenhum `alerta-ui` no arquivo.
- Inspetor confirma: sem sequência de 25 palavras idêntica à fonte; `fontes` bate com o disco
  (legenda.srt e segmentos.json fora da regra); os dois PDFs listados são usados.

Veto 1: **passa**.

## Fidelidade

Contagem do pacote: 36 `lastreada`, 5 `desvio` (006, 014, 027, 038, 043), 2 `faixa-errada`
(007, 025), 0 `sem-lastro`. Todas as 43 unidades têm `confianca: alta`, portanto qualquer desvio
sustentado é veto.

Faixa-errada: 2 de 37 unidades com `faixa` = **5,4 %** (≤ 10 %) — não veta por si.

Leitura crítica de cada item, com a evidência do próprio inspetor:

- **006 (desvio) — não sustentado como veto.** O inspetor mostra que a palavra pesquisada foi
  "Limpeza de ar" e que "limpeza de ar-condicionado" foi o nome dado ao arquivo salvo. A unidade
  inverte os dois nos exemplos (`ex.:` do passo 2 e do passo 3), mas nenhum número, condição ou
  sentido do procedimento muda: pesquisar palavra do nicho, refinar se vier resultado fora do tema
  (coerente com os 2.300 resultados), salvar com nome sequencial. Registro para o redator corrigir
  o exemplo; não conta como desvio de fidelidade.
- **014 (desvio) — sustentado.** O PDF, na citação do inspetor, impõe os 15 % (250 px) "na parte
  superior e inferior da imagem" e nomeia apenas banners de stories. A unidade afirma "Em banner e
  vídeo de stories e reels" e intitula "stories e reels": amplia o escopo da regra (condição de
  aplicação) para reels e para vídeo sem lastro na fonte. Extensão por conhecimento externo com
  `confianca: alta` e sem `nota` ⇒ desvio de condição ⇒ veto.
- **027 (desvio) — sustentado, peso menor.** A evidência ("E eu juro que isso não está no meu
  roteiro aqui") é comentário sobre uma improvisação pontual; a unidade converte em regra geral
  ("não precisa estar no roteiro para funcionar") e acrescenta "a história nasce de anos de
  referência", que o pacote não lastreia. Generalização de sentido com `confianca: alta`; sozinha
  seria discutível, mas cai na mesma correção.
- **038 (desvio) — sustentado.** O inspetor mostra que a fala corta em "você não vai adivinhar o
  que aconteceu" e que o desfecho "mudou de patamar ao migrar para o gerenciador" não é dito. A
  unidade inventa o resultado da história do cliente de R$ 50 mil/mês. Fato sem fonte com
  `confianca: alta` ⇒ veto (na prática, trecho sem-lastro dentro de uma unidade).
- **043 (desvio) — não sustentado como veto.** É unidade `limite`, cujo papel é dizer o que a aula
  não cobre; "não ensina a editar vídeo" é declaração de ausência, não afirmação atribuída à fonte.
  O rótulo "(9.0)" para a aula seguinte não está na fala nem nos PDFs (a fala fala só em "próxima
  aula" com ChatGPT), mas é metadado de estrutura do curso, verificável no manifest, não número da
  aula. Registro: redator confirma o rótulo no manifest ou remove o parêntese (no corpo e no
  Contexto da aula).
- **007 (faixa-errada) — sustentado.** A faixa 00:07:08–00:07:46 só contém "plágio, crime"; a
  frase sobre modelar o manual de criativos está em 00:15:02–00:15:43. Corrigir a faixa (ou
  dividir a unidade). Não veta pelo percentual.
- **025 (faixa-errada) — sustentado.** A transição "se a resposta for sim, tenho um convite" está
  em 00:30:24–00:30:39, fora da faixa 00:23:04–00:24:52. Corrigir a faixa. Não veta pelo percentual.

Veto 2: **falha** (014 e 038; 027 acompanha).

## Cobertura

Duas omissões listadas pelo inspetor, ambas encontradas por ele no PDF-resumo da aula:

- Filtro de localização no Ads Transparency Center (U:009 cita formato, tópico e anunciante/site,
  não localização). É opção de filtro de ferramenta, não número, passo de procedimento nem
  condição: omissão de contexto ⇒ registro.
- Caminho "aba materiais" para baixar o manual de criativos. É navegação na plataforma do curso,
  sem ação do gestor em Ads: omissão de contexto ⇒ registro.

O pacote confirma que as unidades `fato-material` cobrem todos os números e regras textuais do
manual de criativos e que o PDF-resumo não traz número próprio além disso. Nenhuma omissão de
número, passo ou condição.

Veto 3: **passa** (com dois registros).

## Perecibilidade

- **U:006** — procedimento com caminho de clique na Biblioteca de Anúncios do Meta ("selecione o
  país e a categoria", "botão direito", "salvar imagem como", "salvar vídeo como") com
  `perecivel: false` ⇒ veto.
- **U:009** — descrição de filtros e botão "ver todos os anúncios" no Ads Transparency Center do
  Google com `perecivel: false` ⇒ veto.
- Conferência própria: 012–016 e 032 (botão "Saiba mais") estão com `perecivel: true`, correto.
  U:033 cita "clica em saiba mais e se cadastra" como texto de copy, não como descrição de tela;
  U:038 cita "botão impulsionar versus gerenciador" como tópico de roteiro. Registro para o redator
  avaliar, sem veto.

Veto 4: **falha** (006 e 009).

## Falhas

- F3-01 — fidelidade — U:1674fc3d8d94c601:014: regra dos 15 % ampliada para reels e vídeo; o PDF
  só cobre banner de stories. Restringir ao que a fonte diz ou baixar confiança com nota.
- F3-02 — fidelidade — U:1674fc3d8d94c601:038: desfecho "mudou de patamar ao migrar para o
  gerenciador" não está na fala. Remover ou reescrever o "O que aconteceu" até onde a fonte vai.
- F3-03 — fidelidade — U:1674fc3d8d94c601:027: "não precisa estar no roteiro para funcionar" e "a
  história nasce de anos de referência" generalizam comentário pontual. Reescrever ou baixar
  confiança com nota.
- F3-04 — perecibilidade — U:1674fc3d8d94c601:006: caminho de clique com `perecivel: false`;
  trocar para `true`.
- F3-05 — perecibilidade — U:1674fc3d8d94c601:009: filtros e botão de tela com
  `perecivel: false`; trocar para `true`.
- F3-06 — registro (faixa) — U:1674fc3d8d94c601:007: faixa não cobre a frase sobre modelar o
  manual (00:15:02–00:15:43).
- F3-07 — registro (faixa) — U:1674fc3d8d94c601:025: faixa não cobre a transição do convite
  (00:30:24–00:30:39).
- F3-08 — registro — U:1674fc3d8d94c601:006: exemplos de palavra pesquisada e nome de arquivo
  invertidos em relação à fonte.
- F3-09 — registro — U:1674fc3d8d94c601:043 e Contexto da aula: rótulo "(9.0)" sem lastro na fonte;
  confirmar no manifest ou remover.
- F3-10 — registro (cobertura) — filtro de localização do Ads Transparency Center ausente em U:009.
- F3-11 — registro (cobertura) — caminho "aba materiais" para o manual de criativos sem unidade.

## Próximo

redator
