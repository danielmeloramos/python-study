import unittest

from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    
    def setUp(self):
        self.calculadora = Calculadora(10, 10)

    def test_sum_deveria_retornar_valor_vinte_ao_realizar_a_soma(self):
        result = self.calculadora.sum()
        self.assertEqual(result, 20)

    def test_subtraction_deveria_retornar_valor_zero_ao_realizar_a_subtracao(self):
        result = self.calculadora.subtraction()
        self.assertEqual(result, 0)

    def test_multiplication_deveria_retornar_valor_cem_ao_realizar_a_multiplicacao(self):
        result = self.calculadora.multiplication()
        self.assertEqual(result, 100)

    def test_division_deveria_retornar_valor_um_ao_realizar_a_divisao(self):
        result = self.calculadora.division()
        self.assertEqual(result, 1)