tamanho = int(input("Quantos numero deseja somar?: \n"))
cont = 0
soma = 0

for i in range(tamanho):
    num = int(input(f"Digite o numero {cont + 1}: \n"))
    soma += num
    cont += 1
print(f"A soma dos numeros é {soma}!")