"""Perfil do Hardcopy Pro: inventário sem número de aula no manifesto, material avulso e espera por limite de sessão."""
import datetime
import importlib
import os
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


def load(course):
    os.environ['CURSO'] = course
    import base_fcc
    return importlib.reload(base_fcc)


class Inventario(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = load('hardcopy-pro')
        cls.rows = cls.base.inventory()

    @classmethod
    def tearDownClass(cls):
        load('formato-criativo-de-conteudo')

    def test_contagem_e_grupos(self):
        self.assertEqual(len(self.rows), 139)
        self.assertEqual(self.base.inventory_errors(self.rows), [])
        self.assertEqual(len({r[0]['modulo'] for r in self.rows}), 18)
        self.assertEqual(len({r[0]['trilha'] for r in self.rows}), 5)

    def test_paginas_espelham_as_pastas_do_curso(self):
        """Decisão de Will: a biblioteca repete pastas, nomes e ordem do curso; o material avulso mora onde o curso o guarda."""
        paths = {r[0]['aula']: self.base.page_path(r[0]) for r in self.rows}
        self.assertEqual(len(set(paths.values())), 139)
        self.assertEqual(paths['G02_A05'], '01 Hard Copy/2a Temporada - Kishotenketsu/hc_t2_e02_parte_04_o_que_nao_pode_faltar.md')
        self.assertEqual(paths['G10_A03'], '03 Hard Sounds/hc_sounds_e03_o_que_queremos_ouvir.md')
        self.assertEqual(paths['G02_A12'], 'Materiais/01 Hard Copy/Surpresa.md')
        for row, _, _, _ in self.rows:
            page = self.base.SRC / self.base.page_path(row)
            self.assertTrue(page.is_file() or page.with_name(page.stem).is_dir(), page)

    def test_aula_id_vem_da_pasta(self):
        row = next(r[0] for r in self.rows if r[0]['pasta'] == 'hc_t1_e01_piloto')
        self.assertEqual(row['aula'], 'G01_A01')
        self.assertEqual(row['aula_id'], self.base.sha(b'hardcopy-pro/hc_t1_e01_piloto')[:16])

    def test_material_avulso_vira_aula_sem_transcricao(self):
        row, text, segments, material = next(r for r in self.rows if r[0]['aula'] == 'G02_A12')
        self.assertEqual((text, segments, list(row['fontes'])), ('', [], ['material']))
        self.assertIn('Kishotenketsu', material)


class LimiteDeSessao(unittest.TestCase):
    def test_espera_ate_a_renovacao(self):
        import fcc_executar as ex
        now = datetime.datetime(2026, 9, 20, 5, 0)
        raw = {'is_error': True, 'api_error_status': 429, 'result': "You've hit your session limit · resets 6:30am"}
        self.assertEqual(ex.limit_wait(raw, now), 90 * 60 + 120)
        self.assertEqual(ex.limit_wait({**raw, 'result': 'session limit · resets 1am'}, now), 20 * 3600 + 120)
        self.assertEqual(ex.limit_wait({**raw, 'result': 'rate limit'}, now), 1800)
        self.assertIsNone(ex.limit_wait({'is_error': True, 'result': 'timeout de 2400s'}, now))
        self.assertIsNone(ex.limit_wait({'is_error': False, 'result': 'session limit'}, now))


class CopiaBruta(unittest.TestCase):
    """A cópia de 25 palavras é comparada por sequência de palavras: marcação de tempo e Markdown da fonte não a escondem."""

    def test_copia_atravessa_marcacoes_e_markdown(self):
        base = load('hardcopy-pro')
        try:
            words = [f'palavra{i}' for i in range(30)]
            text = '# Aula\n\n' + '\n\n'.join(f'[00:00:{i:02}.000–00:00:{i + 1:02}.000] {w}' for i, w in enumerate(words))
            material = '- *' + '* '.join(words[:15]) + '\n- ' + ', '.join(words[15:])
            body = ' '.join(words[:26])
            self.assertIn(' ' + ' '.join(base.word_seq(body).split()[:25]) + ' ', base.word_seq(text))
            self.assertIn(' ' + ' '.join(base.word_seq(body).split()[:25]) + ' ', base.word_seq(material))
        finally:
            load('formato-criativo-de-conteudo')

    def test_prova_pedida_pelo_juiz_no_piloto(self):
        """A primeira extração de G02_A12 copiava o material em U006 e U009 e o validador antigo não via."""
        import json
        base = load('hardcopy-pro')
        try:
            pilot = base.PROC / 'piloto' / 's5-high'
            rows = {r[0]['aula']: r for r in base.inventory()}
            tax = base.taxonomy()
            before, _ = base.validate_lesson(*rows['G02_A12'], json.loads((pilot / 'G02_A12.json').read_text()), tax)
            after, _ = base.validate_lesson(*rows['G02_A12'], json.loads((pilot / 'ciclo1' / 'G02_A12.json').read_text()), tax)
            self.assertEqual(before, ['G02_A12: U006: cópia de 25 palavras no corpo', 'G02_A12: U009: cópia de 25 palavras no corpo'])
            self.assertEqual(after, [])
        finally:
            load('formato-criativo-de-conteudo')


class ContextoNoLote(unittest.TestCase):
    """Regras de script do fcc_lote.py para o contexto da aula: parêntese com grafia deformada e falha só de contexto."""

    def test_retira_parentese_com_grafia_deformada(self):
        import json
        import tempfile
        base = load('hardcopy-pro')
        try:
            import fcc_lote
            with tempfile.TemporaryDirectory() as tmp:
                folder = Path(tmp)
                data = {'contexto': ['O professor apresenta o CapCut (transcrito ora como "TapCut", ora como "cap cut") como a ferramenta.',
                                     'Usa o TapCut para editar.', 'Frase sem nada (com parêntese comum).'], 'unidades': []}
                (folder / 'G10_A04.json').write_text(json.dumps(data, ensure_ascii=False))
                changed = fcc_lote.strip_context_spellings(folder, 'G10_A04')
                after = json.loads((folder / 'G10_A04.json').read_text())
                self.assertEqual(len(changed), 1)
                self.assertEqual(after['contexto'][0], 'O professor apresenta o CapCut como a ferramenta.')
                self.assertEqual(after['contexto'][1], 'Usa o TapCut para editar.')
                self.assertEqual(after['contexto'][2], 'Frase sem nada (com parêntese comum).')
                self.assertEqual(after['correcoes'][0]['por'], 'script')
                self.assertEqual(after['correcoes'][0]['unidades'], [])
                self.assertTrue(base.DEFORMED.search(after['contexto'][1]))
        finally:
            load('formato-criativo-de-conteudo')

    def test_falha_so_de_contexto_nao_aplicada(self):
        import fcc_lote
        only_context = {'veredito': 'falha', 'falhas': [{'unidades': [], 'veto': 'fidelidade'}]}
        self.assertTrue(fcc_lote.context_only_failure(only_context, ['a', 'b'], ['a', 'b']))
        self.assertFalse(fcc_lote.context_only_failure(only_context, ['a', 'b'], ['a', 'c']))
        self.assertFalse(fcc_lote.context_only_failure({'veredito': 'falha', 'falhas': [{'unidades': [3], 'veto': 'fidelidade'}]}, ['a'], ['a']))
        self.assertFalse(fcc_lote.context_only_failure({'veredito': 'falha', 'falhas': [{'unidades': [], 'veto': 'cobertura'}]}, ['a'], ['a']))
        self.assertFalse(fcc_lote.context_only_failure({'veredito': 'passa', 'falhas': []}, ['a'], ['a']))


class RedatorContexto(unittest.TestCase):
    """O redator devolve o contexto reescrito quando uma falha o pede; o executor aplica e registra."""

    def test_aplica_contexto_e_unidades(self):
        import fcc_executar as ex
        data = {'contexto': ['a', 'b', 'c'], 'retiradas': [], 'unidades': [{'numero': 1, 'versao': 1, 'nota': 'x', 'corpo': 'v'}, {'numero': 2, 'versao': 1, 'nota': None, 'corpo': 'w'}]}
        output = {'unidades_corrigidas': [{'numero': 1, 'nota': '', 'corpo': 'v2'}], 'unidades_novas': [], 'retiradas': [], 'contexto': ['a', 'b2', 'c'], 'observacoes': 'ok'}
        new, changed = ex.apply_fix(data, output, [1], 2, 'opus-5')
        self.assertEqual(changed, [1])
        self.assertEqual(new['contexto'], ['a', 'b2', 'c'])
        self.assertEqual(data['contexto'], ['a', 'b', 'c'])
        self.assertEqual(new['unidades'][0], {'numero': 1, 'versao': 2, 'nota': None, 'corpo': 'v2'})
        self.assertEqual(new['correcoes'][-1]['contexto'], True)
        self.assertEqual(new['correcoes'][-1]['ciclo'], 2)
        again, changed = ex.apply_fix(new, {**output, 'unidades_corrigidas': [], 'contexto': []}, [], 3, 'opus-5')
        self.assertEqual(changed, [])
        self.assertEqual(again['contexto'], ['a', 'b2', 'c'])
        self.assertEqual(again['correcoes'][-1]['contexto'], False)

    def test_esquema_do_redator_pede_contexto(self):
        import fcc_executar as ex
        schema = ex.schema_for('redator', {'tipos': [], 'temas': [], 'tarefas': [], 'plataformas': []})
        self.assertIn('contexto', schema['properties'])
        self.assertEqual(schema['properties']['contexto']['type'], 'array')


if __name__ == '__main__':
    unittest.main()
