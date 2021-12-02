import var
class Eventos():

    def Saludo():
        try:
            var.ui.label.setText('Has pulsado el buty')
        except Exception as error:
            print('Error: '%str(error))