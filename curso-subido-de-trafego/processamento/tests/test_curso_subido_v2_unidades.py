"""Unidades v2 do Curso Subido: parser, validador, hash/versão, arquivos reais."""

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FERRAMENTA = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(FERRAMENTA))

import unidades as lib  # noqa: E402
import validate_unidades as val  # noqa: E402

BASE = ROOT / "conhecimento"
AULA = "1674fc3d8d94c601"  # 001-8-3 (ouro)
SLUG = "001-8-3-anuncios-a-alma-do-seu-trafego-pago"
OURO_005 = "869445a4c64befbf"  # 005-4-0 (ouro)
SLUG_005 = "005-4-0-minha-campanha-esta-gastando-toda-verba-em-um-unico-grupo-de-anuncio-e-agora"

FRONT = f"""---
type: unidades-aula
status: rascunho
title: "8.3 - Anúncios - a alma do seu tráfego pago"
modulo: "001"
ordem: 12
aula_id: {AULA}
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - transcricao.md
  - cst_m01_a8.3_anuncios_a_alma_do_negocio.pdf
  - cst_m01_a83_manual_de_criativos.pdf
extraido_em: 2026-09-13
gerado_por: fable-5.1
retiradas: []
divisoes: []
fusoes: []
---

# 8.3 - Anúncios - a alma do seu tráfego pago

## Contexto da aula
Linha um do contexto.
Linha dois do contexto.
Linha três do contexto.

## Unidades
"""

BLOCO_OK = f"""### U:{AULA}:001 — Referências antes de criar
```yaml
tipo: regua
plataforma: [geral]
tema: criativo
tarefas: [coletar-referencias-de-anuncio]
fonte: fala
faixa: 00:11:52–00:13:10
perecivel: false
confianca: alta
versao: 1
```
Salve pelo menos 10 anúncios de referência antes de produzir o primeiro criativo.
"""

BLOCO_OK_2 = f"""### U:{AULA}:002 — Pré-condição do briefing
```yaml
tipo: procedimento
plataforma: [meta]
tema: criativo
tarefas: [fazer-briefing-de-criativo]
fonte: fala+pdf:cst_m01_a83_manual_de_criativos.pdf
faixa: 00:20:00–00:22:00
perecivel: false
confianca: alta
versao: 1
```
Pré-condição: referências salvas.
1. Descreva a situação.
2. Aponte a referência.
"""

BLOCO_OK_3 = f"""### U:{AULA}:003 — Anúncio decide o custo
```yaml
tipo: conceito
plataforma: [geral]
tema: leilao-e-lances
tarefas: []
fonte: fala
faixa: 00:00:34–00:02:00
perecivel: false
confianca: alta
versao: 1
```
Qualidade do anúncio é o terceiro fator do leilão.
"""

FONTES_DISCO = ["transcricao.md", "cst_m01_a8.3_anuncios_a_alma_do_negocio.pdf", "cst_m01_a83_manual_de_criativos.pdf"]


def _validar(text, **kw):
    manifest = lib.load_manifest()
    tax = lib.load_taxonomia(BASE / "taxonomia.md")
    return val.validar_texto(text, slug=SLUG, manifest=manifest, taxonomia=tax, fontes_disco=FONTES_DISCO, **kw)


