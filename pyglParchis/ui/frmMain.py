# -*- coding: utf-8 -*-
import sys, os, urllib2
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from libglparchis import *

from Ui_frmMain import *
from wdgGame import *
from frmAbout import *
from frmInitGame import *
from frmSettings import *

            
class frmMain(QMainWindow, Ui_frmMain):#    
    def __init__(self, cfgfile, parent = 0,  flags = False):
        QMainWindow.__init__(self)
        self.cfgfile=cfgfile
        self.setupUi(self)
        self.showMaximized()
        self.game=None
        print (os.getcwd())

        
    @pyqtSlot()      
    def on_actionAcercaDe_triggered(self):
        fr=frmAbout(self,"frmabout")
        fr.open()
        
    @pyqtSlot()      
    def on_actionSettings_triggered(self):
        f=frmSettings(self.cfgfile.language,  self)
        f.exec_()
        self.cfgfile.language=f.language
        self.cfgfile.save()
        if self.game!=None:
            self.game.retranslateUi(self)
            self.game.panel1.retranslateUi(self)
            self.game.panel2.retranslateUi(self)
            self.game.panel3.retranslateUi(self)
            self.game.panel4.retranslateUi(self)
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
        web=urllib2.urlopen('http://glparchis.svn.sourceforge.net/viewvc/glparchis/pyglParchis/libglparchis.py?revision=225&content-type=text%2Fplain')
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
        web.readline()        
    @pyqtSlot()      
    def on_actionSalir_triggered(self):
        QtCore.QCoreApplication.instance().quit()
  
    def showWdgGame(self):
        self.actionSound.setEnabled(True)
        if self.game!=None:
            self.layout.removeWidget(self.game)      
        self.game=wdgGame()
        self.layout.addWidget(self.game)
        self.game.assign_mem(self.mem)
        self.actionGuardarPartida.setEnabled(True)
        

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
        initgame=frmInitGame(self.mem)
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
