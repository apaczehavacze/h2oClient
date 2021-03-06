import sys
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
        # slots connections
        QtCore.QObject.connect(self.ui.actionOpen,QtCore.SIGNAL("triggered()"), self.file_form_dialog)
        #QtCore.QObject.connect(self.ui.listWidget_bas,QtCore.SIGNAL("itemChanged(QListWidgetItem *)"), self.write_to_alist)
        #QtCore.QObject.connect(self.ui.listWidget_adv,QtCore.SIGNAL("itemChanged(QListWidgetItem *)"), self.write_to_alist)
        QtCore.QObject.connect(self.ui.send_button,QtCore.SIGNAL("clicked()"), self.save_to_file)

    #def write_to_alist(self, item):
        #self.dictanswers_tmp.append(str(item.text()))

    # clears dictionaries        
    def clear_dictionaries(self):
        self.dictbuttons_tmp = {}
        self.dictanswers_tmp = {}
        
    # saves texts to config file
    def save_to_file(self):
        save_file = open("test.config", "a")
        for x in self.dictbuttons_tmp.keys(): # change status of the button and write its text to the file
            #if self.dictbuttons_tmp[x].isEnabled():
            #    self.dictbuttons_tmp[x].setEnabled(False)
            if self.dictbuttons_tmp[x].currentText() != "Choose one option":
                save_file.write("[" + x + "]" + "\n") # save section
                if self.dictbuttons_tmp[x].currentText() == 'Yes': # changes the answer to bool form
                    save_file.write("answer = " + 'True' + "\n") # save contents
                elif self.dictbuttons_tmp[x].currentText() == 'No': # changes the answer to bool form
                    save_file.write("answer = " + 'False' + "\n") # save contents
        for x in self.dictanswers_tmp.keys():# write to file from LINE EDITS (they are on listWidget)
            if str(self.dictanswers_tmp[x].text()) != "ANSWER HERE": # temporary
                save_file.write("[" + x + "]" + "\n") # save section
                save_file.write("answer = " + str(self.dictanswers_tmp[x].text()) + "\n") # save contents
        self.clear_dictionaries()
        save_file.close()
        self.ui.textBrowser_test.append("Wysylam")

    # creates widgets    
    def widgets_funct(self, i, listw, listw1, cfg): # i - sections from cfg, listw listWidgetItem, cfg - config file
        for y in cfg.options(i):
            if y == 'question':
                if 'type' in cfg.options(i): # if there is a type option that contains bool in cfg file
                    if 'bool' in cfg.get(i, 'type'):
                        label_i = QtGui.QListWidgetItem(cfg.get(i, y)) # creates label that contains question
                        answer = QtGui.QListWidgetItem() # an item that can be replaced by a combobox (by default - line edit)
                        combobox = QtGui.QComboBox(self) # combobox
                        combobox.addItem("Choose one option")
                        combobox.addItem('No')
                        combobox.addItem('Yes')
                        listw1.addItem(label_i)
                        listw1.addItem(answer)
                        listw1.setItemWidget(answer, combobox) # replacing QListWidgetItem with combobox
                        self.dictbuttons_tmp[i] = combobox # if bool put combobox
                    else:
                        label_i = QtGui.QListWidgetItem(cfg.get(i, y)) # creates label that contains question
                        answer = QtGui.QListWidgetItem("ANSWER HERE") # an item that can be replaced by a combobox (by default - line edit)
                        answer.setFlags(answer.flags() | QtCore.Qt.ItemIsEditable) # setting answer to editable
                        listw.addItem(label_i)
                        listw.addItem(answer)
                        self.dictanswers_tmp[i] = answer # if not bool put LINE EDIT

    # opens the file and creates a form    
    def file_form_dialog(self): 
        fd = QtGui.QFileDialog(self) # opens a file window
        self.filename = fd.getOpenFileName() # getting a filename from chosen file

        from os.path import isfile, split

        req_version = (2,8)
        cur_version = sys.version_info
        
        if cur_version >= req_version:
            import configparser
            config = configparser.ConfigParser()
        else:
            import ConfigParser
            config = ConfigParser.ConfigParser()

        if isfile(self.filename):
            head, tail = split(str(self.filename)) # tail - a filename without path
            config.read(tail)

            for x in config.sections():
                # basic operations
                if x[0] == 'b':
                    self.widgets_funct(x, self.ui.listWidget_bas, self.ui.listWidget_bas1, config)
                                    
                # advanced operations
                elif x[0] == 'a':
                    self.widgets_funct(x, self.ui.listWidget_adv, self.ui.listWidget_adv1, config)
                
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    try:
        sys.exit(app.exec_())
    except:
        print('Zamkniecie aplikacji.')
