#!/usr/bin/env python
#-*- coding: utf-8 -*- 

import sys, os
WindowsVersion=False #Hay dos una en libmyquotes y otra en glparchis
if WindowsVersion==True:
    sys.path.append("../lib/glparchis")
else:
    sys.path.append("/usr/lib/glparchis")

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from frmMain import *

def help():
    print ("Ayuda")

try:
    os.makedirs(os.path.expanduser("~/.glparchis/"))
except:
    pass
#Creamos la aplicacion principal y conectamos la señal lastWindowClosed()
#(ultima ventana cerrada) con la funcion quit() (salir de la aplicacion)

sys.setrecursionlimit(50000)

rootdir="/usr/"
# en src windows s ejecuta desde bat seria rootdir="" para que fuera share/... relativo
# en bin windows se ejecuta 
app = QApplication(sys.argv)
app.setApplicationName("glParchis")
app.setQuitOnLastWindowClosed(True)
try:
    from PyQt4.phonon import Phonon
except ImportError:
    QMessageBox.critical(None, "glParchis",  "Tu instalaci´on QT no tiene soporte Phonon")
    sys.exit(1)

translator = QTranslator(app)
locale=QLocale()
a=locale.system()
if WindowsVersion==True:
    translator.load("share/glparchis/glparchis_" + a.name() + ".qm")
else:
    translator.load("/usr/share/glparchis/glparchis_" + a.name() + ".qm")
app.installTranslator(translator);

frmMain = frmMain() 
frmMain.show()
sys.exit(app.exec_())

