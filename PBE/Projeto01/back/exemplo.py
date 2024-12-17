import pandas as pd
import sqlite3

# class Carro:
#     def __init__(self, marca, modelo, ano):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano

#     def detalhes_carro(self):
#         return f'Esse carro é ano {self.ano}, modelo {self.modelo} e da marca {self.marca}'
    
#     def ligar(self):
#         return f'O carro {self.modelo} está ligado.'

# meu_carro = Carro('Toyota', 'Corolla', '2019')

# print(meu_carro.detalhes_carro())
# print(meu_carro.ligar())

# algo = Carro("VW", "UP", "2016")
# print(algo.detalhes_carro())
# print(algo.ligar())

class Programa:
    def __init__(self, db = 'db.sqlite3'):
        self.conn = sqlite3.connect(db)
        self.menu()

    def menu(self):
        while True:
            print("\n"
                "[1] - Create \n"
                "[2] - Read \n"
                "[3] - Update \n"
                "[4] - Delete \n"
                "[5] - Exit \n"
                "\n"
                )
            op = int(input("Escolha uma opção: "))
            match op:
                case 1:
                    self.menu_create()
                case 2:
                    print("Read")
                case 3:
                    print("Update")
                case 4:
                    print("Delete")
                case 5:
                    print("Você saiu!")
                    break
                case _:
                    print("Opção Invalida!")

    def create(self, tituloProduto, preco, descricao, imgProduto, catProduto, classProduto, exibirHome):
        cursor = self.conn.cursor()
        cursor.execute('''
                       INSERT INTO api_produto(tituloProduto, preco, descricao, imgProduto, catProduto, classProduto, exibirHome)
                       VALUES(?,?,?,?,?,?,?)
                       ''', (tituloProduto, preco, descricao, imgProduto, catProduto, classProduto, exibirHome))
        self.conn.commit()
        print("Produto cadastrado com sucesso!")
    
    def menu_create(self):
        print('\n'
              "1 - Titulo\n"
              "2 - Preco\n"
              "3 - Descrição\n"
              "4 - Imagem\n"
              "5 - Categoria\n"
              "6 - Classificação\n"
              "7 - Exibir(true/false)\n"          
              )
        
        tituloProduto = input("Tituo: ")
        preco = float(input("Preço: "))
        descricao = input("Descrição: ")
        imgProduto = input("Imagen: ")
        catProduto = input("Categoria: ")
        classProduto = input("Clasificação: ")
        exibirHome = input("Exibir: ")
        self.create(tituloProduto, preco, descricao, imgProduto, catProduto, classProduto, exibirHome)

programa = Programa()