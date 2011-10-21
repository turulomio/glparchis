## -*- coding: utf-8 -*-
import sys,  random,  ConfigParser,  os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import libglparchis

from Ui_frmMain import *
from frmShowCasilla import *
from frmAbout import *
from wdgUserPanel import *
from wdgGame import *
from frmInitGame import *
from qtablestatistics import *

            
class frmMain(QMainWindow, Ui_frmMain):#    
    def __init__(self, parent = 0,  flags = False):
        QMainWindow.__init__(self, None)
        self.setupUi(self)
        self.showMaximized()

        self.panel1.setColor("yellow")
        self.panel2.setColor("blue")
        self.panel3.setColor("red")
        self.panel4.setColor("green")
                
        self.panels={}
        self.panels["yellow"]=self.panel1
        self.panels["blue"]=self.panel2
        self.panels["red"]=self.panel3
        self.panels["green"]=self.panel4
        
        QtCore.QObject.connect(self.ogl, QtCore.SIGNAL('newLog(QString)'), self.lstLog_newLog)  
        QtCore.QObject.connect(self.ogl, QtCore.SIGNAL('cambiar_jugador()'), self.cambiar_jugador)  
        QtCore.QObject.connect(self.ogl, QtCore.SIGNAL('volver_a_tirar()'), self.volver_a_tirar)  
        QtCore.QObject.connect(self.ogl, QtCore.SIGNAL('showCasilla(int)'), self.showCasilla)  
        self.settings_splitter_load()

        self.table.reload()

        
        
    def on_splitter_splitterMoved(self, position, index):
        self.settings_splitter_save()
        
    @pyqtSignature("")
    def on_cmdTirarDado_clicked(self):
        self.on_actionDado_activated()

#    @pyqtSignature("int")
    def showCasilla(self, selCasilla):
        a=frmShowCasilla(self, Qt.Popup,  self.ogl.casillas[selCasilla])
        a. move(self.ogl.mapToGlobal(QPoint(10, 10))        )
        a.show()

    def lstLog_newLog(self, log):
        self.panels[self.ogl.jugadoractual.color].newLog(log)

    def settings_splitter_save(self):
        config = ConfigParser.ConfigParser()
        config.read(libglparchis.cfgfile)
        if config.has_section("frmMain")==False:
            config.add_section("frmMain")
        config.set("frmMain",  'splitter_state', self.splitter.saveState())
        with open(libglparchis.cfgfile, 'w') as configfile:
            config.write(configfile)
        
    def settings_splitter_load(self):
        config = ConfigParser.ConfigParser()
        config.read(libglparchis.cfgfile)
        try:
            position=config.get("frmMain", "splitter_state")
            self.splitter.restoreState(position)
        except:
            print ("No hay fichero de configuración")    
    
        
    @pyqtSignature("")
    def on_actionAcercaDe_activated(self):
        fr=frmAbout(self, "frmabout")
        fr.open()
    
    @QtCore.pyqtSlot()      
    def on_actionSalir_activated(self):
        sys.exit()
    
    @QtCore.pyqtSlot()      
    def on_actionDado_activated(self):  
        def labeldado():
            numero=self.ogl.historicodado[0]
            numlbl=len(self.ogl.historicodado)
            #Selecciona el panel
            if self.ogl.jugadoractual.color=="yellow":
                panel=self.panel1
            elif self.ogl.jugadoractual.color=="blue":
                panel=self.panel2
            elif self.ogl.jugadoractual.color=="red":
                panel=self.panel3
            elif self.ogl.jugadoractual.color=="green":
                panel=self.panel4
            #Selecciona el label
            if numlbl==1:
                label=panel.lbl1
            elif numlbl==2:
                label=panel.lbl2
            elif numlbl==3:
                label=panel.lbl3
            ico=libglparchis.icodado(numero)
            self.actionDado.setIcon(ico)
            self.cmdTirarDado.setIcon(ico)   
            pix=libglparchis.pixdado(numero)
            label.setPixmap(pix)
                
        def jugador_tiene_todas_fichas_en_casa():
            for f in self.ogl.jugadoractual.fichas:
                if self.ogl.jugadoractual.fichas[f].ruta!=0:
                    return False
            return True
            
#        numero=5
#        numero= int(random.random()*6)+1
        numero= int(random.random()*2)+5
        self.table.registraTirada(self.ogl.jugadoractual.color, numero)
