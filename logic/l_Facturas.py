import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget,QTableWidgetItem, QAbstractItemView, QHeaderView
from PySide6.QtWidgets import QFileDialog
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from interface.ui_Facturas import Ui_Facturas

from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle

from helpers import absPath

class WidgetFacturas(QWidget,Ui_Facturas):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        conexion = QSqlDatabase.addDatabase("QSQLITE")
        conexion.setDatabaseName(absPath("gomeria.db"))
        if not conexion.open():
            print("No se puede conectar a la base de datos")
            sys.exit(True)

        self.model = QSqlTableModel(db=conexion)
        self.model.setQuery("""
            SELECT servicios.id, clientes.nombre, servicios.vehiculo, servicios.descripcion, servicios.precio, servicios.precio_total, servicios.pagado
            FROM servicios
            INNER JOIN clientes ON servicios.id_cliente = clientes.id;
        """)
        self.model.select()
        self.model.setHeaderData(0, Qt.Horizontal, "Id")
        self.model.setHeaderData(1, Qt.Horizontal, "Cliente")
        self.model.setHeaderData(2, Qt.Horizontal, "Vehiculo")
        self.model.setHeaderData(3, Qt.Horizontal, "Descripcion")
        self.model.setHeaderData(4, Qt.Horizontal, "Precio")
        self.model.setHeaderData(5, Qt.Horizontal, "Total")
        self.model.setHeaderData(6, Qt.Horizontal, "Pagado")
    
        # Configura la tabla para usar el modelo
        self.serviciosTable.setModel(self.model)
        self.serviciosTable.hideColumn(0)  # Oculta la columna ID
        self.serviciosTable.hideColumn(3)  # Oculta la columna Precio
        self.serviciosTable.hideColumn(6)  # Oculta la columna Pagado
        self.serviciosTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.serviciosTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.serviciosTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.serviciosTable.setSelectionBehavior(QAbstractItemView.SelectRows)   

        self.btnFactura.clicked.connect(self.imprimir_factura1)
        self.serviciosTable.selectionModel().selectionChanged.connect(self.select_row)
        self.row = -1


    def select_row(self,selecction):
        if selecction.indexes():
            self.row = selecction.indexes()[0].row()

    def facturar(self):
        if self.row != -1:
            id_servicio = self.model.record(self.row).value("id")
            print("Facturar id:", id_servicio)
        else:
            print("No se seleccionó ningún servicio.")

    def imprimir_factura(self):
        if self.row != -1:
            # Obtén el registro del servicio
            record = self.model.record(self.row)

            # Recopila los detalles del servicio
            id_servicio = record.value("id")
            nombre_cliente = record.value("nombre")
            vehiculo = record.value("vehiculo")
            descripcion = record.value("descripcion")
            precio_total = record.value("precio_total")

            # Abre el diálogo de guardado de archivos
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getSaveFileName(self,"Guardar Factura","","PDF Files (*.pdf);;All Files (*)", options=options)

            if fileName:
                # Verifica si el nombre del archivo termina en .pdf y, si no, añade la extensión
                if not fileName.endswith('.pdf'):
                    fileName += '.pdf'

                # Crea un nuevo archivo PDF
                c = canvas.Canvas(fileName)

                # Escribe los detalles del servicio en el PDF
                c.drawString(300, 750, f"Factura de Servicio: ABN-{id_servicio}")
                c.drawString(80, 710, f"Nombre del Cliente: {nombre_cliente}")
                c.drawString(80, 690, f"Vehículo: {vehiculo}")
                c.drawString(80, 670, f"Descripción: {descripcion}")
                c.drawString(80, 650, f"Precio Total: {precio_total}")

                # Guarda el archivo PDF
                c.save()

                print(f"Factura guardada como {fileName}")
            else:
                print("No se seleccionó ningún servicio.")


    ###############################

    def imprimir_factura1(self):
        if self.row != -1:
            # Obtén el registro del servicio
            record = self.model.record(self.row)

            # Recopila los detalles del servicio
            id_servicio = record.value("id")
            nombre_cliente = record.value("nombre")
            vehiculo = record.value("vehiculo")
            descripcion = record.value("descripcion")
            precio = record.value("precio")
            precio_total = record.value("precio_total")

            # Abre el diálogo de guardado de archivos
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getSaveFileName(self,"Guardar Factura","","PDF Files (*.pdf);;All Files (*)", options=options)

            if fileName:
                # Verifica si el nombre del archivo termina en .pdf y, si no, añade la extensión
                if not fileName.endswith('.pdf'):
                    fileName += '.pdf'

                # Crea un nuevo archivo PDF
                pdf = SimpleDocTemplate(fileName, pagesize=letter)
                styles = getSampleStyleSheet()
                custom_style = ParagraphStyle(
                    'CustomStyle',
                    parent=styles['Normal'],
                    fontName='Helvetica',
                    fontSize=12,
                    spaceAfter=12,  # Espacio después del párrafo
                )

                # Crea un párrafo con el nombre del cliente
                
                titulo_factura = Paragraph(f"FACTURA DE SERVICIO: ABN{id_servicio}", custom_style)
                nombre_cliente_paragraph = Paragraph(f"CLIENTE: {nombre_cliente}", custom_style)

                cont_n = 2
                # Crea los datos de la tabla
                data = [
                    ["N#","        Detalle        ","  Cantidad  ","  Precio  ","  Subtotal  "],
                    ["1",descripcion,"1",precio,precio],
                ]
                # Realiza una consulta a la base de datos para obtener los productos/servicios
                query = QSqlQuery()
                query.prepare("""SELECT * FROM productos_servicio 
                                INNER JOIN productos ON productos_servicio.id_producto = productos.id
                                WHERE id_servicio =:id_servicio
                """)
                query.bindValue(":id_servicio", id_servicio)
                query.exec_()

                while query.next():
                    producto_servicio = query.value("descripcion")
                    cantidad = query.value("cantidad")
                    precio = query.value("precio")
                    subtotal = int(cantidad) * float(precio)
                    data.append([cont_n,producto_servicio,cantidad,precio,subtotal])
                    cont_n += 1

                data.append(["TOTAL","","","",precio_total])

                # Crea la tabla
                table = Table(data)

                # Aplica estilos a la tabla
                # style = TableStyle([
                #     ('BACKGROUND', (0,0), (-1,0), colors.grey),
                #     ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),

                #     ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                #     ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                #     ('FONTSIZE', (0,0), (-1,0), 14),

                #     ('BOTTOMPADDING', (0,0), (-1,0), 12),
                #     ('BACKGROUND', (0,1), (-1,-1), colors.white),
                #     ('GRID', (0,0), (-1,-1), 1, colors.black)
                # ])
                style = TableStyle([
                    ('BACKGROUND', (0,0), (-1,0), colors.white),  # Fondo blanco para la primera fila
                    ('TEXTCOLOR', (0,0), (-1,0), colors.grey),  # Texto gris para la primera fila

                    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0,0), (-1,0), 11),

                    ('BOTTOMPADDING', (0,0), (-1,0), 12),
                    ('BACKGROUND', (0,1), (-1,-1), colors.white),
                    ('GRID', (0,0), (-1,-1), 1, colors.grey),
                    ('LINEABOVE', (0,-1), (-1,-1), 2, colors.green),  # Línea verde encima de la última fila
                    ('LINEBELOW', (0,0), (-1,0), 2, colors.black)  # Línea más ancha debajo de la primera fila
                ])
                table.setStyle(style)

                # Guarda el archivo PDF
                pdf.build([titulo_factura,nombre_cliente_paragraph, table])

                print(f"Factura guardada como {fileName}")
        else:
            print("No se seleccionó ningún servicio.")

    

