frase = input("Digite uma frase: ")

letras_contadas = {}

for letra in frase:
    if letra.isalpha():
        letra = letra.lower()
        if letra in letras_contadas:
            letras_contadas[letra] += 1
        else:
            letras_contadas[letra] = 1

for letra, contagem in letras_contadas.items():
    print(f"A letra '{letra}' aparece {contagem} vez(es).")
