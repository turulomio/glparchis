 
import random
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from libglparchis import *
from wdgPlayer import *
from wdgPlayerDado import *
from Ui_frmInitGame import *

class frmInitGame(QWizard, Ui_frmInitGame):
    def __init__(self, mem,  parent = None, name = None, modal = False):
        QDialog.__init__(self, parent)
        
        self.mem=mem
        if name:
            self.setObjectName(name)
        self.setupUi(self)
        self.setGeometry(parent.width()*0.1/2, parent.height()*0.1/2, parent.width()*0.9,  parent.height()*0.9)
        self.wizardPage1.setTitle(self.tr("Configurar la partida"))
        self.wizardPage1.setSubTitle(self.tr("Selecciona las fichas que van a jugar y quién va a jugar con ellas"))

        self.wizardPage2.setTitle(self.tr("Elegir el jugador que empieza la partida"))
        self.wizardPage2.setSubTitle(self.tr("Tirar el dado de tu color. El jugador que saque la puntuación más alta, empieza la partida"))        
        
        self.setButtonText(QWizard.FinishButton, self.tr("¿Quién empieza?"))
        self.dado={}
        self.playerstarts=None
        random.seed(datetime.datetime.now().microsecond)
        self.wdgplayers=[]
        self.wdgplayersdado=[]
        
        for i, j in enumerate(self.mem.jugadores.arr):
            p=wdgPlayer(self)
            self.scrollPlayer.addWidget(p)
            p.setJugador(j)
            self.wdgplayers.append(p)

            d=wdgPlayerDado(mem, j,  self)
            self.scrollPlayerDado.addWidget(d)
            self.wdgplayersdado.append(d)
            self.wdgplayers[i].txt.setText( (self.mem.cfgfile.names[i]))

                
        #Pone juega ordenador en todos menos el primero
        for i in range (1, self.mem.maxplayers):
            self.wdgplayers[i].chkIA.setCheckState(Qt.Checked)
        
        self.currentIdChanged.connect(self.on_currentIdChanged)
            
#        QObject.connect(self, SIGNAL("currentIdChanged(int)"), self.on_currentIdChanged)                 
            
    def on_currentIdChanged(self, id):
        QCoreApplication.processEvents();   
        self.repaint()
        QCoreApplication.processEvents();   
        if id==1:
            time.sleep(1)
            for i,  w in enumerate(self.wdgplayers):
                if w.chkIA.checkState()==Qt.Checked and w.chkPlays.checkState()==Qt.Checked:#IA#Tira el dado de IA si juega y si es AI
                    self.wdgplayersdado[i].on_cmd_released()

    def validateCurrentPage(self):
        if self.currentId()==0:
            #Desactiva el cmd si no juega
            for i,  w in enumerate(self.wdgplayers):
                if w.chkPlays.checkState()==Qt.Unchecked:
                    self.wdgplayersdado[i].cmd.setEnabled(False)
                w.commit()
                self.mem.cfgfile.names[i]=self.wdgplayers[i].txt.text()
                self.wdgplayersdado[i].setName(self.wdgplayers[i].txt.text())
            self.mem.cfgfile.save()
            self.currentPage().setCommitPage(True)#Ya no se puede cambiar nada
            return True
        else:#Pagina 1
            if self.playerstarts==None:
                self.chequea()
                return False
            else:                
                for j in self.mem.jugadores.arr:
                    if j.plays==True:
                        j.fichas.arr[0].mover(0, False,  True)
                        j.fichas.arr[1].mover(0, False,  True)
                        j.fichas.arr[2].mover(0, False,  True)
                        j.fichas.arr[3].mover(0, False,  True)
                self.mem.jugadores.actual=self.mem.jugadores.jugador(self.playerstarts)    
                self.mem.jugadores.actual.movimientos_acumulados=None#Comidas ymetidas
                self.mem.jugadores.actual.LastFichaMovida=None #Se utiliza cuando se va a casa
                print (self.mem.jugadores.actual)
                return True
        
    def hanTiradoTodos(self):
        """Función que comprueba si han tirado todos"""
        resultado=True
        for w in self.wdgplayersdado:
            if w.cmd.isEnabled():
                resultado=False
        return resultado
        
    def maximaPuntuacion(self):
        resultado=0
        for w in self.wdgplayersdado:
            if w.tirada>resultado:
                resultado=w.tirada
        return resultado
        
    def wdgPlayerDado_maximapuntuacion(self, maxima):
        resultado=[]
        for w in self.wdgplayersdado:
            if w.tirada==maxima:
                resultado.append(w)
        return resultado
        
    def maxplayers2colors(self, maxplayers):
        resultado=[]
        for w in maxplayers:
            resultado.append(w.jugador.color.name)
        return resultado
    
        
        
    def chequea(self):
        #Chequea si han lanzado todos
        if self.hanTiradoTodos():
            #Saca el maximo de dado
            max=self.maximaPuntuacion()
            #Busca que colores tienen el maximo
            maxplayers=self.wdgPlayerDado_maximapuntuacion(max)
            #Asigna o vuelve a tirar
            if len(maxplayers)==1:
                self.playerstarts=maxplayers[0].jugador.color.name
                self.lblPlayerStarts.setText(self.tr("El jugador {0} empieza la partida".format(self.playerstarts)))
                self.setButtonText(QWizard.FinishButton, self.tr("Empieza la partida"))          
            else:
                self.lblPlayerStarts.setText(self.tr("{0} deben tirar hasta que se aclare quién empieza la partida".format(self.maxplayers2colors(maxplayers))))
                for w in self.wdgplayersdado:
                    if w not in maxplayers:
                        w.lblDado.setPixmap(self.mem.dado.qpixmap(None))
                        w.tirada=0
                    else:
                        w.cmd.setEnabled(True)
                        if w.jugador.ia==True:
                            w.on_cmd_released()
                    
