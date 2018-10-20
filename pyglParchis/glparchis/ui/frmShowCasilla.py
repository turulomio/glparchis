from glparchis.ui.Ui_frmShowCasilla import Ui_frmShowCasilla
from PyQt5.QtWidgets import QDialog

class frmShowCasilla(QDialog, Ui_frmShowCasilla):
    def __init__(self, parent = None, flags= None,  casilla=None):
        QDialog.__init__(self, parent, flags)
        self.casilla=casilla
        self.setupUi(self)
        self.lblCasilla.setText(self.tr("Casilla {0}".format(self.casilla.id)))
        self.lblMaxCasillas.setText(self.tr("{0} fichas como maximo".format(self.casilla.maxfichas)))
        if self.casilla.seguro==True:
            self.lblSeguro.setText(self.tr("Casilla segura"))
        else:
            self.lblSeguro.setText(self.tr("Casilla insegura"))
            
        if self.casilla.ruta1==True:
            self.lblSeguro.setText(self.lblSeguro.text()+". "+ self.tr("Ruta 1 de {0}".format(self.casilla.color.name)))
            
        fichas=self.casilla.buzon_fichas() #NO se puede usar buzon[0], porque puede estar en [1]
        
        if len(fichas)==0:
            self.lbl1.hide()
            self.lbl2.hide()
            self.lbl3.hide()
            self.lbl4.hide()
            self.grp.setTitle(self.tr("Casilla vacia"))
        elif len(fichas)==1:
            self.lbl1.setPixmap(fichas[0][1].jugador.color.qpixmap())
            self.lbl2.hide()
            self.lbl3.hide()
            self.lbl4.hide()
            self.grp.setTitle(self.tr("Ocupada con una ficha"))
        elif len(fichas)==2:
            self.lbl1.setPixmap(fichas[0][1].jugador.color.qpixmap())
            self.lbl2.setPixmap(fichas[1][1].jugador.color.qpixmap())
            self.lbl3.hide()
            self.lbl4.hide()
            self.grp.setTitle(self.tr("Ocupada con dos fichas"))
        elif len(fichas)==3:
            self.lbl1.setPixmap(fichas[0][1].jugador.color.qpixmap())
            self.lbl2.setPixmap(fichas[1][1].jugador.color.qpixmap())     
            self.lbl3.setPixmap(fichas[2][1].jugador.color.qpixmap())     
            self.lbl4.hide()
            self.grp.setTitle(self.tr("Ocupada con tres fichas"))
        else:
            self.lbl1.setPixmap(fichas[0][1].jugador.color.qpixmap())
            self.lbl2.setPixmap(fichas[1][1].jugador.color.qpixmap())     
            self.lbl3.setPixmap(fichas[2][1].jugador.color.qpixmap())       
            self.lbl4.setPixmap(fichas[3][1].jugador.color.qpixmap())       
            self.grp.setTitle(self.tr("Casilla llena"))

