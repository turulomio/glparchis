# -*- coding: utf-8 -*-
import libglparchis
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Ui_frmAbout import *
from wdgQT import *

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
        self.lblVersion.setText(self.trUtf8("Versión %1").arg(libglparchis.version))
        self.textBrowser.setHtml(
self.trUtf8("La página del proyecto se encuentra en <a targe='_blank' href=\"http://glparchis.sourceforge.net\">http://glparchis.sourceforge.net</a><p> <p>")+
self.trUtf8("Este programa ha sido desarrollado por Mariano Muñoz.<p>")+
self.trUtf8("Ha sido traducido por:")+
self.trUtf8("<ul><li>Mariano Muñoz</li><li>Nadejda Adam</li></ul><p>\n")+
self.trUtf8("a los siguientes idiomas<p>")+
self.trUtf8("<ul><li>Inglés</li><li>Francés</li><li>Español</li></ul><p>")+
self.trUtf8("Los avatares han sido extraídos de la página <a href=\"http://www.nobleavatar.com/\">http://www.nobleavatar.com/</a><p>"))
        
        self.connect(self.cmd, SIGNAL("clicked()"), self.on_cmd_clicked)
    @pyqtSignature("")
    def on_cmd_clicked(self):
        """
        Slot documentation goes here.
        """
        self.done(0)
