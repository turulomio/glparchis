## -*- coding: utf-8 -*-
import sys,  random
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Ui_frmMain import *
from frmAbout import *
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
        
#        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
#        brush.setStyle(QtCore.Qt.SolidPattern)
#        self.panel1.lblAvatar.palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        
        self.p1=wdgUserPanel(self.panel1)
        self.p1.setEnabled(False)
        self.p1.lblAvatar.setPixmap(QtGui.QPixmap(":/glparchis/fichaamarilla.png"))
        self.p1.show()
        self.p2=wdgUserPanel(self.panel2)
        self.p2.setEnabled(False)
        self.p2.lblAvatar.setPixmap(QtGui.QPixmap(":/glparchis/fichaazul.png"))
        self.p2.show()
        self.p3=wdgUserPanel(self.panel3)
        self.p3.setEnabled(False)
        self.p3.show()
        self.p4=wdgUserPanel(self.panel4)
        self.p4.setEnabled(False)
        self.p4.lblAvatar.setPixmap(QtGui.QPixmap(":/glparchis/fichaverde.png"))
        self.p4.show()
        self.logs = []
        self.dado1 = QtGui.QIcon()
        self.p1.setObjectName("dado1")
        self.dado1.addPixmap(QtGui.QPixmap(":/glparchis/cube1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dado2 = QtGui.QIcon()
        self.p1.setObjectName("dado2")
        self.dado2.addPixmap(QtGui.QPixmap(":/glparchis/cube2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dado3 = QtGui.QIcon()
        self.p1.setObjectName("dado3")
        self.dado3.addPixmap(QtGui.QPixmap(":/glparchis/cube3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dado4 = QtGui.QIcon()
        self.p1.setObjectName("dado4")
        self.dado4.addPixmap(QtGui.QPixmap(":/glparchis/cube4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dado5= QtGui.QIcon()
        self.p1.setObjectName("dado5")
        self.dado5.addPixmap(QtGui.QPixmap(":/glparchis/cube5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dado6 = QtGui.QIcon()
        self.p1.setObjectName("dado6")        
        self.logs1=[]
        self.logs2=[]
        self.logs3=[]
        self.logs4=[]
        self.dado6.addPixmap(QtGui.QPixmap(":/glparchis/cube6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        QtCore.QObject.connect(self.ogl, QtCore.SIGNAL('newLog(QString)'), self.lstLog_newLog)  
        QtCore.QObject.connect(self.ogl, QtCore.SIGNAL('cambiar_jugador()'), self.cambiar_jugador)  
        QtCore.QObject.connect(self.ogl, QtCore.SIGNAL('volver_a_tirar()'), self.volver_a_tirar)  
#        QtCore.QObject.connect(self.ogl, QtCore.SIGNAL('tirar_dado()'), self.on_actionDado_activated)  
        #Se activa 
        self.enable_panel(self.ogl.jugadoractual, True)

    @pyqtSignature("")
    def on_cmdTirarDado_clicked(self):
        self.on_actionDado_activated()
        
    def enable_panel(self, idjugador, bool):
        if idjugador==0:
            self.p1.setEnabled(bool)
        elif idjugador==1:
            self.p2.setEnabled(bool)
        elif idjugador==2:
            self.p3.setEnabled(bool)
        elif idjugador==3:
            self.p4.setEnabled(bool)    
            
    def lstLog_newLog(self, log):
        if self.ogl.jugadoractual==0:
            panel=self.p1
            logs=self.logs1
        elif self.ogl.jugadoractual==1:
            panel=self.p2
            logs=self.logs2
        elif self.ogl.jugadoractual==2:
            panel=self.p3
            logs=self.logs3
        elif self.ogl.jugadoractual==3:
            panel=self.p4        
            logs=self.logs4
        logs.append( log)
        panel.lst.setModel(QStringListModel(logs))
        panel.lst.show()

    @pyqtSignature("")
    def on_actionAcercaDe_activated(self):
        fr=frmAbout(self, "frmabout")
        fr.open()
    
    @QtCore.pyqtSlot()      
    def on_actionSalir_activated(self):
        sys.exit()
    
    @QtCore.pyqtSlot()      
    def on_actionDado_activated(self):  
        def labeldado():
            numero=self.ogl.historicodado[0]
            numlbl=len(self.ogl.historicodado)
            #Selecciona el panel
            if self.ogl.jugadoractual==0:
                panel=self.p1
            elif self.ogl.jugadoractual==1:
                panel=self.p2
            elif self.ogl.jugadoractual==2:
                panel=self.p3
            elif self.ogl.jugadoractual==3:
                panel=self.p4
            #Selecciona el label
            if numlbl==1:
                label=panel.lbl1
            elif numlbl==2:
                label=panel.lbl2
            elif numlbl==3:
                label=panel.lbl3
            #Selecciona el pixmap
            if numero==1:
                pix=QtGui.QPixmap(":/glparchis/cube1.png")
                self.actionDado.setIcon(self.dado1)    
                self.cmdTirarDado.setIcon(self.dado1)
            elif numero==2:
                pix=QtGui.QPixmap(":/glparchis/cube2.png")
                self.actionDado.setIcon(self.dado2)    
                self.cmdTirarDado.setIcon(self.dado2)
            elif numero==3:
                pix=QtGui.QPixmap(":/glparchis/cube3.png")
                self.actionDado.setIcon(self.dado3)    
                self.cmdTirarDado.setIcon(self.dado3)
            elif numero==4:
                pix=QtGui.QPixmap(":/glparchis/cube4.png")
                self.actionDado.setIcon(self.dado4)    
                self.cmdTirarDado.setIcon(self.dado4)
            elif numero==5:
                pix=QtGui.QPixmap(":/glparchis/cube5.png")
                self.actionDado.setIcon(self.dado5)    
                self.cmdTirarDado.setIcon(self.dado5)
            elif numero==6:
                pix=QtGui.QPixmap(":/glparchis/cube6.png")
                self.actionDado.setIcon(self.dado6)    
                self.cmdTirarDado.setIcon(self.dado6)
            label.setPixmap(pix)
                
        def jugador_tiene_todas_fichas_en_casa():
            for f in self.ogl.fichas:
                if f.jugador==self.ogl.jugadoractual:
                    if f.ruta!=0:
                        return False
            return True
            
#        numero= int(random.random()*6)+1
        numero=5
        self.lstLog_newLog("Ha salido un " + str(numero))        
        self.ogl.dado=numero
        self.ogl.pendiente=1
        self.ogl.historicodado.insert(0, numero)
        self.actionDado.setEnabled(False)
        self.cmdTirarDado.setEnabled(False)
        labeldado()
        
        #LOGICA QUE NO REQUIERE LA INTEVENCION DEL USUARIO
        if numero!=5 and jugador_tiene_todas_fichas_en_casa()==True:
            self.lstLog_newLog("No ha salido un 5 y las tienes todas en casa")
            self.cambiar_jugador()
            return
        

                    
    def cambiar_jugador(self):
        def limpia_panel(id):
            if id==0:
                self.p1.lbl1.setPixmap(QtGui.QPixmap(":/glparchis/cube.png"))
                self.p1.lbl2.setPixmap(QtGui.QPixmap(":/glparchis/cube.png"))
                self.p1.lbl3.setPixmap(QtGui.QPixmap(":/glparchis/cube.png"))
                self.p1.show()
            elif id==1:
                self.p2.lbl1.setPixmap(QtGui.QPixmap(":/glparchis/cube.png"))
                self.p2.lbl2.setPixmap(QtGui.QPixmap(":/glparchis/cube.png"))
                self.p2.lbl3.setPixmap(QtGui.QPixmap(":/glparchis/cube.png"))
                self.p2.show()
            elif id==2:
                self.p3.lbl1.setPixmap(QtGui.QPixmap(":/glparchis/cube.png"))
                self.p3.lbl2.setPixmap(QtGui.QPixmap(":/glparchis/cube.png"))
                self.p3.lbl3.setPixmap(QtGui.QPixmap(":/glparchis/cube.png"))
                self.p3.show()
            elif id==3:
                self.p4.lbl1.setPixmap(QtGui.QPixmap(":/glparchis/cube.png"))
                self.p4.lbl2.setPixmap(QtGui.QPixmap(":/glparchis/cube.png"))
                self.p4.lbl3.setPixmap(QtGui.QPixmap(":/glparchis/cube.png"))
                self.p4.show()
        self.enable_panel(self.ogl.jugadoractual, False)
        self.ogl.jugadoractual=self.ogl.jugadoractual+1
        self.ogl.historicodado=[]
        self.ogl.pendiente=2
        if self.ogl.jugadoractual>=4:
            self.ogl.jugadoractual=0
#        self.lstLog_newLog("cambiando a jugador "  + str(self.ogl.jugadoractual))
        self.actionDado.setEnabled(True)       
        self.cmdTirarDado.setEnabled(True)
        self.enable_panel(self.ogl.jugadoractual,  True)
        limpia_panel(self.ogl.jugadoractual)

                    
    @QtCore.pyqtSlot()     
    def on_actionRecuperarPartida_activated(self):
        filename=QFileDialog.getOpenFileName(self, "", "", "glParchis game (*.glparchis)")
        print filename
        
    @QtCore.pyqtSlot()     
    def on_actionGuardarPartida_activated(self):
        filename=QFileDialog.getOpenFileName(self, "", "", "glParchis game (*.glparchis)")
        print filename

    def volver_a_tirar(self):
        self.actionDado.setEnabled(True)
