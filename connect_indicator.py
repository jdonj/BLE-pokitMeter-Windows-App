from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QPoint
import sys

# Import ui file created
from ui.connecting_ui import Ui_Connecting

class ConnectIndicator(QtWidgets.QDialog):
    def __init__(self):
        super(ConnectIndicator, self).__init__()
        self.ui = Ui_Connecting()
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
    window = ConnectIndicator()
    app.exec_()