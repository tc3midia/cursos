# Processamento das bases MAC 3.0 e Análises Extraordinárias

Adaptação do método de unidades por aula utilizado no [Curso Subido](../curso-subido-de-trafego/processamento/README.md), executada em 16/09/2026. Este adaptador atende somente `mac-3` e `analises-extraordinarias`; os scripts e dados do Curso Subido permanecem próprios daquele curso.

## Entrega e organização

Cada curso conserva suas transcrições e recebe `conhecimento/` (dados por aula, unidades legíveis, manifesto e índices por tema) e `processamento/` (alcance da revisão e laudos). Uma unidade preserva a orientação, as condições, a faixa da fonte, uma âncora textual, confiança na interpretação e indicação de conteúdo perecível.

O [contrato](CONTRATO.md) define formato, taxonomia, responsabilidades e amostra antes da revisão. O JSON por aula é a fonte editável das unidades; os Markdown e índices são derivados determinísticos. IDs são exclusivos por curso e aula, com prefixo SHA-256 de 16 caracteres e número sequencial da unidade.

As fontes foram fixadas no commit `2130e27fa65c9930a8ef1710bb75ad8fe06233c5` de `tc3midia/cursos`. O manifesto registra o hash de cada transcrição. Timestamps seguem a gravação local em 2× e não são convertidos.

## Processo

1. Inventariar as 31 fontes e preservar seus hashes.
2. Ler cada aula e extrair orientações distintas, evitando tanto transcrição bruta quanto resumo que omita decisões e condições.
3. Validar campos, referências literais, faixas e cobertura de arquivos.
4. Confrontar fonte e unidades em contexto independente. Registrar achados e hash exato do JSON inspecionado; corrigir localmente e reinspecionar.
5. Julgar separadamente seis aulas predefinidas a partir das unidades e evidências de inspeção. O alcance exato é registrado por curso.
6. Gerar os índices, conferir que podem ser reproduzidos, publicar e confirmar o commit remoto.

Autoria: agentes Codex em contextos separados para extração e inspeção; coordenação para julgamento e verificações. Os identificadores internos dos modelos herdados não foram expostos ao contrato desta execução e não são presumidos a partir da experiência anterior. Não foram reutilizados laudos ou selos do Curso Subido.

Nesta execução, o julgamento foi cruzado: o extrator de MAC julgou somente as amostras de Análises, e o extrator de Análises julgou somente as de MAC, sem abrir as transcrições do curso julgado. O inspetor permaneceu em contexto separado. Os juízes solicitaram provas complementares e rejeitaram versões antes das correções; os pareceres preservam esse histórico.

## Fechamento de 16/09/2026

| Curso | Aulas disponíveis processadas | Unidades | Temas | Amostras julgadas |
|---|---:|---:|---:|---:|
| MAC 3.0 | 15/15 | 205 | 10 | 3 |
| Análises Extraordinárias | 16/16 | 193 | 10 | 3 |

As 31 aulas e 398 unidades receberam inspeção com fonte. O julgamento separado abrangeu seis aulas e 105 unidades; não foi julgamento integral das duas bases. As verificações mecânicas cobrem os 31 arquivos, as âncoras literais, os limites temporais, os índices, os links e os hashes atuais de inspeções e julgamentos. As 31 transcrições foram comparadas aos objetos Git do commit de origem e permaneceram intactas.

Foram corrigidas faixas, atribuições, números normalizados indevidamente, omissões de valores de exemplos, espaços de redação e marcações de informação perecível. Inconsistências presentes nas fontes foram preservadas como dúvidas. Os 12 testes do adaptador passaram, incluindo rejeição de evidência fora da faixa e invalidação de laudos após alteração dos insumos.

## Comandos de conferência

Requisitos: Python 3, somente biblioteca padrão. Executar da raiz do repositório:

```sh
python3 processamento/base_consulta.py --course mac-3 --reviews --check
python3 processamento/base_consulta.py --course analises-extraordinarias --reviews --check
python3 -m unittest discover -s processamento/tests
```

Para extrair enquanto algumas aulas ainda faltam, `--partial` verifica somente os arquivos presentes. Nunca utilizar esse modo como evidência de conclusão.

`--patch` emite um patch de reconstrução dos derivados; não escreve arquivos por conta própria. Para uma alteração deliberada, revisar o patch e aplicá-lo com uma ferramenta de edição. `--only caminho` limita a emissão a um único arquivo. Sem `--patch`, a ferramenta apenas valida. A alteração de um JSON exige reinspeção e novo hash; o comando `--reviews` rejeita laudos desatualizados.

## Limites

A base documenta os ensinamentos dos cursos; não confirma suas promessas, projeções ou eficácia financeira. Não houve escuta integral de áudio nesta etapa, nem validação atual de plataformas. Nomes duvidosos, números contraditórios e demonstrações perecíveis devem permanecer sinalizados. Índices de tema não resolvem conflitos entre aulas. Playbooks, estratégia de investimento, voz do professor e integração com agentes operacionais não fazem parte desta entrega.
