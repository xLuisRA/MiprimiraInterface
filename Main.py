from Ventana import *
import var,events

import sys

class Main(QtWidgets.QMainWindow):


    def  __init__(self):

        super(Main,self).__init__()
        var.ui = Ui_Dialog()
        var.ui.setupUi(self)

        var.ui.pushButton.clicked.connect(events.Eventos.Saludo)

if __name__=='__main__':
    app = QtWidgets.QApplication([])
    Window = Main()
    Window.show()
    sys.exit(app.exec())