# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'klienttest.ui'
#
# Created: Tue Mar 26 11:23:57 2013
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
    _encoding = QtGui.QApplication.UnicodeUTF
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
        self.formBas = QtGui.QFormLayout()
        self.formBas.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.formBas.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formBas.setRowWrapPolicy(QtGui.QFormLayout.WrapLongRows)
        self.formBas.setSpacing(6)
        self.formBas.setObjectName(_fromUtf8("formBas"))
        self.verticalLayout.addLayout(self.formBas)
        self.tabWidget_bas.addTab(self.tab_basic, _fromUtf8(""))
        self.tab_advanced = QtGui.QWidget()
        self.tab_advanced.setObjectName(_fromUtf8("tab_advanced"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_advanced)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.formAdv = QtGui.QFormLayout()
        self.formAdv.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.formAdv.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formAdv.setRowWrapPolicy(QtGui.QFormLayout.WrapLongRows)
        self.formAdv.setObjectName(_fromUtf8("formAdv"))
        self.verticalLayout_2.addLayout(self.formAdv)
        self.tabWidget_bas.addTab(self.tab_advanced, _fromUtf8(""))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.tabWidget_bas)
        self.send_button = QtGui.QPushButton(self.centralwidget)
        self.send_button.setObjectName(_fromUtf8("send_button"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.SpanningRole, self.send_button)
        Client.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Client)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 840, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuPreferences = QtGui.QMenu(self.menubar)
        self.menuPreferences.setObjectName(_fromUtf8("menuPreferences"))
        self.menuConnection = QtGui.QMenu(self.menuPreferences)
        self.menuConnection.setObjectName(_fromUtf8("menuConnection"))
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
        self.actionConnect = QtGui.QAction(Client)
        self.actionConnect.setObjectName(_fromUtf8("actionConnect"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionQuit)
        self.menuConnection.addAction(self.actionConnect)
        self.menuPreferences.addAction(self.menuConnection.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuPreferences.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        
        self.retranslateUi(Client)
        self.tabWidget_bas.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("triggered()")), Client.close)
        QtCore.QMetaObject.connectSlotsByName(Client)
        
    def retranslateUi(self, Client):
        Client.setWindowTitle(_translate("Client", "Client", None))
        self.tabWidget_bas.setTabText(self.tabWidget_bas.indexOf(self.tab_basic), _translate("Client", "Basic", None))
        self.tabWidget_bas.setTabText(self.tabWidget_bas.indexOf(self.tab_advanced), _translate("Client", "Advanced", None))
        self.send_button.setText(_translate("Client", "SEND", None))
        self.menuFile.setTitle(_translate("Client", "File", None))
        self.menuPreferences.setTitle(_translate("Client", "Preferences", None))
        self.menuConnection.setTitle(_translate("Client", "Connection", None))
        self.menuHelp.setTitle(_translate("Client", "Help", None))
        self.actionQuit.setText(_translate("Client", "Quit", None))
        self.actionOpen.setText(_translate("Client", "Open", None))
        self.actionConnect.setText(_translate("Client", "Connect", None))
