from PyQt5.QtCore import  Qt
from PyQt5.QtWidgets import QWidget
from glparchis.ui.Ui_wdgUserPanel import Ui_wdgUserPanel

class wdgUserPanel(QWidget, Ui_wdgUserPanel):
    def __init__(self, parent = None, name = None):
        QWidget.__init__(self, parent)
        self.logturno=[]#log de turno
        self.loghistorico=[]
        if name:
            self.setObjectName(name)
        self.setupUi(self)

        self.jugador=None
        
    def setJugador(self, jugador):
        self.jugador=jugador
        self.lblAvatar.setPixmap(jugador.color.qpixmap())      
        self.grp.setStyleSheet('QGroupBox {color: '+self.jugador.color.name+'}')
        self.grp.setTitle( (jugador.name))
        jugador.logEmitted.connect(self.logReceived)
        
    def setLabelDado(self):
        """Actualiza la etiqueta del utlimo valor de tiradaturno"""
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
        """Funcion que se ejecuta para activar un panel. Al hacerlo se cambia el log de turno y se limpian los dados"""
        if bool==True:
            self.lbl1.setPixmap(self.jugador.dado.qpixmap(None))
            self.lbl2.setPixmap(self.jugador.dado.qpixmap(None))
            self.lbl3.setPixmap(self.jugador.dado.qpixmap(None))
            self.grp.setStyleSheet('QGroupBox {font: bold ; color: '+self.jugador.color.name+';}')#'background-color: rgb(170, 170, 170);}')
            self.logturno=[]
        else:
            self.grp.setStyleSheet('QGroupBox {font: Normal; color: '+self.jugador.color.name+';}')
        self.lbl1.setEnabled(bool)
        self.lbl2.setEnabled(bool)
        self.lbl3.setEnabled(bool)
        self.lblAvatar.setEnabled(bool)
        

    def on_chk_stateChanged(self, state):        
        """Reescribe solo cuando cambia el tamano"""
        if state==Qt.Checked and self.lst.count()!=len(self.loghistorico):
            self.lst.clear()
            self.lst.addItems(self.loghistorico)  
            self.lst.setCurrentRow(len(self.loghistorico)-1)
            self.lst.clearSelection()
        elif state==Qt.Unchecked and self.lst.count()!=len(self.logturno):
            self.lst.clear()
            self.lst.addItems(self.logturno)          
            self.lst.setCurrentRow(len(self.logturno)-1)  
            self.lst.clearSelection()
        
    def logReceived(self, log):
        self.logturno.append(log)
        self.loghistorico.append(log)
        self.on_chk_stateChanged(self.chk.checkState())
