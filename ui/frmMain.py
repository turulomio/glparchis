## -*- coding: utf-8 -*-
#
## Copyright (c) 2003 - 2008 Detlev Offenbach <detlev@die-offenbachs.de>
##
#
#"""
#Module implementing a dialog for the configuration of eric4s keyboard shortcuts.
#"""
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Ui_frmMain import *
from frmAbout import *
from frmLanguage import *
from wdgUserPanel import *
from wdgOpenGL import *
#from frmMain import frmMain
#
#
#
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
        
#        self.tab.setFixedSize(self.tab.width(), self.tab.width())

        
#        self.vbox = QVBoxLayout(self.tabGame)
#        self.vbox.setObjectName("vbox")

#        
#        self.vboxlayout9 = QVBoxLayout()
#        self.vboxlayout9.setObjectName("vboxlayout9")
        
#        ogl=wdgOpenGL(self.tabGame)
#        
#        print (0, 0, self.tab.width(), self.tab.height(), self.tabGame.frameGeometry().width(), self.tabGame.frameGeometry().height())        
#        ogl.setGeometry(0, 0,  self.tabGame.frameGeometry().width(), self.tabGame.frameGeometry().height())
#        sizePolicy = QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
#        sizePolicy.setHorizontalStretch(0)
#        sizePolicy.setVerticalStretch(0)
#        sizePolicy.setHeightForWidth(ogl.sizePolicy().hasHeightForWidth())
#        ogl.setSizePolicy(sizePolicy)
#        
#        self.vboxlayout9.addWidget(ogl)
        
#        sizePolicy = QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
##        sizePolicy.setHeightForWidth(ogl.sizePolicy().hasHeightForWidth())
#        ogl.setSizePolicy(sizePolicy)
                
#        ogl.resizeGL(self.tabGame.frameGeometry().width(), self.tabGame.frameGeometry().height())
#        ogl.show()
        
        

        self.connect(self.actionAcercaDe, SIGNAL("activated()"), self.on_actionAcercaDe_activated)
        self.connect(self.actionSalir, SIGNAL("activated()"), self.on_actionSalir_activated)
        self.connect(self.actionLenguaje, SIGNAL("activated()"), self.on_actionLenguaje_activated)
        self.connect(self.actionJugar, SIGNAL("activated()"), self.on_actionJugar_activated)
    
    @pyqtSignature("")
    def on_actionAcercaDe_activated(self):
        fr=frmAbout(self, "frmabout")
#        fr.show()
        fr.exec_()
    
    @pyqtSignature("")
    def on_actionSalir_activated(self):
        sys.exit()
    
    @pyqtSignature("")
    def on_actionJugar_activated(self):
#        dockWidget = QDockWidget(self);
#        dockWidget.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea);
#        dockWidget.setWidget(wdgUserPanel)
#        addDockWidget(Qt.LeftDockWidgetArea, dockWidget); 
        self.ogl.updateGL()
    @pyqtSignature("")
    def on_actionLenguaje_activated(self):
        fr=frmLanguage(self, "frmlanguage")
        fr.show()
        fr.exec_()
