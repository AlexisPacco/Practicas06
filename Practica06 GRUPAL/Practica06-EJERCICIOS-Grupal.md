```python
##Hacer un programa que imprima en pantalla un menu "Numeros Pares e Impares" con opciones:

#funcion para ingresar los numeros de inicio y fin
def ingresar_rango():
    while True:
        try:
            inicio = int(input("Ingrese el numero de inicio del rango: "))
            fin =  int(input("Ingrese el numero de fin del rango: "))
            if inicio > fin:
                print("El inicio debe ser menor que el fin... Intente de nuevo")
                continue
            return inicio, fin
        except ValueError:
            print("Por favor, ingrese solo numeros enteros")

#funcion para imprimir los numeros pares
def imprimir_pares(inicio, fin):
    pares = [num for num in range(inicio, fin + 1) if num % 2 == 0]
    print("Numeros pares: ",pares)

#funcion para imprimir los numeros impares
def imprimir_impares(inicio, fin):
    impares = [num for num in range(inicio, fin + 1) if num % 2 != 0]
    print("Numeros impares: ", impares)

#funcion para verificar si es numero primo
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) +1):
        if num % i == 0:
            return False
    return True

#funcion para imprimir los numeros primos
def imprimir_primos(inicio, fin):
    primos = [num for num in range(inicio, fin + 1) if es_primo(num)]
    print("Numeros primos: ", primos)

#funcion principal
def F_principal():
    titulo = ("   Numeros Pares, Impares y Primos   ")
    print(titulo.center(50, '*'))
    print('\n\n')
    while True:
        print("Seleccione una opcion:")
        print("\t1. Ingresar numeros de inicio y fin del rango")
        print("\t2. Imprimir los numeros pares del rango")
        print("\t3. Imprimir los numeros impares del rango")
        print("\t4. Imprimir los numeros primos del rango")
        print("\t5. Salir")

        try:
            opcion = int(input("Seleccionaste la opcion: "))
            if opcion == 1:
                inicio, fin = ingresar_rango()
            elif opcion == 2:
                imprimir_pares(inicio, fin)
            elif opcion == 3:
                imprimir_impares(inicio, fin)
            elif opcion == 4:
                imprimir_primos(inicio, fin)
            elif opcion == 5:
                print("SALIENDO DEL PROGRAMA...")
                break
            else:
                print("Opcion no valida, intente de nuevo")
        except UnboundLocalError:
            print("Debe ingresar un rango primero (opcion 1)")
        except ValueError:
            print("Por favor, ingrese una opcion valida")

#llamar a la funcion principal
if __name__ == '__main__':
    F_principal()
    print("FINALIZO EL PROGRAMA")

```

    ******   Numeros Pares, Impares y Primos   *******
    
    
    
    Seleccione una opcion:
    	1. Ingresar numeros de inicio y fin del rango
    	2. Imprimir los numeros pares del rango
    	3. Imprimir los numeros impares del rango
    	4. Imprimir los numeros primos del rango
    	5. Salir


    Seleccionaste la opcion:  1
    Ingrese el numero de inicio del rango:  1
    Ingrese el numero de fin del rango:  10


    Seleccione una opcion:
    	1. Ingresar numeros de inicio y fin del rango
    	2. Imprimir los numeros pares del rango
    	3. Imprimir los numeros impares del rango
    	4. Imprimir los numeros primos del rango
    	5. Salir


    Seleccionaste la opcion:  2


    Numeros pares:  [2, 4, 6, 8, 10]
    Seleccione una opcion:
    	1. Ingresar numeros de inicio y fin del rango
    	2. Imprimir los numeros pares del rango
    	3. Imprimir los numeros impares del rango
    	4. Imprimir los numeros primos del rango
    	5. Salir


    Seleccionaste la opcion:  3


    Numeros impares:  [1, 3, 5, 7, 9]
    Seleccione una opcion:
    	1. Ingresar numeros de inicio y fin del rango
    	2. Imprimir los numeros pares del rango
    	3. Imprimir los numeros impares del rango
    	4. Imprimir los numeros primos del rango
    	5. Salir


    Seleccionaste la opcion:  4


    Numeros primos:  [2, 3, 5, 7]
    Seleccione una opcion:
    	1. Ingresar numeros de inicio y fin del rango
    	2. Imprimir los numeros pares del rango
    	3. Imprimir los numeros impares del rango
    	4. Imprimir los numeros primos del rango
    	5. Salir


    Seleccionaste la opcion:  5


    SALIENDO DEL PROGRAMA...
    FINALIZO EL PROGRAMA



