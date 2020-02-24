
from PyQt5 import QtCore, QtGui, QtWidgets
from PIL.ImageQt import ImageQt
from qtpy.QtCore import Signal
import requests

from error import *
from chatBox import *


#initial page to display QR and enter username
class Ui_MainWindow(object):
    def checkSize(self):      
        if len(self.usernameText.text()) >= 3 and not self.submitted:
            self.submit.setEnabled(True)
            
        else:
            self.submit.setEnabled(False)

    def init(self, MainWindow):
        self.MainWindow = MainWindow
        self.submitted = False
        self.refreshButton.clicked.connect(self.onClickRefresh)
        self.submit.clicked.connect(self.submitForm)
        self.submit.setEnabled(False)
        self.usernameText.textEdited.connect(self.checkSize)
        self.sessionID = self.generateSessionID()
        self.link = f'https://www.clawpro.club/api/connect?user={self.sessionID}'
        self.qrcode = self.generateQRCode()
        self.showQR()
        self.textSize = 0

    def generateSessionID(self):
        from datetime import datetime
        return str(hex(hash(datetime.now().timestamp())))

    def generateQRCode(self):
        import qrcode
        img = qrcode.make(self.link)
        img = img.resize((400,400))
        return ImageQt(img)

    def showQR(self):
        img = QtGui.QPixmap.fromImage(self.qrcode)
        scene = QtWidgets.QGraphicsScene()
        scene.addPixmap(img)
        self.QRDisplay.setScene(scene)
        print(scene)

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(681, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        self.MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumHeight(MainWindow.height())
        MainWindow.setMaximumWidth(MainWindow.width())
        MainWindow.setMinimumHeight(MainWindow.height())
        MainWindow.setMinimumWidth(MainWindow.width())
        self.QRGenerator = QtWidgets.QWidget(MainWindow)
        self.QRGenerator.setObjectName("QRGenerator")
        self.QRDisplay = QtWidgets.QGraphicsView(self.QRGenerator)
        self.QRDisplay.setGeometry(QtCore.QRect(150, 70, 400, 400))
        self.QRDisplay.setObjectName("QRDisplay")
        self.refreshButton = QtWidgets.QPushButton(self.QRGenerator)
        self.refreshButton.setGeometry(QtCore.QRect(310, 490, 80, 23))
        self.refreshButton.setObjectName("refreshButton")
        self.usernameText = QtWidgets.QLineEdit(self.QRGenerator)
        self.usernameText.setGeometry(QtCore.QRect(240, 30, 311, 23))
        self.usernameText.setObjectName("usernameText")
        
        
        self.label = QtWidgets.QLabel(self.QRGenerator)
        self.label.setGeometry(QtCore.QRect(90, 32, 91, 20))
        self.label.setObjectName("label")
        self.submit = QtWidgets.QPushButton(self.QRGenerator)
        self.submit.setGeometry(QtCore.QRect(310, 530, 80, 23))
        self.submit.setObjectName("submit")
        
        self.MainWindow.setCentralWidget(self.QRGenerator)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.label.adjustSize()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.init(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "AskEye"))
        self.refreshButton.setText(_translate("MainWindow", "Refresh"))
        self.label.setText(_translate("MainWindow", "Username (>3 char): "))
        self.submit.setText(_translate("MainWindow", "Submit"))

    def refresh(self):
        
        self.sessionID = self.generateSessionID()
        self.submitted = False
        self.link = f'https://www.clawpro.club/api/connect?user={self.sessionID}'
        self.qrcode = self.generateQRCode()

    def onClickRefresh(self):
        print('Refresh clicked')
        self.refresh()
        self.showQR()
        print('New session ID is : ', self.sessionID)
        print('New session Link is : ', self.link)

    def submitForm(self):
        self.username = self.usernameText.text()        
        json = {'hash':self.sessionID}
        
        try:
            req = requests.post(url = 'https://www.clawpro.club/api/start', data=json)
            res = req.json()
            print(res)
            if self.submitted:
                self.submit.setEnabled(False)
            else:
                self.submitted = True
            print(self.submitted)

            ui = Chat_MainWindow()
            
            self.MainWindow = QtWidgets.QMainWindow()
            ui.setupUi(self.MainWindow)
            self.MainWindow.show()
        except requests.exceptions.RequestException as e:
            ui = Ui_Error()
            self.MainWindow = QtWidgets.QMainWindow()
            ui.setupUi(self.MainWindow)
            ui.setErrorLabel(f"Problem occured.\nRequestError : Check your Internet.")
            self.MainWindow.show()
        except Exception as e:
            print(e)
            ui = Ui_Error()
            self.MainWindow = QtWidgets.QMainWindow()
            ui.setupUi(self.MainWindow)
            ui.setErrorLabel(f"Problem occured.\n{e}")
            self.MainWindow.show()
        self.submit.setEnabled(False)
