import os
import sys
#funcion para limpiar la pantalla se usa para que sirva tanto en windows como en linux y mac
def limpiar_p():
    if sys.platform == 'linux' or sys.platform == 'darwin':
        os.system('clear')
    else:
        os.system('cls')
#funcion para pausar pantalla, sirve en todos los sistemas operativos
def pausar_p():
    if sys.platform == 'linux' or sys.platform == 'darwin':
        x = input('Presione enter para continuar ')
    else:
        os.system('pause')
#funcion para validar el tipo, sirve para validar enteros y flotantes, sigue pidiendo el valor
#hasta que el usuario ingresa correctamente el tipo de dato
def validartipo(tipo,msg):
    match tipo:
        case 'int':
            try:
                x = int(input(msg))
            except Exception:
                print('El valor ingresado no es un numero entero')
                pausar_p()
                return validartipo(tipo,msg)
            else:
                limpiar_p()
                return x
        case 'float':
            try:
                x = float(input(msg))
            except Exception:
                print('El valor ingresado no es float')
                pausar_p()
                return validartipo(tipo,msg)
            else:
                limpiar_p()
                return x
        case 'alpha':
            x = input(msg)
            if x.isalpha() == False:
                print('No puedes ingresar numeros')
                pausar_p()
                return validartipo(tipo,msg)