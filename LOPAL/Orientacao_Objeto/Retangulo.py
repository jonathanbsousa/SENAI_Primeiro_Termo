class Retangulo:
    def __init__(self):
        self.altura = 0
        self.largura = 0

    def perimetro(self):
        self.altura = float(input("Digite a altura do retangulo: "))
        self.largura = float(input("Digite a largura do retangulo: "))
        perimetro = 2 * (self.largura + self.altura)
        return f"O perimetro do retangulo é de : {perimetro}"
        
retangulo= Retangulo()

retangulo.perimetro()