class ParserTest(unittest.TestCase):
    def test_round_trip_basico(self):
        arq = lib.parse_arquivo_unidades(FRONT + BLOCO_OK + BLOCO_OK_2 + BLOCO_OK_3)
        self.assertEqual(arq.front["aula_id"], AULA)
        self.assertEqual(arq.front["fontes"][1], "cst_m01_a8.3_anuncios_a_alma_do_negocio.pdf")
        self.assertEqual(len(arq.contexto), 3)
        self.assertEqual([u.nnn for u in arq.unidades], [1, 2, 3])
        u = arq.unidades[0]
        self.assertEqual(u.id, f"U:{AULA}:001")
        self.assertEqual(u.titulo, "Referências antes de criar")
        self.assertEqual(u.meta["plataforma"], ["geral"])
        self.assertEqual(u.meta["tarefas"], ["coletar-referencias-de-anuncio"])
        self.assertEqual(u.meta["faixa"], "00:11:52–00:13:10")
        self.assertEqual(u.corpo, ["Salve pelo menos 10 anúncios de referência antes de produzir o primeiro criativo."])
        self.assertEqual(lib.parse_faixa(u.meta["faixa"]), (712, 790))
        self.assertEqual(arq.unidades[2].meta["tarefas"], [])

    def test_parse_bloco_yaml_plano(self):
        d = lib.parse_bloco_yaml('a: 1\nb: [x, y]\nc: "com: dois pontos"\nd: true\ne: []\n')
        self.assertEqual(d, {"a": 1, "b": ["x", "y"], "c": "com: dois pontos", "d": True, "e": []})

    def test_front_matter_listas_em_bloco(self):
        front, _ = lib.parse_front_matter('---\nx: 1\nlista:\n  - a\n  - "b c"\nvazia: []\n---\ncorpo')
        self.assertEqual(front["lista"], ["a", "b c"])
        self.assertEqual(front["vazia"], [])

    def test_serializa_e_reparseia(self):
        arq = lib.parse_arquivo_unidades(FRONT + BLOCO_OK)
        text = lib.serializar_unidade(arq.unidades[0])
        arq2 = lib.parse_arquivo_unidades(FRONT + text)
        self.assertEqual(lib.hash_unidade(arq.unidades[0]), lib.hash_unidade(arq2.unidades[0]))


