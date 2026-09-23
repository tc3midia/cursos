#!/usr/bin/env python3
"""Planta os defeitos da calibração em cópias das duas aulas ouro aprovadas no piloto.

Rodar de ~/cursos/processamento com CURSO=hardcopy-pro. Lê piloto/s5-high/G02_A05.json e piloto/s5-high/ciclo1/G08_A05.json,
grava calibracao/plantado/<AULA>.json e confere o contrato. O gabarito fica em calibracao/gabarito.json e não entra em
nenhum pacote de modelo. As cópias plantadas nunca são publicadas.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path.cwd()))
import base_fcc as base  # noqa: E402

HERE = Path(__file__).resolve().parent
PILOT = HERE.parent / 'piloto' / 's5-high'
OUT = HERE / 'plantado'


def load(path):
    data = json.loads(path.read_text())
    data.pop('correcoes', None)
    return data, {u['numero']: u for u in data['unidades']}


def swap(unit, field, old, new):
    assert unit[field].count(old) == 1, (unit['numero'], field, old)
    unit[field] = unit[field].replace(old, new)


# ------------------------------------------------------------------ G02_A05, aula de texto
data, u = load(PILOT / 'G02_A05.json')

# P1 número adulterado: 60% do protagonista vira 70%, no corpo e na nota; âncora trocada por outra literal da mesma faixa.
swap(u[2], 'corpo', 'O protagonista ocupa 60% do tempo da VSL', 'O protagonista ocupa 70% do tempo da VSL')
swap(u[2], 'nota', 'A fala dá 60% ao protagonista', 'A fala dá 70% ao protagonista')
u[2]['evidencia'] = 'E os NPCs são participações rápidas'

# P2 condição suprimida: o contato direto vale "se você é o expert"; vira lei para qualquer produto.
u[7].update({
    'titulo': 'O bônus incrível: contato direto com quem vende',
    'condicoes': None,
    'corpo': ('O bônus incrível deve ser sempre o contato direto com quem vende: uma live dizendo à pessoa exatamente o que fazer, uma consultoria grátis ou um grupo de WhatsApp. '
              'O professor diz que essa é a parte mais importante da oferta. Qualquer que seja o produto, dê ao lead (o comprador em potencial) a chance de conversar com o vendedor e de apresentar seus projetos, '
              'porque foi nele que o lead depositou a confiança. Num produto de renda extra com Airbnb, por exemplo, ele sugere 15 minutos, 30 minutos ou 1 hora de live para o lead colocar em prática. '
              'Segundo o professor, o efeito é o lead achar que vale a pena e que está barato.'),
    'evidencia': 'Dê a possibilidade dele apresentar os seus projetos para você.',
})

# P5 perecível escondido em unidade `geral`: o preço de 99 reais continua no corpo e a marca sai.
u[6]['perecivel'] = False

# P4 omissão: sai a regra de dispensar garantia, valor e feedbacks quando há o bônus incrível (U009 original).
# P3 número de copy fictícia promovido a régua: entra no lugar, com o mesmo número, uma régua tirada da fala de venda do produto inventado.
data['unidades'] = [x for x in data['unidades'] if x['numero'] != 9]
data['unidades'].insert(8, {
    'numero': 9,
    'titulo': 'Preço de referência da oferta: 12 vezes de R$ 9,90 e garantia de 7 dias',
    'tipo': 'regua', 'tema': 'preco-e-garantia', 'tarefas': ['definir-preco-e-garantia', 'escrever-pitch-e-cta'], 'plataformas': ['geral'],
    'fonte': 'fala', 'inicio': 428, 'fim': 475, 'condicoes': 'Oferta de produto de aulas vendida por VSL.', 'perecivel': True, 'confianca': 'alta',
    'nota': None, 'proposta_tag': None,
    'corpo': ('Na oferta da VSL, apresente o preço parcelado e não o valor cheio: 12 vezes de R$ 9,90 para um produto de 99 reais. A garantia de referência é de 7 dias. '
              'O professor manda esquecer a comparação com valores maiores, como 1.200, 1.000 ou 500, e ir direto ao parcelado.'),
    'evidencia': 'você vai falar com ela que o valor é 12 vezes de R$9,90',
    'versao': 1,
})
OUT.mkdir(parents=True, exist_ok=True)
(OUT / 'G02_A05.json').write_text(base.dump(data))

# ------------------------------------------------------------------ G08_A05, aula de tela
data, u = load(PILOT / 'ciclo1' / 'G08_A05.json')

# P6 estimativa verbal promovida a régua: "um videozinho ali de 2, 3 minutos" vira duração de referência; sai a marca de preferência.
u[3].update({
    'titulo': 'Vídeo de destino do anúncio: de 2 a 3 minutos',
    'tipo': 'regua', 'condicoes': None,
    'corpo': ('O vídeo de destino deve ter de 2 a 3 minutos. O anúncio de produto físico fecha com uma chamada do tipo "saiba mais e veja na prática" e leva a um vídeo '
              'mostrando o produto com essa duração, que é a referência do professor, ou a uma landing page.'),
})

# P8 passo de tela inventado: copiar link, opção sem marca d'água, aba Uploads e zerar volume não estão na fala.
swap(u[6], 'corpo', '3. Baixe em HD com o SnapTik.\n4. Coloque o vídeo no criativo e organize-o.\n5. Tire a voz que vem no vídeo original.',
     '3. No TikTok, toque em Compartilhar e copie o link do vídeo.\n4. Cole o link no SnapTik e escolha o download em HD, na opção sem marca d\'água.\n'
     '5. Envie o arquivo ao Canva pela aba Uploads, arraste para a página do criativo e organize-o.\n6. Tire a voz que vem no vídeo original, zerando o volume do clipe.')

# P9 grafia deformada promovida a outro conceito: "Cetix" e "linha leve em multilingual" viram painel e versão do modelo; sai a marca de incerteza.
swap(u[10], 'corpo', 'Usa o modelo multilingual e regenera a fala até ouvir o resultado que julga bom.',
     'Dentro do ElevenLabs ele abre o Cetix, o painel de ajuste da voz, e escolhe a linha Leve do modelo multilingual, a versão mais rápida do modelo. Depois regenera a fala até ouvir o resultado que julga bom.')
swap(u[10], 'nota', ' A fala sobre o modelo e a idade está degradada e a interpretação é incerta.', '')
u[10]['confianca'] = 'alta'

# P7 unidade sem lastro com âncora literal verdadeira: completa a copy com conhecimento externo sobre temperatura de cor e melatonina.
data['unidades'].append({
    'numero': 12,
    'titulo': 'Luz quente abaixo de 3000 K favorece o sono',
    'tipo': 'conceito', 'tema': 'anuncio-produto-fisico', 'tarefas': [], 'plataformas': ['geral'],
    'fonte': 'fala', 'inicio': 98, 'fim': 116, 'condicoes': None, 'perecivel': False, 'confianca': 'alta', 'nota': None, 'proposta_tag': None,
    'corpo': ('A base do mecanismo único oculto do abajur é a temperatura de cor. Luz quente, abaixo de 3000 K, não inibe a melatonina como a luz branca e azulada, '
              'e por isso ajuda o corpo a entrar no sono. O professor diz que pesquisou o tema antes de escrever a copy e que a alegação se sustenta.'),
    'evidencia': 'ele tem a cor quente ideal para ajudar o seu subconsciente',
    'versao': 1,
})
(OUT / 'G08_A05.json').write_text(base.dump(data))

# ------------------------------------------------------------------ contrato das cópias plantadas
rows = {r[0]['aula']: r for r in base.inventory()}
tax = base.taxonomy()
for lesson in ('G02_A05', 'G08_A05'):
    row, text, segments, material = rows[lesson]
    errors, warnings = base.validate_lesson(row, text, segments, material, json.loads((OUT / f'{lesson}.json').read_text()), tax)
    print(lesson, 'erros:', errors, 'avisos:', warnings)
