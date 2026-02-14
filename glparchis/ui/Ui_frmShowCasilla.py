# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'glparchis/ui/frmShowCasilla.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmShowCasilla(object):
    def setupUi(self, frmShowCasilla):
        frmShowCasilla.setObjectName("frmShowCasilla")
        frmShowCasilla.resize(292, 184)
        frmShowCasilla.setStyleSheet("background-color: rgb(253, 255, 190);")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(frmShowCasilla)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblCasilla = QtWidgets.QLabel(frmShowCasilla)
        self.lblCasilla.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCasilla.setObjectName("lblCasilla")
        self.verticalLayout.addWidget(self.lblCasilla)
        self.lblMaxCasillas = QtWidgets.QLabel(frmShowCasilla)
        self.lblMaxCasillas.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMaxCasillas.setObjectName("lblMaxCasillas")
        self.verticalLayout.addWidget(self.lblMaxCasillas)
        self.lblSeguro = QtWidgets.QLabel(frmShowCasilla)
        self.lblSeguro.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSeguro.setObjectName("lblSeguro")
        self.verticalLayout.addWidget(self.lblSeguro)
        self.grp = QtWidgets.QGroupBox(frmShowCasilla)
        self.grp.setObjectName("grp")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.grp)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl1 = QtWidgets.QLabel(self.grp)
        self.lbl1.setText("")
        self.lbl1.setPixmap(QtGui.QPixmap(":/glparchis/fichaamarilla.png"))
        self.lbl1.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl1.setObjectName("lbl1")
        self.horizontalLayout.addWidget(self.lbl1)
        self.lbl2 = QtWidgets.QLabel(self.grp)
        self.lbl2.setText("")
        self.lbl2.setPixmap(QtGui.QPixmap(":/glparchis/fichaamarilla.png"))
        self.lbl2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl2.setObjectName("lbl2")
        self.horizontalLayout.addWidget(self.lbl2)
        self.lbl3 = QtWidgets.QLabel(self.grp)
        self.lbl3.setText("")
        self.lbl3.setPixmap(QtGui.QPixmap(":/glparchis/fichaamarilla.png"))
        self.lbl3.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl3.setObjectName("lbl3")
        self.horizontalLayout.addWidget(self.lbl3)
        self.lbl4 = QtWidgets.QLabel(self.grp)
        self.lbl4.setText("")
        self.lbl4.setPixmap(QtGui.QPixmap(":/glparchis/fichaamarilla.png"))
        self.lbl4.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl4.setObjectName("lbl4")
        self.horizontalLayout.addWidget(self.lbl4)
        self.verticalLayout.addWidget(self.grp)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(frmShowCasilla)
        QtCore.QMetaObject.connectSlotsByName(frmShowCasilla)

    def retranslateUi(self, frmShowCasilla):
        _translate = QtCore.QCoreApplication.translate
        frmShowCasilla.setWindowTitle(_translate("frmShowCasilla", "Dialog"))
        self.lblCasilla.setText(_translate("frmShowCasilla", "TextLabel"))
        self.lblMaxCasillas.setText(_translate("frmShowCasilla", "TextLabel"))
        self.lblSeguro.setText(_translate("frmShowCasilla", "TextLabel"))
        self.grp.setTitle(_translate("frmShowCasilla", "Ocupacion"))

import glparchis.images.glparchis_rc
