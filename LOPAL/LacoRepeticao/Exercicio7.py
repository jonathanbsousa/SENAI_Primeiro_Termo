cont = 0
maior = 0

while cont < 5:
    numero = float(input(f"Entre com o numero {cont + 1}: "))

    if numero > maior:
        maior = numero

    cont += 1

print(f"O maior numero entre todos é {maior}")