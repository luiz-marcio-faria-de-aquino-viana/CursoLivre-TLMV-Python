"""
Copyright (c) 2025-2026 TLMV Consultoria e Sistemas EIRELI.

ex11_cliente_rede.py
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

# RESULT_CODES
#
RSERR = -1;
RSOK = 0;

# SERVER/CLIENT DEFINITIONS
#
DEF_LOCALADDRESS = '127.0.0.1';

DEF_CLIENTTARGETADDRESS = '127.0.0.1';
DEF_CLIENTTARGETPORT = 9191;

DEF_CLIENTRECVADDRESS = '0.0.0.0';
DEF_CLIENTRECVPORT = 9192;

DEF_SERVERTERMMSG = '\\.';
DEF_SERVERTERMMSGLEN = 2;

DEF_MAX_NUM_SESSION = 512;

DEF_SESSION_TIMEOUT = 1200;                  # 20 minutes = 1200 seconds

DEF_DEBUGMODE_SLEEPTIME = 3;                 # 3 seconds

# BUFFER SIZE
#
DEF_REQBUFSIZE = 4096;
DEF_RESPBUFSIZE = 4096;
DEF_BUFSZ = 4096;

# NULL VALUES
#
DEF_NULL_INT = -1;
DEF_NULL_INTSTR = "-1";
DEF_NULL_STR = "";

# SEPARATOR
#
DEF_SEP = "^";

# ACOES (TEXTOS)
#
DEF_REQ_ACTION_GET = 'get';
DEF_REQ_ACTION_LISTALL = 'listall';

# ACOES (VALOR)
#
DEF_REQ_ACTIONVAL_GET = 1;
DEF_REQ_ACTIONVAL_LISTALL = 2;

# PARAMETROS
#
# GET
DEF_PARAM_GET_SESSION = 'session'
DEF_PARAM_GET_OID = 'oid';
# LISTALL
DEF_PARAM_LISTALL_SESSION = 'session'

# COMMANDS
#
DEF_CMD_GET_QUESTION = 'get^question^[oid]^[session]';
DEF_CMD_LISTALL_QUESTIONS = 'listall^question^[session]';

# OBJTYPE
#
DEF_REQ_OBJTYPE_QUESTION = "question";

# SERVIDOR_REDE
class ClienteRede(th.Thread):
    
    def __init__(self):
        th.Thread.__init__(self);
        # input socket
        self.inaddr = DEF_CLIENTRECVADDRESS;
        self.inport = DEF_CLIENTRECVPORT;
        self.inSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP);
        self.inSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1);
        # output socket
        self.outaddr = DEF_CLIENTTARGETADDRESS;
        self.outport = DEF_CLIENTTARGETPORT;
        self.outSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP);
        self.outSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1);
        # session data
        self.session = DEF_NULL_INTSTR;
        # request id
        self.reqnum = 0;
        # connection opened flag
        self.isConnected = False;
        # monitor thread
        self.monitorThread = None;
        self.isMonitorRunning = False;

    # run(): funcao do loop de mensagens com o servidor de imagens
    def run(self):
        try:
            self.isMonitorRunning = True;
            self.lsMessage = [];
            
            addr = (self.inaddr, self.inport);
            print('RemoteAddr: ', addr);

            self.inSocket.bind(addr);
    
            while(self.isMonitorRunning == True):
                t.sleep(DEF_DEBUGMODE_SLEEPTIME);
    
                data = self.inSocket.recvfrom(DEF_BUFSZ);
                
                dataStr = data[0].decode('UTF-8');
                inaddr = data[1];
                print("InAddr: ", inaddr);

                message = [ dataStr, inaddr ];
                self.processMessage(message);
          
        except OSError as e:
            self.inSocket.close();
            self.inSocket = None;
            self.isConnected = False;
            print(e);
    
    # processMessage(): funcao que processa mensagem recebida
    # message - mensagem recebida
    # retorno: arquivo XML com o resultado
    def processMessage(self, message):
        dataStr = message[0];
        inaddr = message[1];

        print("RECV_MESSAGE:");
        print("=============");
        print(dataStr);
        print("");

        pos = dataStr.find(DEF_SERVERTERMMSG);
        if pos != -1:
            print("Servidor Terminado!");
            quit();
        return RSOK;

    # startMessageLoop(): funcao que inicia o loop de mensagens
    # retorno: RSCODE
    def startMessageLoop(self):
        if not self.isMonitorRunning:
            # monitor thread
            self.start();
            return RSOK;
        return RSERR;
        
    # stopMessageLoop(): funcao que termina o loop de mensagens
    # retorno: RSCODE
    def stopMessageLoop(self):
        self.isMonitorRunning = False;
        self.join();
        return RSOK;
    
    # sendLocalMessage(): funcao que envia mensagem
    # retorno: RSCODE
    def sendLocalMessage(self, cmd):
        try:
            localaddr = DEF_LOCALADDRESS;
            addr = (localaddr, self.inport);
            print('LocalAddr: ', addr, 'Data: ', cmd);         

            cmdUtf8 = cmd.encode('UTF-8');   
            data = bytearray(cmdUtf8);
            self.outSocket.sendto(data, addr);
            return RSOK;
        
        except OSError as e:
            self.outSocket.close();
            self.outSocket = None;
            self.isConnected = False;
            print(e);

        return RSERR;
    
    # sendMessage(): funcao que envia mensagem
    # retorno: RSCODE
    def sendMessage(self, cmd):
        try:
            addr = (self.outaddr, self.outport);
            print('RemoteAddr: ', addr, 'Data: ', cmd);         

            cmdUtf8 = cmd.encode('UTF-8');   
            data = bytearray(cmdUtf8);
            self.outSocket.sendto(data, addr);
            return RSOK;
        
        except OSError as e:
            self.outSocket.close();
            self.outSocket = None;
            self.isConnected = False;
            print(e);

        return RSERR;
        
    # localServerTerminate(): funcao que envia mensagem de termino ao servidor local
    # retorno: RSCODE
    def localServerTerminate(self):
        rscode = RSERR;
        
        cmd = DEF_SERVERTERMMSG;
        rscode = self.sendLocalMessage(cmd);
        if rscode == RSOK:
            self.isConnected = False;
        return rscode;
        
    # serverTerminate(): funcao que envia mensagem de termino
    # retorno: RSCODE
    def serverTerminate(self):
        rscode = RSERR;
        
        cmd = DEF_SERVERTERMMSG;
        rscode = self.sendMessage(cmd);
        if rscode == RSOK:
            self.isConnected = False;
        return rscode;
        
    # listAllQuestions(): funcao que obtem a lista de questoes do banco de dados
    # retorno: arquivo XML com a lista de usuarios
    def listAllQuestions(self):
        rscode = RSERR;
        
        cmd = DEF_REQ_ACTION_LISTALL + DEF_SEP + DEF_REQ_OBJTYPE_QUESTION + DEF_SEP + self.session;
        rscode = self.sendMessage(cmd);
        return rscode;
        
    # getQuestionAt(): funcao que retorna uma questao do banco de dados
    # pos - posicao da questao no banco de dados
    # retorno: arquivo XML com a lista das tabelas
    def getQuestionAt(self, pos):
        rscode = RSERR;
        
        cmd = DEF_REQ_ACTION_GET + DEF_SEP + DEF_REQ_OBJTYPE_QUESTION + DEF_SEP + str(pos) + DEF_SEP + self.session;
        rscode = self.sendMessage(cmd);
        return rscode;        

# UTILITARIOS #

# funcLeEntradaTeclado(): funcao que apresenta uma mensagem e espera a digitacao de um texto
# mensagem - mensagem a ser apresentada na tela
def funcLeEntradaTeclado(mensagem):
	print(mensagem);

	f = open("/dev/stdin", 'r');
	texto = f.readline(4096);
	f.close();
	return texto;

# MENSAGENS #

# procCopyright(): procedimento que apresenta informacoes sobre o jogo
def procCopyright():
	print("Cliente Rede");
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
    cliente = ClienteRede();
    cliente.startMessageLoop();

    print("REQUEST_QUESTION(0)");
    print("===================");
    cliente.getQuestionAt(0);
    print("");

    funcLeEntradaTeclado("Tecle [ENTER] para prosseguir... ");

    print("LISTALL_QUESTIONS");
    print("=================");
    cliente.listAllQuestions();
    print("");
    
    funcLeEntradaTeclado("Tecle [ENTER] para prosseguir... ");
    cliente.serverTerminate();
    cliente.localServerTerminate();

    print("Tchau!");
    print("");

    quit();

# EXECUCAO #

procCopyright();
procExecuta();
