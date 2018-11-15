# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'glparchis/ui/frmInitGame.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmInitGame(object):
    def setupUi(self, frmInitGame):
        frmInitGame.setObjectName("frmInitGame")
        frmInitGame.resize(1006, 574)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/glparchis/ficharoja.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmInitGame.setWindowIcon(icon)
        frmInitGame.setSizeGripEnabled(False)
        frmInitGame.setModal(True)
        frmInitGame.setWizardStyle(QtWidgets.QWizard.ClassicStyle)
        self.wizardPage1 = QtWidgets.QWizardPage()
        self.wizardPage1.setObjectName("wizardPage1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.wizardPage1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.wizardPage1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 984, 506))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.scrollPlayer = QtWidgets.QVBoxLayout()
        self.scrollPlayer.setObjectName("scrollPlayer")
        self.verticalLayout_7.addLayout(self.scrollPlayer)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.scrollArea)
        frmInitGame.addPage(self.wizardPage1)
        self.wizardPage2 = QtWidgets.QWizardPage()
        self.wizardPage2.setObjectName("wizardPage2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.wizardPage2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.wizardPage2)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 69, 16))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scrollPlayerDado = QtWidgets.QVBoxLayout()
        self.scrollPlayerDado.setObjectName("scrollPlayerDado")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.scrollPlayerDado.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.scrollPlayerDado.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.scrollPlayerDado)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.scrollArea_2)
        self.lblPlayerStarts = QtWidgets.QLabel(self.wizardPage2)
        self.lblPlayerStarts.setText("")
        self.lblPlayerStarts.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPlayerStarts.setObjectName("lblPlayerStarts")
        self.verticalLayout_2.addWidget(self.lblPlayerStarts)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        frmInitGame.addPage(self.wizardPage2)

        self.retranslateUi(frmInitGame)
        QtCore.QMetaObject.connectSlotsByName(frmInitGame)

    def retranslateUi(self, frmInitGame):
        _translate = QtCore.QCoreApplication.translate
        frmInitGame.setWindowTitle(_translate("frmInitGame", "Configuracion inicial de la partida"))

import glparchis.images.glparchis_rc
