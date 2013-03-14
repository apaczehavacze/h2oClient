from PyQt4 import  QtGui
import gui

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = gui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.listModule.insertItem(0, 'pierwszy zajebisty modul')
    ui.listModule.insertItem(0, 'drugi zajebisty modul')
    MainWindow.show()
    sys.exit(app.exec_())