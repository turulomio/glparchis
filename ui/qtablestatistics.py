## -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import libglparchis

class QTableStatistics(QTableWidget):
    def __init__(self, parent=None):
        QTableWidget.__init__(self, parent)    
        self.tiradas=[]
        self.dado1=[]
        self.dado2=[]
        self.dado3=[]
        self.dado4=[]
        self.dado5=[]
        self.dado6=[]
        self.comidaspormi=[]
        self.comidasporotro=[]
        self.tres6seguidos=[]
        for i in range(4):
            self.tiradas.append(0)
            self.dado1.append(0)
            self.dado2.append(0)
            self.dado3.append(0)
            self.dado4.append(0)
            self.dado5.append(0)
            self.dado6.append(0)
            self.comidaspormi.append(0)
            self.comidasporotro.append(0)
            self.tres6seguidos.append(0)

            
    def registraTirada(self, color, dado):
        i=libglparchis.colorid(color)
        self.tiradas[i]=self.tiradas[i]+1
        if dado==1:
            self.dado1[i]=self.dado1[i]+1
        elif dado==2:
            self.dado2[i]=self.dado2[i]+1
        elif dado==3:
            self.dado3[i]=self.dado3[i]+1
        elif dado==4:
            self.dado4[i]=self.dado4[i]+1
        elif dado==5:
            self.dado5[i]=self.dado5[i]+1
        elif dado==6:
            self.dado6[i]=self.dado6[i]+1
        self.reload()
            
            
    def registraTres6Seguidos(self, color):
        i=libglparchis.colorid(color)        
        self.tres6seguidos[i]=self.tres6seguidos[i]+1
        self.reload()
        
    def registraComidaPorMi(self, color):
        i=libglparchis.colorid(color)
        self.comidaspormi[i]=self.comidaspormi[i]+1
        self.reload()
    
    def registraComidaPorOtro(self, color):
        i=libglparchis.colorid(color)
        self.comidasporotro[i]=self.comidasporotro[i]+1
        self.reload()
    
    def reload(self):
        for i in range(4):
            self.item(0, i).setText(str(self.tiradas[i]))
            self.item(2, i).setText(str(self.dado1[i]))
            self.item(3, i).setText(str(self.dado2[i]))
            self.item(4, i).setText(str(self.dado3[i]))
            self.item(5, i).setText(str(self.dado4[i]))
            self.item(6, i).setText(str(self.dado5[i]))
            self.item(7, i).setText(str(self.dado6[i]))
            self.item(9, i).setText(str(self.comidaspormi[i]))
            self.item(10, i).setText(str(self.comidasporotro[i]))
            self.item(12, i).setText(str(self.tres6seguidos[i]))
