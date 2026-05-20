"""
Copyright (c) 2025-2026 TLMV Consultoria e Sistemas EIRELI.

ex02_operacoes_matematicas.py
Autor: 
Luiz Marcio Faria de Aquino Viana, Pos-D.Sc. - Engenheiro, 28/04/2026
Unidade: Universidade do Estado do Rio de Janeiro
Curso: Engenharia Eletrica, Enfase em Engenharia de Sistemas e Computacao
Unico Socio e Administrador da Empresa - Desde: 02/08/2000

Revisoes: ...
"""

import math as m;
import random as r;
import statistics as s;

# OPERACAO: SOMA (POSICAO FINAL)
def teste1_operacaoSoma():
	S0 = 10.0;			# posicao inicial da particula (m)
	dS = 100.0;			# deslocamento da particula em um tempo (dT)

	S1 = S0 + dS;		# posicao final da particula (m)

	print('Posicao inicial (m):', S0);
	print('Deslocamento (m):', dS);
	print('Posicao final (m):', S1);

# OPERACAO: SUBTRACAO (DESLOCAMENTO)
def teste2_operacaoSubtracao():
	S0 = 10.0;			# posicao inicial da particula (m)
	S1 = 110.0;			# posicao final da particula (m)

	dS = S1 - S0;		# deslocamento da particula em um tempo (dT)

	print('Posicao inicial (m):', S0);
	print('Posicao final (m):', S1);
	print('Deslocamento (m):', dS);

# OPERACAO: DIVISAO (VELOCIDADE MEDIA)
def teste3_operacaoDivisao():
	S0 = 10.0;			# posicao inicial da particula (m)
	S1 = 110.0;			# posicao final da particula (m)

	dT = 10.0;			# tempo decorrido (s)
	dS = S1 - S0;		# deslocamento da particula em um tempo (dT)

	Vmedia = dS / dT;	# velocidade media (m/s)

	print('Posicao inicial (m):', S0);
	print('Posicao final (m):', S1);
	print('Tempo decorrido (s):', dT);
	print('Deslocamento (m):', dS);
	print('Velocidade media (m/s):', Vmedia);

# OPERACAO: MULTIPLICACAO (VELOCIDADE FINAL COM ACELERACAO CONSTANTE)
def teste4_operacaoMultiplicacao():
	V0 = 10.0;			# velocidade inicial da particula (m/s)

	A = 0.5;			# aceleracao da particula (m/s2)
	dT = 10.0;			# tempo decorrido (s)

	V1 = V0 + (A * dT);		# velocidade final da particula

	print('Velocidade inicial (m/s):', V0);
	print('Aceleracao (m/s2):', A);
	print('Tempo decorrido (s):', dT);
	print('Velocidade final (m/s):', V1);

# OPERACAO: POTENCIACAO (MOVIMENTO UNIFORMEMENTE ACELERACAO)
def teste5_operacaoPotenciacao():
	S0 = 10.0;			# posicao inicial da particula (m)
	V0 = 10.0;			# velocidade inicial da particula (m/s)

	A = 0.5;			# aceleracao da particula (m/s2)
	dT = 10.0;			# tempo decorrido (s)

	S1 = S0 + (V0 * dT) + (A * (dT ** 2.0));		# posicao final da particula

	print('Posicao inicial (m):', S0);
	print('Velocidade inicial (m/s):', V0);
	print('Aceleracao (m/s2):', A);
	print('Tempo decorrido (s):', dT);
	print("Posicao final: ", S1);

# OPERACAO: RADICIACAO (ENERGIA POTENCIAL GRAVITACIONAL)
def teste6_operacaoRadiciacao():
	m = 10.0;			# massa do corpo (Kg)
	g = 9.8;			# aceleracao da gravidade (m/s2)
	h = 30.0;			# altura (m)

	Ep = m * g * h;		# Energia Potencial Gravitacional (j)

	Ec = Ep;			# Energia Cinetica (no solo) = Energia Potencial Gravitacional (altura = h)

	V1 = (Ec / ((1 / 2) * m) ) ** 0.5;

	print('massa do corpo (Kg):', m);
	print('Aceleracao da gravidade (m/s2):', g);
	print('Altura inicial (m):', h);

	print('Energia Potencial Gravitacional na Altura Inicial (j):', Ep);

	print('Energia Cinetica no Solo (j):', Ec);

	print("Velocidade final (m/s): ", V1);

