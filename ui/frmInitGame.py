## -*- coding: utf-8 -*-
import random
from PyQt4.QtCore import *
from PyQt4.QtGui import *
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
        self.wizardPage1.setSubTitle(self.trUtf8("Selecciona las fichas que van a jugar y quién va a jugar con ellas"))

        self.wizardPage2.setTitle(self.tr("Elegir el jugador que empieza la partida"))
        self.wizardPage2.setSubTitle(self.trUtf8("Tirar el dado de tu color. El jugador que saque la puntuación más alta, empieza la partida"))        
        
        self.setButtonText(QWizard.FinishButton, self.trUtf8("¿Quién empieza?"))
        self.dado={}
        self.playerstarts=None
        random.seed(datetime.datetime.now().microsecond)
        self.wdgplayers=[]
        self.wdgplayersdado=[]
        
        for j in self.mem.jugadores.arr:
            p=wdgPlayer(self)
            self.scrollPlayer.addWidget(p)
            p.setJugador(j)
            self.wdgplayers.append(p)

            d=wdgPlayerDado(mem, j,  self)
            self.scrollPlayerDado.addWidget(d)
            self.wdgplayersdado.append(d)
        
        
        if self.mem.cfgfile.yellowname!=None:
            if self.mem.maxplayers>=4:
                self.wdgplayers[0].txt.setText(self.mem.cfgfile.yellowname)
                self.wdgplayers[1].txt.setText(self.mem.cfgfile.bluename)
                self.wdgplayers[2].txt.setText(self.mem.cfgfile.redname)
                self.wdgplayers[3].txt.setText(self.mem.cfgfile.greenname)
            if self.mem.maxplayers>=6:
                self.wdgplayers[4].txt.setText(self.mem.cfgfile.grayname)
                self.wdgplayers[5].txt.setText(self.mem.cfgfile.pinkname)
            if self.mem.maxplayers>=8:
                self.wdgplayers[4].txt.setText(self.mem.cfgfile.orangename)
                self.wdgplayers[5].txt.setText(self.mem.cfgfile.cyanname)
                
        #Pone juega ordenador en todos menos el primero
        for i in range (1, self.mem.maxplayers):
            self.wdgplayers[i].chkIA.setCheckState(Qt.Checked)
        
    def validateCurrentPage(self):
        if self.currentId()==0:
            #Desactiva el cmd si no juega
            for i,  w in enumerate(self.wdgplayers):
                if w.chkPlays.checkState()==Qt.Unchecked:
                    self.wdgplayersdado[i].cmd.setEnabled(False)
                if w.chkIA.checkState()==Qt.Checked and w.chkPlays.checkState()==Qt.Checked:#IA#Tira el dado de IA si juega y si es AI
                    self.wdgplayersdado[i].on_cmd_released()
                w.commit()
                if self.mem.maxplayers>=4:
                    self.mem.cfgfile.yellowname=self.wdgplayers[0].txt.text()
                    self.mem.cfgfile.bluename=self.wdgplayers[1].txt.text()
                    self.mem.cfgfile.redname=self.wdgplayers[2].txt.text()
                    self.mem.cfgfile.greenname=self.wdgplayers[3].txt.text()
                if self.mem.maxplayers>=6:
                    self.mem.cfgfile.grayname=self.wdgplayers[4].txt.text()
                    self.mem.cfgfile.pinkname=self.wdgplayers[5].txt.text()
                if self.mem.maxplayers>=8:
                    self.mem.cfgfile.orangename=self.wdgplayers[6].txt.text()
                    self.mem.cfgfile.cyanname=self.wdgplayers[7].txt.text()
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
        """Funci´on que comprueba si han tirado todos"""
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
                self.lblPlayerStarts.setText(self.trUtf8("El jugador %1 empieza la partida").arg(self.playerstarts))      
                self.setButtonText(QWizard.FinishButton, self.trUtf8("Empieza la partida"))          
            else:
                self.lblPlayerStarts.setText(self.trUtf8("%1 deben tirar hasta que se aclare quién empieza la partida").arg(str(self.maxplayers2colors(maxplayers))))                
                for w in self.wdgplayersdado:
                    if w not in maxplayers:
                        w.lblDado.setPixmap(self.mem.dado.qpixmap(None))
                        w.tirada=0
                    else:
                        w.cmd.setEnabled(True)
                        if w.jugador.ia==True:
                            w.on_cmd_released()
                    
