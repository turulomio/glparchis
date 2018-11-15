# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'glparchis/ui/frmGameStatistics.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmGameStatistics(object):
    def setupUi(self, frmGameStatistics):
        frmGameStatistics.setObjectName("frmGameStatistics")
        frmGameStatistics.setWindowModality(QtCore.Qt.WindowModal)
        frmGameStatistics.resize(991, 798)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/glparchis/statistics.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmGameStatistics.setWindowIcon(icon)
        frmGameStatistics.setModal(True)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(frmGameStatistics)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblApp = QtWidgets.QLabel(frmGameStatistics)
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
        self.lblPixmap = QtWidgets.QLabel(frmGameStatistics)
        self.lblPixmap.setMaximumSize(QtCore.QSize(68, 68))
        self.lblPixmap.setPixmap(QtGui.QPixmap(":/glparchis/statistics.png"))
        self.lblPixmap.setScaledContents(True)
        self.lblPixmap.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPixmap.setObjectName("lblPixmap")
        self.horizontalLayout.addWidget(self.lblPixmap)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tab = QtWidgets.QTabWidget(frmGameStatistics)
        self.tab.setObjectName("tab")
        self.tabGLParchis = QtWidgets.QWidget()
        self.tabGLParchis.setObjectName("tabGLParchis")
        self.hboxlayout = QtWidgets.QHBoxLayout(self.tabGLParchis)
        self.hboxlayout.setObjectName("hboxlayout")
        self.webInstallation = QtWebEngineWidgets.QWebEngineView(self.tabGLParchis)
        self.webInstallation.setUrl(QtCore.QUrl("about:blank"))
        self.webInstallation.setObjectName("webInstallation")
        self.hboxlayout.addWidget(self.webInstallation)
        self.tab.addTab(self.tabGLParchis, "")
        self.tabLicense = QtWidgets.QWidget()
        self.tabLicense.setObjectName("tabLicense")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.tabLicense)
        self.vboxlayout.setObjectName("vboxlayout")
        self.webWorld = QtWebEngineWidgets.QWebEngineView(self.tabLicense)
        self.webWorld.setUrl(QtCore.QUrl("about:blank"))
        self.webWorld.setObjectName("webWorld")
        self.vboxlayout.addWidget(self.webWorld)
        self.tab.addTab(self.tabLicense, "")
        self.verticalLayout.addWidget(self.tab)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.lblUUID = QtWidgets.QLabel(frmGameStatistics)
        self.lblUUID.setText("")
        self.lblUUID.setObjectName("lblUUID")
        self.verticalLayout_2.addWidget(self.lblUUID)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.retranslateUi(frmGameStatistics)
        self.tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmGameStatistics)

    def retranslateUi(self, frmGameStatistics):
        _translate = QtCore.QCoreApplication.translate
        frmGameStatistics.setWindowTitle(_translate("frmGameStatistics", "Estadisticas de juego"))
        self.lblApp.setText(_translate("frmGameStatistics", "Estadisticas de juego"))
        self.tab.setTabText(self.tab.indexOf(self.tabGLParchis), _translate("frmGameStatistics", "Estadisticas de esta instalacion"))
        self.tab.setTabText(self.tab.indexOf(self.tabLicense), _translate("frmGameStatistics", "Estadisticas mundiales"))

from PyQt5 import QtWebEngineWidgets
import glparchis.images.glparchis_rc
