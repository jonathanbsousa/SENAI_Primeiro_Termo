import random

opcoes = ["pedra" , "papel", "tesoura"]
op_jogador = input("Digite pedra, papel ou tesoura: ").lower()
op_computador = random.choice(["pedra", "papel", "tesoura"])

if op_jogador not in opcoes:
    print("Opção invalida")
else:
    print(f"O computador escolheu {op_computador}")
    if op_jogador == op_computador:
        print("Empate!")
    elif (op_jogador == "pedra" and op_computador == "tesoura") or\
        (op_jogador == "papel" and op_computador == "pedra") or\
        (op_jogador == "tesoura" and op_computador == "papel") :
        print("Você ganhou!")
    else:
        print("Você perdeu!")
