---
type: avaliacao-de-uso
versao_base: v2
recorte: piloto (CP1)
agente_avaliado: sonnet-5
avaliador: fable-5.1
data: 2026-09-13
---

# Resultados — v2 (ouros + playbook piloto), recorte piloto

Base lida pelo agente: `visoes/` + `unidades/` + `indice.md` (só os 2 ouros e o playbook piloto
existiam). Contexto separado por caso. Conferência das citações feita pelo avaliador: cada `U:`
citado foi lido no arquivo de unidades e a unidade foi conferida contra a transcrição/PDF.

## Caso 3 — diagnosticar concentração de verba no YouTube

- Arquivos abertos: 3 (`indice.md`, playbook, arquivo de unidades da 005-4.0).
- Palavras lidas: 2.905.
- Decisões críticas: certas. Três diagnósticos, ordem das soluções, "não pausar", condição das
  metas, pressa ⇒ isolar, ≥2 públicos por campanha, critério de pronto.
- Citações: 15 IDs distintos; **todas sustentam** a afirmação a que estão presas (conferido
  bullet a bullet e unidade a unidade na transcrição).
- Condições preservadas: sim (metas não batendo; valores são exemplo do professor; lance manual
  como pré-condição).
- Perecível: o caminho de tela da solução 2 veio com ressalva explícita ("perecível, pode ter
  mudado"), herdada da seção Perecível do playbook.
- Recomendações indevidas: nenhuma. Nada além do que a aula cobre.
- Lacunas reconhecidas: quatro, adequadas, com citação da unidade `limite`.
- Aprovação pelo critério do caso: **aprovado**.

## Caso 7 — coletar referências de anúncio

- Arquivos abertos: 3 (`indice.md`, página de tema `criativo`, arquivo de unidades da 8.3).
  Não há playbook `coletar-referencias-de-anuncio` ainda; o agente caiu na página de tema e depois
  abriu o arquivo inteiro da aula.
- Palavras lidas: 5.527 (mais que a v1 neste caso: 4.132).
- Decisões críticas: certas. Biblioteca do Meta, Ads Transparency Center, salvar imagem/vídeo
  com `.mp4`, pasta, 3 a 5 por semana e 150–200 no ano, ideal diário, plágio proibido, pesquisa
  ativa.
- Citações: 11 IDs distintos; todas sustentam. Nenhuma recomendação sem lastro.
- Divergência fala/PDF (5–6 vs 3–5 por semana): **não exposta**. A unidade U:008 registra "3 a 5"
  e "não precisa de 50", mas não registra que a fala menciona "cinco, seis" antes de fechar em 3 a
  5. Omissão da unidade, não do agente; vai para o inspetor/juiz do ouro 8.3.
- Perecível: o procedimento U:006 está marcado `perecivel: true`, mas o agente **não** repassou a
  ressalva ao cliente. Sem playbook, a seção Perecível não existe e a marca fica só no metadado.
- Lacunas reconhecidas: quatro, adequadas.
- Aprovação pelo critério do caso: **reprovado** pelo critério "caminho de tela com ressalva de
  perecibilidade" (as demais condições atendidas).

## Síntese v2

| caso | arquivos | palavras | decisões críticas | sem lastro | perecível marcado | resultado |
|---|---|---|---|---|---|---|
| 3 | 3 | 2.905 | certas | 0 | sim | aprovado |
| 7 | 3 | 5.527 | certas | 0 | não | reprovado |

## Comparação v1 × v2 (piloto)

| critério | v1 | v2 |
|---|---|---|
| decisões críticas (2 casos) | certas | certas |
| recomendações sem lastro | 2 (caso 7) | 0 |
| citações verificáveis na fonte | por seção de memo; parte não conferível sem reler a aula | por ID; 26/26 conferidas |
| palavras lidas caso 3 | 9.846 | 2.905 |
| palavras lidas caso 7 | 4.132 | 5.527 |
| ressalva de perecibilidade repassada | 0/2 | 1/2 (só onde havia playbook) |
| lacunas reconhecidas | sim | sim, com citação de `limite` |

Leitura do avaliador: a v2 ganha em correção (zero afirmações sem lastro, rastreabilidade por ID)
e, onde há playbook, em esforço de leitura e em perecibilidade. Onde não há playbook (caso 7), o
agente cai na página de tema e no arquivo inteiro da aula, lendo mais que a v1 e perdendo a
ressalva de perecível. Consequências para as próximas etapas:

1. A página de tema não substitui playbook; a etapa 3 precisa cobrir todas as tarefas da matriz
   (já previsto) e o índice deve apontar a tarefa sem playbook para as unidades por tarefa, não
   para a página de tema.
2. FORMATO §6.5: a página de tema passa a marcar "· perecível" em destaque no título da unidade
   (já faz no subtítulo; manter) e o `pacote.py tarefa` já entrega as unidades por tarefa.
3. Ouro 8.3, U:008: registrar a menção "cinco, seis" da fala antes do "3 a 5" (correção após o
   laudo do juiz, dentro do ciclo de correção).
