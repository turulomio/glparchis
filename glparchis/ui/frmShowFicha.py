from PyQt5.QtCore import pyqtSlot, Qt
from glparchis.ui.Ui_frmShowFicha import Ui_frmShowFicha
from PyQt5.QtWidgets import QDialog, QTableWidgetItem

class frmShowFicha(QDialog, Ui_frmShowFicha):
    def __init__(self,   parent = None, flags= None,  ficha=None, mem=None):
        QDialog.__init__(self, parent, flags)
        self.mem=mem
        self.ficha=ficha
        self.setupUi(self)
        self.lblFicha.setPixmap(self.ficha.jugador.color.qpixmap())       
        self.lblName.setText(self.tr("Nombre: {0}".format(self.ficha.id)))
        self.lblJugador.setText(self.tr("Jugador: {0} ({1})".format(self.ficha.jugador.name, self.ficha.jugador.color.name)))
        self.lblRuta.setText(self.tr("Posicion en ruta: {0}".format(self.ficha.posruta)))
        self.tblAmenazas_reload()
        if self.mem.jugadores.actual.tiradaturno.ultimoValor()!=None:
            (puedemover, movimiento)=self.ficha.puedeMover()
            if puedemover==True:
                self.cmbDestino.setCurrentIndex(self.cmbDestino.findText(str(movimiento)))
                self.on_cmbDestino_currentIndexChanged(str(movimiento))

    def tblAmenazas_reload(self):
        self.table_reload(self.tblAmenazas, self.ficha.amenazas())

    @pyqtSlot(str)      
    def on_cmbDestino_currentIndexChanged(self, stri):
        self.group.setTitle(self.tr("Amenazas en la casilla {0}".format(self.ficha.casilla(self.ficha.posruta+int(stri)).id)))
        self.table_reload(self.tblAmenazasDestino, self.ficha.amenazasDestino( int(stri)))
                
        
    def table_reload(self, table, setamenazas):
#        table.verticalHeader().setResizeMode(QHeaderView.ResizeToContents)
#        table.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
        table.setRowCount(len(setamenazas.arr))        
        for i,  a in enumerate(setamenazas.arr):
            item = QTableWidgetItem()
            item.setIcon(a.atacante.color.qicon())                
            table.setItem(i, 0, QTableWidgetItem(item))
            item = QTableWidgetItem(str(a.atacante.casilla().id))
            item.setTextAlignment(Qt.AlignCenter)
            table.setItem(i, 1, item)
            item = QTableWidgetItem(a.name())
            table.setItem(i, 2, item)