```python
##Hacer un programa que imprima en pantalla menu "Tabla de Multiplicar" con opciones de ingreso, impirmir y salir

#funcion para ingresar el rango de los numeros
def ingresar_rango():
    while True:
        try:
            inicio = int(input("Ingrese el numero inicio del rango: "))
            fin = int(input("Ingrese el numero fin del rango: "))
            if inicio > fin:
                print("El inicio debe ser menor que el fin... Intente de nuevo")
                continue
            return inicio, fin
        except ValueError:
            print("Por favor, ingrese solo numeros enteros")

#funcion para imprimir las tablas de multiplicar de los numeros pares del rango
def tabla_pares(inicio, fin):
    print("Tablas de multiplicar de los numeros pares en el rango: ")
    for num in range(inicio, fin + 1):
        if num % 2 == 0:
            print(f'\nTabla del {num}:')
            for i in range(1, 11):
                print(f'{num} x {i} = {num * i}')

#funcion para imprimir las tablas de multiplicar de los numeros impares del rango
def tabla_impares(inicio, fin):
    print("Tablas de multiplicar de los numeros impares en el rango: ")
    for num in range(inicio, fin + 1):
        if num % 2 != 0:
            print(f'\nTabla del {num}:')
            for i in range(1, 11):
                print(f'{num} x {i} = {num * i}')

#funcion para imprimir la tabla de multiplicar de un solo numero
def tabla_individual():
    while True:
        try:
            numero = int(input("Ingrese el numero para imprimir su tabla de multiplicar: "))
            print(f'\nTabla del {numero}:')
            for i in range(1, 11):
                print(f'{numero} x {i} = {numero * i}')
            break
        except ValueError:
            print("Por favor, ingrese un numero valido")

#funcion principal
def F_principal():
    titulo = ("   Tabla de Multiplicar   ")
    print(titulo.center(50, '*'))
    print('\n')
    while True:
        print("Seleccione una opcion")
        print("1. Ingresar rango de numeros")
        print("2. Imprimir tabla de multiplicar solo de numeros pares del rango")
        print("3. Imprimir tabla de multiplicar solo de numeros impares del rango")
        print("4. Ingrese un numero para imprimir su tabla de multiplicar")
        print("5. Salir")

        try:
            opcion = int(input("Seleccionaste la opcion: "))

            if opcion == 1:
                inicio, fin = ingresar_rango()
            elif opcion == 2:
                tabla_pares(inicio, fin)
            elif opcion == 3:
                tabla_impares(inicio, fin)
            elif opcion == 4:
                tabla_individual()
            elif opcion == 5:
                print("Saliendo del programa...")
                break
            else:
                print("Opcion no valida, intente de nuevo...")
        except UnboundLocalError:
            print("Debe ingresar un rango primero (opcion 1)")
        except ValueError:
            print("Por favor, ingrese una opcion valida")

#llamar a la funcion principal
if __name__ == '__main__':
    F_principal()
    print("FINALIZÓ EL PROGRAMA")

```

    ************   Tabla de Multiplicar   ************
    
    
    Seleccione una opcion
    1. Ingresar rango de numeros
    2. Imprimir tabla de multiplicar solo de numeros pares del rango
    3. Imprimir tabla de multiplicar solo de numeros impares del rango
    4. Ingrese un numero para imprimir su tabla de multiplicar
    5. Salir


    Seleccionaste la opcion:  1
    Ingrese el numero inicio del rango:  1
    Ingrese el numero fin del rango:  3


    Seleccione una opcion
    1. Ingresar rango de numeros
    2. Imprimir tabla de multiplicar solo de numeros pares del rango
    3. Imprimir tabla de multiplicar solo de numeros impares del rango
    4. Ingrese un numero para imprimir su tabla de multiplicar
    5. Salir


    Seleccionaste la opcion:  2


    Tablas de multiplicar de los numeros pares en el rango: 
    
    Tabla del 2:
    2 x 1 = 2
    2 x 2 = 4
    2 x 3 = 6
    2 x 4 = 8
    2 x 5 = 10
    2 x 6 = 12
    2 x 7 = 14
    2 x 8 = 16
    2 x 9 = 18
    2 x 10 = 20
    Seleccione una opcion
    1. Ingresar rango de numeros
    2. Imprimir tabla de multiplicar solo de numeros pares del rango
    3. Imprimir tabla de multiplicar solo de numeros impares del rango
    4. Ingrese un numero para imprimir su tabla de multiplicar
    5. Salir


    Seleccionaste la opcion:  3


    Tablas de multiplicar de los numeros impares en el rango: 
    
    Tabla del 1:
    1 x 1 = 1
    1 x 2 = 2
    1 x 3 = 3
    1 x 4 = 4
    1 x 5 = 5
    1 x 6 = 6
    1 x 7 = 7
    1 x 8 = 8
    1 x 9 = 9
    1 x 10 = 10
    
    Tabla del 3:
    3 x 1 = 3
    3 x 2 = 6
    3 x 3 = 9
    3 x 4 = 12
    3 x 5 = 15
    3 x 6 = 18
    3 x 7 = 21
    3 x 8 = 24
    3 x 9 = 27
    3 x 10 = 30
    Seleccione una opcion
    1. Ingresar rango de numeros
    2. Imprimir tabla de multiplicar solo de numeros pares del rango
    3. Imprimir tabla de multiplicar solo de numeros impares del rango
    4. Ingrese un numero para imprimir su tabla de multiplicar
    5. Salir


    Seleccionaste la opcion:  4
    Ingrese el numero para imprimir su tabla de multiplicar:  5


    
    Tabla del 5:
    5 x 1 = 5
    5 x 2 = 10
    5 x 3 = 15
    5 x 4 = 20
    5 x 5 = 25
    5 x 6 = 30
    5 x 7 = 35
    5 x 8 = 40
    5 x 9 = 45
    5 x 10 = 50
    Seleccione una opcion
    1. Ingresar rango de numeros
    2. Imprimir tabla de multiplicar solo de numeros pares del rango
    3. Imprimir tabla de multiplicar solo de numeros impares del rango
    4. Ingrese un numero para imprimir su tabla de multiplicar
    5. Salir


    Seleccionaste la opcion:  5


    Saliendo del programa...
    FINALIZÓ EL PROGRAMA



