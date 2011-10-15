## -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Ui_frmInitGame import *

class frmInitGame(QWizard, Ui_frmInitGame):
    def __init__(self, parent = None, name = None, modal = False):
        QDialog.__init__(self, parent)
        if name:
            self.setObjectName(name)
        self.setModal(True)
        self.setupUi(self)
