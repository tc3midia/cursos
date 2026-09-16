"""Reconciliação de reextração: IDs preservados, novos no fim, retiradas, divisões e fusões."""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FERRAMENTA = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(FERRAMENTA))

import reconciliar  # noqa: E402
import unidades as lib  # noqa: E402

AULA = "0123456789abcdef"
FRONT = f"""---
type: unidades-aula
status: rascunho
title: "Teste"
modulo: "001"
ordem: 1
aula_id: {AULA}
account_id: account.86ajrj8n9
promoted_by: human.will
fonte_repo: tc3midia/curso-subido-trafego-transcricoes
fonte_commit: f188775
fontes:
  - transcricao.md
extraido_em: 2026-09-14
gerado_por: sonnet-5
retiradas: []
divisoes: []
fusoes: []
---

# Teste

## Contexto da aula
Aula de teste.

## Unidades
"""


def bloco(n: int, titulo: str, corpo: str, versao: int = 1) -> str:
    return f"""### U:{AULA}:{n:03d} — {titulo}
```yaml
tipo: regra
plataforma: [meta]
tema: criativo
tarefas: [configurar-anuncio]
fonte: fala
faixa: 00:01:00–00:02:00
perecivel: false
confianca: alta
versao: {versao}
```
{corpo}

"""


ANTIGO = FRONT + bloco(1, "Um anúncio por ideia", "Cada anúncio testa uma ideia só.") + bloco(2, "Cinco ou seis anúncios por conjunto", "Subir cinco ou seis anúncios por conjunto para o leilão escolher.") + bloco(3, "Trocar criativo cansado", "Trocar o criativo quando a frequência passa de três.")


class ReconciliarTest(unittest.TestCase):
    def test_mesma_unidade_com_texto_corrigido_preserva_id_e_sobe_versao(self):
        novo = FRONT + bloco(1, "Um anúncio por ideia", "Cada anúncio testa uma única ideia.") + bloco(2, "Cinco ou seis anúncios por conjunto", "Subir cinco ou seis anúncios por conjunto para o leilão escolher.") + bloco(3, "Trocar criativo cansado", "Trocar o criativo quando a frequência passa de três.")
        texto, rel = reconciliar.reconciliar(ANTIGO, novo)
        arq = lib.parse_arquivo_unidades(texto)
        ids = [u.id for u in arq.unidades]
        self.assertEqual(ids, [f"U:{AULA}:001", f"U:{AULA}:002", f"U:{AULA}:003"])
        self.assertEqual(arq.unidades[0].meta["versao"], 2)
        self.assertEqual(arq.unidades[1].meta["versao"], 1)
        self.assertEqual(rel["novas"], [])

    def test_divisao_retira_a_antiga_e_numera_as_novas_no_fim(self):
        novo = FRONT + bloco(1, "Um anúncio por ideia", "Cada anúncio testa uma ideia só.") + bloco(2, "Cinco anúncios no mínimo", "Subir pelo menos cinco anúncios por conjunto.") + bloco(3, "Seis anúncios no máximo", "Não passar de seis anúncios por conjunto.") + bloco(4, "Trocar criativo cansado", "Trocar o criativo quando a frequência passa de três.")
        texto, rel = reconciliar.reconciliar(ANTIGO, novo, divisoes=[(f"U:{AULA}:002", [2, 3])])
        arq = lib.parse_arquivo_unidades(texto)
        ids = [u.id for u in arq.unidades]
        self.assertEqual(ids, [f"U:{AULA}:001", f"U:{AULA}:003", f"U:{AULA}:004", f"U:{AULA}:005"])
        self.assertEqual(arq.front["retiradas"], [f"U:{AULA}:002"])
        self.assertEqual(arq.front["divisoes"], [f"U:{AULA}:002 → U:{AULA}:004, U:{AULA}:005"])

    def test_unidade_que_some_vai_para_retiradas(self):
        novo = FRONT + bloco(1, "Um anúncio por ideia", "Cada anúncio testa uma ideia só.") + bloco(2, "Cinco ou seis anúncios por conjunto", "Subir cinco ou seis anúncios por conjunto para o leilão escolher.")
        texto, rel = reconciliar.reconciliar(ANTIGO, novo)
        arq = lib.parse_arquivo_unidades(texto)
        self.assertEqual(arq.front["retiradas"], [f"U:{AULA}:003"])
        self.assertEqual(rel["retiradas"], [f"U:{AULA}:003"])

    def test_numero_retirado_nao_volta(self):
        antigo = ANTIGO.replace("retiradas: []", f"retiradas: [U:{AULA}:004]")
        novo = FRONT + bloco(1, "Um anúncio por ideia", "Cada anúncio testa uma ideia só.") + bloco(2, "Cinco ou seis anúncios por conjunto", "Subir cinco ou seis anúncios por conjunto para o leilão escolher.") + bloco(3, "Trocar criativo cansado", "Trocar o criativo quando a frequência passa de três.") + bloco(4, "Nova orientação", "Regra nova que não existia.")
        texto, rel = reconciliar.reconciliar(antigo, novo)
        arq = lib.parse_arquivo_unidades(texto)
        self.assertEqual([u.id for u in arq.unidades][-1], f"U:{AULA}:005")
        self.assertEqual(rel["novas"], [f"U:{AULA}:005"])


if __name__ == "__main__":
    unittest.main()
