# Dados técnicos do Curso Subido

Antiga pasta `biblioteca/curso-subido-trafego/_gerado`, retirada da navegação de leitura em 16/09/2026.

| Arquivo | Função |
|---|---|
| `unidades.jsonl` | Índice das unidades, IDs, versões e hashes. |
| `cobertura.jsonl` | Matriz de tarefas e plataformas com conteúdo disponível. |
| `propostas_tags.md` | Propostas de classificação ainda fora da taxonomia. |
| `desatualizadas.md` | Derivados que precisam de revisão após mudança dos insumos. |
| `selos.jsonl` | Registro das versões utilizadas na revisão dos derivados. **Preservar: não é apenas cache.** |

`build_indices.py` regenera os índices e o relatório de desatualização; não substitui a revisão humana/modelo nem recria o histórico de aceite de `selos.jsonl`. Os identificadores `_gerado/…` e `revisao/…` são mantidos na API e nos registros para preservar compatibilidade.

Fontes e unidades ficam na [biblioteca](../../conhecimento/README.md); verificações e comandos no [guia da ferramenta](../README.md).
