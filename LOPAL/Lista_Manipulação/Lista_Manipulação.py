import csv
import json
import xml.etree.ElementTree as ET

# TXT ----------------------------------------------------------

with open("aula.txt", "w") as arquivo:
    arquivo.write("Python é legal!\n")
    arquivo.write("Aprendendo manipulação de arquivos")

with open("aula.txt", "r") as arquivo:
    print(arquivo.read())

# CSV ----------------------------------------------------------

with open("alunos.csv", "w", newline = '') as csvfile:
    escrever = csv.writer(csvfile, delimiter = ' ', quotechar = '', quoting=csv.QUOTE_MINIMAL)
    escrever.writerow("João, 20")
    escrever.writerow("Maria, 22")

with open("alunos.csv", newline = ' ') as csvfile:
    ler = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in ler:
        print("".join(row))

# JSON ----------------------------------------------------------

with open("info.json", "w") as f:
    json.dump({"Especie": ["Cachorro", "Gato"],
               "Nome": ["Rex", "Felix"]})
    
with open("info.json", "r") as f:
    data = json.load(f)
    print(data)

# XML ----------------------------------------------------------

config = ET.Element("")

# XLSX ----------------------------------------------------------