class Circulo:
    def __init__(self):
        self.raio = 0

    def area(self):
        self.raio = float(input("Digite o raio da circunferencia: "))
        area = 3.14 * self.raio ** 2
        return f"A area do circulo é de : {area}"

circulo = Circulo()

circulo.area()