escolha = int(input("1 - Celcius\Fahrenheit 2 - Fahrenheit\Celsius \n"))
grau = int(input("Entre com a temperatura a ser convertida: "))

if escolha == 1:
    resultado = (9/5 * grau) + 32
elif escolha == 2:
    resultado = (grau - 32) * 5/9
else:
    print("Escolha uma opção valida!")

print(f"O resultado da conversão é {resultado}")