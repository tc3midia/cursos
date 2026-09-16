# Primeiras 18 aulas: revisão concluída

**A primeira leva do módulo 002 está fechada pela revisão amostral. A próxima etapa são as outras 18 aulas.** Os apontamentos materiais foram resolvidos, as duas conferências adicionais passaram e os candidatos aprovados foram integrados à biblioteca.

Conteúdo, evidências e fechamento registrados no commit local `5a34308`. Sem push. Esta referência segue no commit de registro posterior.

## Resultado por aula

| Aula | Trabalho realizado | Resultado final |
|---|---|---|
| 6.1 — Objetivos e metas de desempenho | Correção residual; depois, dois ajustes de frases e a conferência pontual autorizada por Will | Aprovada; 55 unidades |
| 3.2 — Aprendizado e aquecimento do pixel | Condição causal, preferência por campanhas ativas e faixa de uma unidade corrigidas | Aprovada; 32 unidades |
| 5.4 — Direcionamento detalhado | Hipótese dos 90%, nomes conforme a fonte e orientações omitidas; segundo ciclo corrigiu só a qualificação de grafia incerta | Aprovada; 31 unidades |
| 5.1 — Públicos personalizados | Condições, períodos, organização da lista, nomenclatura e ressalvas corrigidos | Aprovada; 52 unidades |
| 5.0 — Tipos de segmentações | Conferência das causas recorrentes | Passou no escopo focal; sem alteração |
| 6.0 — Criação de campanhas | Conferência das causas recorrentes | Passou no escopo focal; sem alteração |

As duas últimas são conferências por causa, sem alegação de inspeção integral. A amostra inicial de quatro aulas tem cobertura composta: evidência da inspeção integral anterior mais a conferência dos trechos alterados e de suas dependências.

**Nenhuma aula foi reextraída nesta retomada.** As outras 14 aulas existentes ficaram intactas. As 26 aulas anteriores ao módulo 002 também foram preservadas byte a byte.

## Encerramento sem exigir perfeição

Não resta falha material conhecida que impeça fechar esta leva. Dois ajustes menores de referência temporal ficaram registrados nos laudos: U:13b2d9f52cf439b3:030 e U:2adad5b1c731d4ab:025. A evidência permite conferir as orientações; não exigem outra rodada. A incerteza real de nomes na aula 6.1 continua explícita, com confiança baixa e nota.

A 6.1 parou no limite previsto. Will autorizou separadamente uma única conferência de U026/U035, que passou. [Decisão e textos dos dois ajustes](2026-09-15-decisao-pontual-aula-6-1.md). O contador não foi reiniciado. Na 5.4, o primeiro juiz confundiu a etapa com a intervenção residual; a coordenação preservou o diagnóstico e aplicou o segundo ciclo que ainda estava disponível, sem rebaixar o erro por conta própria.

## Validação e estado da biblioteca

- 80 testes aprovados; validador com fontes habilitadas: zero erros.
- Índices atuais; derivados sem erros ou desatualização; quatro laudos aprovados selados.
- Hashes dos candidatos, da rubrica, das fontes e das evidências conferidos antes do julgamento e da integração.
- 44 aulas e 1.225 unidades na biblioteca. O módulo 002 contém 18 aulas e 431 unidades.
- O módulo tem 36 aulas no total; faltam extrair as outras 18. O fechamento desta meia leva não aciona E8: os arquivos do módulo permanecem em `rascunho` até o fechamento do módulo completo, conforme o plano.

As evidências anteriores, as versões usadas como base, os pareceres focais e os mapas de rastreabilidade estão preservados em [arquivo da revisão](../historico/execucoes/2026-09-15-fecho-primeiras-18). Os laudos vigentes e seus comprovantes estão em [laudos](../revisao/laudos). A integridade da composição foi conferida nesta execução; o selo, sozinho, não automatiza essa garantia.

Os arquivos vivos passaram na checagem de espaços do Git. Cópias históricas congeladas mantêm os espaços finais originais para preservar seus hashes; os únicos avisos de `diff --check` pertencem a essas cópias. A limpeza de espaços nos três candidatos integrados não alterou conteúdo nem hash de unidade, e ficou registrada nos manifestos.

## Consumo desta retomada

| Modelo | Função | Chamadas | Entrada + saída |
|---|---|---:|---:|
| Sol | Correção | 5 | 192.445 |
| Terra | Inspeção | 8 | 281.755 |
| Astra | Julgamento | 8 | 309.346 |
| **Total** | | **21** | **783.546** |

Cache já incluído na entrada. O total inclui as tentativas que precisaram de correção e a conferência pontual autorizada; exclui esta conversa de coordenação e o Claudex da regra. Acumulado medido da extração da sessão 5, diagnóstico 5b e esta retomada: **2.612.315 tokens**. A aprovação de conteúdo foi obtida; estes dados não são uma comparação controlada de eficiência entre modelos.

[Métricas completas](2026-09-15-fecho-primeiras-18-metricas.json). Pacotes e logs operacionais em `_saida/tc3/2026-09-14-curso-subido-base-atomica/temporarios/codex/fecho-proporcional/`.

Próxima sessão: **6 — extrair as aulas 19 a 36 do módulo 002**, com Terra na extração/inspeção, Sol nas correções e Astra no julgamento, pela regra proporcional vigente. Estado canônico em tarefas.md (registro no Jarvis 4: `projetos/tc3/frentes/curso-subido-base-atomica/tarefas.md`).
