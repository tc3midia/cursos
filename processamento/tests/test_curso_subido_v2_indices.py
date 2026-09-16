"""Índices gerados v2: JSONL, cobertura, páginas de tema, índice, --check."""

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FERRAMENTA = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(FERRAMENTA))

import build_indices as bi  # noqa: E402
import unidades as lib  # noqa: E402

BASE = ROOT / "conhecimento"
GERADO = lib.diretorio_gerado(BASE)


class IndicesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.saidas = bi.gerar(BASE, revisao="revisao")  # dict caminho -> conteúdo (não grava)

    def test_check_bate_com_disco(self):
        proc = subprocess.run(
            [sys.executable, str(FERRAMENTA / "build_indices.py"), "--root", str(BASE), "--revisao", "revisao", "--check"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)

    def test_jsonl_uma_linha_por_bloco_vivo(self):
        linhas = [json.loads(l) for l in (GERADO / "unidades.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
        vivos = sum(len(arq.unidades) for _, arq in lib.iter_unidades(BASE))
        self.assertEqual(len(linhas), vivos)
        ids = [l["id"] for l in linhas]
        self.assertEqual(len(ids), len(set(ids)))
        for l in linhas:
            for campo in ("id", "aula_id", "slug", "modulo", "ordem", "titulo", "tipo", "plataforma", "tema", "tarefas", "fonte", "faixa", "perecivel", "confianca", "versao", "hash", "grupo"):
                self.assertIn(campo, l)
            self.assertRegex(l["hash"], r"^[0-9a-f]{64}$")

    def test_hash_no_jsonl_bate_com_o_disco(self):
        por_id = {json.loads(l)["id"]: json.loads(l) for l in (GERADO / "unidades.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()}
        for _, arq in lib.iter_unidades(BASE):
            for u in arq.unidades:
                self.assertEqual(por_id[u.id]["hash"], lib.hash_unidade(u), u.id)
                self.assertEqual(por_id[u.id]["versao"], u.meta["versao"], u.id)

    def test_cobertura_tem_toda_a_matriz(self):
        tax = lib.load_taxonomia(BASE / "taxonomia.md")
        linhas = [json.loads(l) for l in (GERADO / "cobertura.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
        pares = {(l["tarefa"], l["plataforma"]) for l in linhas}
        for tarefa, info in tax.tarefas.items():
            for p in info["plataformas"]:
                self.assertIn((tarefa, p), pares)

    def test_paginas_de_tema_so_para_temas_com_unidade_e_sem_prosa_nova(self):
        temas_com_unidade = {u.meta["tema"] for _, arq in lib.iter_unidades(BASE) for u in arq.unidades}
        gerados = {p.stem for p in (BASE / "visoes" / "temas").glob("*.md")}
        self.assertEqual(gerados, temas_com_unidade)
        for p in (BASE / "visoes" / "temas").glob("*.md"):
            text = p.read_text(encoding="utf-8")
            self.assertIn("type: pagina-tema", text)
            self.assertIn("gerado_por: build_indices", text)

    def test_indice_sem_link_para_historico_nem_memos(self):
        text = (BASE / "indice.md").read_text(encoding="utf-8")
        self.assertNotIn("historico/", text)
        self.assertNotIn("memos/", text)
        self.assertIn("unidades/", text)

    def test_determinismo(self):
        outra = bi.gerar(BASE, revisao="revisao")
        self.assertEqual(self.saidas, outra)

    def test_indice_grade_completa_em_ordem_sem_links_para_aulas_pendentes(self):
        text = self.saidas["indice.md"].split("## Unidades por aula", 1)[1]
        entradas = [linha for linha in text.splitlines() if linha.startswith("- ")]
        manifest = lib.load_manifest()
        aulas = sorted(manifest.values(), key=lambda row: (row["modulo3"], int(row["ordem"])))
        processadas = {str(arq.front["aula_id"]): path for path, arq in lib.iter_unidades(BASE)}
        self.assertEqual(len(entradas), len(aulas))
        for entrada, row in zip(entradas, aulas):
            if row["id"] in processadas:
                self.assertTrue(entrada.startswith(f"- [{row['aula']}](unidades/{processadas[row['id']].name})"), entrada)
            else:
                self.assertEqual(entrada, f"- {row['aula']} — a processar; unidades ainda não disponíveis")
        for modulo in {row["modulo"] for row in aulas}:
            self.assertIn(f"### {modulo}\n", text)

    def test_desatualizadas_vazio(self):
        text = (GERADO / "desatualizadas.md").read_text(encoding="utf-8")
        self.assertTrue(bi.desatualizadas_vazio(text), text)


class PaginasTemaTest(unittest.TestCase):
    def test_tema_so_com_unidades_sem_tarefa_nao_quebra_a_geracao(self):
        """Regressão: tema em que nenhuma unidade tem tarefa (só conceitos) derrubava _paginas_tema."""
        tax = lib.load_taxonomia(BASE / "taxonomia.md")
        ids = sorted(lib.todas_unidades(BASE))[:2]
        temas = tax.temas[:2]
        tarefa = next(iter(tax.tarefas))
        base = {"tipo": "conceito", "titulo": "t", "plataforma": ["geral"], "slug": "x", "condicoes": "", "perecivel": False}
        linhas = [
            dict(base, id=ids[0], tema=temas[0], tarefas=[]),
            dict(base, id=ids[1], tema=temas[1], tarefas=[tarefa]),
        ]
        paginas = bi._paginas_tema(BASE, linhas, tax)
        self.assertEqual(set(paginas), set(temas))
        self.assertIn("- nenhum", paginas[temas[0]])


if __name__ == "__main__":
    unittest.main()
