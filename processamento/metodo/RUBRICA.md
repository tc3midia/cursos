# Rubrica v2 — unidades, playbooks e checklists

Sem nota numérica. Revisão proporcional aprovada por Will em 15/09/2026: preservar a qualidade com correção localizada, sem reextração automática de módulo por contagem de reprovações. Cinco vetos, aplicados com evidência e impacto. Ouro que falha continua `bloqueado` e vai para Bravo 1; nunca para o redator.

## Vereditos

- `passa` — nenhum veto; pode conter ajustes menores registrados, sem nova rodada só por eles.
- `falha` — ≥1 veto comprovado; corrigir apenas as unidades/trechos afetados.
- `bloqueado` — ouro reprovado, isolamento inválido, fonte indispensável indisponível ou falha material que persiste após os dois ciclos e a verificação residual final descrita em Gravidade e retrabalho; o caso vai a Will. O bloqueio pertence ao artefato afetado; não reprova nem manda refazer as outras aulas. Contar reprovações, sozinho, não é motivo de bloqueio.

## Gravidade e retrabalho

- **Falha material:** afirmação sem fonte, número/condição/sentido adulterado, etapa essencial ausente ou outro defeito que muda a decisão, impede a execução ou impede verificar a orientação. O apontamento identifica a fonte e explica a consequência prática. Incerteza real pode ser registrada; baixar `confianca` não autoriza manter um erro conhecido.
- **Ajuste menor:** redação, repetição, exemplo complementar, contagem incidental de tela ou detalhe cuja ausência não muda a decisão nem impede executar. Registrar com motivo; corrigir quando simples, sem reabrir extração ou exigir nova chamada de modelo só por isso.
- **Erro mecânico:** campo, formato ou marcação com correção objetiva. Corrigir localmente e verificar por script; zero erros de contrato continua obrigatório. Alteração que exige interpretar a fonte segue o fluxo de conteúdo.
- Antes de corrigir, consolidar uma lista de falhas: ID, evidência, impacto, mudança mínima e critério de aceite. A revisão seguinte confere essa lista e os efeitos da alteração; não procura perfeição editorial no restante. Nova falha material comprovada entra com justificativa; ajuste menor novo não abre outro ciclo.
- Divergência entre avaliadores exige confrontar evidência, regra e efeito prático e fixar o aceite. A coordenação não rebaixa sozinha uma falha da própria correção: o juiz independente decide na verificação focal já prevista, com evidência neutra, sem vereditos anteriores. Não abrir painel adicional. Se faltar prova indispensável ou persistir divergência material após o teto, isolar o item e levar o caso concreto a Will, sem novas chamadas automáticas.
- Corrigir unidades é o padrão. Reextrair uma aula só quando houver problema amplo comprovado nela (por exemplo, fonte errada ou conteúdo majoritariamente sem lastro), com motivo registrado e `reconciliar.py`. Não há gatilho de reextração por “2 de 4”, “3 de 6” ou quantidade de rodadas.
- Mesma causa material confirmada em duas aulas exige uma única ampliação da inspeção para duas aulas adicionais, buscando essa causa, antes de encerrar a revisão da leva, sem reextrair. Depois dessa expansão, qualquer ampliação precisa de evidência de alcance e escopo delimitado; não repetir expansões automáticas. Erro no pacote compartilhado manda corrigir o pacote e identificar quais aulas realmente foram afetadas.
- Dois ciclos de correção e verificação por artefato na etapa são o limite automático. Apontamentos novos, candidatos, mudança da regra ou renomeação da etapa não reiniciam esse contador. Após o teto, admitir uma intervenção localizada da coordenação na lista residual fixa e uma única verificação focal final (inspetor e juiz). Se persistir falha material, manter em rascunho/bloqueado e levar o caso concreto a Will, sem novas chamadas automáticas. Trabalho independente pode continuar; não declarar o módulo fechado enquanto houver falha material conhecida pendente.
- Evidência preservada exige hashes por unidade guardados na inspeção original, fonte identificada, integridade e compatibilidade com a rubrica conferidas. Registrar escopo, cobertura acumulada, IDs e hashes das evidências em `## Rastreabilidade da revisão`. Conferência manual antes do juiz e do selo: o selo atual não cobre evidência nem escopo. Sem comprovação anterior, inspecionar a parte necessária. Parecer parcial fica em temporários; `passa` final exige cobertura acumulada completa das unidades e omissões, além dos efeitos das alterações. Procedimento detalhado na regra de qualidade da frente.

