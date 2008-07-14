# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/keko/pyglParchis/ui/frmLanguage.ui'
#
# Created: Sun Jul 13 19:53:37 2008
#      by: PyQt4 UI code generator 4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_frmLanguage(object):
    def setupUi(self, frmLanguage):
        frmLanguage.setObjectName("frmLanguage")
        frmLanguage.setWindowModality(QtCore.Qt.WindowModal)
        frmLanguage.resize(QtCore.QSize(QtCore.QRect(0,0,372,105).size()).expandedTo(frmLanguage.minimumSizeHint()))
        frmLanguage.setWindowIcon(QtGui.QIcon(":/glparchis/kbabel.png"))
        self.vboxlayout = QtGui.QVBoxLayout(frmLanguage)
        self.vboxlayout.setObjectName("vboxlayout")
        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.lbl = QtGui.QLabel(frmLanguage)
        self.lbl.setObjectName("lbl")
        self.hboxlayout.addWidget(self.lbl)
        self.cmb = QtGui.QComboBox(frmLanguage)
        self.cmb.setObjectName("cmb")
        self.hboxlayout.addWidget(self.cmb)
        self.vboxlayout1.addLayout(self.hboxlayout)
        self.cmd = QtGui.QPushButton(frmLanguage)
        self.cmd.setIcon(QtGui.QIcon(":/glparchis/kbabel.png"))
        self.cmd.setObjectName("cmd")
        self.vboxlayout1.addWidget(self.cmd)
        self.vboxlayout.addLayout(self.vboxlayout1)

        self.retranslateUi(frmLanguage)
        QtCore.QMetaObject.connectSlotsByName(frmLanguage)

    def retranslateUi(self, frmLanguage):
        frmLanguage.setWindowTitle(QtGui.QApplication.translate("frmLanguage", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl.setText(QtGui.QApplication.translate("frmLanguage", "Selecciona un idioma", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb.addItem(QtGui.QApplication.translate("frmLanguage", "English", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb.addItem(QtGui.QApplication.translate("frmLanguage", "Español", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb.addItem(QtGui.QApplication.translate("frmLanguage", "Français", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb.addItem(QtGui.QApplication.translate("frmLanguage", "Русский", None, QtGui.QApplication.UnicodeUTF8))
        self.cmd.setText(QtGui.QApplication.translate("frmLanguage", "C&ambiar Idioma", None, QtGui.QApplication.UnicodeUTF8))

import glparchis_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    frmLanguage = QtGui.QDialog()
    ui = Ui_frmLanguage()
    ui.setupUi(frmLanguage)
    frmLanguage.show()
    sys.exit(app.exec_())

