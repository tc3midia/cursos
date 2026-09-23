# Aula 2 — Configurar domínio e campanha no Joinzap

Origem: `ADS PARA METEÓRICOS ALUNOS #ZDMPRIME.COM.pdf`, páginas 4–8  
Curso: Lançamento Meteórico — módulo 8, Tráfego para Meteóricos  
Conversão conferida em: 2026-09-13

O PDF retrata interfaces e infraestrutura disponíveis à época da aula. Confirme a documentação atual do registrador, do Joinzap e da Meta antes de aplicar; não reutilize IPs ou IDs históricos sem validação.

## Subdomínio para rastrear conversões

1. Acessar o serviço em que o domínio está registrado. O exemplo usa o antigo Google Domains.
2. Abrir a área de DNS e localizar os registros personalizados.
3. Criar o host `grupo` e apontá-lo para o destino informado pelo serviço de redirecionamento.
4. O exemplo antigo do curso usa o IPv4 `165.232.131.70`; ele é apenas registro histórico e precisa ser confirmado antes de qualquer uso.
5. O resultado esperado é um endereço como `grupo.seudominio.com.br`.

## Configuração no Joinzap

1. No Joinzap, abrir **Domínios** e escolher **Novo**.
2. Informar apenas o domínio/subdomínio, sem `https://`, por exemplo `grupo.seudominio.com.br`.
3. Aguardar a propagação do DNS. O material menciona poucos minutos, mas o prazo real depende do provedor e do TTL.
4. Com a campanha já criada, abrir **Integrações**, selecionar Facebook Ads e informar o ID do pixel correspondente.
5. Confirmar que pixel, domínio principal e demais ativos pertencem à mesma estrutura de negócios e estão corretamente verificados.
6. Em **Configurações**, substituir o link nativo do Joinzap pelo subdomínio, formando algo como `grupo.seudominio.com.br/grupo-vip`.
7. Avançar até salvar todas as configurações.

O material alerta que a validação de um domínio novo na Meta pode demorar. Faça essa preparação antes da data de captação.

