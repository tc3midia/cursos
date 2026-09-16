---
type: laudo
arquivo: revisao/calibracao/f4.md
tarefa: diagnosticar-concentracao-de-verba
rodada: 0
veredito: falha
vetos: [aplicabilidade]
isolamento: ok
gerado_por: fable-5.1
insumos_hash: 48897b384f5c5f045db2746533cf42499e97cdd5030b9583f52fb033f724c7a7
---

# Laudo — fixture f4

Insumos lidos: `revisao/papeis/juiz.md`, `revisao/RUBRICA.md`, `FORMATO.md` §6.1 e §8, o artefato
`revisao/calibracao/f4.md`, o arquivo de unidades `unidades/005-4-0-minha-campanha-esta-gastando-toda-verba-em-um-unico-grupo-de-anuncio-e-agora.md`
(aula `869445a4c64befbf`, 17 unidades) e a linha da tarefa em `taxonomia.md`. Nenhum insumo continha
fonte bruta. Julgado como playbook real com `parcial_ate: "005"`.

## Contrato

Validador não roda fora de `visoes/`; checagens do §6.1 aplicadas à mão:

- Seções fixas: as nove presentes, na ordem exigida (Quando usar → Pré-condições → Passos por
  plataforma → Réguas e critérios de pronto → Decisões → Não fazer → O que o curso não cobre → Sem
  resolução no curso → Perecível). Ok.
- Subseções de `Passos por plataforma`: matriz pede `meta, youtube, google-display`; o playbook tem
  `youtube`, `google`, `meta`, `google-display`. As três da matriz estão presentes; `google` é extra.
  Ok.
- Citações: todos os bullets (`- ` e `1.`) das seções 1–6 e 9 terminam com `U:`. As seções 7 e 8
  também citam ou declaram ausência. Ok.
- IDs citados (001, 002, 003, 004, 005, 006, 007, 008, 009, 010, 011, 012, 013, 014, 015, 017):
  todos existem no arquivo de unidades; `retiradas: []`. Ok.
- Registro (sem veto): front matter `plataformas: [youtube, google]` não bate com a matriz
  (`meta, youtube, google-display`); `Sem resolução no curso` usa "Nada até o módulo 005
  (consolidação ainda não rodou)." em vez da fórmula "Nada nas fontes."; cópia bruta (25 palavras)
  não verificável sem pacote do inspetor.

Veredito do veto 1: passa.

## Aplicabilidade

Seis critérios do veto 5:

1. Pré-condições listam o ponto de partida — **atende**: acesso à campanha com leitura de gasto, custo
   real e lance por grupo (U:007), lance manual CPV máximo (U:017), ação valorizada pelo lance (U:001).
2. Subseção por plataforma da matriz — **atende**: `youtube` com 7 passos ordenados; `meta` e
   `google-display` declaram ausência citando U:017 (tipo `limite`). Registro: U:017 nomeia só Meta
   Ads, não Display; a subseção extra `google` cita U:001 (conceito) para uma generalização que o corpo
   da unidade não faz.
3. ≥1 régua observável — **atende**: R$ 0,30 → R$ 0,45 e +R$ 0,05 (U:009), R$ 10/dia por campanha
   (U:012), meta diária de visualizações/conversões (U:005).
4. `O que o curso não cobre` e `Sem resolução no curso` — **atende**: ambas preenchidas; a segunda
   declara vazio por consolidação pendente, compatível com `parcial_ate`.
5. Tipo compatível — **atende com registro**: passos do YouTube citam `decisao`/`regra`/`procedimento`;
   passo 1 de `google` cita `conceito` (U:001); réguas citam `decisao` (005, 006), `exemplo` (009) e
   `procedimento` (012), só uma cita `regua` (008). Não pesa sozinho; o arquivo só tem uma unidade
   `regua`.
