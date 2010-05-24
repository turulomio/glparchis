## -*- coding: utf-8 -*-
import sys,  random
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Ui_frmMain import *
from frmAbout import *
from frmLanguage import *
from wdgUserPanel import *
from wdgGame import *

class frmMain(QMainWindow, Ui_frmMain):#    
    def __init__(self, parent = 0,  flags = False):
        """
        Constructor
        
        @param parent The parent widget of this dialog. (QWidget)
        @param name The name of this dialog. (QString)
        @param modal Flag indicating a modal dialog. (boolean)
        """
        QMainWindow.__init__(self, None)
        self.setupUi(self)
        self.showMaximized()
        
        p1=wdgUserPanel(self.panel1)
        p1.show()
        p2=wdgUserPanel(self.panel2)
        p2.lblAvatar.setPixmap(QtGui.QPixmap(":/glparchis/keki.png"))
        p2.show()
        p3=wdgUserPanel(self.panel3)
        p3.lblAvatar.setPixmap(QtGui.QPixmap(":/glparchis/keke.png"))
        p3.show()
        p4=wdgUserPanel(self.panel4)
        p4.lblAvatar.setPixmap(QtGui.QPixmap(":/glparchis/keka.png"))
        p4.show()
        self.logs = []
        self.dado1 = QtGui.QIcon()
        self.dado1.addPixmap(QtGui.QPixmap(":/glparchis/cube1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dado2 = QtGui.QIcon()
        self.dado2.addPixmap(QtGui.QPixmap(":/glparchis/cube2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dado3 = QtGui.QIcon()
        self.dado3.addPixmap(QtGui.QPixmap(":/glparchis/cube3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dado4 = QtGui.QIcon()
        self.dado4.addPixmap(QtGui.QPixmap(":/glparchis/cube4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dado5= QtGui.QIcon()
        self.dado5.addPixmap(QtGui.QPixmap(":/glparchis/cube5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dado6 = QtGui.QIcon()
        self.dado6.addPixmap(QtGui.QPixmap(":/glparchis/cube6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        QtCore.QObject.connect(self.ogl, QtCore.SIGNAL('newLog(QString)'), self.lstLog_newLog)  
        QtCore.QObject.connect(self.ogl, QtCore.SIGNAL('cambiar_jugador()'), self.cambiar_jugador)  
        QtCore.QObject.connect(self.ogl, QtCore.SIGNAL('volver_a_tirar()'), self.volver_a_tirar)  
    
    def lstLog_newLog(self, log):
        self.logs.insert(0, str(self.ogl.jugadoractual) + "|" + log)
        self.lstLog.setModel(QStringListModel(QStringList(self.logs)))
        self.lstLog.show()

    @pyqtSignature("")
    def on_actionAcercaDe_activated(self):
        fr=frmAbout(self, "frmabout")
        fr.open()
    
    @QtCore.pyqtSlot()      
    def on_actionSalir_activated(self):
        sys.exit()
    
    @QtCore.pyqtSlot()      
    def on_actionDado_activated(self):        
        def jugador_tiene_todas_fichas_en_casa():
            for f in self.ogl.fichas:
                if f.jugador==self.ogl.jugadoractual:
                    if f.ruta!=0:
                        return False
            return True
        numero= int(random.random()*6)+1
        if numero==1:
            self.actionDado.setIcon(self.dado1)    
        elif numero==2:
            self.actionDado.setIcon(self.dado2)    
        elif numero==3:
            self.actionDado.setIcon(self.dado3)    
        elif numero==4:
            self.actionDado.setIcon(self.dado4)    
        elif numero==5:
            self.actionDado.setIcon(self.dado5)    
        elif numero==6:
            self.actionDado.setIcon(self.dado6)        
        
        #LOGICA QUE NO REQUIERE LA INTEVENCION DEL USUARIO
        if numero!=5 and jugador_tiene_todas_fichas_en_casa()==True:
            self.lstLog_newLog("No ha salido un 5 y las tienes todas en casa")
            self.cambiar_jugador()
            return
        
        self.lstLog_newLog("Ha salido un " + str(numero))        
        self.ogl.dado=numero
        self.ogl.pendiente=1
        self.ogl.historicodado.insert(0, numero)
        self.actionDado.setEnabled(False)

                    
    def cambiar_jugador(self):
        if self.ogl.jugadoractual==0:
            self.panel1.setEnabled(False)
        elif self.ogl.jugadoractual==1:
            self.panel2.setEnabled(False)
        elif self.ogl.jugadoractual==2:
            self.panel3.setEnabled(False)
        elif self.ogl.jugadoractual==3:
            self.panel4.setEnabled(False)
            
        self.lstLog_newLog("cambiando a jugador "  + str(self.ogl.jugadoractual))
        self.ogl.jugadoractual=self.ogl.jugadoractual+1
        self.ogl.historicodado=[]
        self.ogl.pendiente=2
        if self.ogl.jugadoractual>=4:
            self.ogl.jugadoractual=0
        self.actionDado.setEnabled(True)       
        
        if self.ogl.jugadoractual==0:
            self.panel1.setEnabled(True)
        elif self.ogl.jugadoractual==1:
            self.panel2.setEnabled(True)
        elif self.ogl.jugadoractual==2:
            self.panel3.setEnabled(True)
        elif self.ogl.jugadoractual==3:
            self.panel4.setEnabled(True)
        
    @QtCore.pyqtSlot()      
    def on_actionLenguaje_activated(self):
        fr=frmLanguage(self, "frmlanguage")
        fr.open()
                    
    def volver_a_tirar(self):
        self.actionDado.setEnabled(True)
