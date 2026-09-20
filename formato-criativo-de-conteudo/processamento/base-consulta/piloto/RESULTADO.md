# Resultado do piloto

19/09/2026. Plano em [PLANO.md](PLANO.md), fixado antes das execuções. Todos os números abaixo saem dos arquivos `.execucao.json`, `.inspecao.json` e `.julgamento.json` das pastas `s5-high/`, `s5-medium/`, `o5-medium/`, `pacote-completo/` e `../calibracao/plantado/`.

Via de todas as chamadas: assinatura do Claude Code, `claude -p` headless 2.1.273, sem ferramentas. Batch API não existe nesta via. Custo em dólar é nominal, a preço de tabela; serve para comparar, não é cobrança.

## Escolha do extrator: Sonnet 5 em `high`

Aulas ouro `M03_A06` (Lapidação) e `M05_A02` (Branding Primitivo). Inspeção integral por Sonnet 5 `xhigh` e julgamento por Fable 5.1 `xhigh`, sem fonte, nas seis saídas.

| Configuração | Unidades (A06 / A02) | Erros de contrato na 1ª saída | Veredito A06 | Veredito A02 | Falhas consolidadas | Custo nominal até o veredito |
|---|---|---:|---|---|---:|---:|
| Sonnet 5 `high` | 18 / 21 | 0 | falha: fidelidade | **passa** | 2 | US$ 3,69 |
| Sonnet 5 `medium` | 14 / 14 | 2 | falha: contrato, fidelidade, perecibilidade, aplicabilidade | falha: contrato | 5 | US$ 3,62 |
| Opus 5 `medium` | 26 / 26 | 4 | falha: contrato, fidelidade, aplicabilidade | falha: contrato, fidelidade | 10 | US$ 5,76 |

Erros de contrato contados com o validador já corrigido (ver "Defeitos do pacote"). Sob a régua `perecivel` criada depois da calibração, a saída de Sonnet 5 `high` em `M03_A06` ganha um erro mecânico (U005, Trello sem marca de perecível).

Leitura:

- **Sonnet 5 `medium` não sustenta a rubrica.** Rodou sem raciocínio (`thinking_tokens: 0` nas duas aulas), produziu um terço a menos de unidades e inventou critério de decisão (`M03_A06` U5: gatilhos para trocar ou insistir no formato que o professor não dá). A economia esperada não existe: o extrator é 9% a 14% do consumo por aula, então cortar o esforço dele quase não mexe no total, e as falhas a mais custam ciclo de correção.
- **Opus 5 `medium` não é melhor que Sonnet 5 `high`.** Granularidade mais fina (26 unidades), mas dez falhas: título afirmando "comunidade paga" sem fonte, caso narrado virando procedimento, notas dizendo que o material confirma nomes que ele não confirma, divergência fala × material resolvida em silêncio. Custo nominal 56% maior.
- **Sonnet 5 `high`** passou direto em `M05_A02`, que tem a divergência mais séria do curso entre fala e material, e falhou em `M03_A06` por duas falhas localizadas: U12 generaliza o caso Sorocaba × Pantera em procedimento e acrescenta "duas ou três hipóteses" e "ritmo"; U12 e U17 deixam o agente com respostas opostas (mudar vários × um elemento por vez) sem avisar da tensão entre fala e material.

Decisão registrada: extrator = `claude-sonnet-5`, esforço `high`. A rota do README se confirma.

## Onde o consumo está

Configuração escolhida, duas aulas, até o veredito:

| Papel | Modelo e esforço | input | output | cache_creation | cache_read | Raciocínio (dentro do output) | Tempo | Nominal | Parte |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Extrator | Sonnet 5 `high` | 4 | 30.808 | 50.176 | 13.574 | 14.125 | 289 s | US$ 0,51 | 14% |
| Inspetor | Sonnet 5 `xhigh` | 4 | 77.911 | 70.080 | 13.970 | 67.955 | 712 s | US$ 1,06 | 29% |
| Juiz | Fable 5.1 `xhigh` | 4 | 24.076 | 45.225 | 13.506 | 15.300 | 279 s | US$ 2,11 | 57% |

Todas as chamadas terminaram com `stop_reason: tool_use` e `terminal_reason: completed`: a saída por esquema do CLI é entregue por uma chamada de ferramenta interna, em dois turnos. Nenhuma recusa, nenhuma ferramenta negada, nenhum erro de API.

**Cache de prefixo funciona.** Na segunda aula de cada rodada, `cache_read_input_tokens` ficou entre 13.506 e 13.970, que é o bloco fixo do papel mais o esquema. Na primeira é zero, como esperado. Dois achados para a rota por API:

1. O CLI também grava em cache o conteúdo da aula (`cache_creation` muito acima do bloco fixo). Na assinatura isso não pesa. Na API, escrever em cache um conteúdo que nunca será relido custa mais que entrada normal: o ponto de cache tem de ficar só no bloco fixo.
2. Editar o FORMATO ou a taxonomia invalida o cache de todos os papéis. Foi o que aconteceu entre o piloto e o teste de `M07_A01` (cache lido caiu para 1.658). Contrato congela antes do lote.

