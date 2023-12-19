import sys
from PySide6.QtWidgets import QApplication,QMainWindow, QMessageBox
from interface.ui_Menu import Ui_MainWindow
from logic.l_Clientes import WidgetClientes
from logic.l_Productos import WidgetProductos
from logic.l_ServicioAdd import WidgetServiciosAdd

class MainWindow(QMainWindow,Ui_MainWindow):
    
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        # Events
        self.btnMenu.clicked.connect(self.toggle_left_menu)
        # self.btnInicio.clicked.connect(self.clicked_btn_inicio)
        self.btnClientes.clicked.connect(self.clicked_btn_clientes)
        self.btnProductos.clicked.connect(self.clicked_btn_productos)
        self.btnServicios.clicked.connect(self.clicked_btn_servicios)

    #Funtions Events
    def toggle_left_menu(self):
        self.leftMenu.setHidden(not self.leftMenu.isHidden())


    def clicked_btn_clientes(self):
        self.destroy_content()
        self.layoutContainer.addWidget(WidgetClientes())

    
    def clicked_btn_productos(self):
        self.destroy_content()
        self.layoutContainer.addWidget(WidgetProductos())

    
    def clicked_btn_servicios(self):
        self.destroy_content()
        self.layoutContainer.addWidget(WidgetServiciosAdd())
    

    def destroy_content(self):
        # Eliminar el contenido actual
        while self.layoutContainer.count():
            item = self.layoutContainer.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)
                widget.deleteLater()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())