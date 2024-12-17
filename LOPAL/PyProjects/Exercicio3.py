num1 = int(input("Entre com um numero: "))
num2 = int(input("Entre com um numero: "))

if num1 > num2:
    print(f"{num1} é maior")
elif num2 > num1:
    print(f"{num2} é maior")
else:
    print("Numeros são iguais")