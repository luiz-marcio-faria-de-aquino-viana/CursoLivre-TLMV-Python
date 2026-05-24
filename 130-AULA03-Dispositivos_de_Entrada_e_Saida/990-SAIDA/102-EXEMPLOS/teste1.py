"""
Copyright (c) 2025-2026.

teste1.py
Autor: 
Wendell Rodrigues - Fisio Terapeuta, 01/05/2026
Unidade: IBMR
Curso: Fisioterapia

Revisoes: ...
"""

import random as r;
import math as m;
import statistics as s;

def teste1_procValorParcela1():
	valorTotal = 1000.0;				# valor total do item
	numeroParcelas  = 24.0;				# numero de parcelas para pagamento

	valorParcelas = valorTotal / numeroParcelas;	# variavel armazena valor das parcelas
	print(valorParcelas);			

def teste1_procValorParcela2(valorTotal, numeroParcelas):
	valorParcelas = valorTotal / numeroParcelas;	# variavel armazena valor das parcelas
	print(valorParcelas);			

def teste1_procValorTotalVenda1():
	valoresTotalItens = [ 5.0, 3.0, 5.0, 3.0, 3.0, 20.0, 30.0, 20.0 ];
	n = len(valoresTotalItens);

	valorTotalVenda = 0.0;
	for i in range(0, n - 1):
		valorItem = valoresTotalItens[i];
		valorTotalVenda = valorTotalVenda + valorItem;
	
	numeroParcelas = 3.0;

	print("Valor total da venda (R$): ", valorTotalVenda);
	print("Numero de parcelas: ", numeroParcelas)

	print("Valor total da parcela: "); 
	teste1_procValorParcela2(valorTotalVenda, numeroParcelas);

def teste1_procValorTotalVenda2(valoresTotalItens):
	n = len(valoresTotalItens);

	valorTotalVenda = 0.0;
	for i in range(0, n - 1):
		valorItem = valoresTotalItens[i];
		valorTotalVenda = valorTotalVenda + valorItem;
	
	numeroParcelas = 3.0;

	print("Valor total da venda (R$): ", valorTotalVenda);
	print("Numero de parcelas: ", numeroParcelas)

	print("Valor total da parcela: "); 
	teste1_procValorParcela2(valorTotalVenda, numeroParcelas);

# OPERACAO: ESTATISTICA BASICA
def teste1_operacaoEstatistica():
	valores = [];
	for i in range(1, 10000):
		rndNormal = r.normalvariate(27.0, 3.0);						# numero aleatorio (Distribuicao Normal)
		#rndNormal = r.uniform(0.0, 1000.0);						# numero aleatorio (Distribuicao Uniforme)
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

def teste1_procProblemaBalistica1(velocidadeProjetil, anguloGraus):
	anguloRadianos = anguloGraus / 180.0 * m.pi;

	velocidadeHorizontalProjetil = velocidadeProjetil * m.cos(anguloRadianos);
	velocidadeVerticalProjetil = velocidadeProjetil * m.sin(anguloRadianos);

	print("VelocidadeHorizontalProjetil: ", velocidadeHorizontalProjetil);
	print("VelocidadeVerticalProjetil: ", velocidadeVerticalProjetil);

def teste1_procProblemaBalistica2(velocidadeVerticalProjetil, velocidadeHorizontalProjetil, aceleracaoGravidade, massaProjetil):
	# calcular a altuma maxima do projetil
	# duracao de percurso = 2x tempo de subida
	# calcular a distancia maxima do projetil

	#print("AlturaMaxima: ", alturaMaxima);
	#print("TempoTotalPercurso: ", tempoTotalPercurso);
	#print("AlcanceDisparo: ", alcanceDisparo);

	import math as m

def teste1_procProblemaBalistica3(velocidadeProjetil, anguloGraus):
	anguloRadianos = anguloGraus / 180.0 * m.pi
	velocidadeHorizontalProjetil = velocidadeProjetil * m.cos(anguloRadianos)
	velocidadeVerticalProjetil = velocidadeProjetil * m.sin(anguloRadianos)
	print("Horizontal: ", velocidadeHorizontalProjetil);
	print("Vertical: ", velocidadeVerticalProjetil);

# funcLeEntradaTexto(): funcao que apresenta uma mensagem e espera a digitacao de um texto
# mensagem - mensagem a ser apresentada na tela
def funcLeEntradaTexto(mensagem):
	print(mensagem);

	f = open("/dev/stdin", 'r');
	texto = f.readline(4096);
	f.close();
	return texto;

# EXECUCAO

#texto = funcLeEntradaTexto("Angulo? ");
#anguloGraus = float(texto);
#velocidadeProjetil = 1000.0;
#teste1_procProblemaBalistica3(velocidadeProjetil, anguloGraus);

questoes = [ "Quantos dias tem 1 ano?", "Quantos minutos tem 1 hora?", "Qual a aceleracao da gravidade?" ];

opcoes = [ 
	[ "(a)200 dias", "(b)360 dias", "(c)365 dias", "(d)366 dias", "(e)Nenhuma" ],
	[ "(a)10 minutos", "(b)30 minutos", "(c)50 minutos", "(d)60 minutos", "(e)Nenhuma" ],
	[ "(a)100 Km/s", "(b)300.000 Km/s", "(c)10 Km/s", "(d)9,8 m/s", "(e)Nenhuma" ] ];

respostas = [ "c", "d", "d" ];

rnd = r.uniform(0.0, 3.0);

numQuestao = m.floor(rnd);
print(numQuestao);

q = questoes[numQuestao];
print(q);

arr = opcoes[numQuestao];
#print(arr);

for o in arr:
	print(o);
print("");

resp = funcLeEntradaTexto("resposta: ");
#print(resp);
resp = resp[0];

respCorreta = respostas[numQuestao];
#print(respCorreta);

if resp == respCorreta:
	print('*** ACERTOU! ***');
else:
	print('*** ERROU! ***');
print('');
