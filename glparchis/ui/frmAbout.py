from glparchis.version import __version__
from PyQt5.QtWidgets import QDialog
from glparchis.ui.Ui_frmAbout import Ui_frmAbout

class frmAbout(QDialog, Ui_frmAbout):
    def __init__(self, parent = None, name = None, modal = False):
        """
        Constructor
        
        @param parent The parent widget of this dialog. (QWidget)
        @param name The name of this dialog. (QString)
        @param modal Flag indicating a modal dialog. (boolean)
        """
        QDialog.__init__(self, parent)
        if name:
            self.setObjectName(name)
        self.setupUi(self)
        self.showMaximized()
        self.lblVersion.setText(self.tr("Version {0}".format(__version__)))
        self.textBrowser.setHtml(
            self.tr("La pagina del proyecto se encuentra en <a href=\"http://glparchis.sourceforge.net\">http://glparchis.sourceforge.net</a><p> <p>")+
            self.tr("Este programa ha sido desarrollado por Mariano Munoz.<p>")+
            self.tr("Ha sido traducido por:")+
            "<ul><li>Mariano Munoz</li><li>Nadejda Adam</li></ul><p>\n"+
            self.tr("a los siguientes idiomas<p>")+
            "<ul><li>English</li><li>Fran\xe7ais</li><li>Espa\xf1ol</li><li>Rom\xe2n</li><li>\u0420\u0443\u0441\u0441\u043a\u0438\u0439</li></ul><p>"+
            self.tr("Los avatares han sido extraidos de la pagina <a href=\"http://www.nobleavatar.com/\">http://www.nobleavatar.com/</a><p>"))
        self.cmd.clicked.connect(self.on_cmd_clicked)

    def on_cmd_clicked(self):
        """
        Slot documentation goes here.
        """
        self.done(0)

    def on_table_itemSelectionChanged(self):
        for i in self.table.selectedItems():#itera por cada item no row.
            if i.column()==0:
                self.wdgso.showObject(i.row())
                self.wdgso.setFocus()
