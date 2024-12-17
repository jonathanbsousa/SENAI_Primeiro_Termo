# Definindo a classe cachorro
class Cachorro:
    def __init__(self, nome, idade):# Inicializamos os atributos da classe
        self.nome = nome
        self.idade = idade

    def latir(self):# Método - cachorro latir
        return "Au Au!"
    
    def idade_humana(self):# Método - idade do cachorro em anos humanas
        return self.idade * 7

# Criando um objeto da clase cachorro
meu_cachorro = Cachorro("Rex", 3)

# Acessando os atributos e métodos do objeto
meu_cachorro.latir()
print(f"O nome do meu cachorro é {meu_cachorro.nome}, ele tem {meu_cachorro.idade} anos e {meu_cachorro.idade_humana()} anos humanos. Ele faz {meu_cachorro.latir()}")