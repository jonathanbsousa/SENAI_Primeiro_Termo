idade = int(input("Insira sua idade: "))
renda = float(input("Insira sua renda mensal: "))

if idade >= 18 and renda >= 1500:
    print("Você é elegivel para o emprestimo")
elif idade >= 18 and renda <= 1500:
    print("Você não é elegivel para o emprestimo")
elif idade < 18 and renda >= 1000:
    print("Você é elegivel para o emprestimo")
elif idade < 18 and renda < 1000:
    print("Você não é elegivel para o emprestimo")