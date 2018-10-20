from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QUrl
from glparchis.ui.Ui_frmGameStatistics import Ui_frmGameStatistics

class frmGameStatistics(QDialog, Ui_frmGameStatistics):
    def __init__(self, uuid, parent = None):
        """
        Constructor
        
        @param parent The parent widget of this dialog. (QWidget)
        @param name The name of this dialog. (QString)
        @param modal Flag indicating a modal dialog. (boolean)
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)       
        print("http://glparchis.sourceforge.net/php/glparchis_statistics_installation.php?installations_uuid={}".format(uuid))
        self.webInstallation.setUrl(QUrl("http://glparchis.sourceforge.net/php/glparchis_statistics_installation.php?installations_uuid={}".format(uuid)))
        self.webWorld.setUrl(QUrl("http://glparchis.sourceforge.net/php/glparchis_statistics.php"))
        self.lblUUID.setText(self.tr("Your statistics UUID is {}").format(uuid))

