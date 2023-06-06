from tela_login import *
from cadastroUsuario import *
from conexao import *

from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QTextBrowser, QLineEdit, QGridLayout, QPushButton, QApplication, QMainWindow, QWidget, QMessageBox

class carregaTelaCadastro(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.enviarCadastro.clicked.connect(lambda :self.cadastro())


    def cadastro(self):
        conecta = Conexao()
        usuario=self.usuarioEdit.text()
        senha=self.senhaEdit.text()
        sql=f"INSERT INTO LOGIN (usuario,senha) VALUES('{usuario}','{senha}')"
        print(sql)
        conecta.executaDML(sql)
        print("Usuario cadastrado")
