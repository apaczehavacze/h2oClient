import sys
from PyQt4 import QtCore, QtGui
from aboutwindow_ui import Ui_aboutWindow

class AboutWindow(QtGui.QScrollArea):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_aboutWindow()
        self.ui.setupUi(self)
