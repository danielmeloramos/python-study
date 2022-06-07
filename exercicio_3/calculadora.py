class ExampleName:
    """Classe de exemplo"""

    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value


class Calculadora:
    """Calculadora

    Calculadora que recebe dois valores e realiza as operações:
    soma, subtração, multiplicação e divisão
    """

    def __init__(self, value_1, value_2):
        self.value_1 = value_1
        self.value_2 = value_2

    def soma(self):
        return self.value_1 + self.value_2

    def subtracao(self):
        return self.value_1 - self.value_2

    def multiplicacao(self):
        return self.value_1 * self.value_2

    def divisao(self):
        return self.value_1 / self.value_2


class CalculadoraCientifica(Calculadora):
    """Calculadora Cientifica

    Calculadora que recebe dois valores e realiza as operações:
    soma, subtração, multiplicação, divisão, exponenciação e resto
    """

    def exponenciacao(self):
        return self.value_1 ** self.value_2

    def resto(self):
        return self.value_1 % self.value_2
