## -*- coding: utf-8 -*-
import random
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from libglparchis import *
from Ui_frmInitGame import *

class frmInitGame(QWizard, Ui_frmInitGame):
    def __init__(self, mem,  parent = None, name = None, modal = False):
        QDialog.__init__(self, parent)
        self.mem=mem
        if name:
            self.setObjectName(name)
        self.setupUi(self)
        self.wizardPage1.setTitle(self.tr("Configurar la partida"))
        self.wizardPage1.setSubTitle(self.trUtf8("Selecciona las fichas que van a jugar y quién va a jugar con ellas"))

        self.wizardPage2.setTitle(self.tr("Elegir el jugador que empieza la partida"))
        self.wizardPage2.setSubTitle(self.trUtf8("Tirar el dado de tu color. El jugador que saque la puntuación más alta, empieza la partida"))        
        
        self.setButtonText(QWizard.FinishButton, self.trUtf8("¿Quién empieza?"))
        self.dado={}
        self.playerstarts=None
        
    def tirar_dado(self, color):
        self.dado[color]=int(random.random()*6)+1
    
    def on_cmdYellow_released(self):
        self.tirar_dado("yellow")
#        print ("yellow",  self.dado['yellow'])
        self.lblDadoYellow.setPixmap(self.mem.dado.qpixmap(self.dado['yellow']))
        self.cmdYellow.setEnabled(False)
#        self.chequea()
    
    def on_cmdBlue_released(self):
        self.tirar_dado("blue")
#        print ("blue",  self.dado['blue'])
        self.lblDadoBlue.setPixmap(self.mem.dado.qpixmap(self.dado['blue']))        
        self.cmdBlue.setEnabled(False)
#        self.chequea()
    
    def on_cmdRed_released(self):
        self.tirar_dado("red")
#        print ("red",  self.dado['red'])
        self.lblDadoRed.setPixmap(self.mem.dado.qpixmap(self.dado['red']))
        self.cmdRed.setEnabled(False)
#        self.chequea()
    
    def on_cmdGreen_released(self):
        self.tirar_dado("green")
#        print ("green",  self.dado['green'])
        self.lblDadoGreen.setPixmap(self.mem.dado.qpixmap(self.dado['green']))
        self.cmdGreen.setEnabled(False)
