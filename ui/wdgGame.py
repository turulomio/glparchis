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
        def settings_splitter_load():
            config = ConfigParser.ConfigParser()
            config.read(libglparchis.cfgfile)
            try:
                position=config.get("frmMain", "splitter_state")
                self.splitter.restoreState(position)
            except:
                print ("No hay fichero de configuración")    
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.mem=mem
        self.ogl.assign_mem(self.mem)
        self.ogl.setFocus()

        
        self.panel1.setJugador(self.mem.jugadores("yellow"))
        self.panel2.setJugador(self.mem.jugadores("blue"))
        self.panel3.setJugador(self.mem.jugadores("red"))
        self.panel4.setJugador(self.mem.jugadores("green"))

        self.panel().setActivated(True)
#
#        QtCore.QObject.connect(self.ogl, QtCore.SIGNAL('CambiarJugador()'), self.CambiarJugador)  
#        QtCore.QObject.connect(self.ogl, QtCore.SIGNAL('showCasillaFicha(int,int)'), self.showCasillaFicha)  
#        QtCore.QObject.connect(self.ogl, QtCore.SIGNAL('JugadorDebeTirar()'), self.on_JugadorDebeTirar)  
#        QtCore.QObject.connect(self.ogl, QtCore.SIGNAL('JugadorDebeMover()'), self.on_JugadorDebeMover)  
#        QtCore.QObject.connect(self.ogl, QtCore.SIGNAL('TresSeisesSeguidos()'), self.on_TresSeisesSeguidos)  
#        QtCore.QObject.connect(self.ogl, QtCore.SIGNAL('HaGanado()'), self.on_HaGanado)  #        
        QtCore.QObject.connect(self.ogl, QtCore.SIGNAL('fichaClicked()'), self.after_ficha_click)  
        settings_splitter_load()

        self.table.reload()
        self.on_JugadorDebeTirar()

    def panel(self, jugador=None):
        """Si se pasa sin parametro da el panel del jugador actual"""
        if jugador==None:
            jugador=self.mem.jugadoractual
        if self.panel1.jugador==jugador:
            return self.panel1
        elif self.panel2.jugador==jugador:
            return self.panel2
        elif self.panel3.jugador==jugador:
            return self.panel3
        elif self.panel4.jugador==jugador:
            return self.panel4
#
#    def on_TresSeisesSeguidos(self):
#            self.table.registraTres6Seguidos(self.mem.jugadoractual.color)
        

    def on_JugadorDebeTirar(self):
        """Se ejecuta cuando el jugador debe tirar:
                - Inicio turno
                - Otras situaciones"""
        self.cmdTirarDado.setEnabled(True)
        if self.mem.jugadoractual.ia==True:
            self.mem.jugadoractual.log(self.trUtf8("IA Tira el dado"))
            self.on_cmdTirarDado_clicked()
        else:
            self.mem.jugadoractual.log(self.trUtf8("Tire el dado"))

       
    def on_JugadorDebeMover(self):
        """Función que se ejecuta cuando un jugador debe mover
        Aquí se evalua si puede mover devolviendo True en caso positivo y """
        if self.mem.jugadoractual.ia==True:
            self.mem.jugadoractual.log(self.trUtf8("IA mueve una ficha"))            
            for f in self.mem.jugadoractual.fichas.arr:
                if f.PuedeMover(self.mem, self.mem.dado.lastthrow):
                    self.mem.selFicha=f
                    self.after_ficha_click()
                    return
        else:
            self.mem.jugadoractual.log(self.trUtf8("Mueva una ficha"))

        
    def on_splitter_splitterMoved(self, position, index):
        config = ConfigParser.ConfigParser()
        config.read(libglparchis.cfgfile)
        if config.has_section("frmMain")==False:
            config.add_section("frmMain")
        config.set("frmMain",  'splitter_state', self.splitter.saveState())
        with open(libglparchis.cfgfile, 'w') as configfile:
            config.write(configfile)

    @QtCore.pyqtSlot()      
    def on_cmdTirarDado_clicked(self):  
        self.cmdTirarDado.setEnabled(False)
        valordado=self.mem.jugadoractual.TirarDado()
        self.panel().setLabelDado()
        
        if valordado==6 and len(self.mem.jugadoractual.tiradaturno.arr)==3:            
            if self.mem.jugadoractual.LastFichaMovida!=None:
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
        

    def after_ficha_click(self):
        puede=self.mem.selFicha.PuedeMover(self.mem,  self.mem.dado.lastthrow)
        if puede[0]==False:
            self.mem.jugadoractual.log(self.trUtf8("No puede mover esta ficha, seleccione otra"))
            return
        
        self.mem.selFicha.mover( self.mem.selFicha.posruta + puede[1])
        #Quita el movimiento acumulados
        if self.mem.jugadoractual.movimientos_acumulados in (10, 20):
            self.mem.jugadoractual.movimientos_acumulados=None

        #Come
        if self.mem.selFicha.come(self.mem.selFicha.posruta)==True:
            if self.mem.jugadoractual.fichas.AlgunaPuedeMover(self.mem)==False:
                if self.habiaSalidoSeis()==True:
                    self.on_JugadorDebeTirar()
                else:
                    self.CambiarJugador()
            else:#si alguna puede mover
                self.on_JugadorDebeMover()
#        print ("No come")
        
        #Mete
        if self.mem.selFicha.mete()==True:
#            print ("mete")
            if self.mem.jugadoractual.fichas.AlgunaPuedeMover(self.mem)==False:
                if self.habiaSalidoSeis()==True:
                    self.on_JugadorDebeTirar()
                else:
                    self.CambiarJugador()
            else:#si alguna puede mover
                self.on_JugadorDebeMover()
#        print (" No mete")       
        
        if self.mem.dado.habiaSalidoSeis()==True:
            self.on_JugadorDebeTirar()
        else:
            self.CambiarJugador()

    

    def CambiarJugador(self):             
        #Comprueba si ha ganado
        if self.mem.jugadoractual.HaGanado()==True:
            m=QMessageBox()
            m.setIcon(QMessageBox.Information)
            m.setText(self.trUtf8("%1 ha ganado").arg(self.mem.jugadoractual.name))
            m.exec_() 
            self.tab.setCurrentIndex(1)
            return
        
        
        self.panel().setActivated(False)
#        if self.mem.jugadoractual.ia==True:
#            time.sleep(0.2)
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
        
        self.mem.jugadoractual.tiradaturno=TiradaTurno()#Se crea otro objeto porque as´i el anterior queda vinculada< a TiradaHistorica.
#        self.mem.jugadoractual.historicodado=[]
        self.mem.jugadoractual.movimientos_acumulados=None
        self.mem.jugadoractual.LastFichaMovida=None
        
        #Activa y limpia
        self.panel().setActivated(True)
        self.panel().lbl1.setPixmap(self.mem.dado.qpixmap(None))
        self.panel().lbl2.setPixmap(self.mem.dado.qpixmap(None))
        self.panel().lbl3.setPixmap(self.mem.dado.qpixmap(None))
        self.panel().show()

        self.on_JugadorDebeTirar()
