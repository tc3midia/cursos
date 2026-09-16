# Piloto Codex: resultado para decidir

Data: 14/09/2026. Implementação e teste autorizados por Will. Aulas processadas em cópias; módulo 002 ainda não iniciado.

## O que eu recomendo agora

**Terra merece ser o primeiro candidato à extração no próximo teste pequeno. Sol fica na correção e Astra no julgamento. Ainda não temos uma distribuição comprovadamente mais econômica para rodar em escala.**

Terra terminou com as duas aulas aprovadas. Sol terminou com uma aprovada e outra ainda com problemas após duas revisões. Isso muda minha hipótese inicial de usar Sol como extrator padrão. A amostra é pequena e a inspeção variou entre rodadas; precisamos melhorar essa conferência antes de ampliar o processamento.

## Como cada um se saiu

Terra conferiu as fontes e Astra julgou todas as saídas abaixo. “Passou” significa aprovado nesse teste, sem promoção à biblioteca.

| Aula / extrator | Primeira revisão | Ajustes feitos | Resultado final |
|---|---|---|---|
| Curta / Sol, 15 orientações | Faltaram números e exemplos | Sol corrigiu 2 orientações | **Passou**, na segunda revisão |
| Curta / Terra, 14 orientações | Passou | Nenhum | **Passou**, de primeira |
| Longa / Sol, 53 orientações | Faltou marcar uma descrição de tela como sujeita a mudança | Correção mecânica de 1 marcação | **Não passou**: a segunda revisão encontrou 2 problemas de conteúdo |
| Longa / Terra, 36 orientações | Um nome foi alterado sem prova; faltaram uma condição e uma explicação ao cliente | Sol corrigiu 3 orientações, em 2 tentativas | **Passou**, na segunda revisão |

Na aula longa do Sol, ficaram uma preferência pelo Google Tag Manager enfraquecida no texto e uma explicação percentual incorreta. Paramos no limite de duas rodadas de julgamento previsto no plano.

A primeira correção da rota Terra deixou uma condição de fora e anexou a lista de erros ao conteúdo. A sessão retirou essa lista; Sol recebeu somente a orientação ainda pendente e a corrigiu. Esse retrabalho entra na medição. As demais orientações foram preservadas.

## O que aconteceu com os tokens

A comparação completa disponível é a da aula longa. Entrada inclui instruções e contexto do Codex, além da aula. Cache já está incluído na entrada.

| Rota da aula longa | Entrada | Saída | Entrada + saída | Situação ao encerrar |
|---|---:|---:|---:|---|
| Sol extrai; Terra confere; Astra julga | 228.677 | 21.386 | **250.063** | Ainda reprovada |
| Terra extrai; Sol corrige; Terra confere; Astra julga | 295.516 | 21.959 | **317.475** | Aprovada |

**Menos tokens com uma aula ainda reprovada não representa economia concluída.** Só na extração inicial, Terra consumiu 52.857 tokens contra 56.606 do Sol, cerca de 6,6% menos. O restante do processo mudou bastante essa conta.

As etapas medidas acumularam até 10min21s na rota Sol e 13min31s na rota Terra. São limites superiores até observarmos o término, sem filas e montagem dos pacotes; não servem como comparação precisa de velocidade.

Na aula curta, faltam os tokens das extrações feitas pelos subagentes nativos. Além disso, a primeira inspeção Sol leu arquivos em várias chamadas, enquanto a outra recebeu o pacote inteiro. Por isso, não calculamos uma economia percentual para essa aula.

Esses números não medem dinheiro nem o limite da assinatura. O experimento também gastou com calibração, implementação e coordenação; não são custos que se repetem integralmente em cada aula. A coordenação principal e os subagentes nativos não tiveram consumo exposto. Os [dados por chamada](2026-09-14-piloto-codex-metricas.json) separam o que foi medido.

## A revisão encontrou os erros conhecidos?

**Sim: os quatro casos foram reprovados pela categoria esperada.**

| Erro colocado no teste | Resultado |
|---|---|
| Números alterados | Fidelidade: detectado |
| Condições retiradas | Fidelidade: detectado |
| Telas sem marcação de mudança | Perecibilidade: detectado |
| Instruções que as citações não sustentam | Aplicabilidade: detectado |

Isso não significa revisão perfeita. No caso de condições, Terra apontou dois itens, mas Astra aceitou um deles porque a condição ainda aparecia no título. Na aula longa do Sol, a segunda inspeção encontrou problema que a primeira não havia apontado, e o julgamento mudou sobre a preferência pelo GTM. Precisamos de evidências mais completas e consistentes para números, condições e preferências.

## O que já está pronto

- Ferramentas aceitam autoria Sol, Terra e Astra, preservando os autores antigos.
- Cada papel recebeu seu próprio contexto. Juízes receberam candidato, evidências e regras; nenhuma transcrição completa.
- **80 testes passaram**, índices conferidos e verificações de derivados sem erros.
- **26 arquivos de aula e suas 794 orientações originais permaneceram idênticos.** Onze registros de dependência foram atualizados por causa da mudança de formato, sem nova revisão de conteúdo.
- A simulação de interrupção confirmou que arquivo presente pode estar incompleto. A retomada precisa conferir validação e resultado da etapa; a lista de arquivos pendentes, sozinha, não basta.

A interface de subagentes atingiu seu limite. As etapas seguintes usaram sessões separadas do Codex CLI com os modelos aprovados. Após as primeiras inspeções, os pacotes foram entregues inteiros, evitando releituras por ferramentas. Nenhuma configuração global foi alterada.

## Próxima decisão

Minha proposta é **manter os três modelos em funções diferentes e testar Terra como extrator em mais uma pequena amostra**, com conferência explícita de números, condições e preferências. Sol corrige apenas os blocos apontados; scripts verificam formato; Astra julga a amostra.

A aprovação atual cobriu este piloto. A escolha para continuar o módulo 002 permanece com Will, à luz deste resultado. Não há motivo medido para colocar Astra em todos os papéis.

### Rastreabilidade

- Aula curta: `869445a4c64befbf`, “Minha campanha está gastando toda verba em um único grupo de anúncio. E agora?”, 2.603 palavras de fonte.
- Aula longa: `54dea110daddeb21`, “Pixel e API de Conversões”, 9.093 palavras de fonte.
- Fonte: clone do curso no commit `f188775`.
- Pacotes, candidatos, evidências, laudos e tentativas: `_saida/tc3/2026-09-14-curso-subido-base-atomica/temporarios/codex/piloto-20260914-2255/`, ignorado pelo Git.
- Metadados e resultados resumidos: [métricas do piloto](2026-09-14-piloto-codex-metricas.json). Laudos do experimento não foram selados nem promovidos à biblioteca.
