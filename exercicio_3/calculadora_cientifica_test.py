import unittest

from calculadora_cientifica import CalculadoraCientifica

class TestCalculadoraCientifica(unittest.TestCase):

    def setUp(self):
        self.calculadora_cientifica = CalculadoraCientifica(1, 1)
    
    def test_exponenciacao_deveria_retornar_valor_um_ao_realizar_a_exponenciacao(self):
        result = self.calculadora_cientifica.exponenciacao()
        self.assertEqual(result, 1)

    def test_resto_divisao_deveria_retornar_valor_zero_ao_realizar_o_resto_de_divisao(self):
        result = self.calculadora_cientifica.resto_divisao()
        self.assertEqual(result, 0)