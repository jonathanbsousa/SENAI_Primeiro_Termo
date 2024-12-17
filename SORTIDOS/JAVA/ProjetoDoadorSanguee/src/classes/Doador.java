package classes;

public class Doador {


		// TODO Auto-generated method stub
		public String nome;
		public String genero;
		public int idade;
		public float peso;
		
		public Doador(String nome, String genero, int idade, float peso) {
			super();
			this.nome = nome;
			this.genero = genero;
			this.idade = idade;
			this.peso = peso;
		}
		
		public String mostrarQuantidadeSangue() {
			if (this.idade >= 18) {
				if (this.genero.equalsIgnoreCase("Masculino")) {
					return "Nome: " + this.nome + "\nIdade: " + this.idade + "\npeso :" + this.peso + "\nGenero: " + this.genero + "\nDoar 700 gramas\n";
				} else {
					return "Nome: " + this.nome + "\nIdade: " + this.idade + "\npeso :" + this.peso + "\nGenero: " + this.genero +"\nDoar 400 gramas\n";
				}
			}else {
				return "Para doasr sangue é necessário ter 18 anos ou mais!\n" ;
			}
		}
		
		
		
	}


