import argparse
import os
import signal
import sys
import json
from colorama import init as colorama_init

from PyQt5.QtCore import QSettings, QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication
from PyQt5.QtNetwork import QHostAddress, QTcpSocket
#    from glparchis.ui.frmMain import frmMain
from glparchis.version import __versiondate__   
from glparchis.loggingsystem import argparse_add_debug_argument, argparse_parsing_debug_argument
from glparchis.functions import signal_handler
from glparchis.libglparchistypes import TGameMode
from glparchis.libglparchismultiplayerqt import command_split, s2b
    
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
        
    def on_connected(self):
        # Connect to server and send data
        print("Asking listgames")
        print(self.c2s_listgames())
        print("Asking creategame")
        print(self.c2s_creategame(TGameMode.Four, True, True, True, True))
        print("Asking startgame")
        print(self.c2s_startgame())
        self.quit.emit()
#        while True:
#            print("Cliente esperando")
#            try:
#                buffer=self.sock.recv(self.BUFSIZ)
#                print(buffer)
#                command, args=command_split(buffer.replace(b"\n", b""))
#                if command=="display":
#                    self.s2c_update_display(command, args)
#            except OSError:  # Possibly client has left the chat.
#                print("Error in client")
#                break
                
    def readSocketData(self):
        buffer=self.sock.readAll().data()#To convert to bytes data    
#        print("on readSocketData", self.buffer)
#        data=b2s(self.buffer)
#        if data.startswith("server_"):
#            result=self.server.process_commands(b2s(self.buffer), self)
#            print(result)
#            self.sock.write(s2b(result))
#            self.sock.flush()
#        else:#Send command to Game
#            result=self.game.process_commands(b2s(self.buffer), self)
#            self.sock.write(s2b(result))
#            self.sock.flush()
        command, args=command_split(buffer.replace(b"\n", b""))
        if command=="display":
            self.s2c_update_display(command, args)
    
    def s2c_update_display(self, command, stream,  wait=200):
        self.status = json.loads(stream)
        print("display",  self.status)
        self.sock.send(s2b("OK\n"))

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

