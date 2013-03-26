import sys, boxconnection
from PyQt4 import QtCore, QtGui
from klienttest_ui import Ui_Client

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent = None):
    QtGui.QWidget.__init__(self, parent)
    self.ui = Ui_Client()
    self.ui.setupUi(self)
    # dictionaries
    self.dictbuttons_tmp = {} # temporary dict of buttons - when I get some idea how to do it other way I'll remove this!
    self.dictanswers_tmp = {} # same as above (DEATH FROM ABOVE!)
    # Connection widget
    self.boxCon = boxconnection.BoxConnection()
    # slots connections
    QtCore.QObject.connect(self.ui.actionOpen,QtCore.SIGNAL("triggered()"), self.file_form_dialog)
    QtCore.QObject.connect(self.ui.actionConnect,QtCore.SIGNAL("triggered()"), self.connect_opt)
    QtCore.QObject.connect(self.ui.send_button,QtCore.SIGNAL("clicked()"), self.save_to_file)
        
    #def write_to_alist(self, item):
        #self.dictanswers_tmp.append(str(item.text()))
            
    # establishes connection with server
    def connect_opt(self):
        #import subprocess
        #subprocess.call([sys.executable, './boxconnection.py'])
        self.boxCon.show()
        #wait()
            
    # clears dictionaries        
    def clear_dictionaries(self):
        self.dictbuttons_tmp = {}
        self.dictanswers_tmp = {}
            
    # saves texts to config file
    def save_to_file(self):
        save_file = open("test.config", "a")
        for x in self.dictbuttons_tmp.keys(): # change status of the button and write its text to the file
            if self.dictbuttons_tmp[x].currentText() != "Choose one option":
                save_file.write("[" + x + "]" + "\n") # save section
                if self.dictbuttons_tmp[x].currentText() == 'Yes': # changes the answer to bool form
                    save_file.write("answer = " + 'True' + "\n") # save contents
                elif self.dictbuttons_tmp[x].currentText() == 'No': # changes the answer to bool form
                    save_file.write("answer = " + 'False' + "\n") # save contents
        for x in self.dictanswers_tmp.keys():# write to file from LINE EDITS (they are on listWidget)
            if str(self.dictanswers_tmp[x].text()) != "": # temporary
                save_file.write("[" + x + "]" + "\n") # save section
                save_file.write("answer = " + str(self.dictanswers_tmp[x].text()) + "\n") # save contents
        self.clear_dictionaries()
        save_file.close()
        self.ui.textBrowser_test.append("Wysylam")
            
    # creates widgets    
    def widgets_funct(self, i, form_lay, cfg): # i - sections from cfg, listw listWidgetItem, cfg - config file
        for y in cfg.options(i):
            if y == 'question':
                if 'type' in cfg.options(i): # if there is a type option that contains bool in cfg file
                    #pass
                    if 'bool' in cfg.get(i, 'type'):
                        txt = cfg.get(i, y) # question
                        comboBox = QtGui.QComboBox(self) #QComboBox
                        comboBox.addItem("Choose one option")
                        comboBox.addItem('No')
                        comboBox.addItem('Yes')
                        _label = QtGui.QLabel(txt, self) # QLabel
                        #_label.setStyleSheet("qproperty-wordWrap: true;") # setting text wrap
                        #_label.adjustSize()
                        form_lay.addRow(_label, comboBox) # adding row in LayoutForm
                        #    label_i = QtGui.QListWidgetItem() # creates label that contains question
                        #    answer = QtGui.QListWidgetItem() # an item that can be replaced by a combobox (by default - line edit)
                        #    comboBox = QtGui.QComboBox(self) # QComboBox
                        #    comboBox.addItem("Choose one option")
                        #    comboBox.addItem('No')
                        #    comboBox.addItem('Yes')
                        #    _label = QtGui.QLabel(txt, self) #QLabel
                        #    _label.setStyleSheet("qproperty-wordWrap: true;") # setting text wrap
                        #    listw1.addItem(label_i) 
                        #    listw1.addItem(answer)
                        #    listw1.setItemWidget(answer, comboBox) # replacing QListWidgetItem with combobox
                        #    listw1.setItemWidget(label_i, _label) # replacing QListWidgetItem with Qlabel
                        self.dictbuttons_tmp[i] = comboBox # if bool put combobox
                    elif 'string' in cfg.get(i, 'type'):
                        txt = cfg.get(i, y) # question
                        lineEdit = QtGui.QLineEdit(self) # QLineEdit
                        _label = QtGui.QLabel(txt, self) # QLabel
                        #_label.setStyleSheet("qproperty-wordWrap: true;") # setting text wrap
                        #_label.adjustSize()
                        form_lay.addRow(_label, lineEdit) # adding row in LayoutForm
                        #    txt = cfg.get(i, y) # question
                        #    label_i = QtGui.QListWidgetItem() # creates label that contains question
                        #    answer = QtGui.QListWidgetItem() # an item that can be replaced by a lineedit (by default - line edit)
                        #answer.setFlags(answer.flags() | QtCore.Qt.ItemIsEditable) # setting answer to editable
                        #    lineEdit = QtGui.QLineEdit(self) # QLineEdit
                        #    lineEdit.setStyleSheet("border: 2px solid gray;" # setting lineedit's style
                        #                           "border-radius: 5px;")
                        #    _label = QtGui.QLabel(txt, self) # QLabel
                        #    _label.setStyleSheet("qproperty-wordWrap: true;") # setting text wrap
                        #    listw.addItem(label_i)
                        #    listw.addItem(answer)
                        #    listw.setItemWidget(answer, lineEdit)
                        #    listw.setItemWidget(label_i, _label) # replacing QListWidgetItem with Qlabel
                        self.dictanswers_tmp[i] = lineEdit # if not bool put LINE EDIT
                    #else:
                    #     label_i = QtGui.QListWidgetItem(cfg.get(i, y)) # creates label that contains question
                    #     answer = QtGui.QListWidgetItem() # an item that can be replaced by a combobox (by default - line edit)
                    #     textbox = QtGui.QTextEdit(self)
                    #     textbox.setWordWrapMode(QtGui.QTextOption.NoWrap)
                    #     textbox.setVerticalScrollBarPolicy(not textbox.verticalScrollBarPolicy())
                    #     textbox.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
                    #     listw1.addItem(label_i)
                    #     listw1.addItem(answer)
                    #     listw1.setItemWidget(answer, textbox)
                    
    # opens the file and creates a form    
    def file_form_dialog(self):
        fd = QtGui.QFileDialog(self) # opens a file window
        self.filename = fd.getOpenFileName() # getting a filename from chosen file
            
        from os.path import isfile, split
        import ConfigParser
            
        config = ConfigParser.ConfigParser()
            
        if isfile(self.filename):
            head, tail = split(str(self.filename)) # tail - a filename without path
            config.read(tail)
                
            for x in config.sections():
                # basic operations
                if x[0] == 'b':
                    self.widgets_funct(x, self.ui.formBas, config)
                        
                # advanced operations
                elif x[0] == 'a':
                    self.widgets_funct(x, self.ui.formAdv, config)
                        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    try:
        sys.exit(app.exec_())
    except:
        print "Zamkniecie aplikacji."
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
