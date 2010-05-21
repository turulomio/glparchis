# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/keko/Proyectos/glparchis/pyglParchis/ui/frmAbout.ui'
#
# Created: Fri May 21 11:40:15 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_frmAbout(object):
    def setupUi(self, frmAbout):
        frmAbout.setObjectName("frmAbout")
        frmAbout.resize(959, 443)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/glparchis/ficharoja.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmAbout.setWindowIcon(icon)
        self.vboxlayout = QtGui.QVBoxLayout(frmAbout)
        self.vboxlayout.setObjectName("vboxlayout")
        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.lblPixmap = QtGui.QLabel(frmAbout)
        self.lblPixmap.setPixmap(QtGui.QPixmap(":/glparchis/keko.png"))
        self.lblPixmap.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPixmap.setObjectName("lblPixmap")
        self.vboxlayout1.addWidget(self.lblPixmap)
        self.lblApp = QtGui.QLabel(frmAbout)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.lblApp.setFont(font)
        self.lblApp.setAlignment(QtCore.Qt.AlignCenter)
        self.lblApp.setObjectName("lblApp")
        self.vboxlayout1.addWidget(self.lblApp)
        self.tab = QtGui.QTabWidget(frmAbout)
        self.tab.setObjectName("tab")
        self.tabGLParchis = QtGui.QWidget()
        self.tabGLParchis.setObjectName("tabGLParchis")
        self.hboxlayout = QtGui.QHBoxLayout(self.tabGLParchis)
        self.hboxlayout.setObjectName("hboxlayout")
        self.textEdit = QtGui.QTextEdit(self.tabGLParchis)
        self.textEdit.setObjectName("textEdit")
        self.hboxlayout.addWidget(self.textEdit)
        self.tab.addTab(self.tabGLParchis, "")
        self.tabLicense = QtGui.QWidget()
        self.tabLicense.setObjectName("tabLicense")
        self.vboxlayout2 = QtGui.QVBoxLayout(self.tabLicense)
        self.vboxlayout2.setObjectName("vboxlayout2")
        self.txtLicense = QtGui.QTextBrowser(self.tabLicense)
        self.txtLicense.setAutoFormatting(QtGui.QTextEdit.AutoNone)
        self.txtLicense.setLineWrapMode(QtGui.QTextEdit.WidgetWidth)
        self.txtLicense.setAcceptRichText(True)
        self.txtLicense.setSource(QtCore.QUrl("LICENSE"))
        self.txtLicense.setObjectName("txtLicense")
        self.vboxlayout2.addWidget(self.txtLicense)
        self.tab.addTab(self.tabLicense, "")
        self.tabQT = QtGui.QWidget()
        self.tabQT.setObjectName("tabQT")
        self.vboxlayout3 = QtGui.QVBoxLayout(self.tabQT)
        self.vboxlayout3.setObjectName("vboxlayout3")
        self.widget = wdgQT(self.tabQT)
        self.widget.setObjectName("widget")
        self.vboxlayout3.addWidget(self.widget)
        self.tab.addTab(self.tabQT, "")
        self.tabObjetos = QtGui.QWidget()
        self.tabObjetos.setObjectName("tabObjetos")
        self.verticalLayout = QtGui.QVBoxLayout(self.tabObjetos)
        self.verticalLayout.setObjectName("verticalLayout")
        self.wdgso = wdgShowObject(self.tabObjetos)
        self.wdgso.setObjectName("wdgso")
        self.verticalLayout.addWidget(self.wdgso)
        self.tab.addTab(self.tabObjetos, "")
        self.vboxlayout1.addWidget(self.tab)
        self.cmd = QtGui.QPushButton(frmAbout)
        self.cmd.setIcon(icon)
        self.cmd.setObjectName("cmd")
        self.vboxlayout1.addWidget(self.cmd)
        self.vboxlayout.addLayout(self.vboxlayout1)

        self.retranslateUi(frmAbout)
        self.tab.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(frmAbout)

    def retranslateUi(self, frmAbout):
        frmAbout.setWindowTitle(QtGui.QApplication.translate("frmAbout", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.lblApp.setText(QtGui.QApplication.translate("frmAbout", "glParchis", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setHtml(QtGui.QApplication.translate("frmAbout", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Los avatares han sido extraídos de la página http://www.nobleavatar.com/</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tab.setTabText(self.tab.indexOf(self.tabGLParchis), QtGui.QApplication.translate("frmAbout", "Page", None, QtGui.QApplication.UnicodeUTF8))
        self.tab.setTabText(self.tab.indexOf(self.tabLicense), QtGui.QApplication.translate("frmAbout", "Licencia", None, QtGui.QApplication.UnicodeUTF8))
        self.tab.setTabText(self.tab.indexOf(self.tabQT), QtGui.QApplication.translate("frmAbout", "Qt", None, QtGui.QApplication.UnicodeUTF8))
        self.tab.setTabText(self.tab.indexOf(self.tabObjetos), QtGui.QApplication.translate("frmAbout", "Objetos", None, QtGui.QApplication.UnicodeUTF8))
        self.cmd.setText(QtGui.QApplication.translate("frmAbout", "S&alir", None, QtGui.QApplication.UnicodeUTF8))

from wdgShowObject import wdgShowObject
from wdgQT import wdgQT
import glparchis_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    frmAbout = QtGui.QDialog()
    ui = Ui_frmAbout()
    ui.setupUi(frmAbout)
    frmAbout.show()
    sys.exit(app.exec_())

