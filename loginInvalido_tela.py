from loginInvalido import *

from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QTextBrowser, QLineEdit, QGridLayout, QPushButton, QApplication, QMainWindow, QWidget, QMessageBox
import sys

class carregaTelaLoginInvalido(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        super().setupUi(self)