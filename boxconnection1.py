import sys, socket, consuc, klient
from PyQt4 import QtCore, QtGui
from boxconnection_ui import Ui_boxConnection

class BoxConnection(QtGui.QGroupBox):
    def __init__(self, cui, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_boxConnection()
        self.ui.setupUi(self)
        # BoxConnection parameters
        self.hostname = ''
        self.portnumber = 0
        self.username = ''
        self.password = ''
        # connection successfull widget
        self.ConSucBox = consuc.ConSuc()
        # data from server
        self.data = ""
        # client ui (needed to modify its modules list)
        self.client_ui = cui
        # slots connections
        QtCore.QObject.connect(self.ui.pushButtonConnect,QtCore.SIGNAL("clicked()"), self.establish_connection)

    def establish_connection(self):
        # clear forms
        self.client_ui.clear_forms(self.client_ui.ui.formBas)
        self.client_ui.clear_forms(self.client_ui.ui.formAdv)  
        # clear modules list
        self.client_ui.ui.list_modules.clear()
        # clear data
        self.data = ""
        # save connection parameters
        self.hostname = self.ui.lineEditHostName.text()
        self.username = self.ui.lineEditUserName.text()
        self.password = self.ui.lineEditPassword.text()
        self.portnumber = self.ui.spinBoxPortNumber.value()
        # a message that is sent to the server
        message = " ".join([self.username, self.password])
        # socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # establish connection
        try:
            # connect to server and send data
            s.connect((self.hostname, self.portnumber))
        except ConnectionRefusedError:
            raise ConnectionRefusedError("There is no such a host")
        else:
            s.sendall(bytes(message, "utf-8"))

            # receive data from the server and shut down
            self.data = s.recv(1024)
            #if data: # TESTOWO - POZNIEJ WYWALIC
            #    self.ConSucBox.show() 
        finally:
            s.close()

        # putting modules on client module list
        tmp_txt = bytes.decode(self.data)
        tmp_txt = tmp_txt.split()
        for x in tmp_txt:
            label_i = QtGui.QListWidgetItem(x)
            self.client_ui.ui.list_modules.addItem(label_i)
        #print("Sent:     {}".format(message))
        #print("Received: {}".format(self.data))
        #self.ConSucBox.show()
     
        #self.client_ui.ui.list_modules.addItem(label_i)
        #self.close()
  

