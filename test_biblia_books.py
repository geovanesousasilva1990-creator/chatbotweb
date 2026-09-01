import unittest

from modelo_ml import responder_com_aprendizado


class TestBibliasBooks(unittest.TestCase):
    def test_reconhece_pergunta_sobre_livros(self):
        resposta = responder_com_aprendizado("quais são os livros da Bíblia")
        self.assertIsNotNone(resposta)

    def test_reconhece_livro_da_biblia(self):
        resposta = responder_com_aprendizado("gênesis")
        self.assertIsNotNone(resposta)


if __name__ == "__main__":
    unittest.main()
