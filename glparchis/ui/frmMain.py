import sys, os, urllib.request,   datetime
from urllib.request import urlopen
from PyQt5.QtCore import QTranslator, Qt, pyqtSlot, QEvent,  QUrl,  pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QKeyEvent, QDesktopServices
from PyQt5.QtWidgets import QMainWindow, QMessageBox, qApp, QDialog, QFileDialog
from glparchis.libglparchis import str2bool, cargarQTranslator, b2s, qmessagebox,  Mem3, Mem4, Mem6, Mem8,  SoundSystem
from glparchis.version import __versiondate__

import configparser
from glparchis.ui.Ui_frmMain import Ui_frmMain
from glparchis.ui.wdgGame import wdgGame
from glparchis.ui.frmAbout import frmAbout
from glparchis.ui.frmGameStatistics import frmGameStatistics
from glparchis.ui.frmInitGame import frmInitGame
from glparchis.ui.frmSettings import frmSettings
from glparchis.ui.frmHelp import frmHelp
from uuid import uuid4

## Pantalla principal de glparchis
class frmMain(QMainWindow, Ui_frmMain):
    showLeftPanel=pyqtSignal(bool)
    def __init__(self, settings, parent = 0,  flags = False):
        QMainWindow.__init__(self)
        self.path_program=os.getcwd()
        self.path_autosaves=os.path.expanduser("~/.glparchis/")
        self.settings=settings
        self.translator=QTranslator()
        cargarQTranslator(self.translator, settings.value("frmSettings/language", "en"))
        
        self.sound=SoundSystem()
        
        self.setupUi(self)
        self.showMaximized()
        self.game=None
        self.setWindowTitle(self.tr("glParchis 2010-{}. GNU General Public License \xa9").format(__versiondate__.year))
        if datetime.date.today()-datetime.date.fromordinal(int(self.settings.value("frmMain/lastupdate", 1)))>=datetime.timedelta(days=7):
            print ("Actualizando")
            self.checkUpdates(False)
        self.setSound(str2bool(self.settings.value("frmSettings/sound", "True")))
        self.setFullScreen(str2bool(self.settings.value("frmMain/fullscreen", "False")))
        self.setAutomaticDice(str2bool(self.settings.value("frmMain/automaticdice", "False")))
        self.setLeftPanel(str2bool(self.settings.value("frmMain/panel", "True")))
        self.setInstallationUUID()
        

        
    def setInstallationUUID(self):
        """
            Sets an update UUID
        """
        if self.settings.value("frmMain/uuid", "None")=="None":
            self.settings.setValue("frmMain/uuid", str(uuid4()))
            if str2bool(self.settings.value("frmSettings/statistics", "True"))==True:
                url='http://glparchis.sourceforge.net/php/glparchis_installations.php?uuid={}'.format(self.settings.value("frmMain/uuid"))
                print(url)
                try:
                    web=b2s(urlopen(url).read())
                except:
                    web=None
                print (web)       
        else:
            print(self.tr("Installation UUID already set"))



    def setFullScreen(self, boolean):
        if boolean==False:
            self.actionFullScreen.setText(self.tr("Cambiar al modo de pantalla completa"))
            self.actionFullScreen.setToolTip(self.tr("Cambiar al modo de pantalla completa"))
            self.actionFullScreen.setChecked(False)
            self.menuBar.show()
            self.removeToolBar(self.toolBar);
            self.addToolBar(Qt.TopToolBarArea, self.toolBar)
            self.toolBar.show()
            self.showNormal()
            self.showMaximized()
        else:      
            self.actionFullScreen.setText(self.tr("Salir del modo de pantalla completa"))
            self.actionFullScreen.setToolTip(self.tr("Salir del modo de pantalla completa"))
            self.actionFullScreen.setChecked(True)
            self.menuBar.hide()
            self.removeToolBar(self.toolBar);
            self.addToolBar(Qt.LeftToolBarArea, self.toolBar)
            self.toolBar.show()
            self.showFullScreen()
        self.settings.setValue("frmMain/fullscreen", str(boolean))
        self.showLeftPanel.emit(self.actionLeftPanel.isChecked())        

    @pyqtSlot()      
    def on_actionAcercaDe_triggered(self):
        fr=frmAbout(self,"frmabout")
        fr.open()

    ## Se ejecuta cuando se pulsa el actionAutomatism
    @pyqtSlot()
    def on_actionAutomatism_triggered(self):
        self.setAutomaticDice(not str2bool(self.settings.value("frmMain/automaticdice")))
        
    ## Función que establece el automatismo del dado en el action y guarda el setting
    def setAutomaticDice(self,  boolean):
        if boolean==True:
            self.actionAutomatism.setToolTip(self.tr("Pulse para desactivar el automatismo del dado y en caso de poder mover solo una ficha")) 
            self.actionAutomatism.setText(self.tr("Desactiva el automatismo del dado")) 
            icon8 = QIcon()
            icon8.addPixmap(QPixmap(":/glparchis/stop.png"), QIcon.Normal, QIcon.Off)
            self.actionAutomatism.setIcon(icon8)
            self.actionAutomatism.setChecked(True)
        else:
            self.actionAutomatism.setToolTip(self.tr("Pulse para mover automaticamente el dado y las fichas cuando solo se pueda mover una"))
            self.actionAutomatism.setText(self.tr("Activa el automatismo del dado")) 
            icon8 = QIcon()
            icon8.addPixmap(QPixmap(":/glparchis/play.png"), QIcon.Normal, QIcon.Off)
            self.actionAutomatism.setIcon(icon8)
            self.actionAutomatism.setChecked(False)
        self.settings.setValue("frmMain/automaticdice", str(boolean))

    ## Se ejecuta cuando se pulsa el actionPanel
    @pyqtSlot()
    def on_actionLeftPanel_triggered(self):
        self.setLeftPanel(not str2bool(self.settings.value("frmMain/panel")))
        
    ## Función que muestra o oculta el panel izquierdo
    def setLeftPanel(self,  boolean):
        if boolean==True:
            self.actionLeftPanel.setToolTip(self.tr("Pulse para ocultar el panel izquierdo")) 
            self.actionLeftPanel.setText(self.tr("Oculta el panel izquierdo")) 
            self.actionLeftPanel.setChecked(True)
        else:
            self.actionLeftPanel.setToolTip(self.tr("Pulse para mostrar el panel izquierdo"))
            self.actionLeftPanel.setText(self.tr("Muestra el panel izquierdo")) 
            self.actionLeftPanel.setChecked(False)
        self.settings.setValue("frmMain/panel", str(boolean))
        self.showLeftPanel.emit(boolean)        

    @pyqtSlot()      
    def on_actionFullScreen_triggered(self):
        self.setFullScreen(not self.isFullScreen())
                
    @pyqtSlot()      
    def on_actionHelp_triggered(self):
        fr=frmHelp(self,"frmHelp")
        fr.open()
        
    @pyqtSlot()      
    def on_actionSettings_triggered(self):
        f=frmSettings(self.settings, self.translator,    self)
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
        self.setSound(not str2bool(self.settings.value("frmSettings/sound")))
    
    def setSound(self, boolean):
        if boolean==True:
            self.actionSound.setText(self.tr("Sonido encendido")) 
            icon8 = QIcon()
            icon8.addPixmap(QPixmap(":/glparchis/sound.png"), QIcon.Normal, QIcon.Off)
            self.actionSound.setIcon(icon8)
        else:
            self.actionSound.setText(self.tr("Sonido apagado"))
            icon8 = QIcon()
            icon8.addPixmap(QPixmap(":/glparchis/soundoff.png"), QIcon.Normal, QIcon.Off)
            self.actionSound.setIcon(icon8)
        self.settings.setValue("frmSettings/sound", str(boolean))
        
    @pyqtSlot()      
    def on_actionUpdates_triggered(self):
        self.checkUpdates(True)
        
    def checkUpdates(self, showdialogwhennoupdates=False):
        #Chequea en Internet
        try:
            web=b2s(urllib.request.urlopen('https://sourceforge.net/projects/glparchis/files/glparchis/').read())
        except:
            web=None
        #Si hay error de internet avisa
        if web==None:
            if showdialogwhennoupdates==True:
                qmessagebox(self.tr("No se ha podido comprobar si hay actualizaciones. Intentelo mas tarde."))
            return
        #Saca la version de internet
        remoteversion=None
        for line in web.split("\n"):
            if line.find('class="folder "')!=-1:
                remoteversion=line.split('glparchis-')[1].split('"') [0]
                break
        #Si no hay version sale
        print ("Remote version",  remoteversion)
        if remoteversion==None:
            return
        dateremoteversion=datetime.date(int(remoteversion[:4]), int(remoteversion[4:6]), int(remoteversion[6:8]))
                
        if dateremoteversion==__versiondate__:
            if showdialogwhennoupdates==True:
                qmessagebox(self.tr("Dispone de la ultima version del juego"))
        else:
            m=QMessageBox()
            m.setIcon(QMessageBox.Information)
            m.setWindowIcon(QIcon(":glparchis/ficharoja.png"))
            m.setTextFormat(Qt.RichText)#this is what makes the links clickable
            m.setText(self.tr("Hay una nueva version del programa. Bajatela de la pagina web del proyecto <a href='http://glparchis.sourceforge.net'>http://glparchis.sourceforge.net</a> o directamente desde <a href='https://sourceforge.net/projects/glparchis/files/glparchis/glparchis-")+remoteversion+"/'>Sourceforge</a>")
            m.exec_() 
        self.settings.setValue("frmMain/lastupdate", datetime.date.today().toordinal())
        

        
    @pyqtSlot(QEvent)   
    def closeEvent(self,event):   
        print ("saliendo")
        if self.game:
            self.game.__del__()
        qApp.closeAllWindows()
        qApp.exit()
        sys.exit(0)
  
    def showWdgGame(self):
        self.actionSound.setEnabled(True)
        self.mem.delay=int(self.settings.value("frmSettings/delay", 300))
        self.mem.difficulty=int(self.settings.value("frmSettings/difficulty", 70))
        if self.game!=None:
            self.layout.removeWidget(self.game)    
            self.game.__del__()
        self.game=wdgGame(self)
        
        self.game.stopthegame=False
        self.layout.addWidget(self.game)
        self.actionGuardarPartida.setEnabled(True)
        self.actionAcercarTablero.setEnabled(True)
        self.actionAlejarTablero.setEnabled(True)
        self.game.assign_mem(self.mem)

    @pyqtSlot()  
    def on_actionAcercarTablero_triggered(self):
        event=QKeyEvent(QEvent.KeyPress, Qt.Key_Plus, Qt.NoModifier, 0, 0, 0)
        self.game.ogl.keyPressEvent(event)

    @pyqtSlot()  
    def on_actionAlejarTablero_triggered(self):
        event=QKeyEvent(QEvent.KeyPress, Qt.Key_Minus, Qt.NoModifier, 0, 0, 0)
        self.game.ogl.keyPressEvent(event)



    @pyqtSlot()  
    def on_actionRecuperarPartida_triggered(self):
        os.chdir(self.path_autosaves)
        #ÐEBE SERLOCAL
        filenam=os.path.basename(QFileDialog.getOpenFileName(self, "", "", "glParchis game (*.glparchis)")[0])
        if filenam!="":
            #Busca si es de 4,6,8
            self.mem=self.selectMem(filenam)
            self.mem.settings=self.settings
            self.mem.translator=self.translator
            self.mem.frmMain=self
            if self.mem.load(filenam)==False:
                self.mem=None
                return
            for i, j in enumerate(self.mem.jugadores.arr):
                j.name=self.mem.settings.value("Players/{}".format(j.color.name), j.DefaultName())
            self.showWdgGame()
            
    @pyqtSlot()
    def on_actionReportBug_triggered(self):
        QDesktopServices.openUrl(QUrl('https://sourceforge.net/p/glparchis/tickets/'))

    def selectMem(self, filename):
        resultado=None
        os.chdir(self.path_autosaves)
        config = configparser.ConfigParser()
        config.read(filename)
        try:
            self.maxplayers=int(config.get("game",  "numplayers"))
        except:
            resultado=Mem4()
            return resultado  
            
        if self.maxplayers==4:
            resultado=Mem4()
        elif self.maxplayers==3:
            resultado=Mem3()
        elif self.maxplayers==6:
            resultado=Mem6()
        elif self.maxplayers==8:
            resultado=Mem8()
        return resultado



    @pyqtSlot()  
    def on_actionMundialStatistics_triggered(self):
        uuid=self.settings.value("frmMain/uuid", "None")
        fr=frmGameStatistics(uuid, self)
        fr.exec_()

            
    @pyqtSlot()  
    def on_actionPartidaNueva3_triggered(self):
        self.mem=Mem3()
        self.mem.settings=self.settings
        self.mem.translator=self.translator
        self.mem.frmMain=self
        initgame=frmInitGame(self.mem,  self)
        salida=initgame.exec_()
        if salida==QDialog.Accepted:
            self.showWdgGame()            
            
    @pyqtSlot()  
    def on_actionPartidaNueva4_triggered(self):
        self.mem=Mem4()
        self.mem.settings=self.settings
        self.mem.translator=self.translator
        self.mem.frmMain=self
        initgame=frmInitGame(self.mem,  self)
        salida=initgame.exec_()
        if salida==QDialog.Accepted:
            self.showWdgGame()

    @pyqtSlot()  
    def on_actionPartidaNueva6_triggered(self):
        self.mem=Mem6()
        self.mem.settings=self.settings
        self.mem.translator=self.translator
        self.mem.frmMain=self
        initgame=frmInitGame(self.mem,  self)
        salida=initgame.exec_()
        if salida==QDialog.Accepted:
            self.showWdgGame()


    @pyqtSlot()  
    def on_actionPartidaNueva8_triggered(self):
        self.mem=Mem8()
        self.mem.settings=self.settings
        self.mem.translator=self.translator
        self.mem.frmMain=self
        initgame=frmInitGame(self.mem,  self)
        salida=initgame.exec_()
        if salida==QDialog.Accepted:
            self.showWdgGame()


    @pyqtSlot()     
    def on_actionGuardarPartida_triggered(self):
        os.chdir(self.path_autosaves)
        filename=os.path.basename(QFileDialog.getSaveFileName(self, "", "", "glParchis game (*.glparchis)")[0])
        if filename!="":       
            if os.path.splitext(filename)[1]!=".glparchis":
                filename=filename+".glparchis"
            self.mem.save(filename)
