package telas;

import java.awt.Color;
import java.awt.HeadlessException;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.security.PublicKey;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPasswordField;
import javax.swing.JTextField;

import arquivos.LerEscreverObjeto;
import classes.Usuario;

public class TelaLogin extends JFrame {
	private JLabel jlLogin, jlSenha;
	private JTextField jtfLogin;
	private JPasswordField jpfSenha;
	private JButton jbLogar, jbCadastrar;
	private Usuario[] usuarios = new Usuario[40];
	private int indice = 0;
	
	public TelaLogin(String title) throws HeadlessException {
		super(title);
		setSize(250, 250);//tamanho da tela
		setLayout(null);//desabilita diencionamento automatico
		getContentPane().setBackground(Color.BLUE);
		setLocationRelativeTo(this);//tela de login aparece no meio da tela
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);//fecha a janela e fecha o programa
		leituraArquivo();
		iniciarComponente();
		criarEventos();
	}
	private void leituraArquivo() {
		
		LerEscreverObjeto leitura = new LerEscreverObjeto("Usuario.bin");
		if (leitura.lerObjeto() != null) {
			usuarios = leitura.lerObjeto();
		}
		
	}
	private void iniciarComponente() {
		jlLogin = new JLabel("Login:");
		jtfLogin = new JTextField();
		jlSenha = new JLabel("Senha: ");
		jpfSenha = new JPasswordField();
		jbLogar = new JButton("login");
		jbCadastrar = new JButton("Cadasatro");
		
		
		add(jlLogin);
		add(jtfLogin);
		add(jlSenha);
		add(jpfSenha);
		add(jbLogar);
		add(jbCadastrar);
		
		
		jlLogin.setBounds(10, 10, 80, 20);
		jtfLogin.setBounds(10, 30, 200, 20);
		jlSenha.setBounds(10, 60, 80, 20);
		jpfSenha.setBounds(10, 80, 200, 20);
		jbLogar.setBounds(10, 150, 100, 20);
		jbCadastrar.setBounds(110, 150, 100, 20);
		
		
		
	}
	private void criarEventos() {
		jbCadastrar.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				TelaCadastro cadastro = new TelaCadastro("Cadastro", usuarios, indice);
				cadastro.setVisible(true);
				++indice;
			}
		});
		jbLogar.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				
				if (usuarios[0] != null) {
					for (int i = 0; i < usuarios.length; i++) {
							if (usuarios[i] != null) {
								if (usuarios[i].login.equals(jtfLogin.getText())
										&& usuarios[i].senha.equals(String.valueOf(jpfSenha.getPassword()))) {
									TelaDoador doador = new TelaDoador("Doação de sangue");
									doador.setVisible(true);
									setVisible(false);
									break;
							}
							
						}
					}
				} else {
					JOptionPane.showInternalMessageDialog(null, "nenhum cadastro foi feito", "Erro", JOptionPane.ERROR_MESSAGE);
				}
			}
		});
		
	}
	public static void main(String[] args) {
		TelaLogin login = new TelaLogin("Login");
		login.setVisible(true);
	}

}
