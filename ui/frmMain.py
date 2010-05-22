## -*- coding: utf-8 -*-
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Ui_frmMain import *
from frmAbout import *
from frmLanguage import *
from wdgUserPanel import *
from wdgGame import *

class frmMain(QMainWindow, Ui_frmMain):#    
    def __init__(self, parent = 0,  flags = False):
        """
        Constructor
        
        @param parent The parent widget of this dialog. (QWidget)
        @param name The name of this dialog. (QString)
        @param modal Flag indicating a modal dialog. (boolean)
        """
        QMainWindow.__init__(self, None)
        self.setupUi(self)
        self.showMaximized()
        
        p1=wdgUserPanel(self.panel1)
        p1.show()
        p2=wdgUserPanel(self.panel2)
        p2.lblAvatar.setPixmap(QtGui.QPixmap(":/glparchis/keki.png"))
        p2.show()
        p3=wdgUserPanel(self.panel3)
        p3.lblAvatar.setPixmap(QtGui.QPixmap(":/glparchis/keke.png"))
        p3.show()
        p4=wdgUserPanel(self.panel4)
        p4.lblAvatar.setPixmap(QtGui.QPixmap(":/glparchis/keka.png"))
        p4.show()
        
    
    @pyqtSignature("")
    def on_actionAcercaDe_activated(self):
        fr=frmAbout(self, "frmabout")
        fr.open()
    
    @QtCore.pyqtSlot()      
    def on_actionSalir_activated(self):
        sys.exit()
    
    @QtCore.pyqtSlot()      
    def on_actionJugar_activated(self):
        self.ogl.updateGL()
        
    @QtCore.pyqtSlot()      
    def on_actionLenguaje_activated(self):
        fr=frmLanguage(self, "frmlanguage")
        fr.open()
