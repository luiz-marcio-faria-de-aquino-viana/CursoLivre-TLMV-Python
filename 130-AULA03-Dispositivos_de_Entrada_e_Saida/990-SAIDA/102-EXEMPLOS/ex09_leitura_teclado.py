"""
Copyright (c) 2025-2026 TLMV Consultoria e Sistemas EIRELI.

ex09_leitura_teclado.py
Autor: 
Luiz Marcio Faria de Aquino Viana, Pos-D.Sc. - Engenheiro, 28/04/2026
Unidade: Universidade do Estado do Rio de Janeiro
Curso: Engenharia Eletrica, Enfase em Engenharia de Sistemas e Computacao
Unico Socio e Administrador da Empresa - Desde: 02/08/2000

Revisoes: ...
"""

import datetime as dt;
import math as m;
import random as r;
import statistics as s;

# CONSTANTES #

DEF_LF = "'\n'"; 		# line feed (nova-linha)
DEF_CR = "'\r'";		# carriege return (retorno de carro)

DEF_CARACTERVALIDO_TEXTO = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,!@#$%&*()[]{^}~/\\+=-_\'\"¨;:><?|";
DEF_CARACTERVALIDO_NUMERO = "+-0123456789.,";
DEF_CARACTERVALIDO_DATA = "0123456789/";

# UTILITARIOS #

# funcSubstr(): funcao que retorna uma parte do texto de entrada
# entrada - texto de entrada
# posI - posicao inicial na cadeia
# posF - posicao final na cadeia
def funcSubstr(entrada, posI, posF):
	texto = "";

	sz = len(entrada);

	if posI < 0:
		posI = 0;

	if posF <= posI or posF > sz:
		posF = sz;

	for i in range(posI, posF):
		ch = entrada[i];
		texto = texto + ch;
	return texto;

# funcOpcoesStr(): funcao que retorna a lista de opcoes como texto concatenado
# arrOpcao[] - lista de opcoes [ "Texto1", "Opcao1", "Texto2", "Opcao2" ... ]
# opcaoPadrao - destaca a opcao padrao
def funcOpcaoToStr(arrOpcao, opcaoPadrao):
	texto = "";

	sz = len(arrOpcao);
	for i in range(0, sz, 2):
		opcao = arrOpcao[i];

		if opcaoPadrao != None:
			if opcao == opcaoPadrao:
				opcao = "<" + opcao + ">";

		if i > 0:
			texto = texto + ", ";
		texto = texto + opcao;
	return texto;

# funcSelecionaOpcao(): funcao que retorna a opcao selecionada
# texto - texto com a opcao de entrada
# arrOpcao[] - lista de opcoes [ "Texto1", "Opcao1", "Texto2", "Opcao2" ... ]
def funcSelecionaOpcao(texto, arrOpcao):
	opcao = None;

	textoPesquisa = texto.upper();
	print("TextoPesquisa: ", textoPesquisa);

	sz = len(arrOpcao);
	for i in range(0, sz, 2):
		textoOriginal = arrOpcao[i];
		opcaoOriginal = arrOpcao[i + 1];

		texto1 = textoOriginal.upper();
		opcao1 = opcaoOriginal.upper();

		if textoPesquisa == texto1 or textoPesquisa == opcao1:
			opcao = textoOriginal;
			break;
	return opcao;

# funcFiltraEntrada(): funcao que filtra o texto de entrada
# entrada - texto de entrada
# filtro - texto contendo caracteres validos
def funcFiltraEntrada(entrada, filtro):
	texto = "";

	sz = len(entrada);
	for i in range(sz):
		ch = entrada[i];
		
		if ch == DEF_LF:
			continue;
		
		if ch == DEF_CR:
			continue;
		
		if filtro == "":
			texto = texto + ch;
		else:
			pos = filtro.find(ch);
			if pos != -1:
				texto = texto + ch;
	return texto;

# funcParseData(): funcao de conversao de texto em data
# entrada - texto de entrada
def funcParseData(entrada):
	data = None;

	sz = len(entrada);
	if sz >= 10:
		dd = funcSubstr(entrada, 0, 2);
		mm = funcSubstr(entrada, 3, 5);
		yy = funcSubstr(entrada, 6, 10);
		
		try:
			valDD = m.floor( float(dd) );
			valMM = m.floor( float(mm) );
			valYY = m.floor( float(yy) );

			data = dt.date(valYY, valMM, valDD);
		except:
			print("ERR: Valor invalido.");

	return data;
			
# funcLeEntradaTeclado(): funcao que apresenta uma mensagem e espera a digitacao de um texto
# mensagem - mensagem a ser apresentada na tela
def funcLeEntradaTeclado(mensagem):
	print(mensagem);

	f = open("/dev/stdin", 'r');
	texto = f.readline(4096);
	f.close();
	return texto;

