# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatBox.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Chat_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(593, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumHeight(MainWindow.height())
        MainWindow.setMaximumWidth(MainWindow.width())
        MainWindow.setMinimumHeight(MainWindow.height())
        MainWindow.setMinimumWidth(MainWindow.width())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sendMessage = QtWidgets.QPushButton(self.centralwidget)
        self.sendMessage.setGeometry(QtCore.QRect(440, 520, 111, 23))
        self.sendMessage.setObjectName("sendMessage")
        self.inputChat = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inputChat.setGeometry(QtCore.QRect(30, 460, 381, 81))
        self.inputChat.setObjectName("inputChat")
        self.chatWindow = QtWidgets.QTextBrowser(self.centralwidget)
        self.chatWindow.setGeometry(QtCore.QRect(30, 30, 381, 401))
        self.chatWindow.setObjectName("chatWindow")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AskEye Chat"))
        self.sendMessage.setText(_translate("MainWindow", "Send Message"))
