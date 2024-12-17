lado1 = float(input("Digite o comprimento de um lado: "))
lado2 = float(input("Digite o comprimento de outro lado: "))
lado3 = float(input("Digite o comprimento de mais um lado: "))
#
# if lado1 > lado2 and lado1 > lado3:
#     if (lado2 + lado3) > lado1:
#         if lado1 == lado2 and lado2 == lado3:
#             print("O triangulo é equilátero")
#         elif lado1 == lado2 or lado2 == lado3:
#             print("O triangulo é isósceles")
#         else:
#             print("O triango é escaleno")
# elif lado2 > lado1 and lado2 > lado3:
#     if (lado1 + lado3) > lado2:
#         if lado1 == lado2 and lado2 == lado3:
#             print("O triangulo é equilátero")
#         elif lado1 == lado2 or lado2 == lado3:
#             print("O triangulo é isósceles")
#         else:
#             print("O triango é escaleno")
# elif lado3 > lado2 and lado3 > lado1:
#     if (lado2 + lado1) > lado3:
#         if lado1 == lado2 and lado2 == lado3:
#             print("O triangulo é equilátero")
#         elif lado1 == lado2 or lado2 == lado3:
#             print("O triangulo é isósceles")
#         else:
#             print("O triango é escaleno")
# else:
#     print("Não é um triangulo!")

if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado3 + lado1 > lado2:
    if lado1 == lado2 and lado2 == lado3:
        print("Equilatero")
    elif lado1 != lado2 and lado2 != lado3:
        print("Escaleno")
    else:
        print("Isósceles")
else:
    print("Não é um triangulo")