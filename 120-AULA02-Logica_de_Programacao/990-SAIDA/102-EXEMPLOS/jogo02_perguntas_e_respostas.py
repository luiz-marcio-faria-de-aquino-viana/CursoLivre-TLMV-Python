"""
Copyright (c) 2025-2026 TLMV Consultoria e Sistemas EIRELI.

jogo02_perguntas_e_respostas.py
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

import ex09_leitura_teclado as ex;

# CONSTANTES #

DEF_LISTA_PERGUNTAS = [
	"1)Qual a probabilidade de em um jogo de dados sair o numero 6?",
	"2)Qual a probabilidade de em um jogo de dados sair um numero par?",
	"3)Joaozinho corre diariamente. Na semana passada ele correu 2000 m, 3000 m, 4000 m, 4000 m, e 2000 m, na semana passada. Qual foi a distancia media que ele correu na semana passada?",
	"4)A escola de Joana dista de sua casa 780 m. Qual a distancia da escola em Notacao Cientifica?"
];

DEF_LISTA_OPCOES = [
	[ "(a)1/2", "a", "(b)1/3", "b", "(c)1/4", "c", "(d)1/6", "d", "(e)Nunhuma das opcoes", "e" ],
	[ "(a)1/2", "a", "(b)1/3", "b", "(c)1/4", "c", "(d)1/6", "d", "(e)Nunhuma das opcoes", "e" ],
	[ "(a)2000 m", "a", "(b)3000 m", "b", "(c)4000 m", "c", "(d)5000 m", "d", "(e)Nunhuma das opcoes", "e" ],
	[ "(a)7,8 x 10^1 m", "a", "(b)7,8 x 10^2 m", "b", "(c)7,8 x 10^3 m", "c", "(d)7,8 x 10^4 m", "d", "(e)Nunhuma das opcoes", "e" ]
];

DEF_LISTA_RESPOSTAS = [
	"(d)1/6",
	"(b)1/3",
	"(b)3000 m",
	"(b)7,8 x 10^2 m"
];

# METODOS #

# funcGeradorValorAleatorio(): funcao que retorna um valor aleatorio entre [0, n]
def funcGeradorValorAleatorio(n):
	valorAleatorio = m.floor( r.uniform(0.0, n) );
	return valorAleatorio;

# MENSAGENS #

# procCopyright(): procedimento que apresenta informacoes sobre o jogo
def procCopyright():
	print("Jogo 02 - Perguntas e Respostas");
	print("");
	print("Autor: Luiz Marcio Faria de Aquino Viana, Post-D.Sc. (COPPE/UFRJ em 2002 e 2022)");
	print("Formacao: Engenheiro Eletricista com Enfase em Engenharia de Sistemas e Computacao (UERJ em 1997");
	print("Registro: 2000103581 CREA-RJ - CPF: 024.723.347-10");
	print("E-mail: lmarcio@tlmv.com.br - Outro e-mail: luiz.marcio.viana@gmail.com");
	print("Telefone: (21)99983-7207)");
	print("");

# CODIGO PRINCIPAL #

# procExecuta(): procedimento principal de execucao do jogo
def procExecuta():
	placar = 0;
	n = 1;

	numMaxPergunta = len( DEF_LISTA_PERGUNTAS );

	while True:
		print('PERGUNTA ', n);
		print('');

		pos = funcGeradorValorAleatorio(numMaxPergunta);

		pergunta = DEF_LISTA_PERGUNTAS[pos];
		arrOpcao = DEF_LISTA_OPCOES[pos];
		resposta = DEF_LISTA_RESPOSTAS[pos];

		opcao = ex.funcLeEntradaOpcao(pergunta, arrOpcao, None, True);
		if opcao == None:
			break;

		if opcao == resposta:
			print("Voce acertou!");
			placar = placar + 30;
		else:
			print("Voce errou! A resposta correta e ", resposta);
			placar = placar - 10;

		print('PLACAR: ', placar);
		print('');

		if placar <= 0.0:
			print("G A M E   O V E R");
			break;

		n = n + 1;

	print('Tchau!');
	print('');

# EXECUCAO #

procCopyright();
procExecuta();
