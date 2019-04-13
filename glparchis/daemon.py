import argparse
import os
import signal
import sys
from colorama import init as colorama_init

from glparchis.functions import signal_handler
from glparchis.version import __versiondate__   
from glparchis.loggingsystem import argparse_add_debug_argument, argparse_parsing_debug_argument
from glparchis.libglparchismultiplayer import Server            
from PyQt5.QtCore import QCoreApplication, QSettings

def main():
    colorama_init()

    try:
        os.makedirs(os.path.expanduser("~/.glparchis/"))
    except:
        pass

    sys.setrecursionlimit(100000)
    global app
    app = QCoreApplication(sys.argv)
    app.setOrganizationName("glParchis")
    app.setOrganizationDomain("glParchis")
    app.setApplicationName("glParchis")
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
    
    server=Server()
    server.start()
    
