---
type: laudo
aula_id: 1674fc3d8d94c601
arquivo: revisao/calibracao/f2.md
rodada: 0
veredito: falha
vetos: [fidelidade, cobertura]
isolamento: ok
gerado_por: fable-5.1
insumos_hash: 47bab08158b646c6c80c762a3785addc8b5161655eef23a162f950864dc16496
---

# Laudo — fixture f2

Julgado como arquivo real de unidades da aula 8.3 (43 unidades, `status: rascunho`). Insumos: papel do juiz, RUBRICA, FORMATO §1–§2 e §8, o artefato e o pacote do inspetor `fixture-f2.evidencia.md`. Nenhuma fonte bruta entrou no contexto; o pacote traz só citações curtas na coluna de evidência, que é o formato previsto em FORMATO §8. Isolamento válido.

## Contrato

O validador não roda fora de `unidades/`; conferi manualmente contra FORMATO §1–§2.

- Front matter: todos os campos obrigatórios presentes e no domínio (`status`, `title`, `modulo "001"`, `ordem 12`, `aula_id` 16 hex igual ao nome lógico, `account_id`, `promoted_by`, `fonte_repo`, `fonte_commit f188775`, `fontes` com transcrição + dois PDFs, `extraido_em`, `gerado_por fable-5.1`, `retiradas/divisoes/fusoes` = `[]`).
- Corpo: `## Contexto da aula` com 5 linhas (faixa 3–8), sem timestamp, `[[` ou "hoje/atualmente"; `## Unidades` em seguida.
- Identidade: IDs `001`–`043` contínuos, sem furo nem repetição; `retiradas` vazia é consistente.
- Regras por tipo, todas cumpridas: `procedimento` (006, 039) começa com `Pré-condição:` e tem lista numerada ≥ 2; `exemplo` (004, 021, 029, 038, 041) tem as três marcas; `decisao` (022 `Se `, 031 `Quando `); `regua` (008, 014, 040) com número; `alerta-ui` (009) `perecivel: true`; `fato-material` (012, 013, 016, 017) com `fonte: pdf:`; `limite` (043) com `tarefas: []`; `conceito` com `tarefas: []` só em 001.
- `fonte`/`faixa`: toda unidade com `fala` tem faixa `hh:mm:ss–hh:mm:ss` com início < fim; as seis unidades só-PDF (012–017) não têm faixa. Nomes de PDF em `fonte` constam em `fontes`.
- Corpos: 1–8 linhas (procedimento/exemplo ≤ 15); nenhum timestamp, `[[`, `**[`, "hoje", "atualmente" ou "neste momento". "1)" e "2 min" em 023/039 não casam com os padrões proibidos.
- `confianca: baixa` não ocorre; nenhuma `nota` obrigatória em falta.
- Inspetor: nenhuma sequência de 25 palavras idêntica à fonte; `fontes` bate com o disco (`.srt` e `.json` não precisam constar).

Não verificável nesta leitura (sem script): valores de `plataforma`/`tema`/`tarefas` contra os enums de `taxonomia.md` e `fim ≤ duracao_segundos + 2 s` do manifest. Sem indício de erro; **veto 1 não falha**.

## Fidelidade

Contagem do pacote do inspetor: 43 unidades — 39 `lastreada`, 3 `desvio` (015, 038, 043), 1 `faixa-errada` (007), 0 `sem-lastro`.

Unidades com `faixa`: 37 (todas exceto 012–017). Faixa-errada: 1/37 = **2,7 %** (< 10 %); mesmo somando o caso de U:020 abaixo, 2/37 = 5,4 %. A regra de percentual **não** dispara.

Leitura crítica de cada não-lastreada:

- **U:007 — faixa-errada.** O inspetor cita "vem até alguns exemplos de anúncios aqui (...) para que você possa modelar. Não usar o mesmo vídeo" em 00:15:02–00:15:43, fora da faixa declarada 00:07:08–00:07:46, que só cobre o trecho do plágio. O corpo da unidade tem de fato duas afirmações de dois momentos diferentes (plágio na biblioteca; modelar os exemplos do manual) e declara só o primeiro. A evidência sustenta o veredito. Conteúdo lastreado; só a faixa está incompleta. Registro, sem veto.
- **U:015 — desvio, confiança alta.** PDF citado: "Nunca imitar um botão no banner no facebook ou instagram (...) nos gráficos não há problema". A unidade diz "Nenhum banner, em qualquer plataforma, pode desenhar um botão falso" e marca `plataforma: [meta, google-display]`. A fonte restringe a proibição a Facebook/Instagram e abre exceção explícita para gráficos (Display); a unidade generaliza e inclui justamente a plataforma excetuada. É condição que a fonte impõe e a unidade omite, com sentido invertido para Display. A evidência sustenta; a seção Material do próprio inspetor confirma a exceção. **Confiança alta ⇒ falha.**
- **U:038 — desvio, confiança alta.** Fala citada: "e aí você não vai adivinhar o que aconteceu. Começo a desenrolar através de um único texto" (00:35:33–00:36:15). A unidade afirma que o cliente "mudou de patamar ao migrar para o gerenciador". O inspetor afirma que a fonte não revela o desfecho; a citação é coerente com isso (o professor abre a história em suspense como demonstração de gancho e o trecho termina aí). Evidência por ausência, mas consistente e não contestável com o que tenho. Aceito: desfecho acrescentado à fonte. **Confiança alta ⇒ falha.**
- **U:043 — desvio, confiança alta.** Fala citada: "na próxima aula a gente vai entrar aqui no chat EPT (...) um roteiro de bom anúncio criado pela inteligência artificial" (00:40:08–00:40:25). A primeira linha da unidade está lastreada; a segunda ("Não há régua de desempenho (CTR, custo) nesta aula; isso fica para as aulas de métricas e otimização") não tem nada na fonte, segundo o inspetor. A frase é inteiramente acrescentada; caberia até `sem-lastro` para essa linha, mas como a unidade é metade lastreada aceito a classificação `desvio`. Em qualquer das duas leituras o resultado é o mesmo. **Confiança alta ⇒ falha.**

