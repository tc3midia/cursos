"""Taxonomia v2 do Curso Subido: enums fechados que o validador lê."""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FERRAMENTA = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(FERRAMENTA))

import unidades as lib  # noqa: E402

BASE = ROOT / "conhecimento"


class TaxonomiaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tax = lib.load_taxonomia(BASE / "taxonomia.md")

    def test_headings_e_ordem(self):
        text = (BASE / "taxonomia.md").read_text(encoding="utf-8")
        pos = [text.index(h) for h in ("## Plataformas", "## Temas", "## Tarefas", "## Tipos")]
        self.assertEqual(pos, sorted(pos))

    def test_plataformas(self):
        self.assertEqual(len(self.tax.plataformas), 8)
        self.assertIn("geral", self.tax.plataformas)
        self.assertIn("ads-editor", self.tax.plataformas)

    def test_temas(self):
        self.assertGreaterEqual(len(self.tax.temas), 15)
        self.assertLessEqual(len(self.tax.temas), 25)

    def test_tarefas_entre_25_e_45_e_matriz_valida(self):
        self.assertGreaterEqual(len(self.tax.tarefas), 25)
        self.assertLessEqual(len(self.tax.tarefas), 45)
        self.assertNotIn("auditar-conta", self.tax.tarefas)
        for slug, info in self.tax.tarefas.items():
            self.assertTrue(info["plataformas"], slug)
            for p in info["plataformas"]:
                self.assertIn(p, self.tax.plataformas, f"{slug}: {p}")
            self.assertIn(info["grupo"], {"fundacao", "planejamento", "segmentacao", "criativo", "execucao", "diagnostico"})

    def test_tipos(self):
        self.assertEqual(
            set(self.tax.tipos),
            {"regra", "regua", "procedimento", "decisao", "conceito", "exemplo", "alerta-ui", "fato-material", "limite"},
        )

    def test_slugs_sao_kebab(self):
        for enum in (self.tax.plataformas, self.tax.temas, list(self.tax.tarefas), self.tax.tipos):
            for s in enum:
                self.assertRegex(s, r"^[a-z0-9]+(-[a-z0-9]+)*$")

    def test_sem_duplicatas(self):
        for enum in (self.tax.plataformas, self.tax.temas, self.tax.tipos):
            self.assertEqual(len(enum), len(set(enum)))


if __name__ == "__main__":
    unittest.main()
