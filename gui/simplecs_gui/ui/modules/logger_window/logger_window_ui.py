# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logger_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoggerWindow(object):
    def setupUi(self, LoggerWindow):
        LoggerWindow.setObjectName("LoggerWindow")
        LoggerWindow.resize(975, 464)
        self.verticalLayout = QtWidgets.QVBoxLayout(LoggerWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(LoggerWindow)
        self.textEdit.setUndoRedoEnabled(False)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)

        self.retranslateUi(LoggerWindow)
        QtCore.QMetaObject.connectSlotsByName(LoggerWindow)

    def retranslateUi(self, LoggerWindow):
        _translate = QtCore.QCoreApplication.translate
        LoggerWindow.setWindowTitle(_translate("LoggerWindow", "Form"))