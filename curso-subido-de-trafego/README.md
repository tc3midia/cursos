# Curso Subido de Tráfego — fontes, conhecimento e voz

Repositório privado com as transcrições locais das aulas do Curso Subido de
Tráfego. Os vídeos originais não fazem parte deste repositório.

## Comece pela necessidade

| Preciso de… | Abro |
|---|---|
| Aulas originais e materiais de apoio | [Índice das fontes](transcricoes/00%20-%20%C3%8Dndice%20geral.md) |
| Orientações já extraídas | [Conhecimento](conhecimento/README.md): 133 aulas, 2.829 unidades e índices por tema |
| Jeito de comunicar do professor, adaptado para um gestor | [Voz textual](voz/README.md): guia, evidências e exemplos para avaliar |
| Método, scripts e revisão | [Processamento](processamento/README.md) |

## Estado do material

- 133 aulas distribuídas em 8 módulos
- aproximadamente 44 horas e 25 minutos de conteúdo
- transcrição em português brasileiro com Whisper `large-v3-turbo`
- lote auditado: 133/133 aulas aprovadas, sem falhas ou alertas pendentes

## Estrutura

Cada aula possui uma pasta própria com:

- `transcricao.md`: texto organizado em parágrafos com timestamps
- `segmentos.json`: saída estruturada, metadados e proveniência
- `legenda.srt`: legenda compatível com players e editores
- material de apoio da aula, quando existir (PDF e, em alguns casos, `.txt`)

Aulas sem arquivo extra são aulas para as quais não havia material para baixar. Os materiais
não ficam numa pasta `Materiais/` paralela: ficam junto da transcrição da mesma aula.

Arquivos na raiz:

- `00 - Índice geral.md`: navegação por módulo e aula
- `manifest.jsonl`: inventário verificável de todo o lote

## Uso

O processamento de conhecimento foi incorporado do Jarvis 4. A revisão das unidades foi por amostragem; playbooks e checklists completos serão produzidos sob demanda. A voz textual é uma entrega separada da voz sonora e permanece sujeita à avaliação do tom antes de entrar no agente.

A transcrição é um derivado automatizado e não substitui uma conferência palavra por palavra com o áudio original. A versão de origem das fontes é `f188775`; novos commits podem acrescentar derivados sem alterar os materiais originais.

## Privacidade

Conteúdo de uso restrito. Não tornar este repositório público nem redistribuir
os arquivos sem autorização do titular do material.
