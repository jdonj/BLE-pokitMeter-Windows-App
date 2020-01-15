# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\Admin\Python\Workspace\Git_projects\python-projects\graphical_user_interface\pokitmeter\gui_files\confirm_switch_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(271, 114)
        Dialog.setMinimumSize(QtCore.QSize(271, 114))
        Dialog.setMaximumSize(QtCore.QSize(271, 114))
        Dialog.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_background_scan_devices_2 = QtWidgets.QLabel(Dialog)
        self.label_background_scan_devices_2.setGeometry(QtCore.QRect(0, 0, 271, 114))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_background_scan_devices_2.setFont(font)
        self.label_background_scan_devices_2.setStyleSheet("background-color: rgb(143, 170, 220);\n"
"border-radius: 13px;\n"
"border-style: solid;\n"
"border-color: rgb(116, 139, 179);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_background_scan_devices_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_background_scan_devices_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_background_scan_devices_2.setLineWidth(1)
        self.label_background_scan_devices_2.setText("")
        self.label_background_scan_devices_2.setObjectName("label_background_scan_devices_2")
        self.label_volt_range_6 = QtWidgets.QLabel(Dialog)
        self.label_volt_range_6.setGeometry(QtCore.QRect(32, 43, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_volt_range_6.setFont(font)
        self.label_volt_range_6.setStyleSheet("QLabel\n"
" {\n"
" font: 63 12pt \"Segoe UI Semibold\";\n"
" color : rgb(47, 85, 151);\n"
" }")
        self.label_volt_range_6.setObjectName("label_volt_range_6")
        self.pushButton_switch = QtWidgets.QPushButton(Dialog)
        self.pushButton_switch.setGeometry(QtCore.QRect(46, 74, 95, 34))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton_switch.setFont(font)
        self.pushButton_switch.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(47, 85, 151);\n"
"border-style: solid;\n"
"font: 63 10pt \"Segoe UI Semibold\";\n"
"color : rgb(143, 170, 220);\n"
"border-width: 4px;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"background-color: rgb(47, 85, 151);\n"
"border-style: solid;\n"
"font: 63 11pt \"Segoe UI Semibold\";\n"
"color : rgb(0, 0, 0);\n"
"border-width: 0px;\n"
"border-radius: 8px;\n"
"}")
        self.pushButton_switch.setFlat(False)
        self.pushButton_switch.setObjectName("pushButton_switch")
        self.pushButton_cancel = QtWidgets.QPushButton(Dialog)
        self.pushButton_cancel.setGeometry(QtCore.QRect(150, 74, 86, 34))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton_cancel.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(47, 85, 151);\n"
"border-style: solid;\n"
"font: 63 10pt \"Segoe UI Semibold\";\n"
"color : rgb(143, 170, 220);\n"
"border-width: 4px;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"background-color: rgb(47, 85, 151);\n"
"border-style: solid;\n"
"font: 63 11pt \"Segoe UI Semibold\";\n"
"color : rgb(0, 0, 0);\n"
"border-width: 0px;\n"
"border-radius: 8px;\n"
"}\n"
"")
        self.pushButton_cancel.setFlat(False)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.pokit_logo_3 = QtWidgets.QLabel(Dialog)
        self.pokit_logo_3.setEnabled(False)
        self.pokit_logo_3.setGeometry(QtCore.QRect(9, 9, 33, 29))
        self.pokit_logo_3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pokit_logo_3.setStyleSheet("border-image: url(:/images/pokit_logo.png);")
        self.pokit_logo_3.setText("")
        self.pokit_logo_3.setScaledContents(True)
        self.pokit_logo_3.setObjectName("pokit_logo_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_volt_range_6.setText(_translate("Dialog", "Switch to AMMETER mode?"))
        self.pushButton_switch.setText(_translate("Dialog", "Switch"))
        self.pushButton_cancel.setText(_translate("Dialog", "Cancel"))

import ui_resource_rc
