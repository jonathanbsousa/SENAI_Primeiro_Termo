let imageIndex = 0;
const images = [
    "/img/1.png",
    "/img/Carrosel/foto2.avif",
    "/img/Carrosel/foto3.jpg",
    "/img/Carrosel/foto2.avif",
];

const carrossel = document.getElementById("carrossel");

function mudarimg() { 
    carrossel.src = images[0];
}
function mudarimg2() {
    carrossel.src = images[1] + 1 ;
}