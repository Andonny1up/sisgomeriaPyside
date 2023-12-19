import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QAbstractItemView, QHeaderView
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from interface.ui_Productos import Ui_Productos
from helpers import absPath


class WidgetProductos(QWidget,Ui_Productos):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        conexion = QSqlDatabase.addDatabase("QSQLITE")
        conexion.setDatabaseName(absPath("gomeria.db"))
        if not conexion.open():
            print("No se puede conectar a la base de datos")
            sys.exit(True)

        #creamos el modelo Productos
        self.modelo = QSqlTableModel()
        self.modelo.setTable("productos")
        self.modelo.select()
        self.modelo.setHeaderData(0, Qt.Horizontal, "Id")
        self.modelo.setHeaderData(1, Qt.Horizontal, "Descripcion")
        self.modelo.setHeaderData(2, Qt.Horizontal, "Marca")
        self.modelo.setHeaderData(3, Qt.Horizontal, "Precio")

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

    def new_row(self):
        descripcion = self.leDescripcion.text()
        marca = self.leMarca.text()
        precio = self.lePrecio.text()

        self.modelo.insertRow(self.modelo.rowCount())
        self.modelo.setData(self.modelo.index(self.modelo.rowCount()-1,1),descripcion)
        self.modelo.setData(self.modelo.index(self.modelo.rowCount()-1,2),marca)
        self.modelo.setData(self.modelo.index(self.modelo.rowCount()-1,3),precio)
        self.modelo.submitAll()
        self.modelo.select()
        self.tableView.resizeColumnsToContents()
        self.tableView.setColumnHidden(0, True)
        
        self.leDescripcion.clear()
        self.leMarca.clear()
        self.lePrecio.clear()