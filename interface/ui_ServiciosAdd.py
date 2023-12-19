# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ServiciosAddEMzCBb.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import resources_rc
import resources_rc

class Ui_ServiciosAdd(object):
    def setupUi(self, ServiciosAdd):
        if not ServiciosAdd.objectName():
            ServiciosAdd.setObjectName(u"ServiciosAdd")
        ServiciosAdd.resize(703, 500)
        ServiciosAdd.setMinimumSize(QSize(0, 500))
        ServiciosAdd.setStyleSheet(u"*{\n"
"	border: none;\n"
"}\n"
"#dashboard{\n"
"	background-color: #eff9fe;\n"
"}\n"
"#cards QFrame{\n"
"	background-color: white;\n"
"	border-radius: 15px;\n"
"}\n"
"#frMain{\n"
"	background-color: white;\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit{\n"
"	background: white;\n"
"	border: 1px solid black;\n"
"	border-radius: 3px;\n"
"}\n"
"QPushButton{\n"
"	padding: 5px;\n"
"	border-radius: 5px;\n"
"	color:white;\n"
"	background: #0d6efd;\n"
"}\n"
"QPushButton:hover{\n"
"	background: #1e7fff;\n"
"}\n"
"#btnAddProduct{\n"
"	background: #198754;\n"
"}\n"
"#btnAddProduct:hover{\n"
"	background: #2A9865;\n"
"}\n"
"QComboBox{\n"
"	border: 1px solid black;\n"
"	border-radius: 3px;\n"
"}")
        self.verticalLayout = QVBoxLayout(ServiciosAdd)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main = QWidget(ServiciosAdd)
        self.main.setObjectName(u"main")
        self.horizontalLayout_15 = QHBoxLayout(self.main)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frMain = QFrame(self.main)
        self.frMain.setObjectName(u"frMain")
        self.frMain.setFrameShape(QFrame.StyledPanel)
        self.frMain.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frMain)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frameView = QFrame(self.frMain)
        self.frameView.setObjectName(u"frameView")
        self.frameView.setMinimumSize(QSize(300, 0))
        self.frameView.setMaximumSize(QSize(350, 16777215))
        self.frameView.setFrameShape(QFrame.StyledPanel)
        self.frameView.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frameView)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget = QWidget(self.frameView)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lblClientes = QLabel(self.frame)
        self.lblClientes.setObjectName(u"lblClientes")

        self.verticalLayout_3.addWidget(self.lblClientes)

        self.cbClientes = QComboBox(self.frame)
        self.cbClientes.setObjectName(u"cbClientes")

        self.verticalLayout_3.addWidget(self.cbClientes)

        self.lblMarca = QLabel(self.frame)
        self.lblMarca.setObjectName(u"lblMarca")

        self.verticalLayout_3.addWidget(self.lblMarca)

        self.leVehiculo = QLineEdit(self.frame)
        self.leVehiculo.setObjectName(u"leVehiculo")

        self.verticalLayout_3.addWidget(self.leVehiculo)

        self.lblDescripcion = QLabel(self.frame)
        self.lblDescripcion.setObjectName(u"lblDescripcion")

        self.verticalLayout_3.addWidget(self.lblDescripcion)

        self.leDescripcionServicio = QLineEdit(self.frame)
        self.leDescripcionServicio.setObjectName(u"leDescripcionServicio")

        self.verticalLayout_3.addWidget(self.leDescripcionServicio)

        self.lblPrecio = QLabel(self.frame)
        self.lblPrecio.setObjectName(u"lblPrecio")

        self.verticalLayout_3.addWidget(self.lblPrecio)

        self.lePrecio = QLineEdit(self.frame)
        self.lePrecio.setObjectName(u"lePrecio")

        self.verticalLayout_3.addWidget(self.lePrecio)


        self.verticalLayout_5.addWidget(self.frame)

        self.frame_5 = QFrame(self.widget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lblProductos = QLabel(self.frame_5)
        self.lblProductos.setObjectName(u"lblProductos")

        self.verticalLayout_9.addWidget(self.lblProductos)

        self.cbProductos = QComboBox(self.frame_5)
        self.cbProductos.setObjectName(u"cbProductos")

        self.verticalLayout_9.addWidget(self.cbProductos)

        self.lblCantidad = QLabel(self.frame_5)
        self.lblCantidad.setObjectName(u"lblCantidad")

        self.verticalLayout_9.addWidget(self.lblCantidad)

        self.leCantidad = QLineEdit(self.frame_5)
        self.leCantidad.setObjectName(u"leCantidad")

        self.verticalLayout_9.addWidget(self.leCantidad)

        self.btnAddProduct = QPushButton(self.frame_5)
        self.btnAddProduct.setObjectName(u"btnAddProduct")
        self.btnAddProduct.setMaximumSize(QSize(200, 16777215))
        self.btnAddProduct.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.btnAddProduct, 0, Qt.AlignRight)


        self.verticalLayout_5.addWidget(self.frame_5, 0, Qt.AlignTop)


        self.verticalLayout_4.addWidget(self.widget)


        self.horizontalLayout.addWidget(self.frameView)

        self.frameAdd = QFrame(self.frMain)
        self.frameAdd.setObjectName(u"frameAdd")
        self.frameAdd.setMinimumSize(QSize(250, 0))
        self.frameAdd.setMaximumSize(QSize(16777215, 16777215))
        self.frameAdd.setFrameShape(QFrame.StyledPanel)
        self.frameAdd.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frameAdd)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frameAdd)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.productosTable = QTableWidget(self.frame_3)
        self.productosTable.setObjectName(u"productosTable")

        self.verticalLayout_7.addWidget(self.productosTable)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.btnGuardar = QPushButton(self.frame_4)
        self.btnGuardar.setObjectName(u"btnGuardar")

        self.verticalLayout_8.addWidget(self.btnGuardar)


        self.verticalLayout_6.addWidget(self.frame_4)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.frameAdd)


        self.horizontalLayout_15.addWidget(self.frMain)


        self.verticalLayout.addWidget(self.main)


        self.retranslateUi(ServiciosAdd)

        QMetaObject.connectSlotsByName(ServiciosAdd)
    # setupUi

    def retranslateUi(self, ServiciosAdd):
        ServiciosAdd.setWindowTitle(QCoreApplication.translate("ServiciosAdd", u"Form", None))
        self.lblClientes.setText(QCoreApplication.translate("ServiciosAdd", u"Cliente", None))
        self.lblMarca.setText(QCoreApplication.translate("ServiciosAdd", u"Detalles del vehiculo", None))
        self.lblDescripcion.setText(QCoreApplication.translate("ServiciosAdd", u"Descripci\u00f3n del Servicio", None))
        self.lblPrecio.setText(QCoreApplication.translate("ServiciosAdd", u"Precio inicial del servio", None))
        self.lblProductos.setText(QCoreApplication.translate("ServiciosAdd", u"Producto", None))
        self.lblCantidad.setText(QCoreApplication.translate("ServiciosAdd", u"Cantidad", None))
        self.btnAddProduct.setText(QCoreApplication.translate("ServiciosAdd", u"A\u00f1adir Producto", None))
        self.btnGuardar.setText(QCoreApplication.translate("ServiciosAdd", u"Guardar", None))
    # retranslateUi

