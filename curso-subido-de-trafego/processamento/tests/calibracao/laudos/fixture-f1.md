---
type: laudo
aula_id: 1674fc3d8d94c601
arquivo: revisao/calibracao/f1.md
rodada: 0
veredito: falha
vetos: [fidelidade]
isolamento: ok
gerado_por: fable-5.1
insumos_hash: 36bb80162a1d8b0d2430ee37147d30d51e1d834329db81a56b83ef43a8210b8f
---

# Laudo — fixture f1

Julgado como arquivo real de unidades da aula 8.3 (43 unidades, `status: rascunho`). Insumos: o
artefato, `RUBRICA.md`, `FORMATO.md` §1–§2 e §8, e o pacote `fixture-f1.evidencia.md`. Nenhuma
fonte bruta foi aberta; as citações do pacote são trechos curtos de evidência, não fonte colada.

## Contrato

Validador não roda fora de `unidades/`; contrato conferido por leitura contra FORMATO §1–§2 e por
checagem mecânica dos enums de `taxonomia.md`.

- Front matter: todos os campos obrigatórios presentes e válidos (`aula_id` 16 hex igual ao
  esperado, `fonte_commit` f188775, `fontes` com transcrição + dois PDFs, `retiradas`/`divisoes`/
  `fusoes` vazios). `type: fixture-calibracao` ignorado por instrução.
- Corpo: `## Contexto da aula` com 5 linhas (faixa 3–8), sem timestamp, `[[` ou "hoje"/"atualmente";
  `## Unidades` na ordem certa.
- Blocos: 43, IDs 001–043 contíguos e únicos; títulos ≤ 80 caracteres; `tipo`, `plataforma`, `tema`
  e `tarefas` todos dentro dos enums da taxonomia; `tarefas: []` só em `conceito` (001) e `limite`
  (043).
- `faixa`: presente nas 37 unidades com `fala`, ausente nas 6 só-PDF (012–017); início < fim em
  todas. Fim ≤ duração não conferido (manifest fora dos insumos); a maior faixa termina em 00:40:25,
  coerente com a última fala citada pelo inspetor.
- Regras por tipo: `procedimento` (006, 039) começam com `Pré-condição:` e têm lista numerada;
  `decisao` (022, 031) começam com `Se `/`Quando `; `exemplo` (004, 021, 029, 038, 041) têm as três
  marcas; `regua` (008, 014, 040) têm número; `alerta-ui` (009) é `perecivel: true`;
  `fato-material` (012, 013, 016, 017) têm `fonte: pdf:`; nenhuma `confianca: baixa`.
- Corpo dos blocos: 1–8 linhas (até 15 em procedimento/exemplo), sem timestamp, `[[`, `**[` nem
  "hoje"/"atualmente"/"neste momento".
- Inspetor: nenhuma sequência de 25 palavras copiada; `fontes` bate com o disco; nenhum PDF do disco
  ficou de fora.

Contrato: **passa**.

## Fidelidade

Contagem do pacote: 38 `lastreada`, 2 `desvio` (008, 040), 2 `faixa-errada` (007, 025), 1
`sem-lastro` (043). Unidades com `faixa`: 37; faixa-errada = 2/37 = **5,4 %** (≤ 10 %, não veta).

Leitura crítica de cada item não lastreado:

- **U:008 — desvio, confiança alta.** O inspetor cita fala ("Toda semana procure de 3 a 5
  anúncios. Não estou falando para você procurar 50", 00:11:28–00:12:05; "150, 200 anúncios" por
  ano, 00:12:05–00:12:47) e PDF ("colete de 3 a 5 anúncios por semana pelo menos"). O corpo da
  unidade diz "8 a 10 por semana", "mais de 500 referências" no ano e ainda atribui ao PDF "8 a 10
  por semana é o mínimo". A evidência citada é numérica e explícita nas duas fontes; o próprio
  título da unidade ("3 a 5 anúncios por semana") contradiz o corpo, o que corrobora o inspetor.
  Número diferente da fonte com `confianca: alta` ⇒ **veta**. A afirmação "o ideal é coletar todos
  os dias" atribuída ao PDF não aparece na citação do inspetor; fica registrada para o redator
  conferir ao corrigir.
