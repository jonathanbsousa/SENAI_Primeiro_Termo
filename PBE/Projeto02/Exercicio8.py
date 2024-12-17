num = int(input("Digite o numero a ser calculado o fatorial: "))
fatorial = 1
cont = num

while cont > 1:
    fatorial *= cont
    cont -= 1
print(f"O resultado do calculo é {fatorial}")