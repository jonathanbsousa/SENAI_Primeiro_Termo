peso = float(input("Insira seu peso: "))
altura = float(input("Insira sua altura: "))

IMC = peso / (altura * altura)

print(f"Seu IMC é: {IMC:.2f}")

if IMC < 18.8:
    print("Baixo peso")
elif IMC < 24.9:
    print("Normal")
elif IMC < 29.9:
    print("Sobrepeso")
elif IMC < 34.9:
    print("Obesidade")
elif IMC < 39.9:
    print("Obesidade grau 2")
else:
    print("Obesidade grau 3")