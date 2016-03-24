#!/usr/bin/python3
import os
import sys

if sys.platform=='win32':
    sys.path.append("ui")
    sys.path.append("images")
else:
    sys.path.append("../lib/glparchis")
    sys.path.append("/usr/lib/glparchis")

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from frmMain import *

try:
    os.makedirs(os.path.expanduser("~/.glparchis/"))
except:
    pass

sys.setrecursionlimit(100000)
app = QApplication(sys.argv)
app.setOrganizationName("Mariano Muñoz ©")
app.setOrganizationDomain("turulomio.users.sourceforge.net")
app.setApplicationName("glParchis")
app.setQuitOnLastWindowClosed(True)

settings=QSettings()

frmMain = frmMain(settings) 
frmMain.show()
sys.exit(app.exec_())

