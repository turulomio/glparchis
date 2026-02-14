from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget
from glparchis.ui.wdgUserPanel import wdgUserPanel
from glparchis.libglparchis import HighScore
from glparchis.functions import str2bool, b2s, qmessagebox, delay
from glparchis.version import __version__
from glparchis.ui.Ui_wdgGame import Ui_wdgGame
from datetime import datetime
from glob import glob
from os import path, unlink
from urllib.request import urlopen

## Clase principal del Juego, aqui esta toda la ciencia, cuando se deba pasar al UI se crearan emits que captura qT para el UI
class wdgGame(QWidget, Ui_wdgGame):
    def __init__(self,   parent=None,  filename=None):        
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.show()
        self.panels=[]

    def __del__(self):
        print ("Destructor wdgGame")
        self.stopthegame=True
        for p in self.panels:
            self.panelScrollLayout.removeWidget(p)
        self.hide()

    def sendStatisticsStart(self):
        if str2bool(self.mem.settings.value("frmSettings/statistics", "True"))==True:
            url='http://glparchis.sourceforge.net/php/glparchis_game_start.php?uuid={}&installations_uuid={}&numplayers={}&maxplayers={}&version={}'.format(self.mem.uuid, self.mem.settings.value("frmMain/uuid"),  self.mem.jugadores.numPlays(), self.mem.maxplayers, __version__)
            print(url)
            try:
                web=b2s(urlopen(url).read())
            except:
                web=None
            print (web)       
        
    def sendStatisticsEnd(self):
        if str2bool(self.mem.settings.value("frmSettings/statistics", "True"))==True:
            url='http://glparchis.sourceforge.net/php/glparchis_game_end.php?uuid={}&installations_uuid={}&human_won={}'.format(self.mem.uuid, self.mem.settings.value("frmMain/uuid"),  not self.mem.jugadores.actual.ia)
            print(url)
            try:
                web=b2s(urlopen(url).read())
            except:
                web=None
            print (web)       

    ## Se ejecuta al mover el splitter
    ## @param position Left position
    ## @param index Looks like always is 1
    def on_splitter_splitterMoved(self, position, index):
        if self.mem.frmMain.actionLeftPanel.isChecked()==False: #If user wants to move splitter  when action is not checked
            self.splitter.blockSignals(True)
            self.splitter.moveSplitter(0,1)
            self.splitter.blockSignals(False)
            return

        if self.mem.frmMain.isFullScreen():
            fs="FS"
        else:
            fs=""
        if position!=0:
            self.mem.settings.setValue("wdgGame/splitter_sizes_{}{}".format(fs, self.mem.maxplayers), self.splitter.sizes())
            print("Stored splliter",  self.splitter.sizes())

    ## Método que muestra u oculta el panel izquierdo según se pase el parámetro.
    def showLeftPanel(self, boolean):
        if boolean==True:#Restores splitter
            if self.mem.frmMain.isFullScreen():
                fs="FS"
            else:
                fs=""
            try:
                arr_strsizes=self.mem.settings.value("wdgGame/splitter_sizes_{}{}".format(fs, self.mem.maxplayers), [100, self.ogl.width()-100]) #Returns a list
                sizes=[int(arr_strsizes[0]), int(arr_strsizes[1])]
            except:            
                sizes=[100, self.ogl.width()-100]
                print("EXCEPT IN SHOWLEFTPANEL")
            self.splitter.setSizes(sizes) #position (left position) and index, always 1??

        else:
            self.splitter.moveSplitter(0,  1) #position (left position) and index, always 1??
        #Hides panelScroll to avoid an ugly white box in screen
        if self.mem.frmMain.actionLeftPanel.isChecked():
            self.panelScroll.show()
        else:
            self.panelScroll.hide()

    ## Recargar tabla de estadisticas
    def table_reload(self):
        self.table.reload()
        self.lblTime.setText(self.tr("Tiempo de partida: {0}".format(str(datetime.now()-self.mem.playedtime).split(".")[0])))

    def assign_mem(self, mem):
        self.mem=mem
        self.sendStatisticsStart()
        self.stopthegame=False
        self.table.assign_mem(self.mem)
        self.ogl.assign_mem(self.mem)
        self.ogl.setFocus()
        self.hs3=HighScore(self.mem, 3)
        self.hs4=HighScore(self.mem, 4)
        self.hs6=HighScore(self.mem, 6)
        self.hs8=HighScore(self.mem, 8)
        self.highscoresUpdate()
        
        for j in self.mem.jugadores.arr:
            if j.plays:
                p=wdgUserPanel(self)
                self.panelScrollLayout.addWidget(p)
                p.setJugador(j)
                self.panels.append(p)
        
        self.panel().setActivated(True)
        self.cmdTirarDado.setStyleSheet('QPushButton {color: '+self.mem.jugadores.actual.color.name+'; font: bold 30px; background-color: rgb(170, 170, 170);}')
        self.mem.jugadores.actual.log(self.tr("Empieza la partida"))

        self.ogl.fichaClicked.connect(self.after_ficha_click)

        self.showLeftPanel(self.mem.frmMain.actionLeftPanel.isChecked())
        self.mem.frmMain.showLeftPanel.connect(self.showLeftPanel)
        
        #Coloca los tabs del widget
        self.tab.setCurrentIndex(0)
        if self.mem.maxplayers==3:
            self.tabHS.setCurrentIndex(0)
        if self.mem.maxplayers==4:
            self.tabHS.setCurrentIndex(1)
        elif self.mem.maxplayers==6:
            self.tabHS.setCurrentIndex(2)
        elif self.mem.maxplayers==8:
            self.tabHS.setCurrentIndex(3)
        
        self.ogl.doubleClicked.connect(self.on_ogl_doubleClicked)
        
        if self.mem.playedtime==None:#Caso de que se cree la partida sin cargar .glparchis
            self.mem.playedtime=datetime.now()
        self.table_reload()
        self.on_JugadorDebeTirar()

    def on_ogl_doubleClicked(self):
        if self.cmdTirarDado.isEnabled()==False:
            return
        self.on_cmdTirarDado_clicked()

    def panel(self, jugador=None):
        """Si se pasa sin parametro da el panel del jugador actual"""
        if jugador==None:
            jugador=self.mem.jugadores.actual
        for p in self.panels:
            if p.jugador==jugador:
                return p

    def afterWinning(self):
        self.mem.jugadores.actual.log(self.tr("Has ganado la partida"))
        self.mem.jugadores.winner=self.mem.jugadores.actual
        self.stopthegame=True
        self.mem.play("win", waittofinish=False)
        if self.mem.jugadores.winner.ia==False:#Solo se genera hs cuando es un humano
            if self.mem.maxplayers==3:
                self.hs3.insert()
                self.hs3.save()
            elif self.mem.maxplayers==4:
                self.hs4.insert()
                self.hs4.save()
            elif self.mem.maxplayers==6:
                self.hs6.insert()
                self.hs6.save()
            elif self.mem.maxplayers==8:
                self.hs8.insert()
                self.hs8.save()           
            self.highscoresUpdate()
        self.table_reload()
        
        self.sendStatisticsEnd()
        qmessagebox(self.tr("{0} ha ganado".format(self.mem.jugadores.actual.name)))
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
            
        self.cmdTirarDado.setText(self.tr("Tira el dado"))
        if self.mem.jugadores.actual.ia==False:#Cuando es IA no debe permitir tirar dado
            if self.mem.frmMain.actionAutomatism.isChecked():
                self.mem.jugadores.actual.log(self.tr("Se ha tirado automaticamente el dado"))
                self.on_cmdTirarDado_clicked()
            else:
                self.cmdTirarDado.setEnabled(True)
                self.cmdTirarDado.setFocus()
                self.mem.jugadores.actual.log(self.tr("Tire el dado"))
        elif self.mem.jugadores.actual.ia==True:
            self.mem.jugadores.actual.log(self.tr("IA Tira el dado"))
            self.on_cmdTirarDado_clicked()

    def on_JugadorDebeMover(self):
        """Funcion que se ejecuta cuando un jugador debe mover
        Aqui se evalua si puede mover devolviendo True en caso positivo y """
        
        if self.mem.jugadores.alguienHaGanado()==True:
            self.afterWinning()
            return
        
        self.cmdTirarDado.setEnabled(False)
        if self.mem.jugadores.actual.ia==True:
            self.mem.jugadores.actual.log(self.tr("IA mueve una ficha"))     
            iaficha=self.mem.jugadores.actual.IASelectFicha()
            if iaficha==None:
                self.cambiarJugador()
            else:
                self.mem.selFicha=iaficha
                self.after_ficha_click()
        else:
            if self.mem.frmMain.actionAutomatism.isChecked():
                if self.mem.jugadores.actual.fichas.fichasAutorizadasAMover().length()==1:
                    iaficha=self.mem.jugadores.actual.IASelectFicha()
                    self.mem.selFicha=iaficha
                    self.after_ficha_click()
                    self.mem.jugadores.actual.log(self.tr("Se ha movido automaticamente la unica ficha disponible"))
            else:
                self.mem.jugadores.actual.log(self.tr("Mueva una ficha"))

    @pyqtSlot()      
    def on_cmdTirarDado_clicked(self):  
        self.cmdTirarDado.setEnabled(False)
        self.cmdTirarDado.setText("")
        if self.mem.dado.lasttirada==6: #Si la ultima tirada fue un 6, espera un poco, ya que si no suena muy seguido
            delay(self.mem.delay*1)
        self.mem.jugadores.actual.tirarDado()
        self.table_reload()
        self.mem.dado.showing=True
        self.mem.play("dice")
        self.ogl.updateGL()
        delay(self.mem.delay*2)
        
        self.panel().setLabelDado()
        
        if self.mem.jugadores.actual.tiradaturno.tresSeises()==True:
            if self.mem.jugadores.actual.LastFichaMovida!=None:
                casilla=self.mem.jugadores.actual.LastFichaMovida.casilla()
                if casilla.rampallegada==True:
                    self.mem.jugadores.actual.log(self.tr("Han salido tres seises, no se va a casa por haber llegado a rampa de llegada"))
                else:
                    if self.mem.jugadores.actual.LastFichaMovida.estaAutorizadaAMover()[0]==True:
                        self.mem.jugadores.actual.log(self.tr("Han salido tres seises, la ultima ficha movida se va a casa"))
                        self.mem.play("threesix")
                        self.ogl.updateGL()
                        delay(self.mem.delay*2)
                        self.mem.jugadores.actual.LastFichaMovida.mover(0)
                    else:
                        self.mem.jugadores.actual.log(self.tr("Han salido tres seises, pero como no puede mover no se va a casa"))
            else:               
                self.mem.jugadores.actual.log(self.tr("Despues de tres seises, ya no puede volver a tirar"))
            self.cambiarJugador()
        else: # si no han salido 3 seises
            if self.mem.jugadores.actual.fichas.algunaEstaAutorizadaAmover()==True:
                #delay(self.mem.delay)
                self.on_JugadorDebeMover()
            else:#ninguna puede mover.
                if self.mem.jugadores.actual.tiradaturno.ultimoEsSeis()==True:
                    #delay(self.mem.delay*2)
                    self.on_JugadorDebeTirar()
                else:            
                    #delay(self.mem.delay*2)
                    self.cambiarJugador()

    def after_ficha_click(self):
        if self.mem.selFicha==None:
            self.mem.jugadores.actual.log(self.tr("Seleccione una ficha..."))
            return
            
        if self.cmdTirarDado.isEnabled():#Esta esperando dado no se puede pulsar ficha para mover.
            return
        
        (puede, movimiento)=self.mem.selFicha.estaAutorizadaAMover(None, True)
            
        if puede==False:
            if self.mem.jugadores.actual.ia==False:
                self.mem.play("click")
            return

                
        if self.mem.selFicha.come(self.mem, self.mem.selFicha.posruta+movimiento) or self.mem.selFicha.mete(self.mem.selFicha.posruta+movimiento):    
            self.table_reload()
            delay(self.mem.delay*1)##Se pone antes también para que los movimientos de comer y meter se vean más
            if self.mem.jugadores.actual.movimientos_acumulados==10:
                self.mem.play("meter")
            else:
                self.mem.play("comer")
            self.ogl.updateGL()
            delay(self.mem.delay*2)
            if self.mem.jugadores.actual.fichas.algunaEstaAutorizadaAmover()==True:
                self.on_JugadorDebeMover()
                return
        else:
            self.mem.selFicha.mover( self.mem.selFicha.posruta + movimiento)    
            if movimiento>7:
                self.mem.play("move")
            self.ogl.updateGL()
            delay(self.mem.delay*2)
            self.table_reload()
       #Quita el movimiento acumulados
        if self.mem.jugadores.actual.movimientos_acumulados in (10, 20):
            self.mem.jugadores.actual.movimientos_acumulados=None

        if self.mem.jugadores.actual.tiradaturno.ultimoEsSeis()==True:
            self.on_JugadorDebeTirar()
        else:
            self.cambiarJugador()

    def cambiarJugador(self):          
        if self.mem.jugadores.alguienHaGanado()==True:
            self.afterWinning()
            return          
        self.mem.jugadores.actual.log (self.tr("Fin de turno"))
