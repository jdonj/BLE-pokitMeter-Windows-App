# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\Admin\Python\Workspace\Git_projects\python-projects\graphical_user_interface\pokitmeter\gui_files\scan_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(340, 382)
        Dialog.setMinimumSize(QtCore.QSize(340, 382))
        Dialog.setMaximumSize(QtCore.QSize(340, 382))
        Dialog.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_background_scan_devices = QtWidgets.QLabel(Dialog)
        self.label_background_scan_devices.setGeometry(QtCore.QRect(0, 0, 340, 381))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_background_scan_devices.setFont(font)
        self.label_background_scan_devices.setStyleSheet("background-color: rgb(47, 85, 151);\n"
"border-radius: 13px;\n"
"border-style: solid;\n"
"border-color: rgb(33, 61, 108);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_background_scan_devices.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_background_scan_devices.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_background_scan_devices.setLineWidth(1)
        self.label_background_scan_devices.setText("")
        self.label_background_scan_devices.setObjectName("label_background_scan_devices")
        self.listWidget_devices = QtWidgets.QListWidget(Dialog)
        self.listWidget_devices.setGeometry(QtCore.QRect(34, 62, 287, 261))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.listWidget_devices.setFont(font)
        self.listWidget_devices.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.listWidget_devices.setStyleSheet("background-color: rgb(143, 170, 220);\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"")
        self.listWidget_devices.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listWidget_devices.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget_devices.setObjectName("listWidget_devices")
        self.label_volt_range_5 = QtWidgets.QLabel(Dialog)
        self.label_volt_range_5.setGeometry(QtCore.QRect(73, 18, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_volt_range_5.setFont(font)
        self.label_volt_range_5.setStyleSheet("QLabel\n"
" {\n"
" font: 63 12pt \"Segoe UI Semibold\";\n"
" color : rgb(143, 170, 220);\n"
" }")
        self.label_volt_range_5.setObjectName("label_volt_range_5")
        self.pokit_logo_2 = QtWidgets.QLabel(Dialog)
        self.pokit_logo_2.setEnabled(False)
        self.pokit_logo_2.setGeometry(QtCore.QRect(18, 12, 33, 29))
        self.pokit_logo_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pokit_logo_2.setStyleSheet("border-image: url(:/images/pokit_logo.png);")
        self.pokit_logo_2.setText("")
        self.pokit_logo_2.setScaledContents(True)
        self.pokit_logo_2.setObjectName("pokit_logo_2")
        self.label_background_scan_devices_3 = QtWidgets.QLabel(Dialog)
        self.label_background_scan_devices_3.setGeometry(QtCore.QRect(20, 52, 301, 318))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_background_scan_devices_3.setFont(font)
        self.label_background_scan_devices_3.setStyleSheet("background-color: rgb(143, 170, 220);\n"
"border-width: 5px;\n"
"border-radius: 6px;\n"
"padding: 6px;")
        self.label_background_scan_devices_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_background_scan_devices_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_background_scan_devices_3.setLineWidth(1)
        self.label_background_scan_devices_3.setText("")
        self.label_background_scan_devices_3.setObjectName("label_background_scan_devices_3")
        self.pushButton_rescan = QtWidgets.QPushButton(Dialog)
        self.pushButton_rescan.setGeometry(QtCore.QRect(120, 331, 103, 36))
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
        self.label_background_scan_devices.raise_()
        self.label_background_scan_devices_3.raise_()
        self.listWidget_devices.raise_()
        self.label_volt_range_5.raise_()
        self.pokit_logo_2.raise_()
        self.pushButton_rescan.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_volt_range_5.setText(_translate("Dialog", "Devices Found"))
        self.pushButton_rescan.setText(_translate("Dialog", "Scan again"))

import ui_resource_rc
