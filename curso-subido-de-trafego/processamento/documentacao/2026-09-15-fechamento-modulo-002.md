# Fechamento do módulo 002 — Facebook e Instagram Ads

## Resultado

As próximas 18 aulas foram concluídas, com **334 unidades novas**. O módulo está completo: **36 aulas e 765 unidades**, validadas pelo processo amostral aprovado. A biblioteca soma 62 aulas e 1.559 unidades.

Will autorizou esta sessão com “podemos avançar”, depois do fechamento da primeira metade. A sessão 7, módulo 004, é a próxima etapa do plano.

## Qualidade sem refazer o lote

- Terra extraiu as 18 aulas com esforço médio, uma chamada independente por aula.
- A amostra foi a aula 6.10, posicionamentos (`05ace36fbf112424`), menor identificador da nova leva. Terra inspecionou em contexto separado; Astra julgou com esforço alto.
- A amostra precisou de uma correção: acrescentar à U017 o risco de associação a conteúdo grave ao escolher inventário completo. Sol fez o ajuste com esforço médio; Terra conferiu o bloco e suas dependências; Astra aprovou. Os outros 20 blocos ficaram intactos.
- Cinco unidades receberam ajustes mecânicos, em três aulas: abertura “Quando” no tipo decisão; duas marcações de interface perecível; duas referências temporais explicitadas. Um cabeçalho teve o identificador alinhado ao manifest. A checagem por script encerrou esses ajustes.
- **Zero reextração.** Uma correção de conteúdo, um ciclo de conferência e nenhum alargamento automático da amostra nesta sessão.

As quatro aprovações e as duas inspeções focais da primeira metade foram preservadas. Validação amostral não significa inspeção integral de todas as 36 aulas.

## Conferências finais

| Controle | Resultado |
|---|---|
| Fonte | Clone `f188775`; hashes dos materiais conferidos |
| Aulas restantes do módulo | 0 |
| Validação da biblioteca | 0 erros |
| Testes | 80 aprovados |
| Índices e documentos derivados | Atuais; zero erros |
| Propostas de tag | Nenhuma; taxonomia preservada |
| Avisos | 21 preexistentes; nenhum novo nesta leva |
| Conteúdo anterior | 44 arquivos preservados; nas primeiras 18 do 002 mudou somente o status para `validado` |
| Laudos anteriores | Preservados byte a byte |

E8 foi cumprido: os 36 arquivos do módulo passaram de `rascunho` a `validado`. Essa marca registra o fechamento amostral. Os 26 arquivos de outros módulos não sofreram alteração.

## Registros menores e próxima etapa

- A U003 da aula 6.10 conserva um ajuste menor de faixa: o suporte indicado está em 00:02:44–00:03:19, enquanto a unidade registra 00:03:19–00:03:55. O laudo aprovou a aula com essa ressalva, sem afirmar que a faixa está correta e sem exigir outra chamada de modelo.
- Os dois registros menores de faixa da primeira metade continuam no fechamento anterior. Detalhes complementares da amostra estão no laudo, sem veto material.
- O aviso de baixa confiança da aula 6.1 é anterior e permanece justificado no fechamento da primeira leva.
- **Playbook piloto:** a cobertura de Meta passou a estar completa, mas suas novas unidades ainda não foram incorporadas à síntese. Refazer o piloto na sessão 13, junto dos demais playbooks; o hash de insumos antigos não detecta essa ampliação da base. Até essa revisão, a síntese permanece a versão parcial anterior.
- Próxima etapa: sessão 7, as 15 aulas do módulo 004. Nenhuma aula desse módulo foi iniciada nesta sessão.

## Consumo dos papéis

| Modelo | Função | Chamadas | Entrada | Entrada em cache | Saída |
|---|---|---:|---:|---:|---:|
| gpt-5.6-terra | Extração e inspeção | 20 | 675,943 | 250,880 | 65,209 |
| gpt-6-astra | Julgamento | 2 | 64,933 | 0 | 2,703 |
| gpt-5.6-sol | Correção pontual | 1 | 29,087 | 0 | 228 |

Total: **23 chamadas**, 769,963 tokens de entrada e 68,140 de saída. Cache está incluído na entrada; não deve ser somado novamente. Valores cobrem os papéis executados, não esta coordenação. Não há comparação controlada que demonstre economia frente a outra rota.

As chamadas terminaram sem uso de ferramentas pelos papéis. O CLI exibiu um aviso de configuração de hooks incompatível; isso não interrompeu a execução e a configuração global ficou preservada.

## Evidências

- [Métricas por aula e chamada](2026-09-15-sessao-06-metricas.json).
- [Laudo aprovado da amostra](../revisao/laudos/05ace36fbf112424.md).
- [Rastreabilidade da revisão](../revisao/laudos/05ace36fbf112424.rastreabilidade.json).
- [Fechamento da primeira metade](2026-09-15-fechamento-primeiras-18.md).
- Tarefas e sequência (registro no Jarvis 4: `projetos/tc3/frentes/curso-subido-base-atomica/tarefas.md`).

Artefatos originais, evidências e registros de execução preservados em `biblioteca/curso-subido-trafego/revisao/arquivo/2026-09-15-sessao-06/`. Pacotes e logs brutos locais em `_saida/tc3/2026-09-14-curso-subido-base-atomica/temporarios/codex/sessao-06/`.

Commit do fechamento: `98e20e5`. Esta referência entra no commit documental seguinte. Push não executado.
