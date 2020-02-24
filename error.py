# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Error(object):

    def setErrorLabel(self,e):
        self.errorLabel.setText(e)
        self.errorLabel.adjustSize()

    def setupUi(self, Error):
        self.Error = Error
        self.Error.setObjectName("Error")
        self.Error.resize(400, 150)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Error.sizePolicy().hasHeightForWidth())
        Error.setSizePolicy(sizePolicy)
        Error.setMaximumWidth(Error.width())
        Error.setMaximumHeight(Error.height())
        Error.setMinimumWidth(Error.width())
        Error.setMinimumHeight(Error.height())
        self.Error.setSizePolicy(sizePolicy)
        self.okButton = QtWidgets.QPushButton(Error)
        self.okButton.setGeometry(QtCore.QRect(175, 90, 61, 23))
        self.okButton.setObjectName("okButton")
        self.okButton.clicked.connect(self.Error.close)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.okButton.sizePolicy().hasHeightForWidth())
        self.okButton.setSizePolicy(sizePolicy)
        self.errorLabel = QtWidgets.QLabel(Error)
        self.errorLabel.setGeometry(QtCore.QRect(50, 30, 211, 51))
        self.errorLabel.setText("")
        self.errorLabel.setObjectName("errorLabel")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.errorLabel.sizePolicy().hasHeightForWidth())
        self.errorLabel.setSizePolicy(sizePolicy)
        #self.Error.show()
        self.retranslateUi(Error)
        QtCore.QMetaObject.connectSlotsByName(Error)

    def retranslateUi(self, Error):
        _translate = QtCore.QCoreApplication.translate
        self.Error.setWindowTitle(_translate("Error", "Error"))
        self.okButton.setText(_translate("Error", "OK"))