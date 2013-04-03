import sys
from PyQt4 import QtCore, QtGui
from consuc_ui import Ui_conSuc

class ConSuc(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_conSuc()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.ok_button,QtCore.SIGNAL("clicked()"), self.ok_func)

    def ok_func(self):
        self.close()
