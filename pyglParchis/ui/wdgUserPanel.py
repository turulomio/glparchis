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
#        self.log=[]
#        self.history=[]
        self.jugador=None
        
    def setJugador(self, jugador):
        self.jugador=jugador
        self.lblAvatar.setPixmap(jugador.qpixmap())      
        self.grp.setTitle(jugador.name)
        
    def setLabelDado(self, historicodado):
        numero=historicodado[0]
        numlbl=len(historicodado)
#            #Selecciona el panel
#            if self.mem.jugadoractual.color.name=="yellow":
#                panel=self.panel1
#            elif self.mem.jugadoractual.color.name=="blue":
#                panel=self.panel2
#            elif self.mem.jugadoractual.color.name=="red":
#                panel=self.panel3
#            elif self.mem.jugadoractual.color.name=="green":
#                panel=self.panel4
        #Selecciona el label
        if numlbl==1:
            label=self.panel().lbl1
        elif numlbl==2:
            label=self.panel().lbl2
        elif numlbl==3:
            label=self.panel().lbl3
        label.setPixmap(jugador.dado.qpixmap(numero))
#    @QtCore.pyqtSlot(bool)      
    def setActivated(self, bool):
        self.grp.setEnabled(bool)
        if bool==True:
            self.log=[]
#
#    def newLog(self, log):
#        log=str(datetime.datetime.now()-self.inittime)[2:-7]+ " " + log
#        self.history.append( log)
#        self.log.append(log)
#        self.on_chk_stateChanged(self.chk.checkState())

    def on_chk_stateChanged(self, state):
        self.lst.clear()
        if libglparchis.c2b(state)==True:
            self.lst.addItems(self.jugador.loghistorico)  
            self.lst.setCurrentRow(len(self.jugador.loghistorico)-1)
        else:
            self.lst.addItems(self.jugador.logturno)          
            self.lst.setCurrentRow(len(self.jugador.logturno)-1)
#            QModelIndex modelIndex = list->rootIndex(); // u have to find the model index of the first item here
#list->setCurrentIndex(modelIndex);
#        self.lst.selectionModel().select(len(self.log)-1, QItemSelectionModel.Select)          
        self.lst.show()            
