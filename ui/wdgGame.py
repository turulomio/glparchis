# -*- coding: utf-8 -*-
import ConfigParser
from PyQt4.QtCore import *
from PyQt4.QtOpenGL import *
from PyQt4.QtGui import *
from wdgUserPanel import *
from wdgGame import *
from qtablestatistics import *
from libglparchis import *
from Ui_wdgGame import *

class wdgGame(QWidget, Ui_wdgGame):
    """Clase principal del Juego, aquí está toda la ciencia, cuando se deba pasar al UI se crearán emits que captura qT para el UI"""
    def __init__(self,   parent=None,  filename=None):        
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.show()
    
    def __del__(self):
        print ("Destructor wdgGame")
        self.stopthegame=True
        self.table.stopReloads()
        self.panel1.stopTimerLog()
        self.panel2.stopTimerLog()
        self.panel3.stopTimerLog()
        self.panel4.stopTimerLog()
        

    def assign_mem(self, mem):
        self.mem=mem
        self.stopthegame=False
        self.table.assign_mem(self.mem)
        self.ogl.assign_mem(self.mem)
        self.ogl.setFocus()
        
        self.panel1.setJugador(self.mem.jugadores.jugador("yellow"))
        self.panel2.setJugador(self.mem.jugadores.jugador("blue"))
        self.panel3.setJugador(self.mem.jugadores.jugador("red"))
        self.panel4.setJugador(self.mem.jugadores.jugador("green"))
        
        self.panel().setActivated(True)
        self.cmdTirarDado.setStyleSheet('QPushButton {color: '+self.mem.jugadoractual.color.name+'; font: bold 30px; background-color: rgb(170, 170, 170);}')
        self.mem.jugadoractual.log(self.tr("Empieza la partida"))


        QtCore.QObject.connect(self.ogl, QtCore.SIGNAL('fichaClicked()'), self.after_ficha_click)  
        if self.mem.cfgfile.splitterstate==None:
            currentSizes = self.splitter.sizes()
            currentSizes[0]=self.width()-self.ogl.height()-100
            currentSizes[1]=self.width()-currentSizes[0]
            self.splitter.setSizes(currentSizes)
        else:
            self.splitter.restoreState(self.mem.cfgfile.splitterstate)

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

    def afterWinning(self):
        self.mem.jugadoractual.log(self.trUtf8("Has ganado la partida"))
        self.mem.play("win")
        self.table.stopReloads()
        self.stopthegame=True
        self.panel1.stopTimerLog()
        self.panel2.stopTimerLog()
        self.panel3.stopTimerLog()
        self.panel4.stopTimerLog()
        m=QMessageBox()
        m.setIcon(QMessageBox.Information)
        m.setText(self.trUtf8("%1 ha ganado").arg(self.mem.jugadoractual.name))
        m.exec_() 
        self.tab.setCurrentIndex(1)


    def on_JugadorDebeTirar(self):
        """Se ejecuta cuando el jugador debe tirar:
                - Inicio turno
                - Otras situaciones"""
        if self.stopthegame==True:
            return
        if self.mem.jugadores.alguienHaGanado()==True:
            self.afterWinning()
            return
            
        #Comprueba si ha ganado
        if self.mem.jugadoractual.HaGanado()==True:
            self.mem.jugadoractual.log(self.trUtf8("Has ganado la partida"))
            self.mem.play("win")
            self.table.stopReloads()
            self.stopthegame=True
            self.panel1.stopTimerLog()
            self.panel2.stopTimerLog()
            self.panel3.stopTimerLog()
            self.panel4.stopTimerLog()
            m=QMessageBox()
            m.setIcon(QMessageBox.Information)
            m.setText(self.trUtf8("%1 ha ganado").arg(self.mem.jugadoractual.name))
            m.exec_() 
            self.tab.setCurrentIndex(1)
            return           
            
        self.cmdTirarDado.setText(self.trUtf8("Tira el dado"))
        if self.mem.jugadoractual.ia==False:#Cuando es IA no debe permitir tirar dado
            self.cmdTirarDado.setEnabled(True)
#        self.cmdTirarDado.setIcon(self.mem.dado.qicon(None))
        if self.mem.jugadoractual.ia==True:
            self.mem.jugadoractual.log(self.trUtf8(u"IA Tira el dado"))
            delay(400)
            self.on_cmdTirarDado_clicked()
            delay(800)
        else:
            self.mem.jugadoractual.log(self.trUtf8(u"Tire el dado"))

       
    def on_JugadorDebeMover(self):
        """Función que se ejecuta cuando un jugador debe mover
        Aquí se evalua si puede mover devolviendo True en caso positivo y """
        
        if self.mem.jugadores.alguienHaGanado()==True:
            self.afterWinning()
            return
        
        self.cmdTirarDado.setEnabled(False)
        if self.mem.jugadoractual.ia==True:
            self.mem.jugadoractual.log(self.trUtf8("IA mueve una ficha"))     
            iaficha=self.mem.jugadoractual.IASelectFicha(self.mem)
            delay(400)
            if iaficha==None:
                self.cambiarJugador()
            else:
                self.mem.selFicha=iaficha
                self.after_ficha_click()
        else:
            self.mem.jugadoractual.log(self.trUtf8("Mueva una ficha"))

        
    def on_splitter_splitterMoved(self, position, index):
        self.mem.cfgfile.splitterstate=self.splitter.saveState()
        self.mem.cfgfile.save()
        self.update()

    @QtCore.pyqtSlot()      
    def on_cmdTirarDado_clicked(self):  
        self.cmdTirarDado.setEnabled(False)
        self.cmdTirarDado.setText("")
        self.mem.play("dice")
        self.mem.jugadoractual.tirarDado()
        self.mem.dado.showing=True
        self.ogl.updateGL()
