"""Revisão v2: rubrica, papéis, fixtures de calibração, laudos e avaliação de uso."""

import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FERRAMENTA = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(FERRAMENTA))

import unidades as lib  # noqa: E402
import validate_visoes as vv  # noqa: E402

BASE = ROOT / "conhecimento"
REV = lib.diretorio_revisao(BASE)
METODO = lib.diretorio_metodo(BASE)
CALIB = FERRAMENTA.parent / "tests" / "calibracao"
OUROS = {"1674fc3d8d94c601", "869445a4c64befbf"}


def _front(path: Path) -> dict:
    front, _ = lib.parse_front_matter(path.read_text(encoding="utf-8"))
    return front


class KitTest(unittest.TestCase):
    def test_rubrica_tem_cinco_vetos_e_sem_nota(self):
        text = (METODO / "RUBRICA.md").read_text(encoding="utf-8")
        for veto in ("Contrato", "Fidelidade", "Cobertura", "Perecibilidade", "Aplicabilidade"):
            self.assertRegex(text, rf"### \d\. {veto}")
        self.assertIn("Sem nota numérica", text)
        self.assertIn("bloqueado", text)

    def test_papeis_v2_com_le_e_nao_le(self):
        for papel in ("extrator", "sintetizador", "inspetor", "juiz", "redator"):
            text = (METODO / "papeis" / f"{papel}.md").read_text(encoding="utf-8")
            self.assertIn("## Lê", text, papel)
            self.assertIn("## Não lê", text, papel)
            self.assertIn("## Escreve", text, papel)
        self.assertIn("memos/", (METODO / "papeis" / "extrator.md").read_text(encoding="utf-8"))
        juiz = (METODO / "papeis" / "juiz.md").read_text(encoding="utf-8")
        self.assertIn("transcricao.md", juiz)

    def test_readme_v2_formato_taxonomia_existem(self):
        for nome in ("README.md", "FORMATO.md", "taxonomia.md"):
            self.assertTrue((BASE / nome).exists(), nome)


class CalibracaoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.esperado = {e["fixture"]: e for e in lib.ler_jsonl(CALIB / "esperado.jsonl")}

    def test_quatro_fixtures_com_veredito_esperado(self):
        self.assertEqual(set(self.esperado), {"f1", "f2", "f3", "f4"})
        vetos = {e["veto_esperado"] for e in self.esperado.values()}
        self.assertEqual(vetos, {"fidelidade", "perecibilidade", "aplicabilidade"})
        for f in self.esperado:
            p = CALIB / f"{f}.md"
            self.assertTrue(p.exists(), f)
            front = _front(p)
            self.assertEqual(front.get("type"), "fixture-calibracao")
            self.assertEqual(front.get("fixture"), f)
            for campo in ("defeito", "veredito_esperado", "veto_esperado"):
                self.assertNotIn(campo, front, f"{f}: {campo} vazaria o defeito ao juiz")

    def test_fixtures_ficam_fora_de_unidades(self):
        for p in (BASE / "unidades").glob("*.md"):
            self.assertNotIn("fixture-calibracao", p.read_text(encoding="utf-8"))

    def test_fixtures_de_unidade_sao_copias_do_ouro_com_diferencas_localizadas(self):
        ouro = lib.parse_arquivo_unidades((BASE / "unidades" / "001-8-3-anuncios-a-alma-do-seu-trafego-pago.md").read_text(encoding="utf-8"))
        hashes = {u.id: lib.hash_unidade(u) for u in ouro.unidades}
        for f in ("f1", "f2", "f3"):
            fx = lib.parse_arquivo_unidades((CALIB / f"{f}.md").read_text(encoding="utf-8"))
            self.assertEqual(len(fx.unidades), len(ouro.unidades), f)
            difs = [u.id for u in fx.unidades if lib.hash_unidade(u) != hashes[u.id]]
            self.assertGreaterEqual(len(difs), 1, f)
            self.assertLessEqual(len(difs), 3, f"{f}: {difs}")

    def test_laudos_das_fixtures_batem_com_o_esperado(self):
        for f, e in self.esperado.items():
            p = CALIB / "laudos" / f"fixture-{f}.md"
            self.assertTrue(p.exists(), f"laudo ausente: {p.name}")
            front = _front(p)
            self.assertEqual(front.get("veredito"), e["veredito_esperado"], f)
            self.assertIn(e["veto_esperado"], front.get("vetos") or [], f"{f}: vetos={front.get('vetos')}")
            self.assertEqual(front.get("gerado_por"), "fable-5.1", f)


class LaudosTest(unittest.TestCase):
    def test_laudos_dos_ouros_e_do_piloto_passam(self):
        for aula in OUROS:
            ev = REV / "laudos" / f"{aula}.evidencia.md"
            self.assertTrue(ev.exists(), ev.name)
            self.assertEqual(_front(ev).get("gerado_por"), "sonnet-5")
            p = REV / "laudos" / f"{aula}.md"
            self.assertTrue(p.exists(), p.name)
            front = _front(p)
            self.assertEqual(front.get("veredito"), "passa", aula)
            self.assertEqual(front.get("vetos"), [], aula)
            self.assertEqual(front.get("gerado_por"), "fable-5.1")
            self.assertEqual(front.get("isolamento"), "ok")
        p = REV / "laudos" / "playbook-diagnosticar-concentracao-de-verba.md"
        self.assertTrue(p.exists())
        self.assertEqual(_front(p).get("veredito"), "passa")

    def test_todo_laudo_tem_veredito_e_secoes(self):
        for p in (REV / "laudos").glob("*.md"):
            if p.name.endswith(".evidencia.md"):
                continue
            text = p.read_text(encoding="utf-8")
            self.assertTrue(re.search(r"^veredito: (passa|falha|bloqueado)$", text, re.M), p.name)
            for sec in ("## Falhas", "## Próximo"):
                self.assertIn(sec, text, p.name)

    def test_laudos_vivos_selados(self):
        """Só laudos vivos: rodadas arquivadas e laudos de fixture são registro histórico (FORMATO §7)."""
        vivos = [p for p in (REV / "laudos").glob("*.md") if not p.name.endswith(".evidencia.md") and not re.search(r"\.rodada-\d+\.md$", p.name) and not p.name.startswith("fixture-")]
        self.assertGreaterEqual(len(vivos), 3)
        for p in vivos:
            front = _front(p)
            self.assertNotEqual(str(front.get("insumos_hash")), "PENDENTE", p.name)
            self.assertEqual(front.get("insumos_hash"), vv.calcular_insumos_hash(BASE, p), p.name)


class AvaliacaoDeUsoTest(unittest.TestCase):
    def test_casos_fechados_antes_da_execucao(self):
        text = (REV / "avaliacao" / "casos.md").read_text(encoding="utf-8")
        casos = re.findall(r"^## Caso (\d+)", text, re.M)
        self.assertGreaterEqual(len(casos), 6)
        for n in casos:
            bloco = text.split(f"## Caso {n}")[1].split("## Caso")[0]
            for campo in ("Entrada", "Esperado", "Não pode aparecer", "Aprovação"):
                self.assertIn(campo, bloco, f"caso {n}: {campo}")

    def test_piloto_registrado_para_v1_e_v2(self):
        for v in ("v1", "v2"):
            p = REV / "avaliacao" / f"resultados-{v}.md"
            self.assertTrue(p.exists(), p.name)
            text = p.read_text(encoding="utf-8")
            self.assertIn("## Caso 3", text)
            self.assertIn("## Caso 7", text)
            self.assertRegex(text, r"(?i)palavras lidas")


if __name__ == "__main__":
    unittest.main()
