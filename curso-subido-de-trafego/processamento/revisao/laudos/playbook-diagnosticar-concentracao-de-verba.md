---
type: laudo
arquivo: visoes/playbooks/diagnosticar-concentracao-de-verba.md
tarefa: diagnosticar-concentracao-de-verba
rodada: 3
veredito: passa
vetos: []
isolamento: ok
gerado_por: fable-5.1
insumos_hash: 964a788a4e432a5125ecfcde5e64cc116542d156a296f437d9aab4e3c6fcdcbd
---

# Laudo — playbook diagnosticar-concentracao-de-verba (rodada 3)

Insumos abertos: `revisao/papeis/juiz.md`, `revisao/RUBRICA.md`, `FORMATO.md` §6.1 e §8, o playbook,
`unidades/005-4-0-...md` (corpo completo, 17 unidades), a linha da tarefa em `taxonomia.md` e a saída de
`validate_visoes.py --playbooks`. Não abri transcrição, PDF, clone, memos, histórico, calibração nem os laudos
`*.rodada-0/1/2.md` deste playbook. Nenhum arquivo aberto continha fonte bruta colada.

## Contrato

- `validate_visoes.py --playbooks`: `0 erros`.
- Front matter completo (`type: playbook`, `tarefa`, `plataformas`, `parcial_ate: "005"`, `rodada: 3`, `insumos_hash`).
- Nove seções fixas presentes e na ordem de §6.1 (linhas 21–79).
- Todos os bullets das seções 1–6 e 9 terminam com ≥1 citação `U:`; os bullets da seção 7 também citam. Nenhum bullet sem lastro.
- Sem "hoje"/"atualmente" no corpo.
- Nenhuma citação a ID retirado (`retiradas: []` no arquivo de unidades).
- Registro (não veto): `plataformas: [youtube]` no front matter enquanto a matriz espera `meta, youtube, google-display`; coerente com `parcial_ate: "005"` e com a nota de calendário no cabeçalho, e o script aceita.

## Aplicabilidade

Pergunta única: um agente executa a tarefa amanhã só com o playbook e a unidade 005-4.0? Sim, dentro do escopo declarado (YouTube, lance manual CPV máximo).

Seis critérios do veto 5:

1. **Pré-condições listam o ponto de partida** — atende. Acesso à campanha com leitura de gasto/custo/lance por grupo (`U:…:007`), lance manual por grupo (`U:…:017`), conhecimento da ação valorizada pelo lance (`U:…:001`).
2. **Subseção por plataforma da matriz** — atende. Matriz (`taxonomia.md` linha 84): `meta, youtube, google-display`. O playbook tem `### youtube` com 7 passos ordenados, e `### meta` e `### google-display` com "Nada nas fontes até o módulo 005" citando `U:…:017` (tipo `limite`), cujo corpo diz que a aula demonstra só em YouTube com CPV máximo e que outras redes do Google e Meta Ads não aparecem. A contradição da rodada anterior não existe mais: as unidades citadas nos passos estão todas em `plataforma: [youtube]`; só `U:…:001` (conceito geral sobre o leilão do Google) mantém `[youtube, google]`, e ela é citada em Pré-condições como conceito, não como passo de google-display.
3. **≥1 régua observável** — atende. `U:…:008` (tipo `regua`): lance R$ 0,30 vs custo real R$ 0,05; lance no nível do custo real tende a não gastar. Critério de pronto cita `U:…:005` (`decisao`), permitido.
4. **"O que o curso não cobre" e "Sem resolução no curso" preenchidos** — atende. Seção 7 com dois bullets lastreados (`U:…:017`, `U:…:009`); seção 8 declara "Nada até o módulo 005 (consolidação ainda não rodou)", coerente com `parcial_ate`.
5. **Tipo compatível por seção** — atende. Passos: 006/002/003/005/015 (`decisao`), 004/013 (`regra`), 007/010/012 (`procedimento`). Régua: 008 (`regua`). "Nada nas fontes": 017 (`limite`). Perecível cita `U:…:010` (`procedimento` com `perecivel: true`); a aula não tem `alerta-ui`, e a unidade citada é exatamente a que carrega o caminho de clique perecível — compatível com a função da seção. Registro, não veto.
6. **A unidade citada sustenta a afirmação** — atende em todos os bullets (tabela abaixo). Números conferidos no corpo: R$ 3 vs R$ 0,30 (006); R$ 0,30 → R$ 0,05, R$ 0,45, +R$ 0,05 (009); lance R$ 0,30 / custo R$ 0,05 (008); R$ 10/dia por campanha (012).

