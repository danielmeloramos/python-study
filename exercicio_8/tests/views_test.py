from tests.base import TestBase


class TestExample(TestBase):
    def test_render_data(self):
        """
            Criando uma resposta falsa para o client
            primeiro parametro: status a ser retornado
            segundo parametro: lista dos itens
        """
        self.mock(200, [{"title": "teste"}])
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Hello, World", response.data.decode("utf-8"))
