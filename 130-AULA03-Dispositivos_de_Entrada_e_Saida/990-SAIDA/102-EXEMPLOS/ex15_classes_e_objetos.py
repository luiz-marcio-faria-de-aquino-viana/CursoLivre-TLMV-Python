"""
Copyright (c) 2025-2026 TLMV Consultoria e Sistemas EIRELI.

ex15_classes_e_objetos.py
Autor: 
Luiz Marcio Faria de Aquino Viana, Pos-D.Sc. - Engenheiro, 24/05/2026
Unidade: Universidade do Estado do Rio de Janeiro
Curso: Engenharia Eletrica, Enfase em Engenharia de Sistemas e Computacao
Unico Socio e Administrador da Empresa - Desde: 02/08/2000

Revisoes: ...
"""

import sys as s
import time as t
import threading as th
import socket as socket

# HIERARQUIA DE CLASSES #

class Documento():

    def __init__(self):
        self.documentoId = -1;
        self.autor = "";
        self.dataDeChegada = "";

    def initDocumento(self, documentoId, autor, dataDeChegada):
        self.documentoId = documentoId;
        self.autor = autor;
        self.dataDeChegada = dataDeChegada;

    def imprimirDocumento(self):
        print("================================================================================")
        print("");
        print("Codigo: ", self.documentoId);
        print("Autor: ", self.autor);
        print("Data de chegada: ", self.dataDeChegada);
        print("");

    def editarDocumento(self, autor, dataDeChegada):
        self.autor = autor;
        self.dataDeChegada = dataDeChegada;

    # Getters/Setters */

    def getAutor(self):
        return self.autor;

    def getDataDeChegada(self):
        return self.dataDeChegada;

class Carta(Documento):

    def __init__(self, documentoId, autor, dataDeChegada):
        self.initDocumento(documentoId, autor, dataDeChegada);
        self.transporte = "";
        self.carta = "";

    def anexarCarta(self, transporte, carta):
        self.transporte = transporte;
        self.carta = carta;

    def imprimirCarta(self):
        self.imprimirDocumento();

        print("Transporte: ", self.transporte);
        print("Carta: ", self.carta);
        print("");

    # Getters/Setters */

    def getTransporte(self):
        return self.transporte;

    def getCarta(self):
        return self.carta;

class Telegrama(Documento):

    def __init__(self, documentoId, autor, dataDeChegada):
        self.initDocumento(documentoId, autor, dataDeChegada);

        self.valorPorCaracter = 0.5;
        self.dataHora = "";
        self.mensagem = "";
        self.valor = 0.0;
        self.bPago = False;

    def registrarTelegrama(self, dataHora, mensagem):
        self.dataHora = dataHora;
        self.mensagem = mensagem;

    def pagarTelegrama(self):
        self.valor = len(self.mensagem) * valorPorCaracter;
        self.bPago = True;

    def imprimirTelegrama(self):
        self.imprimirDocumento();

        print("Data e hora: ", self.dataHora);
        print("Mensagem: ", self.mensagem);
        print("Valor: ", self.valor);

        if self.bPago:
            print("Pago? SIM");
        else:
            print("Pago? NAO");

    # Getters/Setters */

    def getHora(self):
        return self.hora;

    def getMensagem(self):
        return self.mensagem;

    def getValor(self):
        return self.valor;

    def getPago(self):
        return self.bPago;

# PROCEDIMENTOS #

def procAnexarCarta(lsCarta, pos, strTransporte, strCarta):
    szLsCarta = len(lsCarta);
    if pos < szLsCarta:
        oCarta = lsCarta[pos];
        oCarta.anexarCarta(strTransporte, strCarta);

def procRegistrarTelegrama(lsTelegrama, pos, strDataHora, strMensagem):
    szLsTelegrama = len(lsTelegrama);
    if pos < szLsTelegrama:
        oTelegrama = lsTelegrama[pos];
        oTelegrama.registrarTelegrama(strDataHora, strMensagem);

def procPagarTelegrama(lsTelegrama, pos):
    szLsTelegrama = len(lsTelegrama);
    if pos < szLsTelegrama:
        oTelegrama = lsTelegrama[pos];
        oTelegrama.pagarTelegrama();

def procShowAllDocumento(lsDocumento):
    print("=== LISTAGEM DE DOCUMENTOS:");

    for oDocumento in lsDocumento:
        oDocumento.imprimirDocumento();

def procShowAllCarta(lsCarta):
    print("=== LISTAGEM DE CARTAS:");

    for oCarta in lsCarta:
        oCarta.imprimirCarta();

def procShowAllTelegrama(lsTelegrama):
    print("=== LISTAGEM DE TELEGRAMAS:");

    for oTelegrama in lsTelegrama:
        oTelegrama.imprimirTelegrama();

def recursos():
    print('RECURSOS:');
    print('=========');
    print('procAnexarCarta()');
    print('procRegistrarTelegrama()');
    print('procPagarTelegrama()');
    print('procShowAllDocumento()');
    print('procShowAllCarta()');
    print('procShowAllTelegrama()');
    print('');

def executaTudo():
    print('EXECUTA:');
    print('========');
    print('');

    # CARTA #

    lsCarta = [
        Carta(1001, "Joao",       "10/06/2026"),
        Carta(1002, "Jose",       "15/06/2026"),
        Carta(1003, "Isaac",      "20/06/2026"),
        Carta(1004, "Jacob",      "25/06/2026"),
        Carta(1005, "Israel",     "10/07/2026"),
        Carta(1006, "Tiago",      "15/07/2026"),
        Carta(1007, "Miguel",     "20/07/2026"),
        Carta(1008, "Francisco",  "25/07/2026"),
        Carta(1009, "Simao",      "10/08/2026"),
        Carta(1010, "Jeremias",   "15/08/2026") ];

    procAnexarCarta(lsCarta, 3, "aviao", "#3. Hello, World!");
    procAnexarCarta(lsCarta, 4, "caminhao", "#4. Hello, World!");
    procAnexarCarta(lsCarta, 8, "caminhao", "#8. Hello, World!");

    procShowAllCarta(lsCarta);

    # TELEGRAMA #

    lsTelegrama = [
        Telegrama(2001, "Joao",       "01/06/2026"),
        Telegrama(2002, "Jose",       "05/06/2026"),
        Telegrama(2003, "Isaac",      "09/06/2026"),
        Telegrama(2004, "Jacob",      "01/06/2026"),
        Telegrama(2005, "Israel",     "05/07/2026"),
        Telegrama(2006, "Tiago",      "09/07/2026"),
        Telegrama(2007, "Miguel",     "01/07/2026"),
        Telegrama(2008, "Francisco",  "05/07/2026"),
        Telegrama(2009, "Simao",      "09/08/2026"),
        Telegrama(2010, "Jeremias",   "01/08/2026") ];

    procRegistrarTelegrama(lsTelegrama, 3, "09/06/2026 10:30:00", "#3. Hello, World! Again!");
    procRegistrarTelegrama(lsTelegrama, 4, "05/07/2026 11:30:00", "#4. Hello, World! Again!");
    procRegistrarTelegrama(lsTelegrama, 8, "09/08/2026 12:30:00", "#8. Hello, World! Again!");

    procShowAllTelegrama(lsTelegrama);

    # DOCUMENTO #

    procShowAllDocumento(lsCarta);
    procShowAllDocumento(lsTelegrama);

    print("");

def carregado():
    print('Arquivo: ex15_classes_e_objetos.py... carregado!');
    print('');

carregado();
recursos();
executaTudo();
