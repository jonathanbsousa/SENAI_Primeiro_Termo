idade = int(input("Insira a idade: "))

if idade < 2 :
    print("Bebê")
elif idade < 13:
    print("Criança")
elif idade < 18:
    print("Adolescente")
elif idade <60:
    print("Adulto")
else:
    print("Idoso")