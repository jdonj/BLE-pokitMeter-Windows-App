# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\Admin\Python\Workspace\Git_projects\python-projects\graphical_user_interface\pokitmeter\gui_files\connecting_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Connecting(object):
    def setupUi(self, Connecting):
        Connecting.setObjectName("Connecting")
        Connecting.setWindowModality(QtCore.Qt.ApplicationModal)
        Connecting.resize(211, 92)
        Connecting.setMinimumSize(QtCore.QSize(211, 92))
        Connecting.setMaximumSize(QtCore.QSize(211, 92))
        self.label_background_scan_devices_4 = QtWidgets.QLabel(Connecting)
        self.label_background_scan_devices_4.setGeometry(QtCore.QRect(0, 0, 211, 91))
        self.label_background_scan_devices_4.setMinimumSize(QtCore.QSize(211, 91))
        self.label_background_scan_devices_4.setMaximumSize(QtCore.QSize(211, 91))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_background_scan_devices_4.setFont(font)
        self.label_background_scan_devices_4.setStyleSheet("background-color: rgb(143, 170, 220);\n"
"border-radius: 13px;\n"
"border-style: solid;\n"
"border-color: rgb(116, 139, 179);\n"
"border-width: 1px;")
        self.label_background_scan_devices_4.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_background_scan_devices_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_background_scan_devices_4.setLineWidth(1)
        self.label_background_scan_devices_4.setText("")
        self.label_background_scan_devices_4.setObjectName("label_background_scan_devices_4")
        self.label_volt_range_7 = QtWidgets.QLabel(Connecting)
        self.label_volt_range_7.setGeometry(QtCore.QRect(50, 37, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_volt_range_7.setFont(font)
        self.label_volt_range_7.setStyleSheet("QLabel\n"
" {\n"
" font: 63 14pt \"Segoe UI Semibold\";\n"
" color : rgb(47, 85, 151);\n"
" }")
        self.label_volt_range_7.setObjectName("label_volt_range_7")
        self.pokit_logo_3 = QtWidgets.QLabel(Connecting)
        self.pokit_logo_3.setEnabled(False)
        self.pokit_logo_3.setGeometry(QtCore.QRect(9, 9, 37, 33))
        self.pokit_logo_3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pokit_logo_3.setStyleSheet("border-image: url(:/images/pokit_logo.png);")
        self.pokit_logo_3.setText("")
        self.pokit_logo_3.setScaledContents(True)
        self.pokit_logo_3.setObjectName("pokit_logo_3")

        self.retranslateUi(Connecting)
        QtCore.QMetaObject.connectSlotsByName(Connecting)

    def retranslateUi(self, Connecting):
        _translate = QtCore.QCoreApplication.translate
        Connecting.setWindowTitle(_translate("Connecting", "Dialog"))
        self.label_volt_range_7.setText(_translate("Connecting", "Connecting..."))

import ui_resource_rc
