
from qr import *
#initial page to display QR and enter username
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == "__main__":
    import sys
    import socketio
    sio = socketio.AsyncClient()
    app = QtWidgets.QApplication(sys.argv)
    global MainWindow
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    print('%s'%'abc')
    #app loop
    sys.exit(app.exec_())
