#libreria del sistema operativo
import os

def menu():
    """
    Función que limpia la pantalla y muestra nuevamente el menu
    """ 
    
    os.system('clear') # Borra pantalla en un terminal, en Jupyter no funciona
    titulo = (" Menú General ")
    print (titulo.center(50,'*'))
    print ('\n\n')
    print ("Selecciona una Opción")
    print ("\t1 ­ Primera Opción")
    print ("\t2 ­ Segunda Opción")
    print ("\t3 ­ Tercera Opción")
    print ("\t9 ­ salir")

def validar():
    while True:
        # Mostramos el menu
        menu()
        
        # solicituamos una opción al usuario
        opcionMenu = input("inserta un numero valor >> ")
        
        if opcionMenu=="1":
            print ("")
            input("Has pulsado la opción 1...\npulsa una tecla para continuar")
        elif opcionMenu=="2":
            print ("")
            input("Has pulsado la opción 2...\npulsa una tecla para continuar")
        elif opcionMenu=="3":
            print ("")
            input("Has pulsado la opción 3...\npulsa una tecla para continuar")
        elif opcionMenu=="9":
            break
        else:
            print ("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
    return opcionMenu
if __name__ == '__main__':
    validar()
    print('\tFINALIZO EL PROGRAMA!!!!!')
