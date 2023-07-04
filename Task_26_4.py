import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit,QTextEdit,QGridLayout,QLabel,QComboBox,QMessageBox
from PyQt6.QtGui import QIcon,QAction
class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
    def initUI(self):
        self.textP = QLabel(' ')
        self.setCentralWidget(self.textP)
        font = self.textP.font()
        font.setPointSize(16)
        self.textP.setFont(font)

        openAction = QAction(QIcon(),'Открыть',self)
        openAction.setShortcut('Ctrl+Q')
        openAction.setStatusTip('Open application')
        openAction.triggered.connect(self.open)
        self.statusBar()
        menubar = self.menuBar()

        fileMenu = menubar.addMenu('&Описание')
        fileMenu.addAction(openAction)
        fileMenu1 = menubar.addMenu('&Инструкция')
        fileMenu1.addAction(openAction)
        fileMenu2 = menubar.addMenu('&Помощь')
        fileMenu2.addAction(openAction)

        self.setGeometry(300,300,350,250)
        self.setWindowTitle('Программа')
        self.show()
    def open(self):
        self.textP.setText('Открытие...')

if __name__ =='__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


app = QApplication(sys.argv) #
window = Example()#создает окно
window.show()#
app.exec()#