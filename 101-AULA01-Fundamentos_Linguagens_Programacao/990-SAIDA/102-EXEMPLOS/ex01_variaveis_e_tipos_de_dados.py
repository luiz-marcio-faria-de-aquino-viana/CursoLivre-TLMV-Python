"""
Copyright (c) 2025-2026 TLMV Consultoria e Sistemas EIRELI.

ex01_variaveis_e_tipos_de_dados.py
Autor: 
Luiz Marcio Faria de Aquino Viana, Pos-D.Sc. - Engenheiro, 28/04/2026
Unidade: Universidade do Estado do Rio de Janeiro
Curso: Engenharia Eletrica, Enfase em Engenharia de Sistemas e Computacao
Unico Socio e Administrador da Empresa - Desde: 02/08/2000

Revisoes: ...
"""

import statistics as s;
import datetime as dt;

# VARIAVEL: TIPO_INTEIRO
def teste1_variavelTipoInteiro():
	idadeJoao = 10;				# variavel armazena a idade de joao
	idadePai = 37;				# variavel armazena a idade do pai de joao

	diferencaIdade = idadePai - idadeJoao;	# variavel armazena a diferenca entre as idades do pai de joao e joao
	print(diferencaIdade);			# funcao que imprime a diferenca de idades

# VARIAVEL: TIPO_REAL
def teste2_variavelTipoReal():
	valorAzulejo = 22.50;			# valor do azulejo por metro quadrado de area
	
	larguraAmbiente = 3.50;			# largura do ambiente em metros
	comprimentoAmbiente = 8.50;		# comprimento do ambiente em metros
	
	areaAmbiente = larguraAmbiente * comprimentoAmbiente;		# area do ambiente em metro quadrado
	
	valorTotal = valorAzulejo * areaAmbiente;			# valor total de recobrimento do ambiente
	print(valorTotal);

# VARIAVEL: TIPO_CADEIA_CARACTER
def teste3_variavelTipoCadeiaCaracter():
	nomeJoao = "Joao Xavier da Silveira";
	nomeMaria = "Maria da Silva Caetano";
	nomeCarlos = "Carlos Antunes Moreira Fernandes";
	nomeMarcos = "Marcos Araujo Figueira";
	nomeAndre = "Andre Ramos da Cruz";
	nomeMariana = "Mariana Albuquerque Vidal";
	nomeFernanda = "Fernanda da Silva Sauro";

	print("ALUNOS:");
	print(nomeJoao);
	print(nomeMaria);
	print(nomeCarlos);
	print(nomeMarcos);
	print(nomeAndre);
	print(nomeMariana);
	print(nomeFernanda);

# VARIAVEL: TIPO_CARACTER
def teste4_variavelTipoCaracter():
	conceitoExcelente = 'A';		# conceito 'EXCELENTE' para alunos de escolas publicas
	conceitoMuitoBom = 'B';			# conceito 'MUITO_BOM' para alunos de escolas publicas
	conceitoBom = 'C';			# conceito 'BOM' para alunos de escolas publicas
	conceitoInsuficiente = 'D';		# conceito 'INSUFICIENTE' para alunos de escolas publicas
	conceitoPessimo = 'E';			# conceito 'PESSIMO' para alunos de escolas publicas

	nomeJoao = "Joao Xavier da Silveira";
	nomeMaria = "Maria da Silva Caetano";
	nomeCarlos = "Carlos Antunes Moreira Fernandes";
	nomeMarcos = "Marcos Araujo Figueira";
	nomeAndre = "Andre Ramos da Cruz";
	nomeMariana = "Mariana Albuquerque Vidal";
	nomeFernanda = "Fernanda da Silva Sauro";

	notaJoao = conceitoExcelente;
	notaMaria = conceitoBom;
	notaCarlos = conceitoMuitoBom;
	notaMarcos = conceitoPessimo;
	notaAndre = conceitoPessimo;
	notaMariana = conceitoExcelente;
	notaFernanda = conceitoExcelente;
	
	print("NOTAS:");
	print(nomeJoao + ": " + notaJoao);
	print(nomeMaria + ": " + notaMaria);
	print(nomeCarlos + ": " + notaCarlos);
	print(nomeMarcos + ": " + notaMarcos);
	print(nomeAndre + ": " + notaAndre);
	print(nomeMariana + ": " + notaMariana);
	print(nomeFernanda + ": " + notaFernanda);

