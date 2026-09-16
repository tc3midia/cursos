# Resultado do Claudex: regra de qualidade

**Aprovada pelo Claude após três rodadas de revisão, em 15/09/2026.** Codex incorporou as correções à regra, aos papéis e ao plano.

## O que ficou decidido

- Corrigir apenas o conteúdo afetado. Continua cancelada a obrigação de reextrair as outras 16 aulas.
- Erro que muda uma orientação precisa de correção. Detalhe complementar pode ficar registrado sem gerar outra rodada.
- Confiança baixa não permite manter um erro conhecido.
- Reaproveitar evidências anteriores exige comprovar que continuam válidas. Essa conferência ainda é manual.
- Limite de dois ciclos automáticos por aula na etapa, sem reiniciar a contagem. Depois, uma intervenção residual e uma única conferência final; se ainda houver problema material, a aula para para decisão de Will.
- Quem corrige não pode aprovar sozinho o rebaixamento da gravidade de um erro.

## Efeito nas pendências atuais

As aulas 6.1 e 3.2 já esgotaram os dois ciclos; aproveitar os candidatos existentes para a intervenção residual. As aulas 5.4 e 5.1 ainda precisam das correções apontadas.

Conferir as causas recorrentes nas aulas 5.0 e 6.0, uma única vez: condições omitidas, limites/números alterados, hipóteses tratadas como fatos e telas sem marcação de conteúdo perecível. São duas inspeções delimitadas, sem reextração. As outras 18 aulas do módulo continuam sendo trabalho novo.

Esta revisão aprovou a regra. As correções das aulas e essas duas inspeções ainda não foram executadas, e a economia real de tokens até a aprovação do conteúdo ainda precisa ser medida.

## Evidência

O verificador Claudex confirmou que a aprovação corresponde à versão atual da [regra](2026-09-15-regra-qualidade-e-retrabalho.md). As verificações locais passaram: 80 testes, índices atuais e zero erros nos derivados. Os testes conferem compatibilidade dos arquivos, não a qualidade semântica das aulas.

[Pareceres completos, ajustes e limites da revisão](2026-09-15-claudex-regra-qualidade-log.md).
