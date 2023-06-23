# Ejercicio Programación estructurada y modular:

# 1. Realice un programa que muestre el mensaje “Hola Aula X (Indicar el número de aula a la que
# pertenecen), ¿Qué tal?” en tres veces intercambiados entre ellos otro mensajes a su elección.
def saludar():
    print('Hola Aula 1, ¿Qué tal?')
    r1 = input('Respuesta: ')
    print('Me alegro, como te llamas?')
    r2 = input('Respuesta: ')
    print('{}!,un gusto conocerte!'.format(r2))

saludar()

# 2. A partir del siguiente ejemplo “Hola Ana, ¿Qué tal?” realizar el programa la ejecución del mismo con
# al menos otros dos nombres más, es decir, tres mensajes con tres nombres distintos. Recuerda: en
# estos ejercicios trabajamos argumentos.
def sNombre(n1,n2, n3):
    print('Hola {}, ¿Qué tal?'.format(n1))
    print('Como esta {}?'.format(n2))
    print('Saludos a {}!'.format(n3))

sNombre('Ana', 'Martin','Claudia')

# 3. Realizar un programa de funciones que contengan 3 parámetros, el cual derive en una suma. Mostrar
# el resultado dos veces.
def suma(v1,v2,v3):
    c =v1 +v2
    print(c)

suma(4,5,7)

# 4. Realice un programa que lea dos números (dos parámetros), compare si son IGUALES, en ese caso,
# mostrar un mensaje que muestre TRUE.
def comparar(x,y):
    if x ==y:
        print('TRUE')
    else:
        print('FALSE')

comparar(7,7)

# 5. Realice un programa que contenga una función que se llame “sumayresta”, que la misma contenga dos
# variables locales nombradas suma y resta, respectivamente. Recuerda: en estos ejercicios trabajamos
# argumentos para este ejercicio sería dos.