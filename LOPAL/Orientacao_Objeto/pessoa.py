class Pessoa:
    def __init__(self):
        self.nome = ""
        self.idade = 0

    def apresentar(self):
        self.nome = input("Digite seu nome: ")
        self.idade = int(input("Digite a sua idade: "))
        print(f"Olá meu nome é {self.nome} e tenho {self.idade} anos de idade!")
    
pessoa = Pessoa()

pessoa.apresentar()