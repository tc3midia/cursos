# Plano: base de conhecimento do Hardcopy Pro

Registrado em 20/09/2026, antes de qualquer extração. Segundo curso da rota. O método, os papéis e o contrato vêm do Formato Criativo de Conteúdo, fechado na mesma data; este plano registra só o que este curso muda.

Finalidade igual à do primeiro: base consultada por agente, matéria-prima para skills e agentes da TC3. Voz textual, playbooks e checklists ficam fora.

## O que o inventário mostrou

| Medida | Hardcopy Pro | Formato Criativo |
|---|---|---|
| Aulas | 138 gravadas, mais 1 material avulso | 54 |
| Palavras de transcrição | 271.924 | cerca de 172 mil |
| Palavras por aula | 1.970 em média; de 205 a 9.686 | 3.185 em média; até 16 mil |
| Estrutura | 5 trilhas, 18 grupos | 7 módulos |
| Material de apoio | 1 documento, sem aula correspondente | material em 5 dos 7 módulos |
| Gravação | captura em 2× nas 138 aulas, áudio devolvido a 1× antes do Whisper `large-v3-turbo`; sem conferência com o áudio | mesmo processo: 37 aulas em 2× e 17 em 1× |

Trilhas e grupos, na ordem do manifesto:

| Grupo | Trilha e grupo | Aulas | Palavras |
|---|---|---|---|
| G01 | Hard Copy, 1a Temporada: O Início | 9 | 10.858 |
| G02 | Hard Copy, 2a Temporada: Kishotenketsu | 11 + material | 17.343 |
| G03 | Hard Ads, Criatividade | 6 | 6.306 |
| G04 | Hard Ads, Roteirização | 7 | 8.538 |
| G05 | Hard Ads, Edição | 5 | 13.375 |
| G06 | Hard Ads, Produtos com Dores | 12 | 28.918 |
| G07 | Hard Ads, Negócios Locais | 13 | 28.829 |
| G08 | Hard Ads, Produtos Físicos | 10 | 15.429 |
| G09 | Hard Ads, Recapitulando | 7 | 13.300 |
| G10 | Hard Sounds | 7 | 9.671 |
| G11 | Hard IA, Primeira Temporada | 6 | 11.067 |
| G12 | Hard IA, Segunda Temporada | 6 | 14.873 |
| G13 | 0 a 100K, Criação | 6 | 5.537 |
| G14 | 0 a 100K, Copy | 6 | 16.695 |
| G15 | 0 a 100K, Inteligência Artificial | 5 | 8.469 |
| G16 | 0 a 100K, Edição | 9 | 27.715 |
| G17 | 0 a 100K, Estrutura | 5 | 7.519 |
| G18 | 0 a 100K, Escala | 8 | 27.482 |

Fontes no commit `7470ca0`. `base_fcc.py --inventory` com `CURSO=hardcopy-pro`: 139 entradas, zero divergência de hash contra o commit, títulos do manifesto iguais aos cabeçalhos.

## O que este curso tem de diferente, e o que fazer com isso

1. **Vocabulário raro deformado na transcrição.** Não é efeito da captura em 2×: o primeiro curso teve 37 de 54 aulas no mesmo processo (captura em 2×, áudio devolvido a 1× com `atempo` antes do Whisper), e lá as aulas em 2× tiveram menos alucinação de silêncio que as de 1× (1,5 contra 7,4 marcas por 10 mil palavras). O que este curso tem de próprio é o vocabulário: Kishotenketsu aparece em pelo menos sete grafias ("Kinshu", "Kishu", "Kensho", "quinchu", "Kinshutengetsu", "Kim Shu Den Kits", "quinchotem queijo"), e nomes de ferramenta saem irreconhecíveis. O `initial_prompt` do Whisper deste curso não trazia esses termos; o do primeiro trazia o jargão de lá. Há também mais resíduo de silêncio (5,4 marcas por 10 mil palavras contra 3,1): "Legenda Adriana Zanotto", "Copyright Australian Broadcasting Corporation", e laços de repetição em duas aulas de edição do Hard IA. Tratamento: tabela de **grafias da transcrição** no contrato, por termo, com a grafia adotada e a aula de origem. O extrator usa a grafia adotada no corpo, copia a âncora como está na fonte e registra em `nota` quando a identificação do termo for hipótese. Termo não identificável vira `confianca: baixa`, nunca palpite. Resíduo de silêncio conhecido é ignorado por regra do papel e conferido por script.
2. **Muita aula de tela.** Edição no CapCut e no Canva, ElevenLabs, gerenciador de anúncios, Kiwify. A fala diz "clica aqui". Espera-se rendimento baixo nessas aulas e muitas unidades `limite` e `ferramenta`, todas perecíveis. O que ficou só na imagem não entra, e a ausência é registrada.
3. **Cinco assuntos em um curso.** Uma base só, um contrato só, um enum só. A trilha vira campo (`trilha`) em cada aula e em cada linha de `unidades.jsonl`, para o agente filtrar. Cinco bases separadas quebrariam a cobertura por tarefa, que é o que interessa a quem monta skill de copy e anúncio.
4. **Aulas curtas.** Onze têm menos de 500 palavras (abertura, recado, convite). O aviso de "menos de 3 unidades" vai aparecer e é esperado. Aula sem conteúdo rende uma unidade `limite` dizendo isso, como a aula de oferta do primeiro curso.
5. **Material sem aula.** O documento "Surpresa: estruturação de copy" não pertence a nenhuma gravação. Entra como aula só de material (`G02_A12`), com todas as unidades em fonte `material` e sem faixa. É a única fonte escrita do Kishotenketsu e dá a grafia correta do termo. O índice pula o episódio 4 da 2a temporada; não há registro de que o material ocupe esse lugar.
6. **Tempos deslocados.** Os tempos da transcrição seguem a aula original, mas a captura tem margem: a fala começa em até 30 s e o último segmento passa da duração do manifesto em 59 s na mediana. A faixa localiza o trecho na transcrição; no vídeo original pode estar deslocada. Fica registrado como limite.

