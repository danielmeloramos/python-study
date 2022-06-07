import unittest  # biblioteca padrão para realizar testes
from unittest.mock import (
    patch,
    Mock,
)  # pacotes para mockar um determinado comportamento

from feed import app


class TestBase(unittest.TestCase):
    def setUp(self):
        # inicializando um app falsa para teste
        self.app = app.test_client()

    def tearDown(self):
        # resetando tos dos mocks
        self.mock(200, [])

    @patch("alf.client.Client")
    def mock(self, status_code, feeds, MockClient):
        # Cria o client falso
        client = MockClient()

        # Define a resposta do .get
        response_mock = Mock()
        response_mock.json.return_value = {"items": feeds}
        response_mock.status_code = status_code

        # resposta do .post
        response_post_mock = Mock()
        response_post_mock.status_code = status_code

        client.get.return_value = response_mock
        client.post.return_value = response_post_mock
        self.app.application.config["CLIENT"] = client
