```python
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

```

    [H[2J****************** Menú General ******************
    
    
    
    Selecciona una Opción
    	1 ­ Primera Opción
    	2 ­ Segunda Opción
    	3 ­ Tercera Opción
    	9 ­ salir


    inserta un numero valor >>  &/%&/%/&%


    


    No has pulsado ninguna opción correcta...
    pulsa una tecla para continuar 


    [H[2J****************** Menú General ******************
    
    
    
    Selecciona una Opción
    	1 ­ Primera Opción
    	2 ­ Segunda Opción
    	3 ­ Tercera Opción
    	9 ­ salir


    inserta un numero valor >>  1248545315


    


    No has pulsado ninguna opción correcta...
    pulsa una tecla para continuar 


    [H[2J****************** Menú General ******************
    
    
    
    Selecciona una Opción
    	1 ­ Primera Opción
    	2 ­ Segunda Opción
    	3 ­ Tercera Opción
    	9 ­ salir


    inserta un numero valor >>  eerrqqwqw


    


    No has pulsado ninguna opción correcta...
    pulsa una tecla para continuar 


    [H[2J****************** Menú General ******************
    
    
    
    Selecciona una Opción
    	1 ­ Primera Opción
    	2 ­ Segunda Opción
    	3 ­ Tercera Opción
    	9 ­ salir


    inserta un numero valor >>  1


    


    Has pulsado la opción 1...
    pulsa una tecla para continuar 


    ****************** Menú General ******************
    
    
    
    Selecciona una Opción
    	1 ­ Primera Opción
    	2 ­ Segunda Opción
    	3 ­ Tercera Opción
    	9 ­ salir
    [H[2J

    inserta un numero valor >>  3


    


    Has pulsado la opción 3...
    pulsa una tecla para continuar 9


    [H[2J****************** Menú General ******************
    
    
    
    Selecciona una Opción
    	1 ­ Primera Opción
    	2 ­ Segunda Opción
    	3 ­ Tercera Opción
    	9 ­ salir


    inserta un numero valor >>  9


    	FINALIZO EL PROGRAMA!!!!!



```python

```
