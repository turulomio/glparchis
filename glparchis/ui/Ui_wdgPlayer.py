# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'glparchis/ui/wdgPlayer.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_wdgPlayer(object):
    def setupUi(self, wdgPlayer):
        wdgPlayer.setObjectName("wdgPlayer")
        wdgPlayer.resize(799, 88)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(wdgPlayer)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(wdgPlayer)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chkPlays = QtWidgets.QCheckBox(self.frame)
        self.chkPlays.setText("")
        self.chkPlays.setChecked(True)
        self.chkPlays.setObjectName("chkPlays")
        self.horizontalLayout.addWidget(self.chkPlays)
        self.pixmap = QtWidgets.QLabel(self.frame)
        self.pixmap.setText("")
        self.pixmap.setPixmap(QtGui.QPixmap(":/glparchis/fichaamarilla.png"))
        self.pixmap.setObjectName("pixmap")
        self.horizontalLayout.addWidget(self.pixmap)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(200, 0))
        self.label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.txt = QtWidgets.QLineEdit(self.frame)
        self.txt.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txt.setObjectName("txt")
        self.horizontalLayout.addWidget(self.txt)
        self.chkIA = QtWidgets.QCheckBox(self.frame)
        self.chkIA.setObjectName("chkIA")
        self.horizontalLayout.addWidget(self.chkIA)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.frame)

        self.retranslateUi(wdgPlayer)
        QtCore.QMetaObject.connectSlotsByName(wdgPlayer)

    def retranslateUi(self, wdgPlayer):
        _translate = QtCore.QCoreApplication.translate
        wdgPlayer.setWindowTitle(_translate("wdgPlayer", "Form"))
        self.chkPlays.setToolTip(_translate("wdgPlayer", "Seleccionalo si quieres activar al jugador"))
        self.label.setText(_translate("wdgPlayer", "Datos jugador amarillo"))
        self.txt.setToolTip(_translate("wdgPlayer", "Introduce el nombre del jugador"))
        self.txt.setText(_translate("wdgPlayer", "Nombre del Jugador"))
        self.chkIA.setToolTip(_translate("wdgPlayer", "Selecciona si quieres que el jugador lo controle el ordenador"))
        self.chkIA.setText(_translate("wdgPlayer", "Inteligencia artificial?"))

import glparchis.images.glparchis_rc
