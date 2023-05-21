# Ejercicios estructuras repetitivas y estructuras condicionales.
# 1. Realice un programa que lea 4 números y diga cuántos son pares y  cuantos impares y devuelva la sumatoria de
# los pares.
numPares = []
numImpares = []
k = 0

while k < 4:
    n = int(input('Ingrese el numero: '))
    if n % 2 == 0:
        numPares.append(n)
    else:
        numImpares.append(n)
    k += 1

print('''
Hay {} numeros que son pares, su sumatoria es igual a {}. 
Hay {} numeros impares'''.format(len(numPares), sum(numPares),len(numImpares)))

# 2. Leer 10 números y obtener la cantidad de mayores y la cantidad de menores a 100, cuál es el número máximo y cuál
# es el número mínimo.

max = 100
min = 100
cantMenos100 = 0
cantMayores100 = 0
cantVueltas = 0

while cantVueltas < 10:
    numIngresado = int(input('Ingrese el numero solicitado: '))
    if numIngresado < 100:
        cantMenos100 += 1
        if numIngresado < min:
            min = numIngresado
    elif numIngresado > 100:
        cantMayores100 +=1
        if numIngresado > max:
            max = numIngresado
    cantVueltas +=1

if cantMayores100 == 0:
    cantMayores100 = 'No hubo numeros mayores a 100'

if cantMenos100 == 0:
    cantMenos100 = 'No hubo numeros menores a 100'

print('''
La cantidad de mayores a 100 es: {}
La cantidad de menores a 100 es: {}
El numero maximo es: {}
El numero minimo es: {}'''.format(cantMayores100, cantMenos100, max, min))

# 3. Ingresar las edades y el sexo de 15 personas y determinar cuántas son mujeres, cuántos varones, cuántos mayores
# de edad y cuántos menores de edad.
xPersonas = 0
mayoresEdad = 0
menoresEdad = 0
cantFem = 0
cantMasc = 0

while xPersonas < 14:
    edad = int(input('Ingrese la edad: '))
    sexo = input('Ingrese el genero, M para masculino y F para femenino: ')
    if edad >= 18:
        mayoresEdad += 1
    else:
        menoresEdad += 1
    if sexo == 'F':
        cantFem += 1
    elif sexo == 'M':
        cantMasc += 1
    else:
        print('debe ingresar F o M, intente nuevamente')
    xPersonas += 1

print('''
La cantidad de mayores de edad es: {}
La cantidad de menos de edad es: {} 
La cantidad de Mujeres es: {}
La cantidad de varones es: {}'''.format(mayoresEdad, menoresEdad, cantFem, cantMasc))

# 4. Leer 10 números y mostrar solamente los números positivos, y su sumatoria.


# 5. Leer 15 números negativos y convertirlos a positivos e imprimir dichos números.

