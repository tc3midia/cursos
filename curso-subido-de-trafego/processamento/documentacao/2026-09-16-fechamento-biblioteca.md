# Curso Subido — fechamento da biblioteca

16/09/2026 · Direção de Will: polir o material existente, organizar os arquivos técnicos e a revisão, reaproveitar o método para outros cursos e concluir este trabalho como base de consulta. Depois, tratar playbooks e checklists como ações dos agentes, especialmente do Gestor de Tráfego.

## O que ficou pronto

**133 aulas processadas, 2.829 unidades e 19 índices por tema.** Todas as aulas estão no [índice do curso](../../conhecimento/indice.md). Há 131 arquivos com status `validado` e dois `ouro`; a validação de conteúdo foi por amostragem, não uma revisão integral de todas as unidades. O [CP3](2026-09-16-cp3-processamento-completo.md) preserva as estatísticas e a cobertura por módulo.

O fechamento anterior comunicou a extração como concluída sem tornar suficientemente clara a diferença para a entrega de procedimentos completos. **Existe somente um playbook piloto parcial, sobre concentração de verba no YouTube, e nenhum checklist produzido.** As 19 páginas por tema são índices, não consolidações de decisões ou resolução de conflitos entre aulas.

O plano original também previa consolidações, playbooks em lote, checklists, glossário, órfãs e avaliação de uso completa. Essas etapas não foram realizadas. A direção atual encerra a biblioteca neste recorte e transfere a produção de rotinas para uma tarefa própria; não registra aquelas etapas como feitas nem presume aprovação detalhada de toda a matriz de cobertura.

## Organização aplicada

**Destino final ajustado por Will:** todo o material técnico deste trabalho encerrado fica reunido em [ferramentas/arquivo/processamentos/curso-subido](../README.md). A sugestão de colocar o método na TC3 Lab foi rejeitada e não foi executada; a bancada permanece dedicada a testes de agentes. O método fica preservado dentro do próprio arquivo, disponível para adaptar quando outro processamento for necessário.

Conferência após esse ajuste: 84 testes aprovados, índices consistentes, zero erros nas visões e 200 links locais conferidos sem destino ausente. Conteúdo das aulas, contratos, dados de controle, evidências e os três arquivos da TC3 Lab preservados por hash. Os 741 arquivos técnicos foram realocados; apenas caminhos de código e navegação foram ajustados. A rastreabilidade está no [manifesto de arquivamento](../historico/manifesto-arquivamento-ferramentas.json).

| Material | Destino e motivo |
|---|---|
| Aulas, índices por tema, fontes e contratos | Permanecem na [biblioteca](../../conhecimento/README.md), com navegação ajustada ao conteúdo que existe. |
| Antiga `_gerado` | [Dados das ferramentas](../dados/README.md). Os índices servem à busca e à verificação; `selos.jsonl` guarda versões usadas na revisão e precisa ser preservado. |
| Laudos e avaliação piloto | [Revisão do curso junto às ferramentas](../revisao/README.md). Continuam verificáveis e disponíveis para auditoria. |
| Rubrica e cinco papéis | [Processamento de conhecimento](../metodo/README.md), fora do curso, com roteiro de adaptação para novas fontes e taxonomias. |
| Histórico de execuções e README antigo da revisão | [Arquivo de processamento](../historico/README.md), fora da leitura cotidiana. |

**Nada foi excluído ou reprocessado.** O [manifesto de migração](../historico/manifesto-migracao.json) registra os 709 arquivos movidos, seus destinos e hashes. Também registra os hashes das 133 aulas, do FORMATO e da taxonomia, que permaneceram idênticos.

As ferramentas foram ajustadas para os novos caminhos. Nomes históricos nos selos, contratos e evidências continuam como identificadores lógicos, evitando reescrever provas ou refazer revisões apenas por mudança de pasta. Links documentais para os arquivos movidos foram atualizados; comandos e caminhos nas execuções arquivadas continuam representando a época em que foram usados.

## O que foi verificado

- **84 testes aprovados**, incluindo localização dos laudos, identificação de alteração em insumos e isolamento de bases temporárias.
- Validação de unidades: 133 arquivos, 2.829 unidades, **zero erros**; os mesmos 18 avisos preexistentes sobre confiança, densidade e fontes sem texto extraível.
- Geração dos índices conferida com `--check`; validação das visões com zero erros e nenhuma dependência desatualizada registrada.
- Integridade: 709 arquivos movidos e 135 arquivos de conteúdo/contrato conferidos por SHA-256, sem divergência.
- Navegação: 351 links locais conferidos em 39 documentos, sem destino ausente; `git diff --check` sem apontamentos no escopo da organização.
- Fonte original permanece no commit `f188775`. Nenhuma chamada nova de modelo foi necessária para revisar conteúdo do curso nesta organização.

Os selos atestam dependências registradas, não cobertura completa do curso nem aplicabilidade atual das interfaces. A avaliação de uso preservada é a do piloto. A organização não transforma automaticamente o piloto em playbook completo ou os índices em instruções prontas para execução.

## Continuidade para o Gestor de Tráfego

O mapa inicial (registro no Jarvis 4: `projetos/tc3/frentes/gestao-de-entregas/documentos/2026-09-16-rotinas-gestor-trafego-curso-subido.md`) propõe três rotinas: diagnosticar desempenho, investigar concentração de verba e planejar testes. Cada uma tem entradas, saída esperada, pontos de conferência e fontes iniciais. O diagnóstico é a primeira prioridade proposta.

Playbook explica como decidir e agir; checklist confere os requisitos e evidências daquela ação. A tarefa própria (registro no Jarvis 4: `projetos/tc3/frentes/gestao-de-entregas/tarefas/transformar-conhecimento-em-rotinas-de-trafego.md`) mantém a produção e a avaliação dessas rotinas como próximo trabalho. A preparação foi entregue; procedimentos completos e sua integração ao agente ainda não foram executados. Nenhuma conta de cliente foi alterada.

## Encerramento

Esta frente está concluída como **biblioteca de consulta organizada**, conforme a direção atual de Will. Método preparado para adaptação a outros cursos; aplicação operacional segue em sua tarefa. Mudanças locais verificadas, sem novo commit ou publicação nesta organização. Estado canônico e histórico das sessões em tarefas.md (registro no Jarvis 4: `projetos/tc3/frentes/curso-subido-base-atomica/tarefas.md`).
