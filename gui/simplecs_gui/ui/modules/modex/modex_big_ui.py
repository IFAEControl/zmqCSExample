# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modex_big.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ModuleExampleBig(object):
    def setupUi(self, ModuleExampleBig):
        ModuleExampleBig.setObjectName("ModuleExampleBig")
        ModuleExampleBig.resize(1160, 622)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(ModuleExampleBig)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label = QtWidgets.QLabel(ModuleExampleBig)
        self.label.setObjectName("label")
        self.verticalLayout_8.addWidget(self.label)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(ModuleExampleBig)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.ledit_echo_cmd = QtWidgets.QLineEdit(ModuleExampleBig)
        self.ledit_echo_cmd.setText("")
        self.ledit_echo_cmd.setObjectName("ledit_echo_cmd")
        self.horizontalLayout.addWidget(self.ledit_echo_cmd)
        self.pb_echo = QtWidgets.QPushButton(ModuleExampleBig)
        self.pb_echo.setObjectName("pb_echo")
        self.horizontalLayout.addWidget(self.pb_echo)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.line_2 = QtWidgets.QFrame(ModuleExampleBig)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_4.addWidget(self.line_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(ModuleExampleBig)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.lbl_echo_recvd = QtWidgets.QLabel(ModuleExampleBig)
        self.lbl_echo_recvd.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lbl_echo_recvd.setFont(font)
        self.lbl_echo_recvd.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_echo_recvd.setObjectName("lbl_echo_recvd")
        self.horizontalLayout_3.addWidget(self.lbl_echo_recvd)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.lbl_echo_recvd_on = QtWidgets.QLabel(ModuleExampleBig)
        self.lbl_echo_recvd_on.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_echo_recvd_on.setObjectName("lbl_echo_recvd_on")
        self.verticalLayout.addWidget(self.lbl_echo_recvd_on)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_9 = QtWidgets.QLabel(ModuleExampleBig)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_11.addWidget(self.label_9)
        self.ledit_max_rnd = QtWidgets.QLineEdit(ModuleExampleBig)
        self.ledit_max_rnd.setText("")
        self.ledit_max_rnd.setObjectName("ledit_max_rnd")
        self.horizontalLayout_11.addWidget(self.ledit_max_rnd)
        self.pb_set_max_rnd = QtWidgets.QPushButton(ModuleExampleBig)
        self.pb_set_max_rnd.setObjectName("pb_set_max_rnd")
        self.horizontalLayout_11.addWidget(self.pb_set_max_rnd)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem3)
        self.horizontalLayout_10.addLayout(self.verticalLayout_5)
        self.line_6 = QtWidgets.QFrame(ModuleExampleBig)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_10.addWidget(self.line_6)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_10 = QtWidgets.QLabel(ModuleExampleBig)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_12.addWidget(self.label_10)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem4)
        self.lbl_set_max_rnd_recvd = QtWidgets.QLabel(ModuleExampleBig)
        self.lbl_set_max_rnd_recvd.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lbl_set_max_rnd_recvd.setFont(font)
        self.lbl_set_max_rnd_recvd.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_set_max_rnd_recvd.setObjectName("lbl_set_max_rnd_recvd")
        self.horizontalLayout_12.addWidget(self.lbl_set_max_rnd_recvd)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        self.lbl_set_max_rnd_recvd_on = QtWidgets.QLabel(ModuleExampleBig)
        self.lbl_set_max_rnd_recvd_on.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_set_max_rnd_recvd_on.setObjectName("lbl_set_max_rnd_recvd_on")
        self.verticalLayout_6.addWidget(self.lbl_set_max_rnd_recvd_on)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_6.addItem(spacerItem5)
        self.horizontalLayout_10.addLayout(self.verticalLayout_6)
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        self.verticalLayout_11.addLayout(self.verticalLayout_8)
        self.line = QtWidgets.QFrame(ModuleExampleBig)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_11.addWidget(self.line)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_7 = QtWidgets.QLabel(ModuleExampleBig)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_9.addWidget(self.label_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_3 = QtWidgets.QLabel(ModuleExampleBig)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.lbl_last_random = QtWidgets.QLabel(ModuleExampleBig)
        self.lbl_last_random.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.lbl_last_random.setFont(font)
        self.lbl_last_random.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_last_random.setObjectName("lbl_last_random")
        self.horizontalLayout_7.addWidget(self.lbl_last_random)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem7)
        self.horizontalLayout_8.addLayout(self.verticalLayout_4)
        self.line_3 = QtWidgets.QFrame(ModuleExampleBig)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_8.addWidget(self.line_3)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(ModuleExampleBig)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.lbl_avg_minute = QtWidgets.QLabel(ModuleExampleBig)
        self.lbl_avg_minute.setText("")
        self.lbl_avg_minute.setObjectName("lbl_avg_minute")
        self.horizontalLayout_2.addWidget(self.lbl_avg_minute)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(ModuleExampleBig)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.lbl_events_minute = QtWidgets.QLabel(ModuleExampleBig)
        self.lbl_events_minute.setText("")
        self.lbl_events_minute.setObjectName("lbl_events_minute")
        self.horizontalLayout_5.addWidget(self.lbl_events_minute)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout_7.addLayout(self.verticalLayout_3)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_7.addItem(spacerItem10)
        self.horizontalLayout_8.addLayout(self.verticalLayout_7)
        self.verticalLayout_9.addLayout(self.horizontalLayout_8)
        self.verticalLayout_11.addLayout(self.verticalLayout_9)
        self.line_4 = QtWidgets.QFrame(ModuleExampleBig)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_11.addWidget(self.line_4)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_8 = QtWidgets.QLabel(ModuleExampleBig)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_10.addWidget(self.label_8)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.chart = PlotWidget(ModuleExampleBig)
        self.chart.setObjectName("chart")
        self.horizontalLayout_6.addWidget(self.chart)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_6.addItem(spacerItem11)
        self.verticalLayout_10.addLayout(self.horizontalLayout_6)
        self.verticalLayout_11.addLayout(self.verticalLayout_10)

        self.retranslateUi(ModuleExampleBig)
        QtCore.QMetaObject.connectSlotsByName(ModuleExampleBig)

    def retranslateUi(self, ModuleExampleBig):
        _translate = QtCore.QCoreApplication.translate
        ModuleExampleBig.setWindowTitle(_translate("ModuleExampleBig", "Example"))
        self.label.setText(_translate("ModuleExampleBig", "Command example call"))
        self.label_2.setText(_translate("ModuleExampleBig", "Echo command"))
        self.pb_echo.setText(_translate("ModuleExampleBig", "Execute"))
        self.label_5.setText(_translate("ModuleExampleBig", "Received:"))
        self.lbl_echo_recvd.setText(_translate("ModuleExampleBig", "-"))
        self.lbl_echo_recvd_on.setText(_translate("ModuleExampleBig", "on -"))
        self.label_9.setText(_translate("ModuleExampleBig", "Set max random"))
        self.pb_set_max_rnd.setText(_translate("ModuleExampleBig", "Execute"))
        self.label_10.setText(_translate("ModuleExampleBig", "Received:"))
        self.lbl_set_max_rnd_recvd.setText(_translate("ModuleExampleBig", "-"))
        self.lbl_set_max_rnd_recvd_on.setText(_translate("ModuleExampleBig", "on -"))
        self.label_7.setText(_translate("ModuleExampleBig", "Asyncs example"))
        self.label_3.setText(_translate("ModuleExampleBig", "Last random received"))
        self.lbl_last_random.setText(_translate("ModuleExampleBig", "0.0"))
        self.label_4.setText(_translate("ModuleExampleBig", "Average last minute"))
        self.label_6.setText(_translate("ModuleExampleBig", "Events last minute"))
        self.label_8.setText(_translate("ModuleExampleBig", "Async chart example"))
from pyqtgraph import PlotWidget
