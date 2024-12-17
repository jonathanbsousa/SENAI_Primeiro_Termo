# frutas = ["Maças", "Bananas", "Laranjas"]
#
# for fruta in frutas:
#
#     print(fruta)
#
# mensagem = "Hello World"
#
# for caractere in mensagem:
#     print(caractere)
#
# cores = ["Vemelho", "Verde", "Azul", "Amarelo"]
#
# for cor in cores:
#     print("Cor:", cor)
#
# pessoa = {
#     "Nome": "Jonathan",
#     "Idade": "18",
#     "Profissão": "Jovem Aprendiz Soluções Digitais"
# }
#
# for chave, valor in pessoa.items():
#     print(f"{chave}: {valor}")
#
# animais = {"gato", "cachorro", "elefante", "girafa"}
#
# for animal in animais:
#     print("Animal:",animal)
#
# for numero in range(5):
#     print(numero)

nome_arquivo = "T:/1 DS-TB A - 12/LOP/LOPAL-Aula6-EstRepetição-Arquivo.txt"
with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())