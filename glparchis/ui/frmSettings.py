from glparchis.functions import str2bool, cargarQTranslator
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import  QPixmap,  QIcon
from PyQt5.QtWidgets import   QDialog, QApplication

from glparchis.ui.Ui_frmSettings import Ui_frmSettings

class Language:
    def __init__(self, id, name):
        self.id=id
        self.name=name
        
    def qpixmap(self):
        if self.id=="fr":
            return QPixmap(":/flags/france.png")
        elif self.id=="es":
            return QPixmap(":/flags/spain.png")
        elif self.id=="en":
            return QPixmap(":/flags/uk.png")
        elif self.id=="ro":
            return QPixmap(":/flags/rumania.png")
        elif self.id=="ru":
            return QPixmap(":/flags/rusia.png")
            
    def qicon(self):
        ico = QIcon()
        ico.addPixmap(self.qpixmap(), QIcon.Normal, QIcon.Off) 
        return ico

class SetLanguages:
    def __init__(self):
        self.arr=[]
        self.selected=None
        self.load_all()
        
    def append(self, o):
        self.arr.append(o)
        
    def load_all(self):
        self.append(Language("en","English" ))
        self.append(Language("es",QApplication.translate("glparchis","Espanol" )))
        self.append(Language("fr",QApplication.translate("glparchis","Francais" )))
        self.append(Language("ro","Rom\xe2n" ))
        self.append(Language("ru",'\u0420\u0443\u0441\u0441\u043a\u0438\u0439' ))

    def find_by_id(self, id):
        for l in self.arr:
            if l.id==id:
                return l
        return None
    def find_by_name(self, name):
        for l in self.arr:
            if l.name==name:
                return l
        return None    
        
    def order_by_name(self):
        """Orders the Set using self.arr"""
        try:
            self.arr=sorted(self.arr, key=lambda c: c.name,  reverse=False)       
            return True
        except:
            return False        

    def qcombobox(self, combo, selected=None):
        """Selected is id"""
        self.order_by_name()
        for l in self.arr:
            combo.addItem(l.qicon(), l.name, l.id)
        if selected!=None:
                combo.setCurrentIndex(combo.findData(selected))

class frmSettings(QDialog, Ui_frmSettings):
    def __init__(self, settings, translator, parent = None, name = None, modal = False):
        QDialog.__init__(self, parent)
        self.settings=settings
        self.translator=translator
        self.parent=parent
        self.setupUi(self)
        self.languages=SetLanguages()
        self.languages.qcombobox(self.cmbLanguage, self.settings.value("frmSettings/language", "en"))            
        self.spinAutosaves.setValue(int(self.settings.value("frmSettings/autosaves", 15)))
        self.chkStatistics.setChecked(str2bool(self.settings.value("frmSettings/statistics", "True")))
        self.spinDelay.setValue(int(self.settings.value("frmSettings/delay", 300)))
        difficulty=int(self.settings.value("frmSettings/difficulty", 70))
        if difficulty==40:
            self.cmbDifficultyLevel.setCurrentIndex(0)
        elif difficulty==55:
            self.cmbDifficultyLevel.setCurrentIndex(1)
        elif difficulty==70:
            self.cmbDifficultyLevel.setCurrentIndex(2)
        elif difficulty==85:
            self.cmbDifficultyLevel.setCurrentIndex(3)
        elif difficulty==100:
            self.cmbDifficultyLevel.setCurrentIndex(4)

    @pyqtSlot(str)      
    def on_cmbLanguage_currentIndexChanged(self, stri):        
        self.languages.selected=self.languages.find_by_name(stri)
        cargarQTranslator(self.translator, self.languages.selected.id)
        self.retranslateUi(self)
        
    def on_buttonBox_accepted(self):
        self.settings.setValue("frmSettings/language", self.languages.selected.id)
        self.settings.setValue("frmSettings/autosaves", self.spinAutosaves.value())
        self.settings.setValue("frmSettings/statistics", self.chkStatistics.isChecked())
        self.settings.setValue("frmSettings/delay", self.spinDelay.value())
        if self.cmbDifficultyLevel.currentIndex()==0:
            difficulty=40
        elif self.cmbDifficultyLevel.currentIndex()==1:
            difficulty=55
        elif self.cmbDifficultyLevel.currentIndex()==2:
            difficulty=70
        elif self.cmbDifficultyLevel.currentIndex()==3:
            difficulty=85
        elif self.cmbDifficultyLevel.currentIndex()==4:
            difficulty=100
        self.settings.setValue("frmSettings/difficulty", difficulty)
        
    def on_cmdGlobalStatistics_released(self):
        self.parent.on_actionMundialStatistics_triggered()

