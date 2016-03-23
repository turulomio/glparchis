 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from libglparchis import c2b
from Ui_wdgPlayer import *

class wdgPlayer(QWidget, Ui_wdgPlayer):
    def __init__(self, parent = None, name = None):
        QWidget.__init__(self, parent)
        if name:
            self.setObjectName(name)
        self.setupUi(self)

        self.jugador=None

    def setJugador(self, j):
        self.jugador=j
        self.pixmap.setPixmap(j.color.qpixmap())
        self.label.setText(self.tr("Datos del jugador {0}".format( (j.color.name))))
        
    def commit(self):
        """Mete en jugador los datos aceptados"""
        self.jugador.name=self.txt.text()
        self.jugador.ia=c2b(self.chkIA.checkState())
        self.jugador.plays=c2b(self.chkPlays.checkState())
