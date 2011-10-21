## -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import libglparchis, datetime

from Ui_wdgUserPanel import *

    

class wdgUserPanel(QWidget, Ui_wdgUserPanel):
    def __init__(self, parent = None, name = None):
        QWidget.__init__(self, parent)
        self.inittime=datetime.datetime.now()
        if name:
            self.setObjectName(name)
        self.setupUi(self)
        self.color=None
        self.log=[]
        self.history=[]
        
    def setColor(self,  color):
        self.color=color
        if color=="yellow":
            self.lblAvatar.setPixmap(QtGui.QPixmap(":/glparchis/fichaamarilla.png"))
        elif color=="blue":
            self.lblAvatar.setPixmap(QtGui.QPixmap(":/glparchis/fichaazul.png"))
        elif color=="green":
            self.lblAvatar.setPixmap(QtGui.QPixmap(":/glparchis/fichaverde.png"))
        
        
    @QtCore.pyqtSlot(bool)      
    def setEnabled(self, bool):
        if bool==True:
            self.log=[]

    def newLog(self, log):
        log=str(datetime.datetime.now()-self.inittime)[2:-7]+ " " + log
        self.history.append( log)
        self.log.append(log)
        self.on_chk_stateChanged(self.chk.checkState())

    def on_chk_stateChanged(self, state):
        if libglparchis.c2b(state)==True:
            self.lst.setModel(QStringListModel(self.history))
        else:
            self.lst.setModel(QStringListModel(self.log))        
        self.lst.show()            
