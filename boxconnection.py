import sys
from PyQt4 import QtCore, QtGui
from boxconnection_ui import Ui_boxConnection

class BoxConnection(QtGui.QGroupBox):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_boxConnection()
        self.ui.setupUi(self)
        # BoxConnection parameters
        self.hostname = ''
        self.portnumber = 0
        self.username = ''
        self.password = ''
        # slots connections
        QtCore.QObject.connect(self.ui.pushButtonConnect,QtCore.SIGNAL("clicked()"), self.establish_connection)

    def establish_connection(self):
        self.hostname = self.ui.lineEditHostName.text()
        self.username = self.ui.lineEditUserName.text()
        self.password = self.ui.lineEditPassword.text()
        self.portnumber = self.ui.spinBoxPortNumber.value()

#if __name__ == "__main__":
#    app = QtGui.QApplication(sys.argv)
#    boxcon = BoxConnection()
#    boxcon.show()
#    try:
#        sys.exit(app.exec_())
#    except:
#        pass

