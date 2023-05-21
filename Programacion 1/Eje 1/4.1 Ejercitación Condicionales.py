# 4.1 Ejercitación Condicionales

# Ejercicio estructura condicional simple:

# 1. Realice un programa que solicite dos letras ingresadas por el usuario y verifique si son iguales o no,
# mostrando un mensaje.
primerLetra = input('Ingrese la primer letra: ')
segundaLetra = input('Ingrese la segunda letra: ')

if primerLetra == segundaLetra:
    print('Las letras {} y {}, son iguales'.format(primerLetra,segundaLetra))
else:
    print('Las letras {} y {}, son diferentes'.format(primerLetra,segundaLetra))

# 2. Hacer un programa que permita decidir si dos palabras son iguales o  diferentes. Mostrar mensaje por pantalla.
palabra1 = input('Ingrese la primer palabra: ')
palabra2 = input('Ingrese la segunda palabra: ')

if palabra1 == palabra2:
    print('Las palabras {} son iguales'.format(palabra1))
else:
    print('Las palabras {} y {} son diferentes'.format(palabra1,palabra2))

# 3. Realizar un programa que permita ingresar “f” o “m” y determinar si vota  en mesa femenina o masculina.
genero = input('Ingrese letra correspondiente: ')
generoA = genero.lower()

if generoA == 'f':
    print('Vota en una mesa femenina')
elif generoA == 'm':
    print('Vota en una mesa masculina')
else:
    print('Debe ingresar f o m')

# 4. Realice un programa que lea dos números y diga cuál es el mayor.
numeroA = int(input('ingrese el primer numero: '))
numeroB = int(input('ingrese el segundo numero: '))

if numeroA > numeroB:
    print('El mayor es: {}'.format(numeroA))
elif numeroA == numeroB:
    print('Los numeros son iguales')
else:
    print('El mayor es: {} '.format(numeroB))

# 5. Realice un programa que cambie pesos a dólares. Mejórelo, añadiendo el cambio de dólares a pesos y que sea el
# usuario quién decida qué tipo de cambio quiere, si de dólares a pesos o viceversa.
moneda = input('Ingrese "dolares" o "pesos", dependiento el tipo de cambio que necesite: ')
monedaA = moneda.lower()
precioDolar = 397.46

if monedaA == "dolares":
    cant = float(input('Ingrese la cantidad de pesos a cambiar: '))
    cant /= precioDolar
    print('El total en dolares es: {}'.format(cant))
elif monedaA == "pesos":
    cant = float(input('Ingrese la cantidad de dolares a cambiar: '))
    cant *= precioDolar
    print('El total en pesos es: {}'.format(cant))
else:
    print('Palabra incorrecta, debe ingresar "dolares" o "pesos", reintentelo por favor ')

# 6. Realice un programa donde el usuario ingrese su edad. Si es mayor de  16 años, muestre un mensaje
# diciendo “puede votar”, sino “no vota”.
edad = int(input('Ingrese la edad: '))

if edad > 16:
    print('Puede votar')
else:
    print('No puede votar')

# --------------------------------------------------------------------------------------------------------------
# Ejercicios estructura condicional compuesto (IF anidados)
# 1. Introducir los lados de un triángulo y visualizar por pantalla si dicho  triángulo es equilátero, isósceles
# o escaleno.
lado1 = float(input('Ingrese la medida del primer lado: '))
lado2 = float(input('Ingrese la medida del segundo lado: '))
lado3 = float(input('Ingrese la medida del tercer lado: '))

if lado1 == lado2 and lado1 == lado3:
    print('El triangulo es Equilatero, todos los lados son iguales')
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print('El triangulo es Escaleno, ningun lado es igual')
elif lado1 == lado2 and lado1 != lado3:
    print('El triangulo es Isoceles, dos de sus lados son iguales')
elif lado1 == lado3 and lado1 != lado2:
    print('El triangulo es Isoceles, dos de sus lados son iguales')