6. A unidade citada sustenta a afirmação — **não atende**: três bullets citam unidade que diz número,
   condição ou sentido diferente (tabela abaixo, linhas marcadas "não").

| bullet (resumo) | citação | sustenta? | observação |
|---|---|---|---|
| **Quando usar** | | | |
| Campanha gasta tudo num grupo, outros sem gasto | U:002 | sim | 002 descreve o gasto indo todo ao frio e quentes sem verba |
| Se entrega visualizações/conversões diárias, concentração não é o problema | U:005 | sim | literal |
| Problema real é concentração sem decisão consciente; com metas batendo, pode ficar | U:014 | sim | literal |
| **Pré-condições** | | | |
| Acesso com leitura de gasto, custo real e lance por grupo | U:007 | sim | pré-condição da 007 |
| Lance manual por grupo (CPV máximo); não cobre automáticos | U:017 | sim | literal |
| Saber qual ação o lance valoriza; Google concentra onde ela sai mais barata | U:001 | sim | literal |
| **Passos — youtube** | | | |
| 1. Compare lances; R$ 3 vs R$ 0,30 = diagnóstico 3 | U:006 | sim | 006 manda comparar lances antes de tudo |
| 2. Compare audiências; grupo muito mais amplo = diagnóstico 1 (frio + quente juntos) | U:002 | sim | literal |
| 3. Todos quentes e um menor concentra = diagnóstico 2 | U:003 | sim | literal |
| 4. Pause o grupo que concentra por 48 horas para redistribuir | U:004 | **não** | 004 diz o oposto ("não pause"; pausar piora a campanha) e não há "48 horas" em nenhuma unidade; contradiz o próprio `Não fazer` |
| 5. Solução 1: reduz lance de quem concentra, sobe nos qualificados (mais em zero, menos em pouco); espera | U:007 | sim | passos 1–4 da 007 |
| 6. Solução 2 se a 1 não resolveu: públicos-alvo → exclusões → remover | U:010 | sim | pré-condição e passos da 010 |
| 7. Solução 3: isolar em campanha própria, orçamento por campanha, ≥2 públicos em cada | U:012 | sim | "em cada" extrapola levemente: 012 pede +1 frio na campanha fria; 013 (não citada aqui) dá o "pelo menos dois" |
| **Passos — google** | | | |
| 1. Três diagnósticos e três soluções valem para Google Ads com lance manual; aula demonstra em YouTube | U:001 | parcial | 001 só descreve o mecanismo de concentração; não afirma que as três soluções valem para Google Ads em geral; apoio vem apenas do campo `plataforma` das unidades |
| 2. Sequência e espera são as mesmas | U:011 | sim | 011 é a regra de escalada |
| **Passos — meta** | | | |
| Nada nas fontes até 005; entra com módulo 002 | U:017 | sim | 017 declara não cobrir Meta Ads |
| **Passos — google-display** | | | |
| Nada nas fontes até 005; entra com módulo 006 | U:017 | parcial | 017 não menciona Display; só diz que a aula trata YouTube |
| **Réguas e critérios de pronto** | | | |
| Lance ~10x acima (R$ 3 vs R$ 0,30) explica sozinho | U:006 | sim | "10 vezes" é a razão do exemplo, não limiar dito pelo professor; registro |
| Reduza o lance de quem concentra em exatamente 20% a cada rodada | U:008 | **não** | 008 fala de R$ 0,30 → R$ 0,05 e da distância lance/custo real; nenhum percentual; 007 e 017 dizem que o quanto reduzir é "feeling" |
| Zerado e qualificado R$ 0,30 → R$ 0,45; que gastaram pouco +R$ 0,05 | U:009 | sim | literal |
| Pronto quando entrega visualizações/conversões diárias desejadas, mesmo desigual | U:005 | sim | literal |
| Ao isolar, orçamento explícito por campanha (R$ 10/dia cada) | U:012 | sim | passo 3 da 012 |
| **Decisões** | | | |
| Metas diárias batendo, não mexa | U:005 | sim | literal |
| Pressa → solução 3 direto; sem pressa → 1, 2, 3 com espera | U:015 | sim | literal |
| Lance muito maior → regule o lance antes de qualquer outra coisa | U:006 | sim | 006 diz "compare antes de qualquer outra ação"; regular é a solução 1, primeira da escalada; sentido preservado |
| **Não fazer** | | | |
| Pausar o grupo que concentra e traz resultado | U:004 | sim | literal (e contradiz o passo 4 do youtube) |
| Aplicar as três soluções de uma vez | U:011 | sim | literal |
| Criar campanha com menos de 3 públicos ao isolar | U:013 | **não** | 013 diz "pelo menos dois públicos"; o bullet proíbe campanha com 2, que a unidade permite |
| **O que o curso não cobre** (sem obrigação de citar) | | | |
| Quanto mexer no lance e quantos dias: feeling / uns dias | U:017 | sim | literal |
| Lances automáticos e o problema em Meta Ads ou Display | U:017 | parcial | Display não está em 017 |
| **Perecível** | | | |
| Caminho de tela para remover exclusões descreve a UI na data da aula | U:010 | sim | 010 tem `perecivel: true` |

