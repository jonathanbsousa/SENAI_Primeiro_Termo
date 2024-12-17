def menu():
    print("Qual exercicio você gostaria de fazer? "
          "\n 1 - Triangulo \n 2 - Carro \n 3 - Animal \n 4 - VAluno"
          "5 - Transação Bancaria \n 6 - GerenciadorFinanceiro")

    escolha = int(input("Digite a opção escolhida: "))

    match escolha:
        case (1):
            # Atividade 1

            class Triangulo:
                def __init__(self):
                    self.base = float(input("Digite a base do triângulo: "))
                    self.altura = float(input("Digite a altura do triângulo: "))

                def area(self):
                    return (self.base * self.altura) / 2

            triangulo = Triangulo()
            print(f"A área do triângulo é: {triangulo.area()}")

        case (2):

            # Atividade 2

            class Carro:
                def __init__(self):
                    self.modelo = input("Digite o modelo do carro: ")
                    self.ano = int(input("Digite o ano do carro: "))
                    self.quilometragem = float(input("Digite a quilometragem do carro: "))

                def detalhes(self):
                    print(f"Modelo: {self.modelo}")
                    print(f"Ano: {self.ano}")
                    print(f"Quilometragem: {self.quilometragem} km")

            carro = Carro()
            carro.detalhes()

        case (3):

            # Atividade 3

            class Animal:
                def __init__(self):
                    self.especie = input("Digite a espécie do animal: ")
                    self.som = input(f"Digite o som que o {self.especie} faz: ")

                def emitir_som(self):
                    print(f"O {self.especie} faz o som: {self.som}")

            animal = Animal()
            animal.emitir_som()

        case (4):
            
            # Atividade 4

            class Aluno:
                def __init__(self):
                    self.nome = input("Digite o nome do aluno: ")
                    self.notas = list(map(float, input("Digite as notas do aluno separadas por espaço: ").split()))

                def media(self):
                    return sum(self.notas) / len(self.notas)

            # Teste
            aluno = Aluno()
            print(f"A média das notas do aluno {aluno.nome} é: {aluno.media()}")

        case (5):

            # Atividade 5

            class TransacaoBancaria:
                def __init__(self):
                    self.saldo = float(input("Digite o saldo inicial: "))
                    self.historico_transacoes = []

                def depositar(self, valor):
                    self.saldo += valor
                    self.historico_transacoes.append(f"Depósito: R${valor:.2f}")

                def sacar(self, valor):
                    if valor <= self.saldo:
                        self.saldo -= valor
                        self.historico_transacoes.append(f"Saque: R${valor:.2f}")
                    else:
                        print("Saldo insuficiente para o saque.")

                def extrato(self):
                    print("Histórico de Transações:")
                    for transacao in self.historico_transacoes:
                        print(transacao)
                    print(f"Saldo atual: R${self.saldo:.2f}")

            conta = TransacaoBancaria()
            conta.depositar(float(input("Digite o valor a ser depositado: ")))
            conta.sacar(float(input("Digite o valor a ser sacado: ")))
            conta.extrato()

        case (6):
            # Desafio 1
            class GerenciadorFinanceiro:
                class Conta:
                    def __init__(self, tipo_conta):
                        self.saldo = 0.0
                        self.historico_transacoes = []
                        self.tipo_conta = tipo_conta

                    def depositar(self, valor):
                        self.saldo += valor
                        self.historico_transacoes.append(f"Depósito: R${valor:.2f}")

                    def sacar(self, valor):
                        if valor <= self.saldo:
                            self.saldo -= valor
                            self.historico_transacoes.append(f"Saque: R${valor:.2f}")
                        else:
                            print("Saldo insuficiente.")

                    def transferir(self, valor, conta_destino):
                        if valor <= self.saldo:
                            self.saldo -= valor
                            conta_destino.saldo += valor
                            self.historico_transacoes.append(f"Transferência para outra conta: R${valor:.2f}")
                            conta_destino.historico_transacoes.append(f"Transferência recebida: R${valor:.2f}")
                        else:
                            print("Saldo insuficiente para transferência.")

                    def consultar_extrato(self):
                        print("Histórico de Transações:")
                        for transacao in self.historico_transacoes:
                            print(transacao)
                        print(f"Saldo atual: R${self.saldo:.2f}")

                    def calcular_juros(self):
                        if self.tipo_conta == 'Poupança':
                            juros = self.saldo * 0.05  # 5% de juros
                            self.saldo += juros
                            self.historico_transacoes.append(f"Juros adicionados: R${juros:.2f}")
                        else:
                            print("Conta não é poupança, juros não aplicados.")

                def __init__(self):
                    self.contas = {}

                def criar_conta(self, id_conta, tipo_conta):
                    nova_conta = self.Conta(tipo_conta)
                    self.contas[id_conta] = nova_conta

                def depositar(self, id_conta, valor):
                    if id_conta in self.contas:
                        self.contas[id_conta].depositar(valor)
                    else:
                        print("Conta não encontrada.")

                def sacar(self, id_conta, valor):
                    if id_conta in self.contas:
                        self.contas[id_conta].sacar(valor)
                    else:
                        print("Conta não encontrada.")

                def transferir(self, id_origem, id_destino, valor):
                    if id_origem in self.contas and id_destino in self.contas:
                        self.contas[id_origem].transferir(valor, self.contas[id_destino])
                    else:
                        print("Uma das contas não foi encontrada.")

                def consultar_extrato(self, id_conta):
                    if id_conta in self.contas:
                        self.contas[id_conta].consultar_extrato()
                    else:
                        print("Conta não encontrada.")

                def calcular_juros(self, id_conta):
                    if id_conta in self.contas:
                        self.contas[id_conta].calcular_juros()
                    else:
                        print("Conta não encontrada.")

            # Teste
            gerenciador = GerenciadorFinanceiro()
            gerenciador.criar_conta(1, 'Corrente')
            gerenciador.criar_conta(2, 'Poupança')
            gerenciador.depositar(1, 1000)
            gerenciador.depositar(2, 500)
            gerenciador.transferir(1, 2, 200)
            gerenciador.calcular_juros(2)
            gerenciador.consultar_extrato(1)
            gerenciador.consultar_extrato(2)

menu()