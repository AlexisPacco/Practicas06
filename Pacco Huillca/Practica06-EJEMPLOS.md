```python
##Hacer un programa que imprima un menu de opciones y que valide correctamente los ingresos:

#libreria del sistema operativo
import os

def menu():
    """
    Funcion que limpia la pantalla y muestra nuevamente el menu
    """
    #borra pantalla en un terminal
    os.system('clear')
    titulo = ("   Menu General   ")
    print(titulo.center(50,'*'))
    print('\n\n')
    print("Selecciona una Opcion")
    print("\t1 - Primera Opcion")
    print("\t2 - Segunda Opcion")
    print("\t3 - Tercera Opcion")
    print("\t9 - Salir")


def validar():
    while True:
        #mostramos el menu
        menu()

        #solicitamos una opcion al usuario
        opcionMenu = input("inserta un numero valor >> ")

        if opcionMenu == "1":
            print("")
            input("Has pulsado la opcion 1...\npulsa una tecla para continuar")
        elif opcionMenu == "2":
            print("")
            input("Has pulsado la opcion 2...\npulsa una tecla para continuar")
        elif opcionMenu == "3":
            print("")
            input("Has pulsado la opcion 3...\npulsa una tecla para continuar")
        elif opcionMenu == "9":
            break
        else:
            print("")
            input("No has pulsado ninguna opcion correcta...\npulsa una tecla para continuar")
    return opcionMenu

if __name__ == '__main__':
    validar()
    print('\tFINALIZO EL PROGRAMA!!!')


```

    ****************   Menu General   ****************
    
    
    
    Selecciona una Opcion
    	1 - Primera Opcion
    	2 - Segunda Opcion
    	3 - Tercera Opcion
    	9 - Salir
    [H[2J

    inserta un numero valor >>  "#$"#$


    


    No has pulsado ninguna opcion correcta...
    pulsa una tecla para continuar 


    [H[2J****************   Menu General   ****************
    
    
    
    Selecciona una Opcion
    	1 - Primera Opcion
    	2 - Segunda Opcion
    	3 - Tercera Opcion
    	9 - Salir


    inserta un numero valor >>  qwrqweqwr


    


    No has pulsado ninguna opcion correcta...
    pulsa una tecla para continuar 


    ****************   Menu General   ****************
    
    
    
    Selecciona una Opcion
    	1 - Primera Opcion
    	2 - Segunda Opcion
    	3 - Tercera Opcion
    	9 - Salir
    [H[2J

    inserta un numero valor >>  1


    


    Has pulsado la opcion 1...
    pulsa una tecla para continuar 


    [H[2J****************   Menu General   ****************
    
    
    
    Selecciona una Opcion
    	1 - Primera Opcion
    	2 - Segunda Opcion
    	3 - Tercera Opcion
    	9 - Salir


    inserta un numero valor >>  


    


    No has pulsado ninguna opcion correcta...
    pulsa una tecla para continuar 3


    [H[2J****************   Menu General   ****************
    
    
    
    Selecciona una Opcion
    	1 - Primera Opcion
    	2 - Segunda Opcion
    	3 - Tercera Opcion
    	9 - Salir


    inserta un numero valor >>  


    


    No has pulsado ninguna opcion correcta...
    pulsa una tecla para continuar 


    [H[2J****************   Menu General   ****************
    
    
    
    Selecciona una Opcion
    	1 - Primera Opcion
    	2 - Segunda Opcion
    	3 - Tercera Opcion
    	9 - Salir


    inserta un numero valor >>  9


    	FINALIZO EL PROGRAMA!!!



```python

```
