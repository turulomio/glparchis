import random
#from PyQt5.QtCore import *
#from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from libglparchis import *
from wdgPlayer import *
from wdgPlayerDado import *
from Ui_frmInitGame import *

class frmInitGame(QWizard, Ui_frmInitGame):
    def __init__(self, mem,  parent = None, name = None, modal = False):
        QWizard.__init__(self, parent)
        self.mem=mem
        if name:
            self.setObjectName(name)
        self.setupUi(self)
        self.setGeometry(parent.width()*0.2/2, parent.height()*0.2/2, parent.width()*0.8,  parent.height()*0.8)
        self.wizardPage1.setTitle(self.tr("Configurar la partida"))
        self.wizardPage1.setSubTitle(self.tr("Selecciona las fichas que van a jugar y quién va a jugar con ellas"))

        self.wizardPage2.setTitle(self.tr("Elegir el jugador que empieza la partida"))
        self.wizardPage2.setSubTitle(self.tr("El jugador que saque la puntuación más alta, empieza la partida"))        
        
        self.setButtonText(QWizard.FinishButton, self.tr("Los jugadores lanzan sus dados"))
        self.dado={}
        random.seed(datetime.datetime.now().microsecond)
        self.players=[]#players primera del wizard
        self.set=None #SetWdgPlayers()#Set para tirar dados un turno
        
        for i, j in enumerate(self.mem.jugadores.arr):
            p=wdgPlayer(self)
            self.scrollPlayer.addWidget(p)
            p.setJugador(j)
            p.txt.setText(self.mem.settings.value("Players/{}".format(j.color.name), j.DefaultName()))
            self.players.append(p)
                
        #Pone juega ordenador en todos menos el primero
        for i in range (1, self.mem.maxplayers):
            self.players[i].chkIA.setCheckState(Qt.Checked)
        

    def validateCurrentPage(self):
        """Valida la pestaña del widget"""
        if self.currentId()==0:
            #Desactiva el cmd si no juega
            self.set=SetWdgPlayers()
            for i,  w in enumerate(self.players):
                w.commit()#Rellena objeto jugador
                self.mem.settings.setValue("Players/{}".format(w.jugador.color.name), w.jugador.name)
                if w.chkPlays.checkState()==Qt.Unchecked:#Quita los que no juegan
                    continue
                self.set.arr.append(w)
            self.scrollPlayerDado.addWidget(self.set.qwidget())
            self.currentPage().setCommitPage(True)#Ya no se puede cambiar nada
            return True
        elif self.currentId()==1:
            if self.mem.jugadores.actual==None:
                self.set.Players_throws()
                maxplayers=self.set.arrWdgPlayers_MaximaPuntuacion()
                if len(maxplayers.arr)==1:
                    self.mem.jugadores.actual=maxplayers.arr[0].jugador
                    self.lblPlayerStarts.setStyleSheet('QLabel {font: bold ; color: '+ self.mem.jugadores.actual.color.name+';}')
                    self.lblPlayerStarts.setText(self.tr("El jugador {0} empieza la partida".format(self.mem.jugadores.actual.name)))
                    self.setButtonText(QWizard.FinishButton, self.tr("Empieza la partida"))          
                    return False#Debe haber la validaci´on con playerstarts
                else:#Mas de dos jugadores
                    self.lblPlayerStarts.setText(self.tr("Los jugadores {} deben tirar hasta que se aclare quién empieza la partida".format(maxplayers.strNames())))
                    self.set=maxplayers
                    self.scrollPlayerDado.addWidget(self.set.qwidget())
                    return False
            else:#Si existe playerstarts
                for j in self.mem.jugadores.arr:
                    if j.plays==True:
                        j.fichas.arr[0].mover(0, False,  True)
                        j.fichas.arr[1].mover(0, False,  True)
                        j.fichas.arr[2].mover(0, False,  True)
                        j.fichas.arr[3].mover(0, False,  True)
                self.mem.jugadores.actual.movimientos_acumulados=None#Comidas ymetidas
                self.mem.jugadores.actual.LastFichaMovida=None #Se utiliza cuando se va a casa
                return True