#        self.lstLog_newLog("Ha salido un " + str(numero))        
#        self.ogl.dado=numero
        self.ogl.pendiente=1
        self.ogl.historicodado.insert(0, numero)
        self.actionDado.setEnabled(False)
        self.cmdTirarDado.setEnabled(False)
        labeldado()
        
        #LOGICA QUE NO REQUIERE LA INTEVENCION DEL USUARIO
        if jugador_tiene_todas_fichas_en_casa()==True:
            if numero <5:
                self.lstLog_newLog(str(numero)+ "No es un 5 y las tienes todas en casa")
                self.cambiar_jugador()
                return
            elif numero==6 and len(self.ogl.historicodado)==3:
                self.lstLog_newLog("No ha salido un 5, y ha sacado 3 seises, ya no puede volver a tirar")
                self.table.registraTres6seguidos(self.ogl.jugadoractual.color)
                self.cambiar_jugador()
                return            
            elif numero==6 and len(self.ogl.historicodado)<3:
                self.lstLog_newLog("No es 5, pero puede volver a tirar")
                self.ogl.pendiente=2
                self.actionDado.setEnabled(True)
                self.cmdTirarDado.setEnabled(True)
                return

    def cambiar_jugador(self):
        def limpia_panel(color):
            pix=pixdado(None)
            if color=="yellow":
                self.panel1.lbl1.setPixmap(pix)
                self.panel1.lbl2.setPixmap(pix)
                self.panel1.lbl3.setPixmap(pix)
                self.panel1.show()
            elif color=="blue":
                self.panel2.lbl1.setPixmap(pix)
                self.panel2.lbl2.setPixmap(pix)
                self.panel2.lbl3.setPixmap(pix)
                self.panel2.show()
            elif color=="red":
                self.panel3.lbl1.setPixmap(pix)
                self.panel3.lbl2.setPixmap(pix)
                self.panel3.lbl3.setPixmap(pix)
                self.panel3.show()
            elif color=="green":
                self.panel4.lbl1.setPixmap(pix)
                self.panel4.lbl2.setPixmap(pix)
                self.panel4.lbl3.setPixmap(pix)
                self.panel4.show()
                
        #Cambia jugadoractual
        self.panels[self.ogl.jugadoractual.color].setEnabled(False)
        while True:
            if self.ogl.jugadoractual.color=="yellow":
                self.ogl.jugadoractual=self.ogl.jugadores["blue"]
            elif self.ogl.jugadoractual.color=="blue" :
                self.ogl.jugadoractual=self.ogl.jugadores["red"]
            elif self.ogl.jugadoractual.color=="red" :
                self.ogl.jugadoractual=self.ogl.jugadores["green"]
            elif self.ogl.jugadoractual.color=="green" :
                self.ogl.jugadoractual=self.ogl.jugadores["yellow"]
            if self.ogl.jugadoractual.plays:#Comprueba si el actual plays
                break
                
        self.ogl.historicodado=[]
        self.ogl.pendiente=2

        self.actionDado.setEnabled(True)       
        self.cmdTirarDado.setEnabled(True)
        self.panels[self.ogl.jugadoractual.color].setEnabled(True)
        limpia_panel(self.ogl.jugadoractual.color)
        self.lstLog_newLog(self.trUtf8("Ahora puede tirar"))

                    
    @QtCore.pyqtSlot()     
    def on_actionRecuperarPartida_activated(self):
        #ÐEBE SERLOCAL
        filenam=os.path.basename(libglparchis.q2s(QFileDialog.getOpenFileName(self, "", "", "glParchis game (*.glparchis)")))
        self.ogl.load_file(filenam)
        self.panel1.grp.setTitle(self.ogl.jugadores['yellow'].name)
        self.panel2.grp.setTitle(self.ogl.jugadores['blue'].name)
        self.panel3.grp.setTitle(self.ogl.jugadores['red'].name)
        self.panel4.grp.setTitle(self.ogl.jugadores['green'].name)
        config = ConfigParser.ConfigParser()
        config.read(filenam)
        self.panels[config.get("game", 'playerstarts')].setEnabled(True)
        self.actionGuardarPartida.setEnabled(True)
        self.actionDado.setEnabled(True)

    @QtCore.pyqtSlot()     
    def on_actionPartidaNueva_activated(self):
        def save_last_glparchis():
            try:
                os.remove(libglparchis.lastfile)
            except:
                pass
            config = ConfigParser.ConfigParser()
            config.add_section("yellow")
            config.set("yellow",  'ia', int(libglparchis.c2b(initgame.chkYellow.checkState())))
            config.set("yellow",  'name', initgame.txtYellow.text())
            config.set("yellow",  'plays', int(libglparchis.c2b(initgame.chkYellowPlays.checkState())))
            config.add_section("blue")
            config.set("blue",  'ia', int(libglparchis.c2b(initgame.chkBlue.checkState())))
            config.set("blue",  'name', initgame.txtBlue.text())
            config.set("blue",  'plays', int(libglparchis.c2b(initgame.chkBluePlays.checkState())))
            config.add_section("red")
            config.set("red",  'ia', int(libglparchis.c2b(initgame.chkRed.checkState())))
            config.set("red",  'name', initgame.txtRed.text())
            config.set("red",  'plays', int(libglparchis.c2b(initgame.chkRedPlays.checkState())))
            config.add_section("green")
            config.set("green",  'ia', int(libglparchis.c2b(initgame.chkGreen.checkState())))
            config.set("green",  'name', initgame.txtGreen.text())
            config.set("green",  'plays', int(libglparchis.c2b(initgame.chkGreenPlays.checkState())))
                
            for color in libglparchis.colores:
                config.set(color,  'rutaficha1', 0)
                config.set(color,  'rutaficha2', 0)
                config.set(color,  'rutaficha3', 0)
                config.set(color,  'rutaficha4', 0)
            config.add_section("game")
            config.set("game", 'playerstarts', initgame.playerstarts)
            with open(libglparchis.lastfile, 'w') as configfile:
                config.write(configfile)            
                
        initgame=frmInitGame()
        initgame.exec_()


        #Graba fichero .glparchis/last.glparchis
        save_last_glparchis()
        #Carga fichero .glparchis/last.glparchis
