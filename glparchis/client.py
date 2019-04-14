import argparse
import os
import signal
import sys
import json
from colorama import init as colorama_init

from PyQt5.QtCore import QSettings, QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication
from PyQt5.QtNetwork import QHostAddress, QTcpSocket
from glparchis.version import __versiondate__   
from glparchis.loggingsystem import argparse_add_debug_argument, argparse_parsing_debug_argument
from glparchis.functions import signal_handler, s2b
from glparchis.libglparchistypes import TGameMode
from glparchis.libglparchismultiplayer import command_split
    
class MemDisplay(QObject):
    quit=pyqtSignal()
    def __init__(self, host,  port):
        QObject.__init__(self)
        self.BUFSIZ=2048
        self.host=host
        self.port=port
        self.status=None
        self.display=False
        self.sock=QTcpSocket()
        self.sock.connectToHost(QHostAddress.LocalHost, 65432)
        self.sock.connected.connect(self.on_connected)
        self.sock.readyRead.connect(self.readSocketData)
        self.must_move=False
        self.must_throw=False
        
    def on_connected(self):
        # Connect to server and send data
        print("Asking listgames")
        self.c2s_listgames()
        print("Asking creategame")
        self.c2s_creategame(TGameMode.Four, True, True, True, True)
        print("Asking startgame")
        self.c2s_startgame()
                
    def readSocketData(self):
        buffer=self.sock.readAll().data()#To convert to bytes data    
        command, args=command_split(buffer)
        if command=="display":
            self.receive_display(buffer.replace(b"display ", b""))
        elif command=="must_throw":
            self.receive_must_throw()
        else:
            print("Command not found",  buffer)
    
    def receive_display(self, stream,  wait=200):
        self.status = json.loads(stream)
        print("display",  self.status)
        self.sock.write(s2b("True"))
        self.sock.flush()
    
    def receive_must_throw(self):
        print("Receiving must_throw")
        self.must_throw=True
        self.sock.write(b"True")
        self.sock.flush()

    def c2s_creategame(self, mode, *arrPlays):
        self.sock.write(s2b("server_creategame {} True True True True".format(TGameMode.Four)))
        self.sock.flush()
        self.sock.waitForReadyRead()
        return self.sock.readAll()
        
    def c2s_startgame(self):
        self.sock.write(s2b("startgame"))
        self.sock.flush()
        self.sock.waitForReadyRead()
        return self.sock.readAll()

    def c2s_listgames(self):
        self.sock.write(s2b("server_listgames"))
        self.sock.flush()
        self.sock.waitForReadyRead()
        return self.sock.readAll()


BUFSIZ=2048
def main():
    colorama_init()


    try:
        os.makedirs(os.path.expanduser("~/.glparchis/"))
    except:
        pass

    sys.setrecursionlimit(100000)
    global app
    app = QApplication(sys.argv)
    app.setOrganizationName("glParchis")
    app.setOrganizationDomain("glParchis")
    app.setApplicationName("glParchis")
    app.setQuitOnLastWindowClosed(True)
    signal.signal(signal.SIGINT, signal_handler)

    parser=argparse.ArgumentParser(
            prog='glparchis', 
            description=app.translate("Core",'Parchis Game'),  
            epilog=app.translate("Core","If you like this app, please give me a star in Github (https://github.com/Turulomio/glparchis).")+"\n" +
                        app.translate("Core","Developed by Mariano Mu\xf1oz 2006-{} \xa9".format(__versiondate__.year)),
            formatter_class=argparse.RawTextHelpFormatter
        )
    argparse_add_debug_argument(parser)
    args=parser.parse_args()        

    argparse_parsing_debug_argument(args)

    settings=QSettings()
    settings
    

    host = '127.0.0.1'  # The server's hostname or IP address
    port = 65432        # The port used by the server
    
    display=MemDisplay(host,  port)
    display.quit.connect(app.quit)
    app.exec()

#    frmMain = frmMain(settings) 
#    frmMain.show()

