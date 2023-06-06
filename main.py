from login import *
from tela_login import *
from cadastroImovel import *
from cadastroImovel_tela import *
from consultaImovel import *
from conexao import *
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QTextBrowser, QLineEdit, QGridLayout, QPushButton, QApplication, QMainWindow, QWidget, QMessageBox
import sys

class carregaTela(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.login = carregaTelaLogin()
        self.btnCadastrar.clicked.connect(lambda :self.abreLogin())
        self.btnFiltrar_2.clicked.connect(lambda :self.mostraTabela())
        self.btnFiltrar.clicked.connect(lambda:self.filtraTabela())
        self.mostraTabela()



    def filtraTabela(self):
        conecta = Conexao()
        tipo=self.comboTipo_2.currentText()
        tipoImovel=self.comboTipoImovel.currentText()
        precoInicial=self.edPrecoInicial.text()
        precoFinal=self.edPrecoFinal.text()
        sql=None
        if(precoFinal=='' and precoInicial==''):
            sql = f"SELECT idmovel, endereco_cep, login_usuario, numero, complemento, tiponegociacao, statusimovel, descricao, tipoimovel, caracteristicas, preco, observacoes FROM public.imovel WHERE tiponegociacao='{tipo}' AND tipoimovel='{tipoImovel}';"
            resultado = conecta.executaDDL(sql)
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(len(resultado))

            for row, text in enumerate(resultado):
                for column, data in enumerate(text):
                    self.tableWidget.setItem(row, column, QTableWidgetItem(str(data)))
            conecta.desconectar()
        elif(precoFinal=='' and precoInicial!=''):
            sql = f"SELECT idmovel, endereco_cep, login_usuario, numero, complemento, tiponegociacao, statusimovel, descricao, tipoimovel, caracteristicas, preco, observacoes FROM public.imovel WHERE tiponegociacao='{tipo}' AND tipoimovel='{tipoImovel}' AND preco>='{precoInicial}';"
            resultado = conecta.executaDDL(sql)
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(len(resultado))

            for row, text in enumerate(resultado):
                for column, data in enumerate(text):
                    self.tableWidget.setItem(row, column, QTableWidgetItem(str(data)))
            conecta.desconectar()
        elif (precoFinal == '' and precoInicial == ''):
            print(precoFinal)
            print("aqui 2")
            sql = f"SELECT idmovel, endereco_cep, login_usuario, numero, complemento, tiponegociacao, statusimovel, descricao, tipoimovel, caracteristicas, preco, observacoes FROM public.imovel WHERE tiponegociacao='{tipo}' AND tipoimovel='{tipoImovel}' AND preco>='{precoInicial} AND preco<='{precoFinal}';"
            resultado = conecta.executaDDL(sql)
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(len(resultado))

            for row, text in enumerate(resultado):
                for column, data in enumerate(text):
                    self.tableWidget.setItem(row, column, QTableWidgetItem(str(data)))
            conecta.desconectar()


    def abreLogin(self):
        self.login.show()


    def abreCadastraImovel(self):
        self.cadastraImovel.show()

    def mostraTabela(self):
        conecta = Conexao()
        sql = f"SELECT * FROM IMOVEL"
        resultado=conecta.executaDDL(sql)
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(resultado))
        print(len(resultado))

        for row,text in enumerate(resultado):
            for column,data in enumerate(text):
                self.tableWidget.setItem(row,column,QTableWidgetItem(str(data)))
        conecta.desconectar()



def main():
    qt = QApplication(sys.argv)
    tela = carregaTela()
    tela.show()
    qt.exec_()


if __name__=="__main__":
    main()