## Vetos

### 1. Contrato — quem mede: script

`validate_unidades.py` (unidades) e `validate_visoes.py` (visões) com zero erros. Inspetor confirma
que nada bruto foi copiado (sequência de 25 palavras idêntica à fonte) e que `fontes` bate com o disco.

### 2. Fidelidade — quem mede: inspetor lastreia, juiz decide

Cada unidade é `lastreada`, `desvio`, `sem-lastro` ou `faixa-errada` no pacote do inspetor.

- Qualquer `sem-lastro` ⇒ falha.
- `desvio` comprovado (número, condição ou sentido diferente de uma fonte clara) ⇒ falha, qualquer que seja a `confianca` ou a `nota`.
- Fonte realmente ambígua, contraditória ou inaudível pode passar com registro quando o inspetor comprova a incerteza e a unidade a preserva com confiança adequada e nota. Essa exceção não permite manter afirmação reconhecidamente falsa.
- `faixa-errada` em > 10% das unidades com `faixa` ⇒ falha.
- Condição que a fonte impõe e a unidade omite = desvio.
- Nada de Ads "como está em 2026": completar a UI atual é sem-lastro.

### 3. Cobertura — quem mede: inspetor lista, juiz decide

As unidades devem preservar as orientações necessárias para decidir e executar: réguas, passos essenciais, condições, restrições e alertas que alteram a ação. Omissão só veta quando o inspetor a encontra na fonte e o juiz demonstra o efeito prático de faltar aquele item.
Não exigir uma unidade para cada número de exemplo, opção incidental de tela ou repetição. Esses itens podem ficar como ajuste menor quando não mudam a orientação nem impedem executar. Todo número ou afirmação que for incluído deve continuar fiel à fonte.
Usar transcrição e materiais no pacote como origem da cobertura; não usar memos v1 como checklist. Omissão de contexto sem efeito operacional é registro, não veto.

### 4. Perecibilidade — quem mede: inspetor sinaliza, juiz decide

Descrição de tela, menu, botão ou caminho de clique sem `perecivel: true` ⇒ falha. "Hoje",
"atualmente" no corpo ⇒ contrato (script). Playbook sem seção Perecível preenchida quando cita
`alerta-ui` ⇒ falha.

### 5. Aplicabilidade do playbook — quem mede: juiz

Pergunta única: um agente executa a tarefa amanhã só com o playbook e as unidades citadas?

Passa só se todas forem verdade:

1. `Pré-condições` lista o ponto de partida (conta, campanha, acesso, dado necessário).
2. `Passos por plataforma` tem subseção com passos ordenados para cada plataforma da matriz
   (`taxonomia.md`) ou declara "Nada nas fontes." com citação de `limite` quando o curso não ensina.
3. ≥1 régua observável em `Réguas e critérios de pronto`.
4. `O que o curso não cobre` e `Sem resolução no curso` preenchidos quando a matriz ou a
   consolidação mandam.
5. Cada passo cita unidade de tipo compatível (passo ⇒ `procedimento`/`regra`/`decisao`; régua ⇒
   `regua`; tela ⇒ `alerta-ui`).
6. **A unidade citada sustenta a afirmação.** Citação existente que não diz o que o bullet afirma ⇒
   falha (o juiz confere no corpo da unidade, sem transcrição).

## Calibração

`ferramentas/curso-subido/tests/calibracao/` guarda fixtures com defeito conhecido e `veredito_esperado`/`veto_esperado`. O juiz tem
de reprovar cada fixture pelo veto certo. Se não reprovar, a rubrica ou o papel do juiz têm defeito;
corrige-se a causa, nunca a régua para baixo.
