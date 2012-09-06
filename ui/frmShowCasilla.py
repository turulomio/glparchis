## -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Ui_frmShowCasilla import *   

class frmShowCasilla(QDialog, Ui_frmShowCasilla):
    def __init__(self, parent = None, flags= None,  casilla=None):
        QDialog.__init__(self, parent, flags)
        self.casilla=casilla
        self.setupUi(self)
        self.lblCasilla.setText(self.trUtf8("Casilla %1").arg(str(self.casilla.id)))
        self.lblMaxCasillas.setText(self.trUtf8("%1 fichas como máximo").arg(str(self.casilla.maxfichas)))
        if self.casilla.seguro==True:
            self.lblSeguro.setText(self.trUtf8("Casilla segura"))
        else:
            self.lblSeguro.setText(self.trUtf8("Casilla insegura"))
            
        fichas=self.casilla.buzon_fichas() #NO se puede usar buzon[0], porque puede estar en [1]
        
        if len(fichas)==0:
            self.lbl1.hide()
            self.lbl2.hide()
            self.lbl3.hide()
            self.lbl4.hide()
            self.grp.setTitle(self.trUtf8("Casilla vacía"))
        elif len(fichas)==1:
            self.lbl1.setPixmap(fichas[0][1].jugador.qpixmap())
            self.lbl2.hide()
            self.lbl3.hide()
            self.lbl4.hide()
            self.grp.setTitle(self.trUtf8("Ocupada con una ficha"))
        elif len(fichas)==2:
            self.lbl1.setPixmap(fichas[0][1].jugador.qpixmap())
            self.lbl2.setPixmap(fichas[1][1].jugador.qpixmap())
            self.lbl3.hide()
            self.lbl4.hide()
            self.grp.setTitle(self.trUtf8("Ocupada con dos fichas"))
        elif len(fichas)==3:
            self.lbl1.setPixmap(fichas[0][1].jugador.qpixmap())
            self.lbl2.setPixmap(fichas[1][1].jugador.qpixmap())     
            self.lbl3.setPixmap(fichas[2][1].jugador.qpixmap())     
            self.lbl4.hide()
            self.grp.setTitle(self.trUtf8("Ocupada con tres fichas"))
        else:
            self.lbl1.setPixmap(fichas[0][1].jugador.qpixmap())
            self.lbl2.setPixmap(fichas[1][1].jugador.qpixmap())     
            self.lbl3.setPixmap(fichas[2][1].jugador.qpixmap())       
            self.lbl4.setPixmap(fichas[3][1].jugador.qpixmap())       
            self.grp.setTitle(self.trUtf8("Casilla llena"))