```python
##Hacer un programa que imprima en pantalla menu "Numeros Capicúa" con opciones de ingreso, imprimir y salir

#funcion para ingresar un rango de numeros
def ingresar_rango():
    while True:
        try:
            inicio = int(input("Ingrese el numero de inicio del rango: "))
            fin = int(input("Ingrese el numero de fin del rango: "))
            #limitar el rango a 4 cifras
            if inicio < 10 or fin > 9999 or inicio > fin:
                print("Por favor ingrese un rango valido (Hasta 4 cifras)")
                print("Asegurese de que el inicio sea menor que el fin")
                continue
            return inicio, fin
        except ValueError:
            print("Por favor, ingrese solo numeros enteros")

#funcion para verificar si un numero es capicúa
def es_capicua(num):
    return str(num) == str(num)[::-1]

#funcion para imprimir los numeros capicúa de dos cifras en el rango
def imprimir_capicua_dos_cifras(inicio, fin):
    print("Numeros capicua de dos cifras en el rango:")
    for num in range(inicio,fin + 1):
        if 10 <= num <= 99 and es_capicua(num):
            print(num)

#funcion para imprimir los numeros capicua de tres cifras en el rango
def imprimir_capicua_tres_cifras(inicio, fin):
    print("Numeros capicua de tres crifras en el rango:")
    for num in range(inicio, fin + 1):
        if 100 <= num <= 999 and es_capicua(num):
            print(num)

#funcion principal que controla el menu
def menu():
    titulo = ("   Numeros Capicua   ")
    print(titulo.center(50, '*'))
    print('\n')
    while True:
        print("Seleccione una opcion")
        print("\t1. Ingresar un rango de numeros de hasta 4 cifras")
        print("\t2. Imprimir numeros capicua de dos cifras del rango")
        print("\t3. Imprimir numeros capicua de tres cifras del rango")
        print("\t4. Salir")

        try:
            opcion = int(input("Seleccionaste la opcion: "))

            if opcion == 1:
                inicio, fin = ingresar_rango()
            elif opcion == 2:
                imprimir_capicua_dos_cifras(inicio, fin)
            elif opcion == 3:
                imprimir_capicua_tres_cifras(inicio, fin)
            elif opcion == 4:
                print("Saliendo del programa...")
                break
            else:
                print("Opcion no valida... Intente de nuevo")
        except UnboundLocalError:
            print("Debe ingresar un rango primero (opcion 1)")
        except ValueError:
            print("Por favor, ingrese una opcion valida")

#llamar a la funcion principal
if __name__ == '__main__':
    menu()
    print("FINALIZÓ EL PROGRAMA")             
    
```

    **************   Numeros Capicua   ***************
    
    
    Seleccione una opcion
    	1. Ingresar un rango de numeros de hasta 4 cifras
    	2. Imprimir numeros capicua de dos cifras del rango
    	3. Imprimir numeros capicua de tres cifras del rango
    	4. Salir


    Seleccionaste la opcion:  10


    Opcion no valida... Intente de nuevo
    Seleccione una opcion
    	1. Ingresar un rango de numeros de hasta 4 cifras
    	2. Imprimir numeros capicua de dos cifras del rango
    	3. Imprimir numeros capicua de tres cifras del rango
    	4. Salir


    Seleccionaste la opcion:  1
    Ingrese el numero de inicio del rango:  10
    Ingrese el numero de fin del rango:  999


    Seleccione una opcion
    	1. Ingresar un rango de numeros de hasta 4 cifras
    	2. Imprimir numeros capicua de dos cifras del rango
    	3. Imprimir numeros capicua de tres cifras del rango
    	4. Salir


    Seleccionaste la opcion:  2


    Numeros capicua de dos cifras en el rango:
    11
    22
    33
    44
    55
    66
    77
    88
    99
    Seleccione una opcion
    	1. Ingresar un rango de numeros de hasta 4 cifras
    	2. Imprimir numeros capicua de dos cifras del rango
    	3. Imprimir numeros capicua de tres cifras del rango
    	4. Salir


    Seleccionaste la opcion:  3


    Numeros capicua de tres crifras en el rango:
    101
    111
    121
    131
    141
    151
    161
    171
    181
    191
    202
    212
    222
    232
    242
    252
    262
    272
    282
    292
    303
    313
    323
    333
    343
    353
    363
    373
    383
    393
    404
    414
    424
    434
    444
    454
    464
    474
    484
    494
    505
    515
    525
    535
    545
    555
    565
    575
    585
    595
    606
    616
    626
    636
    646
    656
    666
    676
    686
    696
    707
    717
    727
    737
    747
    757
    767
    777
    787
    797
    808
    818
    828
    838
    848
    858
    868
    878
    888
    898
    909
    919
    929
    939
    949
    959
    969
    979
    989
    999
    Seleccione una opcion
    	1. Ingresar un rango de numeros de hasta 4 cifras
    	2. Imprimir numeros capicua de dos cifras del rango
    	3. Imprimir numeros capicua de tres cifras del rango
    	4. Salir


    Seleccionaste la opcion:  4


    Saliendo del programa...
    FINALIZÓ EL PROGRAMA



