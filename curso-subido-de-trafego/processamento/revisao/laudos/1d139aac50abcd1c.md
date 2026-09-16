---
type: laudo
aula_id: 1d139aac50abcd1c
arquivo: unidades/001-8-1-lances.md
rodada: 1
veredito: passa
vetos: []
gerado_por: fable-5.1
isolamento: ok
insumos_hash: 2c73cb5e2d9e9abc0429c679ac942bc2a7eaa304075f47f8248d838394a6b324
---

# Laudo — 1d139aac50abcd1c (rodada 1)

Insumos lidos: o arquivo de unidades, `RUBRICA.md`, `laudos/1d139aac50abcd1c.evidencia.md` (inspetor, sonnet-5) e a saída do validador (`{"arquivos": 1, "unidades": 22, "erros": [], "warnings": []}`). Nenhuma transcrição, PDF, memo, clone, outro laudo ou playbook entrou neste contexto.

## Fidelidade

- 22 de 22 unidades `lastreada` no pacote do inspetor; nenhuma `sem-lastro`, nenhum `desvio`, nenhuma `faixa-errada`.
- U:1d139aac50abcd1c:014 é a única com `confianca: media`; a `nota` explica a confusão de unidades do ROAS na fala (150%/200% vs. R$ 5 por R$ 1 e "ROAS de 500") e o corpo evita fixar número. Conforme a rubrica: passa com registro.
- Registro (sem veto): em U:1d139aac50abcd1c:002 a ordem de "limite de lance" e "outras opções" está invertida em relação à fala; conjunto e sentido idênticos.
- Etiquetas `plataforma` conferem com o que a aula demonstra: `meta` nas unidades do volume mais alto e do objetivo (U:006, U:011, U:013, U:015), `google` nas de CPA desejado, opções de lance e mouse sobre a tela (U:003, U:008, U:009, U:010, U:014, U:016, U:017), `geral` só em analogia e princípio (U:001, U:004, U:005, U:019, U:022). Nenhuma etiqueta ampla sem demonstração.
- Condições que a fonte impõe aparecem nas unidades: exceção de teste para sair do volume mais alto (U:013), CPA desejado preenchido versus em branco (U:010), lance mínimo que não ganha leilão (U:017).
- Nada de "Ads como está em 2026": as três `alerta-ui` descrevem só o que a aula mostra.

## Cobertura

- Inspetor não encontrou omissão; as 22 unidades cobrem 00:00:00–00:13:03 sem lacuna, e o PDF é redundante com a fala em todos os pontos verificados.
- Todos os números da fonte têm unidade: 99,9% (U:006), R$ 100/dia e R$ 700/semana (U:006, U:011), R$ 4 mil e 8/9/10 mil do leilão de boi (U:004), R$ 10 por venda (U:012), CPA 100 vs. 5 (U:016), um centavo e R$ 1 (U:017); ROAS 150%/200% registrado em `nota` de U:014.
- Decisões condicionais cobertas: U:013 (quando sair do volume mais alto) e U:021 (ajustar lance pelo custo por resultado).
- Limites declarados pela aula têm unidade própria: U:007, U:018, U:022.
- Conteúdo conversacional sem orientação não conta como omissão.

## Perecibilidade

- U:002, U:003 e U:008 descrevem tela ou campo e estão com `perecivel: true`; nenhuma descrição de tela, menu ou caminho de clique ficou sem a marca.
- Registro (sem veto): U:009, U:010 e U:014 citam nomes de opção ou campo ("CPA desejado", "valor da conversão", "foco em conversões") dentro de conceito e regra. São o mecanismo e a orientação, não a descrição da tela; se a nomenclatura da plataforma mudar, a página de tema aponta para as `alerta-ui` correspondentes.
- Nenhuma ocorrência de "hoje"/"atualmente" no corpo (validador e inspetor).

## Contrato

- Validador: 1 arquivo, 22 unidades, 0 erros, 0 warnings.
- Inspetor confirma ausência de sequência de 25 palavras idêntica à fonte e que `fontes` (`cst_m01_a8.1_lances.pdf`, `transcricao.md`) bate com o disco da aula, sem PDF/txt fora de uso.
- Regras por tipo conferidas no corpo: `decisao` começa com "Quando " (U:013) e "Se " (U:021); `exemplo` traz as três marcas (U:004); `alerta-ui` com `perecivel: true` (U:002, U:003, U:008); `limite` diz o que a aula não cobre (U:007, U:018, U:022); `conceito` e `limite` são os únicos com `tarefas: []`.
- Identidade: 001..022 presentes, `retiradas`, `divisoes` e `fusoes` vazias, sem furos.

## Falhas

Nenhuma.

## Próximo

nada