# OPERACAO: SENO / COSENO (DECOMPOSICAO DA VELOCIDADE INICIAL DO PROJETIL)
def teste7_operacaoSenoCoseno():
	V0 = 1000.0;					# velocidade inicial do projetil (m/s)
	angGr = 60.0;					# angulo de disparo do projetil (graus)
	
	angRad = angGr * (m.pi / 180.0);	# angulo de disparo do projetil (radianos)

	VY0 = V0 * m.sin(angRad);			# velocidade inicial vertical do projetil (m/s)
	VX0 = V0 * m.cos(angRad);			# velocidade inicial horizontal do projetil (m/s)

	print('Velocidade inicial (m/s):', V0);
	print('Angulo de disparo (graus):', angGr);
	print('Conversao do angulo de disparo para radianos:', angRad);
	print("Velocidade vertical inicial (m/s): ", VY0);
	print("Velocidade horizontal inicial (m/s): ", VX0);

# OPERACAO: NUMEROS ALEATORIOS
def teste8_operacaoNumerosAleatorios():
	for i in range(1, 10):
		rndUniform = r.uniform(0.0, 5.0);						# numero aleatorio (Distribuicao Uniforme)
		rndNormal = r.normalvariate(0.0, 1.0);					# numero aleatorio (Distribuicao Normal)
		rndExp = r.expovariate(1.0);							# numeros aleatorio (Distribuicao Exponencial)

		print('ITERACAO:', i)
		print('=========')
		print("Uniform:", rndUniform);
		print("Normal:", rndNormal);
		print("Exponencial:", rndExp);

	print('');

# OPERACAO: ESTATISTICA BASICA
def teste9_operacaoEstatistica():
	valores = [];
	for i in range(1, 100):
		rndNormal = r.normalvariate(0.0, 1.0);					# numero aleatorio (Distribuicao Normal)
		rndNormal = m.floor( rndNormal * 10.0 ) / 10.0;

		valores.append( rndNormal );

	moda = s.mode(valores);										# moda
	mediana = s.median(valores);								# mediana
	media = s.mean(valores);									# media
	varianca = s.variance(valores);								# varianca
	stdev = s.stdev(valores);									# desvio padrao

	print('Valores:', valores);
	print('');
	print('Moda:', moda);
	print('Mediana:', mediana);
	print('Media:', media);
	print('Varianca:', varianca);
	print('Desvio padrao:', stdev);
	print('');

# OPERACAO: RESTO DIVISAO (MAXIMO DIVISOR COMUM - FORCA BRUTA)
def teste10_operacaoResto():
	valor1 = 192;
	valor2 = 256;

	valorMenor = valor1;
	if(valor2 < valorMenor):
		valorMenor = valor2;
	hValorMenor = m.floor( valorMenor / 2.0 );

	mdc = 1;
	for i in range(2, hValorMenor):
		resto1 = valor1 % i;
		resto2 = valor2 % i;

		if( (resto1 == 0) and (resto2 == 0) ):
			mdc = i;

	print('Valor 1:', valor1);
	print('Valor 2:', valor2);
	print('MDC:', mdc);
	print('');

def recursos():
	print('RECURSOS:');
	print('=========');
	print('teste1_operacaoSoma()');
	print('teste2_operacaoSubtracao()');
	print('teste3_operacaoDivisao()');
	print('teste4_operacaoMultiplicacao()');
	print('teste5_operacaoPotenciacao()');
	print('teste6_operacaoRadiciacao()');
	print('teste7_operacaoSenoCoseno()');
	print('teste8_operacaoNumerosAleatorios()');
	print('teste9_operacaoEstatistica()');
	print('teste10_operacaoResto()');
	print('');

def executaTudo():
	print('EXECUTA:');
	print('========');
	print('');

	print('Executa: teste1_operacaoSoma()');
	teste1_operacaoSoma();
	print('');

	print('Executa: teste2_operacaoSubtracao()');
	teste2_operacaoSubtracao();
	print('');

	print('Executa: teste3_operacaoDivisao()');
	teste3_operacaoDivisao();
	print('');

	print('Executa: teste4_operacaoMultiplicacao()');
	teste4_operacaoMultiplicacao();
	print('');

	print('Executa: teste5_operacaoPotenciacao()');
	teste5_operacaoPotenciacao();
	print('');

	print('Executa: teste6_operacaoRadiciacao()');
	teste6_operacaoRadiciacao();
	print('');

	print('Executa: teste7_operacaoSenoCoseno()');
	teste7_operacaoSenoCoseno();
	print('');

	print('Executa: teste8_operacaoNumerosAleatorios()');
	teste8_operacaoNumerosAleatorios();
	print('');

	print('Executa: teste9_operacaoEstatistica()');
	teste9_operacaoEstatistica();
	print('');

	print('teste10_operacaoResto()');
	teste10_operacaoResto();
	print('');

def carregado():
	print('Arquivo: ex02_operacoes_matematicas.py... carregado!');
	print('');

