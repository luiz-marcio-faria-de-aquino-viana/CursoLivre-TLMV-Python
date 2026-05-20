"""
Copyright (c) 2025-2026 TLMV Consultoria e Sistemas EIRELI.

ex03_operacoes_com_cadeia_de_caracteres.py
Autor: 
Luiz Marcio Faria de Aquino Viana, Pos-D.Sc. - Engenheiro, 28/04/2026
Unidade: Universidade do Estado do Rio de Janeiro
Curso: Engenharia Eletrica, Enfase em Engenharia de Sistemas e Computacao
Unico Socio e Administrador da Empresa - Desde: 02/08/2000

Revisoes: ...
"""

# OPERACAO: TIPO_CARACTER / TIPO_CADEIA_CARACTER (STRING)
def teste1_variavelTipoCadeiaCaracter():
	# NOTA: CADEIA DE CARACTERES PODEM SER DELIMITADAS POR (') OU (")
	nomeJoao = "Joao Xavier da Silveira";		# TIPO_CADEIA_CARACTER (STRING)
	nomeMaria = 'Maria da Silva Caetano';		# TIPO_CADEIA_CARACTER (STRING)

	conceitoExcelente = "'A'";			# TIPO_CARACTER (BYTE 0-127) - conceito 'EXCELENTE' para alunos de escolas publicas
	conceitoMuitoBom = "'B'";			# TIPO_CARACTER (BYTE 0-127) - conceito 'MUITO_BOM' para alunos de escolas publicas
	conceitoBom = "'C'";				# TIPO_CARACTER (BYTE 0-127) - conceito 'BOM' para alunos de escolas publicas
	conceitoInsuficiente = "'D'";		# TIPO_CARACTER (BYTE 0-127) - conceito 'INSUFICIENTE' para alunos de escolas publicas
	conceitoPessimo = "'E'";			# TIPO_CARACTER (BYTE 0-127) - conceito 'PESSIMO' para alunos de escolas publicas

	notas = [];							# TIPO_VETOR (LISTA)
	notas.append( [ nomeJoao, conceitoExcelente, conceitoBom, conceitoMuitoBom ] );
	notas.append( [ nomeMaria, conceitoBom, conceitoInsuficiente, conceitoMuitoBom ] );

	print('RESULTADO:');
	print('==========');
	for o in notas:
		print( o );
	print('');

# OPERACAO: CONCETENACAO DE CADEIA CARACTER
def teste2_variavelConcatenacao():
	nomeAluno = [];
	nomeAluno.append( "Joao" );
	nomeAluno.append( "Maria" );
	nomeAluno.append( "Carlos" );
	nomeAluno.append( "Marcos" );
	nomeAluno.append( "Andre" );
	nomeAluno.append( "Mariana" );
	nomeAluno.append( "Fernanda" );

	sobrenomeAluno = [];
	sobrenomeAluno.append( "Xavier da Silveira" );
	sobrenomeAluno.append( "da Silva Caetano" );
	sobrenomeAluno.append( "Antunes Moreira Fernandes" );
	sobrenomeAluno.append( "Araujo Figueira" );
	sobrenomeAluno.append( "Ramos da Cruz" );
	sobrenomeAluno.append( "Albuquerque Vidal" );
	sobrenomeAluno.append( "da Silva Sauro" );

	print('RESULTADO:');
	print('==========');
	for i in range(0, 7):
		nomeCompleto = nomeAluno[i] + " " + sobrenomeAluno[i];
		print('NOME:', nomeAluno[i], ' - SOBRENOME:', sobrenomeAluno[i], ' - NOME_COMPLETO:', nomeCompleto);
	print('');

# OPERACAO: CONVERSAO LETRAS MAIUSCULAS E MINUSCULAS
def teste3_conversaoLetrasMaiusculasMinusculas():
	nomeAluno = [];
	nomeAluno.append( "Joao" );
	nomeAluno.append( "Maria" );
	nomeAluno.append( "Carlos" );
	nomeAluno.append( "Marcos" );
	nomeAluno.append( "Andre" );
	nomeAluno.append( "Mariana" );
	nomeAluno.append( "Fernanda" );

	sobrenomeAluno = [];
	sobrenomeAluno.append( "Xavier da Silveira" );
	sobrenomeAluno.append( "da Silva Caetano" );
	sobrenomeAluno.append( "Antunes Moreira Fernandes" );
	sobrenomeAluno.append( "Araujo Figueira" );
	sobrenomeAluno.append( "Ramos da Cruz" );
	sobrenomeAluno.append( "Albuquerque Vidal" );
	sobrenomeAluno.append( "da Silva Sauro" );

	print('RESULTADO:');
	print('==========');
	for i in range(0, 7):
		nomeCompleto = nomeAluno[i] + " " + sobrenomeAluno[i];

		#LETRAS_MINUSCULAS
		nomeMinuscula = nomeAluno[i].lower();
		sobrenomeMinuscula = sobrenomeAluno[i].lower();
		nomeCompletoMinuscula = nomeCompleto.lower();
		print('NOME:', nomeMinuscula, ' - SOBRENOME:', sobrenomeMinuscula, ' - NOME_COMPLETO:', nomeCompletoMinuscula);

		#LETRAS_MAIUSCULAS
		nomeMaiuscula = nomeAluno[i].upper();
		sobrenomeMaiuscula = sobrenomeAluno[i].upper();
		nomeCompletoMaiuscula = nomeCompleto.upper();
		print('NOME:', nomeMaiuscula, ' - SOBRENOME:', sobrenomeMaiuscula, ' - NOME_COMPLETO:', nomeCompletoMaiuscula);
	print('');