#        self.chequea()
        
    def validateCurrentPage(self):
        if self.currentId()==0:
            #Desactiva el cmd si no juega
            if self.chkYellowPlays.checkState()==Qt.Unchecked:
                self.cmdYellow.setEnabled(False)
            if self.chkBluePlays.checkState()==Qt.Unchecked:
                self.cmdBlue.setEnabled(False)
            if self.chkRedPlays.checkState()==Qt.Unchecked:
                self.cmdRed.setEnabled(False)
            if self.chkGreenPlays.checkState()==Qt.Unchecked:
                self.cmdGreen.setEnabled(False)
            #Tira el dado de IA si juega y si es AI
            if self.chkYellow.checkState()==Qt.Checked and self.chkYellowPlays.checkState()==Qt.Checked:#IA
                self.on_cmdYellow_released()
            if self.chkBlue.checkState()==Qt.Checked and self.chkBluePlays.checkState()==Qt.Checked:#IA
                self.on_cmdBlue_released()
            if self.chkRed.checkState()==Qt.Checked and self.chkRedPlays.checkState()==Qt.Checked:#IA
                self.on_cmdRed_released()
            if self.chkGreen.checkState()==Qt.Checked and self.chkGreenPlays.checkState()==Qt.Checked:#IA
                self.on_cmdGreen_released()
            self.currentPage().setCommitPage(True)#Ya no se puede cambiar nada
            return True
        else:
            if self.playerstarts==None:
                self.chequea()
                return False
            else:
                #Comienza la partida
                self.mem.jugadores.jugador('yellow').name=self.txtYellow.text()
                self.mem.jugadores.jugador('yellow').ia=c2b(self.chkYellow.checkState())
                self.mem.jugadores.jugador('yellow').plays=c2b(self.chkYellowPlays.checkState())
                self.mem.jugadores.jugador('blue').name=self.txtBlue.text()
                self.mem.jugadores.jugador('blue').ia=c2b(self.chkBlue.checkState())
                self.mem.jugadores.jugador('blue').plays=c2b(self.chkBluePlays.checkState())
                self.mem.jugadores.jugador('red').name=self.txtRed.text()
                self.mem.jugadores.jugador('red').ia=c2b(self.chkRed.checkState())
                self.mem.jugadores.jugador('red').plays=c2b(self.chkRedPlays.checkState())
                self.mem.jugadores.jugador('green').name=self.txtGreen.text()
                self.mem.jugadores.jugador('green').ia=c2b(self.chkGreen.checkState())
                self.mem.jugadores.jugador('green').plays=c2b(self.chkGreenPlays.checkState())

                for j in self.mem.jugadores.arr:
                    if j.plays==True:
                        j.fichas.arr[0].mover(0, False,  True)
                        j.fichas.arr[1].mover(0, False,  True)
                        j.fichas.arr[2].mover(0, False,  True)
                        j.fichas.arr[3].mover(0, False,  True)
                self.mem.jugadoractual=self.mem.jugadores.jugador(self.playerstarts)    
                self.mem.jugadoractual.movimientos_acumulados=None#Comidas ymetidas
                self.mem.jugadoractual.LastFichaMovida=None #Se utiliza cuando se va a casa
                print (self.mem.jugadoractual)
                return True
        
    def chequea(self):
            
        #Chequea si han lanzado todos
        if self.cmdYellow.isEnabled()==False and self.cmdBlue.isEnabled()==False and self.cmdRed.isEnabled()==False and self.cmdGreen.isEnabled()==False:
            #Saca el maximo de dado
            max=0
            for color in self.dado:
                if self.dado[color]>max:
                    max=self.dado[color]
            #Busca que colores tienen el maximo
            colormax=[]
            for color in self.dado:
                if self.dado[color]==max:
                    colormax.append(color)
#            print (colormax)
            #Asigna o vuelve a tirar
            if len(colormax)==1:
                self.playerstarts=colormax[0]
                self.lblPlayerStarts.setText(self.trUtf8("El jugador %1 empieza la partida").arg(self.playerstarts))      
                self.setButtonText(QWizard.FinishButton, self.trUtf8("Empieza la partida"))          
            else:
                self.lblPlayerStarts.setText(self.trUtf8("%1 deben tirar hasta que se aclare quién empieza la partida").arg(str(colormax)))                
                self.dado={}
                if 'yellow' not in colormax:
                    self.lblDadoYellow.setPixmap(self.mem.dado.qpixmap(None))
                if 'blue' not in colormax:
                    self.lblDadoBlue.setPixmap(self.mem.dado.qpixmap(None))
                if 'red' not in colormax:
                    self.lblDadoRed.setPixmap(self.mem.dado.qpixmap(None))
                if 'green' not in colormax:
                    self.lblDadoGreen.setPixmap(self.mem.dado.qpixmap(None))
                        
                for c in colormax:
                    #Debe ir primero porque chequea comprueba si esta enabled
                    if c=='yellow' and self.chkYellow.checkState()==Qt.Unchecked:
                        self.cmdYellow.setEnabled(True)
                    if c=='blue' and self.chkBlue.checkState()==Qt.Unchecked:
                        self.cmdBlue.setEnabled(True)
                    if c=='green' and self.chkGreen.checkState()==Qt.Unchecked:
                        self.cmdGreen.setEnabled(True)
                    if c=='red' and self.chkRed.checkState()==Qt.Unchecked:
                        self.cmdRed.setEnabled(True)   
                    
                    if c=='yellow'and self.chkYellow.checkState()==Qt.Checked:
                        self.on_cmdYellow_released()
                    if c=='blue' and self.chkBlue.checkState()==Qt.Checked:
                        self.on_cmdBlue_released()
                    if c=='red' and self.chkRed.checkState()==Qt.Checked:
                        self.on_cmdRed_released()
                    if c=='green' and self.chkGreen.checkState()==Qt.Checked:
                        self.on_cmdGreen_released()