```python
##Hacer un programa que imprima en pantalla un menu de "Datos del Postulante" que solicite sus datos para ingresar

#funcion para validar el nombre y apellido
def validar_nombre_apellido(cadena):
    #sin numeros ni simbolos extraños
    if all(caracter.isalpha() or caracter.isspace() for caracter in cadena):
        return True
    return False

#funcion para validar el DNI
def validar_dni(dni):
    #solo numeros
    return dni.isdigit() and len(dni) == 8

#funcion para validar el numero de celular 
def validar_celular(celular):
    #solo numeros y limitarlo a 9 digitos
    return celular.isdigit() and len(celular) == 9

#funcion para validar la altura
def validar_altura(altura):
    try:
        altura = float(altura)
        #solo numeros positivos
        return altura > 0
    except ValueError:
        return False

#funcion par avalidar el peso
def validar_peso(peso):
    try:
        peso =float(peso)
        #solo numeros positivos
        return peso > 0
    except ValueError:
        return False

#funcion para ingresar los datos del postulante
def ingresar_datos():
    datos = {}

    #nombre
    while True:
        nombre = input("Ingresar el nombre del postulante: ")
        if validar_nombre_apellido(nombre):
            datos['nombre'] = nombre
            break
        else:
            print("Nombre invalido... Solo puede contener letras")

    #apellido
    while True:
        apellido = input("Ingresar el apellido del postulante: ")
        if validar_nombre_apellido(apellido):
            datos['Apellido'] = apellido
            break
        else:
            print("Apellido invalido... Solo puede contener letras")

    #DNI
    while True:
        dni = input("Ingrese el DNI del postulante (8 digitos): ")
        if validar_dni(dni):
            datos['DNI'] = dni
            break
        else:
            print("DNI invalido... Debe tener 8 digitos numericos")

    #celular 1
    while True:
        celular1 = input("Ingrese el primer numero de celular (9 digitos): ")
        if validar_celular(celular1):
            datos['Celular 1'] = celular1
            break
        else:
            print("Numero de celular invalido... Debe tener 9 digitos numericos")

    #celular 2
    while True:
        celular2 = input("Ingrese el segundo numero de celular (9 digitos): ")
        if validar_celular(celular2):
            datos['Celular 2'] = celular2
            break
        else:
            print("Numero de celular invalido... Debe tener 9 digitos numericos")

    #altura
    while True:
        altura = input("Ingrese la altura del postulante (en metros): ")
        if validar_altura(altura):
            datos['Altura'] = altura
            break
        else:
            print("Altura invalida... Debe ser un numero positivo")

    #peso
    while True:
        peso = input("Ingrese el peso del postulante (en Kg): ")
        if validar_peso(peso):
            datos['Peso'] = peso
            break
        else:
            print("Peso invalido... Debe ser un numero positivo")

    return datos

#funcion para imprimir los datos colocados
def imprimir_datos(datos):
    print("\nDatos del Postulante:")
    for clave, valor in datos.items():
        print(f'{clave}: {valor}')

#funcion principal que controla el menu
def menu():
    datos_postulante = {}
    titulo = ("   Datos del Postulante   ")
    print(titulo.center(50, '*'))
    print('\n')
    while True:
        print("Seleccione una opcion")
        print("\t1. Ingresar nombre")
        print("\t2. Ingresar apellido")
        print("\t3. Ingresar DNI")
        print("\t4. Ingresar celular 1")
        print("\t5. Ingresar celular 2")
        print("\t6. Ingresar altura")
        print("\t7. Ingresar peso")
        print("8. Imprimir los datos ingresados del postulante")
        print("9. Salir")

        try:
            opcion = int(input("Seleccione una opcion: "))

            if opcion == 1:
                datos_postulante['Nombre'] = input("Ingrese el nombre: ")
            elif opcion == 2:
                datos_postulante['Apellido'] = input("Ingrese el apellido: ")
            elif opcion == 3:
                datos_postulante['DNI'] = input("Ingrese el DNI: ")
            elif opcion == 4:
                datos_postulante['Celular 1'] = input("Ingrese el primer numero de celular: ")
            elif opcion == 5:
                datos_postulante['Celular 2'] = input("Ingrese el segundo numero de celular: ")
            elif opcion == 6:
                datos_postulante['Altura'] = input("Ingrese la altura: ")
            elif opcion == 7:
                datos_postulante['Peso'] = input("Ingrese el peso: ")
            elif opcion == 8:
                imprimir_datos(datos_postulante)
            elif opcion == 9:
                print("Saliendo del programa...")
                break
            else:
                print("Opcion no valida intente de nuevo")
        except ValueError:
            print("Por favor, ingrese una opcion valida")

#llamar a la funcion principal
if __name__ == '__main__':
    menu()
    print("FINALIZÓ EL PROGRAMA")

```

    ************   Datos del Postulante   ************
    
    
    Seleccione una opcion
    	1. Ingresar nombre
    	2. Ingresar apellido
    	3. Ingresar DNI
    	4. Ingresar celular 1
    	5. Ingresar celular 2
    	6. Ingresar altura
    	7. Ingresar peso
    8. Imprimir los datos ingresados del postulante
    9. Salir


    Seleccione una opcion:  1
    Ingrese el nombre:  luis


    Seleccione una opcion
    	1. Ingresar nombre
    	2. Ingresar apellido
    	3. Ingresar DNI
    	4. Ingresar celular 1
    	5. Ingresar celular 2
    	6. Ingresar altura
    	7. Ingresar peso
    8. Imprimir los datos ingresados del postulante
    9. Salir


    Seleccione una opcion:  2
    Ingrese el apellido:  perez


    Seleccione una opcion
    	1. Ingresar nombre
    	2. Ingresar apellido
    	3. Ingresar DNI
    	4. Ingresar celular 1
    	5. Ingresar celular 2
    	6. Ingresar altura
    	7. Ingresar peso
    8. Imprimir los datos ingresados del postulante
    9. Salir


    Seleccione una opcion:  3
    Ingrese el DNI:  12345678


    Seleccione una opcion
    	1. Ingresar nombre
    	2. Ingresar apellido
    	3. Ingresar DNI
    	4. Ingresar celular 1
    	5. Ingresar celular 2
    	6. Ingresar altura
    	7. Ingresar peso
    8. Imprimir los datos ingresados del postulante
    9. Salir


    Seleccione una opcion:  4
    Ingrese el primer numero de celular:  123456789


    Seleccione una opcion
    	1. Ingresar nombre
    	2. Ingresar apellido
    	3. Ingresar DNI
    	4. Ingresar celular 1
    	5. Ingresar celular 2
    	6. Ingresar altura
    	7. Ingresar peso
    8. Imprimir los datos ingresados del postulante
    9. Salir


    Seleccione una opcion:  5
    Ingrese el segundo numero de celular:  987654312


    Seleccione una opcion
    	1. Ingresar nombre
    	2. Ingresar apellido
    	3. Ingresar DNI
    	4. Ingresar celular 1
    	5. Ingresar celular 2
    	6. Ingresar altura
    	7. Ingresar peso
    8. Imprimir los datos ingresados del postulante
    9. Salir


    Seleccione una opcion:  6
    Ingrese la altura:  1.70


    Seleccione una opcion
    	1. Ingresar nombre
    	2. Ingresar apellido
    	3. Ingresar DNI
    	4. Ingresar celular 1
    	5. Ingresar celular 2
    	6. Ingresar altura
    	7. Ingresar peso
    8. Imprimir los datos ingresados del postulante
    9. Salir


    Seleccione una opcion:  8


    
    Datos del Postulante:
    Nombre: luis
    Apellido: perez
    DNI: 12345678
    Celular 1: 123456789
    Celular 2: 987654312
    Altura: 1.70
    Seleccione una opcion
    	1. Ingresar nombre
    	2. Ingresar apellido
    	3. Ingresar DNI
    	4. Ingresar celular 1
    	5. Ingresar celular 2
    	6. Ingresar altura
    	7. Ingresar peso
    8. Imprimir los datos ingresados del postulante
    9. Salir


    Seleccione una opcion:  7
    Ingrese el peso:  65


    Seleccione una opcion
    	1. Ingresar nombre
    	2. Ingresar apellido
    	3. Ingresar DNI
    	4. Ingresar celular 1
    	5. Ingresar celular 2
    	6. Ingresar altura
    	7. Ingresar peso
    8. Imprimir los datos ingresados del postulante
    9. Salir


    Seleccione una opcion:  8


    
    Datos del Postulante:
    Nombre: luis
    Apellido: perez
    DNI: 12345678
    Celular 1: 123456789
    Celular 2: 987654312
    Altura: 1.70
    Peso: 65
    Seleccione una opcion
    	1. Ingresar nombre
    	2. Ingresar apellido
    	3. Ingresar DNI
    	4. Ingresar celular 1
    	5. Ingresar celular 2
    	6. Ingresar altura
    	7. Ingresar peso
    8. Imprimir los datos ingresados del postulante
    9. Salir


    Seleccione una opcion:  9


    Saliendo del programa...
    FINALIZÓ EL PROGRAMA