elif lado2 == lado3 and lado2 != lado1:
    print('El triangulo es Isoceles, dos de sus lados son iguales')

# 2. Realice un programa que le permita al usuario simular el pago  ingresando el importe y la forma de pago:
# • Contado (1): se aplica un descuento del 10% al importe
# • Tarjeta (2): se aplica un interés de 10%
# • Débito (3): se aplica un descuento del 5%
# Mostrar el importe, el descuento o interés y el importe total.
monto = float(input('Ingrese el monto de la compra: '))
codigoPago = int(input('Ingrese 1 si el pago es de contado, 2 si es con tarjeta o 3 si es con debito: '))

if codigoPago == 1:
    descuento = monto * 0.1
    importeFinal = monto - descuento
    print('El monto es ${}. El descuento es de ${}. El importe total a abonar es de $ {}'.format(monto,descuento, importeFinal))
elif codigoPago == 2:
    interes = monto * 0.1
    importeFinal = monto + interes
    print('El monto es ${}. El interes es de ${}. El importe total a abonar es de $ {}'.format(monto, interes, importeFinal))
else:
    descuento = monto * 0.05
    importeFinal = monto - descuento
    print('El monto es ${}. El descuento es de ${}. El importe total a abonar es de $ {}'.format(monto, descuento, importeFinal))

# 3. Realice un programa que lea tres números, muestre cuál es el mayor y  determine si es par o impar.
n1 = int(input('Ingrese primer numero: '))
n2 = int(input('Ingrese segundo numero: '))
n3 = int(input('Ingrese tercer numero: '))

if n1 > n2 and n1 >n3:
    if n1 % 2 == 0:
        print('El numero {} es el mayor y es par'.format(n1))
    else:
        print('El numero {} es el mayor y es impar'.format(n1))
elif n2 > n1 and n2 >n3:
    if n2 % 2 == 0:
        print('El numero {} es el mayor y es par'.format(n2))
    else:
        print('El numero {} es el mayor y es impar'.format(n2))
elif n3 > n1 and n3 > n2:
    if n3%2 == 0:
        print('El numero {} es el mayor y es par'.format(n3))
    else:
        print('El numero {} es el mayor y es impar'.format(n3))
else:
    print('Los tres numeros {} son iguales'.format(n1))

# 4. Confeccione un programa que pida un número del 1 al 7 y diga el día de  la semana correspondiente.
nDia = int(input('Ingrese el numero del dia del 1 al 7: '))

if nDia == 1:
    print('El dia es Lunes')
elif nDia == 2:
    print('El dia es Martes')
elif nDia == 3:
    print('El dia es Miercoles')
elif nDia == 4:
    print('El dia es Jueves')
elif nDia == 5:
    print('El dia es Viernes')
elif nDia == 6:
    print('El dia es Sabado')
elif nDia == 7:
    print('El dia es Domingo')
else:
    print('Error, debe ingresar un numero del 1 al 7. Intentelo nuevamente')

# 5. Realice un programa que pida un número del 1 al 12 y diga el nombre del mes correspondiente

nMes = int(input('Ingrese el numero del dia del 1 al 12: '))

if nMes == 1:
    print('El dia es Enero')
elif nMes == 2:
    print('El dia es Febrero')
elif nMes == 3:
    print('El dia es Marzo')
elif nMes == 4:
    print('El dia es Abril')
elif nMes == 5:
    print('El dia es Mayo')
elif nMes == 6:
    print('El dia es Junio')
elif nMes == 7:
    print('El dia es Julio')
elif nMes == 8:
    print('El dia es Agosto')
elif nMes == 9:
    print('El dia es Septiembre')
elif nMes == 10:
    print('El dia es Octubre')
elif nMes == 11:
    print('El dia es Noviembre')
elif nMes == 12:
    print('El dia es Diciembre')
else:
    print('Error, debe ingresar un numero del 1 al 12. Intentelo nuevamente')