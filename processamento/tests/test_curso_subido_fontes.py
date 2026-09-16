"""Integridade das fontes independente do HEAD do repositório."""
import hashlib,json,sys,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import unidades as lib

class FontesTest(unittest.TestCase):
    def test_fontes_incorporadas_intactas(self):
        self.assertEqual(lib.verificar_fontes(), [])

    def test_alteracao_e_ausencia_identificadas_sem_consultar_head(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); (root/'dados').mkdir()
            fonte=root/'transcricao.md'; fonte.write_text('original')
            baseline={'fonte_commit':lib.FONTE_COMMIT,'arquivos':{'transcricao.md':hashlib.sha256(fonte.read_bytes()).hexdigest()}}
            (root/'dados/fontes-originais.json').write_text(json.dumps(baseline))
            with patch.object(lib,'FERRAMENTA',root),patch.object(lib,'clone_commit',side_effect=AssertionError('HEAD não define a integridade das fontes')):
                self.assertEqual(lib.verificar_fontes(root),[])
                fonte.write_text('alterada')
                self.assertEqual(lib.verificar_fontes(root),['fonte alterada: transcricao.md'])
                fonte.unlink()
                self.assertEqual(lib.verificar_fontes(root),['fonte ausente: transcricao.md'])
