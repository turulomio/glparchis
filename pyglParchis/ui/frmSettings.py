# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Ui_frmSettings import *
from wdgQT import *

class frmSettings(QDialog, Ui_frmSettings):
    def __init__(self, parent = None, name = None, modal = False):
        QDialog.__init__(self, parent)
        self.setupUi(self)
