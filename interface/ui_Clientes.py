# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ClientesMKpspr.ui'
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

class Ui_clientes(object):
    def setupUi(self, clientes):
        if not clientes.objectName():
            clientes.setObjectName(u"clientes")
        clientes.resize(703, 500)
        clientes.setMinimumSize(QSize(0, 500))
        clientes.setStyleSheet(u"*{\n"
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
        self.verticalLayout = QVBoxLayout(clientes)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main = QWidget(clientes)
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

        self.leNombre = QLineEdit(self.frame)
        self.leNombre.setObjectName(u"leNombre")

        self.verticalLayout_3.addWidget(self.leNombre)

        self.lblCi = QLabel(self.frame)
        self.lblCi.setObjectName(u"lblCi")

        self.verticalLayout_3.addWidget(self.lblCi)

        self.leCi = QLineEdit(self.frame)
        self.leCi.setObjectName(u"leCi")

        self.verticalLayout_3.addWidget(self.leCi)

        self.lblTel = QLabel(self.frame)
        self.lblTel.setObjectName(u"lblTel")

        self.verticalLayout_3.addWidget(self.lblTel)

        self.leTel = QLineEdit(self.frame)
        self.leTel.setObjectName(u"leTel")

        self.verticalLayout_3.addWidget(self.leTel)

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


        self.retranslateUi(clientes)

        QMetaObject.connectSlotsByName(clientes)
    # setupUi

    def retranslateUi(self, clientes):
        clientes.setWindowTitle(QCoreApplication.translate("clientes", u"Form", None))
        self.lblNombre.setText(QCoreApplication.translate("clientes", u"Nombre", None))
        self.lblCi.setText(QCoreApplication.translate("clientes", u"Carnet de Identidad", None))
        self.lblTel.setText(QCoreApplication.translate("clientes", u"Telefono", None))
        self.btnCreate.setText(QCoreApplication.translate("clientes", u"A\u00f1adir", None))
    # retranslateUi

