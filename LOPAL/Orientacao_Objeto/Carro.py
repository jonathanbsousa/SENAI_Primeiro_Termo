class Carro:
    def __init__(self, velocidade):
        self.velocidade = velocidade

    def on_off(self):
        if self.velocidade == 0:
            self.velocidade += 1
        elif self.velocidade == 1:
            self.velocidade = 0
            

    def acelerar(self):
        if self.velocidade > 0:
            self.velocidade += 10
            print("Velocidade atual: ", self.velocidade)
        else:
            print("Carro está desligado!")

    def frear(self):
        if self.velocidade > 0:
            if self.velocidade - 10 < 0:
                velocidade_zero = abs(self.velocidade)
                self.velocidade - velocidade_zero
            else:
                self.velocidade -= 10

    def verificar_velocidade(self):
        print("A velocidade atual é: ", self.velocidade)
    
carro = Carro(5)

for i in range (0,2):
    carro.acelerar()

carro.frear()

carro.verificar_velocidade()