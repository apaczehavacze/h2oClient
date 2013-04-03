
from PyQt4 import QtCore, QtGui
from klienttest_ui import Ui_Client
from gui import Ui_MainWindow

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.listModule.insertItem(0, 'pierwszy zaj.... modulasdasd')
        self.ui.listModule.insertItem(1, 'drugi zaj..... modul')
        self.ui.listModule.insertItem(2, 'drugi zaj..... mo')
        self.ui.listModule.setMinimumWidth(self.ui.listModule.visualItemRect(self.ui.listModule.item(0)).size().width()+15)
        self.file_dialog()
        # tutaj dajemy wlasne polaczenia slotow
#      QtCore.QObject.connect(self.ui.actionOpen,QtCore.SIGNAL("triggered()"), self.file_dialog)
#        QtCore.QObject.connect(self.ui.buttonOpt,QtCore.SIGNAL("clicked()"), self.clickSend)
#        QtCore.QObject.connect(self.ui.listWidget_adv,QtCore.SIGNAL("itemChanged(QListWidgetItem *)"), self.test_fun)
    
        
    def file_dialog(self):
        req_version = (2,8)
        cur_version = sys.version_info
        
        if cur_version >= req_version:
            import configparser
            config = configparser.ConfigParser()
        else:
            import ConfigParser
            config = ConfigParser.ConfigParser()
            
        config = configparser.RawConfigParser()
        config.read('example.config')
        for x in config.sections(): 
            for y in config.options(x):
                if y == 'question':
                    if 'type' in config.options(x):
                        if 'bool' in config.get(x, 'type'):
                            answer = QtGui.QCheckBox()
                        elif 'string' in config.get(x, 'type'):
                            answer = QtGui.QLineEdit()
                        elif 'choice' in config.get(x, 'type'):
                            answer = QtGui.QComboBox()
                        self.ui.appendForm(QtGui.QLabel(config.get(x, y)), answer)

                
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
