let usuario_verificado = "Allison"
let senha_verificado = "123"

console.log("js ok")



function Login() {  
    let usuario = document.getElementById("login").value
    let senha = document.getElementById("senha").value

     if (usuario == usuario_verificado && senha == senha_verificado ) {
        window.location.href = "http://127.0.0.1:5500/loja.html";
     }
     else {
        alert("O login esta incorreto")
    }
}