#!/usr/bin/python3
import os
import sys

def main():
    if sys.platform=='win32':
        if os.path.isdir(os.path.dirname(sys.argv[0])): #Without this lines windows shortcuts anchored to init failed. Work when installed
            os.chdir(os.path.dirname(sys.argv[0]))

    from PyQt5.QtCore import QSettings
    from PyQt5.QtWidgets import QApplication
    from glparchis.ui.frmMain import frmMain
    
    try:
        os.makedirs(os.path.expanduser("~/.glparchis/"))
    except:
        pass

    sys.setrecursionlimit(100000)
    app = QApplication(sys.argv)
    app.setOrganizationName("glParchis")
    app.setOrganizationDomain("glparchis.sourceforge.net")
    app.setApplicationName("glParchis")
    app.setQuitOnLastWindowClosed(True)

    settings=QSettings()

    frmMain = frmMain(settings) 
    frmMain.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
