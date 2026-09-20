# Rubrica — unidades da base Formato Criativo de Conteúdo

Versão 1 · 19/09/2026. Adaptada da rubrica v2 do Curso Subido. Sem nota numérica. Cinco vetos, aplicados com evidência e impacto. Revisão proporcional: corrigir o que está errado, sem reextrair módulo por contagem de reprovações.

## Vereditos

- `passa` — nenhum veto. Pode conter ajustes menores registrados; eles não abrem nova rodada.
- `falha` — ao menos um veto comprovado. Corrigem-se só as unidades e trechos afetados.
- `bloqueado` — referência ouro reprovada, evidência do inspetor insuficiente para decidir, fonte indispensável indisponível, ou falha material que persiste após os dois ciclos e a conferência focal final. O caso vai a Will. O bloqueio pertence ao artefato; não reprova as outras aulas.

## Gravidade

- **Falha material:** afirmação sem fonte; número, condição ou sentido adulterado; etapa ou parte essencial ausente; exemplo de caso apresentado como parâmetro geral; ou outro defeito que muda a decisão de quem consulta, impede executar ou impede verificar. O apontamento identifica o trecho da fonte e a consequência prática. Baixar `confianca` não autoriza manter erro conhecido.
- **Ajuste menor:** redação, repetição, exemplo complementar, detalhe cuja falta não muda a decisão nem impede executar. Registra-se com motivo. Não abre ciclo.
- **Erro mecânico:** campo, formato ou marcação com correção objetiva. Corrige-se localmente e confere-se por script. Zero erros de contrato é obrigatório.

## Vetos

### 1. Contrato — quem mede: script

`base_fcc.py` com zero erros no arquivo. O juiz recebe o resultado do validador e não o refaz.

### 2. Fidelidade — inspetor lastreia, juiz decide

Cada unidade é `lastreada`, `desvio`, `sem-lastro` ou `faixa-errada`.

- Qualquer `sem-lastro` de gravidade material ⇒ falha. Inclui completar com conhecimento externo.
- `desvio` comprovado (número, condição ou sentido diferente de uma fonte clara) ⇒ falha, qualquer que seja a `confianca` ou a `nota`.
- Condição que a fonte impõe e a unidade omite = desvio.
- Número de caso narrado apresentado como `regua` ou como regra geral = desvio.
- Preferência do professor apresentada como lei universal = desvio.
- Fonte ambígua, contraditória ou mal transcrita pode passar quando o inspetor comprova a incerteza e a unidade a preserva com `confianca` adequada e `nota`.
- Divergência entre fala e material resolvida em silêncio para um dos lados = desvio. O esperado é registrar as duas versões.
- `faixa-errada` em mais de 10% das unidades com faixa ⇒ falha.

### 3. Cobertura — inspetor lista, juiz decide

As unidades preservam o que é necessário para decidir e executar: réguas, passos e partes essenciais de procedimentos e estruturas, condições, restrições e alertas que mudam a ação. Omissão só veta quando o inspetor a localiza na fonte e o juiz demonstra o efeito prático de faltar aquilo. Não se exige uma unidade para cada exemplo, repetição ou comentário lateral. Trecho de oferta comercial e trecho degradado de transcrição não contam como omissão. Oferta sem o `limite` correspondente é ajuste menor.

### 4. Perecibilidade — inspetor sinaliza, juiz decide

Tela, menu, configuração, prompt, recurso de plataforma, recurso do curso (link, documento-modelo, quadro, comunidade), equipamento específico, preço, data, oferta ou número de mercado sem `perecivel: true` ⇒ falha. O script já barra plataforma específica sem a marca; o que sobra para inspetor e juiz é o perecível escondido em unidade marcada `geral`. Marcador temporal no corpo é contrato (script).

### 5. Aplicabilidade — quem mede: juiz

O leitor é um agente que consulta a unidade sem a aula ao lado. Pergunta: a unidade se sustenta sozinha?

Falha quando, de forma que muda o uso:

- o corpo depende de referência que ficou na aula ("esse vídeo", "como eu mostrei", jargão do curso sem explicação);
- `tipo`, `tema`, `tarefas` ou `plataformas` levam o agente ao lugar errado (unidade de gravação marcada só como roteiro; plataforma específica quando a orientação é geral, ou o contrário);
- `procedimento` ou `estrutura` sem as partes que a evidência do inspetor mostra existirem na fonte;
- `condicoes` vazio quando o corpo só vale para um perfil ou situação.

Classificação discutível entre dois valores defensáveis é ajuste menor.

## O juiz e a evidência

O juiz não vê transcrição, material nem repositório. Decide com as unidades, a evidência do inspetor, o resultado do validador e esta rubrica. Por isso:

- Apontamento do inspetor sem `trecho_fonte`, ou listado em `citacoes_nao_literais`, vale menos: o juiz pode pedir prova em `proximo` em vez de vetar por ele.
- Inspeção que não cobre todas as unidades, ou que não declara ter buscado omissões, não sustenta `passa`. O veredito é `bloqueado` por evidência insuficiente.
- O juiz não rebaixa gravidade por simpatia com o texto, nem veta por preferência de redação.

## Retrabalho

- Antes de corrigir, consolida-se a lista de falhas: ID, unidades, veto, evidência, impacto, mudança mínima, critério de aceite. A revisão seguinte confere essa lista e os efeitos da alteração; não procura perfeição editorial no resto.
- **Teto: dois ciclos de correção e verificação por artefato na etapa.** Renomear a rodada, mudar a regra ou acrescentar apontamento não reinicia a contagem. Depois do teto, uma intervenção localizada da coordenação sobre a lista residual e uma única conferência focal final, com inspetor e juiz. Persistindo falha material, o item fica pendente e vai a Will, sem novas chamadas automáticas.
- A coordenação não rebaixa sozinha a gravidade de um problema que ela própria corrigiu.
- Reextrair uma aula só com problema amplo comprovado nela, com motivo registrado.
- Mesma causa material confirmada em duas aulas ⇒ uma única ampliação focal para duas aulas adicionais, buscando essa causa, antes de fechar o lote. Erro no pacote compartilhado manda corrigir o pacote e identificar as aulas realmente afetadas.
- Referência ouro que falha vai para decisão humana; não entra na fila do redator.
- Evidência de unidades intactas é preservada quando o hash da unidade, a fonte e a rubrica continuam os mesmos.

## Calibração

`calibracao/` guarda casos com defeito plantado e o veto esperado de cada um. Inspetor e juiz precisam apontar cada defeito pelo veto certo. Se não apontarem, o defeito está no papel ou na rubrica: corrige-se a causa, nunca a régua para baixo.
