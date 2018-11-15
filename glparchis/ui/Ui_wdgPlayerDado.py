# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'glparchis/ui/wdgPlayerDado.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_wdgPlayerDado(object):
    def setupUi(self, wdgPlayerDado):
        wdgPlayerDado.setObjectName("wdgPlayerDado")
        wdgPlayerDado.resize(156, 178)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(wdgPlayerDado)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(wdgPlayerDado)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblName = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblName.sizePolicy().hasHeightForWidth())
        self.lblName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblName.setFont(font)
        self.lblName.setAlignment(QtCore.Qt.AlignCenter)
        self.lblName.setObjectName("lblName")
        self.verticalLayout.addWidget(self.lblName)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pixmap = QtWidgets.QLabel(self.frame)
        self.pixmap.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pixmap.setText("")
        self.pixmap.setPixmap(QtGui.QPixmap(":/glparchis/fichaazul.png"))
        self.pixmap.setAlignment(QtCore.Qt.AlignCenter)
        self.pixmap.setObjectName("pixmap")
        self.horizontalLayout.addWidget(self.pixmap)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.lblDado = QtWidgets.QLabel(self.frame)
        self.lblDado.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lblDado.setText("")
        self.lblDado.setPixmap(QtGui.QPixmap(":/glparchis/cube.png"))
        self.lblDado.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDado.setObjectName("lblDado")
        self.horizontalLayout_3.addWidget(self.lblDado)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addWidget(self.frame)

        self.retranslateUi(wdgPlayerDado)
        QtCore.QMetaObject.connectSlotsByName(wdgPlayerDado)

    def retranslateUi(self, wdgPlayerDado):
        _translate = QtCore.QCoreApplication.translate
        wdgPlayerDado.setWindowTitle(_translate("wdgPlayerDado", "Form"))

import glparchis.images.glparchis_rc
