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

from Ui_frmLanguage import *
#from frmMain import frmMain
#
#
#
class frmLanguage(QDialog, Ui_frmLanguage):#    
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

        self.connect(self.cmd, SIGNAL("clicked()"), self.on_cmd_clicked)
        self.connect(self.cmd, SIGNAL("textChanged(QString)"), self.on_cmb_textChanged)
    
    @pyqtSignature("")
    def on_cmd_clicked(self):
        self.done(0)

    
    @pyqtSignature("QString")
    def on_cmb_textChanged(self, p0):
#        translator = QTranslator(app)
        if p0==QString("Español"):
            language="es"
        elif p0==QString("English"):
            language="en"
        elif p0==QString("Français"):
            language="fr"
        elif p0==QString("Русский"):
            language="ru"
        translator.load("glparchis_" + language + ".qm")
        app.installTranslator(translator);
