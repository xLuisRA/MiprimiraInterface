import var


class Clientes:
    def validarDNI():
        try:
            dni = var.ui.textoDni.text()
            var.ui.textoDni(dni.upper())
            tabla = 'TRWAGMYFPDXBNJXSQVHLCKE'
            dig_ext ='XYZ'
            reemp_dig_ext ={'x':'0','y':'1','z':'2'}
            numeros = '1234567890'
            dni = dni.upper()
            if len(dni)== 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni)==len([n for n in dni if n in numeros]) and tabla [int(dni)%23] == dig_control:
                    var.ui.lblValidoDNI.setStyleSheet('QLabel{color:green;}')
                    var.ui.lblValidoDNI.setText('V')
                else:
                    var.ui.lblValidoDNI.setStyleSheet('QLabel{color:red;}')
                    var.ui.lblValidoDNI.setText('x')
            else:
                var.ui.lblValidoDNI.setStyleSheet('QLabel{color:red;}')
                var.ui.lblValidoDNI.setText('x')
        except Exception as error:
            print('Error en modulo validar DNI',error)

