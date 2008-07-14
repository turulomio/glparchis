# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/keko/pyglParchis/ui/wdgUserPanel.ui'
#
# Created: Sun Jul 13 23:17:43 2008
#      by: PyQt4 UI code generator 4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_wdgUserPanel(object):
    def setupUi(self, wdgUserPanel):
        wdgUserPanel.setObjectName("wdgUserPanel")
        wdgUserPanel.resize(QtCore.QSize(QtCore.QRect(0,0,378,125).size()).expandedTo(wdgUserPanel.minimumSizeHint()))
        self.vboxlayout = QtGui.QVBoxLayout(wdgUserPanel)
        self.vboxlayout.setObjectName("vboxlayout")
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.lblAvatar = QtGui.QLabel(wdgUserPanel)
        self.lblAvatar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblAvatar.setPixmap(QtGui.QPixmap(":/glparchis/keko.png"))
        self.lblAvatar.setScaledContents(False)
        self.lblAvatar.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAvatar.setObjectName("lblAvatar")
        self.vboxlayout1.addWidget(self.lblAvatar)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.lblTurn = QtGui.QLabel(wdgUserPanel)
        self.lblTurn.setPixmap(QtGui.QPixmap(":/glparchis/star.png"))
        self.lblTurn.setScaledContents(False)
        self.lblTurn.setObjectName("lblTurn")
        self.hboxlayout1.addWidget(self.lblTurn)
        self.lbl1 = QtGui.QLabel(wdgUserPanel)
        self.lbl1.setPixmap(QtGui.QPixmap(":/glparchis/cube6.png"))
        self.lbl1.setScaledContents(True)
        self.lbl1.setObjectName("lbl1")
        self.hboxlayout1.addWidget(self.lbl1)
        self.lbl2 = QtGui.QLabel(wdgUserPanel)
        self.lbl2.setPixmap(QtGui.QPixmap(":/glparchis/cube6.png"))
        self.lbl2.setScaledContents(True)
        self.lbl2.setObjectName("lbl2")
        self.hboxlayout1.addWidget(self.lbl2)
        self.lbl3 = QtGui.QLabel(wdgUserPanel)
        self.lbl3.setPixmap(QtGui.QPixmap(":/glparchis/cube6.png"))
        self.lbl3.setScaledContents(True)
        self.lbl3.setObjectName("lbl3")
        self.hboxlayout1.addWidget(self.lbl3)
        self.vboxlayout1.addLayout(self.hboxlayout1)
        self.hboxlayout.addLayout(self.vboxlayout1)
        self.lst = QtGui.QListView(wdgUserPanel)
        self.lst.setObjectName("lst")
        self.hboxlayout.addWidget(self.lst)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.retranslateUi(wdgUserPanel)
        QtCore.QMetaObject.connectSlotsByName(wdgUserPanel)

    def retranslateUi(self, wdgUserPanel):
        wdgUserPanel.setWindowTitle(QtGui.QApplication.translate("wdgUserPanel", "Form", None, QtGui.QApplication.UnicodeUTF8))

import glparchis_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    wdgUserPanel = QtGui.QWidget()
    ui = Ui_wdgUserPanel()
    ui.setupUi(wdgUserPanel)
    wdgUserPanel.show()
    sys.exit(app.exec_())

