class Calculadora:

    def __init__(self, first_value, second_value):
        self.first_value = first_value
        self.second_value = second_value

    def sum(self):
        return self.first_value + self.second_value

    def subtraction(self):
        return self.first_value - self.second_value

    def multiplication(self):
        return self.first_value * self.second_value

    def division(self):
        return self.first_value / self.second_value
