# def mensagem_boas_vindas():
#     print("Bem-vindo ao curso de programação!")
# mensagem_boas_vindas()

# def soma(a,b):
#     resultado = a + b
#     print(f"O resultado da soma é {resultado}")
#     return resultado
#
# valor = soma(5, 2)
# print(f"Valor retornado {valor}")

def calclar_media(nota1 , nota2):
    media = (nota1 + nota2)/2
    return media

nota1 = float(input("Digite um numero: "))
nota2 = float(input("Digite outro numero: "))

resultado = calclar_media(nota1, nota2)

print(f"A média entre as notas {nota1} e {nota2} é {resultado:.2f}")