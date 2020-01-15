# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\Admin\Python\Workspace\Git_projects\python-projects\graphical_user_interface\pokitmeter\gui_files\main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(639, 388)
        MainWindow.setMinimumSize(QtCore.QSize(639, 388))
        MainWindow.setMaximumSize(QtCore.QSize(639, 388))
        MainWindow.setWindowTitle("")
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.dmm_main_background = QtWidgets.QLabel(self.centralwidget)
        self.dmm_main_background.setEnabled(False)
        self.dmm_main_background.setGeometry(QtCore.QRect(0, -1, 641, 391))
        self.dmm_main_background.setMinimumSize(QtCore.QSize(641, 391))
        self.dmm_main_background.setMaximumSize(QtCore.QSize(641, 391))
        self.dmm_main_background.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.dmm_main_background.setStyleSheet("border-image: url(:/images/main_window.png);")
        self.dmm_main_background.setText("")
        self.dmm_main_background.setIndent(4)
        self.dmm_main_background.setObjectName("dmm_main_background")
        self.lcd_display = QtWidgets.QLabel(self.centralwidget)
        self.lcd_display.setGeometry(QtCore.QRect(202, 116, 251, 81))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(36)
        self.lcd_display.setFont(font)
        self.lcd_display.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lcd_display.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(143, 170, 220);\n"
