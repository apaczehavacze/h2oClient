# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'boxconnection.ui'
#
# Created: Tue Mar 26 12:12:54 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_boxConnection(object):
    def setupUi(self, boxConnection):
        boxConnection.setObjectName(_fromUtf8("boxConnection"))
        boxConnection.resize(400, 300)
        boxConnection.setFlat(False)
        self.labelHostName = QtGui.QLabel(boxConnection)
        self.labelHostName.setGeometry(QtCore.QRect(10, 30, 251, 16))
        self.labelHostName.setObjectName(_fromUtf8("labelHostName"))
        self.lineEditHostName = QtGui.QLineEdit(boxConnection)
        self.lineEditHostName.setGeometry(QtCore.QRect(10, 50, 251, 20))
        self.lineEditHostName.setObjectName(_fromUtf8("lineEditHostName"))
        self.labelPortNumber = QtGui.QLabel(boxConnection)
        self.labelPortNumber.setGeometry(QtCore.QRect(280, 30, 111, 16))
        self.labelPortNumber.setObjectName(_fromUtf8("labelPortNumber"))
        self.spinBoxPortNumber = QtGui.QSpinBox(boxConnection)
        self.spinBoxPortNumber.setGeometry(QtCore.QRect(280, 50, 111, 20))
        self.spinBoxPortNumber.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBoxPortNumber.setObjectName(_fromUtf8("spinBoxPortNumber"))
        self.labelUserName = QtGui.QLabel(boxConnection)
        self.labelUserName.setGeometry(QtCore.QRect(10, 100, 181, 16))
        self.labelUserName.setObjectName(_fromUtf8("labelUserName"))
        self.lineEditUserName = QtGui.QLineEdit(boxConnection)
        self.lineEditUserName.setGeometry(QtCore.QRect(10, 120, 181, 20))
        self.lineEditUserName.setObjectName(_fromUtf8("lineEditUserName"))
        self.labelPassword = QtGui.QLabel(boxConnection)
        self.labelPassword.setGeometry(QtCore.QRect(210, 100, 181, 16))
        self.labelPassword.setObjectName(_fromUtf8("labelPassword"))
        self.lineEditPassword = QtGui.QLineEdit(boxConnection)
        self.lineEditPassword.setGeometry(QtCore.QRect(210, 120, 181, 20))
        self.lineEditPassword.setObjectName(_fromUtf8("lineEditPassword"))
        self.pushButtonConnect = QtGui.QPushButton(boxConnection)
        self.pushButtonConnect.setGeometry(QtCore.QRect(80, 260, 90, 30))
        self.pushButtonConnect.setObjectName(_fromUtf8("pushButtonConnect"))
        self.pushButtonClose = QtGui.QPushButton(boxConnection)
        self.pushButtonClose.setGeometry(QtCore.QRect(230, 260, 90, 30))
        self.pushButtonClose.setObjectName(_fromUtf8("pushButtonClose"))

        self.retranslateUi(boxConnection)
        QtCore.QObject.connect(self.pushButtonClose, QtCore.SIGNAL(_fromUtf8("clicked()")), boxConnection.close)
        QtCore.QMetaObject.connectSlotsByName(boxConnection)

    def retranslateUi(self, boxConnection):
        boxConnection.setWindowTitle(_translate("boxConnection", "Connection", None))
        boxConnection.setTitle(_translate("boxConnection", "Session", None))
        self.labelHostName.setText(_translate("boxConnection", "Host name", None))
        self.labelPortNumber.setText(_translate("boxConnection", "Port number", None))
        self.labelUserName.setText(_translate("boxConnection", "User Name", None))
        self.labelPassword.setText(_translate("boxConnection", "Password", None))
        self.pushButtonConnect.setText(_translate("boxConnection", "Connect", None))
        self.pushButtonClose.setText(_translate("boxConnection", "Close", None))

