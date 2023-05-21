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


# 3. Ingresar las edades y el sexo de 15 personas y determinar cuántas son mujeres, cuántos varones, cuántos mayores
# de edad y cuántos menores de edad.


# 4. Leer 10 números y mostrar solamente los números positivos, y su sumatoria.


# 5. Leer 15 números negativos y convertirlos a positivos e imprimir dichos números.

