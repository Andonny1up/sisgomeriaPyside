# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MenuPdMvXD.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 602)
        MainWindow.setMinimumSize(QSize(0, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	border: none;\n"
"}\n"
"#centralwidget{\n"
"	background-color: #eff9fe;\n"
"}\n"
"#leftMenu{\n"
"	background-color: #0d6efd;\n"
"}\n"
"#topMenu{\n"
"	background-color: #0d6efd ;\n"
"}\n"
"#lblNameAplication{\n"
"	color: white;\n"
"}\n"
"#frMenuButtons QPushButton{\n"
"	color: white;\n"
"	text-align: left;\n"
"	padding: 15px;\n"
"	padding-left:25px;\n"
"}\n"
"#frMenuButtons QPushButton:hover{\n"
"	background-color: #1e7fff;\n"
"}\n"
"#header{\n"
"	background-color: #FDFDFD;\n"
"}\n"
"#header #lblDashboard{\n"
"	color: #3838FF;\n"
"	background-color: white;\n"
"	border-radius: 12px;\n"
"	padding: 5px; \n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QWidget(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(270, 0))
        self.leftMenu.setMaximumSize(QSize(270, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frLeftMenu = QFrame(self.leftMenu)
        self.frLeftMenu.setObjectName(u"frLeftMenu")
        self.frLeftMenu.setFrameShape(QFrame.StyledPanel)
        self.frLeftMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frLeftMenu)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.topMenu = QWidget(self.frLeftMenu)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setMinimumSize(QSize(0, 78))
        self.topMenu.setMaximumSize(QSize(16777215, 78))
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(9, -1, -1, -1)
        self.frTopMenu = QFrame(self.topMenu)
        self.frTopMenu.setObjectName(u"frTopMenu")
        self.frTopMenu.setFrameShape(QFrame.StyledPanel)
        self.frTopMenu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frTopMenu)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lblNameAplication = QLabel(self.frTopMenu)
        self.lblNameAplication.setObjectName(u"lblNameAplication")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        self.lblNameAplication.setFont(font)
        self.lblNameAplication.setCursor(QCursor(Qt.ArrowCursor))
        self.lblNameAplication.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lblNameAplication.setMargin(0)

        self.horizontalLayout_3.addWidget(self.lblNameAplication)


        self.verticalLayout_8.addWidget(self.frTopMenu, 0, Qt.AlignLeft)


        self.verticalLayout_10.addWidget(self.topMenu)

        self.frMenuButtons = QFrame(self.frLeftMenu)
        self.frMenuButtons.setObjectName(u"frMenuButtons")
        self.frMenuButtons.setFrameShape(QFrame.StyledPanel)
        self.frMenuButtons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frMenuButtons)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btnInicio = QPushButton(self.frMenuButtons)
        self.btnInicio.setObjectName(u"btnInicio")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.btnInicio.setFont(font1)
        self.btnInicio.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnInicio.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.btnInicio)

        self.btnClientes = QPushButton(self.frMenuButtons)
        self.btnClientes.setObjectName(u"btnClientes")
        font2 = QFont()
        font2.setPointSize(12)
        self.btnClientes.setFont(font2)
        self.btnClientes.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnClientes.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.btnClientes)

        self.btnProductos = QPushButton(self.frMenuButtons)
        self.btnProductos.setObjectName(u"btnProductos")
        self.btnProductos.setFont(font2)
        self.btnProductos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnProductos.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.btnProductos)

        self.btnServicios = QPushButton(self.frMenuButtons)
        self.btnServicios.setObjectName(u"btnServicios")
        self.btnServicios.setFont(font2)
        self.btnServicios.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnServicios.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.btnServicios)


        self.verticalLayout_10.addWidget(self.frMenuButtons, 0, Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.frLeftMenu)


        self.horizontalLayout.addWidget(self.leftMenu)

        self.mainContainer = QWidget(self.centralwidget)
        self.mainContainer.setObjectName(u"mainContainer")
        self.verticalLayout = QVBoxLayout(self.mainContainer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.mainContainer)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 0))
        self.header.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.menuButton = QWidget(self.header)
        self.menuButton.setObjectName(u"menuButton")
        self.horizontalLayout_4 = QHBoxLayout(self.menuButton)
        self.horizontalLayout_4.setSpacing(12)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btnMenu = QPushButton(self.menuButton)
        self.btnMenu.setObjectName(u"btnMenu")
        self.btnMenu.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icon-black/assets/icon_black/align-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnMenu.setIcon(icon)
        self.btnMenu.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.btnMenu)


        self.horizontalLayout_2.addWidget(self.menuButton, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.header)

        self.layoutContainer = QVBoxLayout()
        self.layoutContainer.setObjectName(u"layoutContainer")
        self.widgetIInicio = QWidget(self.mainContainer)
        self.widgetIInicio.setObjectName(u"widgetIInicio")

        self.layoutContainer.addWidget(self.widgetIInicio)


        self.verticalLayout.addLayout(self.layoutContainer)


        self.horizontalLayout.addWidget(self.mainContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Gomeria", None))
        self.lblNameAplication.setText(QCoreApplication.translate("MainWindow", u"Gomeria", None))
        self.btnInicio.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.btnClientes.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.btnProductos.setText(QCoreApplication.translate("MainWindow", u"Productos", None))
        self.btnServicios.setText(QCoreApplication.translate("MainWindow", u"Servicios", None))
        self.btnMenu.setText("")
    # retranslateUi