"border-radius: 13px;")
        self.lcd_display.setScaledContents(True)
        self.lcd_display.setAlignment(QtCore.Qt.AlignCenter)
        self.lcd_display.setObjectName("lcd_display")
        self.lcd_background = QtWidgets.QLabel(self.centralwidget)
        self.lcd_background.setEnabled(False)
        self.lcd_background.setGeometry(QtCore.QRect(191, 105, 271, 101))
        self.lcd_background.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lcd_background.setStyleSheet("background-color: rgb(47, 85, 151);\n"
"border-radius: 13px;")
        self.lcd_background.setText("")
        self.lcd_background.setObjectName("lcd_background")
        self.pokit_logo = QtWidgets.QLabel(self.centralwidget)
        self.pokit_logo.setEnabled(False)
        self.pokit_logo.setGeometry(QtCore.QRect(22, 332, 45, 41))
        self.pokit_logo.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pokit_logo.setStyleSheet("border-image: url(:/images/pokit_logo.png);")
        self.pokit_logo.setText("")
        self.pokit_logo.setScaledContents(True)
        self.pokit_logo.setObjectName("pokit_logo")
        self.lcd_background_2 = QtWidgets.QLabel(self.centralwidget)
        self.lcd_background_2.setEnabled(False)
        self.lcd_background_2.setGeometry(QtCore.QRect(100, 306, 459, 6))
        self.lcd_background_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lcd_background_2.setStyleSheet("background-color: rgb(47, 85, 151);\n"
"border-radius: 13px;")
        self.lcd_background_2.setText("")
        self.lcd_background_2.setObjectName("lcd_background_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(22, 13, 121, 61))
        self.label.setStyleSheet("border-image: url(:/images/logo_maxv.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.button_close = QtWidgets.QPushButton(self.centralwidget)
        self.button_close.setGeometry(QtCore.QRect(597, 18, 21, 24))
        self.button_close.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.button_close.setStyleSheet("QPushButton\n"
"{\n"
"   border-image: url(:/images/logo_close.png);\n"
"}\n"
"")
        self.button_close.setText("")
        self.button_close.setFlat(True)
        self.button_close.setObjectName("button_close")
        self.button_settings = QtWidgets.QPushButton(self.centralwidget)
        self.button_settings.setGeometry(QtCore.QRect(575, 18, 23, 24))
        self.button_settings.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.button_settings.setStyleSheet("QPushButton\n"
"{\n"
"   border-image: url(:/images/logo_settings.png);\n"
"}\n"
"")
        self.button_settings.setText("")
        self.button_settings.setFlat(True)
        self.button_settings.setObjectName("button_settings")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setEnabled(True)
        self.splitter.setGeometry(QtCore.QRect(98, 240, 461, 61))
        self.splitter.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.splitter.setStyleSheet("background-color: rgb(68, 114, 196);")
        self.splitter.setLineWidth(1)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(6)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.button_dc_volt = QtWidgets.QPushButton(self.splitter)
        self.button_dc_volt.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.button_dc_volt.setStyleSheet("QPushButton\n"
"{\n"
"   border-image: url(:/images/logo_dc_volt_off.png);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   border-image: url(:/images/logo_dc_volt_on.png);\n"
"}\n"
"\n"
"\n"
"")
        self.button_dc_volt.setText("")
        self.button_dc_volt.setDefault(False)
        self.button_dc_volt.setFlat(True)
        self.button_dc_volt.setObjectName("button_dc_volt")
        self.button_dc_amp = QtWidgets.QPushButton(self.splitter)
        self.button_dc_amp.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.button_dc_amp.setStyleSheet("QPushButton\n"
"{\n"
"   border-image: url(:/images/logo_dc_amp_off.png);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   border-image: url(:/images/logo_dc_amp_on.png);\n"
"}")
        self.button_dc_amp.setText("")
        self.button_dc_amp.setFlat(True)
        self.button_dc_amp.setObjectName("button_dc_amp")
        self.button_dc_ohm = QtWidgets.QPushButton(self.splitter)
        self.button_dc_ohm.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.button_dc_ohm.setStyleSheet("QPushButton\n"
"{\n"
"   border-image: url(:/images/logo_dc_ohm_off.png);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   border-image: url(:/images/logo_dc_ohm_on.png);\n"
"}")
        self.button_dc_ohm.setText("")
        self.button_dc_ohm.setFlat(True)
        self.button_dc_ohm.setObjectName("button_dc_ohm")
        self.button_dc_cont = QtWidgets.QPushButton(self.splitter)
        self.button_dc_cont.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.button_dc_cont.setStyleSheet("QPushButton\n"
"{\n"
"   border-image: url(:/images/logo_dc_cont_off.png);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   border-image: url(:/images/logo_dc_cont_on.png);\n"
"}")
        self.button_dc_cont.setText("")
        self.button_dc_cont.setFlat(True)
        self.button_dc_cont.setObjectName("button_dc_cont")
        self.button_ac_amp = QtWidgets.QPushButton(self.splitter)
        self.button_ac_amp.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.button_ac_amp.setStyleSheet("QPushButton\n"
"{\n"
"   border-image: url(:/images/logo_ac_amp_off.png);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   border-image: url(:/images/logo_ac_amp_on.png);\n"
"}")
        self.button_ac_amp.setText("")
        self.button_ac_amp.setFlat(True)
        self.button_ac_amp.setObjectName("button_ac_amp")
        self.button_ac_volt = QtWidgets.QPushButton(self.splitter)
        self.button_ac_volt.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.button_ac_volt.setStyleSheet("QPushButton\n"
"{\n"
"   border-image: url(:/images/logo_ac_volt_off.png);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   border-image: url(:/images/logo_ac_volt_on.png);\n"
"}")
        self.button_ac_volt.setText("")
        self.button_ac_volt.setFlat(True)
        self.button_ac_volt.setObjectName("button_ac_volt")
        self.button_diode = QtWidgets.QPushButton(self.splitter)
        self.button_diode.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.button_diode.setStyleSheet("QPushButton\n"
"{\n"
"   border-image: url(:/images/logo_diode_off.png);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   border-image: url(:/images/logo_diode_on.png);\n"
"}")
        self.button_diode.setText("")
        self.button_diode.setFlat(True)
        self.button_diode.setObjectName("button_diode")
        self.button_temp = QtWidgets.QPushButton(self.splitter)
        self.button_temp.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.button_temp.setStyleSheet("QPushButton\n"
"{\n"
"   border-image: url(:/images/logo_temp_off.png);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   border-image: url(:/images/logo_temp_on.png);\n"
"}")
        self.button_temp.setText("")
        self.button_temp.setFlat(True)
        self.button_temp.setObjectName("button_temp")
        self.dmm_main_background.raise_()
        self.lcd_background_2.raise_()
        self.lcd_background.raise_()
        self.lcd_display.raise_()
        self.pokit_logo.raise_()
        self.label.raise_()
        self.splitter.raise_()
        self.button_close.raise_()
        self.button_settings.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.lcd_display.setText(_translate("MainWindow", "- - - - -"))

import ui_resource_rc
