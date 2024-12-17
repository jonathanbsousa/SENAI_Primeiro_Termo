target_sequence = [112, 114, 111]

found_letters = []

for num in target_sequence:
    found_letters.append(chr(num))

print("".join(found_letters))

def calcular_valor(numeros):
    return max(numeros)