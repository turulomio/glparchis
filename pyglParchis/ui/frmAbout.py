## -*- coding: utf-8 -*-
#
## Copyright (c) 2003 - 2008 Detlev Offenbach <detlev@die-offenbachs.de>
##
#
#"""
#Module implementing a dialog for the configuration of eric4s keyboard shortcuts.
#"""
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Ui_frmAbout import *
from wdgQT import *
#from frmMain import frmMain
#
#
#
class frmAbout(QDialog, Ui_frmAbout):
    def __init__(self, parent = None, name = None, modal = False):
        """
        Constructor
        
        @param parent The parent widget of this dialog. (QWidget)
        @param name The name of this dialog. (QString)
        @param modal Flag indicating a modal dialog. (boolean)
        """
        QDialog.__init__(self, parent)
        if name:
            self.setObjectName(name)
        self.setModal(True)
        self.setupUi(self)
        self.showMaximized()
#
#        qt=wdgQT(self.tabQT)
#        
#        qt.setGeometry(1, 1, 400, 400)
#        qt.show()
        
#        self.txtLicense.setSource(QUrl("LICENSE"))
        
        self.connect(self.cmd, SIGNAL("clicked()"), self.on_cmd_clicked)
    
    @pyqtSignature("")
    def on_cmd_clicked(self):
        """
        Slot documentation goes here.
        """
        self.done(0)
