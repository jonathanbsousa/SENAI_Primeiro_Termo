import random

numero_secreto = random.randint(1, 10)

print("Bem-vindo ao jogo de adivinhação!")
print("Adivinhe um número entre 1 e 10.")

tentativas = 0
limite_tentativas = 3

while tentativas < limite_tentativas:
    palpite = int(input("Digite seu palpite: "))

    if palpite < 1 or palpite > 10:
        print("Por favor, digite um número entre 1 e 10.")
    elif palpite < numero_secreto:
        print("Muito baixo! Tente novamente.")
    elif palpite > numero_secreto:
        print("Muito alto! Tente novamente.")
    else:
        print("Parabéns! Você acertou!")
        break

    tentativas += 1
    if tentativas < limite_tentativas:
        print(f"Você ainda tem {limite_tentativas - tentativas} tentativa(s) restante(s).")
    else:
        print(f"Você esgotou suas tentativas! O número secreto era {numero_secreto}.")