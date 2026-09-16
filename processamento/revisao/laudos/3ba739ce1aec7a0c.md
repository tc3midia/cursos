---
type: laudo
aula_id: 3ba739ce1aec7a0c
arquivo: unidades/001-0-0-como-tirar-o-melhor-proveito-do-curso.md
rodada: 2
veredito: passa
vetos: []
gerado_por: fable-5.1
isolamento: ok
insumos_hash: 758ff73a1e034b1d6116608b6842228b0da55931b86f3d96e58083c8fbc345a9
---

# Laudo — 3ba739ce1aec7a0c (rodada 2)

Insumos: arquivo de unidades (19 unidades vivas, `retiradas: []`), pacote do inspetor `3ba739ce1aec7a0c.evidencia.md` (rodada 1), RUBRICA.md, FORMATO.md §8, taxonomia.md e saída do validador `{"arquivos": 1, "unidades": 19, "erros": [], "warnings": []}`. Não abri transcrição, PDF, clone, memos, playbooks, `_saida/` nem o laudo da rodada 1. A rodada 1 apontou dois itens (F1: U:017; F2: régua do fecho sem unidade própria); esta rodada confere só a correção deles e reaplica os vetos ao arquivo inteiro.

## Fidelidade

- 16 unidades `lastreada` na tabela do inspetor, sem alteração de corpo desde a rodada 1 (versões só mudaram por retag de tarefa, registrado em `nota`): mantidas.
- U:017 (`desvio` na rodada 1): o corpo agora traz "15 anos" e "120 aulas", que é exatamente o que a evidência cita em [00:06:41–00:07:19]; `versao: 3` e `nota` registram a correção manual e avisam que é hipérbole. O desvio foi sanado; trato como lastreada.
- U:019 (nova, sem linha na tabela): julgada pela seção de omissões da evidência, que transcreve a frase da fonte na faixa [00:06:41–00:07:19]. O corpo reproduz os três números (100%, 50%, 50%) e a condição da segunda metade ("gestão de tráfego do próprio negócio") sem inventar rótulo para o 100%, que a frase citada não atribui a perfil. `faixa` bate com a da evidência; `condicoes` reflete a condição que a fonte impõe; `confianca: media` com `nota` que explica o conflito de rótulos com U:007 e U:010 e o encaminha à consolidação, sem suprimir. Lastreada.
- U:010 (`desvio`, `confianca: media`, nota explica a inversão de rótulo no fecho): passa com registro, como na rubrica. O par U:010/U:019 fica declarado nos dois lados; a resolução é da consolidação, não do redator.
- `faixa-errada`: nenhuma. Nenhum `sem-lastro`. Nenhum desvio com `confianca: alta`.

## Cobertura

- A única omissão da evidência (régua 100% / 50% e 50% do fecho) agora tem unidade própria, U:019, do tipo `regua`, com número e condição.
- O inspetor declara que nenhum outro número, passo, decisão condicional ou alerta de tela ficou sem unidade e que não há memo v1 para cruzar. Sem omissão pendente.

## Perecibilidade

- U:001 é `alerta-ui` com `perecivel: true`.
- U:016 descreve caminho de uso da tela (lupa de pesquisa da comunidade) e está `perecivel: true`; U:012 e U:015 dependem de contagem que muda e também estão marcadas.
- U:019 não descreve tela nem contagem; `perecivel: false` está correto. Nenhuma unidade nova ou alterada introduziu descrição de tela sem marca.

## Contrato

- Validador com zero erros e zero warnings para 19 unidades. Identidade fechada: presentes 001..019, `retiradas`, `divisoes` e `fusoes` vazias, número novo atribuído após o maior existente.
- Inspetor (rodada 1) confirma zero sequências de 25 palavras copiadas e `fontes` batendo com o disco (só `transcricao.md`). U:019 e o novo corpo de U:017 não passaram por esse n-grama no pacote; comparando com as frases que a evidência transcreve, ambos parafraseiam e nenhum reproduz sequência longa da fonte. Registro, não veto.
- Registro: U:017 é `regra` com números no corpo (15 anos, 120 aulas). O FORMATO diz "sem número obrigatório" e o validador aceita; a taxonomia diz "sem número". Os números são hipérbole do professor, não critério observável, então `regra` continua sendo o tipo certo. Fica anotado para a triagem da taxonomia decidir se ajusta a definição.
- Registro herdado da rodada 1: `gerado_por: opus-5` numa aula de 1492 palavras destoa da regra de escolha de modelo do extrator; ambos os valores são válidos no enum e isso não é veto.

## Falhas

Nenhuma. Os dois itens da rodada 1 (F1: U:017; F2: U:019) foram corrigidos e nenhum veto novo se acionou.

## Próximo

nada
