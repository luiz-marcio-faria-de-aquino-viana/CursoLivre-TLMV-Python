"""
Copyright (c) 2025-2026 TLMV Consultoria e Sistemas EIRELI.

ex12_excecoes.py
Autor: 
Luiz Marcio Faria de Aquino Viana, Pos-D.Sc. - Engenheiro, 07/05/2026
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

EXCEPTION_ENABLED = True;

DEF_CLIENTTARGETADDRESS = '127.0.0.1';
DEF_CLIENTTARGETPORT = 9191;

# METODOS #

# DIV0
#
def procDiv0(val):
    print('=> procDiv0()');

    result = val / 0.0;
    print(result);

def procDiv0_except(val):
    print('=> procDiv0()');

    try:
        result = val / 0.0;
    except:
        result = 0.0;
    print(result);

# I/O ERROR
#
def procOSError():
    print('=> procOSError()');

    f = open("arquivo.inexistente.txt", 'r');
    texto = f.readline(4096);
    f.close();

    print(texto);

def procOSError_except():
    print('=> procOSError()');

    try:
        f = open("arquivo.inexistente.txt", 'r');
        texto = f.readline(4096);
        f.close();

    except OSError as e:
        texto = "ERR: Falha na leitura do arquivo.";
        print(e);

    print(texto);

# NET ERROR
#
def procNetError():
    print('=> procNetError()');

    texto = "Hello, world!";

    outaddr = DEF_CLIENTTARGETADDRESS;
    outport = DEF_CLIENTTARGETPORT;

    outSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP);
    outSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1);

    addr = (outaddr, outport);

    textoUtf8 = texto.encode('UTF-8');
    data = bytearray(textoUtf8);
    outSocket.sendto(data, addr);

    outSocket.close();
    outSocket = None;

    print(texto);

def procNetError_except():
    print('=> procNetError()');

    texto = "Hello, world!";

    outaddr = DEF_CLIENTTARGETADDRESS;
    outport = DEF_CLIENTTARGETPORT;

    outSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP);
    outSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1);

    try:
        addr = (outaddr, outport);

        textoUtf8 = texto.encode('UTF-8');
        data = bytearray(textoUtf8);
        outSocket.sendto(data, addr);

    except OSError as e:
        print(e);

    finally:
        outSocket.close();
        outSocket = None;

    print(texto);

def recursos():
    print('RECURSOS:');
    print('=========');
    print('procDiv0()');
    print('procOSError()');
    print('procNetError()');
    print('');

def executaTudo():
    print('EXECUTA:');
    print('========');
    print('');

    if EXCEPTION_ENABLED:
        procDiv0_except(100.0);
        procOSError_except();
        procNetError_except();
    else:
        #procDiv0(100.0);
        #procOSError();
        procNetError();

def carregado():
    print('Arquivo: ex12_excecoes.py... carregado!');
    print('');

carregado();
recursos();
executaTudo();
