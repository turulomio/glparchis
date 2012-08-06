# -*- coding: utf-8 -*-
import ConfigParser
from PyQt4.QtCore import *
from PyQt4.QtOpenGL import *
from PyQt4.QtGui import *
from frmShowCasilla import *
from frmShowFicha import *
from wdgUserPanel import *
from wdgGame import *
from qtablestatistics import *
from libglparchis import *

from Ui_wdgGame import *



class wdgGame(QWidget, Ui_wdgGame):
    """Clase principal del Juego, aquí está toda la ciencia, cuando se deba pasar al UI se crearán emits que captura qT para el UI"""
    def __init__(self, mem,  parent=None,  filename=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.mem=Mem4()
        self.ogl.assign_mem(self.mem)
        self.ogl.setFocus()

        self.on_JugadorDebeTirar()
        
        self.panel1.setJugador(self.mem.jugadores("yellow"))
        self.panel2.setJugador(self.mem.jugadores("blue"))
        self.panel3.setJugador(self.mem.jugadores("red"))
        self.panel4.setJugador(self.mem.jugadores("green"))


        self.panel().setActivated(True)

        
#        QtCore.QObject.connect(self.ogl, QtCore.SIGNAL('newLog(QString)'), self.lstLog_newLog)  
        QtCore.QObject.connect(self.ogl, QtCore.SIGNAL('CambiarJugador()'), self.CambiarJugador)  
#        QtCore.QObject.connect(self.ogl, QtCore.SIGNAL('volver_a_tirar()'), self.volver_a_tirar)  
        QtCore.QObject.connect(self.ogl, QtCore.SIGNAL('showCasillaFicha(int,int)'), self.showCasillaFicha)  
        QtCore.QObject.connect(self.ogl, QtCore.SIGNAL('JugadorDebeTirar()'), self.on_JugadorDebeTirar)  
        QtCore.QObject.connect(self.ogl, QtCore.SIGNAL('JugadorDebeMover()'), self.on_JugadorDebeMover)  
        QtCore.QObject.connect(self.ogl, QtCore.SIGNAL('TresSeisesSeguidos()'), self.on_TresSeisesSeguidos)  
        QtCore.QObject.connect(self.ogl, QtCore.SIGNAL('HaGanado()'), self.on_HaGanado)  
        self.settings_splitter_load()

        self.table.reload()

    def panel(self, jugador=None):
        """Si se pasa sin parametro da el panel del jugador actual"""
        jugador=self.mem.jugadoractual
        if self.panel1.jugador==jugador:
            return panel1
        elif self.panel2.jugador==jugador:
            return panel2
        elif self.panel3.jugador==jugador:
            return panel3
        elif self.panel4.jugador==jugador:
            return panel4

    def on_TresSeisesSeguidos(self):
            self.table.registraTres6Seguidos(self.mem.jugadoractual.color)
        

    def on_JugadorDebeTirar(self):
        """Se ejecuta cuando se emite JugadorDebeTirar"""
        self.cmdTirarDado.setEnabled(True)
        if self.mem.jugadoractual.ia==True:
#            time.sleep(1)
            self.mem.jugadoractual.log(self.trUtf8("IA Tira el dado"))
            self.on_cmdTirarDado_clicked()
        else:
            self.mem.jugadoractual.log(self.trUtf8("Tire el dado"))
            

    def on_HaGanado(self):
        m=QMessageBox()
        m.setIcon(QMessageBox.Information)
        m.setText(self.trUtf8("%1 ha ganado").arg(self.mem.jugadoractual.name))
        m.exec_() 
        self.tab.setCurrentIndex(1)
        
        
    def on_JugadorDebeMover(self):
        self.cmdTirarDado.setEnabled(False)
        if self.mem.jugadoractual.ia==True:
#            time.sleep(1)
            self.mem.jugadoractual.log(self.trUtf8("IA mueve una ficha"))            
            for f in self.mem.jugadoractual.fichas.arr:
                if f.PuedeMover(self.mem, self.mem.dado.lastthrow):
                    self.mem.selFicha=f
                    self.ogl.after_ficha_click()
                    return
        else:
            self.mem.jugadoractual.log(self.trUtf8("Mueva una ficha"))

        
    def on_splitter_splitterMoved(self, position, index):
        self.settings_splitter_save()

#    @pyqtSignature("int")
    def showCasillaFicha(self, selCasilla, selFicha):
        """selCasilla y selFicha son integers"""
        a=frmShowCasilla(self,  Qt.Popup,  self.mem.casillas(selCasilla))
        a. move(self.ogl.mapToGlobal(QPoint(10, 10))        )
        a.show()
        if selFicha!=-99:
            ficha=self.mem.fichas(selFicha)
            a=frmShowFicha(self, Qt.Popup,  ficha)
            a. move(self.ogl.mapToGlobal(QPoint(500, 10))        )
            a.show()
#
#    def lstLog_newLog(self, log):
#        self.panels[self.mem.jugadoractual.color.name].newLog(log)

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
    
  
    @QtCore.pyqtSlot()      
    def on_cmdTirarDado_clicked(self):  
        numerodado= self.mem.dado.tirar()
        self.mem.jugadoractual.historicodado.insert(0, numerodado)        
#        self.table.registraTirada(self.mem.jugadoractual.color, numero)

        self.panel().setLabelDado(self.mem.jugadoractual.historicodado)
        self.cmdTirarDado.setIcon(self.mem.dado.qicon(numero))
        
        if numerodado==6 and len(self.mem.jugadoractual.historicodado)==3:            
#            self.emit(SIGNAL("TresSeisesSeguidos()"))      
#            print "Ultima ficha movida",  self.mem.jugadoractual.LastFichaMovida
            if self.mem.jugadoractual.LastFichaMovida!=None:
#                print self.mem.jugadoractual.LastFichaMovida.name
                casilla=self.mem.jugadoractual.LastFichaMovida.casilla()
                if casilla.rampallegada==True:
                    self.mem.jugadoractual.log(self.trUtf8("Han salido tres seises, no se va a casa por haber llegado a rampa de llegada"))
                else:
                    self.mem.jugadoractual.log(self.trUtf8("Han salido tres seises, la última ficha movida se va a casa"))
                    self.mem.jugadoractual.LastFichaMovida.mover(0)
            else:               
                self.mem.jugadoractual.log(self.trUtf8("Después de tres seises, ya no puede volver a tirar"))
            self.CambiarJugador()
        else: # si no han salido 3 seises
            if self.mem.jugadoractual.fichas.AlgunaPuedeMover(self.mem)==True:
                self.on_JugadorDebeMover()
            else:#alguna no puede mover.
                if self.mem.jugadoractual.historicodado[0]==6:
                    self.on_JugadorDebeTirar()
                else:            
                    self.CambiarJugador()
        


    def CambiarJugador(self):
#        def limpia_panel(color):
#            pix=self.mem.dado.qpixmap(None)
#            
#            if color=="yellow":
#                self.panel1.lbl1.setPixmap(pix)
#                self.panel1.lbl2.setPixmap(pix)
#                self.panel1.lbl3.setPixmap(pix)
#                self.panel1.show()
#            elif color=="blue":
#                self.panel2.lbl1.setPixmap(pix)
#                self.panel2.lbl2.setPixmap(pix)
#                self.panel2.lbl3.setPixmap(pix)
#                self.panel2.show()
#            elif color=="red":
#                self.panel3.lbl1.setPixmap(pix)
#                self.panel3.lbl2.setPixmap(pix)
#                self.panel3.lbl3.setPixmap(pix)
#                self.panel3.show()
#            elif color=="green":
#                self.panel4.lbl1.setPixmap(pix)
#                self.panel4.lbl2.setPixmap(pix)
#                self.panel4.lbl3.setPixmap(pix)
#                self.panel4.show()
                
        #Cambia jugadoractual
        self.panel().setActivated(False)
        if self.mem.jugadoractual.ia==True:
            time.sleep(0.2)
        while True:
            if self.mem.jugadoractual.color=="yellow":
                self.mem.jugadoractual=self.mem.jugadores("blue")
            elif self.mem.jugadoractual.color=="blue" :
                self.mem.jugadoractual=self.mem.jugadores("red")
            elif self.mem.jugadoractual.color=="red" :
                self.mem.jugadoractual=self.mem.jugadores("green")
            elif self.mem.jugadoractual.color=="green" :
                self.mem.jugadoractual=self.mem.jugadores("yellow")
            if self.mem.jugadoractual.plays:#Comprueba si el actual plays
                break
          
        self.setWindowIcon(self.mem.jugadoractual.qicon())
        self.mem.jugadoractual.historicodado=[]
        self.mem.jugadoractual.movimientos_acumulados=None
        self.mem.jugadoractual.LastFichaMovida=None
        
        #Activa y limpia
        self.panel().setActivated(True)
        self.panel().lbl1.setPixmap(self.mem.dado.qpixmap(None))
        self.panel().lbl2.setPixmap(self.mem.dado.qpixmap(None))
        self.panel().lbl3.setPixmap(self.mem.dado.qpixmap(None))
        self.panel().show()

        self.on_JugadorDebeTirar()
