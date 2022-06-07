# Pacote padrão para realizar testes unitários
import unittest

from calculadora import ExampleName


class TestExample(unittest.TestCase):
    """Classe de exemplo

    PEP8: Nome da classe com CamelCase
    """

    def setUp(self):
        """Construtor do teste

        Permite definir instruções que serão executadas antes
        de cada método de teste
        """
        self.example = ExampleName(30)

    def test_get_value(self):
        """Método de teste

        PEP8: Nome do método em letras_minusculas_com_underscore

        Sempre começa com `test_` e testa se uma funcionalidade está sendo aceita
        """
        result = self.example.get_value()
        self.assertEqual(result, 30)
