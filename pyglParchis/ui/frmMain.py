## -*- coding: utf-8 -*-
import sys,  random
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from xml.dom.minidom import parse

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
            
#        numero=5
#        numero= int(random.random()*6)+1
        numero= int(random.random()*2)+5
#        self.lstLog_newLog("Ha salido un " + str(numero))        
#        self.ogl.dado=numero
        self.ogl.pendiente=1
        self.ogl.historicodado.insert(0, numero)
        self.actionDado.setEnabled(False)
        self.cmdTirarDado.setEnabled(False)
        labeldado()
        
        print "num"+ str(numero)
        #LOGICA QUE NO REQUIERE LA INTEVENCION DEL USUARIO
        if jugador_tiene_todas_fichas_en_casa()==True:
            if numero <5:
                self.lstLog_newLog(str(numero)+ "No es un 5 y las tienes todas en casa")
                self.cambiar_jugador()
                return
            elif numero==6 and len(self.ogl.historicodado)==3:
                self.lstLog_newLog("No ha salido un 5, y ha sacado 3 seises, ya no puede volver a tirar")
                self.cambiar_jugador()
                return            
            elif numero==6 and len(self.ogl.historicodado)<3:
                self.lstLog_newLog("No es 5, pero puede volver a tirar")
                self.ogl.pendiente=2
                self.actionDado.setEnabled(True)
                self.cmdTirarDado.setEnabled(True)
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

        names = []
        values = []
        f=open(filename)
        dom = parse(f)
        self.ogl.jugadoractual=int(dom.getElementsByTagName("jugadores")[0].getAttribute("actual"))
        print self.ogl.jugadoractual
        fichas=dom.getElementsByTagName("ficha")
        for i in range(len(fichas)):
            id=int(fichas[i].getAttribute("id"))
            ruta=int(fichas[i].getAttribute("posicion_ruta"))
            self.ogl.mover(id, ruta)
#            value = data[i].getElementsByTagName("value")
#            values.append(value[0].firstChild.nodeValue.encode("utf-8"))

        
    @QtCore.pyqtSlot()     
    def on_actionGuardarPartida_activated(self):
        filename=QFileDialog.getOpenFileName(self, "", "", "glParchis game (*.glparchis)")
        f=open(filename,"w")
        f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
        f.write("<glParchis version=\"1.0\">\n")
        f.write("<partida>\n")
        f.write("  <jugadores numero=\""+str(4)+"\" actual=\""+str(self.ogl.jugadoractual)+"\">\n" )
        f.write('    <jugador id="0" nombre="amarillo" tipo="'+str(0)+'">\n') #Deberá ser cambiado cuando haya IA
        f.write("      <fichas>\n")
        f.write('        <ficha id="0" posicion_ruta="'+str(self.ogl.fichas[0].ruta)+'" />\n')
        f.write('        <ficha id="1" posicion_ruta="'+str(self.ogl.fichas[1].ruta)+'" />\n')
        f.write('        <ficha id="2" posicion_ruta="'+str(self.ogl.fichas[2].ruta)+'" />\n')
        f.write('        <ficha id="3" posicion_ruta="'+str(self.ogl.fichas[3].ruta)+'" />\n')
        f.write("      </fichas>\n")
        f.write("    </jugador>\n")
        f.write('    <jugador id="1" nombre="azul" tipo="'+str(0)+'">\n')
        f.write("      <fichas>\n")
        f.write('        <ficha id="4" posicion_ruta="'+str(self.ogl.fichas[4].ruta)+'" />\n')
        f.write('        <ficha id="5" posicion_ruta="'+str(self.ogl.fichas[5].ruta)+'" />\n')
        f.write('        <ficha id="6" posicion_ruta="'+str(self.ogl.fichas[6].ruta)+'" />\n')
        f.write('        <ficha id="7" posicion_ruta="'+str(self.ogl.fichas[7].ruta)+'" />\n')
        f.write("      </fichas>\n")
        f.write("    </jugador>\n")
        f.write('    <jugador id="2" nombre="rojo" tipo="'+str(0)+'">\n')
        f.write("      <fichas>\n")
        f.write('        <ficha id="8" posicion_ruta="'+str(self.ogl.fichas[8].ruta)+'" />\n')
        f.write('        <ficha id="9" posicion_ruta="'+str(self.ogl.fichas[9].ruta)+'" />\n')
        f.write('        <ficha id="10" posicion_ruta="'+str(self.ogl.fichas[10].ruta)+'" />\n')
        f.write('        <ficha id="11" posicion_ruta="'+str(self.ogl.fichas[11].ruta)+'" />\n')
        f.write("      </fichas>\n")
        f.write("    </jugador>\n")
        f.write('    <jugador id="3" nombre="verde" tipo="'+str(0)+'">\n')
        f.write("      <fichas>\n")
        f.write('        <ficha id="12" posicion_ruta="'+str(self.ogl.fichas[12].ruta)+'" />\n')
        f.write('        <ficha id="13" posicion_ruta="'+str(self.ogl.fichas[13].ruta)+'" />\n')
        f.write('        <ficha id="14" posicion_ruta="'+str(self.ogl.fichas[14].ruta)+'" />\n')
        f.write('        <ficha id="15" posicion_ruta="'+str(self.ogl.fichas[15].ruta)+'" />\n')
        f.write("      </fichas>\n")
        f.write("    </jugador>\n")
        f.write("  </jugadores>\n")
        f.write("  <dado ultima_tirada=\"5\" num_debugs=\"0\">\n");
        f.write("     <!-- <debug tirada=\"0\" /> -->\n");
        f.write("  </dado>\n")
        f.write("</partida>\n")
        f.write("</glParchis>\n")
        f.close()

    def volver_a_tirar(self):
        self.actionDado.setEnabled(True)
