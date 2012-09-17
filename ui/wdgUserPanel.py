## -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Ui_wdgUserPanel import *

class wdgUserPanel(QWidget, Ui_wdgUserPanel):
    def __init__(self, parent = None, name = None):
        QWidget.__init__(self, parent)
        if name:
            self.setObjectName(name)
        self.setupUi(self)

        self.jugador=None
        self.timerLog = QTimer()
        QObject.connect(self.timerLog, SIGNAL("timeout()"), self.refreshLog)     
        self.timerLog.start(300)
        
    def setJugador(self, jugador):
        self.jugador=jugador
        self.lblAvatar.setPixmap(jugador.qpixmap())      
        self.grp.setTitle(jugador.name)
        
    def setLabelDado(self):
        """Actualiza la etiqueta del útlimo valor de tiradaturno"""
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
        self.lbl1.setEnabled(bool)
        self.lbl2.setEnabled(bool)
        self.lbl3.setEnabled(bool)
        self.lblAvatar.setEnabled(bool)
        if bool==True:
            self.jugador.logturno=[]
        self.show()

    def on_chk_stateChanged(self, state):        
        """Reescribe solo cuando cambia el tamaño"""
        if state==Qt.Checked and self.lst.count()!=len(self.jugador.loghistorico):
            self.lst.clear()
            self.lst.addItems(self.jugador.loghistorico)  
            self.lst.setCurrentRow(len(self.jugador.loghistorico)-1)
            self.lst.clearSelection()
        elif state==Qt.Unchecked and self.lst.count()!=len(self.jugador.logturno):
            self.lst.clear()
            self.lst.addItems(self.jugador.logturno)          
            self.lst.setCurrentRow(len(self.jugador.logturno)-1)  
            self.lst.clearSelection()
        
    def refreshLog(self):
        self.on_chk_stateChanged(self.chk.checkState())
        
