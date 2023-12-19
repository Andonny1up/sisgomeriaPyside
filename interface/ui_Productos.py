# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProductosYLeFrj.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableView, QVBoxLayout, QWidget)
import resources_rc
import resources_rc

class Ui_Productos(object):
    def setupUi(self, Productos):
        if not Productos.objectName():
            Productos.setObjectName(u"Productos")
        Productos.resize(703, 500)
        Productos.setMinimumSize(QSize(0, 500))
        Productos.setStyleSheet(u"*{\n"
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
"}")
        self.verticalLayout = QVBoxLayout(Productos)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main = QWidget(Productos)
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
        self.frameView.setFrameShape(QFrame.StyledPanel)
        self.frameView.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frameView)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget = QWidget(self.frameView)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tableView = QTableView(self.widget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_5.addWidget(self.tableView)


        self.verticalLayout_4.addWidget(self.widget)


        self.horizontalLayout.addWidget(self.frameView)

        self.frameAdd = QFrame(self.frMain)
        self.frameAdd.setObjectName(u"frameAdd")
        self.frameAdd.setMinimumSize(QSize(250, 0))
        self.frameAdd.setMaximumSize(QSize(350, 16777215))
        self.frameAdd.setFrameShape(QFrame.StyledPanel)
        self.frameAdd.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frameAdd)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frameAdd)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lblNombre = QLabel(self.frame)
        self.lblNombre.setObjectName(u"lblNombre")

        self.verticalLayout_3.addWidget(self.lblNombre)

        self.leDescripcion = QLineEdit(self.frame)
        self.leDescripcion.setObjectName(u"leDescripcion")

        self.verticalLayout_3.addWidget(self.leDescripcion)

        self.lblMarca = QLabel(self.frame)
        self.lblMarca.setObjectName(u"lblMarca")

        self.verticalLayout_3.addWidget(self.lblMarca)

        self.leMarca = QLineEdit(self.frame)
        self.leMarca.setObjectName(u"leMarca")

        self.verticalLayout_3.addWidget(self.leMarca)

        self.lblPrecio = QLabel(self.frame)
        self.lblPrecio.setObjectName(u"lblPrecio")

        self.verticalLayout_3.addWidget(self.lblPrecio)

        self.lePrecio = QLineEdit(self.frame)
        self.lePrecio.setObjectName(u"lePrecio")

        self.verticalLayout_3.addWidget(self.lePrecio)

        self.btnCreate = QPushButton(self.frame)
        self.btnCreate.setObjectName(u"btnCreate")
        self.btnCreate.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btnCreate)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.frameAdd)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.frameAdd)


        self.horizontalLayout_15.addWidget(self.frMain)


        self.verticalLayout.addWidget(self.main)


        self.retranslateUi(Productos)

        QMetaObject.connectSlotsByName(Productos)
    # setupUi

    def retranslateUi(self, Productos):
        Productos.setWindowTitle(QCoreApplication.translate("Productos", u"Form", None))
        self.lblNombre.setText(QCoreApplication.translate("Productos", u"Nombre - Descripci\u00f3n", None))
        self.lblMarca.setText(QCoreApplication.translate("Productos", u"Marca - Modelo", None))
        self.lblPrecio.setText(QCoreApplication.translate("Productos", u"Precio", None))
        self.btnCreate.setText(QCoreApplication.translate("Productos", u"A\u00f1adir", None))
    # retranslateUi

