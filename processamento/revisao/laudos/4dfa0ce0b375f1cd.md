---
type: laudo
aula_id: 4dfa0ce0b375f1cd
arquivo: unidades/003-5-0-os-10-tipos-de-segmentacoes-do-google-ads.md
rodada: 2
veredito: passa
vetos: []
gerado_por: fable-5.1
isolamento: ok
insumos_hash: 0bb499c96dd6c1911bd524ae338ff6af7ffe94c28edea858a0aca3c5278eefe6
---

# Laudo — 4dfa0ce0b375f1cd (5.0 - Os 10 tipos de segmentações do Google Ads), rodada 2

Insumos: arquivo de unidades (53 unidades), `laudos/4dfa0ce0b375f1cd.evidencia.md` (inspetor, tabela de 51 linhas + Omissões), saída do validador (0 erros, 1 warning). Nenhuma fonte bruta entrou no contexto.

## Fidelidade

- Nenhuma unidade `sem-lastro` na tabela do inspetor.
- U:028 (única `desvio`, confiança alta): a justificativa "alcançam gente que ainda não teve contato com o anunciante", apontada como inferência sem fala, foi retirada. O corpo atual fica no que a evidência sustenta (interesse ou intenção de compra a partir de termos, sites e aplicativos; "públicos mais geniais"). Resolvido.
- `faixa-errada` (rodada 1: U:007, 013, 023, 037, 044 — 5 de 50 com faixa, no limite dos 10%): todas as faixas foram estendidas ou recuadas para os trechos que o inspetor localizou. U:007 → 00:01:29–00:23:31 (cobre [SITE], [APP]/[YT] 00:08:36–00:09:13, [LISTA] 00:11:42, [SP] 00:15:27–00:16:38, [SC] 00:22:49–00:23:31). U:013 → 00:01:29–00:08:36 (passos 1–2). U:023 → 00:11:42–00:22:19 (contraste com o segmento combinado em 00:21:44–00:22:19). U:037 → 00:22:21–00:31:46 (divisões completadas em 00:23:31–00:24:08 e 00:31:19–00:31:46). U:044 → 00:28:16–00:31:46 (mapeamento em 00:31:19–00:31:46). Zero `faixa-errada` restante.
- U:052 e U:053 (novas): lastro na seção Omissões da evidência. U:052 (00:16:01–00:16:38, PDF pág. 13, "[SP] [PESQUISARAM NO GOOGLE]" + termo) e U:053 (00:17:20–00:17:56, PDF pág. 14, "[SP] [VISITAM SITES]" + site/plataforma) reproduzem exatamente a faixa, a página e a nomenclatura que o inspetor apontou; o passo de escolher a opção é o mesmo conteúdo já lastreado em U:030 e U:031. Sem desvio.
- U:016 (`confianca: media`, nota explica a separação das duas ideias da mesma fala) e U:042 (`confianca: baixa`, nota registra a autocorreção do professor; inspetor confirma a leitura) passam com registro.
- Registro R1: U:007 passa a cobrir 22 minutos de fala. Não é veto (a rubrica exige que a faixa contenha o lastro, e contém), mas uma faixa tão larga perde valor de localização; alternativa futura seria listar as faixas dos marcadores na `nota`.

## Cobertura

- As três omissões da evidência foram fechadas: nomenclatura e criação do subtipo "pesquisaram no Google" (U:052) e do subtipo "sites semelhantes" (U:053), ambas do tipo `procedimento`, em paralelo a U:029 (intenção de compra) e U:032 (aplicativos semelhantes). Os quatro subtipos do segmento personalizado agora têm procedimento.
- Números, réguas e decisões condicionais da tabela seguem cobertos (janela 1–540, preenchimento retroativo de 30 dias, escada de 11 janelas, exemplo dos 300 mil/70 mil, 540 dias direto para convertidos, seis interações de YouTube, descontinuação dos semelhantes com prazo maio de 2023 e passagem de dez para nove tipos, ordem de prioridade de testes).
- Registro R2: U:052 e U:053 têm dois passos cada, proporcional à faixa curta (37 s e 36 s) apontada pelo inspetor. Suficiente para o que a fonte demonstra; não há passo omitido a cobrar.

## Perecibilidade

- U:039 e U:040 (apontadas pelo inspetor: correspondência, restrição, exclusão e busca na tela de segmento combinado) agora `perecivel: true`. U:006 (menu do botão de mais) e U:044 (rótulos da tela de segmento combinado) também marcadas. U:052 e U:053 nasceram com `perecivel: true`, correto para escolha de opção e campo de nome.
- Nenhum "hoje"/"atualmente" no corpo (inspetor, seção Contrato; validador sem erro).
- Registro R3: U:004 (três colunas do gerenciador) e U:041 (número exibido ao montar o combinado) continuam `perecivel: false`. Nenhuma das duas foi apontada pelo inspetor nem pelo laudo da rodada 1; o conteúdo principal é conceitual (taxonomia de três tipos, que o PDF também fixa e que a própria unidade diz tender a se manter; significado da estimativa de impressões semanais). Fica registrado como limítrofe, sem veto, para eventual `perecivel: true` numa próxima revisão de conteúdo.

## Contrato

- Validador: 1 arquivo, 53 unidades, 0 erros. Warning único: U:042 `confianca: baixa`, com `nota` que explica (autocorreção do professor). Warning não é erro de contrato.
- Inspetor: nenhuma sequência de 25 palavras idêntica à fonte; nenhum "[[" ou timestamp solto; `fontes` do front matter bate com o pacote em disco.
- Registro R4: a checagem de cópia do inspetor precede U:052 e U:053. Os corpos novos são curtos e reestruturados (pré-condição + dois passos) em torno de duas strings de nomenclatura de poucas palavras; não há como formarem 25 palavras idênticas. Sem risco de contrato.
- Versões e notas das unidades alteradas apontam para os itens da rodada 1 (F1–F8), o que mantém a rastreabilidade da correção.

## Falhas

Nenhuma.

## Próximo

nada