# OPERACAO: PESQUISA TEXTO
def teste4_pesquisaTexto():
	textoPesquisa = "silva";

	nomeAluno = [];
	nomeAluno.append( "Joao" );
	nomeAluno.append( "Maria" );
	nomeAluno.append( "Carlos" );
	nomeAluno.append( "Marcos" );
	nomeAluno.append( "Andre" );
	nomeAluno.append( "Mariana" );
	nomeAluno.append( "Fernanda" );

	sobrenomeAluno = [];
	sobrenomeAluno.append( "Xavier da Silveira" );
	sobrenomeAluno.append( "da Silva Caetano" );
	sobrenomeAluno.append( "Antunes Moreira Fernandes" );
	sobrenomeAluno.append( "Araujo Figueira" );
	sobrenomeAluno.append( "Ramos da Cruz" );
	sobrenomeAluno.append( "Albuquerque Vidal" );
	sobrenomeAluno.append( "da Silva Sauro" );

	print('RESULTADO:');
	print('==========');

	textoPesquisaMaiuscula = textoPesquisa.upper();
	for i in range(0, 7):
		nomeCompleto = nomeAluno[i] + " " + sobrenomeAluno[i];

		#LETRAS_MAIUSCULAS
		nomeCompletoMaiuscula = nomeCompleto.upper();
		pos = nomeCompletoMaiuscula.find(textoPesquisaMaiuscula);
		if pos != -1:			# alunos que possuem 'SILVA' no nome
			print('NOME_COMPLETO:', nomeCompletoMaiuscula);
	print('');

# OPERACAO: SOLETRANDO OS NOMES DOS ALUNOS
def teste5_soletrandoNomesAlunos():
	nomeAluno = [];
	nomeAluno.append( "Joao" );
	nomeAluno.append( "Maria" );
	nomeAluno.append( "Carlos" );
	nomeAluno.append( "Marcos" );
	nomeAluno.append( "Andre" );
	nomeAluno.append( "Mariana" );
	nomeAluno.append( "Fernanda" );

	sobrenomeAluno = [];
	sobrenomeAluno.append( "Xavier da Silveira" );
	sobrenomeAluno.append( "da Silva Caetano" );
	sobrenomeAluno.append( "Antunes Moreira Fernandes" );
	sobrenomeAluno.append( "Araujo Figueira" );
	sobrenomeAluno.append( "Ramos da Cruz" );
	sobrenomeAluno.append( "Albuquerque Vidal" );
	sobrenomeAluno.append( "da Silva Sauro" );

	print('RESULTADO:');
	print('==========');

	for i in range(0, 7):
		nomeCompleto = nomeAluno[i] + " " + sobrenomeAluno[i];
		sz = len(nomeCompleto);

		soletrando = [];
		for j in range(0, sz):
			letra = nomeCompleto[j];
			soletrando.append( letra );

		print("NOME:", nomeCompleto, " - SOLETRANDO:", soletrando);

	print('');

def recursos():
	print('RECURSOS:');
	print('=========');
	print('teste1_variavelTipoCadeiaCaracter()');
	print('teste2_variavelConcatenacao()');
	print('teste3_conversaoLetrasMaiusculasMinusculas()');
	print('teste4_pesquisaTexto()');
	print('teste5_soletrandoNomesAlunos()');
	print('');

def executaTudo():
	print('EXECUTA:');
	print('========');
	print('');

	print('Executa: teste1_variavelTipoCadeiaCaracter()');
	teste1_variavelTipoCadeiaCaracter();
	print('');

	print('Executa: teste2_variavelConcatenacao()');
	teste2_variavelConcatenacao();
	print('');

	print('teste3_conversaoLetrasMaiusculasMinusculas()');
	teste3_conversaoLetrasMaiusculasMinusculas();
	print('');

	print('teste4_pesquisaTexto()');
	teste4_pesquisaTexto();
	print('');

	print('teste5_soletrandoNomesAlunos()');
	teste5_soletrandoNomesAlunos();
	print('');

def carregado():
	print('Arquivo: ex03_operacoes_com_cadeia_de_caracteres.py... carregado!');
	print('');