```python
##Hacer un programa que imprima en pantalla un menu de "Datos del Alumno" con las opciones

#funcion para validar que el nombre o apellido solo contenga letras
def validar_nombre_apellido(cadena):
    return all(caracter.isalpha() or caracter.isspace() for caracter in cadena)

#funcion para validar que la nota esté en el rango de 0 a 20
def validar_nota(nota):
    try:
        nota = float(nota)
        return 0 <= nota <= 20
    except ValueError:
        return False

#funcion para calcular el promedio
def calcular_promedio(nota1, nota2, nota3, nota4, nota_proyecto_final):
    #se suman 5 puntos a las primeras 4 notas
    nota1 += 5
    nota2 += 5
    nota3 += 5
    nota4 += 5
    #calculo del promedio
    promedio = (nota1 + nota2 + nota3 + nota4 + (nota_proyecto_final * 3)) / 7
    return promedio

#funcion para determinar el estado del alumno
def determinar_estado(promedio):
    if promedio > 19.5:
        return "DECIMO SUPERIOR"
    elif promedio > 17.5:
        return "QUINTO SUPERIOR"
    elif promedio > 10.5:
        return "APROBADO"
    else:
        return "DESAPROBADO"

#funcion principal del menu
def menu():
    #solicitar los datos del alumno
    while True:
        nombre = input("Ingrese el nombre del alumno: ")
        if not validar_nombre_apellido(nombre):
            print("Nombre inválido... Solo puede contener letras y espacios.")
            continue
        apellido = input("Ingrese el apellido del alumno: ")
        if not validar_nombre_apellido(apellido):
            print("Apellido inválido... Solo puede contener letras y espacios.")
            continue
        
        #validar notas
        while True:
            try:
                nota1 = float(input("Ingrese la Nota 1 (0-20): "))
                if not validar_nota(nota1):
                    print("Nota inválida... Debe ser un número entre 0 y 20.")
                    continue
                nota2 = float(input("Ingrese la Nota 2 (0-20): "))
                if not validar_nota(nota2):
                    print("Nota inválida... Debe ser un número entre 0 y 20.")
                    continue
                nota3 = float(input("Ingrese la Nota 3 (0-20): "))
                if not validar_nota(nota3):
                    print("Nota inválida... Debe ser un número entre 0 y 20.")
                    continue
                nota4 = float(input("Ingrese la Nota 4 (0-20): "))
                if not validar_nota(nota4):
                    print("Nota inválida... Debe ser un número entre 0 y 20.")
                    continue
                nota_proyecto_final = float(input("Ingrese la Nota del Proyecto Final (0-20): "))
                if not validar_nota(nota_proyecto_final):
                    print("Nota inválida... Debe ser un número entre 0 y 20.")
                    continue
                break
            except ValueError:
                print("Por favor, ingrese solo números válidos para las notas.")
        
        #opción de imprimir el promedio o salir
        while True:
            titulo2 = ("   Datos del Alumno   ")
            print(titulo2.center(50, '*'))
            print('\n')
            print("Seleccione una opcion")
            print("\t1. Imprimir promedio del alumno")
            print("\t2. Salir")
            
            try:
                opcion = int(input("Seleccionaste la opción: "))
                
                if opcion == 1:
                    #calcular el promedio
                    promedio = calcular_promedio(nota1, nota2, nota3, nota4, nota_proyecto_final)
                    print(f'\nPromedio: {promedio}')
                    
                    #determinar el estado y mostrar los resultados
                    estado = determinar_estado(promedio)
                    print(f'Estado: {estado}')
                    
                    #mostrar mensaje adicional si es necesario
                    if estado == "QUINTO SUPERIOR":
                        print("¡Felicidades, estás en el Quinto Superior!")
                    elif estado == "DECIMO SUPERIOR":
                        print("¡Excelente, estás en el Décimo Superior!")
                
                elif opcion == 2:
                    print("Saliendo del programa...")
                    return
                else:
                    print("Opción no válida, intente de nuevo.")
            
            except ValueError:
                print("Por favor, ingrese una opción válida.")

#llamar a la función principal
if __name__ == '__main__':
    menu()
    print("FINALIZÓ EL PROGRAMA")

```

    Ingrese el nombre del alumno:  juan
    Ingrese el apellido del alumno:  tesla
    Ingrese la Nota 1 (0-20):  11
    Ingrese la Nota 2 (0-20):  19
    Ingrese la Nota 3 (0-20):  18
    Ingrese la Nota 4 (0-20):  19
    Ingrese la Nota del Proyecto Final (0-20):  18


    **************   Datos del Alumno   **************
    
    
    Seleccione una opcion
    	1. Imprimir promedio del alumno
    	2. Salir


    Seleccionaste la opción:  1


    
    Promedio: 20.142857142857142
    Estado: DECIMO SUPERIOR
    ¡Excelente, estás en el Décimo Superior!
    **************   Datos del Alumno   **************
    
    
    Seleccione una opcion
    	1. Imprimir promedio del alumno
    	2. Salir


    Seleccionaste la opción:  2


    Saliendo del programa...
    FINALIZÓ EL PROGRAMA



