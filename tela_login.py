from tela_cadastroUsuario import *
from cadastroImovel_tela import *
from loginInvalido_tela import *
from login import *
from conexao import *

from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QTextBrowser, QLineEdit, QGridLayout, QPushButton, QApplication, QMainWindow, QWidget, QMessageBox
import sys

class carregaTelaLogin(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.cadastro=carregaTelaCadastro()
        self.cadastraImovel=carregaTelaCadastraImovel()
        self.loginInvalido=carregaTelaLoginInvalido()
        self.btnCadastrar.clicked.connect(lambda: self.cadastraUsuario())
        self.btnLogin.clicked.connect(lambda: self.login())


    def cadastraUsuario(self):
        conecta = Conexao()
        self.cadastro.show()

    def login(self):
        realizado=0
        conecta = Conexao()
        sql="SELECT * FROM LOGIN"
        usuarios=conecta.executaDDL(sql)
        logins=[]
        senhas=[]
        login=self.edUsuario.text()
        senha=self.edSenha.text()
        ativo=None
        x=len(usuarios)
        for i in range (x):
            logins.append(usuarios[i][0])
        for i in range (x):
            senhas.append(usuarios[i][1])
        for i in range (x):
            if(login==logins[i] and senha==senhas[i]):
                ativo=login
                print("Login realizado")
                realizado=1

        if(realizado):
            self.cadastraImovel.salvaLogin(ativo)
            self.cadastraImovel.show()
        else:
            self.loginInvalido.show()



