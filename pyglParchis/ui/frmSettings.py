 
import os,  libglparchis
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Ui_frmSettings import *
from wdgQT import *

class frmSettings(QDialog, Ui_frmSettings):
    def __init__(self, cfgfile, parent = None, name = None, modal = False):
        QDialog.__init__(self, parent)
        self.cfgfile=cfgfile
        self.setupUi(self)
        
        if self.cfgfile.language=="en":
            self.cmbLanguage.setCurrentIndex(self.cmbLanguage.findText("English"))
        elif self.cfgfile.language=="es":
            self.cmbLanguage.setCurrentIndex(self.cmbLanguage.findText('Español'))
        elif self.cfgfile.language=="fr":
            self.cmbLanguage.setCurrentIndex(self.cmbLanguage.findText('Français'))
        elif self.cfgfile.language=="ro":
            self.cmbLanguage.setCurrentIndex(self.cmbLanguage.findText('Rom\xe2n'))
        elif self.cfgfile.language=="ru":
            self.cmbLanguage.setCurrentIndex(self.cmbLanguage.findText('\u0420\u0443\u0441\u0441\u043a\u0438\u0439'))#ruso
            
        self.spinAutosaves.setValue(self.cfgfile.autosaves)

    @pyqtSlot(str)      
    def on_cmbLanguage_currentIndexChanged(self, stri):
        if stri=="English":
            self.cfgfile.language="en"
        elif stri=='Español':
            self.cfgfile.language="es"
        elif stri=='Fran\xe7ais':
            self.cfgfile.language="fr"
        elif stri=='Rom\xe2n':
            self.cfgfile.language="ro"
        elif stri=='\u0420\u0443\u0441\u0441\u043a\u0438\u0439':#ruso
            self.cfgfile.language="ru"
        
        libglparchis.cargarQTranslator(self.cfgfile)
        self.retranslateUi(self)
        
    def on_buttonBox_accepted(self):
        self.on_cmbLanguage_currentIndexChanged(self.cmbLanguage.currentText())
        self.cfgfile.autosaves=self.spinAutosaves.value()
        self.cfgfile.save()
