package telas;


import java.awt.Color;
import java.awt.HeadlessException;
import java.awt.Image;
import java.awt.Scrollbar;
import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.net.URI;
import java.net.URL;

import javax.swing.ButtonGroup;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JRadioButton;
import javax.swing.JScrollBar;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

import classes.Doador;

public class TelaDoador extends JFrame {
	private JLabel jlnome, jlpeso, jlidade, jlgenero, jlimagem;
	private JTextField jtfnome, jtfpeso, jtfidade; //usado para pequenos textos
	private JButton jbcadastrar, jbmostrar;
	private JTextArea jtaMostrar; //usado para grandes textos
	private JScrollPane jspMostrar;
	private Doador[] doadores = new Doador[40];
	private ButtonGroup bggenero;
	private JRadioButton jrbmasculino, jrbfeminino;
	private ImageIcon imagem;
	private int indice = 0;
	
	public TelaDoador(String title) throws HeadlessException {
		super(title);
		setSize(240, 600);//tamanho da tela
		setLayout(null);//desabilita diencionamento automatico
		getContentPane().setBackground(Color.ORANGE);
		
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);//fecha a janela e fecha o programa
		iniciarComponente();
		criarEventos();
	}
	
	private void iniciarComponente() {
		URL url = this.getClass().getResource("/imagens/doacaozinho.png");
		Image iconeTitulo = Toolkit.getDefaultToolkit().getImage(url);
		this.setIconImage(iconeTitulo);
		
		
		imagem = new ImageIcon(getClass().getResource("/imagens/doacaooo.png"));
	
		jlimagem = new JLabel(imagem); //JLabel suportando uma imagem
		jlnome = new JLabel("Nome");
		jtfnome = new JTextField();
		jlpeso = new JLabel("Peso");
		jtfpeso = new JTextField();
		jlidade = new JLabel("Idade");
		jtfidade = new JTextField();
		jbcadastrar = new JButton("Cadastrar");
		jbmostrar = new JButton("Mostrar");
		bggenero = new ButtonGroup();
		jlgenero = new JLabel("Gênero");
		jrbfeminino = new JRadioButton("Feminino", true);
		jrbmasculino = new JRadioButton("Masculino");
		jrbmasculino.setOpaque(false);
		jrbfeminino.setOpaque(false);
		jtaMostrar = new JTextArea();
		jspMostrar = new JScrollPane(jtaMostrar);
		
		
		add(jlnome);
		add(jtfnome);
		add(jlpeso);
		add(jtfpeso);
		add(jlidade);
		add(jtfidade);
		add(jbcadastrar);
		add(jbmostrar);
		add(jrbfeminino);
		add(jrbmasculino);
		bggenero.add(jrbfeminino);
		bggenero.add(jrbmasculino);
		add(jlgenero);
		add(jspMostrar);
		add(jlimagem);
		
		jlnome.setBounds(10,130,50,20);
		jtfnome.setBounds(10,150,200,20);
		jlpeso.setBounds(10, 170, 50, 20);
		jtfpeso.setBounds(10, 190, 50, 20);
		jlidade.setBounds(160, 170, 50, 20);
		jtfidade.setBounds(160, 190, 50, 20);
		jbcadastrar.setBounds(110, 240, 100, 20);
		jbmostrar.setBounds(110, 260, 100, 20);
		jlgenero.setBounds(10,220,100,20);
		jrbmasculino.setBounds(10, 240, 100, 20);
		jrbfeminino.setBounds(10, 260, 100, 20);
		jspMostrar.setBounds(10, 290, 200, 250);
		jlimagem.setBounds(48, 10, 128, 128);
		
		
		
		
	}
	
	private void criarEventos() {
		jbcadastrar.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				String nome, genero;
				int idade;
				float peso;
				
				if (!jtfnome.getText().isEmpty()
						&& !jtfpeso.getText().isEmpty()
						&& !jtfidade.getText().isEmpty()) {
					
					nome = jtfnome.getText();
					idade =Integer.parseInt(jtfidade.getText());
					peso = Float.parseFloat(jtfpeso.getText());
					if (jrbmasculino.isSelected()) {
						genero = "Masculino";
						
					} else {
						genero = "Feminino";
					}
					
					doadores[indice] = new Doador(nome, genero, idade, peso);

					indice++;
					jtfidade.setText("");
					jtfnome.setText("");
					jtfpeso.setText("");
					
					
				} else {
					JOptionPane.showInternalMessageDialog(null, "Falta de dados", "Erro de cadastro", JOptionPane.ERROR_MESSAGE);
				}
				
				
				
			}
		});
		
		jbmostrar.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub                                                               
				if (doadores[0] != null) {
					jtaMostrar.setText("              Doação de sangue\n ");
					for (int i = 0; i < indice; i++) {
						jtaMostrar.append(doadores[i].mostrarQuantidadeSangue()+"\n");
					}
					
					
				} else {
					JOptionPane.showMessageDialog(null, "Nenhuma cadastro encontrado", "Erro no sístema", JOptionPane.ERROR_MESSAGE);
				}
					
			}
		});
		
	}

}