- **U:040 — desvio, confiança alta.** O inspetor cita "Eu não entro num evento online sem pelo
  menos 60. 60 anúncios gravados... a gente sempre grava 120, 150 anúncios diferentes"
  (00:37:35–00:38:59). O corpo diz "menos de 20 anúncios gravados" e "40 vídeos diferentes"; o
  título diz "60 no mínimo". A evidência sustenta: os números do corpo não existem na fonte e o
  título contradiz o corpo. Régua com número trocado e `confianca: alta` ⇒ **veta**.
- **U:043 — sem-lastro.** O inspetor cita a fala ("Na próxima aula a gente vai entrar aqui no chat
  EPT", 00:40:08–00:40:25) e o PDF ("no próximo material nós vamos aprender como usar o ChatGPT") e
  afirma que nenhuma fonte numera a aula seguinte como "9.0". Leitura: o que a aula não ensina e o
  ponteiro para ChatGPT estão lastreados; a numeração "9.0" é um fato específico que nenhuma das
  três `fontes` contém e que a unidade afirma com `confianca: alta`. A rubrica não abre exceção
  para fragmento sem lastro dentro de unidade majoritariamente lastreada; o inspetor classificou a
  unidade como `sem-lastro` e a evidência sustenta a classificação. Qualquer sem-lastro ⇒ **veta**.
  Correção é trivial (retirar "(9.0)" ou lastrear no manifest via `nota`). O mesmo "(9.0)" aparece
  na linha 5 do `Contexto da aula`; não é unidade, mas deve sair junto.
- **U:007 — faixa-errada.** Inspetor: a parte sobre modelar os exemplos do manual está em
  00:15:02–00:15:43, fora de 00:07:08–00:07:46; a parte sobre plágio está dentro. A evidência
  sustenta a classificação (conteúdo existe na fonte, faixa incompleta). Registro; não veta.
- **U:025 — faixa-errada.** Inspetor: a transição "se a resposta for sim, tenho um convite" está em
  00:29:48–00:30:24, fora de 00:23:04–00:24:52; o gancho de dor/desejo está dentro. A evidência
  sustenta. Registro; não veta.

Fidelidade: **falha** (008, 040, 043).

## Cobertura

Duas omissões listadas pelo inspetor:

1. Contagens de resultado da busca na Biblioteca de Anúncios ("29 mil", "2.300"). São números de
   uma demonstração ao vivo, não parâmetro, régua nem passo que um agente usaria; o próprio
   inspetor os chama de anedóticos. Anedota sem ação não conta como omissão. Registro.
2. Ponteiro do PDF para a aba "materiais" da plataforma do curso. É navegação do ambiente do
   curso, não passo de tarefa de tráfego. Omissão de contexto. Registro.

Nenhum número, passo ou condição da fonte apontado como ausente. Cobertura: **passa**.

## Perecibilidade

Inspetor: todas as unidades que descrevem tela, menu, botão ou caminho de clique (006, 009, 012,
013, 014, 015, 016, 032) estão `perecivel: true`. Conferido no artefato. As demais com
`perecivel: false` que mencionam elementos de plataforma (011 formatos por posicionamento, 018
recursos orgânicos, 033 e 038 texto de roteiro/exemplo) não descrevem UI nem caminho de clique.
Perecibilidade: **passa**.

## Falhas

- F1-01 — U:1674fc3d8d94c601:008 — desvio numérico com confiança alta: corpo diz "8 a 10 por semana" e "mais de 500"; fonte diz 3 a 5 por semana e 150–200 no ano; título já traz "3 a 5". Corrigir corpo pela fonte e conferir a atribuição "ideal é todos os dias" ao PDF.
- F1-02 — U:1674fc3d8d94c601:040 — desvio numérico com confiança alta: corpo diz "menos de 20" e "40 vídeos"; fonte diz pelo menos 60 e 120–150; título já traz "60". Corrigir corpo pela fonte.
- F1-03 — U:1674fc3d8d94c601:043 — sem-lastro: numeração "9.0" da aula seguinte não existe em nenhuma das três fontes. Retirar "(9.0)" (também da linha 5 do Contexto da aula) ou lastrear com `nota` apontando o manifest.

Registros (não vetam, não exigem correção nesta rodada): U:007 e U:025 faixa incompleta (5,4 % das
unidades com faixa); omissões 1 e 2 do inspetor são anedota/contexto.

## Próximo

redator
