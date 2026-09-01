import unittest

from modelo_ml import responder_com_aprendizado


class TestBibliasBooks(unittest.TestCase):
    def test_reconhece_pergunta_sobre_livros(self):
        resposta = responder_com_aprendizado("quais são os livros da Bíblia")
        self.assertIsNotNone(resposta)

    def test_reconhece_livro_da_biblia(self):
        resposta = responder_com_aprendizado("gênesis")
        self.assertIsNotNone(resposta)

    def test_responde_diretamente_o_primeiro_livro_da_biblia(self):
        from chatbot import responder

        resposta = responder("qual foi o primeiro livro da Bíblia")
        self.assertIn("Gênesis", resposta)

    def test_registra_pergunta_e_resposta_no_banco(self):
        from database import registrar_resposta, listar_respostas

        pergunta = "qual é a mensagem de Gênesis?"
        resposta = "Gênesis fala sobre a criação e a história dos patriarcas."

        registrar_resposta(pergunta, resposta, categoria="biblia")
        registros = listar_respostas(limit=5)
        self.assertTrue(any(item["pergunta"] == pergunta for item in registros))


if __name__ == "__main__":
    unittest.main()
