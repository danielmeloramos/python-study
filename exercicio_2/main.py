from calculadora import Calculadora
from calculadora_cientifica import CalculadoraCientifica

FIRST_VALUE = 10
SECOND_VALUE = 20

# Sem Heranca
calculator = Calculadora(FIRST_VALUE, SECOND_VALUE)

response_sum = calculator.sum()
response_subtraction = calculator.subtraction()
response_multiplication = calculator.multiplication()
response_division = calculator.division()

print(f"SEM HERANCA")
print(f"Soma: {response_sum}")
print(f"Subtratacao: {response_subtraction}")
print(f"Multiplicacao: {response_multiplication}")
print(f"Divisao: {response_division}")

# Com Heranca
calculatorCientifica = CalculadoraCientifica(FIRST_VALUE, SECOND_VALUE)
response_sum = calculatorCientifica.sum()
response_subtraction = calculatorCientifica.subtraction()
response_multiplication = calculatorCientifica.multiplication()
response_division = calculatorCientifica.division()
response_exponenciacao = calculatorCientifica.exponenciacao()
response_division_rest = calculatorCientifica.resto_divisao()

print(f"COM HERANCA")
print(f"Soma: {response_sum}")
print(f"Subtratacao: {response_subtraction}")
print(f"Multiplicacao: {response_multiplication}")
print(f"Divisao: {response_division}")
print(f"Exponenciacao: {response_exponenciacao}")
print(f"Resto de divisao: {response_division_rest}")