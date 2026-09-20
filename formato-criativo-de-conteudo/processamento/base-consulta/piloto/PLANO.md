# Plano do piloto

Registrado em 19/09/2026, antes de qualquer extração. A escolha das aulas, das configurações e da amostra fica fixada aqui para não ser ajustada depois de ver resultado.

## Via de execução

Assinatura do Claude Code, não API. Decisão de Will em 19/09/2026, porque a `ANTHROPIC_API_KEY` do Jarvis 4 fica vazia por desenho. Cada papel roda em um processo `claude -p` isolado, em diretório vazio, sem ferramentas, sem configurações do usuário, com modelo e esforço explícitos e saída por esquema JSON. Consequências em relação à rota escrita para a API:

- **Batch API não existe nesta via.** Extração e inspeção rodam como chamadas normais, em paralelo controlado. O campo "via" de cada execução registra isso.
- **Cache de prefixo** continua valendo: o bloco fixo do papel vai no system prompt, idêntico byte a byte entre aulas. A primeira aula de cada rodada roda sozinha para gravar o cache; as demais leem. Conferência por `cache_read_input_tokens`.
- O custo em dólar que o CLI devolve é **nominal** (preço de tabela), não cobrança. O que se consome de fato é cota da assinatura. Registram-se os quatro contadores e o custo nominal para comparar configurações.

## Aulas ouro

| Aula | Por quê |
|---|---|
| `M03_A06` Lapidação | Régua numérica real (levas de vídeos), procedimento, decisão condicionada (continuar ou trocar de formato), material de apoio relevante e nomes de criadores que variam entre fala e material |
| `M05_A02` Branding Primitivo | Estrutura de sete partes, números de caso que não podem virar régua, e divergência séria entre fala e material (exemplos classificados em categorias diferentes) |

## Configurações de extrator comparadas

1. `claude-sonnet-5`, esforço `high`
2. `claude-sonnet-5`, esforço `medium`
3. `claude-opus-5`, esforço `medium`

Mesmo pacote nas três. Cada saída passa por: validador, inspeção integral por `claude-sonnet-5` em `xhigh` (execução separada) e julgamento por `claude-fable-5-1` em `xhigh`, sem fonte.

## O que decide

Na ordem: (1) falhas materiais apontadas pelo juiz por aula; (2) omissões materiais; (3) erros de contrato na primeira saída; (4) consumo total até o veredito, incluindo o que a correção custaria. Se a configuração 2 sustentar a rubrica, ela vence por consumo. Se a 3 for claramente melhor que a 1 por consumo parecido, a rota muda. Empate de qualidade se resolve pelo menor consumo.

## Casos com erro plantado

Depois de escolhido o extrator, a coordenação planta defeitos conhecidos em cópias das duas extrações ouro, um arquivo por aula, e guarda o gabarito em `calibracao/gabarito.json`. Defeitos: número adulterado, condição suprimida, unidade sem lastro, número de caso promovido a régua, item perecível sem marca, e remoção de unidade que carrega parte essencial (omissão). Inspetor e juiz rodam sobre os arquivos plantados sem saber do gabarito. Mede-se, por defeito: o inspetor apontou? o juiz vetou pelo veto certo? Defeito não detectado manda corrigir papel ou rubrica antes de liberar lote.

## Conferência do pacote completo

Antes de liberar os demais módulos, o pacote roda em `M07_A01` (16 mil palavras, oferta misturada com aula) com a configuração escolhida, para testar tamanho e o tratamento de oferta.

## Amostra de julgamento para os lotes

Regra fixada aqui: inspeção com fonte em **todas** as aulas; julgamento nas duas ouro e em duas aulas por módulo, escolhidas pela ordem crescente de `aula_id`, excluídas as ouro.

`M01_A06`, `M01_A02`, `M02_A05`, `M02_A08`, `M03_A07`, `M03_A02`, `M04_A03`, `M04_A01`, `M05_A07`, `M05_A01`, `M06_A08`, `M06_A05`, `M07_A02`, `M07_A01`.

São 16 aulas julgadas de 54 (30%). A seleção alcança oferta (`M01_A06`, `M07_A01`), Q&A (`M07_A02`), divergência de material (`M05_A01`) e aulas de formato dos módulos 2 e 4. Aula fora da amostra em que a inspeção apontar falha material entra no julgamento como conferência adicional, registrada como tal.

Ajuste de 20/09/2026, depois do lote 2: o gatilho da conferência adicional passa a ser qualquer `desvio` ou `sem-lastro` registrado pelo inspetor, mesmo com gravidade menor, além de apontamento material, omissão material e perecível sem marca. Motivo: a gravidade é decisão do juiz, e em `M01_A01` a primeira inspeção classificou como menor uma falha que uma segunda inspeção e o juiz trataram como material. A lista da amostra não muda. Segundo ajuste, depois do lote 4: faixa errada em mais de 10% das unidades com faixa também aciona a conferência, porque a rubrica reprova nesse limiar e a conta é objetiva. Nasceu de `M04_A03`, aula da amostra com inspeção sem apontamento material que o juiz reprovou por isso.

Teto de correção: dois ciclos por artefato, depois uma intervenção da coordenação e uma conferência focal final, conforme a RUBRICA.
