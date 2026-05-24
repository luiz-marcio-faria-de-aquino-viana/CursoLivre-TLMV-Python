"""
Copyright (c) 2025-2026 TLMV Consultoria e Sistemas EIRELI.

ex16_simple_HTTP_server.py
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

from http import HTTPStatus as httpstatus;
from http import server as httpsrv;

# DEFINICOES #

DEF_SERVERADDRESS = '0.0.0.0';
DEF_SERVERPORT = 9191;

DEF_SERVICENAME_TABUADA = "Tabuada";

DEF_COMMANDNAME_COPYRIGHT = "copyright";
DEF_COMMANDNAME_LISTALL = "listall";
DEF_COMMANDNAME_LIST = "list";

# CLASSES #

class RequestCommand():

    def __init__(self, requestStr):
        self.serviceName = "";
        self.commandName = "";
        self.commandParam = "";

        self.parse(requestStr);

    def parse(self, requestStr):
        arr1 = requestStr.split("/");

        szArr1 = len(arr1);
        if szArr1 >= 2:
            self.serviceName = arr1[1];
            if szArr1 >= 3:
                self.commandName = arr1[2];
                if szArr1 >= 4:
                    self.commandParam = arr1[3];

    def debug(self):
        print("ServiceName: ", self.serviceName);
        print("CommandName: ", self.commandName);
        print("CommandParam: ", self.commandParam);

    # Getters/Setters #

    def getServiceName(self):
        return self.serviceName;

    def getCommandName(self):
        return self.commandName;

    def getCommandParam(self):
        return self.commandParam;

class RequestHandler(httpsrv.SimpleHTTPRequestHandler):

    def conteudo(self, val):
        mensagem = "<table><tr><td>Operacao</td><td>Resultado</td></tr>";
        for i in range(2, 10):
            valMult = val * i;
            mensagem = mensagem + "<tr><td>" + str(val) + " x " + str(i) + "</td><td>" + str(valMult) + "</td></tr>";
        mensagem = mensagem + "</table>";
        return mensagem;

    def copyright(self):
        mensagem = """
            <html>
            <body>
            
            <h1>Copyright (c) 2025-2026 TLMV Consultoria e Sistemas EIRELI.</h1>
            
            <br/>
            
            <p>
            Autor: Luiz Marcio Faria de Aquino Viana, Pos-D.Sc. - Engenheiro, 24/05/2026<br/>
            Unidade: Universidade do Estado do Rio de Janeiro<br/>
            Curso: Engenharia Eletrica, Enfase em Engenharia de Sistemas e Computacao<br/>
            Unico Socio e Administrador da Empresa - Desde: 02/08/2000<br/>
            </p>
            
            </body>
            
            </html>
            """
        return mensagem;

    def list(self, val):
        strTitulo = "TABOADA DE " + str(val);
        strConteudo = self.conteudo(val);
        mensagem = "<html><body><h1>" + strTitulo + "</h1><br/>" + strConteudo + "</body></html>";
        return mensagem;

    def listall(self):
        mensagem = "<html><body>";
        for j in range(2, 10):
            strTitulo = "TABOADA DE " + str(j);
            strConteudo = self.conteudo(j);
            mensagem = mensagem + "<h1>" + strTitulo + "</h1><br/>" + strConteudo + "<br/><br/>";
        mensagem = mensagem + "</body></html>";
        return mensagem;

    def do_GET(self):
        requestStr = self.path;
        print(requestStr);

        cmd = RequestCommand(requestStr);
        cmd.debug();

        mensagem = "<html><body><h1>Hello, world!</h1></body></html>";

        if cmd.getServiceName() == DEF_SERVICENAME_TABUADA:
            if cmd.getCommandName() == DEF_COMMANDNAME_COPYRIGHT:
                mensagem = self.copyright();
            elif cmd.getCommandName() == DEF_COMMANDNAME_LISTALL:
                mensagem = self.listall();
            elif cmd.getCommandName() == DEF_COMMANDNAME_LIST:
                val = int(cmd.getCommandParam());
                mensagem = self.list(val);

        szMensagem = len(mensagem);

        print("Resposta: ", mensagem);

        self.send_response(httpstatus.OK);
        self.send_header("content-type", "text/html");
        self.send_header("content-length", str(szMensagem));
        self.end_headers();
        self.wfile.write(mensagem.encode("UTF-8"));

class HttpServer():

    def __init__(self, addr):
        print('ServerAddr: ', addr);
        self.httpServer = httpsrv.HTTPServer(addr, RequestHandler, True);

    def start(self):
        self.httpServer.serve_forever();

    def stop(self):
        self.httpServer.shutdown();

# PROCEDIMENTOS #

# funcLeEntradaTeclado(): funcao que apresenta uma mensagem e espera a digitacao de um texto
# mensagem - mensagem a ser apresentada na tela
def funcLeEntradaTeclado(mensagem):
	print(mensagem);

	f = open("/dev/stdin", 'r');
	texto = f.readline(4096);
	f.close();
	return texto;

# funcLeEntradaTexto(): funcao que apresenta uma mensagem e espera a digitacao de um texto
# mensagem - mensagem a ser apresentada na tela
# bAceitaNulo - aceita valores nulos
def funcLeEntradaTexto(mensagem, bAceitaNulo):
	texto = "";
	while True:
		texto = funcLeEntradaTeclado(mensagem);
		texto = funcFiltraEntrada(texto, DEF_CARACTERVALIDO_TEXTO);
		if texto != "":
			break;
		else:
			if bAceitaNulo:
				print("Valor nulo.");
				return None;
			else:
				print("ERR: Valor nulo nao e valido.");

	print("Texto informado: ", texto);
	return texto;

# procInitHttpServer(): procedimento que inicializa o servidor HTTP
def procInitHttpServer():
    inaddr = DEF_SERVERADDRESS;
    inport = DEF_SERVERPORT;

    addr = (inaddr, inport);

    localServer = HttpServer(addr);
    localServer.start();

    funcLeEntradaTexto("PRESSIONE [ENTER] PARA PARAR O SERVIDOR... ", True);
    localServer.stop();

def recursos():
    print('RECURSOS:');
    print('=========');
    print('funcLeEntradaTeclado()');
    print('funcLeEntradaTexto()');
    print('procInitHttpServer()');
    print('');

def executaTudo():
    print('EXECUTA:');
    print('========');
    print('');

    procInitHttpServer();

    print("");

def carregado():
    print('Arquivo: ex16_simple_http_server.py... carregado!');
    print('');

carregado();
recursos();
executaTudo();
