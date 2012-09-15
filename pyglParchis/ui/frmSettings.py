# -*- coding: utf-8 -*-
import os,  libglparchis
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Ui_frmSettings import *
from wdgQT import *

class frmSettings(QDialog, Ui_frmSettings):
    def __init__(self, language, parent = None, name = None, modal = False):
        QDialog.__init__(self, parent)
        self.language=language
        self.setupUi(self)
        if self.language=="en":
            self.cmbLanguage.setCurrentIndex(self.cmbLanguage.findText("English"))
        elif self.language=="es":
            self.cmbLanguage.setCurrentIndex(self.cmbLanguage.findText(QString(u'Espa\xf1ol')))
        elif self.language=="fr":
            self.cmbLanguage.setCurrentIndex(self.cmbLanguage.findText("France"))
        elif self.language=="ru":
            self.cmbLanguage.setCurrentIndex(self.cmbLanguage.findText("Ruso"))

    @pyqtSlot(QString)      
    def on_cmbLanguage_currentIndexChanged(self, stri):
        if stri==QString(u"English"):
            self.language="en"
        elif stri==QString(u'Espa\xf1ol'):#problemas con unicode en python2
            self.language="es"
        elif stri==QString(u"France"):
            self.language="fr"
        elif stri==QString(u"Ruso"):
            self.language="ru"
        
        libglparchis.cargarQTranslator(self.language)
        self.retranslateUi(self)
        
    def on_buttonBox_accepted(self):
        self.on_cmbLanguage_currentIndexChanged(self.cmbLanguage.currentText())
