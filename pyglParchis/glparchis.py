#!/usr/bin/env python
#-*- coding: utf-8 -*- 

import sys
sys.path.append("/usr/lib/pyglparchis")

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from frmMain import *

def help():
    print "Ayuda"

#Creamos la aplicacion principal y conectamos la señal lastWindowClosed()
#(ultima ventana cerrada) con la funcion quit() (salir de la aplicacion)
app = QApplication(sys.argv)

translator = QTranslator(app)
locale=QLocale()
a=locale.system()
translator.load("/usr/share/pyglparchis/glparchis_" + a.name() + ".qm")
app.installTranslator(translator);

frmMain = frmMain() 
frmMain.ogl.setFocus()
frmMain.show()

sys.exit(app.exec_())