class ValidadorTest(unittest.TestCase):
    def test_arquivo_valido_zero_erros(self):
        erros, _ = _validar(FRONT + BLOCO_OK + BLOCO_OK_2 + BLOCO_OK_3)
        self.assertEqual(erros, [])

    def test_gerado_por_aceita_modelos_claude_e_codex(self):
        modelos = ("sonnet-5", "opus-5", "fable-5.1", "gpt-5.6-sol", "gpt-5.6-terra", "gpt-6-astra")
        for modelo in modelos:
            with self.subTest(modelo=modelo):
                front = FRONT.replace("gerado_por: fable-5.1", f"gerado_por: {modelo}")
                erros, _ = _validar(front + BLOCO_OK + BLOCO_OK_2 + BLOCO_OK_3)
                self.assertEqual(erros, [])

    def test_menos_de_tres_unidades_e_erro(self):
        erros, _ = _validar(FRONT + BLOCO_OK)
        self.assertTrue(any("mínimo" in e or "minimo" in e for e in erros), erros)

    def test_tema_fora_do_enum(self):
        erros, _ = _validar(FRONT + BLOCO_OK.replace("tema: criativo", "tema: inexistente") + BLOCO_OK_2 + BLOCO_OK_3)
        self.assertTrue(any("tema" in e and "inexistente" in e for e in erros), erros)

    def test_faixa_fora_da_duracao(self):
        erros, _ = _validar(FRONT + BLOCO_OK.replace("00:11:52–00:13:10", "00:41:00–00:42:00") + BLOCO_OK_2 + BLOCO_OK_3)
        self.assertTrue(any("faixa" in e for e in erros), erros)

    def test_timestamp_no_corpo(self):
        bad = BLOCO_OK.replace("antes de produzir", "antes de produzir (aos 11:52)")
        erros, _ = _validar(FRONT + bad + BLOCO_OK_2 + BLOCO_OK_3)
        self.assertTrue(any("timestamp" in e for e in erros), erros)

    def test_hoje_no_corpo(self):
        bad = BLOCO_OK.replace("Salve pelo menos", "Hoje salve pelo menos")
        erros, _ = _validar(FRONT + bad + BLOCO_OK_2 + BLOCO_OK_3)
        self.assertTrue(any("hoje" in e.lower() for e in erros), erros)

    def test_regua_sem_numero(self):
        bad = BLOCO_OK.replace("Salve pelo menos 10 anúncios", "Salve anúncios")
        erros, _ = _validar(FRONT + bad + BLOCO_OK_2 + BLOCO_OK_3)
        self.assertTrue(any("regua" in e for e in erros), erros)

    def test_regua_com_numeral_por_extenso_passa(self):
        ok = BLOCO_OK.replace("Salve pelo menos 10 anúncios", "Salve pelo menos cinco anúncios")
        erros, _ = _validar(FRONT + ok + BLOCO_OK_2 + BLOCO_OK_3)
        self.assertEqual(erros, [])

    def test_descricao_de_tela_exige_perecivel(self):
        bad = BLOCO_OK.replace("Salve pelo menos 10 anúncios de referência antes de produzir o primeiro criativo.", "Abra a aba Anúncios e use o botão Salvar pelo menos 10 vezes.")
        erros, _ = _validar(FRONT + bad + BLOCO_OK_2 + BLOCO_OK_3)
        self.assertTrue(any("perecivel" in e and "tela" in e for e in erros), erros)
        inocente = BLOCO_OK.replace("Salve pelo menos 10 anúncios de referência antes de produzir o primeiro criativo.", "Espere pelo menos 10 cliques por anúncio antes de julgar o CTR.")
        self.assertEqual(_validar(FRONT + inocente + BLOCO_OK_2 + BLOCO_OK_3)[0], [])
        ok = bad.replace("perecivel: false", "perecivel: true")
        erros, _ = _validar(FRONT + ok + BLOCO_OK_2 + BLOCO_OK_3)
        self.assertEqual(erros, [])

    def test_alerta_ui_exige_perecivel(self):
        bad = BLOCO_OK.replace("tipo: regua", "tipo: alerta-ui")
        erros, _ = _validar(FRONT + bad + BLOCO_OK_2 + BLOCO_OK_3)
        self.assertTrue(any("perecivel" in e for e in erros), erros)

    def test_tarefas_vazia_so_em_conceito_ou_limite(self):
        bad = BLOCO_OK.replace("tarefas: [coletar-referencias-de-anuncio]", "tarefas: []")
        erros, _ = _validar(FRONT + bad + BLOCO_OK_2 + BLOCO_OK_3)
        self.assertTrue(any("tarefas" in e for e in erros), erros)

    def test_furo_na_numeracao(self):
        b3 = BLOCO_OK_3.replace(f"U:{AULA}:003", f"U:{AULA}:005")
        erros, _ = _validar(FRONT + BLOCO_OK + BLOCO_OK_2 + b3)
        self.assertTrue(any("furo" in e or "001..max" in e for e in erros), erros)

    def test_retirada_fecha_o_furo_e_numero_retirado_nao_volta(self):
        front = FRONT.replace("retiradas: []", f"retiradas: [U:{AULA}:003]")
        b4 = BLOCO_OK_3.replace(f"U:{AULA}:003", f"U:{AULA}:004")
        erros, _ = _validar(front + BLOCO_OK + BLOCO_OK_2 + b4)
        self.assertEqual(erros, [])
        erros, _ = _validar(front + BLOCO_OK + BLOCO_OK_2 + BLOCO_OK_3)
        self.assertTrue(any("retirad" in e for e in erros), erros)

    def test_fonte_pdf_fora_de_fontes(self):
        bad = BLOCO_OK_2.replace("fala+pdf:cst_m01_a83_manual_de_criativos.pdf", "fala+pdf:outro.pdf")
        erros, _ = _validar(FRONT + BLOCO_OK + bad + BLOCO_OK_3)
        self.assertTrue(any("outro.pdf" in e for e in erros), erros)

    def test_pdf_no_disco_ausente_de_fontes(self):
        front = FRONT.replace("  - cst_m01_a83_manual_de_criativos.pdf\n", "")
        b2 = BLOCO_OK_2.replace("fala+pdf:cst_m01_a83_manual_de_criativos.pdf", "fala")
        erros, _ = _validar(front + BLOCO_OK + b2 + BLOCO_OK_3)
        self.assertTrue(any("manual_de_criativos" in e for e in erros), erros)

    def test_confianca_baixa_exige_nota(self):
        bad = BLOCO_OK.replace("confianca: alta", "confianca: baixa")
        erros, _ = _validar(FRONT + bad + BLOCO_OK_2 + BLOCO_OK_3)
        self.assertTrue(any("nota" in e for e in erros), erros)

    def test_copia_bruta_de_25_palavras(self):
        palavras = " ".join(f"p{i}" for i in range(30))
        bad = BLOCO_OK.replace("Salve pelo menos 10 anúncios de referência antes de produzir o primeiro criativo.", "Salve 10: " + palavras)
        erros, _ = _validar(FRONT + bad + BLOCO_OK_2 + BLOCO_OK_3, textos_fonte={"transcricao.md": "x " + palavras + " y"})
        self.assertTrue(any("cópia" in e or "copia" in e for e in erros), erros)


