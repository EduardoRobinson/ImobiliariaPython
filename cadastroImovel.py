# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastroImovel.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(864, 687)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 731, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 63, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 430, 821, 241))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        self.edID = QtWidgets.QLineEdit(self.centralwidget)
        self.edID.setGeometry(QtCore.QRect(160, 60, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.edID.setFont(font)
        self.edID.setObjectName("edID")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 100, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.edCEP = QtWidgets.QLineEdit(self.centralwidget)
        self.edCEP.setGeometry(QtCore.QRect(160, 92, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.edCEP.setFont(font)
        self.edCEP.setObjectName("edCEP")
        self.edRua = QtWidgets.QLineEdit(self.centralwidget)
        self.edRua.setGeometry(QtCore.QRect(160, 122, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.edRua.setFont(font)
        self.edRua.setObjectName("edRua")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 129, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.edBairro = QtWidgets.QLineEdit(self.centralwidget)
        self.edBairro.setGeometry(QtCore.QRect(160, 152, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.edBairro.setFont(font)
        self.edBairro.setObjectName("edBairro")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(100, 158, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.edCidade = QtWidgets.QLineEdit(self.centralwidget)
        self.edCidade.setGeometry(QtCore.QRect(160, 184, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.edCidade.setFont(font)
        self.edCidade.setObjectName("edCidade")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(100, 190, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.edUF = QtWidgets.QLineEdit(self.centralwidget)
        self.edUF.setGeometry(QtCore.QRect(160, 214, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.edUF.setFont(font)
        self.edUF.setObjectName("edUF")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(100, 220, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.edNumero = QtWidgets.QLineEdit(self.centralwidget)
        self.edNumero.setGeometry(QtCore.QRect(160, 242, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.edNumero.setFont(font)
        self.edNumero.setObjectName("edNumero")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(-20, 246, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.edComplemento = QtWidgets.QLineEdit(self.centralwidget)
        self.edComplemento.setGeometry(QtCore.QRect(160, 276, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.edComplemento.setFont(font)
        self.edComplemento.setObjectName("edComplemento")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(-20, 280, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(450, 60, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.comboTipo = QtWidgets.QComboBox(self.centralwidget)
        self.comboTipo.setGeometry(QtCore.QRect(600, 50, 181, 22))
        self.comboTipo.setObjectName("comboTipo")
        self.comboTipo.addItem("")
        self.comboTipo.addItem("")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(450, 95, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.comboStatus = QtWidgets.QComboBox(self.centralwidget)
        self.comboStatus.setGeometry(QtCore.QRect(599, 86, 181, 22))
        self.comboStatus.setObjectName("comboStatus")
        self.comboStatus.addItem("")
        self.comboStatus.addItem("")
        self.comboStatus.addItem("")
        self.edDescricao = QtWidgets.QLineEdit(self.centralwidget)
        self.edDescricao.setGeometry(QtCore.QRect(599, 120, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.edDescricao.setFont(font)
        self.edDescricao.setObjectName("edDescricao")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(479, 126, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(480, 156, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.comboTipoImovel = QtWidgets.QComboBox(self.centralwidget)
        self.comboTipoImovel.setGeometry(QtCore.QRect(600, 150, 181, 22))
        self.comboTipoImovel.setObjectName("comboTipoImovel")
        self.comboTipoImovel.addItem("")
        self.comboTipoImovel.addItem("")
        self.comboTipoImovel.addItem("")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(470, 189, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.edCaract = QtWidgets.QTextEdit(self.centralwidget)
        self.edCaract.setGeometry(QtCore.QRect(600, 190, 231, 71))
        self.edCaract.setObjectName("edCaract")
        self.edPreco = QtWidgets.QLineEdit(self.centralwidget)
        self.edPreco.setGeometry(QtCore.QRect(600, 274, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.edPreco.setFont(font)
        self.edPreco.setObjectName("edPreco")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(480, 280, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.edObs = QtWidgets.QTextEdit(self.centralwidget)
        self.edObs.setGeometry(QtCore.QRect(600, 311, 231, 71))
        self.edObs.setObjectName("edObs")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(470, 310, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 330, 75, 23))
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 330, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 330, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 60, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(140, 380, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setUnderline(False)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cadastro de Imóveis"))
        self.label.setText(_translate("MainWindow", "CADASTRO DE IMÓVEIS"))
        self.label_2.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "CEP"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "NUMERO"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "COMPLEMENTO"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "STATUS"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "DESCRIÇÃO"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "TIPO IMÓVEL"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "CARACTERÍSTICAS"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "PREÇO"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "OBSERVAÇÕES"))
        self.label_3.setText(_translate("MainWindow", "CEP"))
        self.label_4.setText(_translate("MainWindow", "RUA"))
        self.label_5.setText(_translate("MainWindow", "BAIRRO"))
        self.label_6.setText(_translate("MainWindow", "CIDADE"))
        self.label_7.setText(_translate("MainWindow", "UF"))
        self.label_8.setText(_translate("MainWindow", "NÚMERO RESIDÊNCIA"))
        self.label_9.setText(_translate("MainWindow", "COMPLEMENTO"))
        self.label_10.setText(_translate("MainWindow", "TIPO DE NEGOCIAÇÃO"))
        self.comboTipo.setItemText(0, _translate("MainWindow", "LOCAÇÃO"))
        self.comboTipo.setItemText(1, _translate("MainWindow", "VENDA"))
        self.label_11.setText(_translate("MainWindow", "STATUS IMÓVEL"))
        self.comboStatus.setItemText(0, _translate("MainWindow", "DISPONÍVEL"))
        self.comboStatus.setItemText(1, _translate("MainWindow", "LOCADO"))
        self.comboStatus.setItemText(2, _translate("MainWindow", "VENDIDO"))
        self.label_12.setText(_translate("MainWindow", "DESCRIÇÃO"))
        self.label_13.setText(_translate("MainWindow", "TIPO DE IMÓVEL"))
        self.comboTipoImovel.setItemText(0, _translate("MainWindow", "APARTAMENTO"))
        self.comboTipoImovel.setItemText(1, _translate("MainWindow", "CASA"))
        self.comboTipoImovel.setItemText(2, _translate("MainWindow", "TERRENO"))
        self.label_14.setText(_translate("MainWindow", "CARACTERÍSTICAS"))
        self.label_15.setText(_translate("MainWindow", "PREÇO"))
        self.label_16.setText(_translate("MainWindow", "OBSERVAÇÕES"))
        self.pushButton.setText(_translate("MainWindow", "GRAVAR"))
        self.pushButton_2.setText(_translate("MainWindow", "ATUALIZAR"))
        self.pushButton_3.setText(_translate("MainWindow", "EXCLUIR"))
        self.pushButton_4.setText(_translate("MainWindow", "CONSULTAR"))
        self.pushButton_5.setText(_translate("MainWindow", "Criar JSON"))