```python
##Hacer un programa que imprima en pantalla un menu "Numeros Capicua" con sus opciones

#funcion para verificar si un número de 3 cifras es capicúa
def es_capicua_3_cifras(numero):
    if len(str(numero)) == 3:
        str_num = str(numero)
        return str_num == str_num[::-1]
    return False

#funcion para verificar si un número de 4 cifras es capicúa
def es_capicua_4_cifras(numero):
    if len(str(numero)) == 4:
        str_num = str(numero)
        return str_num == str_num[::-1]
    return False

#funcion para imprimir números capicúa de 3 cifras
def imprimir_capicua_3_cifras():
    print("Numeros Capicua de 3 cifras:")
    for num in range(100, 1000):
        if es_capicua_3_cifras(num):
            print(num)

#funcion para imprimir números capicúa de 4 cifras
def imprimir_capicua_4_cifras():
    print("Numeros Capicua de 4 cifras:")
    for num in range(1000, 10000):
        if es_capicua_4_cifras(num):
            print(num)

#funcion para validar si un número de 3 cifras es capicúa
def validar_capicua_3_cifras():
    try:
        numero = int(input("Ingrese un numero de 3 cifras: "))
        if 100 <= numero <= 999:
            if es_capicua_3_cifras(numero):
                print(f'El numero {numero} es capicua.')
            else:
                print(f'El numero {numero} no es capicua.')
        else:
            print("El numero no tiene 3 cifras.")
    except ValueError:
        print("Por favor ingrese un numero válido.")

#funcion para validar si un numero de 4 cifras es capicúa
def validar_capicua_4_cifras():
    try:
        numero = int(input("Ingrese un numero de 4 cifras: "))
        if 1000 <= numero <= 9999:
            if es_capicua_4_cifras(numero):
                print(f'El numero {numero} es capicua.')
            else:
                print(f'El numero {numero} no es capicua.')
        else:
            print("El numero no tiene 4 cifras.")
    except ValueError:
        print("Por favor ingrese un numero valido.")

#funcion principal que gestiona el meno
def menu():
    while True:
        titulo = ("   Numeros Capicua   ")
        print(titulo.center(50, '*'))
        print('\n')
        print("Seleccione una opcion")
        print("\t1. Imprimir Numeros Capicua de 3 cifras")
        print("\t2. Imprimir Numeros Capicua de 4 cifras")
        print("\t3. Validar Numeros Capicua de 3 cifras")
        print("\t4. Validar Numeros Capicua de 4 cifras")
        print("\t5. Salir")
        
        try:
            opcion = int(input("Seleccionaste la opcion: "))
            
            if opcion == 1:
                imprimir_capicua_3_cifras()
            elif opcion == 2:
                imprimir_capicua_4_cifras()
            elif opcion == 3:
                validar_capicua_3_cifras()
            elif opcion == 4:
                validar_capicua_4_cifras()
            elif opcion == 5:
                print("Saliendo del programa...")
                break
            else:
                print("Opcion no valida... intente de nuevo.")
        except ValueError:
            print("Por favor ingrese una opción valida.")

#llamar a la funcion principal
if __name__ == "__main__":
    menu()
    print("FINALIZÓ EL PROGRAMA")

```

    **************   Numeros Capicua   ***************
    
    
    Seleccione una opcion
    	1. Imprimir Numeros Capicua de 3 cifras
    	2. Imprimir Numeros Capicua de 4 cifras
    	3. Validar Numeros Capicua de 3 cifras
    	4. Validar Numeros Capicua de 4 cifras
    	5. Salir


    Seleccionaste la opcion:  1


    Numeros Capicua de 3 cifras:
    101
    111
    121
    131
    141
    151
    161
    171
    181
    191
    202
    212
    222
    232
    242
    252
    262
    272
    282
    292
    303
    313
    323
    333
    343
    353
    363
    373
    383
    393
    404
    414
    424
    434
    444
    454
    464
    474
    484
    494
    505
    515
    525
    535
    545
    555
    565
    575
    585
    595
    606
    616
    626
    636
    646
    656
    666
    676
    686
    696
    707
    717
    727
    737
    747
    757
    767
    777
    787
    797
    808
    818
    828
    838
    848
    858
    868
    878
    888
    898
    909
    919
    929
    939
    949
    959
    969
    979
    989
    999
    **************   Numeros Capicua   ***************
    
    
    Seleccione una opcion
    	1. Imprimir Numeros Capicua de 3 cifras
    	2. Imprimir Numeros Capicua de 4 cifras
    	3. Validar Numeros Capicua de 3 cifras
    	4. Validar Numeros Capicua de 4 cifras
    	5. Salir


    Seleccionaste la opcion:  2


    Numeros Capicua de 4 cifras:
    1001
    1111
    1221
    1331
    1441
    1551
    1661
    1771
    1881
    1991
    2002
    2112
    2222
    2332
    2442
    2552
    2662
    2772
    2882
    2992
    3003
    3113
    3223
    3333
    3443
    3553
    3663
    3773
    3883
    3993
    4004
    4114
    4224
    4334
    4444
    4554
    4664
    4774
    4884
    4994
    5005
    5115
    5225
    5335
    5445
    5555
    5665
    5775
    5885
    5995
    6006
    6116
    6226
    6336
    6446
    6556
    6666
    6776
    6886
    6996
    7007
    7117
    7227
    7337
    7447
    7557
    7667
    7777
    7887
    7997
    8008
    8118
    8228
    8338
    8448
    8558
    8668
    8778
    8888
    8998
    9009
    9119
    9229
    9339
    9449
    9559
    9669
    9779
    9889
    9999
    **************   Numeros Capicua   ***************
    
    
    Seleccione una opcion
    	1. Imprimir Numeros Capicua de 3 cifras
    	2. Imprimir Numeros Capicua de 4 cifras
    	3. Validar Numeros Capicua de 3 cifras
    	4. Validar Numeros Capicua de 4 cifras
    	5. Salir


    Seleccionaste la opcion:  3
    Ingrese un numero de 3 cifras:  123


    El numero 123 no es capicua.
    **************   Numeros Capicua   ***************
    
    
    Seleccione una opcion
    	1. Imprimir Numeros Capicua de 3 cifras
    	2. Imprimir Numeros Capicua de 4 cifras
    	3. Validar Numeros Capicua de 3 cifras
    	4. Validar Numeros Capicua de 4 cifras
    	5. Salir


    Seleccionaste la opcion:  5


    Saliendo del programa...
    FINALIZÓ EL PROGRAMA



