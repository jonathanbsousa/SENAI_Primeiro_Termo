package telas;

import java.awt.Color;
import java.awt.HeadlessException;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPasswordField;
import javax.swing.JTextField;

import arquivos.LerEscreverObjeto;
import classes.Usuario;

public class TelaCadastro extends JFrame {
	private JLabel jlLogin, jlSenha;
	private JTextField jtfLogin;
	private JPasswordField jpfSenha;
	private JButton jbCadastrar;
	private Usuario[] usuarios;
	private int indice;

	public TelaCadastro(String title, Usuario[] usuarios, int indice) throws HeadlessException {
		super(title);
		this.usuarios = usuarios;
		this.indice = indice;
		setSize(250, 250);//tamanho da tela
		setLayout(null);//desabilita diencionamento automatico
		getContentPane().setBackground(Color.gray);
		setLocationRelativeTo(this);//tela de login aparece no meio da tela
		setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);//fecha a janela e fecha o programa
		iniciarComponente();
		criarEventos();
	}
	private void iniciarComponente() {
		jlLogin = new JLabel("Login:");
		jtfLogin = new JTextField();
		jlSenha = new JLabel("Senha: ");
		jpfSenha = new JPasswordField();
		jbCadastrar = new JButton("Cadasatro");
		
		
		add(jlLogin);
		add(jtfLogin);
		add(jlSenha);
		add(jpfSenha);
		add(jbCadastrar);
		
		
		jlLogin.setBounds(10, 10, 80, 20);
		jtfLogin.setBounds(10, 30, 200, 20);
		jlSenha.setBounds(10, 60, 80, 20);
		jpfSenha.setBounds(10, 80, 200, 20);
		jbCadastrar.setBounds(10, 150, 100, 20);
		
		
		
	}
	private void criarEventos() {
		jbCadastrar.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				String login = jtfLogin.getText();
				String senha = String.valueOf(jpfSenha.getPassword());//ValueOf converte um valor como char[] para String
				for (int i = 0; i < usuarios.length; i++) {
					if (usuarios[i] == null) {
						usuarios[indice] = new Usuario(login, senha);
						setVisible(false);
						LerEscreverObjeto gravar = new LerEscreverObjeto("Usuario.bin");
						gravar.escreverObjeto(usuarios);
						break;
					}
				}
				
				
			}
		});
	
		
	}

}