# VARIAVEL: TIPO_VETOR (LISTAS)
def teste5_variavelTipoVetor():
	conceitoExcelente = 'A';		# conceito 'EXCELENTE' para alunos de escolas publicas
	conceitoMuitoBom = 'B';			# conceito 'MUITO_BOM' para alunos de escolas publicas
	conceitoBom = 'C';			# conceito 'BOM' para alunos de escolas publicas
	conceitoInsuficiente = 'D';		# conceito 'INSUFICIENTE' para alunos de escolas publicas
	conceitoPessimo = 'E';			# conceito 'PESSIMO' para alunos de escolas publicas

	alunos = [ 
		"Joao Xavier da Silveira",
		"Maria da Silva Caetano",
		"Carlos Antunes Moreira Fernandes",
		"Marcos Araujo Figueira",
		"Andre Ramos da Cruz",
		"Mariana Albuquerque Vidal",
		"Fernanda da Silva Sauro" ];

	notas = [ 
		conceitoExcelente,
		conceitoBom,
		conceitoMuitoBom,
		conceitoPessimo,
		conceitoPessimo,
		conceitoExcelente,
		conceitoExcelente ];
	
	print("NOTAS:");
	print(alunos[0] + ": " + notas[0]);
	print(alunos[1] + ": " + notas[1]);
	print(alunos[2] + ": " + notas[2]);
	print(alunos[3] + ": " + notas[3]);
	print(alunos[4] + ": " + notas[4]);
	print(alunos[5] + ": " + notas[5]);
	print(alunos[6] + ": " + notas[6]);

# VARIAVEL: TIPO_MATRIZ (LISTAS)
def teste6_variavelTipoMatriz():
	# PECAS BRANCAS
	brR = 'R';
	brD = 'D';
	brT = 'T';
	brB = 'B';
	brC = 'C';
	brP = 'P';

	# PECAS NEGRAS
	ngR = 'r';
	ngD = 'd';
	ngT = 't';
	ngB = 'b';
	ngC = 'c';
	ngP = 'p';

	tabuleiro = [ [ ' ', '1', '2', '3', '4', '5', '6', '7', '8' ],
	              [ 'H', ngT, ngC, ngB, ngD, ngR, ngB, ngC, ngT ], 
	              [ 'G', ngP, ngP, ngP, ngP, ngP, ngP, ngP, ngP ], 
	              [ 'F', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ], 
	              [ 'E', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ], 
	              [ 'D', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ], 
	              [ 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ], 
	              [ 'B', brP, brP, brP, brP, brP, brP, brP, brP ], 
	              [ 'A', brT, brC, brB, brD, brR, brB, brC, brT ] ]; 

	print("BOB FISHER x JOAOZINHO: INICIO DE JOGO");
	print(tabuleiro[0]);
	print(tabuleiro[1]);
	print(tabuleiro[2]);
	print(tabuleiro[3]);
	print(tabuleiro[4]);
	print(tabuleiro[5]);
	print(tabuleiro[6]);
	print(tabuleiro[7]);
	print(tabuleiro[8]);

	# MOVIMENTO 1: P4R P4R
	# BOB FISHER
	tabuleiro[7][5] = ' ';
	tabuleiro[5][5] = brP;
	# JOAOZINHO
	tabuleiro[2][5] = ' ';
	tabuleiro[4][5] = ngP;

	print("BOB FISHER x JOAOZINHO: JOGADA 1");
	print(tabuleiro[0]);
	print(tabuleiro[1]);
	print(tabuleiro[2]);
	print(tabuleiro[3]);
	print(tabuleiro[4]);
	print(tabuleiro[5]);
	print(tabuleiro[6]);
	print(tabuleiro[7]);
	print(tabuleiro[8]);

	# MOVIMENTO 2: C3BR C3BD
	# BOB FISHER
	tabuleiro[8][7] = ' ';
	tabuleiro[6][6] = brC;
	# JOAOZINHO
	tabuleiro[1][2] = ' ';
	tabuleiro[3][3] = ngC;

	print("BOB FISHER x JOAOZINHO: JOGADA 2");
	print(tabuleiro[0]);
	print(tabuleiro[1]);
	print(tabuleiro[2]);
	print(tabuleiro[3]);
	print(tabuleiro[4]);
	print(tabuleiro[5]);
	print(tabuleiro[6]);
	print(tabuleiro[7]);
	print(tabuleiro[8]);

