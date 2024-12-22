#validar ingreso de numero eneteros
while True:
    try:
        x = int(input('Ingresar numero: '))
        break
    except ValueError:
        print('Error!!! no es un numero valido ')



#Validar ingreso de numeros enteros positivos
while True:
    try:
        x = int(input('Ingresar un numero positivo:'))
    except ValueError:
        print('Error !!! no es un numero postivo valido ')
        continue
    if x < 0:
        print('\t Por favor numero positivo')
        continue
    break
        


#Inicio mis programas con varias funciones
def uno():
    print('Inicio de Programa')

def dos():
    pass

def fin():
    print('\n\n\n Fin del programa')


#Programa Main principal
if __name__=='__main__':
    uno()
    dos()
    uno()
    dos()
    fin()
    
    
    
    
#Mi primera funcion validar dni
def validar_dni():
    while True:
        try:
            dni = int(input('Ingresar DNI: '))
            if len(str(dni)) == 8:
                print('\n\tDNI VALIDO')
                break
            else:
                print('\tError!Longitud de DNI no valido')
                continue
        except ValueError:
            print('\tError!!! No es un DNI Valido ... Intente de Nuevo')
    return dni


#Programa MAIN principal
if __name__ == '__main__':
    titulo = ('BONO FAMILIAR UNIVERSAL   ')
    print (titulo.center(50,'*'))
    print('\n\n')


    val_dni = validar_dni()

    print('\n\n EL DNI INGRESADO es: ==>',val_dni)  