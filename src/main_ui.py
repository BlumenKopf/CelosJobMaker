import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, uic, QtWidgets
import sys
import os
import datetime

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class ListBoxWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(500, 300)
        self.setAcceptDrops(True)
    
    def dragEnterEvent(self, e: QtGui.QDragEnterEvent) -> None:
        if e.mimeData().hasUrls:
            e.accept()
        else:
            e.ignore()

    def dragMoveEvent(self, e: QtGui.QDragMoveEvent) -> None:
        if e.mimeData().hasUrls():
            e.setDropAction(QtCore.Qt.CopyAction)
            e.accept()
        else:
            e.ignore()
    
    def dropEvent(self, event: QtGui.QDropEvent) -> None:
        if event.mimeData().hasUrls():
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()

            links = []
            for url in event.mimeData().urls():
                links.append()

            print(event.mimeData().urls())
            

class PageOne(QTabWidget):    
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()
    
    def initUI(self):
        # Define the First Window
        self.setFocus()
        self.setGeometry(500,500,1000,500)
        self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(os.path.join('icons','Celos.bmp'))))
        self.setWindowTitle('Job Information')
        self.setFont(QtGui.QFont('Arial', 10))

        self.tab1 = QTabWidget(self)#.tabBar().setTabButton(0, QTabBar.RightSide, None)
        self.tab2 = QTabWidget(self)
        
        # Tab 1 
        self.addTab(self.tab1, 'Tab 1')

        self.jobnamelbl = QLabel('Job Name:', self.tab1)
        self.jobnamelbl.setFixedSize(100, 30)
        self.jobnamelbl.move(10, 10)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.jobnamelbl.setFont(font)        

        self.jobnametxt = QLineEdit(self.tab1)
        self.jobnametxt.setFixedSize(200, 30)
        self.jobnametxt.move(10, 40)

        self.jobidlbl = QLabel('Job ID:', self.tab1)
        self.jobidlbl.setFixedSize(100, 30)
        self.jobidlbl.move(250, 10)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.jobidlbl.setFont(font)

        self.jobidtxt = QLineEdit(self.tab1)
        self.jobidtxt.setFixedSize(200, 30)
        self.jobidtxt.move(250, 40)

        self.custnamelbl = QLabel('Customer Name:', self.tab1)
        self.custnamelbl.move(10, 80)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.custnamelbl.setFont(font)
        
        self.custnametxt = QLineEdit(self.tab1)
        self.custnametxt.setFixedSize(200, 30)
        self.custnametxt.move(10, 105)

        self.custidlbl = QLabel('Customer ID:', self.tab1)
        self.custidlbl.move(250, 80)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.custidlbl.setFont(font)

        self.custidtxt = QLineEdit(self.tab1)
        self.custidtxt.setFixedSize(200, 30)
        self.custidtxt.move(250, 105)

        self.date = QDateEdit(self.tab1)
        self.date.move(10,200)
        now = datetime.datetime.today()
        self.date.setDate(now)

        self.time = QTimeEdit(self.tab1)
        self.time.move(135,200)        

        self.button1 = QPushButton('Button', self.tab1)
        self.button1.move(10, 300)
        self.button1.setText('Next')
        self.button1.clicked.connect(self.next)

        self.button2 = QPushButton('Button', self.tab1)
        self.button2.move(100, 300)
        self.button2.setText('Cancel')
        self.button2.clicked.connect(self.btn_close) 

        self.combobox = QComboBox(self.tab1)
        self.combobox.addItems([
            'Heidenhain',
            'Siemens',
            'Mapps'
        ])
        self.combobox.move(10, 400) 

        #Tab 2  
             
        self.addTab(self.tab2, 'Tab 2') 

        self.btn1_t2 = QPushButton('Button', self.tab2)
        self.btn1_t2.move(10, 300)
        self.btn1_t2.setText('Back')
        self.btn1_t2.clicked.connect(self.back)

        self.btn2_t2 = QPushButton('Button', self.tab2)
        self.btn2_t2.move(1000, 300)
        self.btn2_t2.setText('Next')
        self.btn2_t2.clicked.connect(self.next)

        self.lstv = ListBoxWidget(self.tab2)




    def next(self):
        index = self.currentIndex()
        index += 1
        self.setCurrentIndex(index)

    def back(self):
        index = self.currentIndex()
        index -= 1
        self.setCurrentIndex(index)

    def btn_close(self):
        self.close()
    
    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.msg = QMessageBox(self)
        self.msg.setWindowTitle('Close App')
        self.msg.setText('You are sure to close the App')
        self.msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        returnvalue = self.msg.exec_()

        if returnvalue == QMessageBox.Yes:
            if not type(event) == bool:
                event.accept()
            else:
                sys.exit()
        else:
            if not type(event) == bool:
                event.ignore()



def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    mainWin = PageOne()
    app.quit()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
