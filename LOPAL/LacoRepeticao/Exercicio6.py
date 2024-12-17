numero = int(input("Digite um numero (5-0): "))

if numero >= 5:
    while numero > 0:
        print(numero)
        numero -= 1
else:
    print("Numero invalido")