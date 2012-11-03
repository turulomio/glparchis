# -*- coding: utf-8 -*-
import sys, os, urllib2,  datetime
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from libglparchis import *

from Ui_frmMain import *
from wdgGame import *
from frmAbout import *
from frmInitGame import *
from frmSettings import *
from frmHelp import *

            
class frmMain(QMainWindow, Ui_frmMain):#    
    def __init__(self, cfgfile, parent = 0,  flags = False):
        QMainWindow.__init__(self)
        self.cfgfile=cfgfile
        self.setupUi(self)
        self.showMaximized()
        self.game=None
        if datetime.date.today()-datetime.date.fromordinal(self.cfgfile.lastupdate)>=datetime.timedelta(days=7):
            print ("Actualizando")
            self.checkUpdates(False)
        
    @pyqtSlot()      
    def on_actionAcercaDe_triggered(self):
        fr=frmAbout(self,"frmabout")
        fr.open()
                
    @pyqtSlot()      
    def on_actionHelp_triggered(self):
        fr=frmHelp(self,"frmHelp")
        fr.open()
        
    @pyqtSlot()      
    def on_actionSettings_triggered(self):
        f=frmSettings(self.cfgfile,   self)
        f.exec_()
        if self.game!=None:
            self.game.retranslateUi(self)
            for p in self.game.panels:
                p.retranslateUi(self)
                p.repaint()
                p.setJugador(p.jugador)#Se repinta
        self.retranslateUi(self)
        self.repaint()
        
    @pyqtSlot()      
    def on_actionSound_triggered(self):
        self.game.mem.sound=not self.game.mem.sound
        if self.game.mem.sound:
            self.actionSound.setText(self.trUtf8("Sonido encendido"))       
            icon8 = QtGui.QIcon()
            icon8.addPixmap(QtGui.QPixmap(":/glparchis/sound.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionSound.setIcon(icon8)
        else:
            self.actionSound.setText(self.trUtf8("Sonido apagado"))
            icon8 = QtGui.QIcon()
            icon8.addPixmap(QtGui.QPixmap(":/glparchis/soundoff.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionSound.setIcon(icon8)
        
    @pyqtSlot()      
    def on_actionUpdates_triggered(self):
        self.checkUpdates(True)
        
    def checkUpdates(self, showdialogwhennoupdates=False):
        #Chequea en Internet
        try:
            web=urllib2.urlopen('https://sourceforge.net/projects/glparchis/files/glparchis/').read()
        except:
            web=None
        #Si hay error de internet avisa
        if web==None:
            if showdialogwhennoupdates==True:
                m=QMessageBox()
                m.setIcon(QMessageBox.Information)
                m.setText(self.trUtf8("No se ha podido comprobar si hay actualizaciones. Inténtelo más tarde."))
                m.exec_() 
            return
        #Saca la version de internet
        remoteversion=None
        for line in web.split("\n"):
            if line.find('folder warn')!=-1:
                remoteversion=line.split('glparchis-')[1].split('"') [0]
                break
        #Si no hay version sale
        print ("Remote version",  remoteversion)
        if remoteversion==None:
            return
                
        if remoteversion==version.replace("+", ""):#Quita el más de desarrollo 
            if showdialogwhennoupdates==True:
                m=QMessageBox()
                m.setIcon(QMessageBox.Information)
                m.setText(self.trUtf8("Dispone de la última versión del juego"))
                m.exec_() 
        else:
            m=QMessageBox()
            m.setIcon(QMessageBox.Information)
            m.setTextFormat(Qt.RichText)#this is what makes the links clickable
            m.setText(self.trUtf8("Hay una nueva versión del programa. Bájatela de la página web del proyecto <a href='http://glparchis.sourceforge.net'>http://glparchis.sourceforge.net</a> o directamente desde <a href='https://sourceforge.net/projects/glparchis/files/glparchis/glparchis-")+remoteversion+"/'>Sourceforge</a>")
            m.exec_()                 
        self.cfgfile.lastupdate=datetime.date.today().toordinal()
        self.cfgfile.save()
        
    @pyqtSlot()      
    def on_actionSalir_triggered(self):
        print ("saliendo")
        if self.game:
            self.game.__del__()
        qApp.closeAllWindows()
        qApp.exit()
        sys.exit(0)
        
    @pyqtSlot(QEvent)   
    def closeEvent(self,event):
        self.on_actionSalir_triggered()
  
    def showWdgGame(self):
        self.actionSound.setEnabled(True)
        if self.game!=None:
            self.layout.removeWidget(self.game)    
            self.game.__del__()
#            self.game.deleteLater()
        self.game=wdgGame(self)
        self.game.stopthegame=False
        self.layout.addWidget(self.game)
        self.actionGuardarPartida.setEnabled(True)
        self.game.assign_mem(self.mem)
        

    @pyqtSlot()  
    def on_actionRecuperarPartida_triggered(self):
        cwd=os.getcwd()
        os.chdir(os.path.expanduser("~/.glparchis/"))
        #ÐEBE SERLOCAL
        filenam=os.path.basename(libglparchis.q2s(QFileDialog.getOpenFileName(self, "", "", "glParchis game (*.glparchis)")))
        if filenam!="":
            #Busca si es de 4,6,8
            self.mem=self.selectMem(filenam)
            #Lo carga
            self.mem.cfgfile=self.cfgfile
            if self.mem.load(filenam)==False:
                self.mem=None
                return
            for i, j in enumerate(self.mem.jugadores.arr):
                j.name=self.cfgfile.names[i]
#            self.mem.jugadores.jugador("yellow").name=self.cfgfile.yellowname
#            self.mem.jugadores.jugador("blue").name=self.cfgfile.bluename
#            self.mem.jugadores.jugador("red").name=self.cfgfile.redname
#            self.mem.jugadores.jugador("green").name=self.cfgfile.greenname
            self.showWdgGame()
        os.chdir(cwd)

    def selectMem(self, filename):
        resultado=None
        cwd=os.getcwd()
        os.chdir(os.path.expanduser("~/.glparchis/"))
        config = ConfigParser.ConfigParser()
        config.read(filename)
        try:
            self.maxplayers=int(config.get("game",  "numplayers"))
        except:
            resultado=Mem4()
            os.chdir(cwd)
            return resultado            
        os.chdir(cwd)
            
        if self.maxplayers==4:
            resultado=Mem4()
        elif self.maxplayers==6:
            resultado=Mem6()
        elif self.maxplayers==8:
            resultado=Mem8()
        return resultado



    @pyqtSlot()  
    def on_actionPartidaNueva4_triggered(self):
        self.mem=Mem4()
        self.mem.cfgfile=self.cfgfile
        initgame=frmInitGame(self.mem,  self)
        salida=initgame.exec_()
        if salida==QDialog.Accepted:
            self.showWdgGame()

    @pyqtSlot()  
    def on_actionPartidaNueva6_triggered(self):
        if developing()==True:
            self.mem=Mem6()
            self.mem.cfgfile=self.cfgfile
            initgame=frmInitGame(self.mem,  self)
            salida=initgame.exec_()
            if salida==QDialog.Accepted:
                self.showWdgGame()

    @pyqtSlot()  
    def on_actionPartidaNueva8_triggered(self):
        if developing()==True:
            self.mem=Mem8()
            self.mem.cfgfile=self.cfgfile
            initgame=frmInitGame(self.mem,  self)
            salida=initgame.exec_()
            if salida==QDialog.Accepted:
                self.showWdgGame()
                
#        if developing()==True:
#            self.mem=Mem8()
#            self.mem.cfgfile=self.cfgfile
#            for j in self.mem.jugadores.arr:
#                j.name=j.color.name
#                j.plays=True
#                j.ia=False
#                self.mem.jugadores.actual=j
#                posicion=0
#                count=0
#
#                for f in j.fichas.arr:
#                    f.mover(1, False,  True)
#            self.showWdgGame()
                
                
#        if developing()==True:
#            self.mem=Mem8()
#            self.mem.cfgfile=self.cfgfile
#            for j in self.mem.jugadores.arr:
#                j.name=j.color.name
#                j.plays=True
#                j.ia=False
#                self.mem.jugadores.actual=self.mem.jugadores.jugador("blue")
#                posicion=0
#                count=0
#
#                for f in j.fichas.arr:
#                    f.mover(posicion, False,  True)
#                    if count==1:
#                        posicion=posicion+3
#                        count=0
#                    else:
#                        count=count+1
#            self.showWdgGame()



    @pyqtSlot()     
    def on_actionGuardarPartida_triggered(self):
        cwd=os.getcwd()
        os.chdir(os.path.expanduser("~/.glparchis/"))
        filename=os.path.basename(libglparchis.q2s(QFileDialog.getSaveFileName(self, "", "", "glParchis game (*.glparchis)")))
        if filename!="":       
            if os.path.splitext(filename)[1]!=".glparchis":
                filename=filename+".glparchis"
            self.mem.save(filename)
        os.chdir(cwd)
