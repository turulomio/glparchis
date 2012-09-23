# -*- coding: utf-8 -*-
import os,  libglparchis
from PyQt4.QtCore import *
from PyQt4.QtGui import *

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
            self.cmbLanguage.setCurrentIndex(self.cmbLanguage.findText(QString(u'Espa\xf1ol')))
        elif self.cfgfile.language=="fr":
            self.cmbLanguage.setCurrentIndex(self.cmbLanguage.findText(QString(u'Fran\xe7ais')))
        elif self.cfgfile.language=="ro":
            self.cmbLanguage.setCurrentIndex(self.cmbLanguage.findText(QString(u'Rom\xe2n')))
        elif self.cfgfile.language=="ru":
            self.cmbLanguage.setCurrentIndex(self.cmbLanguage.findText(QString(u'\u0420\u0443\u0441\u0441\u043a\u0438\u0439')))#ruso

    @pyqtSlot(QString)      
    def on_cmbLanguage_currentIndexChanged(self, stri):
        if stri==QString(u"English"):
            self.cfgfile.language="en"
        elif stri==QString(u'Espa\xf1ol'):#problemas con unicode en python2
            self.cfgfile.language="es"
        elif stri==QString(u'Fran\xe7ais'):
            self.cfgfile.language="fr"
        elif stri==QString(u'Rom\xe2n'):
            self.cfgfile.language="ro"
        elif stri==QString(QString(u'\u0420\u0443\u0441\u0441\u043a\u0438\u0439')):#ruso
            self.cfgfile.language="ru"
        
        libglparchis.cargarQTranslator(self.cfgfile)
        self.retranslateUi(self)
        
    def on_buttonBox_accepted(self):
        self.on_cmbLanguage_currentIndexChanged(self.cmbLanguage.currentText())
        self.cfgfile.save()
