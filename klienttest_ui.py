# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'klienttest.ui'
#
# Created: Sat Mar 23 17:18:28 2013
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

class Ui_Client(object):
    def setupUi(self, Client):
        Client.setObjectName(_fromUtf8("Client"))
        Client.resize(840, 593)
        self.centralwidget = QtGui.QWidget(Client)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.formLayout = QtGui.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.textBrowser_test = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser_test.setObjectName(_fromUtf8("textBrowser_test"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.textBrowser_test)
        self.tabWidget_bas = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tabWidget_bas.sizePolicy().hasHeightForWidth())
        self.tabWidget_bas.setSizePolicy(sizePolicy)
        self.tabWidget_bas.setSizeIncrement(QtCore.QSize(0, 0))
        self.tabWidget_bas.setObjectName(_fromUtf8("tabWidget_bas"))
        self.tab_basic = QtGui.QWidget()
        self.tab_basic.setObjectName(_fromUtf8("tab_basic"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab_basic)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.form_label = QtGui.QLabel(self.tab_basic)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.form_label.setFont(font)
        self.form_label.setFrameShape(QtGui.QFrame.Box)
        self.form_label.setLineWidth(1)
        self.form_label.setMidLineWidth(0)
        self.form_label.setTextFormat(QtCore.Qt.AutoText)
        self.form_label.setScaledContents(False)
        self.form_label.setAlignment(QtCore.Qt.AlignCenter)
        self.form_label.setObjectName(_fromUtf8("form_label"))
        self.verticalLayout.addWidget(self.form_label)
        self.listWidget_bas = QtGui.QListWidget(self.tab_basic)
        self.listWidget_bas.setObjectName(_fromUtf8("listWidget_bas"))
        self.verticalLayout.addWidget(self.listWidget_bas)
        self.listWidget_bas1 = QtGui.QListWidget(self.tab_basic)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_bas1.sizePolicy().hasHeightForWidth())
        self.listWidget_bas1.setSizePolicy(sizePolicy)
        self.listWidget_bas1.setObjectName(_fromUtf8("listWidget_bas1"))
        self.verticalLayout.addWidget(self.listWidget_bas1)
        self.tabWidget_bas.addTab(self.tab_basic, _fromUtf8(""))
        self.tab_advanced = QtGui.QWidget()
        self.tab_advanced.setObjectName(_fromUtf8("tab_advanced"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_advanced)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.tab_advanced)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtGui.QFrame.Box)
        self.label_2.setLineWidth(1)
        self.label_2.setMidLineWidth(0)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.listWidget_adv = QtGui.QListWidget(self.tab_advanced)
        self.listWidget_adv.setObjectName(_fromUtf8("listWidget_adv"))
        self.verticalLayout_2.addWidget(self.listWidget_adv)
        self.listWidget_adv1 = QtGui.QListWidget(self.tab_advanced)
        self.listWidget_adv1.setObjectName(_fromUtf8("listWidget_adv1"))
        self.verticalLayout_2.addWidget(self.listWidget_adv1)
        self.send_button = QtGui.QPushButton(self.tab_advanced)
        self.send_button.setObjectName(_fromUtf8("send_button"))
        self.verticalLayout_2.addWidget(self.send_button)
        self.tabWidget_bas.addTab(self.tab_advanced, _fromUtf8(""))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.tabWidget_bas)
        Client.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Client)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 840, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuPreferences = QtGui.QMenu(self.menubar)
        self.menuPreferences.setObjectName(_fromUtf8("menuPreferences"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        Client.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Client)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Client.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(Client)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionOpen = QtGui.QAction(Client)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuPreferences.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Client)
        self.tabWidget_bas.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("triggered()")), Client.close)
        QtCore.QMetaObject.connectSlotsByName(Client)

    def retranslateUi(self, Client):
        Client.setWindowTitle(_translate("Client", "Client", None))
        self.form_label.setText(_translate("Client", "FORM", None))
        self.tabWidget_bas.setTabText(self.tabWidget_bas.indexOf(self.tab_basic), _translate("Client", "Basic", None))
        self.label_2.setText(_translate("Client", "FORM", None))
        self.send_button.setText(_translate("Client", "SEND", None))
        self.tabWidget_bas.setTabText(self.tabWidget_bas.indexOf(self.tab_advanced), _translate("Client", "Advanced", None))
        self.menuFile.setTitle(_translate("Client", "File", None))
        self.menuPreferences.setTitle(_translate("Client", "Preferences", None))
        self.menuHelp.setTitle(_translate("Client", "Help", None))
        self.actionQuit.setText(_translate("Client", "Quit", None))
        self.actionOpen.setText(_translate("Client", "Open", None))