# funcLeEntradaTexto(): funcao que apresenta uma mensagem e espera a digitacao de um texto
# mensagem - mensagem a ser apresentada na tela
# bAceitaNulo - aceita valores nulos
def funcLeEntradaTexto(mensagem, bAceitaNulo):
	texto = "";
	while True:
		texto = funcLeEntradaTeclado(mensagem);
		texto = funcFiltraEntrada(texto, DEF_CARACTERVALIDO_TEXTO);
		if texto != "":
			break;
		else:
			if bAceitaNulo:
				print("Valor nulo.");
				return None;
			else:
				print("ERR: Valor nulo nao e valido.");

	print("Texto informado: ", texto);
	return texto;

# funcLeEntradaNumero(): funcao que apresenta uma mensagem e espera a digitacao de um valor numerico
# mensagem - mensagem a ser apresentada na tela
# bAceitaNulo - aceita valores nulos
def funcLeEntradaNumero(mensagem, bAceitaNulo):
	numero = 0.0;
	while True:
		texto = funcLeEntradaTeclado(mensagem);
		texto = funcFiltraEntrada(texto, DEF_CARACTERVALIDO_NUMERO);
		if texto == "":
			if bAceitaNulo:
				print("Valor nulo.");
				return None;
			else:
				print("ERR: Valor nulo nao e valido.");
				continue;

		try:
			numero = float(texto);
			break;
		except:
			print("ERR: Valor invalido.");

	print("Valor informado: ", numero);
	return numero;

# funcLeEntradaData(): funcao que apresenta uma mensagem e espera a digitacao de um valor data (formato: dd/mm/yyyy)
# mensagem - mensagem a ser apresentada na tela
# bAceitaNulo - aceita valores nulos
def funcLeEntradaData(mensagem, bAceitaNulo):
	data = None;
	while True:
		texto = funcLeEntradaTeclado(mensagem);
		texto = funcFiltraEntrada(texto, DEF_CARACTERVALIDO_DATA);
		if texto == "":
			if bAceitaNulo:
				print("Valor nulo.");
				return None;
			else:
				print("ERR: Valor nulo nao e valido.");
				continue;

		data = funcParseData(texto);
		if data != None:
			break;
		else:
			print("ERR: Valor invalido.");

	print("Data informada: ", data);
	return data;

# funcLeEntradaOpcoes(): funcao que apresenta uma mensagem e espera a digitacao de uma opcao
# mensagem - mensagem a ser apresentada na tela
# arrOpcao[] - lista de opcoes [ "Texto1", "Opcao1", "Texto2", "Opcao2" ... ]
# bAceitaNulo - aceita valores nulos
def funcLeEntradaOpcao(mensagem, arrOpcao, opcaoPadrao, bAceitaNulo):
	opcao = None;

	while True:
		textoOpcao = funcOpcaoToStr(arrOpcao, opcaoPadrao);

		texto = funcLeEntradaTeclado(mensagem + " " + textoOpcao + ": ");
		texto = funcFiltraEntrada(texto, DEF_CARACTERVALIDO_TEXTO);
		if texto == "":
			if opcaoPadrao != None:
				texto = opcaoPadrao;

		if texto == "":
			if bAceitaNulo:
				print("Valor nulo.");
				return None;
			else:
				print("ERR: Valor nulo nao e valido.");
				continue;

		opcao = funcSelecionaOpcao(texto, arrOpcao);
		if opcao != None:
			break;
		else:
			print("ERR: Opcao invalida.");

	print("Opcao selecionada: ", opcao);
	return opcao;

def recursos():
	print('RECURSOS:');
	print('=========');
	print('funcSubstr()');
	print('funcOpcaoToStr()');
	print('funcSelecionaOpcao()');
	print('funcFiltraEntrada()');
	print('funcParseData()');
	print('funcLeEntradaTeclado()');
	print('funcLeEntradaTexto()');
	print('funcLeEntradaNumero()');
	print('funcLeEntradaData()');
	print('funcLeEntradaOpcao()');
	print('');

def executaTudo():
	print('EXECUTA:');
	print('========');
	print('');

	nomeCompleto = funcLeEntradaTexto("Qual o seu nome? ", False);
	print("Nome completo: ", nomeCompleto);

	idade = funcLeEntradaNumero("Quantos anos você tem? ", False);
	print("Idade: ", idade);

	dataNasc = funcLeEntradaData("Qual a sua data de nascimento? ", False);
	print("Data nascimento: ", dataNasc);

	arrOpcao = [ "(1)Azul", "1", "(2)Vermelho", "2", "(3)Verde", "3", "(4)Amarelo", "4", "(5)Preto", "5", "(6)Branco", "6" ]
	opcao = funcLeEntradaOpcao("Qual a sua cor preferida? ", arrOpcao, "(6)Branco", False);
	print("Cor preferida: ", opcao);
		
def carregado():
	print('Arquivo: ex09_leitura_teclado.py... carregado!');
	print('');
