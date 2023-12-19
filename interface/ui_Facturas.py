# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FacturasRjzFlH.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QPushButton, QSizePolicy, QTableView, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc
import resources_rc

class Ui_Facturas(object):
    def setupUi(self, Facturas):
        if not Facturas.objectName():
            Facturas.setObjectName(u"Facturas")
        Facturas.resize(703, 500)
        Facturas.setMinimumSize(QSize(0, 500))
        Facturas.setStyleSheet(u"*{\n"
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
        self.verticalLayout = QVBoxLayout(Facturas)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main = QWidget(Facturas)
        self.main.setObjectName(u"main")
        self.horizontalLayout_15 = QHBoxLayout(self.main)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frMain = QFrame(self.main)
        self.frMain.setObjectName(u"frMain")
        self.frMain.setFrameShape(QFrame.StyledPanel)
        self.frMain.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frMain)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frameAdd = QFrame(self.frMain)
        self.frameAdd.setObjectName(u"frameAdd")
        self.frameAdd.setMinimumSize(QSize(250, 0))
        self.frameAdd.setMaximumSize(QSize(16777215, 16777215))
        self.frameAdd.setFrameShape(QFrame.StyledPanel)
        self.frameAdd.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frameAdd)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.serviciosTable = QTableView(self.frameAdd)
        self.serviciosTable.setObjectName(u"serviciosTable")

        self.verticalLayout_2.addWidget(self.serviciosTable)

        self.serviciosTable1 = QTableWidget(self.frameAdd)
        self.serviciosTable1.setObjectName(u"serviciosTable1")

        self.verticalLayout_2.addWidget(self.serviciosTable1)

        self.btnFactura = QPushButton(self.frameAdd)
        self.btnFactura.setObjectName(u"btnFactura")

        self.verticalLayout_2.addWidget(self.btnFactura, 0, Qt.AlignRight)


        self.horizontalLayout.addWidget(self.frameAdd)


        self.horizontalLayout_15.addWidget(self.frMain)


        self.verticalLayout.addWidget(self.main)


        self.retranslateUi(Facturas)

        QMetaObject.connectSlotsByName(Facturas)
    # setupUi

    def retranslateUi(self, Facturas):
        Facturas.setWindowTitle(QCoreApplication.translate("Facturas", u"Form", None))
        self.btnFactura.setText(QCoreApplication.translate("Facturas", u"Imprimir factura", None))
    # retranslateUi

