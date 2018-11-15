# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'glparchis/ui/frmHelp.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmHelp(object):
    def setupUi(self, frmHelp):
        frmHelp.setObjectName("frmHelp")
        frmHelp.setWindowModality(QtCore.Qt.WindowModal)
        frmHelp.resize(549, 607)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/glparchis/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmHelp.setWindowIcon(icon)
        frmHelp.setSizeGripEnabled(True)
        frmHelp.setModal(True)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(frmHelp)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblApp = QtWidgets.QLabel(frmHelp)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblApp.setFont(font)
        self.lblApp.setAlignment(QtCore.Qt.AlignCenter)
        self.lblApp.setObjectName("lblApp")
        self.verticalLayout.addWidget(self.lblApp)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lblPixmap = QtWidgets.QLabel(frmHelp)
        self.lblPixmap.setMaximumSize(QtCore.QSize(68, 68))
        self.lblPixmap.setPixmap(QtGui.QPixmap(":/glparchis/help.png"))
        self.lblPixmap.setScaledContents(True)
        self.lblPixmap.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPixmap.setObjectName("lblPixmap")
        self.horizontalLayout.addWidget(self.lblPixmap)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.browser = QtWidgets.QTextBrowser(frmHelp)
        self.browser.setOpenExternalLinks(True)
        self.browser.setObjectName("browser")
        self.verticalLayout.addWidget(self.browser)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(frmHelp)
        QtCore.QMetaObject.connectSlotsByName(frmHelp)

    def retranslateUi(self, frmHelp):
        _translate = QtCore.QCoreApplication.translate
        frmHelp.setWindowTitle(_translate("frmHelp", "Ayuda de glParchis"))
        self.lblApp.setText(_translate("frmHelp", "Ayuda de glParchis"))

import glparchis.images.glparchis_rc
