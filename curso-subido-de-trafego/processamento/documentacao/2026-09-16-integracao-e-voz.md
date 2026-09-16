# Integração do processamento e extração da voz

Execução autorizada por Will em 16/09/2026: integrar o processamento neste repositório, fazer commit e push, manter a biblioteca no Jarvis 4 e depositar a voz em `_entrada/voz-pedro-sobral/`. Essa decisão substitui a proposta anterior de deixar apenas um apontador no Vault.

## Entrega

- `conhecimento/`: base de 133 aulas e 2.829 unidades, 19 índices por tema e o playbook piloto parcial. Os 133 arquivos de unidades, FORMATO, taxonomia e selos foram preservados.
- `processamento/`: scripts adaptados ao repositório, testes, dados, método, laudos, documentação técnica e histórico. Os scripts não dependem do caminho do Jarvis.
- `voz/`: guia textual, evidências, amostras e quatro casos hipotéticos. Revisão técnica passou; aceite do tom e incorporação ao agente continuam pendentes.

As fontes e o inventário original permanecem na versão `f188775`. A verificação de 485 arquivos usa hashes, pois o HEAD pode avançar ao incorporar derivados. Nenhuma aula foi reextraída.

## Extração da voz

Inventário das 133 aulas, seleção de 12 aulas em oito módulos, três janelas por aula e reserva de outra aula por módulo: 44 janelas, 20 aulas distintas, 10.400 palavras. Os 36 trechos de extração foram analisados em dois lotes Terra; Sol sintetizou o guia; Astra avaliou os padrões e as quatro respostas, incluindo oito trechos reservados fora da síntese.

Uma citação candidata não coincidiu literalmente com a fonte e foi descartada antes da síntese. Cinco padrões usados no guia tiveram apoio em aulas distintas e reapareceram na reserva. Duas manifestações adicionais ficaram inconclusivas na reserva, conforme `voz/validacao.md`. O resultado é amostral, sem pretensão de identidade exclusiva ou análise integral das 133 transcrições.

O método de amostras reais mais orientação de voz foi inspirado na Q2/etapa 3 da skill `onboard` do Jarvis. A análise em lotes, conferência literal e avaliação reservada são adaptações deste trabalho. Não foi executado novo onboarding pessoal nem alterada a voz do Will.

Consumo das quatro chamadas: 149.771 tokens de entrada (11.776 em cache, incluídos), 5.870 de saída. Contextos isolados e nenhuma ferramenta chamada pelos modelos. Registros em `processamento/revisao/voz/`; pacotes de trabalho e logs transitórios permaneceram fora da publicação.

## Verificações

- Cópia em outro diretório, sem `.git` e sem dependência do Jarvis: 86 testes aprovados.
- Unidades: 133 arquivos, 2.829 unidades, zero erros e os mesmos 18 avisos históricos.
- Índices: `--check` aprovado; visões: zero erros e nenhuma dependência desatualizada.
- Integridade: fontes, arquivos de aulas, FORMATO, taxonomia e selos comparados com as origens.
- Voz depositada no Jarvis conferida byte a byte com `voz/`.
- Repositório de destino confirmado privado. Nenhuma alteração foi aplicada ao contrato do Gestor de Tráfego, à TC3 Lab ou às contas de clientes.

## Uso local e manutenção

A biblioteca do Jarvis e a pasta de voz são consultáveis sem este clone. As evidências da voz incluem os textos amostrados e links para fontes em versão fixa no repositório privado. Auditoria completa das fontes, nova extração ou regeneração dos índices exige este repositório; se o clone for retirado, clonar novamente para essa manutenção.

Playbooks e checklists continuam sob demanda. A entrega da voz é um candidato para avaliar o tom, não uma instalação no agente.
