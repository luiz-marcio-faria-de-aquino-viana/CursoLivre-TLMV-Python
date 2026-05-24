"""
Copyright (c) 2025-2026 TLMV Consultoria e Sistemas EIRELI.

jogo03_funcoes_estatisticas.py
Autor: 
Luiz Marcio Faria de Aquino Viana, Pos-D.Sc. - Engenheiro, 23/05/2026
Unidade: Universidade do Estado do Rio de Janeiro
Curso: Engenharia Eletrica, Enfase em Engenharia de Sistemas e Computacao
Unico Socio e Administrador da Empresa - Desde: 02/08/2000

Revisoes: ...
"""

import math as m;
import random as r;
import statistics as s;

# DEFINICOES #

DEF_NUM_MAX_ELEMENTOS = 100;

DEF_DISTRIB_UNIOFORM 		= 0;
DEF_DISTRIB_NORMAL 			= 1;
DEF_DISTRIB_LOGNORMAL 		= 2;
DEF_DISTRIB_EXPONENCIAL 	= 3;

DEF_VALOR_MINIMO			= 0.0;
DEF_VALOR_MAXIMO			= 10.0
DEF_VALOR_MEDIO				= 5.0
DEF_VALOR_DESVIOPADRAO		= 1.0

#gDistrib = DEF_DISTRIB_UNIOFORM;
gDistrib = DEF_DISTRIB_NORMAL;

# CLASSES #

class FreqValor:
	valor = 0.0;
	freq = 0.0;

	def __init__(self, val):
		self.valor = val;
		self.freq = 0.0;

	def add(self):
		self.freq = self.freq + 1;
		return self.freq;

	# Getters/Setters */

	def getValor(self):
		return self.valor;

	def getFreq(self):
		return self.freq;

# METODOS #

# gera_amostra(): funcao que gera amostra com valores aleatorios
def gera_amostra():
	lsResult = [];
	for i in range(0, DEF_NUM_MAX_ELEMENTOS):
		rnd = 0.0;
		if gDistrib == DEF_DISTRIB_UNIOFORM:
			rnd = m.floor( r.uniform(DEF_VALOR_MINIMO, DEF_VALOR_MAXIMO) );		# numero aleatorio (Distribuicao Uniforme)
		elif gDistrib == DEF_DISTRIB_NORMAL:
			rnd = r.normalvariate(DEF_VALOR_MEDIO, DEF_VALOR_DESVIOPADRAO);		# numero aleatorio (Distribuicao Normal)
		elif gDistrib == DEF_DISTRIB_LOGNORMAL:
			rnd = r.lognormalvariate(DEF_VALOR_MEDIO, DEF_VALOR_DESVIOPADRAO);	# numero aleatorio (Distribuicao Lognormal)
		elif gDistrib == DEF_DISTRIB_EXPONENCIAL:
			rnd = r.expovariate(DEF_VALOR_MEDIO);								# numeros aleatorio (Distribuicao Exponencial)
		lsResult.append( m.fabs( rnd ) );
	return lsResult;

# busca_item(): funcao que busca item na lista de valores e frequencias
# ls - vetor de valores
# val - valor a ser pesquisado
def busca_item(ls, val):
	n = len(ls);
	for i in range(0, n):
		item = ls[i];
		itemValor = item.getValor();
		if itemValor == val:
			return item;
	return None;

# lista_freq_amostra(): funcao que retorna a lista de frequencia da amostra
# ls - vetor de valores
def lista_freq_amostra(ls):
	lsFreq = [];

	n = len(ls);
	for i in range(0, n):
		val = ls[i];

		item = busca_item(lsFreq, val);
		if item == None:
			item = FreqValor(val);
			lsFreq.append( item );
		item.add();
	return lsFreq;

# minimo_amostra(): funcao que retorna o valor minimo da amostra
# ls - vetor de valores
def minimo_amostra(ls):
	result = 9999.0;
	n = len(ls);
	for i in range(0, n):
		val = ls[i];
		if val < result:
			result = val;
	return result;

# maximo_amostra(): funcao que retorna o valor maximo da amostra
# ls - vetor de valores
def maximo_amostra(ls):
	result = -9999.0;
	n = len(ls);
	for i in range(0, n):
		val = ls[i];
		if val > result:
			result = val;
	return result;

# media_amostra(): funcao que retorna a media da amostra
# ls - vetor de valores
def media_amostra(ls):
	soma = 0.0;
	n = len(ls);
	for i in range(0, n):
		val = ls[i];
		soma = soma + val;
	media = soma / n;
	return media;

# range_amostra(): funcao que retorna os valores minimos e maximos da amostra
# ls - vetor de valores
def range_amostra(ls):
	valMin = minimo_amostra(ls);
	valMax = maximo_amostra(ls);
	result = [ valMin, valMax ];
	return result;

# desvio_absoluto_amostra(): funcao que retorna o desvio absoluto da amostra
# ls - vetor de valores
def desvio_absoluto_amostra(ls):
	media = media_amostra(ls);
	soma_desvio = 0.0;
	n = len(ls);
	for i in range(0, n):
		val = ls[i];
		dist_media = m.fabs( val - media );
		soma_desvio = soma_desvio + dist_media;
	desvio_absoluto = soma_desvio / n;
	return desvio_absoluto;

# variancia_amostra(): funcao que retorna a variancia da amostra
# ls - vetor de valores
def variancia_amostra(ls):
	media = media_amostra(ls);
	soma_desvio = 0.0;
	n = len(ls);
	for i in range(0, n):
		val = ls[i];
		dist_media = m.pow(val - media, 2.0);
		soma_desvio = soma_desvio + dist_media;
	variancia = soma_desvio / n;
	return variancia;

