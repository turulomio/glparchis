from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QUrl
from glparchis.ui.Ui_frmGameStatistics import Ui_frmGameStatistics
from logging import info

class frmGameStatistics(QDialog, Ui_frmGameStatistics):
    def __init__(self, url_statistics_world, url_statistics_installation, uuid_installation, parent = None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        info(url_statistics_world)
        info(url_statistics_installation)
        self.webInstallation.setUrl(QUrl(url_statistics_installation))
        self.webWorld.setUrl(QUrl(url_statistics_world))
        self.lblUUID.setText(self.tr("Your statistics UUID is {}").format(uuid_installation))

