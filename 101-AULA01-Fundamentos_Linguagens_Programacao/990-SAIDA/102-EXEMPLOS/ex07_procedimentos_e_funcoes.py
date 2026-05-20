"""
Copyright (c) 2025-2026 TLMV Consultoria e Sistemas EIRELI.

ex07_procedimentos_e_funcoes.py
Autor: 
Luiz Marcio Faria de Aquino Viana, Pos-D.Sc. - Engenheiro, 28/04/2026
Unidade: Universidade do Estado do Rio de Janeiro
Curso: Engenharia Eletrica, Enfase em Engenharia de Sistemas e Computacao
Unico Socio e Administrador da Empresa - Desde: 02/08/2000

Revisoes: ...
"""

# PROCEDIMENTO
def procDiferencaIdade(idadeJoao, idadePai):
	diferencaIdade = idadePai - idadeJoao;	# variavel armazena a diferenca entre as idades do pai de joao e joao
	print(diferencaIdade);			# funcao que imprime a diferenca de idades

def procValorRecobrimentoAmbiente(valorAzulejo, larguraAmbiente, comprimentoAmbiente):
	areaAmbiente = larguraAmbiente * comprimentoAmbiente;		# area do ambiente em metro quadrado
	valorTotal = valorAzulejo * areaAmbiente;			# valor total de recobrimento do ambiente
	print(valorTotal);
	
# FUNCOES
def funcDiferencaIdade(idadeJoao, idadePai):
	diferencaIdade = idadePai - idadeJoao;	# variavel armazena a diferenca entre as idades do pai de joao e joao
	return(diferencaIdade);

def funcValorRecobrimentoAmbiente(valorAzulejo, larguraAmbiente, comprimentoAmbiente):
	areaAmbiente = larguraAmbiente * comprimentoAmbiente;		# area do ambiente em metro quadrado
	valorTotal = valorAzulejo * areaAmbiente;			# valor total de recobrimento do ambiente
	return(valorTotal);

# FUNCOES RECURSIVAS
def funcFibonaci(n):
	if(n == 0): 
		return(0);

	if(n == 1): 
		return(1);

	valorN = funcFibonaci(n - 2) + funcFibonaci(n - 1);	
	return(valorN);

def funcFatorial(n):
	if(n == 0): 
		return(1);

	valorN = n * funcFatorial(n - 1);	
	return(valorN);

def recursos():
	print('RECURSOS:');
	print('=========');
	print('procDiferencaIdade()');
	print('procValorRecobrimentoAmbiente()');
	print('funcDiferencaIdade()');
	print('funcValorRecobrimentoAmbiente()');
	print('funcFibonaci()');
	print('funcFatorial()');
	print('');

def executaTudo():
	print('EXECUTA:');
	print('========');
	print('');

	print('Executa: procDiferencaIdade()');
	procDiferencaIdade(10, 37);
	print('');

	print('Executa: procValorRecobrimentoAmbiente()');
	procValorRecobrimentoAmbiente(22.5, 3.0, 6.0);
	print('');

	print('Executa: funcDiferencaIdade()');
	diferencaIdade = funcDiferencaIdade(10, 37);
	print('Diferenca de idade:', diferencaIdade);
	print('');

	print('Executa: funcValorRecobrimentoAmbiente()');
	valorRecobrimento = funcValorRecobrimentoAmbiente(22.5, 3.0, 6.0);
	print('Valor para recobrimento da area com azulejo:', valorRecobrimento);
	print('');

	print('Executa: funcFibonaci()');
	sequencia = funcFibonaci(10);
	print('Sequencia de Fibonaci de 10:', sequencia);
	print('');

	print('Executa: funcFatorial()');
	fatorial = funcFatorial(10);
	print('Fatorial de 10:', fatorial);

def carregado():
	print('Arquivo: ex07_procedimentos_e_funcoes.py... carregado!');
	print('');

