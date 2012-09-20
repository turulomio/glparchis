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
            self.on_actionUpdates_triggered()
        
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
            self.game.panel1.retranslateUi(self)
            self.game.panel2.retranslateUi(self)
            self.game.panel3.retranslateUi(self)
            self.game.panel4.retranslateUi(self)
            self.game.panel1.setJugador(self.mem.jugadores.jugador("yellow"))
            self.game.panel2.setJugador(self.mem.jugadores.jugador("blue"))
            self.game.panel3.setJugador(self.mem.jugadores.jugador("red"))
            self.game.panel4.setJugador(self.mem.jugadores.jugador("green"))
            self.game.panel1.repaint()
            self.game.panel2.repaint()
            self.game.panel3.repaint()
            self.game.panel4.repaint()
        self.retranslateUi(self)
        self.repaint()
        
    @pyqtSlot()      
    def on_actionSound_triggered(self):
        self.game.mem.sound=not self.game.mem.sound
        if self.game.mem.sound:
            self.actionSound.setText(self.trUtf8("Sonido encendido"))
        else:
            self.actionSound.setText(self.trUtf8("Sonido apagado"))
        
    @pyqtSlot()      
    def on_actionUpdates_triggered(self):
        try:
            web=urllib2.urlopen('http://glparchis.svn.sourceforge.net/viewvc/glparchis/pyglParchis/libglparchis.py?content-type=text%2Fplain')
        except:
            web=None
        if web==None:
            m=QMessageBox()
            m.setIcon(QMessageBox.Information)
            m.setText(self.trUtf8("No se ha podido comprobar si hay actualizaciones. Inténtelo más tarde."))
            m.exec_() 
        for line in web.readlines():
            if line.find('version="')!=-1:
                remoteversion=line.split('"')[1]
                if version!=remoteversion:
                    m=QMessageBox()
                    m.setIcon(QMessageBox.Information)
                    m.setTextFormat(Qt.RichText)#this is what makes the links clickable
                    m.setText(self.trUtf8("Hay una nueva versión del programa. Bájatela de <a href='http://glparchis.sourceforge.net'>http://glparchis.sourceforge.net</a>"))
                    m.exec_() 
                else:
                    m=QMessageBox()
                    m.setIcon(QMessageBox.Information)
                    m.setText(self.trUtf8("Dispone de la última versión del juego"))
                    m.exec_() 
        self.cfgfile.lastupdate=datetime.date.today().toordinal()
        self.cfgfile.save()
        
    @pyqtSlot()      
    def on_actionSalir_triggered(self):
        print ("salidendo")
        if self.game:
            self.game.stopthegame=True
            del (self.game)
            self.game=None
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
            del self.game 
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
            self.mem=Mem4()
            self.mem.cfgfile=self.cfgfile
            self.mem.load(filenam)
            self.mem.jugadores.jugador("yellow").name=self.cfgfile.yellowname
            self.mem.jugadores.jugador("blue").name=self.cfgfile.bluename
            self.mem.jugadores.jugador("red").name=self.cfgfile.redname
            self.mem.jugadores.jugador("green").name=self.cfgfile.greenname
            self.showWdgGame()
        os.chdir(cwd)


    @pyqtSlot()  
    def on_actionPartidaNueva_triggered(self):
        self.mem=Mem4()
        self.mem.cfgfile=self.cfgfile
        initgame=frmInitGame(self.mem,  self)
        salida=initgame.exec_()
        if salida==QDialog.Accepted:
            self.showWdgGame()



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
