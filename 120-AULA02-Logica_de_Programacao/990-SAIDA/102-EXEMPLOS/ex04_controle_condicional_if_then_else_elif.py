"""
Copyright (c) 2025-2026 TLMV Consultoria e Sistemas EIRELI.

ex04_controle_condicional_if_then_else_elif.py
Autor: 
Luiz Marcio Faria de Aquino Viana, Pos-D.Sc. - Engenheiro, 28/04/2026
Unidade: Universidade do Estado do Rio de Janeiro
Curso: Engenharia Eletrica, Enfase em Engenharia de Sistemas e Computacao
Unico Socio e Administrador da Empresa - Desde: 02/08/2000

Revisoes: ...
"""

import math as m;
import random as rnd;
import datetime as dt;

# CONTROLE_CONDICIONAL: IF_THEN
def teste1_controleCondicional_IF_THEN():
	valores = [];
	for i in range(0, 100):
		rndNormal = rnd.normalvariate(0.0, 1.0);
		rndNormal = m.floor( rndNormal * 100.0 ) / 10.0;

		valores.append( rndNormal );

	minVal = 9999999.0;
	maxVal = -9999999.0;

	for val in valores:
		if(val < minVal): 
			minVal = val;

		if(val > maxVal): 
			maxVal = val;

	print("Valores:", valores);
	print("Valor Minimo:", minVal);
	print("Valor Maximo:", maxVal);

# CONTROLE_CONDICIONAL: IF_THEN_ELSE
def teste2_controleCondicional_IF_THEN_ELSE():
	arrDiasMes = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ];
	arrDiaSemana = [ 'Segunda-feira', 'Terca-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sabado', 'Domingo' ];

	objDate = dt.date;

	dataAtual = objDate.today();

	#dd = dataAtual.day;
	mm = dataAtual.month;
	yy = dataAtual.year;

	diasMes = arrDiasMes[mm];
	if mm == 1:					# Se Mes de Fevereiro => 28 ou 29 dias
		anoBisexto = yy % 4;
		if anoBisexto == 0:
			diasMes = 29;		# Mes de Fevereiro e Ano Bisexto

	primeiroDiaMes = dt.date(yy, mm, 1);
	primeiroDiaSemana = primeiroDiaMes.weekday();
	strPrimeiroDiaSemana = arrDiaSemana[primeiroDiaSemana];

	print('Data Atual:', dataAtual);
	print('Primeiro Dia do Mes:', primeiroDiaMes, 'Dia da Semana:', strPrimeiroDiaSemana);

	for i in range(0, diasMes - 1):
		valDiaSemana = (primeiroDiaSemana + i) % 7;
		strDiaSemana = arrDiaSemana[valDiaSemana];

		diaMes = i + 1;

		if valDiaSemana == 5 or valDiaSemana == 6:
			print('Dia:', diaMes, "Dia da Semana:", strDiaSemana, "*** DIA DE DESCANSO ***");
		else:
			print('Dia:', diaMes, "Dia da Semana:", strDiaSemana);
	print('');

# CONTROLE_CONDICIONAL: IF_THEN_ELSE_ELIF
def teste3_controleCondicional_IF_THEN_ELSE_ELIF():
	arrDiasMes = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ];
	arrDiaSemana = [ 'Segunda-feira', 'Terca-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sabado', 'Domingo' ];

	objDate = dt.date;

	dataAtual = objDate.today();

	#dd = dataAtual.day;
	mm = dataAtual.month;
	yy = dataAtual.year;

	diasMes = arrDiasMes[mm];
	if mm == 1:					# Se Mes de Fevereiro => 28 ou 29 dias
		anoBisexto = yy % 4;
		if anoBisexto == 0:
			diasMes = 29;		# Mes de Fevereiro e Ano Bisexto

	primeiroDiaMes = dt.date(yy, mm, 1);
	primeiroDiaSemana = primeiroDiaMes.weekday();
	strPrimeiroDiaSemana = arrDiaSemana[primeiroDiaSemana];

	print('Data Atual:', dataAtual);
	print('Primeiro Dia do Mes:', primeiroDiaMes, 'Dia da Semana:', strPrimeiroDiaSemana);

	for i in range(0, diasMes - 1):
		valDiaSemana = (primeiroDiaSemana + i) % 7;
		strDiaSemana = arrDiaSemana[valDiaSemana];

		diaMes = i + 1;

		if valDiaSemana == 5 or valDiaSemana == 6:
			print('Dia:', diaMes, "Dia da Semana:", strDiaSemana, "*** DIA DE DESCANCO! ***");
		elif valDiaSemana == 0:
			print('Dia:', diaMes, "Dia da Semana:", strDiaSemana, "*** VOLTA AS AULAS! ***");
		elif valDiaSemana == 4:
			print('Dia:', diaMes, "Dia da Semana:", strDiaSemana, "*** HOJE E SEXTA-FEIRA! ***");
		else:
			print('Dia:', diaMes, "Dia da Semana:", strDiaSemana);
		
	print('');

def recursos():
	print('RECURSOS:');
	print('=========');
	print('teste1_controleCondicional_IF_THEN()');
	print('teste2_controleCondicional_IF_THEN_ELSE()');
	print('teste3_controleCondicional_IF_THEN_ELSE_ELIF()');
	print('');

def executaTudo():
	print('EXECUTA:');
	print('========');
	print('');

	print('Executa: teste1_controleCondicional_IF_THEN()');
	teste1_controleCondicional_IF_THEN();
	print('');

	print('teste2_controleCondicional_IF_THEN_ELSE');
	teste2_controleCondicional_IF_THEN_ELSE();
	print('');

	print('teste3_controleCondicional_IF_THEN_ELSE_ELIF()');
	teste3_controleCondicional_IF_THEN_ELSE_ELIF();
	print('');

def carregado():
	print('Arquivo: ex04_controle_condicional_IF_THEN_ELSE_ELIF.py... carregado!');
	print('');

