from Ventana import *
from Gestión import *
import var ,events,clientes

import sys

class Main(QtWidgets.QMainWindow):


    def  __init__(self):

        super(Main,self).__init__()
       #var.ui = Ui_Dialog()
        var.ui = Ui_Archivo()
        var.ui.setupUi(self)

        #var.ui.pushButton.clicked.connect(events.Eventos.Saludo)
        var.ui.actionSalir.triggered.connect(events.Eventos.salir)
        var.ui.textoDni.editingFinished.connect(clientes.Clientes.validarDNI())

if __name__=='__main__':
    app = QtWidgets.QApplication([])
    Window = Main()
    Window.show()
    sys.exit(app.exec())