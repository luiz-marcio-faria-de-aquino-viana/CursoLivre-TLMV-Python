"""
Copyright (c) 2025-2026 TLMV Consultoria e Sistemas EIRELI.

ex13_leitura_escrita_arquivos_textuais.py
Autor: 
Luiz Marcio Faria de Aquino Viana, Pos-D.Sc. - Engenheiro, 23/05/2026
Unidade: Universidade do Estado do Rio de Janeiro
Curso: Engenharia Eletrica, Enfase em Engenharia de Sistemas e Computacao
Unico Socio e Administrador da Empresa - Desde: 02/08/2000

Revisoes: ...
"""

import sys as s
import time as t
import threading as th
import socket as socket

# DEFINICOES #

DEF_NOME_ARQUIVO = "./_DATASETS/20260523-TEXTO_COPYRIGHT.txt";

DEF_TEXTO_1 = """
/*
 * Copyright (C) 2000-2022 TLMV CONSULTORIA E SISTEMAS EIRELI
 *
 * Autor: 
 *   Luiz Marcio Faria de Aquino Viana, Pos-D.Sc. - Engenheiro
 *   Registro: 20001035871 CREA-RJ
 *
 *   Graduacao: Engenharia Eletrica
 *   Unidade: UERJ - Universidade do Estado do Rio de Janeiro
 *   Curso: Engenharia Eletrica com Enfase em Engenharia de Sistemas e Computação
 *
 *   Mestrado/Doutorado/Pos-Doutoramento: Programa de Engenharia de Sistemas e Computacao - PESC
 *   Unidade: COPPE/UFRJ - Universidade Federal do Rio de Janeiro
 *   Area: Arquitetura de Computadores e Sistemas Operacionais
 *
 *   Unico Socio e Administrador da Empresa - Desde: 02/08/2000
 *
 */
""";

DEF_TEXTO_2 = """

#include<stdio.h>

int main(int argc, char** argv)
{
    printf("Hello, World!");
    return(0);
}

""";

# METODOS #

def procWriteFile(nomeArquivo, texto):
    print("=> procWriteFile()" + "\n");

    try:
        f = open(nomeArquivo, 'w');
        f.write(texto);
        f.flush();
        f.close();

        print("Arquivo gravado com sucesso!\n");
    except OSError as e:
        print("ERR: Falha na escrita do arquivo.");
        print(e);

    print("\n");

def procAppendFile(nomeArquivo, texto):
    print("=> procAppendFile()" + "\n");

    try:
        f = open(nomeArquivo, 'a');
        f.write(texto);
        f.flush();
        f.close();

        print("Arquivo atualizado com sucesso!\n");
    except OSError as e:
        print("ERR: Falha na atualizacao do arquivo.");
        print(e);

    print("\n");

def procReadFile(nomeArquivo):
    print("=> procReadFile()" + "\n");

    try:
        f = open(nomeArquivo, 'r');
        texto = f.read(8192);
        f.close();

        print("Arquivo lido com sucesso!\n");
        print(texto + "\n");
    except OSError as e:
        texto = "ERR: Falha na leitura do arquivo.";
        print(e);

    print("\n");

def recursos():
    print('RECURSOS:');
    print('=========');
    print('procWriteFile()');
    print('procAppendFile()');
    print('procReadFile()');
    print('');

def executaTudo():
    print('EXECUTA:');
    print('========');
    print('');

    procWriteFile(DEF_NOME_ARQUIVO, DEF_TEXTO_1);
    procReadFile(DEF_NOME_ARQUIVO);

    procAppendFile(DEF_NOME_ARQUIVO, DEF_TEXTO_2);
    procReadFile(DEF_NOME_ARQUIVO);

def carregado():
    print('Arquivo: ex13_leitura_escrita_arquivos_textuais.py... carregado!');
    print('');

carregado();
recursos();
executaTudo();
