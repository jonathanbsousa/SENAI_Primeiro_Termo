class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self.tinta = 100 # Tinta em porcentagem
    
    def escrever(self):
        if self.tinta > 0:
            print(f"Escrevendo com a caneta de cor {self.cor}")
            self.tinta -= 10 # gastar tinta
        else:
            print("Caneta sem tinta!")
    
    def recarregar(self):
        print("Recarregando a caneta")
        self.tinta = 100
    
    def verificar_tinta(self):
        return f"Tinta restante: {self.tinta}%"

# Usando a classe Caneta
minha_caneta = Caneta("azul")# Sáida: Escrever com a caneta azul

for i in range(0, 5):
    minha_caneta.escrever()

print(minha_caneta.verificar_tinta())# Sáida: Tinta restante 90%

minha_caneta.recarregar()