#        self.cmdTirarDado.setIcon(self.mem.dado.qicon(self.mem.jugadoractual.tiradaturno.ultimoValor()))
        self.panel().setLabelDado()
        
        if self.mem.jugadoractual.tiradaturno.tresSeises()==True:
            if self.mem.jugadoractual.LastFichaMovida!=None:
                casilla=self.mem.jugadoractual.LastFichaMovida.casilla()
                if casilla.rampallegada==True:
                    self.mem.jugadoractual.log(self.trUtf8("Han salido tres seises, no se va a casa por haber llegado a rampa de llegada"))
                else:
                    if self.mem.jugadoractual.LastFichaMovida.estaAutorizadaAMover(self.mem)[0]==True:
                        self.mem.jugadoractual.log(self.trUtf8("Han salido tres seises, la ultima ficha movida se va a casa"))
                        self.mem.play("comer")
                        self.mem.jugadoractual.LastFichaMovida.mover(0)
                    else:
                        self.mem.jugadoractual.log(self.trUtf8(u"Han salido tres seises, pero como no puede mover no se va a casa"))
            else:               
                self.mem.jugadoractual.log(self.trUtf8(u"Despues de tres seises, ya no puede volver a tirar"))
            self.cambiarJugador()
        else: # si no han salido 3 seises
            if self.mem.jugadoractual.fichas.algunaEstaAutorizadaAmover(self.mem)==True:
                self.on_JugadorDebeMover()
            else:#ninguna puede mover.
                if self.mem.jugadoractual.tiradaturno.ultimoEsSeis()==True:
                    self.on_JugadorDebeTirar()
                else:            
                    self.cambiarJugador()

    def after_ficha_click(self):
        if self.mem.selFicha==None:
            self.mem.jugadoractual.log(self.trUtf8("Seleccione una ficha..."))
            return
            
        if self.cmdTirarDado.isEnabled():#Esta esperando dado no se puede pulsar ficha para mover.
            return
        
        (puede, movimiento)=self.mem.selFicha.estaAutorizadaAMover(self.mem, True)
            
        if puede==False:
            if self.mem.jugadoractual.ia==False:
                self.mem.play("click")
            return

                
        if self.mem.selFicha.come(self.mem, self.mem.selFicha.posruta+movimiento) or self.mem.selFicha.mete(self.mem.selFicha.posruta+movimiento):    
            self.ogl.updateGL()
            if self.mem.jugadoractual.movimientos_acumulados==10:
                self.mem.play("meter")
            else:
                self.mem.play("comer")            
            delay(600)
            if self.mem.jugadoractual.fichas.algunaEstaAutorizadaAmover(self.mem)==True:
                self.on_JugadorDebeMover()
                return
        else:
            self.mem.selFicha.mover( self.mem.selFicha.posruta + movimiento)    
            self.ogl.updateGL()
       #Quita el movimiento acumulados
        if self.mem.jugadoractual.movimientos_acumulados in (10, 20):
            self.mem.jugadoractual.movimientos_acumulados=None

        if self.mem.jugadoractual.tiradaturno.ultimoEsSeis()==True:
            self.on_JugadorDebeTirar()
        else:
            self.cambiarJugador()

    def cambiarJugador(self):          
        self.mem.jugadoractual.log (self.trUtf8("Fin de turno"))
        self.ogl.updateGL()        
        delay(400)
        self.mem.dado.showing=False
        self.ogl.updateGL()        

        self.panel().setActivated(False)
        self.panel().grp.update()
        
        while True:
            if self.mem.jugadoractual.color.name=="yellow":
                self.mem.jugadoractual=self.mem.jugadores.jugador("blue")
            elif self.mem.jugadoractual.color.name=="blue" :
                self.mem.jugadoractual=self.mem.jugadores.jugador("red")
            elif self.mem.jugadoractual.color.name=="red" :
                self.mem.jugadoractual=self.mem.jugadores.jugador("green")
            elif self.mem.jugadoractual.color.name=="green" :
                self.mem.jugadoractual=self.mem.jugadores.jugador("yellow")
            if self.mem.jugadoractual.plays:#Comprueba si el actual plays y sale del bucle
                break

        self.mem.jugadoractual.tiradaturno=TiradaTurno()#Se crea otro objeto porque así el anterior queda vinculada< a TiradaHistorica.
        self.mem.jugadoractual.movimientos_acumulados=None
        self.mem.jugadoractual.LastFichaMovida=None
    
        self.panel().setActivated(True) #Activa y limpia panel
        self.panel().grp.update()

        self.cmdTirarDado.setStyleSheet('QPushButton {color: '+self.mem.jugadoractual.color.name+'; font: bold 30px; background-color: rgb(170, 170, 170);}')
        self.on_JugadorDebeTirar()


