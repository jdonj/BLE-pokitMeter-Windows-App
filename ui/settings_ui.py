# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\Admin\Python\Workspace\Git_projects\python-projects\graphical_user_interface\pokitmeter\gui_files\settings_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(273, 245)
        Dialog.setMinimumSize(QtCore.QSize(273, 245))
        Dialog.setMaximumSize(QtCore.QSize(273, 245))
        self.label_background_settings = QtWidgets.QLabel(Dialog)
        self.label_background_settings.setGeometry(QtCore.QRect(0, 0, 271, 245))
        self.label_background_settings.setMinimumSize(QtCore.QSize(271, 245))
        self.label_background_settings.setMaximumSize(QtCore.QSize(271, 245))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_background_settings.setFont(font)
        self.label_background_settings.setStyleSheet("background-color: rgb(47, 85, 151);\n"
"border-radius: 13px;\n"
"border-style: solid;\n"
"border-color: rgb(33, 61, 108);\n"
"border-width: 1px;")
        self.label_background_settings.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_background_settings.setText("")
        self.label_background_settings.setObjectName("label_background_settings")
        self.pushButton_ok = QtWidgets.QPushButton(Dialog)
        self.pushButton_ok.setGeometry(QtCore.QRect(106, 208, 75, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_ok.setFont(font)
        self.pushButton_ok.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(143, 170, 220);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"background-color: rgb(143, 170, 220);\n"
"border-style: solid;\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"font-weight: bold;\n"
"color : rgb(0, 0, 0);\n"
"border-width: 0px;\n"
"}")
        self.pushButton_ok.setFlat(False)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.comboBox_volt_range = QtWidgets.QComboBox(Dialog)
        self.comboBox_volt_range.setGeometry(QtCore.QRect(130, 40, 111, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_volt_range.setFont(font)
        self.comboBox_volt_range.setStyleSheet("background-color: rgb(143, 170, 220);\n"
"border-width: 5px;\n"
"border-radius: 6px;")
        self.comboBox_volt_range.setObjectName("comboBox_volt_range")
        self.comboBox_volt_range.addItem("")
        self.comboBox_volt_range.addItem("")
        self.comboBox_volt_range.addItem("")
        self.comboBox_volt_range.addItem("")
        self.comboBox_volt_range.addItem("")
        self.comboBox_volt_range.addItem("")
        self.comboBox_volt_range.addItem("")
        self.label_volt_range = QtWidgets.QLabel(Dialog)
        self.label_volt_range.setGeometry(QtCore.QRect(40, 40, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_volt_range.setFont(font)
        self.label_volt_range.setStyleSheet("QLabel\n"
" {\n"
" font: 63 12pt \"Segoe UI Semibold\";\n"
" color : rgb(143, 170, 220);\n"
" }")
        self.label_volt_range.setObjectName("label_volt_range")
        self.label_volt_range_2 = QtWidgets.QLabel(Dialog)
        self.label_volt_range_2.setGeometry(QtCore.QRect(40, 80, 91, 21))
        self.label_volt_range_2.setMaximumSize(QtCore.QSize(91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_volt_range_2.setFont(font)
        self.label_volt_range_2.setStyleSheet("QLabel\n"
" {\n"
" font: 63 12pt \"Segoe UI Semibold\";\n"
" color : rgb(143, 170, 220);\n"
" }")
        self.label_volt_range_2.setObjectName("label_volt_range_2")
        self.comboBox_amp_range = QtWidgets.QComboBox(Dialog)
        self.comboBox_amp_range.setGeometry(QtCore.QRect(130, 80, 111, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_amp_range.setFont(font)
        self.comboBox_amp_range.setStyleSheet("background-color: rgb(143, 170, 220);\n"
"border-width: 5px;\n"
"border-radius: 6px;")
        self.comboBox_amp_range.setObjectName("comboBox_amp_range")
        self.comboBox_amp_range.addItem("")
        self.comboBox_amp_range.addItem("")
        self.comboBox_amp_range.addItem("")
        self.comboBox_amp_range.addItem("")
        self.comboBox_amp_range.addItem("")
        self.comboBox_amp_range.addItem("")
        self.label_volt_range_3 = QtWidgets.QLabel(Dialog)
        self.label_volt_range_3.setGeometry(QtCore.QRect(40, 120, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_volt_range_3.setFont(font)
        self.label_volt_range_3.setStyleSheet("QLabel\n"
" {\n"
" font: 63 12pt \"Segoe UI Semibold\";\n"
" color : rgb(143, 170, 220);\n"
" }")
        self.label_volt_range_3.setObjectName("label_volt_range_3")
        self.comboBox_ohm_range = QtWidgets.QComboBox(Dialog)
        self.comboBox_ohm_range.setGeometry(QtCore.QRect(130, 120, 111, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_ohm_range.setFont(font)
        self.comboBox_ohm_range.setStyleSheet("background-color: rgb(143, 170, 220);\n"
"border-width: 5px;\n"
"border-radius: 6px;")
        self.comboBox_ohm_range.setObjectName("comboBox_ohm_range")
        self.comboBox_ohm_range.addItem("")
        self.comboBox_ohm_range.addItem("")
        self.comboBox_ohm_range.addItem("")
        self.comboBox_ohm_range.addItem("")
        self.comboBox_ohm_range.addItem("")
        self.comboBox_ohm_range.addItem("")
        self.comboBox_ohm_range.addItem("")
        self.comboBox_ohm_range.addItem("")
        self.comboBox_ohm_range.addItem("")
        self.label_volt_range_4 = QtWidgets.QLabel(Dialog)
        self.label_volt_range_4.setGeometry(QtCore.QRect(40, 160, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_volt_range_4.setFont(font)
        self.label_volt_range_4.setStyleSheet("QLabel\n"
" {\n"
" font: 63 12pt \"Segoe UI Semibold\";\n"
" color : rgb(143, 170, 220);\n"
" }")
        self.label_volt_range_4.setObjectName("label_volt_range_4")
        self.comboBox_temp = QtWidgets.QComboBox(Dialog)
        self.comboBox_temp.setGeometry(QtCore.QRect(140, 160, 101, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_temp.setFont(font)
        self.comboBox_temp.setStyleSheet("background-color: rgb(143, 170, 220);\n"
"border-width: 5px;\n"
"border-radius: 6px;")
        self.comboBox_temp.setObjectName("comboBox_temp")
        self.comboBox_temp.addItem("")
        self.comboBox_temp.addItem("")
        self.line_display = QtWidgets.QLabel(Dialog)
        self.line_display.setEnabled(False)
        self.line_display.setGeometry(QtCore.QRect(38, 196, 201, 2))
        self.line_display.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.line_display.setStyleSheet("background-color:  rgb(143, 170, 220);\n"
"\n"
"")
        self.line_display.setText("")
        self.line_display.setObjectName("line_display")
        self.pokit_logo_3 = QtWidgets.QLabel(Dialog)
        self.pokit_logo_3.setEnabled(False)
        self.pokit_logo_3.setGeometry(QtCore.QRect(9, 9, 33, 29))
        self.pokit_logo_3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pokit_logo_3.setStyleSheet("border-image: url(:/images/pokit_logo.png);")
        self.pokit_logo_3.setText("")
        self.pokit_logo_3.setScaledContents(True)
        self.pokit_logo_3.setObjectName("pokit_logo_3")

        self.retranslateUi(Dialog)
        self.comboBox_volt_range.setCurrentIndex(6)
        self.comboBox_amp_range.setCurrentIndex(5)
        self.comboBox_ohm_range.setCurrentIndex(8)
        self.comboBox_temp.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_ok.setText(_translate("Dialog", "OK"))
        self.comboBox_volt_range.setItemText(0, _translate("Dialog", "0mV - 300mV"))
        self.comboBox_volt_range.setItemText(1, _translate("Dialog", "300mV - 2V"))
        self.comboBox_volt_range.setItemText(2, _translate("Dialog", "2V - 6V"))
        self.comboBox_volt_range.setItemText(3, _translate("Dialog", "6V - 12V"))
        self.comboBox_volt_range.setItemText(4, _translate("Dialog", "12V - 30V"))
        self.comboBox_volt_range.setItemText(5, _translate("Dialog", "30V - 60V"))
        self.comboBox_volt_range.setItemText(6, _translate("Dialog", "Auto range"))
        self.label_volt_range.setText(_translate("Dialog", "Voltage"))
        self.label_volt_range_2.setText(_translate("Dialog", "Current"))
        self.comboBox_amp_range.setItemText(0, _translate("Dialog", "0A - 10mA"))
        self.comboBox_amp_range.setItemText(1, _translate("Dialog", "10mA - 30mA"))
        self.comboBox_amp_range.setItemText(2, _translate("Dialog", "30mA - 150mA"))
        self.comboBox_amp_range.setItemText(3, _translate("Dialog", "150mA - 300mA"))
        self.comboBox_amp_range.setItemText(4, _translate("Dialog", "300mA - 3A"))
        self.comboBox_amp_range.setItemText(5, _translate("Dialog", "Auto range"))
        self.label_volt_range_3.setText(_translate("Dialog", "Resistance"))
        self.comboBox_ohm_range.setItemText(0, _translate("Dialog", "0Ω - 160Ω"))
        self.comboBox_ohm_range.setItemText(1, _translate("Dialog", "160Ω - 330Ω"))
        self.comboBox_ohm_range.setItemText(2, _translate("Dialog", "330Ω - 890Ω"))
        self.comboBox_ohm_range.setItemText(3, _translate("Dialog", "890Ω - 1.5kΩ"))
        self.comboBox_ohm_range.setItemText(4, _translate("Dialog", "1.5kΩ - 10kΩ"))
        self.comboBox_ohm_range.setItemText(5, _translate("Dialog", "10kΩ - 100kΩ"))
        self.comboBox_ohm_range.setItemText(6, _translate("Dialog", "100kΩ - 470kΩ"))
        self.comboBox_ohm_range.setItemText(7, _translate("Dialog", "470kΩ - 1MΩ"))
        self.comboBox_ohm_range.setItemText(8, _translate("Dialog", "Auto range"))
        self.label_volt_range_4.setText(_translate("Dialog", "Temperature"))
        self.comboBox_temp.setItemText(0, _translate("Dialog", "Celsius"))
        self.comboBox_temp.setItemText(1, _translate("Dialog", "Fahrenheit"))

import ui_resource_rc