Veredito do veto 5: **falha** (critério 6).

## Fidelidade

Sem pacote do inspetor para playbook; coerência bullet ↔ unidade conferida no corpo das unidades.
Três divergências de confiança alta, já contadas no veto 5:

- Passo 4 (youtube) inverte o sentido de U:004 e acrescenta número ("48 horas") ausente da fonte.
- Régua "exatamente 20%" acrescenta número ausente de U:008 e contraria U:007/U:017 ("feeling").
- "Menos de 3 públicos" troca o número de U:013 ("pelo menos dois").

O playbook contradiz a si mesmo: o passo 4 manda pausar o que o `Não fazer` (mesma citação U:004)
proíbe. Um agente executando amanhã não teria como resolver o conflito só com o playbook.

Divergências menores (registro): passo 1 de `google` generaliza além do corpo de U:001; "10 vezes"
apresentado como régua quando U:006 só dá um exemplo.

## Cobertura

Unidades marcadas com a tarefa no arquivo 005-4-0: 001, 002, 003, 004, 005, 006, 007, 009, 010, 011,
012, 014, 015. O playbook usa todas, mais 008, 013 e 017 (pertinentes, não marcadas). Nenhum outro
arquivo em `unidades/` marca a tarefa até o módulo 005. Sem omissão de número, passo ou condição.

Registro de contexto (sem veto): o passo 1 de U:012 (nomear a campanha nova com o mesmo nome e sufixo
quente/frio) e o passo 4 (o público frio adicional pode ser palavras-chave, interesses ou afinidade)
foram comprimidos no bullet da solução 3.

## Perecibilidade

Única unidade `perecivel: true` citada é U:010 (caminho de clique públicos-alvo → exclusões), e a
seção `Perecível` a declara. Nenhuma `alerta-ui` citada. Nenhum "hoje"/"atualmente" no corpo. Passa.

## Falhas

- youtube/passo 4 → U:004: unidade diz "não pause o grupo que concentra"; bullet manda pausar; "48 horas" não existe em nenhuma unidade. Remover o passo ou reescrever no sentido de U:004.
- Réguas/bullet 2 → U:008: "exatamente 20% a cada rodada" não consta da unidade; U:007 e U:017 dizem que o quanto reduzir é feeling. Remover o percentual.
- Não fazer/bullet 3 → U:013: unidade diz "pelo menos dois públicos"; bullet diz "menos de 3". Corrigir para "menos de 2".
- google/passo 1 → U:001: corpo da unidade não afirma que os três diagnósticos e soluções valem para Google Ads em geral. Citar unidade que sustente ou rebaixar a afirmação ao que 001 diz.

## Próximo

redator