#        self.ogl.updateGL()        
#        delay(self.mem.delay)
        self.mem.dado.showing=False
        self.ogl.updateGL()        
        delay(self.mem.delay*2)

        self.panel().setActivated(False)
        
        self.mem.jugadores.cambiarJugador()
        self.autosave()    

        if self.chkAvanza.isChecked()==True:
            self.panelScroll.ensureWidgetVisible(self.panel())
        self.panel().setActivated(True) #Activa y limpia panel

        self.cmdTirarDado.setStyleSheet('QPushButton {color: '+self.mem.jugadores.actual.color.name+'; font: bold 30px; background-color: rgb(170, 170, 170);}')
        self.on_JugadorDebeTirar()


    def autosave(self):
        """
            Makes an autosave of the game
        """
                
        #Realiza el autosave
        maxautosaves= int(self.mem.settings.value("frmSettings/autosaves", 15))
        if maxautosaves>0 and self.mem.jugadores.actual.ia==False:
            #Borra el n-esimo autosave
            autosaves=[]
            for infile in glob( path.join(path.expanduser("~/.glparchis/"), 'autosave_*.glparchis') ):
                autosaves.append(infile)
            autosaves.sort()
            if len(autosaves)>=maxautosaves:
                for f in autosaves[:len(autosaves)-maxautosaves+1]:
                    unlink(f)
            #Graba el ultimo autosave
            n=datetime.now()
            dt="{0}{1:02d}{2:02d}_{3:02d}{4:02d}{5:02d}".format(n.year, n.month, n.day, n.hour, n.minute, n.second)
            self.mem.save("autosave_{0}_{1}_{2}.glparchis".format(dt, self.mem.maxplayers, self.mem.jugadores.actual.color.name ))

    def highscoresUpdate(self):
        self.hs3.qtablewidget(self.tblHighScores3)
        self.hs4.qtablewidget(self.tblHighScores4)
        self.hs6.qtablewidget(self.tblHighScores6)
        self.hs8.qtablewidget(self.tblHighScores8)