#        self.ogl=wdgGame(filename=libglparchis.lastfile)
        self.ogl.load_file(libglparchis.lastfile)
        
        self.panel1.grp.setTitle(self.ogl.jugadores['yellow'].name)
        self.panel2.grp.setTitle(self.ogl.jugadores['blue'].name)
        self.panel3.grp.setTitle(self.ogl.jugadores['red'].name)
        self.panel4.grp.setTitle(self.ogl.jugadores['green'].name)
        self.panels[initgame.playerstarts].setEnabled(True)

        self.actionGuardarPartida.setEnabled(True)
        self.actionDado.setEnabled(True)


    def save(self, filename):
        config = ConfigParser.ConfigParser()
        config.add_section("yellow")
        config.set("yellow",  'ia', int(self.ogl.jugadores['yellow'].ia))
        config.set("yellow",  'name', self.ogl.jugadores['yellow'].name)
        config.set("yellow",  'plays', int(self.ogl.jugadores['yellow'].plays))
        config.set("yellow",  'rutaficha1', self.ogl.fichas[0].ruta)
        config.set("yellow",  'rutaficha2',  self.ogl.fichas[1].ruta)
        config.set("yellow",  'rutaficha3',  self.ogl.fichas[2].ruta)
        config.set("yellow",  'rutaficha4',  self.ogl.fichas[3].ruta)        
        config.add_section("blue")
        config.set("blue",  'ia', int(self.ogl.jugadores['blue'].ia))
        config.set("blue",  'name', self.ogl.jugadores['blue'].name)
        config.set("blue",  'plays', int(self.ogl.jugadores['blue'].plays))
        config.set("blue",  'rutaficha1', self.ogl.fichas[4].ruta)
        config.set("blue",  'rutaficha2',  self.ogl.fichas[5].ruta)
        config.set("blue",  'rutaficha3',  self.ogl.fichas[6].ruta)
        config.set("blue",  'rutaficha4',  self.ogl.fichas[7].ruta)        
        config.add_section("red")
        config.set("red",  'ia', int(self.ogl.jugadores['red'].ia))
        config.set("red",  'name', self.ogl.jugadores['red'].name)
        config.set("red",  'plays', int(self.ogl.jugadores['red'].plays))
        config.set("red",  'rutaficha1', self.ogl.fichas[8].ruta)
        config.set("red",  'rutaficha2',  self.ogl.fichas[9].ruta)
        config.set("red",  'rutaficha3',  self.ogl.fichas[10].ruta)
        config.set("red",  'rutaficha4',  self.ogl.fichas[11].ruta)         
        config.add_section("green")
        config.set("green",  'ia', int(self.ogl.jugadores['green'].ia))
        config.set("green",  'name', self.ogl.jugadores['green'].name)
        config.set("green",  'plays', int(self.ogl.jugadores['green'].plays))
        config.set("green",  'rutaficha1', self.ogl.fichas[12].ruta)
        config.set("green",  'rutaficha2',  self.ogl.fichas[13].ruta)
        config.set("green",  'rutaficha3',  self.ogl.fichas[14].ruta)
        config.set("green",  'rutaficha4',  self.ogl.fichas[15].ruta)              
        config.add_section("game")
        config.set("game", 'playerstarts',self.ogl.jugadoractual.color)
        with open(filename, 'w') as configfile:
            config.write(configfile)            


    @QtCore.pyqtSlot()     
    def on_actionGuardarPartida_activated(self):
        filename=os.path.basename(libglparchis.q2s(QFileDialog.getOpenFileName(self, "", "", "glParchis game (*.glparchis)")))
        self.save(filename)


    def volver_a_tirar(self):
        self.actionDado.setEnabled(True)
        self.lstLog_newLog(self.trUtf8("Ahora puede volver a tirar"))
