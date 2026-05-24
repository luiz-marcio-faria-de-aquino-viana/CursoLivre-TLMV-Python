"""
Copyright (c) 2025-2026 TLMV Consultoria e Sistemas EIRELI.

ex05_controleCondicional_FOR_WHILE.py
Autor: 
Luiz Marcio Faria de Aquino Viana, Pos-D.Sc. - Engenheiro, 28/04/2026
Unidade: Universidade do Estado do Rio de Janeiro
Curso: Engenharia Eletrica, Enfase em Engenharia de Sistemas e Computacao
Unico Socio e Administrador da Empresa - Desde: 02/08/2000

Revisoes: ...
"""

# CONTROLE_CONDICIONAL: FOR1
def teste1_controleCondicional_FOR1():
	arrDiaSemana = [ 'Segunda-feira', 'Terca-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sabado', 'Domingo' ];

	for diaSemana in arrDiaSemana:
		print("Dia da Semana:", diaSemana);
	print("");

# CONTROLE_CONDICIONAL: FOR2
def teste2_controleCondicional_FOR2():
	arrDiaSemana = [ 'Segunda-feira', 'Terca-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sabado', 'Domingo' ];

	for i in range(0, 7):
		strDiaSemana = arrDiaSemana[i];
		print("Dia da Semana:", strDiaSemana);
	print("");

# CONTROLE_CONDICIONAL: FOR3
def teste3_controleCondicional_FOR3():
	arrDiaSemana = [ 'Segunda-feira', 'Terca-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sabado', 'Domingo' ];

	for i in range(0, 7, 2):
		strDiaSemana = arrDiaSemana[i];
		print("Dia da Semana:", strDiaSemana);
	print("");

# CONTROLE_CONDICIONAL: FOR4
def teste6_controleCondicional_FOR4():
	arrDiaSemana = [ 'Segunda-feira', 'Terca-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sabado', 'Domingo' ];

	for i in range(7):
		strDiaSemana = arrDiaSemana[i];
		print("Dia da Semana:", strDiaSemana);
	print("");

# CONTROLE_CONDICIONAL: WHILE1
def teste4_controleCondicional_WHILE1():
	arrDiaSemana = [ 'Segunda-feira', 'Terca-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sabado', 'Domingo' ];

	valDiaSemana = 0;
	while valDiaSemana <= 6:
		strDiaSemana = arrDiaSemana[valDiaSemana];
		print("Dia da Semana:", strDiaSemana);

		valDiaSemana = valDiaSemana + 2;
	print("");

# CONTROLE_CONDICIONAL: WHILE2
def teste5_controleCondicional_WHILE2():
	arrDiaSemana = [ 'Segunda-feira', 'Terca-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sabado', 'Domingo' ];

	valDiaSemana = 0;
	while valDiaSemana <= 6:
		strDiaSemana = arrDiaSemana[valDiaSemana];

		if valDiaSemana == 5 or valDiaSemana == 6:
			print("Dia da Semana:", strDiaSemana, "*** DIA DE DESCANCO ***");
		else:
			print("Dia da Semana:", strDiaSemana);

		valDiaSemana = valDiaSemana + 2;
	print("");

def recursos():
	print('RECURSOS:');
	print('=========');
	print('teste1_controleCondicional_FOR1()');
	print('teste2_controleCondicional_FOR2()');
	print('teste3_controleCondicional_FOR3()');
	print('teste4_controleCondicional_WHILE1()');
	print('teste5_controleCondicional_WHILE2()');
	print('teste6_controleCondicional_FOR4()');
	print('');

def executaTudo():
	print('EXECUTA:');
	print('========');
	print('');

	print('Executa: teste1_controleCondicional_FOR1()');
	teste1_controleCondicional_FOR1();
	print('');

	print('Executa: teste2_controleCondicional_FOR2()');
	teste2_controleCondicional_FOR2();
	print('');

	print('Executa: teste3_controleCondicional_FOR3()');
	teste3_controleCondicional_FOR3();
	print('');

	print('Executa: teste4_controleCondicional_WHILE1()');
	teste4_controleCondicional_WHILE1();
	print('');

	print('Executa: teste5_controleCondicional_WHILE2()');
	teste5_controleCondicional_WHILE2();
	print('');

	print('Executa: teste6_controleCondicional_FOR4()');
	teste6_controleCondicional_FOR4();
	print('');

def carregado():
	print('Arquivo: ex05_controleCondicional_FOR_WHILE.py... carregado!');
	print('');

