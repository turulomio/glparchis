## -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import libglparchis

from Ui_wdgUserPanel import *

class wdgUserPanel(QWidget, Ui_wdgUserPanel):
    def __init__(self, parent = None, name = None):
        QWidget.__init__(self, parent)
        if name:
            self.setObjectName(name)
        self.setupUi(self)

        self.jugador=None
        
    def setJugador(self, jugador):
        self.jugador=jugador
        self.lblAvatar.setPixmap(jugador.qpixmap())      
        self.grp.setTitle(jugador.name)
        
    def setLabelDado(self):
        """Actualiza la etiqueta del ´utlimo valor de tiradaturno"""
        numlbl=len(self.jugador.tiradaturno.arr)
        #Selecciona el label
        if numlbl==1:
            label=self.lbl1
        elif numlbl==2:
            label=self.lbl2
        elif numlbl==3:
            label=self.lbl3
        else:
            return
        label.setPixmap(self.jugador.dado.qpixmap(self.jugador.tiradaturno.ultimoValor()))

    def setActivated(self, bool):
        self.grp.setEnabled(bool)
        if bool==True:
            self.jugador.logturno=[]

    def on_chk_stateChanged(self, state):
        refresh()
        
    def refresh(self):
        self.lst.clear()
        if libglparchis.c2b(self.chk.checkState())==True:
            self.lst.addItems(self.jugador.loghistorico)  
            self.lst.setCurrentRow(len(self.jugador.loghistorico)-1)
        else:
            self.lst.addItems(self.jugador.logturno)          
            self.lst.setCurrentRow(len(self.jugador.logturno)-1)  
        self.lst.show()            