## Código da aula e identificador

O manifesto não numera aulas. O código `Gxx_Ayy` vem da posição no manifesto (grupo na ordem de aparição, aula na ordem dentro do grupo) e serve para nome de arquivo e ordenação. O `aula_id` vem do nome da pasta da aula, que é estável: `sha256("hardcopy-pro/<pasta>")[:16]`. Se o manifesto ganhar aula no meio, os arquivos mudam de nome e as citações `U:<aula_id>:<nnn>` continuam valendo.

## Scripts

Os cinco scripts do primeiro curso passam a atender os dois, por perfil de curso em `base_fcc.py` (variável de ambiente `CURSO`). O Formato Criativo continua gerando saída idêntica byte a byte (`--reviews --check` sem erro) e os 10 testes passam. Falta para este curso:

- testes próprios do inventário do Hardcopy (grupos, material avulso, `aula_id` pela pasta);
- **retomada automática no limite de sessão da assinatura** (HTTP 429): o executor guarda a tentativa, espera a renovação e continua. No primeiro curso isso foi manual e aconteceu uma vez em 297 chamadas; aqui são esperadas de 700 a 900 chamadas;
- regra de script para a tabela de grafias: grafia deformada conhecida no corpo de unidade vira erro de contrato.

## Piloto

O primeiro curso já decidiu o extrator com evidência (Sonnet 5 `high`; `medium` rodou sem raciocínio e Opus 5 `medium` falhou mais e custou mais), e a rota registra que nível de esforço é mecânica que transfere. O piloto daqui **não repete a comparação de três configurações**. Ele mede o que é novo:

1. Duas aulas ouro, escolhidas depois do levantamento de conteúdo: uma de texto com estrutura de várias partes e régua, uma de tela com transcrição difícil.
2. Casos com erro plantado nas duas, com o gabarito do primeiro curso e mais dois defeitos próprios: grafia deformada promovida a termo e passo de tela inventado onde a fala só diz "clica aqui".
3. Pacote completo na aula mais longa (`hc_100k_t4_a02_audio_pronto`, 9.686 palavras) e em uma aula sem conteúdo.
4. Medida de consumo por aula, para projetar o curso.

Se a extração das ouro reprovar por causa da transcrição e não do extrator, o plano para e volta para Will. Retranscrever com o vocabulário do curso no `initial_prompt` do Whisper é barato e ataca a causa provável; fica como opção, não como passo.

## Lotes

Por grupo, na ordem do curso, um lote por vez com saída temporária e conferência antes de publicar. Grupos pequenos vizinhos da mesma trilha andam juntos. Primeiro lote completo: G01 e G02 (Hard Copy, 21 entradas), que é a trilha de texto e a que mais interessa para skill.

## Revisão

Inspeção com a fonte em todas as aulas, em blocos de até 20 unidades. **Julgamento em todas as aulas desde o começo**: no primeiro curso a amostra mais os gatilhos já levava 41 de 54 aulas ao juiz, e julgar as 13 restantes custou US$ 13 e achou 2 falhas. Teto de dois ciclos de correção por aula, conferência focal depois da correção, aula ouro que reprova vai para decisão de Will.

## Consumo esperado

O primeiro curso custou US$ 148 nominais para 172 mil palavras e 831 unidades. Pela proporção de palavras, este fica entre **US$ 220 e 300 nominais**, mais US$ 15 a 25 de piloto e calibração. É estimativa com erro grande: as aulas de tela rendem menos unidades por palavra, e o vocabulário deformado pode aumentar reprovação na primeira passagem. O piloto corrige o número. O consumo real é cota da assinatura.

## Ponto de parada

Depois do piloto e antes de liberar o primeiro lote completo, a coordenação para e consulta Will com: resultado das ouro, calibração, consumo medido e projeção, taxonomia derivada e a decisão sobre julgar tudo.
