# Cursos — acervo privado

Repositório central de fontes transcritas, materiais de apoio e conhecimento derivado dos cursos selecionados por Will. Os vídeos ficam no acervo local e, quando publicados, no Drive; este repositório reúne as transcrições, os materiais de apoio, as bases de conhecimento derivadas e as ferramentas de processamento.

## Cursos disponíveis

- [Curso Subido de Tráfego](curso-subido-de-trafego/README.md): 133 aulas, transcrições auditadas, materiais de apoio, base de conhecimento, processamento e voz textual.
- [Conversão Extrema](conversao-extrema/README.md): seleção atual de 149 aulas em 155 vídeos, com transcrição automática e manifesto. O áudio ainda não passou por revisão integral.
- [Lançamento Meteórico](lancamento-meteorico/README.md): 88 vídeos em dez módulos, transcrições automáticas, materiais de apoio e manifesto.
- [Formato Criativo de Conteúdo](formato-criativo-de-conteudo/README.md): 54 aulas em sete módulos, transcrições automáticas, materiais de apoio e manifesto; base de conhecimento por aula para consulta por agentes, com índices por tema e tarefa e laudos.
- [Hardcopy Pro](hardcopy-pro/README.md): 138 aulas completas em 19/09/2026, com transcrições automáticas e manifesto; áudio ainda sem revisão integral; base de conhecimento por aula para consulta por agentes, em construção: 100 de 139 entradas publicadas, com índices por tema e tarefa e laudos.
- [MAC 3.0](mac-3/README.md): 15 aulas com transcrição revisada em texto, base de conhecimento por aula, índices por tema e laudos; vídeos na pasta privada do Drive.
- [Análises Extraordinárias](analises-extraordinarias/README.md): 16 aulas da Águia Spread com transcrição revisada em texto, base de conhecimento por aula, índices por tema e laudos; vídeos na pasta privada do Drive.
- [Workshop Sistema de Demanda — Agência de Valor](workshop-sistema-de-demanda/README.md): oito aulas com transcrição automática revisada em texto; vídeos na pasta privada do Drive.

## Organização

Desde 22/09/2026 todos os cursos têm a mesma estrutura:

- `transcricoes/`: os módulos do curso, com um arquivo `<aula>.md` por aula (transcrição automática com tempos), os materiais de apoio em `Materiais/`, o índice geral e o manifesto que lista as aulas na ordem do curso.
- `conhecimento/`: as transcrições processadas, nos cursos já processados: unidades citáveis por aula nas mesmas pastas de `transcricoes/`, `unidades.jsonl`, índices por tema e tarefa, contrato e taxonomia.
- `processamento/`: scripts, laudos e registros de execução do curso. Os scripts compartilhados ficam em [processamento/](processamento/README.md).

Legendas, segmentos brutos do Whisper, metadados de captura e `status.json` saíram do checkout em 22/09/2026 porque nenhuma base os lê; ficam no histórico até o commit `0f82fa8`.

Cada curso tem sua própria pasta e índice. As fontes e conclusões de um curso não são automaticamente transferidas para outro. Conteúdo de uso restrito; manter o repositório privado.
