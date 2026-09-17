# Processamento de MAC 3.0

Base de consulta das 15 transcrições disponíveis neste repositório. A seleção existente não comprova que todas as aulas do curso comercial estejam presentes. Fonte fixada no commit `2130e27fa65c9930a8ef1710bb75ad8fe06233c5`; hashes e caminhos no [manifesto](../conhecimento/manifest.json).

## Método e limites

- [Método comum](../../processamento/README.md) e [contrato](../../processamento/CONTRATO.md).
- Extração por aula, preservando números, condições, fontes, dúvidas e informações perecíveis.
- Inspeção independente de todas as aulas e unidades; os [laudos](revisao/inspecao/) informam o hash da versão inspecionada e os achados.
- Julgamento separado da amostra definida antes da extração: M01_A07 (risco), M02_A06 (alavancagem), M04_A02 (tela), usando unidades e evidências do inspetor. [Laudos da amostra](revisao/julgamento/).
- Correções localizadas e reinspeção quando há falhas; os laudos conservam seu histórico. Julgamento de seis aulas entre os dois cursos não equivale a julgamento integral.

Os tempos seguem a gravação local em 2×. Não houve nova escuta de áudio nem verificação externa da eficácia das técnicas. Afirmações financeiras são atribuídas ao instrutor; dúvidas aritméticas ou de transcrição permanecem explícitas. Conteúdo de interface exige conferência atual antes de uso. Índices não resolvem divergências entre aulas.

## Manutenção

Editar os JSONs em `conhecimento/dados/`, mantendo a identidade da unidade após a publicação, incrementando a versão quando alterar seu significado. Corrigir a inspeção e o julgamento aplicável para a versão nova. Reconstruir os arquivos derivados e executar, da raiz:

```sh
python3 processamento/base_consulta.py --course mac-3 --reviews --check
```

A extração assistida e a inspeção não são uma auditoria financeira nem garantia de ausência de omissões. O estado final e as contagens estão no [índice da base](../conhecimento/README.md).
