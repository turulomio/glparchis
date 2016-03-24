from PyQt5.QtWidgets import *
from libglparchis import *

class QTableStatistics(QTableWidget):
    def __init__(self, parent=None):
        QTableWidget.__init__(self, parent)    


    def assign_mem(self, mem):
        self.mem=mem
        #UI headers
        self.setColumnCount(self.mem.maxplayers+1)        
        for i, j in enumerate(self.mem.jugadores.arr):
            self.setColumnWidth(i, 90)
            item = QTableWidgetItem(j.name)
            item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter)
            item.setIcon(j.color.qicon())   
            self.setHorizontalHeaderItem(i, item)
        item = QTableWidgetItem(self.tr("Total"))
        item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter)
        self.setHorizontalHeaderItem(self.mem.maxplayers, item)
        
        #Crea items
        for i in range(self.mem.maxplayers+1+1):
            for j in range(17):
                item=QTableWidgetItem()
                item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter)
                self.setItem( j,i, item )
                
        #Rallando la tabla
        for i, j in ((11, self.mem.maxplayers), (12, self.mem.maxplayers), (14, self.mem.maxplayers), (16, self.mem.maxplayers)):
            item = QTableWidgetItem()
            item.setTextAlignment(Qt.AlignRight|Qt.AlignVCenter)
            brush = QBrush(QColor(0, 0, 0))
            brush.setStyle(Qt.BDiagPattern)
            item.setBackground(brush)
            self.setItem(i, j, item)
            
#negrita
#        item = QTableWidgetItem()
#        item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter)
#        font = QFont()
#        font.setBold(True)
#        font.setWeight(75)
#        item.setFont(font)
#        self.setItem(16, 0, item)
                
    def widgetCentered(self, qpixmap):
                #Define el widget cron para que aparezca centrado el icon dentro de qtableitem
        w=QWidget()
        lay=QHBoxLayout(w)
        lay.addSpacing(0)
        pix = QLabel()
        pix.setMaximumSize(QSize(24, 24))
        pix.setScaledContents(True)
        pix.setPixmap(qpixmap)
        pix.setAlignment(Qt.AlignCenter)
        lay.addWidget(pix)
        lay.addSpacing(0)
        w.setLayout(lay)
        return w
    
    def reload(self):        
        tj=TiradaJuego(self.mem)
        ganando=self.mem.jugadores.vaGanando()
        for j in self.mem.jugadores.arr:
            column=self.mem.colores.index(j.color)
            self.item(0, column).setText(str(j.tiradahistorica.numThrows()))
            for i in range(2, 8):
                self.item(i, column).setText(str(j.tiradahistorica.numTimesDiceGetNumber(i-1)))
            self.item(9, column).setText(str(j.tiradahistorica.numThreeSixes()))
            self.item(11, column).setText(str(j.comidaspormi))
            self.item(12, column).setText(str(j.comidasporotro))
            
            
            if j==ganando:
                self.setCellWidget(13, column, self.widgetCentered(QPixmap(":/glparchis/corona.png")))    
            else:
                w=QWidget()
                self.setCellWidget(13, column, w)
            
            item=QTableWidgetItem(str(j.casillasMovidas()))
            item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
            self.setItem(14, column, item)    
    
            self.item(16, column).setText(str(j.score()))
        #Ultima columna
        self.item(0, self.mem.maxplayers).setText(str(tj.numThrows()))
        for i in range(2, 8):
            self.item(i, self.mem.maxplayers).setText(str(tj.numTimesDiceGetNumber(i-1)))
        self.item(9, self.mem.maxplayers).setText(str(tj.numThreeSixes()))
        

