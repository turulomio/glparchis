## -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import libglparchis
from Ui_frmShowFicha import *   

class frmShowFicha(QDialog, Ui_frmShowFicha):
    def __init__(self, parent = None, flags= None,  ficha=None,  jugador=None):
        QDialog.__init__(self, parent, flags)
        self.ficha=ficha
        self.jugador=jugador
        self.setupUi(self)
        self.lblFicha.setPixmap(libglparchis.pixficha(self.ficha.colorname))       
        self.lblName.setText(self.trUtf8("Nombre: %1").arg(self.ficha.name))
        self.lblJugador.setText(self.trUtf8("Jugador: %1 (%2)").arg(str(self.jugador.name)).arg(self.jugador.id))
#        self.lblPosicion.setText(self.trUtf8("Posición en casilla: %1").arg(str(self.ficha.numposicion)))
        self.lblRuta.setText(self.trUtf8("Posición en ruta: %1").arg(str(self.ficha.ruta)))
