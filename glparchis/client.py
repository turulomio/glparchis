import argparse
import os
import signal
import sys
from colorama import init as colorama_init
import socket
import json


BUFSIZ=2048
def main():
    colorama_init()

    from PyQt5.QtCore import QSettings
    from PyQt5.QtWidgets import QApplication
#    from glparchis.ui.frmMain import frmMain
    from glparchis.version import __versiondate__   
    from glparchis.loggingsystem import argparse_add_debug_argument, argparse_parsing_debug_argument
    from glparchis.functions import signal_handler
    from glparchis.libglparchismultiplayer import b2list, s2b

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
    

    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 65432        # The port used by the server

    # Create a socket (SOCK_STREAM means a TCP socket)
    global sock
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    # Connect to server and send data
    sock.send(s2b("listgames 4\n"))
    lists=sock.recv(BUFSIZ)
    print (lists)
    sock.send(s2b("creategame 4\n"))
    sock.recv(BUFSIZ)#OK
    while True:
        try:
            bruto=sock.recv(BUFSIZ).replace(b"\n", b"")
            data = b2list(bruto)
            if data[0]=="gamecreated":
                print("Game has been created",  data)
            elif data[0]=="gameuserid":
                print("Assignes user id",  data)
            elif data[0]=="gamestart":
                print("Game starts",  data)
            elif data[0]=="status":
                js=bruto.replace(b"status ", b"")
                d = json.loads(js)
                print("status",  d)
            sock.send(s2b("OK\n"))
        except OSError:  # Possibly client has left the chat.
            print("Error in client")
            break


#
#
#
#    frmMain = frmMain(settings) 
#    frmMain.show()
#    sys.exit(app.exec_())
#        except socket.error as e:
#            print(str(e))
#
#    print("Waiting for a connection")
#    while True:
#        conn, addr = sock.accept()
#        print("Connected to: ", addr)
#        player=None
#        start_new_thread(threaded_client, (player,))
        
#    
#def threaded_client( player):
#    print("threaded_client in client")
#    pass
#    data=b2list(player.socket.recv(1024))
#    if data[0]=="creategame":
#        game=ServerGame(data[1])
#        player.socket.send(s2b("gamecreated {}\n".format(game.id)))
#        player.socket.send(s2b("gameuserid {}_{}\n".format(game.id, game.assign_id())))
