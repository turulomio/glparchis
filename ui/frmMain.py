import sys, os, urllib.request,   datetime
from urllib.request import urlopen
from PyQt5.QtCore import QTranslator, Qt, pyqtSlot, QSize, QEvent, QUrl
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QMessageBox, qApp, QLabel, QSpacerItem, QDialog, QHBoxLayout, QVBoxLayout, QFileDialog, QSizePolicy
from PyQt5.QtWebEngineWidgets import QWebEngineView
from libglparchis import dateversion, str2bool, cargarQTranslator, b2s, qmessagebox,  Mem4, Mem6, Mem8

import configparser
from Ui_frmMain import Ui_frmMain
from wdgGame import wdgGame
from frmAbout import frmAbout
from frmInitGame import frmInitGame
from frmSettings import frmSettings
from frmHelp import frmHelp
from uuid import uuid4

class frmMain(QMainWindow, Ui_frmMain):#    
    def __init__(self, settings, parent = 0,  flags = False):
        QMainWindow.__init__(self)
        self.settings=settings
        self.translator=QTranslator()
        cargarQTranslator(self.translator, settings.value("frmSettings/language", "en"))
        self.setupUi(self)
        self.showMaximized()
        self.game=None
        self.setWindowTitle(self.tr("glParchis 2010-{}. GNU General Public License \xa9").format(dateversion.year))
        if datetime.date.today()-datetime.date.fromordinal(int(self.settings.value("frmMain/lastupdate", 1)))>=datetime.timedelta(days=7):
            print ("Actualizando")
            self.checkUpdates(False)
        self.setSound(str2bool(self.settings.value("frmSettings/sound", "True")))
        self.setFullScreen(str2bool(self.settings.value("frmMain/fullscreen", "False")))
        self.setInstallationUUID()
        
    def setInstallationUUID(self):
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



    def setFullScreen(self, bool):
        if bool==False:
            self.actionFullScreen.setText(self.tr("Cambiar al modo de pantalla completa"))
            self.actionFullScreen.setToolTip(self.tr("Cambiar al modo de pantalla completa"))
            self.menuBar.show()
            self.showMaximized()
            self.removeToolBar(self.toolBar);
            self.addToolBar(Qt.TopToolBarArea, self.toolBar)
            self.toolBar.show()
            self.settings.setValue("frmMain/fullscreen", "False")
        else:      
            self.actionFullScreen.setText(self.tr("Salir del modo de pantalla completa"))
            self.actionFullScreen.setToolTip(self.tr("Salir del modo de pantalla completa"))
            self.showFullScreen()
            self.menuBar.hide()
            self.removeToolBar(self.toolBar);
            self.addToolBar(Qt.LeftToolBarArea, self.toolBar)
            self.toolBar.show()
            self.settings.setValue("frmMain/fullscreen", "True")
        if self.game!=None:
            self.game.restoreSplitter()

    @pyqtSlot()      
    def on_actionAcercaDe_triggered(self):
        fr=frmAbout(self,"frmabout")
        fr.open()

    @pyqtSlot()      
    def on_actionFullScreen_triggered(self):
        if self.isFullScreen():
            self.setFullScreen(False)
        else:
            self.setFullScreen(True)
                
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
    
    def setSound(self, bool):
        if bool==True:
            self.actionSound.setText(self.tr("Sonido encendido")) 
            icon8 = QIcon()
            icon8.addPixmap(QPixmap(":/glparchis/sound.png"), QIcon.Normal, QIcon.Off)
            self.actionSound.setIcon(icon8)
        else:
            self.actionSound.setText(self.tr("Sonido apagado"))
            icon8 = QIcon()
            icon8.addPixmap(QPixmap(":/glparchis/soundoff.png"), QIcon.Normal, QIcon.Off)
            self.actionSound.setIcon(icon8)
        self.settings.setValue("frmSettings/sound", bool)
        
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
                
        if dateremoteversion==dateversion: 
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
        self.game.assign_mem(self.mem)

    @pyqtSlot()  
    def on_actionRecuperarPartida_triggered(self):
        cwd=os.getcwd()
        os.chdir(os.path.expanduser("~/.glparchis/"))
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
        os.chdir(cwd)

    def selectMem(self, filename):
        resultado=None
        cwd=os.getcwd()
        os.chdir(os.path.expanduser("~/.glparchis/"))
        config = configparser.ConfigParser()
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
    def on_actionMundialStatistics_triggered(self):
        d=QDialog()#Use frmMain because in invoked from frmSettings to        
        d.setWindowTitle(self.tr("Estadisticas mundiales"))       
        d.setWindowModality(Qt.WindowModal)
        d.resize(549, 607)
        icon = QIcon()
        icon.addPixmap(QPixmap(":/glparchis/statistics.png"), QIcon.Normal, QIcon.Off)
        d.setWindowIcon(icon)
        d.setModal(True)
        self.horizontalLayout_2 = QHBoxLayout(d)
        self.verticalLayout = QVBoxLayout()
        
        self.lblApp = QLabel(d)
        self.lblApp.setText(self.tr("Estadisticas mundiales"))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblApp.setFont(font)
        self.lblApp.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.lblApp)
        
        self.horizontalLayout = QHBoxLayout()
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lblPixmap = QLabel(d)
        self.lblPixmap.setMaximumSize(QSize(68, 68))
        self.lblPixmap.setPixmap(QPixmap(":/glparchis/statistics.png"))
        self.lblPixmap.setScaledContents(True)
        self.lblPixmap.setAlignment(Qt.AlignCenter)
        self.horizontalLayout.addWidget(self.lblPixmap)
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        self.webView = QWebEngineView(d)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webView.sizePolicy().hasHeightForWidth())
        self.webView.setSizePolicy(sizePolicy)
        self.webView.setUrl(QUrl("http://glparchis.sourceforge.net/php/glparchis_statistics.php"))
        self.verticalLayout.addWidget(self.webView)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        d.setFocus()
        d.exec_()
            
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
        cwd=os.getcwd()
        os.chdir(os.path.expanduser("~/.glparchis/"))
        filename=os.path.basename(QFileDialog.getSaveFileName(self, "", "", "glParchis game (*.glparchis)")[0])
        if filename!="":       
            if os.path.splitext(filename)[1]!=".glparchis":
                filename=filename+".glparchis"
            self.mem.save(filename)
        os.chdir(cwd)
