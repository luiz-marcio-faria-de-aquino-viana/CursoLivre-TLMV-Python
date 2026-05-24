"""
Copyright (c) 2025-2026 TLMV Consultoria e Sistemas EIRELI.

ex08_escrita_tela.py
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

# procEscreveTela(): funcao que apresenta uma mensagem na tela
# mensagem - mensagem a ser apresentada na tela
def procEscreveTela(mensagem):
	print(mensagem);

# procEscreveLinha(): funcao que apresenta uma mensagens na mesma linha da tela
# mensagem - mensagem a ser apresentada na tela
def procEscreveLinha(mensagem):
	print(mensagem, sep=' ', end='');


# procExemploFormatacao(): funcao que apresenta uma mensagens formatada na tela
def procExemploFormatacao():
	# EXEMPLO_001
	largura = 10;
	for numero in range(0, 32): 
		for formato in 'dXob':
   			print('{0:{width}{base}}'.format(numero, base=formato, width=largura), end=' ');
		print('');

def recursos():
	print('RECURSOS:');
	print('=========');
	print('procEscreveTela()');
	print('procEscreveLinha()');
	print('procExemploFormatacao()');
	print('');

def executaTudo():
	print('EXECUTA:');
	print('========');
	print('');

	# procEscreveTela(): funcao que apresenta uma mensagem na tela
	procEscreveTela("Hello, World!\n\r");	
		
	# procEscreveLinha(): funcao que apresenta uma mensagens na mesma linha da tela
	procEscreveLinha("Processando... ");
	for i in range(0, 100):
		procEscreveLinha(".");
	procEscreveTela("Concluido!\n\r");

	# procExemploFormatacao(): funcao que apresenta uma mensagens formatada na tela
	procExemploFormatacao();

def carregado():
	print('Arquivo: ex08_escrita_tela.py... carregado!');
	print('');
