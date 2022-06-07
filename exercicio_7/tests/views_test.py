import unittest

from blog import app


class TestViews(unittest.TestCase):
    def setUp(self):
        """Cria uma app falsa do flask"""
        self.app = app.test_client()

    def test_blog_view(self):
        """Test da rota principal

        Simula uma requisição para a rota `/` com o método GET e
        verifica se o conteúdo está dentro do resultado
        """
        result = self.app.get("/")
        self.assertIn("Hello, World", result.data.decode("utf-8"))
