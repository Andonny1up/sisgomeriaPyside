import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget,QTableWidgetItem, QAbstractItemView, QHeaderView
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQueryModel
from interface.ui_ServiciosAdd import Ui_ServiciosAdd
from helpers import absPath

class WidgetServiciosAdd(QWidget,Ui_ServiciosAdd):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        # configurar tabla de productos
        self.productosTable.setColumnCount(3)
        self.productosTable.setHorizontalHeaderLabels(["ID","Producto","Cantidad"])
        self.productosTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.productosTable.hideColumn(0)
        

        conexion = QSqlDatabase.addDatabase("QSQLITE")
        conexion.setDatabaseName(absPath("gomeria.db"))
        if not conexion.open():
            print("No se puede conectar a la base de datos")
            sys.exit(True)
        self.cargarClientes()
        self.cargarProductos()
        self.btnAddProduct.clicked.connect(self.agregarProducto)


    def cargarClientes(self):
        model = QSqlQueryModel()
        model.setQuery("SELECT id,nombre FROM clientes")
        self.cbClientes.setModel(model)
        self.cbClientes.setModelColumn(1)


    def cargarProductos(self):
        model = QSqlQueryModel()
        model.setQuery("SELECT id,descripcion FROM productos")
        self.cbProductos.setModel(model)
        self.cbProductos.setModelColumn(1)

    
    def agregarProducto(self):
        id_producto = self.cbProductos.model().record(self.cbProductos.currentIndex()).value("id")
        producto_seleccionado = self.cbProductos.currentText()
        cantidad = self.leCantidad.text()

        row = self.productosTable.rowCount()
        self.productosTable.insertRow(row)

        self.productosTable.setItem(row, 0, QTableWidgetItem(str(id_producto)))
        self.productosTable.setItem(row, 1, QTableWidgetItem(producto_seleccionado))
        self.productosTable.setItem(row, 2, QTableWidgetItem(str(cantidad)))
        self.productosTable.resizeColumnsToContents()

        self.leCantidad.clear()
