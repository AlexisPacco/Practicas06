```python
###Estructura Excepciones: las 'Excepciones' se utiliza para evitar cortes durante la ejecucion del programa
try:
    <codigo>
    <codigo>
    .........
except:
    <codigo>
    <codigo>
    .........
```


```python
##Tripicos Errores
1/0
z = 25
print(z)

```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    Cell In[1], line 2
          1 ##Tripicos Errores
    ----> 2 1/0
          3 z = 25
          4 print(z)


    ZeroDivisionError: division by zero



```python
n = int(input())
z = 25
print(z)

```

     asdasd



    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[2], line 1
    ----> 1 n = int(input())
          2 z = 25
          3 print(z)


    ValueError: invalid literal for int() with base 10: 'asdasd'



```python
##Validacion de numeros:
#validar ingreso de numero entero
while True:
    try:
        x = int(input('Ingresar un numero: '))
        break
    except ValueError:
        print('Error!! no es un numero valido')

```

    Ingresar un numero:  !"#


    Error!! no es un numero valido


    Ingresar un numero:  qweqwe


    Error!! no es un numero valido


    Ingresar un numero:  23



```python
##Validacion de numeros y otra condicion:
#validar numeros enteros positivos
while True:
    try:
        x = int(input('Ingresar un numero positivo: '))
    except ValueError:
        print('Error!! no es un numero positivo valido')
        continue
    if x < 0:
        print('\tPor favor ingrese numero positivo')
        continue
    break

```

    Ingresar un numero positivo:  31213!"#


    Error!! no es un numero positivo valido


    Ingresar un numero positivo:  qwqwe


    Error!! no es un numero positivo valido


    Ingresar un numero positivo:  -13216


    	Por favor ingrese numero positivo


    Ingresar un numero positivo:  123



```python
###Estructura Funciones
def nombre_de_funcion(<argumento,a>):
    <codigo>
    <codigo>
    ...............
```


```python
##Funcion Principal 'main'
#Inicio mis programas con varias funciones
def uno():
    print('Inicio de Programa')

def dos():
    pass

def fin():
    print('\n\n\n Fin del programa')

#Programa 'main' principal
if __name__ == '__main__':
    uno()
    dos()
    uno()
    dos()
    fin()
    
```

    Inicio de Programa
    Inicio de Programa
    
    
    
     Fin del programa



```python
##Hacer un programa que solicite ingreso de DNI correctamente:
#Mi primera funcion validar dni
def validar_dni():
    while True:
        try:
            dni = int(input('Ingresar DNI: '))
            if len(str(dni)) == 8:
                print('\n\tDNI VALIDO')
                break
            else:
                print('\tError: Longitud de DNI no Valido... Intente de nuevo')
                continue

        except ValueError:
            print('\tError!!! No es un DNI Valido.. Intente de nuevo')

    return dni

#Programa 'main' principal
if __name__ == '__main__':
    titulo = ('    BONO FAMILIAR UNIVERSAL    ')
    print(titulo.center(50,'*'))
    print('\n\n')

    val_dni = validar_dni()

    print('\n\n El DNI Ingresado es: ==>',val_dni)
```

    *********    BONO FAMILIAR UNIVERSAL    **********
    
    
    


    Ingresar DNI:  !"#$!"


    	Error!!! No es un DNI Valido.. Intente de nuevo


    Ingresar DNI:  asdasdqw


    	Error!!! No es un DNI Valido.. Intente de nuevo


    Ingresar DNI:  2135654645654


    	Error: Longitud de DNI no Valido... Intente de nuevo


    Ingresar DNI:  12345678


    
    	DNI VALIDO
    
    
     El DNI Ingresado es: ==> 12345678



```python

```
