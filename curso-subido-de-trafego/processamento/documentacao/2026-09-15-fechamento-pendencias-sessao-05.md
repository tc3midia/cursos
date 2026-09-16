# Sessão 5b: correções antes da próxima etapa

**Atualização posterior de Will, 15/09/2026:** a [nova regra de qualidade e retrabalho](2026-09-15-regra-qualidade-e-retrabalho.md) revogou a obrigação de reextrair as outras 16 aulas e o bloqueio automático por número de julgamento. Os apontamentos serão triados para correção localizada; nenhum candidato foi aprovado por essa mudança. Este relatório preserva o diagnóstico, as regras usadas naquele momento e o consumo histórico. O estado vigente está em tarefas.md (registro no Jarvis 4: `projetos/tc3/frentes/curso-subido-base-atomica/tarefas.md`).

**A revisão ainda não está fechada.** A classificação pendente foi resolvida, mas as quatro aulas da amostra reprovaram. Duas foram reextraídas e corrigidas; ambas chegaram à terceira reprovação e ficaram **bloqueadas**, conforme a rubrica. As outras 16 reextrações não começaram. A sessão 6 permanece suspensa.

Correções e diagnóstico registrados no commit local `ae9eba5`. Nenhum push realizado.

## O que ficou resolvido e salvo

- A proposta `otimizar-campanhas`, em `U:f5fd46cdb63a8963:004`, foi recusada. `nomear-campanhas` e `ler-metricas-e-relatorios` já cobrem a orientação. A unidade está na versão 3, com nota; a taxonomia foi preservada.
- A primeira correção da aula 6.1 ajustou quatro unidades e acrescentou oito, preservando as outras 40. Esse arquivo intermediário ficou na biblioteca, com 52 unidades e **status rascunho**.
- O papel do extrator foi ajustado no commit local `9d6b779`: conferir a fonte inteira, preservar limites numéricos exatos, condições, ressalvas, hipóteses e opções operacionais.
- Índices atualizados, **80 testes aprovados**, zero erros de validação e nenhum derivado desatualizado. Os 20 avisos globais são anteriores a esta sessão.
- A biblioteca contém **44 aulas e 1.208 unidades**; o módulo 002 tem **18 aulas e 414 unidades em rascunho**. As 26 aulas anteriores continuam idênticas.

Essas verificações comprovam a consistência dos arquivos. **Não substituem a aprovação de conteúdo**, que não foi obtida.

## Resultado da revisão

A amostra começou pela menor `aula_id` das 18 aulas existentes. As falhas ampliaram a seleção para quatro aulas. Terra inspecionou as fontes e Astra julgou as evidências em contextos separados; Sol coordenou e corrigiu os itens apontados.

| Aula | Diagnóstico inicial | Depois da reextração e correção | Último resultado |
|---|---|---|---|
| 6.1: Seleção de objetivos e metas de desempenho | Falha | Falha no segundo julgamento | **Bloqueado no terceiro**; candidato temporário com 54 unidades |
| 3.2: Fase de aprendizado e aquecimento do pixel | Falha | Falha no segundo julgamento | **Bloqueado no terceiro**; candidato temporário com 32 unidades |
| 5.4: Direcionamento detalhado | Falha | Não iniciada | Pendente; incluída nas outras 16 |
| 5.1: Públicos personalizados | Falha | Não iniciada | Pendente; incluída nas outras 16 |

Os problemas se repetiram: cobertura operacional incompleta, limites e condições alterados, hipóteses ou nomes incertos tratados como fatos e descrições de interface sem marcação perecível. A reextração com o papel corrigido também deixou de fora pontos já identificados; precisou de assistência Sol e ainda não passou.

O primeiro laudo apontou também falta de comprovação da correspondência entre fontes declaradas e arquivos em disco. A coordenação forneceu essa prova mecânica aos julgamentos seguintes. Essa pendência documental foi tratada separadamente das falhas de conteúdo.

### Por que o processamento parou

A [RUBRICA](../metodo/RUBRICA.md) define `bloqueado` para a terceira falha do mesmo artefato. A contagem adotada, explicitada no [plano](planos/2026-09-14-plano-de-sessoes.md), foi diagnóstico inicial + até dois ciclos de correção e novo julgamento. Nenhum contador foi reiniciado na reextração.

As duas aulas atingiram esse limite. Nenhum candidato reextraído foi promovido, nenhum novo laudo foi selado e o módulo não passou a validado. Os candidatos finais e todas as rodadas estão preservados para retomada.

## Pendências exatas nos candidatos finais

Os IDs abaixo pertencem aos **candidatos temporários**, não necessariamente à versão atual na biblioteca.

