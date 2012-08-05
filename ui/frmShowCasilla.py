## -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Ui_frmShowCasilla import *   
import libglparchis

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
        if len(self.casilla.buzon)==0:
            self.lbl1.hide()
            self.lbl2.hide()
            self.lbl3.hide()
            self.lbl4.hide()
            self.grp.setTitle(self.trUtf8("Casilla vacía"))
        elif len(self.casilla.buzon)==1:
            self.lbl1.setPixmap(libglparchis.pixficha(self.casilla.buzon[0].colorname))    
            self.lbl2.hide()
            self.lbl3.hide()
            self.lbl4.hide()
            self.grp.setTitle(self.trUtf8("Ocupada con una ficha"))
        elif len(self.casilla.buzon)==2:
            self.lbl1.setPixmap(libglparchis.pixficha(self.casilla.buzon[0].colorname))       
            self.lbl2.setPixmap(libglparchis.pixficha(self.casilla.buzon[1].colorname))   
            self.lbl3.hide()
            self.lbl4.hide()
            self.grp.setTitle(self.trUtf8("Ocupada con dos fichas"))
        elif len(self.casilla.buzon)==3:
            self.lbl1.setPixmap(libglparchis.pixficha(self.casilla.buzon[0].colorname))       
            self.lbl2.setPixmap(libglparchis.pixficha(self.casilla.buzon[1].colorname))       
            self.lbl3.setPixmap(libglparchis.pixficha(self.casilla.buzon[2].colorname))    
            self.lbl4.hide()
            self.grp.setTitle(self.trUtf8("Ocupada con tres fichas"))
        else:
            self.lbl1.setPixmap(libglparchis.pixficha(self.casilla.buzon[0].colorname))       
            self.lbl2.setPixmap(libglparchis.pixficha(self.casilla.buzon[1].colorname))       
            self.lbl3.setPixmap(libglparchis.pixficha(self.casilla.buzon[2].colorname))       
            self.lbl4.setPixmap(libglparchis.pixficha(self.casilla.buzon[3].colorname)) 
            self.grp.setTitle(self.trUtf8("Casilla llena"))

