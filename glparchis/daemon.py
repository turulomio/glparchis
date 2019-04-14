import argparse
import os
import signal
import sys
import logging
from colorama import init as colorama_init, Style, Fore

from glparchis.version import __versiondate__   
from glparchis.loggingsystem import argparse_add_debug_argument, argparse_parsing_debug_argument
from glparchis.libglparchismultiplayer import Server            
from PyQt5.QtCore import QCoreApplication, QSettings
from PyQt5.QtNetwork import QHostAddress

    
    
def signal_handler(signal, frame):
    logging.critical(Style.BRIGHT+Fore.RED+QCoreApplication.translate("Core","You pressed 'Ctrl+C', exiting..."))
    server.close()
    sys.exit(1)
        
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
    global server    
    server=Server(QHostAddress.Any,  65432)
    server.quit.connect(app.quit)
    app.exec()
    
