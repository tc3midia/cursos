# Qualidade com correção localizada

**Decisão de Will em 15/09/2026:** retirar a regra que manda reprocessar um módulo inteiro por falhas na amostra. Manter qualidade com retrabalho proporcional ao problema e atenção ao consumo de tokens.

Esta decisão substitui os gatilhos anteriores de reextração em lote. A aplicação operacional está na [RUBRICA](../metodo/RUBRICA.md), nos papéis e em E7 do [plano](planos/2026-09-14-plano-de-sessoes.md).

Registrada no commit local `69cc598`, sem push. Verificação: 80 testes aprovados, índices atuais, derivados sem erros e nenhuma alteração nas unidades ou laudos existentes. Isso verifica a compatibilidade dos arquivos; a nova regra ainda não foi aplicada a outra avaliação por modelo.

## Regra em linguagem simples

| Situação | Tratamento |
|---|---|
| Informação inventada, número alterado ou condição essencial ausente | Corrigir a unidade afetada e conferir a correção com a fonte. |
| Detalhe complementar que não muda a decisão nem impede executar | Registrar como ajuste menor; corrigir se simples, sem outra rodada só por isso. |
| Campo, formato ou marcação objetiva errada | Ajustar localmente e verificar por script. |
| Mesma causa material confirmada em duas aulas | Conferir uma única vez duas aulas adicionais buscando essa causa, antes de encerrar a revisão da leva. Isso amplia a inspeção, não a extração. |
| Problema amplo comprovado em uma aula | Reextrair somente essa aula, justificando por que a correção localizada não basta. |
| Avaliadores discordam | Comparar evidência, regra e consequência prática antes de mandar refazer conteúdo. |

**Nenhuma contagem de reprovações manda refazer o módulo.** Uma inconsistência localizada não invalida automaticamente as outras aulas.

## Como encerrar uma correção

1. Consolidar uma lista: o que está errado, onde está a prova, qual o efeito prático e qual a mudança mínima necessária.
2. Corrigir só essa lista, preservando IDs, versões e blocos intactos.
3. Conferir os trechos alterados e suas dependências. Preservar a evidência válida do restante, com hashes/versões conferidos; não declarar uma revisão completa que não ocorreu.
4. Encerrar quando os problemas materiais forem resolvidos e as verificações mecânicas passarem. Ajustes menores registrados não impedem aprovação.

Uma falha material nova continua podendo ser apontada, com prova e justificativa. Preferência editorial nova não reabre o ciclo. A lista evita mudanças arbitrárias do critério, sem esconder erros reais.

O limite de rotina é de dois ciclos automáticos de correção e verificação por artefato na etapa. Apontamentos novos, candidatos, mudança da regra ou renomeação da etapa não reiniciam esse contador. Depois do teto, a coordenação pode fazer uma intervenção localizada sobre a lista residual fixa, seguida de uma única verificação focal final (inspetor e juiz). Se persistir falha material, manter a aula em rascunho/bloqueada e levar o caso concreto a Will; nenhuma nova chamada automática. O bloqueio não se espalha para o módulo. Ouro, isolamento inválido e falta de fonte indispensável continuam com proteção própria.

Erro conhecido continua sendo erro mesmo com `confianca: baixa`. Incerteza só permite registro quando está na própria fonte e a unidade a preserva. Se houver discordância, fixar o critério com evidência e efeito prático. Sol não pode rebaixar sozinho uma falha da própria correção: Astra decide independentemente na verificação focal já prevista, com evidência neutra do inspetor e sem os vereditos anteriores. Não abrir outro painel de modelos. Divergência material ainda sem solução segue a parada acima.

## Evidência suficiente sem reler tudo

Na primeira inspeção, guardar a fonte identificada por commit/hash, a evidência integral e os hashes por unidade calculados por `unidades.hash_unidade`. Na revisão focal, a coordenação registra em `## Rastreabilidade da revisão`, no corpo do laudo, o escopo desta rodada (focal/completo), a cobertura acumulada (parcial/completa), IDs conferidos, SHA256 da RUBRICA e da evidência atual, além da relação ID → hash original → caminho/hash da evidência preservada. Registrar também quem conferiu essa composição e o resultado.

Antes do juiz e antes de selar, comparar as unidades atuais com os hashes guardados na inspeção original. Mudanças e dependências afetadas entram no escopo; evidência reaproveitada precisa continuar íntegra, aplicável à fonte e compatível com a rubrica vigente. Sem esse registro original, não presumir validade: inspecionar a parte sem comprovação. A cobertura acumulada precisa reunir todas as unidades atuais e a checagem original de omissões na fonte, com os efeitos das alterações conferidos. Um parecer parcial fica em temporários; só emitir laudo final `passa` com essa cobertura completa e sem falha material conhecida.

