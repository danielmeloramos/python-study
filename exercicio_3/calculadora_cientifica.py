from calculadora import Calculadora

class CalculadoraCientifica(Calculadora):

    def exponenciacao(self):
        return self.first_value ** self.second_value

    def resto_divisao(self):
        return self.first_value % self.second_value