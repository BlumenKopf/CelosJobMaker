import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, uic, QtWidgets
import sys
import os

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class PageOne(QWidget):    
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()
    
    def initUI(self):
        # Define the Main Window
        self.setFocus()
        self.setGeometry(500,500,1000,500)
        self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(os.path.join('icon','Celos.bmp'))))
        self.setWindowTitle('Job Information')
        self.setFont(QtGui.QFont('Arial', 10))

        self.jobnamelbl = QLabel('Job Name:', self)
        self.jobnamelbl.setFixedSize(100, 30)
        self.jobnamelbl.move(10, 10)

        self.jobnametxt = QLineEdit(self)
        self.jobnametxt.setFixedSize(200, 30)
        self.jobnametxt.move(10, 40)

        self.jobidlbl = QLabel('Job ID:', self)
        self.jobidlbl.setFixedSize(100, 30)
        self.jobidlbl.move(250, 10)

        self.jobidtxt = QLineEdit(self)
        self.jobidtxt.setFixedSize(200, 30)
        self.jobidtxt.move(250, 40)

        self.button1 = QPushButton('Button', self)
        self.button1.move(10, 300)
        self.button1.setText('Next')
        self.button1.clicked.connect(self.next)

        self.button2 = QPushButton('Button', self)
        self.button2.move(100, 300)
        self.button2.setText('Cancel')
        self.button2.clicked.connect(self.btn_close) 

        self.combobox = QComboBox(self)
        self.combobox.addItems([
            'Heidenhain',
            'Siemens',
            'Mapps'
        ])
        self.combobox.move(10, 100)
       
        

    def next():
        pass    
    
    def btn_close(self):
        self.close()

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    mainWin = PageOne()
    app.quit()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
