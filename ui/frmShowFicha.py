## -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Ui_frmShowFicha import *   

class frmShowFicha(QDialog, Ui_frmShowFicha):
    def __init__(self,   parent = None, flags= None,  ficha=None):
        QDialog.__init__(self, parent, flags)
        self.ficha=ficha
        self.setupUi(self)
        self.lblFicha.setPixmap(self.ficha.jugador.qpixmap())       
        self.lblName.setText(self.trUtf8("Nombre: %1").arg(self.ficha.id))
        self.lblJugador.setText(self.trUtf8("Jugador: %1 (%2)").arg(str(self.ficha.jugador.name)).arg(self.ficha.jugador.color.name))
#        self.lblPosicion.setText(self.trUtf8("Posición en casilla: %1").arg(str(self.ficha.numposicion)))
        self.lblRuta.setText(self.trUtf8("Posición en ruta: %1").arg(str(self.ficha.posruta)))
