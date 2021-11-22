from Ventana import *


import sys

class Main(QtWidgets.QMainWindow):


    def  __init__(self):

        super(Main,self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)



if __name__=='__main__':
    app = QtWidgets.QApplication([])
    Window = Main()
    Window.show()
    sys.exit(app.exec())