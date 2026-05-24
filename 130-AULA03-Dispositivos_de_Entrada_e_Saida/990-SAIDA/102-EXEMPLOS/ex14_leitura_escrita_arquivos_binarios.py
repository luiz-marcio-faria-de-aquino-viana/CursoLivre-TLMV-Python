"""
Copyright (c) 2025-2026 TLMV Consultoria e Sistemas EIRELI.

ex14_leitura_escrita_arquivos_binarios.py
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

# DEFINICOES #

DEF_FILE_VARCHARSZ = 32;

DEF_BUFSZ = 128;

DEF_NOME_ARQUIVO = "./_DATASETS/20260524-CONTATOS.dat";

# CLASSES #

class Contato():

    def __init__(self, contatoId, nome, telefone, email):
        self.contatoId = contatoId;
        self.nome = nome;
        self.telefone = telefone;
        self.email = email;
        self.bNew = True;

    def show(self):
        print("================================================================================")
        print("");
        print("Codigo: ", self.contatoId);
        print("Nome: ", self.nome);
        print("Telefone: ", self.telefone);
        print("E-mail: ", self.email);
        print("");

    def fillRight(self, strVal, n, ch):
        strNewVal = strVal;
        szStrNewVal = len(strNewVal);

        diff = n - szStrNewVal;
        if(diff < 0):
            diff = 0;
            strNewVal = left(strNewVal, n);

        for i in range(0, diff):
            strNewVal = strNewVal + ch;
        return strNewVal;

    def save(self, f):
        if not self.bNew:
            return;

        strContatoId = str(self.contatoId);
        strNome = str(self.nome);
        strTelefone = str(self.telefone);
        strEmail = str(self.email);

        strContatoId = self.fillRight(str(self.contatoId), DEF_FILE_VARCHARSZ, " ");
        strNome = self.fillRight(self.nome, DEF_FILE_VARCHARSZ, " ");
        strTelefone = self.fillRight(self.telefone, DEF_FILE_VARCHARSZ, " ");
        strEmail = self.fillRight(self.email, DEF_FILE_VARCHARSZ, " ");

        strBuf = strContatoId + strNome + strTelefone + strEmail;
        strBufUtf8 = strBuf.encode('UTF-8');
        
        data = bytearray(strBufUtf8);
        szData = len(data);

        data = data.replace(b'\r', b' ');
        data = data.replace(b'\n', b' ');

        try:
            f.write(data);
            self.bNew = False;

            print("Registro: ", str(self.contatoId), " gravado com sucesso. TAM=", szData);

        except OSError as e:
            print("ERR: Falha na gravacao do registro: ", str(self.contatoId) );
            print(e);
        print("");

    def load(self, f):
        bResult = False;

        try:
            databuf = f.read(DEF_BUFSZ);
            if(databuf == None):
                return False;

            szDatabuf = len(databuf);
            if szDatabuf == 0:
                return False;

            posI = 0;
            posF = posI + DEF_FILE_VARCHARSZ;

            strContatoId = str(databuf[posI:posF], 'UTF-8');
            posI = posF;
            posF = posI + DEF_FILE_VARCHARSZ;

            strNome = str(databuf[posI:posF], 'UTF-8');
            posI = posF;
            posF = posI + DEF_FILE_VARCHARSZ;

            strTelefone = str(databuf[posI:posF], 'UTF-8');
            posI = posF;
            posF = posI + DEF_FILE_VARCHARSZ;

            strEmail = str(databuf[posI:posF], 'UTF-8');
            posI = posF;
            posF = posI + DEF_FILE_VARCHARSZ;

            self.contatoId = int(strContatoId);
            self.nome = strNome;
            self.telefone = strTelefone;
            self.email = strEmail;

            print("Registro: ", str(self.contatoId), " lido com sucesso. TAM=", szDatabuf);

            bResult = True;

        except OSError as e:
            print("ERR: Falha na leitura do registro.");
            print(e);
        print("");

        return bResult;

    # Getters/Setters */

    def getContatoId(self):
        return self.contatoId;

    def setContatoId(self, contatoId):
        self.contatoId = contatoId;
        self.bNew = True;

    def getNome(self):
        return self.nome;

    def setNome(self, nome):
        self.nome = nome;
        self.bNew = True;

    def getTelefone(self):
        return self.telefone;

    def setTelefone(self, telefone):
        self.telefone = telefone;
        self.bNew = True;

    def getEmail(self):
        return self.email;

    def setEmail(self, email):
        self.email = email;
        self.bNew = True;

    def isNew(self):
        return self.bNew;

# METODOS #

def procWriteFile(nomeArquivo, lsContato):
    print("=> procWriteFile()" + "\n");

    try:
        f = open(nomeArquivo, 'w+b');
        
        szLsContato = len(lsContato);
        for i in range(0, szLsContato):
            oContato = lsContato[i];
            if not oContato.isNew():
                continue;

            oContato = lsContato[i];
            oContato.save(f);

        f.flush();
        f.close();

        print("Arquivo gravado com sucesso!\n");

    except OSError as e:
        print("ERR: Falha na gravacao do arquivo.");
        print(e);

    print("\n");

def procReadFile(nomeArquivo):
    print("=> procReadFile()" + "\n");

    lsContato = [];

    try:
        f = open(nomeArquivo, 'r+b');

        while True:
            oContato = Contato(-1, "", "", "");

            bResult = oContato.load(f);
            if not bResult:
                break;
            lsContato.append(oContato);

        f.flush();
        f.close();

        print("Arquivo lido com sucesso!\n");

    except OSError as e:
        print("ERR: Falha na leitura do arquivo.");
        print(e);
    print("\n");

    return lsContato;

def procWriteRecordAt(nomeArquivo, numreg, oContato):
    print("=> procWriteRecordAt()" + "\n");

    try:
        print("Gravando registro: ", numreg);

        filepos = numreg * DEF_BUFSZ;

        f = open(nomeArquivo, 'r+b');
        f.seek(filepos);
        oContato.save(f);
        f.flush();
        f.close();

        print("Registro gravado com sucesso!\n");

    except OSError as e:
        print("ERR: Falha na gravacao do registro.");
        print(e);

    print("\n");

def procReadRecordAt(nomeArquivo, numreg):
    print("=> procReadRegistroAt()" + "\n");

    oContato = None;

    try:
        print("Gravando registro: ", numreg);

        filepos = numreg * DEF_BUFSZ;

        f = open(nomeArquivo, 'r+b');
        f.seek(filepos);
        oContato = Contato(-1, "", "", "");
        oContato.load(f);
        f.close();

        print("Registro lido com sucesso!\n");

    except OSError as e:
        print("ERR: Falha na leitura do registro.");
        print(e);
    print("\n");

    return oContato;

def procShowAll(lsContato):
    print("=> procShowAll()" + "\n");

    for oContato in lsContato:
        oContato.show();
    print("");

def recursos():
    print('RECURSOS:');
    print('=========');
    print('procWriteFile()');
    print('procReadFile()');
    print('procWriteRecordAt()');
    print('procReadRecordAt()');
    print('procShowAll()');
    print('');

def executaTudo():
    print('EXECUTA:');
    print('========');
    print('');

    lsContato = [
        Contato(1001, "Joao",       "(21)2222-2221", "joao@test.com"),
        Contato(1002, "Jose",       "(21)2222-2222", "jose@test.com"),
        Contato(1003, "Isaac",      "(21)2222-2223", "isaac@test.com"),
        Contato(1004, "Jacob",      "(21)2222-2224", "jacob@test.com"),
        Contato(1005, "Israel",     "(21)2222-2225", "israel@test.com"),
        Contato(1006, "Tiago",      "(21)2222-2226", "tiago@test.com"),
        Contato(1007, "Miguel",     "(21)2222-2227", "miguel@test.com"),
        Contato(1008, "Francisco",  "(21)2222-2228", "francisco@test.com"),
        Contato(1009, "Simao",      "(21)2222-2229", "simao@test.com"),
        Contato(1010, "Jeremias",   "(21)2222-2230", "jeremias@test.com") ];

    procWriteFile(DEF_NOME_ARQUIVO, lsContato);

    lsNewContato1 = procReadFile(DEF_NOME_ARQUIVO);
    procShowAll(lsNewContato1);

    oContato = procReadRecordAt(DEF_NOME_ARQUIVO, 5);
    if oContato != None:
        oContato.show();
    print("");

    oContato.setNome("Joaozinho");
    oContato.setTelefone("(21)3333-3331");
    oContato.setEmail("joaozinho@test.com");

    procWriteRecordAt(DEF_NOME_ARQUIVO, 5, oContato);
    print("");

    lsNewContato2 = procReadFile(DEF_NOME_ARQUIVO);
    procShowAll(lsNewContato2);
    print("");

def carregado():
    print('Arquivo: ex14_leitura_escrita_arquivos_binarios.py... carregado!');
    print('');

carregado();
recursos();
executaTudo();
