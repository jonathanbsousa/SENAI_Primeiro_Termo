tabuada = int(input("Digite o numero da tabuada que deseja saber: "))

for multplicador in range(1,11):
    resultado = tabuada * multplicador
    print(f"{tabuada} * {multplicador} = {resultado}")