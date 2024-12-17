// let nome = window.prompt("Escreva seu nome: ")
// alert("este é o seu nome: " + nome)

// let num1 = Number.parseInt(window.prompt("Escreva um número: "))
// let num2 = Number.parseInt(window.prompt("Escreva outro número: "))
// let soma = num1 + num2
// alert(soma)

// console.log("Olá")

                    // // CALCULADORA:
// let numero1 = Number.parseFloat(window.prompt("Escreva um número :"))
// let numero2 = Number.parseFloat(window.prompt("Escreva um segundo número :"))
// let soma = numero1 + numero2

// let opcao = window.prompt("Escolha sua opção: 1. Divisão, 2. Multiplicação, 3.Subtração, 4.Divisão")

// if (opcao == "+") {
//   resultado = numero1 + numero2
//   alert(resultado) 
// } else if (opcao == "*") {
//     resultado = numero1 * numero2
//   alert(resultado)
    
// } else if (opcao == "-") {
//     resultado = numero1 - numero2
//   alert(resultado)
    
// } else if (opcao == "/") {
//     resultado = numero1 / numero2
//   alert(resultado)
    
// }else alert("Opção inválida")

function Login(){
    var usuario = document.getElementById("caixa_nome").value;
    var senha = document.getElementById("caixa_senha").value;

    if (usuario == "Jonathan Brasil" && senha == "123"){
        alert("Sua semha está correta");
    } else {
        alert("Sua senha está errada");
    }

}