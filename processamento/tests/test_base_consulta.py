import copy
import importlib.util
import unittest
import tempfile
from unittest.mock import patch
from pathlib import Path

SPEC=importlib.util.spec_from_file_location('base_consulta',Path(__file__).resolve().parents[1]/'base_consulta.py')
base=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(base)

class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.row={'aula':'M01_A01','titulo':'Teste','fim_segundos':60}
        self.text='O instrutor usa apenas 5% do patrimônio disponível. A segunda passagem trata da plataforma.'
        self.segments=[(0,30,'O instrutor usa apenas 5% do patrimônio disponível.'),(30,60,'A segunda passagem trata da plataforma.')]
        self.unit={'numero':1,'titulo':'Exposição','tipo':'regua','tema':'gestao-de-risco','tarefas':['gerenciar-risco'],'plataformas':['geral'],'inicio':0,'fim':30,'condicoes':'Patrimônio disponível','perecivel':False,'confianca':'alta','nota':None,'corpo':'O professor limita o valor destinado às operações a 5% do patrimônio que está disponível.','evidencia':'apenas 5% do patrimônio disponível.','versao':1}
        self.data={'curso':'mac-3','aula':'M01_A01','titulo':'Teste','contexto':['Aula de teste.','Critério de risco.','Sem aplicação externa.'],'unidades':[self.unit]}

    def validate(self):
        return base.validate_lesson('mac-3',self.row,self.text,self.segments,self.data)

    def test_valid_unit(self):
        self.assertEqual(self.validate(),[])

    def test_evidence_must_be_literal(self):
        self.unit['evidencia']='usa 50% do patrimônio'
        self.assertTrue(any('não literal' in e for e in self.validate()))

    def test_literal_outside_range_is_rejected(self):
        self.unit['inicio'],self.unit['fim']=30,60
        self.assertTrue(any('fora da faixa' in e for e in self.validate()))

    def test_out_of_bounds_range(self):
        self.unit['fim']=100
        self.assertTrue(any('faixa inválida' in e for e in self.validate()))

    def test_low_confidence_requires_note(self):
        self.unit['confianca']='baixa'
        self.assertTrue(any('sem nota' in e for e in self.validate()))

    def test_screen_must_be_perishable(self):
        self.unit['tipo']='alerta-ui'
        self.assertTrue(any('tela não perecível' in e for e in self.validate()))

    def test_duplicate_number(self):
        self.data['unidades'].append(copy.deepcopy(self.unit))
        self.assertTrue(any('sequência' in e for e in self.validate()))

    def test_course_isolation(self):
        self.data['curso']='analises-extraordinarias'
        self.assertTrue(any('curso diferente' in e for e in self.validate()))

    def test_typo_in_task_rejected(self):
        self.unit['tarefas']=['gerir-risco-inventado']
        self.assertTrue(any('tarefas inválidas' in e for e in self.validate()))

    def test_future_type_rejected(self):
        self.unit['tipo']='recomendacao-garantida'
        self.assertTrue(any('tipo inválido' in e for e in self.validate()))

    def test_review_hash_invalidates_after_edit(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(base,'ROOT',Path(folder)):
            data=Path(folder)/'mac-3/conhecimento/dados/M01_A01.json'
            data.parent.mkdir(parents=True)
            data.write_text(base.dump(self.data))
            review=Path(folder)/'mac-3/processamento/revisao/inspecao/M01_A01.json'
            review.parent.mkdir(parents=True)
            review.write_text(base.dump({'arquivo_sha256':base.sha(data.read_bytes()),'veredito':'passa','unidades_verificadas':[1]}))
            self.assertEqual(base.review_errors('mac-3',self.row,data),[])
            self.unit['corpo']+=' Frase alterada.'
            data.write_text(base.dump(self.data))
            self.assertTrue(any('desatualizada' in e for e in base.review_errors('mac-3',self.row,data)))

    def test_sample_requires_judgment_bound_to_review(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(base,'ROOT',Path(folder)):
            row={**self.row,'aula':'M01_A07'}
            data=Path(folder)/'mac-3/conhecimento/dados/M01_A07.json'
            data.parent.mkdir(parents=True)
            data.write_text(base.dump(self.data))
            review=Path(folder)/'mac-3/processamento/revisao/inspecao/M01_A07.json'
            review.parent.mkdir(parents=True)
            review.write_text(base.dump({'arquivo_sha256':base.sha(data.read_bytes()),'veredito':'passa','unidades_verificadas':[1]}))
            self.assertTrue(any('julgamento da amostra ausente' in e for e in base.review_errors('mac-3',row,data)))
            judgment=Path(folder)/'mac-3/processamento/revisao/julgamento/M01_A07.json'
            judgment.parent.mkdir(parents=True)
            judgment.write_text(base.dump({'arquivo_sha256':base.sha(data.read_bytes()),'inspecao_sha256':base.sha(review.read_bytes()),'veredito':'passa'}))
            self.assertEqual(base.review_errors('mac-3',row,data),[])
            review.write_text(review.read_text()+'\n')
            self.assertTrue(any('julgamento desatualizado' in e for e in base.review_errors('mac-3',row,data)))

if __name__=='__main__':
    unittest.main()
