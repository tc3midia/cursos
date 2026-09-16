---
type: playbook
status: piloto
title: "Diagnosticar concentração de verba"
tarefa: diagnosticar-concentracao-de-verba
plataformas: [youtube]
parcial_ate: "005"
account_id: account.86ajrj8n9
promoted_by: human.will
gerado_por: fable-5.1
gerado_em: 2026-09-13
rodada: 3
insumos_hash: 2eac1762ec4a8781f383311ed84060233664d9ff07454171cc327e827b8db838
---

# Playbook — diagnosticar concentração de verba

Playbook piloto (CP1). Cobre só a aula 005-4.0 (YouTube). Calendário: as subseções `meta` e
`google-display` da matriz serão preenchidas quando os módulos 002 e 006 forem extraídos (etapa 1).

## Quando usar

- A campanha gasta toda a verba em um único grupo de anúncio ou conjunto e os outros ficam sem gasto `U:869445a4c64befbf:002`.
- Antes de agir, decida se isso é problema: se a campanha entrega a quantidade diária de visualizações ou conversões desejada, a concentração não é o problema `U:869445a4c64befbf:005`.
- O problema real é concentração sem decisão consciente do gestor; com metas batendo, pode ficar como está `U:869445a4c64befbf:014`.

## Pré-condições

- Acesso à campanha com leitura de gasto, custo real e lance por grupo de anúncio `U:869445a4c64befbf:007`.
- Campanha com lance manual por grupo (no caso do curso, CPV máximo no YouTube); a aula não cobre lances automáticos `U:869445a4c64befbf:017`.
- Saber qual ação a estratégia de lance valoriza, porque o Google concentra onde encontra essa ação mais barata `U:869445a4c64befbf:001`.

## Passos por plataforma

### youtube

1. Compare os lances entre os grupos; se um grupo tem lance muito acima dos demais (ex.: R$ 3 contra R$ 0,30), esse é o motivo (diagnóstico 3) `U:869445a4c64befbf:006`.
2. Compare o tamanho das audiências; se o grupo que concentra é muito mais amplo, em geral público frio junto com quente na mesma campanha, é o diagnóstico 1 `U:869445a4c64befbf:002`.
3. Se todos os grupos são quentes e um grupo até menor concentra, o Google está encontrando ali a ação valorizada pelo lance: diagnóstico 2 `U:869445a4c64befbf:003`.
4. Não pause o grupo que concentra e traz o resultado `U:869445a4c64befbf:004`.
5. Solução 1: reduza o lance do grupo que concentra e aumente o dos grupos qualificados que não gastam (mais forte em quem gastou zero, menos em quem gastou pouco); espere alguns dias `U:869445a4c64befbf:007`.
6. Solução 2, se a 1 não resolveu: no grupo que não gasta, abra públicos-alvo, exclusões, e remova a exclusão da hierarquia `U:869445a4c64befbf:010`.
7. Solução 3, se as anteriores não resolveram: isole o grupo que concentra em campanha própria (quente e frio separados), com orçamento por campanha (no exemplo do professor, R$ 10 por dia em cada) e pelo menos dois públicos em cada `U:869445a4c64befbf:012` `U:869445a4c64befbf:013`.

### meta

- Nada nas fontes até o módulo 005: a aula demonstra só em YouTube; Meta Ads não aparece `U:869445a4c64befbf:017`.

### google-display

- Nada nas fontes até o módulo 005: a aula demonstra só em campanha de YouTube com CPV máximo; outras redes do Google não aparecem `U:869445a4c64befbf:017`.

## Réguas e critérios de pronto

- O custo real pode ficar bem abaixo do lance (lance R$ 0,30, custo por visualização R$ 0,05); lance igual ao custo real tende a não gastar `U:869445a4c64befbf:008`.
- Critério de pronto: a campanha entrega a quantidade diária de visualizações ou conversões que você queria, mesmo com gasto desigual `U:869445a4c64befbf:005`.

## Decisões

- Se as metas diárias estão batendo, não mexa `U:869445a4c64befbf:005`.
- Se há pressa, pule direto para a solução 3 (isolar em campanhas quente e fria); sem pressa, escale 1, 2, 3 com espera entre elas `U:869445a4c64befbf:015`.
- Se um grupo tem lance muito acima dos demais (ex.: R$ 3 contra R$ 0,30), esse é o diagnóstico; compare os lances antes de qualquer outra ação `U:869445a4c64befbf:006`.

## Não fazer

- Pausar o grupo que concentra o gasto e traz o resultado `U:869445a4c64befbf:004`.
- Aplicar as três soluções de uma vez, sem esperar entre elas `U:869445a4c64befbf:011`.
- Criar campanha com um único público ao isolar `U:869445a4c64befbf:013`.

## O que o curso não cobre

- Quanto reduzir ou aumentar o lance e quantos dias esperar: o professor fala em "feeling" e "uns dias" `U:869445a4c64befbf:017`; os valores que ele usou ao vivo (R$ 0,30 para R$ 0,05 no frio; R$ 0,45 no grupo zerado; R$ 0,05 a mais nos demais) são exemplo, não régua `U:869445a4c64befbf:009`.
- Lances automáticos e o mesmo problema em Meta Ads `U:869445a4c64befbf:017`.

## Sem resolução no curso

Nada até o módulo 005 (consolidação ainda não rodou).

## Perecível

- O caminho de tela para remover exclusões (grupo de anúncio, públicos-alvo, exclusões, remover) descreve a interface do Google Ads na data da aula `U:869445a4c64befbf:010`.
