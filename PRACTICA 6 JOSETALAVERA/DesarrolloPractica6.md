```python
#validar ingreso de numero eneteros
while True:
    try:
        x = int(input('Ingresar numero: '))
        break
    except ValueError:
        print('Error!!! no es un numero valido ')

```

    Ingresar numero:  1&%%


    Error!!! no es un numero valido 


    Ingresar numero:  1233



```python
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
        
```

    Ingresar un numero positivo: 55985152&


    Error !!! no es un numero postivo valido 


    Ingresar un numero positivo: fsdfsdfs


    Error !!! no es un numero postivo valido 


    Ingresar un numero positivo: 12121



```python
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
```

    Inicio de Programa
    Inicio de Programa
    
    
    
     Fin del programa



```python
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
    
```

    ************BONO FAMILIAR UNIVERSAL   ************
    
    
    


    Ingresar DNI:  &$%$%$%#


    	Error!!! No es un DNI Valido ... Intente de Nuevo


    Ingresar DNI:  jsdkjk


    	Error!!! No es un DNI Valido ... Intente de Nuevo


    Ingresar DNI:  548469546545414


    	Error!Longitud de DNU no valido


    Ingresar DNI:  12368549


    
    	DNI VALIDO
    
    
     EL DNI INGRESADO es: ==> 12368549



```python

```