class HashVersaoTest(unittest.TestCase):
    def test_hash_ignora_versao_e_nota_mas_ve_corpo(self):
        a = lib.parse_arquivo_unidades(FRONT + BLOCO_OK).unidades[0]
        b = lib.parse_arquivo_unidades(FRONT + BLOCO_OK.replace("versao: 1", "versao: 2\nnota: \"x\"")).unidades[0]
        c = lib.parse_arquivo_unidades(FRONT + BLOCO_OK.replace("pelo menos 10", "pelo menos 12")).unidades[0]
        self.assertEqual(lib.hash_unidade(a), lib.hash_unidade(b))
        self.assertNotEqual(lib.hash_unidade(a), lib.hash_unidade(c))

    def test_versao_tem_de_subir_quando_hash_muda(self):
        a = lib.parse_arquivo_unidades(FRONT + BLOCO_OK).unidades[0]
        prev = {a.id: {"hash": lib.hash_unidade(a), "versao": 1}}
        erros, _ = _validar(FRONT + BLOCO_OK.replace("pelo menos 10", "pelo menos 12") + BLOCO_OK_2 + BLOCO_OK_3, prev=prev)
        self.assertTrue(any("versao" in e for e in erros), erros)
        erros, _ = _validar(
            FRONT + BLOCO_OK.replace("pelo menos 10", "pelo menos 12").replace("versao: 1", "versao: 2") + BLOCO_OK_2 + BLOCO_OK_3,
            prev=prev,
        )
        self.assertEqual(erros, [])


