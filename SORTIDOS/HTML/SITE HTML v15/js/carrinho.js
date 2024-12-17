preco = Number.parseInt(document.getElementById("price1"))
quantidade = Number.parseInt(document.getElementById("qty"))
total = Number.parseInt(document.getElementById("preco-final"))
botao = document.getElementById("aumentar")


Vezes = preco * quantidade

document.getElementById("price-final").innerHTML = Vezes;

function Somar() {

    total = quantidade + 1
    
}