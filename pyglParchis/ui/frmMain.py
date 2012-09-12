# -*- coding: utf-8 -*-
import sys,    os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from libglparchis import *

from Ui_frmMain import *
from wdgGame import *
from frmAbout import *
from frmInitGame import *
from frmSettings import *

            
class frmMain(QMainWindow, Ui_frmMain):#    
    def __init__(self, parent = 0,  flags = False):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.showMaximized()
        self.game=None

        
    @pyqtSlot()      
    def on_actionAcercaDe_triggered(self):
        fr=frmAbout(self, "frmabout")
        fr.open()
        
    @pyqtSlot()      
    def on_actionSettings_triggered(self):
        f=frmSettings(self)
        f.exec_()
        
    @pyqtSlot()      
    def on_actionSalir_triggered(self):
        sys.exit()
  
    def showWdgGame(self):
        if self.game!=None:
            self.layout.removeWidget(self.game)
        self.game=wdgGame()
        self.layout.addWidget(self.game)
        self.game.assign_mem(self.mem)
        self.actionGuardarPartida.setEnabled(True)
        

    @pyqtSlot()  
    def on_actionRecuperarPartida_triggered(self):
        #ÐEBE SERLOCAL
        filenam=os.path.basename(libglparchis.q2s(QFileDialog.getOpenFileName(self, "", "", "glParchis game (*.glparchis)")))
        if filenam!="":
            self.mem=Mem4()
            self.mem.load(filenam)
            self.showWdgGame()


    @pyqtSlot()  
    def on_actionPartidaNueva_triggered(self):
        self.mem=Mem4()
        initgame=frmInitGame(self.mem)
        salida=initgame.exec_()
        if salida==QDialog.Accepted:
            self.showWdgGame()



    @pyqtSlot()     
    def on_actionGuardarPartida_triggered(self):
        filename=os.path.basename(libglparchis.q2s(QFileDialog.getOpenFileName(self, "", "", "glParchis game (*.glparchis)")))
        if filename!="":
            self.mem.save(filename)