# VARIAVEL: TIPO_VETOR (LISTAS)
def teste7_variavelTipoTabela():
	nomeAluno = [];
	nomeAluno.append( "Joao Xavier da Silveira" );
	nomeAluno.append( "Maria da Silva Caetano" );
	nomeAluno.append( "Carlos Antunes Moreira Fernandes" );
	nomeAluno.append( "Marcos Araujo Figueira" );
	nomeAluno.append( "Andre Ramos da Cruz" );
	nomeAluno.append( "Mariana Albuquerque Vidal" );
	nomeAluno.append( "Fernanda da Silva Sauro" );

	notaAluno = [];
	notaAluno.append( [ 10.0, 8.0, 6.0 ] );
	notaAluno.append( [ 10.0, 7.0, 5.0 ] );
	notaAluno.append( [  8.0, 6.0, 4.0 ] );
	notaAluno.append( [  8.0, 7.0, 7.0 ] );
	notaAluno.append( [  6.0, 6.0, 8.0 ] );
	notaAluno.append( [  6.0, 8.0, 5.0 ] );
	notaAluno.append( [  4.0, 9.0, 4.0 ] );

	mediaAluno = [];
	mediaAluno.append( s.mean( notaAluno[0] ) );
	mediaAluno.append( s.mean( notaAluno[1] ) );
	mediaAluno.append( s.mean( notaAluno[2] ) );
	mediaAluno.append( s.mean( notaAluno[3] ) );
	mediaAluno.append( s.mean( notaAluno[4] ) );
	mediaAluno.append( s.mean( notaAluno[5] ) );
	mediaAluno.append( s.mean( notaAluno[6] ) );

	print('MEDIA:')
	print('======')
	print('Nome:', nomeAluno[0], 'Notas:', notaAluno[0], 'Media:', mediaAluno[0] );
	print('Nome:', nomeAluno[1], 'Notas:', notaAluno[1], 'Media:', mediaAluno[1] );
	print('Nome:', nomeAluno[2], 'Notas:', notaAluno[2], 'Media:', mediaAluno[2] );
	print('Nome:', nomeAluno[3], 'Notas:', notaAluno[3], 'Media:', mediaAluno[3] );
	print('Nome:', nomeAluno[4], 'Notas:', notaAluno[4], 'Media:', mediaAluno[4] );
	print('Nome:', nomeAluno[5], 'Notas:', notaAluno[5], 'Media:', mediaAluno[5] );
	print('Nome:', nomeAluno[6], 'Notas:', notaAluno[6], 'Media:', mediaAluno[6] );


# VARIAVEL: TIPO_DATAHORA
def teste8_variavelTipoData():
	arrDiaSemana = [ 'Segunda-feira', 'Terca-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sabado', 'Domingo' ];

	objDateTime = dt.datetime;
	dataHoraAtual = objDateTime.now();

	dd = dataHoraAtual.day;
	mm = dataHoraAtual.month;
	yy = dataHoraAtual.year;

	objDate = dt.date;
	dataAtual = objDate.today();

	diaSemanaAtual = objDate.weekday( dataAtual );
	strDiaSemanaAtual = arrDiaSemana[ diaSemanaAtual ];

	print('Data e Hora Atual:', dataHoraAtual);
	print('Data Atual:', dataAtual);
	print('Dia Semana Atual:', strDiaSemanaAtual);

def recursos():
	print('RECURSOS:');
	print('=========');
	print('teste1_variavelTipoInteiro()');
	print('teste2_variavelTipoReal()');
	print('teste3_variavelTipoCadeiaCaracter()');
	print('teste4_variavelTipoCaracter()');
	print('teste5_variavelTipoVetor()');
	print('teste6_variavelTipoMatriz()');
	print('teste7_variavelTipoTabela()');
	print('teste8_variavelTipoData()');
	print('');

def executaTudo():
	print('EXECUTA:');
	print('========');
	print('');

	print('Executa: teste1_variavelTipoInteiro()');
	teste1_variavelTipoInteiro();
	print('');

#	print('Executa: teste2_variavelTipoReal()');
#	teste2_variavelTipoReal();
#	print('');

#	print('Executa: teste3_variavelTipoCadeiaCaracter()');
#	teste3_variavelTipoCadeiaCaracter();
#	print('');

#	print('Executa: teste4_variavelTipoCaracter()');
#	teste4_variavelTipoCaracter();
#	print('');

#	print('Executa: teste5_variavelTipoVetor()');
#	teste5_variavelTipoVetor();
#	print('');

#	print('Executa: teste6_variavelTipoMatriz()');
#	teste6_variavelTipoMatriz();
#	print('');

#	print('Execute: teste7_variavelTipoTabela()');
#	teste7_variavelTipoTabela();
#	print('');

#	print('teste8_variavelTipoData()');
#	teste8_variavelTipoData();
#	print('');

def carregado():
	print('Arquivo: ex01_variaveis_e_tipos_de_dados.py... carregado!');
	print('');

