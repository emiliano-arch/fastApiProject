
class Suma:

    def __init__(self, num1, num2):
        self.numero = num1
        self.numero2 = num2

    def sumar(self):
        return self.numero + 100

    def sumaCompleta(self):
        return self.numero + self.numero2


    @property
    def __str__(self):
        return f"{sumaCompleta()}"
