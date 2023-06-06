
from cadastroImovel import *
from conexao import *
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QTextBrowser, QLineEdit, QGridLayout, QPushButton, QApplication, QMainWindow, QWidget, QMessageBox
import sys
import json
class carregaTelaCadastraImovel(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.pushButton.clicked.connect(lambda: self.consultaCEP())
        self.pushButton_4.clicked.connect(lambda: self.consultaImovel())
        self.pushButton_5.clicked.connect(lambda: self.gerarJson())
        self.pushButton_2.clicked.connect(lambda :self.atualizaImovel())
        self.login=None
        self.mostraTabela()


    def salvaLogin(self,ativo):
        self.login=ativo

    def gravaImovel(self,endereco,cep,rua,bairro,cidade,uf):
        conecta = Conexao()
        print(self.login)
        numero = self.edNumero.text()
        complemento = self.edComplemento.text()
        tipo = self.comboTipo.currentText()
        status = self.comboStatus.currentText()
        descricao = self.edDescricao.text()
        tipoImovel = self.comboTipoImovel.currentText()
        caracteristicas = self.edCaract.toPlainText()
        preco = self.edPreco.text()
        observacoes = self.edObs.toPlainText()
        sql = f"INSERT INTO  IMOVEL (ENDERECO_CEP,LOGIN_USUARIO,NUMERO,COMPLEMENTO,TIPONEGOCIACAO,STATUSIMOVEL,DESCRICAO,TIPOIMOVEL,CARACTERISTICAS,PRECO,OBSERVACOES) VALUES('{cep}','{self.login}','{numero}','{complemento}','{tipo}','{status}','{descricao}','{tipoImovel}','{caracteristicas}','{preco}','{observacoes}')"
        conecta.executaDML(sql)
        self.mostraTabela()

    def deleteImovel(self,comando):
        print("Deleta")
        conecta = Conexao()
        conecta.executaDML(comando)
        self.mostraTabela()

    def atualizaImovel(self):
        conecta = Conexao()
        id = self.edID.text()
        sql = f"SELECT * FROM IMOVEL WHERE IDMOVEL='{id}'"
        imovel = 0
        imovel = conecta.executaDDL(sql)
        sql = f"SELECT * FROM ENDERECO WHERE CEP='{imovel[0][1]}'"
        endereco = conecta.executaDDL(sql)
        if (imovel != 0):
            cep = self.edCEP.setText(endereco[0][0])
            rua = self.edRua.setText(endereco[0][1])
            bairro = self.edBairro.setText(endereco[0][2])
            cidade = self.edCidade.setText(endereco[0][3])
            uf = self.edUF.setText(endereco[0][4])
            numero = self.edNumero.setText(str(imovel[0][3]))
            descricao = self.edDescricao.setText(imovel[0][7])
            complemento = self.edComplemento.setText(imovel[0][4])
            observacoes = self.edObs.setText(imovel[0][11])
            descricao = self.edDescricao.setText(imovel[0][7])
            caracteristicas = self.edCaract.setText(imovel[0][9])
            tipo = self.comboTipo.setCurrentText(imovel[0][5])
            preco = self.edPreco.setText(str(imovel[0][10]))
            status = self.comboStatus.setCurrentText(imovel[0][6])
            tipoImovel = self.comboTipoImovel.setCurrentText(imovel[0][8])
            cept = self.edCEP.text()
            ruat = self.edRua.text()
            bairrot = self.edBairro.text()
            cidadet = self.edCidade.text()
            uft = self.edUF.text()
            numerot = self.edNumero.text()
            complementot = self.edComplemento.text()
            tipot = self.comboTipo.currentText()
            statust = self.comboStatus.currentText()
            descricaot = self.edDescricao.text()
            tipoImovelt = self.comboTipoImovel.currentText()
            caracteristicast = self.edCaract.toPlainText()
            precot = self.edPreco.text()
            observacoest = self.edObs.toPlainText()
            sql=''
            sql=f"UPDATE public.imovel SET  endereco_cep='{cept}', numero='{numerot}', complemento='{complementot}', tiponegociacao='{tipot}', statusimovel='{statust}', descricao='{descricaot}', tipoimovel='{tipoImovelt}', caracteristicas='{caracteristicast}', preco='{precot}', observacoes='{observacoest}' WHERE IDMOVEL='{id}';"
            conecta.executaDML(sql)
            print(sql)
            self.mostraTabela()




    def gerarJson(self):
        conecta = Conexao()
        sql = f"SELECT * FROM IMOVEL"
        resultado = conecta.executaDDL(sql)
        vetor=[]
        x=len(resultado)
        for i in range(x):
            imovel={
                "id":resultado[i][0],
                "cep":resultado[i][1],
                "login":resultado[i][2],
                "numero":resultado[i][3],
                "complemento":resultado[i][4],
                "tiponegociacao":resultado[i][5],
                "status":resultado[i][6],
                "descricao":resultado[i][7],
                "tipoimovel":resultado[i][8],
                "caracteristicas":resultado[i][9],
                "preco":resultado[i][10],
                "observacoes":resultado[i][11]
            }
            vetor.append(imovel)
        json_object=json.dumps(vetor,indent=12)
        with open("imovel.json", "w") as outfile:
            outfile.write(json_object)

    def consultaImovel(self):
        conecta=Conexao()
        id=self.edID.text()
        sql = f"SELECT * FROM IMOVEL WHERE IDMOVEL='{id}'"
        imovel=0
        imovel = conecta.executaDDL(sql)
        sql = f"SELECT * FROM ENDERECO WHERE CEP='{imovel[0][1]}'"
        endereco = conecta.executaDDL(sql)
        if(imovel!=0):
            cep = self.edCEP.setText(endereco[0][0])
            rua = self.edRua.setText(endereco[0][1])
            bairro = self.edBairro.setText(endereco[0][2])
            cidade = self.edCidade.setText(endereco[0][3])
            uf = self.edUF.setText(endereco[0][4])
            numero=self.edNumero.setText(str(imovel[0][3]))
            descricao = self.edDescricao.setText(imovel[0][7])
            complemento = self.edComplemento.setText(imovel[0][4])
            observacoes = self.edObs.setText(imovel[0][11])
            descricao = self.edDescricao.setText(imovel[0][7])
            caracteristicas = self.edCaract.setText(imovel[0][9])
            tipo=self.comboTipo.setCurrentText(imovel[0][5])
            preco=self.edPreco.setText(str(imovel[0][10]))
            status=self.comboStatus.setCurrentText(imovel[0][6])
            tipoImovel=self.comboTipoImovel.setCurrentText(imovel[0][8])
            delete=''
            delete=f"DELETE FROM IMOVEL WHERE IDMOVEL='{id}'"
            self.pushButton_3.clicked.connect(lambda :self.deleteImovel(delete))





    def consultaCEP(self):
        conecta=Conexao()
        cep=self.edCEP.text()
        sql=f"SELECT * FROM ENDERECO WHERE CEP='{cep}'"
        endereco=0
        endereco=conecta.executaDDL(sql)
        if(endereco!=0):
            rua = self.edRua.setText(endereco[0][1])
            bairro = self.edBairro.setText(endereco[0][2])
            cidade = self.edCidade.setText(endereco[0][3])
            uf = self.edUF.setText(endereco[0][4])
            self.gravaImovel(endereco, cep, rua, bairro, cidade, uf)

    def mostraTabela(self):
        conecta = Conexao()
        sql = f"SELECT * FROM IMOVEL"
        resultado=conecta.executaDDL(sql)
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(resultado))

        for row,text in enumerate(resultado):
            for column,data in enumerate(text):
                self.tableWidget.setItem(row,column,QTableWidgetItem(str(data)))
        conecta.desconectar()