## Conferência do pacote completo: `M07_A01`

16.178 palavras, aula com convidado e oferta misturada. Sonnet 5 `high`: 52 unidades, 52.683 tokens de saída (32.131 de raciocínio), 498 s, US$ 0,86 nominal, `completed`. O teto de saída do CLI para o modelo é 64.000 tokens: a aula mais longa do curso usa 82% dele. Cabe, com folga pequena. A oferta virou dois `limite`, como o FORMATO pede; 19 das 52 unidades saíram perecíveis (preço, mercado, WhatsApp).

Saíram 3 erros mecânicos de contrato (dois títulos acima de 80 caracteres, um "hoje" no corpo). O **reparo de contrato** (`corrigir` sem julgamento, Sonnet 5 `high`, ciclo 0) corrigiu as 3 unidades em 19 s, 2.252 tokens de saída, sem tocar nas outras 49, e o validador zerou. O reparo roda antes da inspeção e não conta como ciclo de correção de conteúdo.

## Calibração com erro plantado

Sete defeitos plantados pela coordenação em cópias das extrações Sonnet 5 `high`, mais a falha real de U12 que já estava em `M03_A06`. Gabarito em `../calibracao/gabarito.json`, fora de qualquer pacote. Inspetor e juiz rodaram sem saber dele.

| Defeito | Inspetor | Juiz |
|---|---|---|
| P1 número adulterado (duas levas → três levas) | desvio, material | fidelidade ✔ |
| P2 condição suprimida (vídeo não pode ser de trend) | desvio, material | fidelidade ✔ |
| P3 caso e estimativa verbal promovidos a régua | desvio, material; também em perecibilidade | fidelidade ✔ |
| P4 omissão (decisão depois das duas levas retirada) | omissão material, com trecho e tempo | cobertura ✔ |
| P5 perecível sem marca (procedimento preso a link do Google Docs) | **não apontou** | **não vetou** |
| P6 regra condicionada virou lei para todo vídeo | desvio, material | fidelidade ✔ |
| P7 unidade sem lastro com âncora literal verdadeira | sem-lastro, material | fidelidade ✔ |
| E1 falha real preexistente (U12) | desvio, material, de novo | fidelidade ✔ |

6 de 7 plantados detectados pelo veto certo; a falha real foi reencontrada de forma consistente em execução independente; zero citação não literal do inspetor nas oito inspeções do piloto. Nenhum veto falso sobre unidade intacta.

**P5 escapou dos dois.** Causa: a lista de perecíveis não citava recurso do curso, e a conferência dependia de julgamento. Correção da causa, não da régua: virou regra de script. Qualquer plataforma além de `geral` exige `perecivel: true` [E]; a lista de perecíveis do FORMATO, da RUBRICA e do papel do inspetor ganhou "recurso do curso (link, documento-modelo, quadro, comunidade)". Reconferido: o validador agora barra o arquivo plantado em U003. A mesma regra achou 1 caso real em `M03_A06` e 6 em `M07_A01` que o extrator tinha deixado sem marca, o que confirma que o defeito era sistemático. O executor passou a aplicar essa marcação de forma determinística na extração e a registrar em `normalizacoes`.

Perecível escondido em unidade marcada `geral` continua dependendo do inspetor. No P3 ele apontou; é o único caso testado desse tipo.

## Defeitos do pacote achados e corrigidos no piloto

| Defeito | De quem | Correção |
|---|---|---|
| Régua exigia algarismo; o professor diz "duas levas de três vídeos" | validador | aceita número por extenso |
| Âncora que atravessa duas marcações de tempo vizinhas era reprovada | validador | comparação por sequência de palavras, sem marcações, caixa nem pontuação |
| Perecibilidade dependia só de julgamento | contrato | regra de script + normalização determinística |
| Títulos longos e marcador temporal escapam do extrator | extrator | passo de reparo de contrato antes da inspeção |

As três configurações foram revalidadas com o mesmo validador corrigido antes de irem para inspeção e julgamento.

## Pendente de decisão humana

`M03_A06` é referência ouro e foi reprovada (2 falhas de fidelidade, U12 e U17, mais 1 erro mecânico em U005). Pela rubrica, ouro reprovado não entra sozinho na fila do redator. A decisão é de Will.

## Projeção para o curso inteiro

Com Sonnet 5 `high` na extração, inspeção integral e julgamento nas 16 aulas da amostra, por regra de três sobre as médias do piloto (extrator ~US$ 0,26 por aula média, inspetor ~US$ 0,53, juiz ~US$ 1,05): extração das 54 aulas ~US$ 16, inspeção das 54 ~US$ 30, julgamento de 16 ~US$ 17, reparos e correções ~US$ 5 a 10. **Ordem de US$ 70 nominais**, que na assinatura se traduz em cota. Tempo de parede com três chamadas em paralelo: extração ~1 h, inspeção ~2,5 h, julgamento ~20 min. Os dois módulos mais caros são o 3 e o 7.
