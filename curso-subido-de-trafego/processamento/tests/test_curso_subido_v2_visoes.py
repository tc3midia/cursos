"""Visões v2: validador de playbooks, insumos_hash e ciclo de correção com fixtures."""

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FERRAMENTA = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(FERRAMENTA))

import build_indices as bi  # noqa: E402
import unidades as lib  # noqa: E402
import validate_visoes as vv  # noqa: E402

BASE = ROOT / "conhecimento"
PILOTO = BASE / "visoes" / "playbooks" / "diagnosticar-concentracao-de-verba.md"


class PlaybookPilotoTest(unittest.TestCase):
    def test_piloto_existe_e_valida(self):
        self.assertTrue(PILOTO.exists())
        erros = vv.validar_visoes(BASE)
        self.assertEqual(erros, [], erros)

    def test_piloto_tem_secoes_fixas_e_citacoes(self):
        text = PILOTO.read_text(encoding="utf-8")
        for sec in vv.SECOES_PLAYBOOK:
            self.assertIn(f"## {sec}", text)
        self.assertGreaterEqual(len(set(lib.find_citacoes(text))), 5)
        self.assertIn("gerado_por: fable-5.1", text)

    def test_insumos_hash_do_piloto_esta_selado(self):
        front, _ = lib.parse_front_matter(PILOTO.read_text(encoding="utf-8"))
        self.assertEqual(front["insumos_hash"], vv.calcular_insumos_hash(BASE, PILOTO))

    def test_desatualizadas_vazio(self):
        linhas = vv.desatualizadas(BASE, revisao="revisao")
        self.assertEqual(linhas, [], linhas)

    def test_revisao_fora_da_biblioteca_continua_coberta_pelos_selos(self):
        laudos = [p for p in vv._artefatos(BASE, "revisao") if p.parent.name == "laudos"]
        self.assertGreater(len(laudos), 0)
        selos = vv._ler_selos(BASE)
        for p in laudos:
            ref = lib.referencia_artefato(BASE, p)
            self.assertTrue(ref.startswith("revisao/laudos/"))
            self.assertIn(ref, selos)
            self.assertEqual(lib.caminho_artefato(BASE, ref), p)
        self.assertFalse((BASE / "_gerado").exists())
        self.assertFalse((BASE / "revisao").exists())


class CicloDeCorrecaoTest(unittest.TestCase):
    """Fixtures em cópia temporária da base: (a) régua alterada mantendo ID ⇒ playbook desatualizado;
    (b) retirada de unidade citada ⇒ erro no validador de visões."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.base = self.tmp / "base"
        shutil.copytree(BASE, self.base, ignore=shutil.ignore_patterns("historico"))
        shutil.copytree(lib.diretorio_gerado(BASE), self.base / "_gerado")
        shutil.copytree(lib.diretorio_revisao(BASE), self.base / "revisao")
        front, _ = lib.parse_front_matter(PILOTO.read_text(encoding="utf-8"))
        self.citada = sorted(set(lib.find_citacoes(PILOTO.read_text(encoding="utf-8"))))[0]
        self.aula_id = self.citada.split(":")[1]
        self.arquivo = next(p for p in (self.base / "unidades").glob("*.md") if self.aula_id in p.read_text(encoding="utf-8"))

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def _corpo_da_citada(self):
        arq = lib.parse_arquivo_unidades(self.arquivo.read_text(encoding="utf-8"))
        return next(u for u in arq.unidades if u.id == self.citada)

    def test_a_regua_alterada_mantendo_id_desatualiza_o_playbook(self):
        u = self._corpo_da_citada()
        text = self.arquivo.read_text(encoding="utf-8")
        u.corpo = u.corpo[:-1] + [u.corpo[-1] + " Ajuste de teste."]
        u.meta["versao"] += 1
        self.arquivo.write_text(lib.substituir_unidade(text, u), encoding="utf-8")
        bi.escrever(self.base, revisao="revisao")
        linhas = vv.desatualizadas(self.base, revisao="revisao")
        artefatos = {l["artefato"] for l in linhas}
        self.assertTrue(any("diagnosticar-concentracao-de-verba" in a for a in artefatos), linhas)
        self.assertTrue(any(l["insumo"] == self.citada and l["mudanca"] == "corpo" for l in linhas), linhas)

    def test_laudo_migrado_detecta_mudanca_em_insumo_registrado(self):
        laudo = self.base / "revisao" / "laudos" / f"{self.aula_id}.md"
        ids, _ = vv.insumos_de(self.base, laudo)
        self.assertTrue(ids)
        arq = lib.parse_arquivo_unidades(self.arquivo.read_text(encoding="utf-8"))
        u = next(u for u in arq.unidades if u.id == ids[0])
        u.corpo.append("Alteração do insumo para verificar a dependência do laudo.")
        u.meta["versao"] += 1
        self.arquivo.write_text(lib.substituir_unidade(self.arquivo.read_text(encoding="utf-8"), u), encoding="utf-8")
        linhas = vv.desatualizadas(self.base)
        self.assertTrue(any(l["artefato"] == f"revisao/laudos/{self.aula_id}.md" and l["insumo"] == u.id and l["mudanca"] == "corpo" for l in linhas), linhas)

    def test_base_avulsa_nao_escreve_dados_oficiais(self):
        selos = lib.diretorio_gerado(BASE) / "selos.jsonl"
        antes = selos.read_bytes()
        bi.escrever(self.base)
        laudo = self.base / "revisao" / "laudos" / f"{self.aula_id}.md"
        vv.selar(self.base, laudo)
        self.assertEqual(selos.read_bytes(), antes)
        self.assertTrue((self.base / "_gerado/unidades.jsonl").exists())
        self.assertEqual(lib.diretorio_metodo(self.base), self.base / "revisao")

    def test_b_retirada_de_unidade_citada_e_erro(self):
        u = self._corpo_da_citada()
        text = lib.remover_unidade(self.arquivo.read_text(encoding="utf-8"), u.id)
        text = text.replace("retiradas: []", f"retiradas: [{u.id}]", 1)
        self.arquivo.write_text(text, encoding="utf-8")
        bi.escrever(self.base, revisao="revisao")
        erros = vv.validar_visoes(self.base)
        self.assertTrue(any(u.id in e and "retirad" in e for e in erros), erros)
        linhas = vv.desatualizadas(self.base, revisao="revisao")
        self.assertTrue(any(l["insumo"] == u.id and l["mudanca"] == "retirado" for l in linhas), linhas)


if __name__ == "__main__":
    unittest.main()
