## -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from libglparchis import *
import datetime

class QTableStatistics(QTableWidget):
    def __init__(self, parent=None):
        QTableWidget.__init__(self, parent)    



#
#        self.table.setObjectName(_fromUtf8("table"))
#        self.table.setColumnCount(5)
#        self.table.setRowCount(17)
#        item = QTableWidgetItem()
#        self.table.setVerticalHeaderItem(0, item)
#        item = QTableWidgetItem()
#        self.table.setVerticalHeaderItem(1, item)
#        item = QTableWidgetItem()
#        icon1 = QIcon()
#        icon1.addPixmap(QPixmap(_fromUtf8(":/glparchis/cube1.png")), QIcon.Normal, QIcon.Off)
#        item.setIcon(icon1)
#        self.table.setVerticalHeaderItem(2, item)


    def assign_mem(self, mem):
        self.inicio=datetime.datetime.now()
        self.mem=mem
        #UI headers
        self.setColumnCount(self.mem.maxplayers+1)        
        for i, j in enumerate(self.mem.jugadores.arr):
            item = QTableWidgetItem(j.color.name)
            item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter)
            item.setIcon(j.qicon())
            self.setHorizontalHeaderItem(i, item)
        item = QTableWidgetItem(self.trUtf8("Total"))
        item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter)
        icon11 = QIcon()
        icon11.addPixmap(QPixmap(":/glparchis/star.png"), QIcon.Normal, QIcon.Off)
        item.setIcon(icon11)
        self.setHorizontalHeaderItem(self.mem.maxplayers, item)
        
        #Crea items
        for i in range(self.mem.maxplayers+1+1):
            for j in range(17):
                item=QTableWidgetItem()
                item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter)
                self.setItem( j,i, item )
                
        #Rallando la tabla
        for i, j in ((9, self.mem.maxplayers), (10, self.mem.maxplayers), (14, self.mem.maxplayers), (16, self.mem.maxplayers)):
            item = QTableWidgetItem()
            item.setTextAlignment(Qt.AlignRight|Qt.AlignVCenter)
            brush = QBrush(QColor(0, 0, 0))
            brush.setStyle(Qt.BDiagPattern)
            item.setBackground(brush)
            self.setItem(i, j, item)
            
        for i in range(1, self.mem.maxplayers):
            item = QTableWidgetItem()
            item.setTextAlignment(Qt.AlignRight|Qt.AlignVCenter)
            brush = QBrush(QColor(0, 0, 0))
            brush.setStyle(Qt.BDiagPattern)
            item.setBackground(brush)
            self.setItem(16, i, item)


        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.setItem(16, 0, item)
                
        #Timer
        self.timer = QTimer()
        QObject.connect(self.timer, SIGNAL("timeout()"), self.reload)     
        self.timer.start(500)

    
    def stopReloads(self):
        self.timer.stop()
    
    def reload(self):
        #########################################
        if self.mem.maxplayers!=4:
            return
        tj=TiradaJuego(self.mem)
        for j in self.mem.jugadores.arr:
            column=self.mem.colores.index(j.color)
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
