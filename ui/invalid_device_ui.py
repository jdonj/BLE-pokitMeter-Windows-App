# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\Admin\Python\Workspace\Git_projects\python-projects\graphical_user_interface\pokitmeter\gui_files\invalid_dev_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(222, 114)
        Dialog.setMinimumSize(QtCore.QSize(222, 114))
        Dialog.setMaximumSize(QtCore.QSize(222, 114))
        self.label_background_scan_devices_2 = QtWidgets.QLabel(Dialog)
        self.label_background_scan_devices_2.setGeometry(QtCore.QRect(0, 0, 221, 114))
        self.label_background_scan_devices_2.setMinimumSize(QtCore.QSize(221, 114))
        self.label_background_scan_devices_2.setMaximumSize(QtCore.QSize(221, 114))
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
        self.label_volt_range_6.setGeometry(QtCore.QRect(50, 40, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_volt_range_6.setFont(font)
        self.label_volt_range_6.setStyleSheet("QLabel\n"
" {\n"
" font: 63 14pt \"Segoe UI Semibold\";\n"
" color : rgb(47, 85, 151);\n"
" }")
        self.label_volt_range_6.setObjectName("label_volt_range_6")
        self.pushButton_rescan = QtWidgets.QPushButton(Dialog)
        self.pushButton_rescan.setGeometry(QtCore.QRect(15, 74, 95, 34))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton_rescan.setFont(font)
        self.pushButton_rescan.setStyleSheet("QPushButton\n"
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
        self.pushButton_rescan.setFlat(False)
        self.pushButton_rescan.setObjectName("pushButton_rescan")
        self.pushButton_exit = QtWidgets.QPushButton(Dialog)
        self.pushButton_exit.setGeometry(QtCore.QRect(119, 74, 86, 34))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton_exit.setStyleSheet("QPushButton\n"
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
        self.pushButton_exit.setFlat(False)
        self.pushButton_exit.setObjectName("pushButton_exit")
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
        self.label_volt_range_6.setText(_translate("Dialog", "Invalid device!"))
        self.pushButton_rescan.setText(_translate("Dialog", "Scan again"))
        self.pushButton_exit.setText(_translate("Dialog", "Exit"))

import ui_resource_rc
