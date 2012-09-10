## -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from libglparchis import *
import datetime

class QTableStatistics(QTableWidget):
    def __init__(self, parent=None):
        QTableWidget.__init__(self, parent)    

    
    def assign_mem(self, mem):
        self.inicio=datetime.datetime.now()
        self.mem=mem
        self.timer = QTimer()
        QObject.connect(self.timer, SIGNAL("timeout()"), self.reload)     
        self.timer.start(500)

    
    def stopReloads(self):
        self.timer.stop()
    
    def reload(self):
        def color2column(color):
            if color=="yellow":
                return 0
            elif color=="blue":
                return 1
            elif color=="red":
                return 2
            elif color=="green":
                return 3
        #########################################
        tj=TiradaJuego(self.mem)
        for j in self.mem.jugadores.arr:
            column=color2column(j.color.name)
            self.item(0, column).setText(str(j.tiradahistorica.numThrows()))
            for i in range(2, 8):
                self.item(i, column).setText(str(j.tiradahistorica.numTimesDiceGetNumber(i-1)))
            self.item(9, column).setText(str(j.comidaspormi))
            self.item(10, column).setText(str(j.comidasporotro))
            self.item(12, column).setText(str(j.tiradahistorica.numThreeSixes()))
            item=QTableWidgetItem(str(j.casillasMovidas()))
            item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
            if j==self.mem.jugadores.vaGanando():
                icon = QIcon()
                icon.addPixmap(QPixmap(":/glparchis/corona.png"), QIcon.Normal, QIcon.Off)
                item.setIcon(icon)
            self.setItem(14, column, item)
            
        self.item(0, 4).setText(str(tj.numThrows()))
        for i in range(2, 8):
            self.item(i, 4).setText(str(tj.numTimesDiceGetNumber(i-1)))
        self.item(12, 4).setText(str(tj.numThreeSixes()))
        
        self.item(16, 0).setText(str(datetime.datetime.now()-self.inicio).split(".")[0])