| Aula | Unidade | Correção ainda necessária segundo o último laudo |
|---|---|---|
| 6.1 | `U:132b49d477065deb:034` | Restringir ao Instagram o modelo de mensagens demonstrado, sem estendê-lo ao Messenger. |
| 6.1 | `U:132b49d477065deb:057` | Preservar a ressalva sobre as demais metas de tráfego em site. |
| 6.1 | `U:132b49d477065deb:027` | Preservar a associação habitual entre maximizar cliques e instalação. |
| 6.1 | `U:132b49d477065deb:035` | Preservar a condição favorável à Advantage Plus para quem não usa o método. |
| 6.1 | `U:132b49d477065deb:035` / nova unidade | Registrar o alerta de catálogo inicialmente selecionado na campanha manual. |
| 6.1 | `U:132b49d477065deb:004` | Marcar a descrição dos seis objetivos visíveis como perecível. |
| 3.2 | `U:13b2d9f52cf439b3:023` | Incluir no corpo a preferência por manter todas as campanhas ativas. |
| 3.2 | `U:13b2d9f52cf439b3:019` | Preservar a qualificação causal sobre aquecimento do pixel. |

Há ainda uma faixa incorreta em `U:13b2d9f52cf439b3:031`, registrada sem veto por representar 1 de 32 unidades. A incerteza de nomes em `U:132b49d477065deb:026` ficou explícita em nota e confiança baixa; passou com registro.

**Variação entre julgamentos:** na aula 3.2, o segundo julgamento tratou a ressalva causal do pixel como contexto sem falha independente; o terceiro a considerou condição diagnóstica e aplicou veto. Isso precisa ser resolvido na retomada para evitar ciclos que mudem o critério de aceitação. Todos os apontamentos das inspeções foram preservados e enviados aos juízes.

## Preservação e rastreabilidade

Os dois candidatos finais têm zero erros mecânicos com as fontes habilitadas. O candidato da aula 6.1 tem um aviso de confiança baixa; o da aula 3.2 não tem avisos. Ambos continuam bloqueados por conteúdo.

A reconciliação automática reconheceu inicialmente só 13 de 52 IDs na aula 6.1 e 2 de 20 na aula 3.2. A coordenação registrou correspondências semânticas e divisões/fusões explícitas, preservando 40 e 16 IDs, respectivamente. Todas as unidades antigas ficaram contabilizadas, sem colisões. Relatórios automáticos originais, mapas e versões anteriores foram preservados; nenhuma ferramenta global foi alterada.

A fonte continua no clone `f188775`. Os candidatos reextraídos, evidências e laudos ficam fora do Git, em:

`_saida/tc3/2026-09-14-curso-subido-base-atomica/temporarios/codex/fecho-sessao-05/`

Arquivos principais para retomada:

- `resultado.json`: histórico completo, chamadas e hashes.
- `reextracao/candidatos/<aula_id>.reconciliado.md`: candidatos finais bloqueados.
- `reextracao/candidatos/<aula_id>.r3.evidencia.md` e `<aula_id>.r3.juiz.md`: evidência e laudo final.
- `reextracao/itens-inspecao-<aula_id>-r3.json`: quadro integral enviado ao juiz.
- `reextracao/reconciliacao-<aula_id>.json`: mapa de identidade e versões.
- `reextracao/baseline/`: versões anteriores à reextração.

Os metadados essenciais e o consumo também estão salvos nas [métricas duráveis](2026-09-15-sessao-05b-codex-metricas.json).

## Consumo medido

| Modelo / função | Chamadas | Entrada | Saída | Soma |
|---|---:|---:|---:|---:|
| Terra: extração e inspeção | 10 | 436.906 | 48.627 | 485.533 |
| Sol: correção | 5 | 212.099 | 5.287 | 217.386 |
| Astra: julgamento | 8 | 313.655 | 12.039 | 325.694 |
| **Total desta sessão** | **23** | **962.660** | **65.953** | **1.028.613** |

Cache já está incluído na entrada. O consumo da coordenação e desta conversa não está incluído. As 23 chamadas terminaram; nenhuma ficou ativa.

Somado à extração da sessão 5, o consumo medido é **1.828.769 tokens**, ainda sem aprovação da revisão. Portanto, a eficiência dessa rota **não foi demonstrada**.

Duas inspeções sofreram reconexões e terminaram com resultados válidos, sem repetição. O tempo de parede incluiu suspensão; não serve como medida de tempo ativo.

## Retomada recomendada

Manter a sessão 6 suspensa. Antes de repetir a extração em lote, tratar o bloqueio destas duas aulas com uma lista fixa de falhas e critérios de aceitação, incluindo a divergência entre os julgamentos. O próximo tratamento precisa preservar o histórico de reprovações e definir como encerrar a revisão bloqueada; não deve iniciar outro ciclo automaticamente.

Depois da aprovação dessas duas aulas, retomar as 16 reextrações previstas e concluir a amostra. Só então avaliar o avanço para as 18 aulas ainda não extraídas do módulo 002.

Estado e commits em tarefas.md (registro no Jarvis 4: `projetos/tc3/frentes/curso-subido-base-atomica/tarefas.md`).
