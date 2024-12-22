
import os


def menu():
    """
    Funcion que limpia la pantalla y muestra nuevamente el menu
    """
    os.system('clear') 
    titulo = (" Menu General ")
    print (titulo.center(50,'*'))
    print ('\n\n')
    print ("Selecciona una opcion")
    print ("\t1 - Primera opcion")
    print ("\t2 - Segunda opcion")
    print ("\t3 - Tercera opcion")
    print ("\t9 - salir")
    
def validar():
    while True:
         menu()
         
         opcionMenu = input("Inserta un numero valor >> ")
         
         if opcionMenu=="1":
             print("")
             input("Has pulsado la opcion 1...\npulsa una tecla para continuar")
         elif opcionMenu=="2":
             print("")
             input("Has pulsado la opcion 2...\npulsa una tecla para continuar")
         elif opcionMenu=="3": 
             print("")
             input("Has pulsado la opcion 3...\npulsa una tecla para continuar")
         elif opcionMenu=="9":
             break
         else:
             print("")
             input("No has pulsado ninguna opcion correcta...\npulsa una tecla para continuar")
    return opcionMenu

if __name__ == '__main__':
    validar()
    
    print('\tFINALIZO EL PROGRAMA!!!!!')