Achado do juiz sobre uma `lastreada`:

- **U:020.** A evidência citada pelo inspetor está em 00:20:17–00:21:01, mas a faixa declarada da unidade é 00:18:13–00:20:17: o trecho começa exatamente onde a faixa acaba. A evidência sustenta o conteúdo, não a faixa. Trato como provável faixa-errada; não altera o percentual acima do limiar. Registro para o redator conferir/estender a faixa.

Sem `sem-lastro`. Nenhum caso de UI "como está em 2026" completada. Demais lastreadas: as citações do inspetor caem dentro das faixas declaradas (U:027 com sobreposição parcial 00:25:02–00:25:31, aceitável).

**Veto 2 falha** por três desvios com `confianca: alta` (015, 038, 043).

## Cobertura

Omissões listadas pelo inspetor, com minha decisão:

1. **"Cinco, seis anúncios" por semana** (fala 00:10:25–00:10:42: "Você tem que toda semana salvar. Cinco. Seis anúncios."). Nenhuma unidade registra essa cifra nem a contrasta com o "3 a 5" de U:008 (dito depois e no PDF). É número de régua da fonte, dito dentro da própria faixa de U:008 (00:10:25–00:12:47), e a unidade reporta só a segunda cifra. Pela regra literal, omissão de número ⇒ **falha**. Correção esperada: U:008 registra as duas cifras (ou baixa a confiança com `nota` explicando a discrepância do professor).
2. **Filtro de localização** no Ads Transparency Center (PDF: "selecionar os formatos dos anúncios que você quer ver e a localização"), ausente de U:009. Detalhe de tela perecível, não número/passo/condição ⇒ registro.
3. **Filtro de horário** (fala 00:10:47–00:11:28: "Qualquer horário onde os anúncios estão aparecendo"), ausente de U:009. A citação é ambígua quanto a ser um filtro; detalhe de tela ⇒ registro.

Material: o inspetor confirma que os números e políticas do manual de criativos estão integralmente em 012–017 e 014/015, e que o PDF-resumo é redundante com a fala e aparece como `fala+pdf:` nas unidades correspondentes. Nada a apontar nos PDFs. (A lista de IDs na seção Material do pacote contém o ruído "036 não"; U:036 é `fonte: fala`, consistente.)

**Veto 3 falha** pela omissão do número em (1).

## Perecibilidade

Unidades que descrevem tela, menu, botão ou caminho de clique: 006 (Biblioteca de Anúncios: país, categoria, botão direito, "salvar como"), 009 (Ads Transparency Center), 016 (CTA "saiba mais"/"arrasta para cima"), 032 (botão "Saiba mais"); todas `perecivel: true`. Também `true`: 012, 013, 014, 015, 017 não (ideias de criativo, sem UI — correto como `false`).

Borderline, sem veto: U:033 cita "clica em saiba mais e se cadastra" como frase de copy dentro da estrutura 2, não como descrição de botão; U:038 usa "botão impulsionar versus gerenciador" como tópico de roteiro. Não tratados como descrição de UI. Registro.

**Veto 4 não falha.**

## Falhas

- F2-01 — U:1674fc3d8d94c601:015 — fidelidade/desvio (confiança alta): fonte restringe a proibição de botão falso a Facebook/Instagram e excetua gráficos de Display; unidade generaliza para "qualquer plataforma" e inclui `google-display`. Corrigir escopo, condição e `plataforma`.
- F2-02 — U:1674fc3d8d94c601:038 — fidelidade/desvio (confiança alta): desfecho "mudou de patamar ao migrar para o gerenciador" não está na fonte. Remover o desfecho ou reduzir o exemplo ao que a fonte diz.
- F2-03 — U:1674fc3d8d94c601:043 — fidelidade/desvio (confiança alta): frase sobre régua de desempenho (CTR, custo) e "aulas de métricas e otimização" não está na fonte. Remover.
- F2-04 — U:1674fc3d8d94c601:008 — cobertura/omissão de número: cifra "cinco, seis por semana" (00:10:25–00:10:42) não registrada nem contrastada com "3 a 5". Registrar as duas cifras ou baixar confiança com `nota`.
- F2-05 — U:1674fc3d8d94c601:007 — registro (faixa-errada, abaixo do limiar): faixa 00:07:08–00:07:46 não cobre o trecho do manual (00:15:02–00:15:43). Corrigir a faixa ou dividir a unidade.
- F2-06 — U:1674fc3d8d94c601:020 — registro (faixa provável errada): evidência em 00:20:17–00:21:01, fora da faixa 00:18:13–00:20:17. Conferir e ajustar a faixa.

Registros sem correção obrigatória: filtros de localização e horário em U:009; menção a "saiba mais" em U:033.

## Próximo

redator
