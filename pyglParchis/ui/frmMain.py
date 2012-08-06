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
        QMainWindow.__init__(self, None)
        self.setupUi(self)
        self.showMaximized()
        
        
    @pyqtSignature("")
    def on_actionAcercaDe_activated(self):
        fr=frmAbout(self, "frmabout")
        fr.open()
        
    @QtCore.pyqtSlot()      
    def on_actionSettings_activated(self):
        f=frmSettings(self)
        f.exec_()
        
    @QtCore.pyqtSlot()      
    def on_actionSalir_activated(self):
        sys.exit()
  
    def showWdgGame(self):
        w=wdgGame(self.mem, self.wdg)
        w.show()
        self.actionGuardarPartida.setEnabled(True)

    @QtCore.pyqtSlot()     
    def on_actionRecuperarPartida_activated(self):
        #ÐEBE SERLOCAL
        self.mem=Mem4()
        filenam=os.path.basename(libglparchis.q2s(QFileDialog.getOpenFileName(self, "", "", "glParchis game (*.glparchis)")))
        self.mem.load(filenam)
        self.showWdgGame()


    @QtCore.pyqtSlot()     
    def on_actionPartidaNueva_activated(self):
#        def save_last_glparchis():
#            try:
#                os.remove(libglparchis.lastfile)
#            except:
#                pass
#            config = ConfigParser.ConfigParser()
#            config.add_section("yellow")
#            config.set("yellow",  'ia', int(libglparchis.c2b(initgame.chkYellow.checkState())))
#            config.set("yellow",  'name', initgame.txtYellow.text())
#            config.set("yellow",  'plays', int(libglparchis.c2b(initgame.chkYellowPlays.checkState())))
#            config.add_section("blue")
#            config.set("blue",  'ia', int(libglparchis.c2b(initgame.chkBlue.checkState())))
#            config.set("blue",  'name', initgame.txtBlue.text())
#            config.set("blue",  'plays', int(libglparchis.c2b(initgame.chkBluePlays.checkState())))
#            config.add_section("red")
#            config.set("red",  'ia', int(libglparchis.c2b(initgame.chkRed.checkState())))
#            config.set("red",  'name', initgame.txtRed.text())
#            config.set("red",  'plays', int(libglparchis.c2b(initgame.chkRedPlays.checkState())))
#            config.add_section("green")
#            config.set("green",  'ia', int(libglparchis.c2b(initgame.chkGreen.checkState())))
#            config.set("green",  'name', initgame.txtGreen.text())
#            config.set("green",  'plays', int(libglparchis.c2b(initgame.chkGreenPlays.checkState())))
#                
#            for color in self.mem.colores():
#                config.set(color.name,  'rutaficha1', 0)
#                config.set(color.name,  'rutaficha2', 0)
#                config.set(color.name,  'rutaficha3', 0)
#                config.set(color.name,  'rutaficha4', 0)
#            config.add_section("game")
#            config.set("game", 'playerstarts', initgame.playerstarts)
#            config.set("game", 'fakedice','')
#            with open(libglparchis.lastfile, 'w') as configfile:
#                config.write(configfile)            
#                
                
        self.mem=Mem4()
        initgame=frmInitGame(self.mem)
        initgame.exec_()
        self.showWdgGame()

        #Graba fichero .glparchis/last.glparchis
#        save_last_glparchis()
        #Carga fichero .glparchis/last.glparchis
#        self.ogl=wdgGame(filename=libglparchis.lastfile)
#        self.load_file(libglparchis.lastfile)




    @QtCore.pyqtSlot()     
    def on_actionGuardarPartida_activated(self):
        filename=os.path.basename(libglparchis.q2s(QFileDialog.getOpenFileName(self, "", "", "glParchis game (*.glparchis)")))
        self.mem.save(filename)
