import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, uic, QtWidgets
import sys
import os
import datetime

class wintab2(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.tab2 = QTabWidget(self)
        self.addTab(self.tab2, 'Tab 2')

        self.btn1_t2 = QPushButton('Button', self.tab2)
        self.btn1_t2.move(10, 300)
        self.btn1_t2.setText('Back')
        self.btn1_t2.clicked.connect(self.back)

        self.btn2_t2 = QPushButton('Button', self.tab2)
        self.btn2_t2.move(100, 300)
        self.btn2_t2.setText('Next')
        self.btn2_t2.clicked.connect(self.next)
