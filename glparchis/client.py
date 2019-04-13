import argparse
import os
import signal
import sys
from colorama import init as colorama_init

from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QApplication
#    from glparchis.ui.frmMain import frmMain
from glparchis.version import __versiondate__   
from glparchis.loggingsystem import argparse_add_debug_argument, argparse_parsing_debug_argument
from glparchis.functions import signal_handler
from glparchis.libglparchismultiplayer import MemDisplay

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

#    frmMain = frmMain(settings) 
#    frmMain.show()

