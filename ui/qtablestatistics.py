## -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import libglparchis

class QTableStatistics(QTableWidget):
    def __init__(self, parent=None):
        QTableWidget.__init__(self, parent)    

    
    def assign_mem(self, mem):
        self.mem=mem
        self.timer = QTimer()
        QObject.connect(self.timer, SIGNAL("timeout()"), self.reload)     
        self.timer.start(300)

            
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
        for j in self.mem.jugadores():
            column=color2column(j.color.name)
            self.item(0, column).setText(str(j.tiradahistorica.numThrows()))
            #Rellena numeros
            for i in range(2, 8):
                self.item(i, column).setText(str(j.tiradahistorica.numTimesDiceGetNumber(i-1)))

            self.item(9, column).setText(str(j.comidaspormi))
            self.item(10, column).setText(str(j.comidasporotro))
            self.item(12, column).setText(str(j.tiradahistorica.numThreeSixes()))
