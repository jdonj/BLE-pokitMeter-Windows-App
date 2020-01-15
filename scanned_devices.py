from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QPoint
import sys

# Import ui file created
from ui.scanned_devices_ui import Ui_Dialog

class ScanGui(QtWidgets.QDialog):
    def __init__(self):
        super(ScanGui, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon(":/images/pokit_logo.png"))
        self.center()
        # self.show()   # for debugging only

    def add_item(self, devices):
        self.ui.listWidget_devices.clear()
        for key in devices.keys():
            self.ui.listWidget_devices.insertItem(-1, key)

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = ScanGui()
    items = {'a':0, 'b':1}
    window.add_item(items)

    app.exec_()