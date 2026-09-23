# Exemplos de granularidade

Os exemplos abaixo vêm de uma aula fictícia sobre pão de fermentação natural, de propósito fora do assunto do curso. Servem para mostrar tamanho, tom e uso dos campos. Nada deles é conteúdo da aula que você vai receber. Os valores de `tema`, `tarefas` e `plataformas` aparecem como `<…>` porque a taxonomia deles não é a deste curso.

```json
{"titulo": "Autólise: descansar farinha e água antes do fermento",
 "tipo": "procedimento", "tema": "<tema>", "tarefas": ["<tarefa>"], "plataformas": ["geral"],
 "fonte": "fala", "inicio": 312, "fim": 401,
 "condicoes": "Farinha branca ou mistura com até metade de integral; com 100% integral o professor pula esta etapa.",
 "perecivel": false, "confianca": "alta", "nota": null, "proposta_tag": null,
 "corpo": "Pré-condição: farinha e água pesadas, fermento ainda fora da mistura.\n1. Misture só farinha e água até não sobrar farinha seca.\n2. Cubra e deixe descansar de 30 a 60 minutos.\n3. Só então acrescente o fermento e, por último, o sal.\nO descanso adianta a formação do glúten e encurta a sova, porque a farinha hidrata sem competir com o sal.",
 "evidencia": "deixa ali de meia hora a uma hora, só farinha e água, sem mexer em mais nada"}
```

```json
{"titulo": "Hidratação de partida para quem está começando",
 "tipo": "regua", "tema": "<tema>", "tarefas": ["<tarefa>"], "plataformas": ["geral"],
 "fonte": "fala+material", "inicio": 125, "fim": 170,
 "condicoes": "Primeiros pães; o professor sobe a hidratação depois que a modelagem estiver dominada.",
 "perecivel": false, "confianca": "media",
 "nota": "A fala diz 65% a 70% de água sobre a farinha; o material de apoio traz 68% fixo. As duas versões ficam registradas.",
 "proposta_tag": null,
 "corpo": "Comece com 65% a 70% de água em relação ao peso da farinha. Massa mais molhada que isso dá miolo mais aberto, mas o professor desaconselha no início porque a modelagem fica difícil e o erro desanima.",
 "evidencia": "começa com sessenta e cinco, setenta por cento, não inventa de ir pra oitenta agora"}
```

```json
{"titulo": "Aluna que vendia 40 pães por semana não vira meta",
 "tipo": "exemplo", "tema": "<tema>", "tarefas": ["<tarefa>"], "plataformas": ["geral"],
 "fonte": "fala", "inicio": 905, "fim": 968,
 "condicoes": null, "perecivel": true, "confianca": "alta", "nota": null, "proposta_tag": null,
 "corpo": "Situação: uma aluna começou a vender para vizinhos três meses depois do curso.\nO que aconteceu: segundo o professor, chegou a 40 pães por semana a R$ 25 cada, assando em forno doméstico.\nLógica: ele conta o caso para mostrar que fornada pequena e constante fideliza. Não apresenta 40 pães nem R$ 25 como meta ou preço recomendado.",
 "evidencia": "quarenta pães por semana, no forninho de casa, vinte e cinco reais cada um"}
```

```json
{"titulo": "A aula não cobre fermento biológico seco",
 "tipo": "limite", "tema": "<tema>", "tarefas": [], "plataformas": ["geral"],
 "fonte": "fala", "inicio": 40, "fim": 66,
 "condicoes": null, "perecivel": false, "confianca": "alta", "nota": null, "proposta_tag": null,
 "corpo": "O professor declara que tudo na aula vale para fermento natural e que pão com fermento biológico seco fica para outro módulo. Tempos e proporções daqui não devem ser transpostos para fermento seco.",
 "evidencia": "fermento de pacotinho é outra conversa, a gente vê lá na frente"}
```

Repare: o procedimento guarda a exceção em `condicoes`; a régua registra a divergência entre fala e material sem escolher lado; o número do caso ficou em `exemplo`, perecível, com a ressalva de que não é meta; o limite diz o que não transpor.
