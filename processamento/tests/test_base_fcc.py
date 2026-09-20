import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import base_fcc as base


class ValidacaoFCC(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tax = base.taxonomy()
        cls.rows = {r[0]['aula']: r for r in base.inventory()}

    def lesson(self, code='M02_A09'):
        row, text, segments, material = self.rows[code]
        start, end, body = segments[3]
        evidence = ' '.join(body.split()[:8])
        unit = {'numero': 1, 'titulo': 'Experimento Social: roteiro nasce na rua', 'tipo': 'regra', 'tema': 'formato-experimento-social',
                'tarefas': ['escrever-roteiro'], 'plataformas': ['geral'], 'fonte': 'fala', 'inicio': start, 'fim': end + 5, 'condicoes': None,
                'perecivel': False, 'confianca': 'alta', 'nota': None, 'proposta_tag': None,
                'corpo': 'Planeje só a pergunta e o quadro; a fala do vídeo acontece na interação com as pessoas.', 'evidencia': evidence, 'versao': 1}
        data = {'curso': base.COURSE, 'aula': code, 'titulo': row['titulo'], 'retiradas': [], 'contexto': ['Frase um.', 'Frase dois.', 'Frase três.'],
                'unidades': [unit, {**copy.deepcopy(unit), 'numero': 2}, {**copy.deepcopy(unit), 'numero': 3}]}
        return row, text, segments, material, data

    def errors(self, mutate, code='M02_A09'):
        row, text, segments, material, data = self.lesson(code)
        mutate(data)
        return base.validate_lesson(row, text, segments, material, data, self.tax)[0]

    def test_inventario(self):
        self.assertEqual(len(self.rows), 54)
        self.assertEqual(base.inventory_errors(list(self.rows.values())), [])
        self.assertIsNone(self.rows['M02_A09'][3], 'material divergente não entra no pacote')
        self.assertIsNotNone(self.rows['M03_A03'][3])
        self.assertIsNone(self.rows['M06_A01'][3])

    def test_aula_valida(self):
        self.assertEqual(self.errors(lambda d: None), [])

    def test_evidencia_fora_da_faixa(self):
        def mutate(d):
            d['unidades'][0].update(inicio=300, fim=320)
        self.assertTrue(any('evidência fora da faixa' in e for e in self.errors(mutate)))

    def test_evidencia_inventada(self):
        self.assertTrue(any('não literal' in e for e in self.errors(lambda d: d['unidades'][0].update(evidencia='frase que ninguém disse na aula'))))

    def test_enum_fora_da_taxonomia(self):
        self.assertTrue(any('tema inválido' in e for e in self.errors(lambda d: d['unidades'][0].update(tema='gestao-de-risco'))))
        self.assertTrue(any('tarefas inválidas' in e for e in self.errors(lambda d: d['unidades'][0].update(tarefas=['subir-campanha']))))

    def test_regras_por_tipo(self):
        self.assertTrue(any('régua sem número' in e for e in self.errors(lambda d: d['unidades'][0].update(tipo='regua'))))
        self.assertTrue(any('Pré-condição' in e for e in self.errors(lambda d: d['unidades'][0].update(tipo='procedimento'))))
        self.assertTrue(any('estrutura exige' in e for e in self.errors(lambda d: d['unidades'][0].update(tipo='estrutura'))))
        self.assertTrue(any('decisão começa' in e for e in self.errors(lambda d: d['unidades'][0].update(tipo='decisao'))))
        self.assertTrue(any('ferramenta exige' in e for e in self.errors(lambda d: d['unidades'][0].update(tipo='ferramenta'))))
        self.assertTrue(any('tarefas vazias' in e for e in self.errors(lambda d: d['unidades'][0].update(tarefas=[]))))

    def test_material_em_aula_sem_material(self):
        def mutate(d):
            d['unidades'][0].update(fonte='material', inicio=None, fim=None)
        self.assertTrue(any('não tem material utilizável' in e for e in self.errors(mutate)))

    def test_copia_bruta_e_marcador_temporal(self):
        row, text, *_ = self.rows['M02_A09']
        words = base.norm(text.split(']', 1)[1]).split()[:30]
        self.assertTrue(any('cópia de 25 palavras' in e for e in self.errors(lambda d: d['unidades'][0].update(corpo=' '.join(words)))))
        self.assertTrue(any('marcador temporal' in e for e in self.errors(lambda d: d['unidades'][0].update(corpo='Atualmente o roteiro nasce na rua, na interação.'))))

    def test_numeracao_sem_furo(self):
        self.assertTrue(any('furo' in e for e in self.errors(lambda d: d['unidades'].pop(1))))
        self.assertEqual(self.errors(lambda d: (d['unidades'].pop(1), d['retiradas'].append(2))), [])

    def test_hash_ignora_nota_e_muda_com_corpo(self):
        row, *_, data = self.lesson()
        unit = data['unidades'][0]
        before = base.unit_hash(row, unit)
        self.assertEqual(before, base.unit_hash(row, {**unit, 'nota': 'x', 'versao': 9}))
        self.assertNotEqual(before, base.unit_hash(row, {**unit, 'corpo': unit['corpo'] + ' Mais.'}))


if __name__ == '__main__':
    unittest.main()
