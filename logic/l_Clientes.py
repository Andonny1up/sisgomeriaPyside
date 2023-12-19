import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QAbstractItemView, QHeaderView
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from interface.ui_Clientes import Ui_clientes
from helpers import absPath

class WidgetClientes(QWidget,Ui_clientes):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        conexion = QSqlDatabase.addDatabase("QSQLITE")
        conexion.setDatabaseName(absPath("gomeria.db"))
        if not conexion.open():
            print("No se puede conectar a la base de datos")
            sys.exit(True)

        #creamos el modelo clientes
        self.modelo = QSqlTableModel()
        self.modelo.setTable("clientes")
        self.modelo.select()
        self.modelo.setHeaderData(0, Qt.Horizontal, "Id")
        self.modelo.setHeaderData(1, Qt.Horizontal, "Nombre")
        self.modelo.setHeaderData(2, Qt.Horizontal, "Carnet de Identidad")
        self.modelo.setHeaderData(3, Qt.Horizontal, "Telefono")

        #configuramos la tabla
        self.tableView.setModel(self.modelo)
        self.tableView.resizeColumnsToContents()
        self.tableView.setColumnHidden(0, True)

        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        # self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # self.tableView.selectionModel().selectionChanged.connect(self.select_row)
        self.btnCreate.clicked.connect(self.new_row)

        self.row = -1

    def select_row(self,selecction):
        if selecction.indexes():
            self.row = selecction.indexes()[0].row()
            name = self.modelo.index(self.row, 1).data()
            ci = self.modelo.index(self.row, 2).data()
            telefono = self.modelo.index(self.row, 3).data()
            self.leNombre.setText(name)
            self.leCi.setText(ci)
            self.leTel.setText(telefono)


    def new_row(self):
        name = self.leNombre.text()
        ci = self.leCi.text()
        telefono = self.leTel.text()

        self.modelo.insertRows(self.modelo.rowCount(),1)
        self.modelo.setData(self.modelo.index(self.modelo.rowCount()-1,1),name)
        self.modelo.setData(self.modelo.index(self.modelo.rowCount()-1,2),ci)
        self.modelo.setData(self.modelo.index(self.modelo.rowCount()-1,3),telefono)
        self.modelo.submitAll()
        self.modelo.select()
        self.tableView.resizeColumnsToContents()
        self.tableView.setColumnHidden(0, True)

        self.leNombre.setText("")
        self.leCi.setText("")
        self.leTel.setText("")