"""
Copyright (c) 2025-2026 TLMV Consultoria e Sistemas EIRELI.

ex05_controleCondicional_BREAK_CONTINUE.py
Autor: 
Luiz Marcio Faria de Aquino Viana, Pos-D.Sc. - Engenheiro, 28/04/2026
Unidade: Universidade do Estado do Rio de Janeiro
Curso: Engenharia Eletrica, Enfase em Engenharia de Sistemas e Computacao
Unico Socio e Administrador da Empresa - Desde: 02/08/2000

Revisoes: ...
"""

# CONTROLE_CONDICIONAL: CONTINUE1
def teste1_controleCondicional_CONTINUE1():
	arrDiaSemana = [ 'Segunda-feira', 'Terca-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sabado', 'Domingo' ];

	for diaSemana in arrDiaSemana:
		if diaSemana == 'Segunda-feira' or diaSemana == 'Terca-feira':
			continue; 

		print("Dia da Semana:", diaSemana);
	print("");

# CONTROLE_CONDICIONAL: BREAK1
def teste2_controleCondicional_BREAK1():
	arrDiaSemana = [ 'Segunda-feira', 'Terca-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sabado', 'Domingo' ];

	for i in range(0, 6):
		if i == 5:
			break;

		strDiaSemana = arrDiaSemana[i];
		print("Dia da Semana:", strDiaSemana);
	print("");

# CONTROLE_CONDICIONAL: CONTINUE2
def teste3_controleCondicional_CONTINUE2():
	arrDiaSemana = [ 'Segunda-feira', 'Terca-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sabado', 'Domingo' ];

	valDiaSemana = 0;
	while valDiaSemana <= 6:
		if valDiaSemana < 2 or valDiaSemana > 4:
			valDiaSemana = valDiaSemana + 1;
			continue; 

		strDiaSemana = arrDiaSemana[valDiaSemana];
		print("Dia da Semana:", strDiaSemana);

		valDiaSemana = valDiaSemana + 1;
	print("");

# CONTROLE_CONDICIONAL: BREAK2
def teste4_controleCondicional_BREAK2():
	arrDiaSemana = [ 'Segunda-feira', 'Terca-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sabado', 'Domingo' ];

	valDiaSemana = 0;
	while valDiaSemana <= 6:
		if valDiaSemana == 5:
			break;

		strDiaSemana = arrDiaSemana[valDiaSemana];
		print("Dia da Semana:", strDiaSemana);

		valDiaSemana = valDiaSemana + 1;
	print("");

def recursos():
	print('RECURSOS:');
	print('=========');
	print('teste1_controleCondicional_CONTINUE1()');
	print('teste2_controleCondicional_BREAK1()');
	print('teste3_controleCondicional_CONTINUE2()');
	print('teste4_controleCondicional_BREAK2()');
	print('');

def executaTudo():
	print('EXECUTA:');
	print('========');
	print('');

	print('Executa: teste1_controleCondicional_CONTINUE1()');
	teste1_controleCondicional_CONTINUE1();
	print('');

	print('Executa: teste2_controleCondicional_BREAK1()');
	teste2_controleCondicional_BREAK1();
	print('');

	print('Executa: teste3_controleCondicional_CONTINUE2()');
	teste3_controleCondicional_CONTINUE2();
	print('');

	print('Executa: teste4_controleCondicional_BREAK2()');
	teste4_controleCondicional_BREAK2();
	print('');

def carregado():
	print('Arquivo: ex06_controleCondicional_BREAK_CONTINUE.py... carregado!');
	print('');

