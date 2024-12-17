package arquivos;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInput;
import java.io.ObjectInputStream;
import java.io.ObjectOutput;
import java.io.ObjectOutputStream;

import javax.swing.JOptionPane;

import classes.Usuario;

public class LerEscreverObjeto {
	
	private String nomeArquivo;

	public LerEscreverObjeto(String nomearquivo) {
		this.nomeArquivo = nomearquivo;
		
	}
	public void escreverObjeto(Usuario[] usuarios) {
		try {
			FileOutputStream fluxo = new FileOutputStream(nomeArquivo);//passo o nome do arquivo
			ObjectOutputStream objeto = new ObjectOutputStream(fluxo);
			objeto.writeObject(usuarios);
			objeto.close();
			JOptionPane.showMessageDialog(null, "Gravado com sucesso!");
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
	public Usuario[] lerObjeto() {
		Usuario[] usuario = null;//Variavel vai receber o objeto do arquivo, de classe Crianca
		FileInputStream fluxo;
		try {
			fluxo = new FileInputStream(nomeArquivo);//Ler arquivo
			ObjectInputStream objeto = new ObjectInputStream(fluxo);
			usuario = (Usuario[]) objeto.readObject();//devolve em object(A classe mãe de todas as outra
			objeto.close();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (ClassNotFoundException e) {//pode-se adicionar vaios catchs para um try
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
		
		return usuario;
	}
}
