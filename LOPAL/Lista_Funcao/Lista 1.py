def menu():
    print("Qual exercicio você gostaria de fazer? "
          "\n 1 - IMC \n 2 - Maior \n 3 - Par ou Impar \n 4 - Vogal"
          "5 - Contagem Regresiva \n 6 - Conta Letras \n 7 - Ordenar Lista"
          "\n 8 - Contagem Regressiva Recusristas")

    escolha = int(input("Digite a opção escolhida: "))

    match escolha:
        case (1):
            # Atividade 1
            def imc():
                peso = float(input("Digite seu peso: "))
                altura = float(input("Digite sua altura: "))

                return f"Seu IMC é {peso / altura * altura}"

            print(imc())

        case (2):
            # Atividade 2
            def maior_n(numeros):
                maior = numeros[0]  # Assume que o primeiro número é o maior
                for numero in numeros:
                    if numero > maior:
                        maior = numero
                return maior

            lista_numeros = input("Digite números inteiros separados por espaço: ").split()
            lista_numeros = [int(num) for num in lista_numeros]
            maior = maior_n(lista_numeros)
            print("O maior número é:", maior)

        case (3):
            # Atividade 3
            def par_ou_impar(numero):
                if numero % 2 == 0:
                    return "Par"
                else:
                    return "Ímpar"

            num = int(input("Digite um número inteiro: "))
            resultado = par_ou_impar(num)
            print("O número é:", resultado)

        case (4):
            # Atividade 4
            lista = []
            separado = []

            def conta_vogal():
                palavra = input("Digite uma plavra qualquer: ").lower()
                lista.append(palavra)

                for i in lista:
                    if i == "a":
                        separado.append(i)
                    elif i == "e":
                        separado.append(i)
                    elif i == "i":
                        separado.append(i)
                    elif i == "o":
                        separado.append(i)
                    elif i == "u":
                        separado.append(i)

            conta_vogal()

        case (5):

            # Atividade 5
            def contagem_regressiva():
                n = int(input("Digite um número: "))
                if n < 0:
                    return
                print(n)
                if n > 0:
                    contagem_regressiva(n - 1)
                else:
                    print("Fim")

            contagem_regressiva()

        case (6):
            # Desafio 1
            def conta_letras():
                palavra = input("Digite uma palavra: ")
                contagem = {}
                for letra in palavra:
                    if letra in contagem:
                        contagem[letra] += 1
                    else:
                        contagem[letra] = 1
                print(contagem)

            conta_letras()

        case (7):
            # Desafio 2
            def ordena_lista():
                lista = input("Digite uma lista de números: ")
                lista = list(map(int, lista.split()))

                lista_ordenada = []
                while lista:
                    menor = lista[0]
                    for numero in lista:
                        if numero < menor:
                            menor = numero
                    lista_ordenada.append(menor)
                    lista.remove(menor)

                print("Lista ordenada:", lista_ordenada)

            ordena_lista()

        case (8):
            # Atividade 3
            def contagem_regressiva_recursiva():
                n = int(input("Digite um número inteiro para a contagem regressiva: "))

                def contagem(n):
                    if n <= 0:
                        print("Fim")
                    else:
                        print(n)
                        contagem(n - 1)

                contagem(n)

            contagem_regressiva_recursiva()

menu()