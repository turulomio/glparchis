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
        

#        self.connect(self.cmd, SIGNAL("clicked()"), self.on_cmd_clicked)
    
    @pyqtSignature("")
    def on_cmd_clicked(self):        
        print "Hola",  self.cmb.currentText()
        if self.cmb.currentText()==QString("Español"):
            language="es"
        elif self.cmb.currentText()==QString("English"):
            language="en"
        elif self.cmb.currentText()==QString("Français"):
            language="fr"
        elif self.cmb.currentText()==QString("Русский"):
            language="ru"
        app=QApplication.instance()
        translator=QTranslator(app)
        QCore.removeTranslator("/usr/share/pyglparchis/glparchis_en.qm")
        translator.load("/usr/share/pyglparchis/glparchis_" + language + ".qm")
        app.installTranslator(translator);
        self.done(0)


