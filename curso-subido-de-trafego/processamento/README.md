# Processamento do Curso Subido

Scripts, método, dados e evidências que produziram a [base de conhecimento](../conhecimento/README.md). Incorporados do Jarvis 4 em 16/09/2026. Nenhuma aula foi reextraída nesta integração.

| Local | Conteúdo |
|---|---|
| `scripts/` | Leitura das fontes, pacotes, índices, reconciliação e validação |
| `tests/` | Testes e fixtures com defeitos conhecidos para calibração |
| [metodo/](metodo/README.md) | Rubrica e papéis preservados |
| [dados/](dados/README.md) | Índices, selos e hashes das fontes |
| [revisao/](revisao/README.md) | Laudos da amostra, evidências e avaliação piloto |
| `documentacao/` | Specs e registros técnicos, datados e com limites históricos |
| [historico/](historico/README.md) | Execuções anteriores e rastreabilidade das movimentações |

## Executar neste repositório

Python 3.10+ e `pdftotext` disponível no PATH para PDFs. Python usa apenas a biblioteca padrão. Rodar a partir da raiz:

```bash
python3 processamento/scripts/validate_unidades.py
python3 processamento/scripts/build_indices.py --check
python3 processamento/scripts/validate_visoes.py --playbooks --desatualizadas
python3 -m unittest discover -s processamento/tests -p 'test_curso_subido_*.py'
```

`build_indices.py` sem `--check` atualiza índices. `pacote.py pendentes` lista aulas ainda sem unidades. Outros modos montam pacotes para extração, inspeção e tarefas. Pacotes e logs temporários devem ficar fora do controle de versão. Nenhum comando acima chama um modelo ou publica mudanças.

## Caminhos e versões

O padrão usa `conhecimento/` e as fontes na raiz deste repositório. `CURSO_SUBIDO_CLONE` permite apontar para outra cópia das fontes; os 485 arquivos de origem são conferidos contra `dados/fontes-originais.json`. O HEAD pode avançar com novos derivados sem mudar a fonte `f188775`.

`FORMATO.md`, taxonomia, IDs e selos foram mantidos. Os identificadores lógicos `_gerado/…` e `revisao/…` são preservados, com resolução para `processamento/dados/` e `processamento/revisao/`. Bases avulsas em `--root` continuam autocontidas com `_gerado/` e `revisao/`; para elas, copiar os respectivos dados e método quando necessários.

Rubrica, papéis e documentos históricos contêm nomes de pastas usados no Jarvis. Nesta instalação: os scripts ficam em `processamento/scripts/`, a calibração em `processamento/tests/calibracao/`, os papéis em `processamento/metodo/papeis/` e as unidades em `conhecimento/unidades/`. Os pacotes incluem o conteúdo necessário; nomes antigos não indicam que é preciso ter o Jarvis instalado.

Selos verificam dependências registradas, não cobertura integral das fontes nem aprovação automática de interfaces atuais. A matriz e a avaliação de uso do piloto não são procedimentos completos para todas as tarefas.