class ArquivosReaisTest(unittest.TestCase):
    """Adicionado no commit em que os ouros passam a existir; contagens totais só em S9."""

    def test_preflight_clone_e_pdftotext(self):
        self.assertEqual(lib.verificar_fontes(), [])
        self.assertTrue(lib.pdftotext_disponivel())

    def test_slug_de_todas_as_aulas_bate_com_a_lista_v1(self):
        manifest = lib.load_manifest()
        self.assertEqual(len(manifest), 133)
        esperados = set((FERRAMENTA.parent / "tests" / "slugs-v1.txt").read_text(encoding="utf-8").split())
        self.assertEqual({row["slug"] for row in manifest.values()}, esperados)

    def test_ouros_existem_e_validam_sem_erros(self):
        ouros = [p for p in (BASE / "unidades").glob("*.md") if "status: ouro" in p.read_text(encoding="utf-8")]
        self.assertGreaterEqual(len(ouros), 2)
        resultado = val.validar_root(BASE)
        self.assertEqual(resultado["erros"], [], json.dumps(resultado["erros"], ensure_ascii=False, indent=1))

    def test_ouro_8_3_nao_e_gerado_por_subagente(self):
        text = (BASE / "unidades" / f"{SLUG}.md").read_text(encoding="utf-8")
        self.assertIn("gerado_por: fable-5.1", text)
        self.assertIn("status: ouro", text)

    MODULOS_FECHADOS = {"001": 18, "002": 36, "003": 7, "004": 15, "005": 28, "006": 8, "007": 7, "008": 14}   # módulo: aulas; todos os módulos fechados

    def test_modulos_fechados_completos_e_validados(self):
        for mod, n in self.MODULOS_FECHADOS.items():
            arquivos = sorted((BASE / "unidades").glob(f"{mod}-*.md"))
            self.assertEqual(len(arquivos), n, mod)
            for p in arquivos:
                front, _ = lib.parse_front_matter(p.read_text(encoding="utf-8"))
                self.assertIn(front["status"], {"validado", "revisado", "ouro"}, p.name)
                self.assertNotIn("proposta_tag", p.read_text(encoding="utf-8"), p.name)

    def test_pendentes_lista_so_aulas_sem_arquivo(self):
        import pacote
        pend = pacote.pendentes(BASE)
        slugs_extraidos = {p.stem for p in (BASE / "unidades").glob("*.md")}
        self.assertEqual(len(pend) + len(slugs_extraidos), 133)
        self.assertTrue(all(r["slug"] not in slugs_extraidos for r in pend))
        self.assertEqual(len(pacote.pendentes(BASE, modulo="002")), 0)  # Sessão 6: módulo completo e validado por amostra

    def test_palavras_da_aula_contam_so_transcricao_e_pdfs(self):
        """total - aula = tudo que não é fonte (papel, FORMATO, taxonomia, âncora, cabeçalhos)."""
        import pacote
        row = lib.load_manifest()[OURO_005]
        texto = pacote.pacote_extracao(BASE, OURO_005)
        aula = pacote.palavras_aula(row)
        resto = texto
        for nome in lib.fontes_no_disco(row):
            t = lib.texto_fonte(row, nome)
            if nome == "transcricao.md":
                t = lib.transcricao_sem_cabecalho(t)
            self.assertIn(t, resto, nome)
            resto = resto.replace(t, "", 1)
        self.assertEqual(len(texto.split()) - aula, len(resto.split()))
        self.assertGreater(aula, 0)

    def test_cli_extracao_imprime_total_e_palavras_da_aula(self):
        import io
        import re
        import tempfile
        from contextlib import redirect_stdout
        import pacote
        with tempfile.TemporaryDirectory() as tmp:
            buf = io.StringIO()
            with redirect_stdout(buf):
                pacote.main(["extracao", OURO_005, "--root", str(BASE), "--saida", tmp])
            m = re.search(r" (\d+) palavras \(aula: (\d+)\)\s*$", buf.getvalue())
            self.assertIsNotNone(m, buf.getvalue())
            self.assertGreater(int(m.group(1)), int(m.group(2)))

    def test_cli_extracao_e_reextracao_propagam_gerado_por(self):
        import subprocess
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            for modo, modelo in (("extracao", "gpt-5.6-sol"), ("reextracao", "gpt-6-astra")):
                with self.subTest(modo=modo, modelo=modelo):
                    proc = subprocess.run(
                        [sys.executable, str(FERRAMENTA / "pacote.py"), modo, OURO_005, "--root", str(BASE), "--saida", tmp, "--gerado-por", modelo],
                        capture_output=True,
                        text=True,
                    )
                    self.assertEqual(proc.returncode, 0, proc.stderr)
                    texto = (Path(tmp) / f"{modo}-{SLUG_005}.md").read_text(encoding="utf-8")
                    self.assertIn(f"gerado_por: {modelo}", texto)

    def test_cli_extracao_mantem_default_legado(self):
        import subprocess
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            proc = subprocess.run(
                [sys.executable, str(FERRAMENTA / "pacote.py"), "extracao", OURO_005, "--root", str(BASE), "--saida", tmp],
                capture_output=True,
                text=True,
            )
            self.assertEqual(proc.returncode, 0, proc.stderr)
            texto = (Path(tmp) / f"extracao-{SLUG_005}.md").read_text(encoding="utf-8")
            self.assertIn("gerado_por: sonnet-5", texto)

    def test_cli_rejeita_modelo_desconhecido(self):
        import subprocess
        proc = subprocess.run(
            [sys.executable, str(FERRAMENTA / "pacote.py"), "extracao", OURO_005, "--root", str(BASE), "--gerado-por", "modelo-inexistente"],
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("invalid choice", proc.stderr)

    def test_cli_rejeita_gerado_por_em_modo_que_nao_o_utiliza(self):
        import subprocess
        proc = subprocess.run(
            [sys.executable, str(FERRAMENTA / "pacote.py"), "pendentes", "--root", str(BASE), "--gerado-por", "gpt-5.6-sol"],
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("só pode ser usado", proc.stderr)

    PACOTE_EXTRACAO_OURO_005_ANTES_DA_3B = 6663  # palavras medidas em 2026-09-14 com FORMATO.md inteiro no pacote

    def test_pacote_de_extracao_traz_so_formato_1_a_4(self):
        import pacote
        texto = pacote.pacote_extracao(BASE, OURO_005)
        self.assertLess(len(texto.split()), self.PACOTE_EXTRACAO_OURO_005_ANTES_DA_3B)
        self.assertNotIn("## 5.", texto)
        self.assertNotIn("## 6.", texto)
        self.assertIn("## 3. Identidade", texto)
        self.assertIn("## taxonomia.md", texto)

    def test_pacote_de_inspecao_sem_taxonomia_extrator_nem_ancora(self):
        import pacote
        texto = pacote.pacote_inspecao(BASE, OURO_005)
        self.assertNotIn("## taxonomia.md", texto)
        self.assertNotIn("Âncora", texto)
        self.assertNotIn("Papel — extrator", texto)
        self.assertIn("Papel — inspetor", texto)
        self.assertIn("## RUBRICA.md", texto)
        self.assertIn("## 8. Laudo", texto)
        self.assertNotIn("## 6.", texto)
        self.assertIn((BASE / "unidades" / f"{SLUG_005}.md").read_text(encoding="utf-8"), texto)
        row = lib.load_manifest()[OURO_005]
        self.assertIn(lib.transcricao_sem_cabecalho(lib.texto_fonte(row, "transcricao.md")), texto)

    def test_correcao_e_inspecao_preservam_autoria_do_insumo(self):
        import pacote
        uid = f"U:{OURO_005}:001"
        correcao = pacote.pacote_correcao(BASE, OURO_005, unidades=[uid], erros="erro de teste")
        inspecao = pacote.pacote_inspecao(BASE, OURO_005)
        self.assertIn("gerado_por: fable-5.1", correcao)
        self.assertIn("gerado_por: fable-5.1", inspecao)

    def test_pacote_de_correcao_e_enxuto_e_traz_bloco_e_trecho_da_faixa(self):
        """Limiar medido em 2026-09-14: papel (352) + FORMATO §1 a §4 (1051) já são 21% do pacote do ouro 005; 25% não fecha nessa aula curta."""
        import re
        import pacote
        uid = f"U:{OURO_005}:001"
        texto = pacote.pacote_correcao(BASE, OURO_005, unidades=[uid], erros=f"{uid}: regua sem número ou unidade")
        extracao = pacote.pacote_extracao(BASE, OURO_005)
        self.assertLess(len(texto.split()), 0.4 * len(extracao.split()))
        arq = lib.parse_arquivo_unidades((BASE / "unidades" / f"{SLUG_005}.md").read_text(encoding="utf-8"))
        u = next(x for x in arq.unidades if x.id == uid)
        self.assertIn(lib.serializar_unidade(u), texto)
        outra = next(x for x in arq.unidades if x.id != uid)
        self.assertNotIn(lib.serializar_unidade(outra), texto)
        row = lib.load_manifest()[OURO_005]
        tr = lib.transcricao_sem_cabecalho(lib.texto_fonte(row, "transcricao.md"))
        a, b = lib.parse_faixa(u.meta["faixa"])
        dentro, fora = [], []
        for m in re.finditer(r"\*\*\[(\d\d:\d\d:\d\d)[–-](\d\d:\d\d:\d\d)\]\*\*", tr):
            x, y = lib.parse_faixa(f"{m.group(1)}–{m.group(2)}")
            (dentro if (y >= a - 60 and x <= b + 60) else fora).append(m.group(0))
        self.assertTrue(dentro and fora)
        for marca in dentro:
            self.assertIn(marca, texto)
        for marca in fora:
            self.assertNotIn(marca, texto)
        self.assertNotIn("## taxonomia.md", texto)
        self.assertNotIn("Âncora", texto)
        self.assertNotIn("## 5.", texto)
        self.assertIn("regua sem número ou unidade", texto)
        self.assertIn("aula_id: " + OURO_005, texto)

    def test_correcao_de_unidade_sem_faixa_usa_janela_das_vizinhas(self):
        import pacote
        arq = lib.parse_arquivo_unidades((BASE / "unidades" / f"{SLUG_005}.md").read_text(encoding="utf-8"))
        alvo = arq.unidades[3]
        anterior, seguinte = arq.unidades[2], arq.unidades[4]
        faixa = pacote.faixa_para_janela(arq.unidades, alvo.id, ignorar_propria=True)
        a, b = lib.parse_faixa(faixa)
        self.assertEqual(a, lib.parse_faixa(anterior.meta["faixa"])[0])
        self.assertEqual(b, lib.parse_faixa(seguinte.meta["faixa"])[1])

    def test_cli_correcao_e_inspecao_imprimem_caminho_e_palavras(self):
        import io
        import tempfile
        from contextlib import redirect_stdout
        import pacote
        with tempfile.TemporaryDirectory() as tmp:
            buf = io.StringIO()
            with redirect_stdout(buf):
                pacote.main(["correcao", OURO_005, "--root", str(BASE), "--saida", tmp, "--unidades", f"U:{OURO_005}:001,U:{OURO_005}:002", "--erros", "erro de teste"])
                pacote.main(["inspecao", OURO_005, "--root", str(BASE), "--saida", tmp])
            linhas = buf.getvalue().strip().splitlines()
            self.assertEqual(len(linhas), 2, buf.getvalue())
            for l in linhas:
                self.assertRegex(l, r" \d+ palavras$")
            self.assertTrue((Path(tmp) / f"correcao-{SLUG_005}.md").exists())
            self.assertTrue((Path(tmp) / f"inspecao-{SLUG_005}.md").exists())


if __name__ == "__main__":
    unittest.main()
