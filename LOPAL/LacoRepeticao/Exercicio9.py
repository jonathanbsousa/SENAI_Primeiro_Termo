# tamanho = int(input("Digite o tamanho da lista de números: "))
#
# soma = 0
# lista = []
#
# for numeros in range(tamanho):
#    numero = float(input(f"Digite o número {numeros + 1}: "))
#    lista.append(numero)
#    soma += lista[numeros]
#
# media = soma / tamanho if tamanho > 0 else 0
#
# print("A média dos números é:", media)

tamanho = int(input("Digite o tamanho da lista: "))

cont = 0
soma = 0
lista = []

while cont < tamanho:
    numero = float(input(f"Digite o número {cont + 1}: "))
    lista.append(numero)
    soma += numero
    cont += 1

media = soma / tamanho if tamanho > 0 else 0

print("A média dos números é:", media)
