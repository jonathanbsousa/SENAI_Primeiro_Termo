print("Gostaria de converter qual temperatura? \n 1 - Celsius/Fahrenheit \n 2 - Fahrenheit/Celsius \n 3 - Sair")
opcao = int(input("Digite a opção desejada: "))
temp = float(input("Digite a temperatura a ser convertida: "))

match opcao:
    case(1):
        fahrenheit = temp * 9/5 + 32
        print(f"A temperatura convertida é {fahrenheit}")
    case(2):
        celcius = (temp - 32) * 5/9
        print(f"A temperatura convertida é {celcius}")
    case(_):
        print("Até a próxima!")