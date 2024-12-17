import csv
import json
import xml.etree.ElementTree as ET
import pandas as pd
from openpyxl.workbook import Workbook

# TXT -----------------------------------------------------------

with open("meu_arquivo.txt", "w") as arquivo:
    arquivo.write("Olá mundo!\n")
    arquivo.write("Aprendendo Pyhton\n")

with open("meu_arquivo.txt", "r") as arquivo:
    print(arquivo.read())

# CSV -----------------------------------------------------------

# Exemplo 1
with open("meu_arquivo.csv", "w", newline= '') as csvfile:
    escrever = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    escrever.writerow("Nome,Preço")
    escrever.writerow("Livro,20")

with open('meu_arquivo.csv', newline='') as csvfile:
    ler = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in ler:
        print("".join(row))

# Exemplo 2
with open("produtos.csv", "w", newline='') as f:
    escrever = csv.writer(f)
    escrever.writerow(["Nome", "Preço"])
    escrever.writerow(["Livro", 20])

with open("produtos.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# JSON -----------------------------------------------------------

# Exemplo 1
dados = {
    "Nome": "João",
    "Idade": "30",
    "Cidade": "São Paulo",
}

arquivo = open("dados.json", "w")
json.dump(dados, arquivo)
arquivo.close()

arquivo = open("dados.json", "r")
dados = json.load(arquivo)
arquivo.close()

print(dados)

#Exemplo 2

with open("dados2.json", "w") as f:
    json.dump({"Nomes": "João", "Idade": 25}, f)

with open("dados2.json", "r") as f:
    data = json.load(f)
    print(data)

# XML -----------------------------------------------------------

config = ET.Element("Config")
versao = ET.SubElement(config, "versao")
versao.text = "1.0"

tree = ET.ElementTree(config)
tree.write("Config.xml", encoding="utf-8", xml_declaration=True)

tree = ET.parse('config.xml')
root = tree.getroot()

versao = root.find('versao').text
print(f"Versão: {versao}")

# xlsx -----------------------------------------------------------

dados = {"Produto": ["Celular"],
         "Preço": [10],}

vendas = pd.DataFrame(dados)
vendas.to_excel("Vendas.xlsx", index=False)

vendas1 = pd.read_excel("Vendas.xlsx")
print(vendas)