| bullet (resumo) | citação | sustenta? | observação |
|---|---|---|---|
| **Quando usar** — verba toda em um grupo/conjunto, outros sem gasto | 002 | sim | 002 descreve o grupo que concentra e "os quentes ficam sem verba"; "conjunto" é sinônimo do playbook, não aparece na unidade (registro) |
| Quando usar — se entrega visualizações/conversões diárias desejadas, concentração não é problema | 005 | sim | corpo idêntico em condição e sentido ("não é o maior problema") |
| Quando usar — problema é concentração sem decisão consciente; com metas batendo pode ficar | 014 | sim | corpo: "o problema é não ter consciência disso nem ter decidido que está tudo bem" |
| **Pré-condições** — acesso com leitura de gasto, custo real e lance por grupo | 007 | sim | pré-condição explícita em 007 |
| Pré-condições — lance manual por grupo (CPV máximo); não cobre automáticos | 017 | sim | 017: "lance manual de CPV máximo; … lances automáticos … não aparecem" |
| Pré-condições — saber qual ação o lance valoriza; Google concentra onde ela sai barata | 001 | sim | tipo `conceito`, aceitável em pré-condição |
| **youtube 1** — comparar lances; R$ 3 vs R$ 0,30 = diagnóstico 3 | 006 | sim | número e condição iguais |
| youtube 2 — comparar tamanho de audiência; amplo = diagnóstico 1, quente+frio juntos | 002 | sim | — |
| youtube 3 — todos quentes e um menor concentra = diagnóstico 2 (ação valorizada) | 003 | sim | — |
| youtube 4 — não pausar o grupo que concentra e traz resultado | 004 | sim | — |
| youtube 5 — Solução 1: reduzir lance de quem concentra, subir mais em quem zerou, menos em quem gastou pouco; esperar dias | 007 | sim | passos 1–4 de 007 |
| youtube 6 — Solução 2, se a 1 não resolveu: públicos-alvo → exclusões → remover | 010 | sim | pré-condição e passos 1–3 de 010 |
| youtube 7 — Solução 3, se anteriores falharam: isolar em campanha própria, R$ 10/dia cada, ≥2 públicos em cada | 012, 013 | sim | 012 traz orçamento e "pelo menos mais um público frio"; 013 generaliza "pelo menos dois públicos" para campanha nova |
| **meta** — Nada nas fontes até 005; só YouTube; Meta Ads não aparece | 017 | sim | tipo `limite`; corpo cita Meta Ads explicitamente |
| **google-display** — Nada nas fontes até 005; só YouTube CPV máx.; outras redes Google não aparecem | 017 | sim | tipo `limite`; corpo cita "outras redes do Google" |
| **Réguas** — custo real bem abaixo do lance (R$ 0,30 / R$ 0,05); lance = custo real tende a não gastar | 008 | sim | tipo `regua`; sentido "provavelmente … não consegue gastar" preservado |
| Réguas — critério de pronto: entrega visualizações/conversões diárias desejadas mesmo com gasto desigual | 005 | sim | `decisao` como critério de pronto, permitido |
| **Decisões** — metas diárias batendo → não mexa | 005 | sim | "não se preocupe com o grupo que não gasta"; reforçado por 014 |
| Decisões — pressa → solução 3 direto; sem pressa → 1, 2, 3 com espera | 015 | sim | a "espera entre elas" vem de 011, mas 015 já fixa a ordem 1→2→3 (registro) |
| Decisões — lance muito acima (R$ 3 vs R$ 0,30) é o diagnóstico; comparar lances antes de tudo | 006 | sim | frase "antes de qualquer outra ação" está em 006 |
| **Não fazer** — pausar grupo que concentra e traz resultado | 004 | sim | — |
| Não fazer — aplicar as três soluções de uma vez | 011 | sim | — |
| Não fazer — campanha com um único público ao isolar | 013 | sim | — |
| **Não cobre** — quanto ajustar lance / quantos dias ("feeling", "uns dias"); valores ao vivo são exemplo | 017, 009 | sim | 009 é `exemplo` com exatamente os valores citados |
| Não cobre — lances automáticos e Meta Ads | 017 | sim | — |
| **Perecível** — caminho de tela para remover exclusões descreve a UI na data da aula | 010 | sim | 010 tem `perecivel: true` e os passos de clique |

## Fidelidade

Sem pacote de inspetor para playbook; a fidelidade foi conferida bullet a bullet contra o corpo das unidades (tabela acima). Nenhum número, condição ou sentido diverge do que a unidade citada diz. Nenhuma afirmação sem unidade. Nenhuma complementação de UI atual: o único caminho de clique vem de 010 e está marcado perecível.

## Cobertura

Unidades da aula 005-4.0 etiquetadas com `diagnosticar-concentracao-de-verba`: 001, 002, 003, 004, 005, 006, 007, 009, 010, 011, 012, 014, 015 — todas citadas no playbook. Também citadas, sem etiqueta da tarefa: 008 (régua), 013 (regra de ≥2 públicos), 017 (limite). Não citada: 016 (nomenclatura 00/01/02), etiquetada `nomear-campanhas`, fora desta tarefa. Os três diagnósticos, as três soluções em escalada, a regra de não pausar, a regra de uma solução por vez e as duas decisões (metas batendo; pressa) estão todos no playbook. Sem omissão de número, passo ou condição até o módulo 005.

## Perecibilidade

O playbook não cita `alerta-ui` (a aula não tem). Ainda assim a seção Perecível está preenchida e aponta o único caminho de clique do playbook (passo youtube 6), lastreado em 010 com `perecivel: true`. Sem "hoje"/"atualmente". Atende.

## Falhas

(nenhuma)

## Próximo

nada
