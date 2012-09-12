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

app = QApplication(sys.argv)

translator = QTranslator(app)
locale=QLocale()
a=locale.system()
if WindowsVersion==True:
    translator.load("../share/glparchis/glparchis_" + a.name() + ".qm")
else:
    translator.load("/usr/share/glparchis/glparchis_" + a.name() + ".qm")
app.installTranslator(translator);

os.chdir(os.path.expanduser("~/.glparchis/"))
frmMain = frmMain() 
frmMain.show()
sys.exit(app.exec_())

