import sys

class Eventos:
    def salir():
        try:
            sys.exit()
        except Exception as error:
            print("Error %s: " % str(error))

