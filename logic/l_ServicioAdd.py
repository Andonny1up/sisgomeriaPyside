import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget,QTableWidgetItem, QAbstractItemView, QHeaderView
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQueryModel, QSqlQuery
from interface.ui_ServiciosAdd import Ui_ServiciosAdd
from helpers import absPath

class WidgetServiciosAdd(QWidget,Ui_ServiciosAdd):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        # configurar tabla de productos
        self.productosTable.setColumnCount(4)
        self.productosTable.setHorizontalHeaderLabels(["ID","Producto","Precio","Cantidad"])
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
        self.btnGuardar.clicked.connect(self.guardarServicio)


    def cargarClientes(self):
        model = QSqlQueryModel()
        model.setQuery("SELECT id,nombre FROM clientes")
        self.cbClientes.setModel(model)
        self.cbClientes.setModelColumn(1)


    def cargarProductos(self):
        model = QSqlQueryModel()
        model.setQuery("SELECT id,descripcion,precio FROM productos")
        self.cbProductos.setModel(model)
        self.cbProductos.setModelColumn(1)

    
    def agregarProducto(self):
        id_producto = self.cbProductos.model().record(self.cbProductos.currentIndex()).value("id")
        producto_seleccionado = self.cbProductos.currentText()
        precio_producto = self.cbProductos.model().record(self.cbProductos.currentIndex()).value("precio")
        cantidad = self.leCantidad.text()

        row = self.productosTable.rowCount()
        self.productosTable.insertRow(row)

        self.productosTable.setItem(row, 0, QTableWidgetItem(str(id_producto)))
        self.productosTable.setItem(row, 1, QTableWidgetItem(producto_seleccionado))
        self.productosTable.setItem(row, 2, QTableWidgetItem(str(precio_producto)))
        self.productosTable.setItem(row, 3, QTableWidgetItem(str(cantidad)))
        # self.productosTable.resizeColumnsToContents()

        self.leCantidad.clear()


    def guardarServicio(self):
        id_cliente = self.cbClientes.model().record(self.cbClientes.currentIndex()).value("id")
        vehiculo_descripcion = self.leVehiculo.text()
        servicio_descripcion = self.leDescripcionServicio.text()
        precio_servicio = self.lePrecio.text()
        precio_total = 0

        query = QSqlQuery()
        query.prepare("INSERT INTO servicios (id_cliente, vehiculo, descripcion, precio, precio_total, pagado) VALUES (:id_cliente, :vehiculo, :descripcion, :precio, :precio_total, :pagado)")
        query.bindValue(":id_cliente", id_cliente)
        query.bindValue(":vehiculo", vehiculo_descripcion)
        query.bindValue(":descripcion", servicio_descripcion)
        query.bindValue(":precio", precio_servicio)
        query.bindValue(":precio_total", precio_total)
        query.bindValue(":pagado", False)

        if not query.exec_():
            print("Error al insertar servicio:", query.lastError().text())
            return

        id_servicio = query.lastInsertId()
        precio_total = 0
        for row in range(self.productosTable.rowCount()):
            id_producto = int(self.productosTable.item(row, 0).text())
            precio_producto = float(self.productosTable.item(row, 2).text())
            cantidad = int(self.productosTable.item(row, 3).text())
            precio_total += precio_producto * cantidad
            query.prepare("INSERT INTO productos_servicio (id_servicio, id_producto, cantidad, precio) VALUES (:id_servicio, :id_producto, :cantidad, :precio)")
            query.bindValue(":id_servicio", id_servicio)
            query.bindValue(":id_producto", id_producto)
            query.bindValue(":precio", precio_producto)
            query.bindValue(":cantidad", cantidad)



            if not query.exec_():
                print("Error al insertar detalle de servicio:", query.lastError().text())
        
        precio_total += float(precio_servicio)

        print("Precio total:", precio_total)
        # Actualiza el precio total del servicio en la base de datos
        query.prepare("UPDATE servicios SET precio_total = :precio_total WHERE id = :id")
        query.bindValue(":precio_total", precio_total)
        query.bindValue(":id", id_servicio)
        if not query.exec_():
            print("Error al actualizar el precio total del servicio:", query.lastError().text())

        self.leVehiculo.clear()
        self.leDescripcionServicio.clear()
        self.lePrecio.clear()
        self.productosTable.setRowCount(0)

