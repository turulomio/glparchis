from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QApplication
from glparchis.functions import c2b
from glparchis.ui.Ui_wdgPlayer import Ui_wdgPlayer
from glparchis.ui.wdgPlayerDado import wdgPlayerDado

class SetWdgPlayers:
    """Set Jugadores que deben tirar un turno de inicio"""
    def __init__(self):
        self.arr=[]
        
    def qwidget(self):
        q=QWidget()
        horizontalLayout = QHBoxLayout(q)
        label=QLabel(QApplication.translate("glparchis","Ronda de tiradas"))
        horizontalLayout.addWidget(label)
        for wdgplayer in self.arr:
            if wdgplayer.needsToThrowAgain():
                wpd=wdgplayer.newWdgPlayerDado()
                wpd.setName(wdgplayer.txt.text())
                horizontalLayout.addWidget(wpd)
        return q
                
    def Players_throws(self):
        """wdgPlayerDado throws if IA"""
        for i,  w in enumerate(self.arr):
            if w.chkPlays.checkState()==Qt.Checked:#IA#Tira el dado de IA si juega y si es AI
                w.wdgplayerdado.on_cmd_released()

    def strNames(self):
        """Muestra un string con los colores del set"""
        resultado=""
        for w in self.arr:
            resultado=resultado +" " + w.jugador.name +", "
        return resultado[:-2]
        
    def arrWdgPlayers_MaximaPuntuacion(self):
        """Devuelve un SetWdgPlayer con los del arary que tengan maxima puntuaci´on"""
        resultado=SetWdgPlayers()
        max=0
        #Saca la maxima
        for w in self.arr:
            if w.wdgplayerdado.tirada>max:
                max=w.wdgplayerdado.tirada
            
        #Busca cuales tienen la maxima
        for w in self.arr:
            if w.wdgplayerdado.tirada==max:
                resultado.arr.append(w)
        return resultado


class wdgPlayer(QWidget, Ui_wdgPlayer):
    def __init__(self, parent = None, name = None):
        QWidget.__init__(self, parent)
        if name:
            self.setObjectName(name)
        self.setupUi(self)

        self.jugador=None
        self._needsToThrowAgain=True
        self.wdgplayerdado=None#Refers only to the last

    def setJugador(self, j):
        self.jugador=j
        self.pixmap.setPixmap(j.color.qpixmap())
        self.label.setText(self.tr("Datos del jugador {0}".format( (j.color.name))))
        
    def commit(self):
        """Mete en jugador los datos aceptados"""
        self.jugador.name=self.txt.text()
        self.jugador.ia=c2b(self.chkIA.checkState())
        self.jugador.plays=c2b(self.chkPlays.checkState())
        
    def setNeedsToThrowAgain(self, bool):
        self._needsToThrowAgain=bool
        
    def needsToThrowAgain(self):
        return self._needsToThrowAgain
        
    def newWdgPlayerDado(self):
        self.wdgplayerdado=wdgPlayerDado(self.jugador.mem, self.jugador, self)
        return self.wdgplayerdado
        
