from argparse import ArgumentParser, RawTextHelpFormatter
from os import path, makedirs
from signal import signal, SIGINT
from sys import setrecursionlimit, argv, exit
from colorama import init as colorama_init


def main():
    colorama_init()

    from PyQt5.QtCore import QSettings
    from PyQt5.QtWidgets import QApplication
    from glparchis.ui.frmMain import frmMain
    from glparchis.version import __versiondate__   
    from glparchis.loggingsystem import argparse_add_debug_argument, argparse_parsing_debug_argument
    from glparchis.functions import signal_handler

    try:
        makedirs(path.expanduser("~/.glparchis/"))
    except:
        pass

    setrecursionlimit(100000)
    global app
    app = QApplication(argv)
    app.setOrganizationName("glParchis")
    app.setOrganizationDomain("glParchis")
    app.setApplicationName("glParchis")
    app.setQuitOnLastWindowClosed(True)
    signal(SIGINT, signal_handler)

    parser=ArgumentParser(
            prog='glparchis', 
            description=app.translate("Core",'Parchis Game'),  
            epilog=app.translate("Core","If you like this app, please give me a star in Github (https://github.com/Turulomio/glparchis).")+"\n" +
                        app.translate("Core","Developed by Mariano Mu\xf1oz 2006-{} \xa9".format(__versiondate__.year)),
            formatter_class=RawTextHelpFormatter
        )
    argparse_add_debug_argument(parser)
    args=parser.parse_args()        

    argparse_parsing_debug_argument(args)

    settings=QSettings()

    frmMain = frmMain(settings) 
    frmMain.show()
    exit(app.exec_())