# desvio_padrao_amostra(): funcao que retorna a variancia da amostra
# ls - vetor de valores
def desvio_padrao_amostra(ls):
	variancia = variancia_amostra(ls);
	desvio_padrao = m.pow(variancia, 0.5);
	return desvio_padrao;

# moda_amostra(): funcao que retorna a moda da amostra
# ls - vetor de valores
def moda_amostra(ls):
	moda = FreqValor(0.0);

	lsFreq = lista_freq_amostra(ls);
	n = len(lsFreq);
	for i in range(0, n):
		item = lsFreq[i];
		itemFreq = item.getFreq();

		modaFreq = moda.getFreq();
		if itemFreq > modaFreq:
			moda = item;
	return moda;

# mediana_amostra(): funcao que retorna a mediana dos valores da amostra
# ls - vetor de valores
def mediana_amostra(ls):
	mediana = FreqValor(0.0);

	ls.sort();

	lsFreq = lista_freq_amostra(ls);
	n = len(lsFreq);	

	resto = n % 2;
	if resto == 0:
		pos0 = m.floor(n / 2.0);
		item0 = lsFreq[pos0];
		itemVal0 = item0.getValor();

		pos1 = pos0 + 1;
		item1 = lsFreq[pos1];
		itemVal1 = item1.getValor();

		val = (itemVal0 + itemVal1) / 2.0;
	else:
		pos0 = m.floor( (n + 1) / 2.0 );
		item0 = lsFreq[pos0];
		itemVal0 = item0.getValor();

		val = itemVal0;
	return val;

# quartil1_amostra(): funcao que retorna o quartil Q1 da amostra (25% menores valores)
# ls - vetor de valores
def quartil1_amostra(ls):
	val = 0.0;

	ls.sort();

	lsFreq = lista_freq_amostra(ls);
	n = len(lsFreq);	
	
	resto = n % 4;
	if resto == 0:
		pos0 = m.floor(n / 4.0);
		item0 = lsFreq[pos0];
		itemVal0 = item0.getValor();

		pos1 = pos0 + 1;
		item1 = lsFreq[pos1];
		itemVal1 = item1.getValor();

		val = (itemVal0 + itemVal1) / 2.0;
	else:
		pos0 = m.floor(n / 4.0);
		item0 = lsFreq[pos0];
		itemVal0 = item0.getValor();

		val = itemVal0;
	return val;

# quartil2_amostra(): funcao que retorna o quartil Q2 da amostra (= mediana)
# ls - vetor de valores
def quartil2_amostra(ls):
	val = mediana_amostra(ls);
	return val;

# quartil3_amostra(): funcao que retorna o quartil Q3 da amostra (25% maiores valores)
# ls - vetor de valores
def quartil3_amostra(ls):
	val = 0.0;

	ls.sort();

	lsFreq = lista_freq_amostra(ls);
	n = len(lsFreq);	
	
	k = 3.0 * n;

	resto = k % 4;
	if resto == 0:
		pos0 = m.floor(k / 4.0);
		item0 = lsFreq[pos0];
		itemVal0 = item0.getValor();

		pos1 = pos0 + 1;
		item1 = lsFreq[pos1];
		itemVal1 = item1.getValor();

		val = (itemVal0 + itemVal1) / 2.0;
	else:
		pos0 = m.floor(k / 4.0);
		item0 = lsFreq[pos0];
		itemVal0 = item0.getValor();

		val = itemVal0;
	return val;

# MENSAGENS #

# procCopyright(): procedimento que apresenta informacoes sobre o jogo
def procCopyright():
	print("Jogo 03 - Funcoes Estatisticas");
	print("");
	print("Autor: Luiz Marcio Faria de Aquino Viana, Post-D.Sc. (COPPE/UFRJ em 2002 e 2022)");
	print("Formacao: Engenheiro Eletricista com Enfase em Engenharia de Sistemas e Computacao (UERJ em 1997");
	print("Registro: 2000103581 CREA-RJ - CPF: 024.723.347-10");
	print("E-mail: lmarcio@tlmv.com.br - Outro e-mail: luiz.marcio.viana@gmail.com");
	print("Telefone: (21)99983-7207");
	print("");

# CODIGO PRINCIPAL #

def procExecuta():
	ls = gera_amostra();

	valMin = minimo_amostra(ls);
	valMax = maximo_amostra(ls);
	valMedia = media_amostra(ls);
	valRange = range_amostra(ls);
	valDesvioAbsoluto = desvio_absoluto_amostra(ls);
	valVariancia = variancia_amostra(ls);
	valDesvioPadrao = desvio_padrao_amostra(ls);
	valModa = moda_amostra(ls);
	valMediana = mediana_amostra(ls);
	valQ1 = quartil1_amostra(ls);
	valQ2 = quartil2_amostra(ls);
	valQ3 = quartil3_amostra(ls);

	print('Amostra:', ls);
	print('');

	print('Minimo:', valMin);
	print('Maximo:', valMax);
	print('');

	print('Range:', valRange);
	print('');

	print('Media:', valMedia);
	print('Desvio Absoluto:', valDesvioAbsoluto);
	print('Variancia:', valVariancia);
	print('Desvio Padrao:', valDesvioPadrao);
	print('');

	print('Moda:', valModa.getValor(), 'Freq: ', valModa.getFreq());
	print('Mediana:', valMediana);
	print('');

	print('Q1:', valQ1);
	print('Q2:', valQ2);
	print('Q3:', valQ3);
	print('');

procCopyright();
procExecuta();

