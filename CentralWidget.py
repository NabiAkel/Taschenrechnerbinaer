import PyQt6
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QSlider, QHBoxLayout, QTextBrowser, QGridLayout, QLabel, QLineEdit, QTextBrowser
from PyQt6.QtCore import pyqtSlot, Qt, QSize


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.binlabel = QLabel("Bitte gebe eine Binärzahl zwischen 0-1111 1111 ein:  ", self)
        self.binlabel1 = QLineEdit(self)
        self.binlabel1.setInputMask("Bbbbbbbb")

        self.hexalabel = QLabel("Bitte gebe eine Hexadezimalzahl zwischen 0 und FF ein: ", self)
        self.hexalabel1 = QLineEdit(self)
        self.hexalabel1.setInputMask("Hh")

        self.ergebnis = QLabel("Ergebnis", self)
        self.ergebnis1 = QTextBrowser(self)

        self.binlabel1.editingFinished.connect(self.calc)
        self.hexalabel1.editingFinished.connect(self.calc)

        layout = QGridLayout(self)

        layout.addWidget(self.binlabel, 1, 1)
        layout.addWidget(self.binlabel1, 1, 2)
        layout.addWidget(self.hexalabel, 2, 1)
        layout.addWidget(self.hexalabel1, 2, 2)
        layout.addWidget(self.ergebnis, 3, 1)
        layout.addWidget(self.ergebnis1, 3, 2)

    @pyqtSlot()
    def calc(self):
            str_bin = self.binlabel1.text()
            str_hex = self.hexalabel1.text()

            print(str_bin + str_hex)

            self.ergebnis1.append(str_bin + str_hex)