Essa conferência é manual por enquanto: o selo atual cobre unidades, FORMATO e taxonomia, mas não prova o escopo nem a integridade da evidência. Não mudar FORMATO nem resselar laudos antigos só para acrescentar esse registro às próximas revisões.

O pacote focal deve conter a lista fixa de falhas/aceite, blocos alterados ou novos, dependências afetadas, janela da fonte de cada apontamento (inclusive da passagem omitida), identificação/hash dos insumos e resultado atual do validador. O pacote de correção do extrator não substitui esse pacote quando o redator precisa criar ou retirar unidades. Se faltar contexto, retornar `contexto insuficiente`, sem aprovação; a coordenação prepara a janela necessária. A chamada fica registrada no consumo e não reinicia o teto nem autoriza tentativas ilimitadas.

## O que muda no trabalho atual

- Está **cancelada a obrigação de reextrair as outras 16 aulas** da primeira metade.
- As quatro aulas que tiveram apontamentos entram em triagem pela regra nova. Reaproveitar candidatos, evidências e correções existentes; não começar do zero.
- As quatro aulas já examinadas contam como amostra realizada. O diagnóstico anterior documenta condições operacionais omitidas nas aulas 6.1 e 3.2: essa recorrência exige uma única inspeção focal nas próximas duas ainda não revisadas por `aula_id`: `2ca16f54f7e1bd7a` (5.0) e `42508f24eb7b3b3b` (6.0). Conferir a fonte dessas aulas buscando a causa, antes de encerrar a revisão da primeira metade. Registrar o alcance encontrado e corrigir somente os itens afetados; nenhuma expansão automática adicional.
- Nessa mesma inspeção de 5.0 e 6.0, o escopo inclui todas as causas registradas como repetidas no diagnóstico: condições e ressalvas omitidas, limites ou números alterados, hipóteses ou nomes incertos tratados como fatos e descrições de tela sem `perecivel`. Usar as janelas necessárias a essas causas; não limitar a conferência à condição omitida. A checagem de tela pode ser mecânica nos casos efetivamente detectados pelo validador; os demais exigem conferência focal. Isso não acrescenta aulas nem transforma a inspeção por causa em inspeção integral.
- Primeiro, separar erros materiais, ajustes menores e divergências de avaliação. A mudança da regra não transforma os laudos antigos em aprovação.
- Inspeções adicionais só se justificam por uma causa material recorrente e por um escopo delimitado. As outras 18 aulas do módulo continuam sendo trabalho novo, separado desta correção.
- A divisão de modelos permanece: Terra extrai/inspeciona, Sol coordena/corrige e Astra julga. Scripts fazem as verificações mecânicas.
- Nas aulas 6.1 e 3.2, os dois ciclos automáticos já foram consumidos. Resta somente a intervenção residual e a única verificação final acima. As aulas 5.4 e 5.1 têm diagnóstico inicial, sem ciclo de correção consumido nesta revisão. Preservar o histórico e o consumo de todas as chamadas anteriores.
- Para `U:13b2d9f52cf439b3:019`, preservar no corpo a condição causal apontada na evidência como critério fixo de aceite; não resolver a divergência simplesmente omitindo a condição ou baixando a confiança.

## Limites e verificação

Esta atualização modifica os contratos e o plano. Não executa nova extração, não promove candidatos e não altera os resultados históricos. O formato dos arquivos, a taxonomia e os testes de fontes/IDs continuam iguais.

O comando padrão de inspeção ainda monta o pacote da aula inteira. Na retomada, a coordenação deve montar o pacote focal em temporários para as correções; apenas instruir o modelo a ignorar parte de um pacote grande não reduz os tokens de entrada. Não foi implementado um novo modo automático de pacote nesta alteração.

Exemplos de aplicação: trocar “até 50” por “menos de 50” continua sendo erro; omitir um contador incidental de exemplo não reprova por si só; faltar uma pré-condição que impede executar precisa de correção; dois revisores discordarem exige resolver o critério antes de repetir trabalho.

Estado da frente em tarefas.md (registro no Jarvis 4: `projetos/tc3/frentes/curso-subido-base-atomica/tarefas.md`). O [relatório da sessão 5b](2026-09-15-fechamento-pendencias-sessao-05.md) preserva o diagnóstico produzido sob a regra anterior.
