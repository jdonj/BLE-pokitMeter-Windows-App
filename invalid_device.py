from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QPoint
import sys

# Import ui file created
from ui.invalid_device_ui import Ui_Dialog

class InvalidDevice(QtWidgets.QDialog):
    def __init__(self):
        super(InvalidDevice, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon(":/images/pokit_logo.png"))
        self.center()
        # self.show()   # for debugging only

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = InvalidDevice()
    app.exec_()