```python
##Hacer un programa que imprima en pantalla un menu "Datos del Paciente" y que solicite ingresar opciones

#funcion para solicitar nombre sin numeros ni simbolos extraños
def solicitar_nombre():
    while True:
        nombre = input("Ingrese el nombre: ")
        if nombre.isalpha():
            return nombre
        else:
            print("El nombre no debe contener numeros o simbolos extraños")

#funcion para solicitar el apellido sin numeros ni simbolos extraños
def solicitar_apellido():
    while True:
        apellido = input("Ingrese el apellido: ")
        if apellido.isalpha():
            return apellido
        else:
            print("El apellido no debe contener numeros o simbolos extraños")

#funcion para solicitar la edad
def solicitar_edad():
    while True:
        try:
            edad = int(input("Ingrese la edad: "))
            if edad > 0:
                return edad
            else:
                print("La edad debe ser un numero positivo")
        except ValueError:
            print("Por favor, ingrese un número válido")

#funcion para solicitar el peso
def solicitar_peso():
    while True:
        try:
            peso = float(input("Ingrese el peso (en Kg): "))
            if peso > 0:
                return peso
            else:
                print("El peso debe ser un numero positivo")
        except ValueError:
            print("Por favor, ingrese un numero valido")

#funcion para solicitar el sexo del paciente
def solicitar_sexo():
    while True:
        sexo = input("Ingrese el sexo (M/F): ").upper()
        if sexo == 'M' or sexo == 'F':
            return sexo
        else:
            print("El sexo debe ser 'M' para masculino o 'F' para femenino")

def imprimir_dieta(sexo, peso):
    #para mujeres
    if sexo == 'F':
        if peso < 40:
            print("No hay dieta recomendada")
        elif 40 <= peso < 50:
            print("Dieta rica en vegetales: Ensaladas, brócoli, espinacas, zanahorias")
        elif 50 <= peso < 60:
            print("Dieta rica en vegetales y frutas: Ensaladas, brócoli, espinacas, manzanas, fresas")
        elif 60 <= peso < 80:
            print("Dieta rica en vegetales, frutas y semillas: Ensaladas, brócoli, espinacas, manzanas, fresas, chía, almendras")
        elif peso >= 80:
            print("Debe someterse a cirugía")

    #para hombres
    elif sexo == 'M':
        if peso < 60:
            print("No hay dieta recomendada")
        elif 60 <= peso < 75:
            print("Dieta rica en vegetales: Ensaladas, brócoli, espinacas, zanahorias")
        elif 75 <= peso < 95:
            print("Dieta rica en vegetales y frutas: Ensaladas, brócoli, espinacas, manzanas, fresas")
        elif 95 <= peso < 120:
            print("Dieta rica en vegetales, frutas y semillas: Ensaladas, brócoli, espinacas, manzanas, fresas, chía, almendras")
        elif peso >= 120:
            print("Debe someterse a cirugía")

#funcion principal del menu
def menu():
    while True:
        titulo = ("   Datos del Paciente   ")
        print(titulo.center(50, '*'))
        print('\n')
        print("Seleccione una opcion")
        print("\t1. Nombre")
        print("\t2. Apellido")
        print("\t3. Edad")
        print("\t4. Peso")
        print("\t5. Sexo")
        print("\t6. Imprimir Dieta")
        print("\t7. Salir")

        opcion = input("Seleccionaste la opcion: ")

        if opcion == '1':
            nombre = solicitar_nombre()
        elif opcion == '2':
            apellido = solicitar_apellido()
        elif opcion == '3':
            edad = solicitar_edad()
        elif opcion == '4':
            peso = solicitar_peso()
        elif opcion == '5':
            sexo = solicitar_sexo()
        elif opcion == '6':
            imprimir_dieta(sexo, peso)
        elif opcion == '7':
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida... por favor seleccione una opcion entre 1 y 7")

#llamar a la funcion principal
if __name__ == "__main__":
    menu()
    print("FINALIZÓ EL PROGRAMA")

```

    *************   Datos del Paciente   *************
    
    
    Seleccione una opcion
    	1. Nombre
    	2. Apellido
    	3. Edad
    	4. Peso
    	5. Sexo
    	6. Imprimir Dieta
    	7. Salir


    Seleccionaste la opcion:  1
    Ingrese el nombre:  maria


    *************   Datos del Paciente   *************
    
    
    Seleccione una opcion
    	1. Nombre
    	2. Apellido
    	3. Edad
    	4. Peso
    	5. Sexo
    	6. Imprimir Dieta
    	7. Salir


    Seleccionaste la opcion:  2
    Ingrese el apellido:  fuentes


    *************   Datos del Paciente   *************
    
    
    Seleccione una opcion
    	1. Nombre
    	2. Apellido
    	3. Edad
    	4. Peso
    	5. Sexo
    	6. Imprimir Dieta
    	7. Salir


    Seleccionaste la opcion:  3
    Ingrese la edad:  18


    *************   Datos del Paciente   *************
    
    
    Seleccione una opcion
    	1. Nombre
    	2. Apellido
    	3. Edad
    	4. Peso
    	5. Sexo
    	6. Imprimir Dieta
    	7. Salir


    Seleccionaste la opcion:  4
    Ingrese el peso (en Kg):  55


    *************   Datos del Paciente   *************
    
    
    Seleccione una opcion
    	1. Nombre
    	2. Apellido
    	3. Edad
    	4. Peso
    	5. Sexo
    	6. Imprimir Dieta
    	7. Salir


    Seleccionaste la opcion:  5
    Ingrese el sexo (M/F):  F


    *************   Datos del Paciente   *************
    
    
    Seleccione una opcion
    	1. Nombre
    	2. Apellido
    	3. Edad
    	4. Peso
    	5. Sexo
    	6. Imprimir Dieta
    	7. Salir


    Seleccionaste la opcion:  6


    Dieta rica en vegetales y frutas: Ensaladas, brócoli, espinacas, manzanas, fresas
    *************   Datos del Paciente   *************
    
    
    Seleccione una opcion
    	1. Nombre
    	2. Apellido
    	3. Edad
    	4. Peso
    	5. Sexo
    	6. Imprimir Dieta
    	7. Salir


    Seleccionaste la opcion:  7


    Saliendo del programa...
    FINALIZÓ EL PROGRAMA



```python

```
