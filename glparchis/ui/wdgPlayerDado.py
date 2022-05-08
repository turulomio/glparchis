from PyQt5.QtWidgets import QWidget
from random import random
from glparchis.ui.Ui_wdgPlayerDado import Ui_wdgPlayerDado

class wdgPlayerDado(QWidget, Ui_wdgPlayerDado):
    def __init__(self, mem,  jugador, parent = None, name = None):
        QWidget.__init__(self, parent)
        self.mem=mem
        if name:
            self.setObjectName(name)
        self.setupUi(self)

        self.jugador=jugador
        self.tirada=0
        self.pixmap.setPixmap(self.jugador.color.qpixmap())
    
    def hasPlayed(self):
        if self.tirada!=0:
            return True
        return False

    def setName(self, name):
        """Se hace asi porque al principio no se sabe el name del jugador """
        self.lblName.setText(name)

    def on_cmd_released(self):
        self.tirada=int(random()*6)+1
        self.lblDado.setPixmap(self.mem.dado.qpixmap(self.tirada))
