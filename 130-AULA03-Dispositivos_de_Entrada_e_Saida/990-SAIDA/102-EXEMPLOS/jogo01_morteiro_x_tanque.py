"""
Copyright (c) 2025-2026 TLMV Consultoria e Sistemas EIRELI.

jogo01_morteiro_x_tanque.py
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

DEF_ACELERACAO_GRAVIDADE = 9.8;					# aceleracao da gravidade (m/s2)

DEF_VELOCIDADE_PROJETIL = 1000.0;				# velocidade media do projetil (m/s)
DEF_VARIACAO_VELOCIDADE_PROJETIL = 100.0;		# desvio maximo esperado para a velocidade do projetil (m/s)
DEF_MASSA_PROJETIL = 1.0;						# massa do projetil (Kg)

DEF_VELOCIDADE_TANQUE = 50.0;					# velocidade media do tanque (Km/h)
DEF_VARIACAO_VELOCIDADE_TANQUE = 5.0;			# desvio maximo esperado para a velocidade do tanque (Km/h)

DEF_DISTANCIA_TANQUE = 100.0 * 1000.0;			# distancia media do tanque (m)
DEF_VARIACAO_DISTANCIA_TANQUE = 5.0 * 1000.0;	# desvio maximo esperado para a distancia do tanque (m)
DEF_COMPRIMENTO_TANQUE = 10.0;					# comprimento do tanque (m)

# VARIAVEIS #

gVelocidadeInicialProjetil = 0.0;				# velocidade inicial do projetil (m/s)
gVelocidadeInicialTanque = 0.0;					# velocidade inicial do projetil (m/s)
gDistanciaInicialTanque = 0.0;					# distancoa inicial do tanque (Km)

# METODOS #

# funcGeradorValorAleatorio(): funcao que retorna um valor aleatorio entre [-0.6, 0.6]
def funcGeradorValorAleatorio():
	valorAleatorio = r.normalvariate(0, 1);
	if(valorAleatorio > 0.6):
		valorAleatorio = 0.6;
	if(valorAleatorio < -0.6):
		valorAleatorio = -0.6;
	return valorAleatorio;

# MOVIMENTO: PROJETIL #

# funcVelocidadeInicialProjetil(): funcao que retorna a velocidade inicial do projetil
# velocidadeBase - velocidade esperada para o projetil
# variacaoVelocidadeBase - desvio maximo esperado para a velocidade do projetil
def funcVelocidadeInicialProjetil(velocidadeBase, variacaoVelocidadeBase):
	valorAleatorio = funcGeradorValorAleatorio();

	variacaoVelocidade = valorAleatorio * variacaoVelocidadeBase;
	velocidadeInicial = velocidadeBase + variacaoVelocidade;
	return velocidadeInicial;

# funcVelocidadeVerticalInicialProjetil(): funcao que retorna a velocidade vertical inicial do projetil
# velocidadeInicial - velocidade inicial do projetil
# anguloGraus - angulo de lancamento do projetil
def funcVelocidadeVerticalInicialProjetil(velocidadeInicial, anguloGraus):
	anguloRadianos = anguloGraus * (m.pi / 180.0);

	velocidadeVerticalInicial = velocidadeInicial * m.sin(anguloRadianos);
	return velocidadeVerticalInicial;

# funcVelocidadeHorizontalInicialProjetil(): funcao que retorna a velocidade horizontal inicial do projetil
# velocidadeInicial - velocidade inicial do projetil
# anguloGraus - angulo de lancamento do projetil
def funcVelocidadeHorizontalInicialProjetil(velocidadeInicial, anguloGraus):
	anguloRadianos = anguloGraus * (m.pi / 180.0);

	velocidadeHorizontalInicial = velocidadeInicial * m.cos(anguloRadianos);
	return velocidadeHorizontalInicial;

# funcAlturaMaximaProjetil(): funcao que retorna a altura maxima do disparo do projetil
# velocidadeVerticalProjetil - velocidade vertical inicial do projetil
# massaProjetil - massa do projetil
# aceleracaoGravidade - aceleracao da gravidade
def funcAlturaMaximaProjetil(velocidadeVerticalProjetil, massaProjetil, aceleracaoGravidade):
	# Ec = 1/2 x MASSA x ( VELOCIDADE x VELOCIDADE ) = Ep = MASSA x ACELERACAO_GRAVIDADE x ALTURA
	# Logo: ALTURA = ( 1/2 x VELOCIDADE x VELOCIDADE ) / ACELERACAO_GRAVIDADE

	# NOTA: MASSA PROJETIL E DESCONSIDERADA
	alturaMaxima = 0.5 * ( velocidadeVerticalProjetil ** 2.0 ) / aceleracaoGravidade;
	return alturaMaxima;

# funcDistanciaPercorridaProjetil(): funcao que retorna a distancia percorrida pelo projetil
# velocidadeHorizontalProjetil - velocidade horizontal do projetil (movimento com velocidade constante)
# tempo - tempo percorrido pelo projetil
def funcDistanciaPercorridaProjetil(velocidadeHorizontalProjetil, tempo):
	# DISTANCIA_PERCORRIDA = VELOCIDADE_HORIZONTAL_PROJETIL x TEMPO

	distanciaPercorrida = velocidadeHorizontalProjetil * tempo;
	return distanciaPercorrida;

# funcTempoQuedaLivre(): funcao que retorna o tempo de queda livre de um corpo
# alturaInicial - altura inicial do corpo em queda livre
# aceleracaoGravidade - aceleracao da gravidade
def funcTempoQuedaLivre(alturaInicial, aceleracaoGravidade):
	# POSICAO_FINAL = POSICAO_INICIAL + ( VELOCIDADE_INICIAL x TEMPO ) + ( 1/2 x ACELERACAO_GRAVIDADE x TEMPO x TEMPO )
	#
	# PARA CORPO EM QUEDA LIVRE:
	# ==========================
	# POSICAO_FINAL = 0 (ALTURA_SOLO)
	# VELOCIDADE_INICIAL = 0 (VELOCIDADE NA ALTURA_INICIAL)
	#
	# Logo: 0 = ALTURA_INICIAL + 0 + 1/2 x ACELERACAO_GRAVIDADE x TEMPO x TEMPO

	tempoQuedaLivre = ( alturaInicial / ( 0.5 * aceleracaoGravidade ) ) ** 0.5;
	return tempoQuedaLivre;

# MOVIMENTO: TANQUE #

# funcVelocidadeInicialTanque(): funcao que retorna a velocidade inicial do tanque
# velocidadeBase - velocidade esperada para o tanque
# variacaoVelocidadeBase - desvio maximo esperado para a velocidade do tanque
def funcVelocidadeInicialTanque(velocidadeBase, variacaoVelocidadeBase):
	valorAleatorio = funcGeradorValorAleatorio();

	variacaoVelocidade = valorAleatorio * variacaoVelocidadeBase;
	velocidadeInicial = velocidadeBase + variacaoVelocidade;
	return velocidadeInicial;

# funcDistanciaInicialTanque(): funcao que retorna a distancia inicial do tanque
# distanciaBase - distancia esperada para o tanque
# variacaoDistanciaBase - desvio maximo esperado para a distancia do tanque
def funcDistanciaInicialTanque(distanciaBase, variacaoDistanciaBase):
	valorAleatorio = funcGeradorValorAleatorio();

	variacaoDistancia = valorAleatorio * variacaoDistanciaBase;
	distanciaInicial = distanciaBase + variacaoDistancia;
	return distanciaInicial;

# funcDistanciaPercorridaTanque(): funcao que retorna a distancia percorrida pelo tanque
# velocidadeTanque - velocidade do tanque em movimento com velocidade constante (Km/h)
# tempo - tempo percorrido pelo tanque (s)
def funcDistanciaPercorridaTanque(velocidadeTanque, tempo):
	# DISTANCIA_PERCORRIDA = VELOCIDADE_TANQUE (M/S) x TEMPO (S)
	velocidadeTanqueMetros = velocidadeTanque * 1000.0 / 3600.0;

	distanciaPercorrida = velocidadeTanqueMetros * tempo;
	return distanciaPercorrida;

# funcTestaProjetilAcertouTanque(): funcao que verifica se projetil acertou tanque
# posicaoFinalProjetil - posicao final do projetil
# posicaoFinalTanque - posicao final do tanque
# comprimentoTanque - comprimento do tanque
def funcTestaProjetilAcertouTanque(posicaoFinalProjetil, posicaoFinalTanque, comprimentoTanque):
	meioComprimentoTanque = comprimentoTanque / 2.0;

	distanciaImpacto = 100.0 + meioComprimentoTanque;		# distancia de impacto na explosao do projetil (distancia de 100 m ao redor do tanque)

	posicaoFrente = posicaoFinalTanque - distanciaImpacto;
	posicaoTraseira = posicaoFinalTanque + distanciaImpacto;

	bAcertou = False;
	if posicaoFinalProjetil >= posicaoFrente and posicaoFinalProjetil <= posicaoTraseira:
		bAcertou = True;
	return bAcertou;

# UTILITARIOS #

# funcLeEntradaTexto(): funcao que apresenta uma mensagem e espera a digitacao de um texto
# mensagem - mensagem a ser apresentada na tela
def funcLeEntradaTexto(mensagem):
	print(mensagem);

	f = open("/dev/stdin", 'r');
	texto = f.readline(4096);
	f.close();
	return texto;

# funcLeEntradaAnguloGraus(): funcao que apresenta uma mensagem e espera a digitacao de um angulo
# mensagem - mensagem a ser apresentada na tela
def funcLeEntradaAnguloGraus():
	anguloGraus = 0.0;
	bSucesso = False;

	while not bSucesso:
		strAnguloGraus = funcLeEntradaTexto("Informe um angulo entre 22.5 e 85.0 graus (ou SAIR para terminar): ");
		pos = strAnguloGraus.find("SAIR");
		if(pos != -1):
			print("Processamento terminado!");
			quit();

		try:
			anguloGraus = float(strAnguloGraus);

			if anguloGraus < 22.5:
				anguloGraus = 22.5;
			elif anguloGraus > 85.0:
				anguloGraus = 85.0;

			bSucesso = True;
		except:
			print("ERR: Valor invalido.");

			bSucesso = False;
		finally:
			print("");

	return anguloGraus;

# MENSAGENS #

# procCopyright(): procedimento que apresenta informacoes sobre o jogo
def procCopyright():
	print("Jogo 01 - Morteiro x Tanque");
	print("");
	print("Autor: Luiz Marcio Faria de Aquino Viana, Post-D.Sc. (COPPE/UFRJ em 2002 e 2022)");
	print("Formacao: Engenheiro Eletricista com Enfase em Engenharia de Sistemas e Computacao (UERJ em 1997");
	print("Registro: 2000103581 CREA-RJ - CPF: 024.723.347-10");
	print("E-mail: lmarcio@tlmv.com.br - Outro e-mail: luiz.marcio.viana@gmail.com");
	print("Telefone: (21)99983-7207)");
	print("");

# procMostraParametrosIniciais(): procedimento que apresenta os parametros iniciais do jogo
# velocidadeInicialProjetil - velocidade inicial do projetil (m/s)
# velocidadeInicialTanque - velocidade inicial do tanque (Km/h)
# distanciaInicialTanque - distancia inicial do tanque (m)
def procMostraParametrosIniciais(velocidadeInicialProjetil, velocidadeInicialTanque, distanciaInicialTanque):
	print("PARAMETROS INICIAIS:");
	print("====================");
	print("Velocidade inicial do projetil: ", velocidadeInicialProjetil, "m/s");
	print("Velocidade inicial do tanque: ", velocidadeInicialTanque, "Km/h");
	print("Distancia inicial do tanque: ", distanciaInicialTanque, "m");
	print("");

# procMostraDadosNovaTentativa(): procedimento que apresenta os dados para nova tentativa
# numetoTentativa - numero da tentativa
# distanciaInicialTanque - distancia inicial do tanque (m)
def procMostraDadosNovaTentativa(numetoTentativa, distanciaInicialTanque):
	print("TENTATIVA: ", numetoTentativa);
	print("Distancia inicial do tanque: ", distanciaInicialTanque, "m");

# procMostraResultadoProcessamento(): procedimento que apresenta o resultado do processamento
#	velocidadeVerticalProjetil - velocidade vertical do projetil
#	velocidadeHorizontalProjetil - velocidade horizontal do projetil
#	velocidadeTanque - velocidade do tanque
#	distanciaTanque - distancia do tanque
#	anguloGraus - angulo do disparo em graus
#	alturaMaximaDisparo - altura maxima do disparo
#	tempoQuedaLivre tempo de queda livre
#	tempoTotalDisparo - tempo total do disparo
#	distanciaPercorridaDisparo - distancia percorrida pelo disparo
#	distanciaPercorridaTanque - distancia percorrida pelo tanque
#	distanciaFinalTanque - distancia final do tanque
#	mensagemProjetilAcertouTanque - mensagem de resultado (projetil acertou tanque)
def procMostraResultadoProcessamento(
	velocidadeVerticalProjetil,
	velocidadeHorizontalProjetil,
	velocidadeTanque,
	distanciaTanque,
	anguloGraus,
	alturaMaximaDisparo,
	tempoQuedaLivre,
	tempoTotalDisparo,
	distanciaPercorridaDisparo,
	distanciaPercorridaTanque,
	distanciaFinalTanque,
	distanciaProjetilTanque,
	mensagemProjetilAcertouTanque):
	print("RESULTADO PROCESSAMENTO:");
	print("========================");
	print("Velocidade vertical do projetil: ", velocidadeVerticalProjetil, "m/s");
	print("Velocidade horizontal do projetil: ", velocidadeHorizontalProjetil, "m/s");
	print("Velocidade do tanque: ", velocidadeTanque, "Km/h");
	print("Distancia do tanque: ", distanciaTanque, "m");
	print("Angulo de disparo: ", anguloGraus, "Graus");
	print("Altura maxima do disparo: ", alturaMaximaDisparo, "m");
	print("Tempo de queda livre: ", tempoQuedaLivre, "s");
	print("Tempo total do disparo: ", tempoTotalDisparo, "s");
	print("Alcance do disparo: ", distanciaPercorridaDisparo, "m");
	print("Distancia percorrida pelo tanque: ", distanciaPercorridaTanque, "m");
	print("Distancia final do tanque: ", distanciaFinalTanque, "m");
	print("Distancia do alvo: ", distanciaProjetilTanque, "m");
	print("Projetil acertou o tanque: ", mensagemProjetilAcertouTanque);
	print("");

# procMostraResultadoBalistivo(): procedimento que apresenta o resultado balistico
#	larguraScr - largura da matriz de tela
#	alturaScr - altura da matriz de tela
#	larguraMcs - largura maxima metrica
#	alturaMcs - altura maxima metrica
#	alturaMaximaDisparoMcs - altura maxima do disparo
#	distanciaPercorridaDisparoMcs - distancia percorrida pelo disparo
#	distanciaFinalTanqueMcs - distancia final do tanque
def procMostraResultadoBalistico(
	larguraScr,
	alturaScr,
	larguraMcs,
	alturaMcs,
	alturaMaximaDisparoMcs,
	distanciaPercorridaDisparoMcs,
	distanciaFinalTanqueMcs):

	# DEFINICAO_ESCALA
	escalaX = larguraScr / larguraMcs;
	escalaY = alturaScr / alturaMcs;

	dXMcs = 1.0 / escalaX;
	dYMcs = 1.0 / escalaY;

	alturaFinalScr = alturaScr + 2;
	larguraFinalScr = larguraScr + 2;

	# ESCALA_ELEMENTOS
	alturaMaximaDisparoScr = m.floor( alturaMaximaDisparoMcs * escalaY );
	distanciaPercorridaDisparoScr = m.floor( distanciaPercorridaDisparoMcs * escalaX );
	distanciaFinalTanqueScr = m.floor( distanciaFinalTanqueMcs * escalaX );

	meioDistanciaPercorridaDisparoMcs = distanciaPercorridaDisparoMcs / 2.0;

	meioDistanciaPercorridaDisparoScr = m.floor( meioDistanciaPercorridaDisparoMcs * escalaX );

	# IMPRIME_TELA
	yProjetilMcs = 0.0;
	for yScr in range(0, alturaFinalScr + 1):
		y = alturaFinalScr - yScr;

		linha = "";
		for xScr in range(0, larguraFinalScr + 1):
			x = xScr;

			if y == 0:
				linha = linha + "=";
			elif y == alturaScr:
				linha = linha + "=";
			elif y == 1:
				if x == 0:
					linha = linha + "M";
				elif x == distanciaPercorridaDisparoScr:
					linha = linha + "X";
				elif x == distanciaFinalTanqueScr:
					linha = linha + "T";
				else:
					linha = linha + " ";
			elif y == alturaMaximaDisparoScr:
				if x == meioDistanciaPercorridaDisparoScr:
					linha = linha + "O";
				else:
					linha = linha + " ";
			else:
				linha = linha + " ";
		print(linha);
	print("");

# CODIGO PRINCIPAL #

# procExecuta(): procedimento principal de execucao do jogo
def procExecuta():
	gVelocidadeInicialProjetil = funcVelocidadeInicialProjetil(DEF_VELOCIDADE_PROJETIL, DEF_VARIACAO_VELOCIDADE_PROJETIL);
	gVelocidadeInicialTanque = funcVelocidadeInicialTanque(DEF_VELOCIDADE_TANQUE, DEF_VARIACAO_VELOCIDADE_TANQUE);
	gDistanciaInicialTanque = funcDistanciaInicialTanque(DEF_DISTANCIA_TANQUE, DEF_VARIACAO_DISTANCIA_TANQUE);

	procMostraParametrosIniciais(gVelocidadeInicialProjetil, gVelocidadeInicialTanque, gDistanciaInicialTanque);

	n = 1;
	velocidadeTanque = gVelocidadeInicialTanque;
	distanciaTanque = gDistanciaInicialTanque;

	while( True ):
		procMostraDadosNovaTentativa(n, distanciaTanque);

		anguloGraus = funcLeEntradaAnguloGraus();

		velocidadeVerticalProjetil = funcVelocidadeVerticalInicialProjetil(gVelocidadeInicialProjetil, anguloGraus);
		velocidadeHorizontalProjetil = funcVelocidadeHorizontalInicialProjetil(gVelocidadeInicialProjetil, anguloGraus);

		alturaMaximaDisparo = funcAlturaMaximaProjetil(velocidadeVerticalProjetil, DEF_MASSA_PROJETIL, DEF_ACELERACAO_GRAVIDADE);

		tempoQuedaLivre = funcTempoQuedaLivre(alturaMaximaDisparo, DEF_ACELERACAO_GRAVIDADE);

		tempoTotalDisparo = 2.0 * tempoQuedaLivre;

		distanciaPercorridaDisparo = funcDistanciaPercorridaProjetil(velocidadeHorizontalProjetil, tempoTotalDisparo);

		distanciaPercorridaTanque = funcDistanciaPercorridaTanque(velocidadeTanque, tempoTotalDisparo);

		distanciaFinalTanque = distanciaTanque - distanciaPercorridaTanque;

		distanciaProjetilTanque = m.fabs( distanciaFinalTanque - distanciaPercorridaDisparo );

		bProjetilAcertouTanque = funcTestaProjetilAcertouTanque(distanciaPercorridaDisparo, distanciaFinalTanque, DEF_COMPRIMENTO_TANQUE);

		procMostraResultadoBalistico(
			80,
			20,
			100000,
			60000.0,
			alturaMaximaDisparo,
			distanciaPercorridaDisparo,
			distanciaFinalTanque);

		strProjetilAcertouTanque = "[ ERROU ]";
		if bProjetilAcertouTanque:
			strProjetilAcertouTanque = "[ ACERTOU ]";

		procMostraResultadoProcessamento(
			velocidadeVerticalProjetil,
			velocidadeHorizontalProjetil,
			velocidadeTanque,
			distanciaTanque,
			anguloGraus,
			alturaMaximaDisparo,
			tempoQuedaLivre,
			tempoTotalDisparo,
			distanciaPercorridaDisparo,
			distanciaPercorridaTanque,
			distanciaFinalTanque,
			distanciaProjetilTanque,
			strProjetilAcertouTanque);

		if distanciaFinalTanque < 0:
			print("VOCE PERDEU! O INIMIGO ATRAVESSOU A BARREIRA!");
			print("Distancia final do tanque: ", distanciaFinalTanque, "m");
			break;

		if bProjetilAcertouTanque:
			print("PARABENS, INIMIGO DESTRUIDO!");
			break;

		distanciaTanque = distanciaFinalTanque;
		n = n + 1;

	print("Processamento concluido!");

# EXECUCAO #

procCopyright();
procExecuta();
