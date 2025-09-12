# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i1 in range (101):
    print (i1)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

num2 = float(input("ingrese un número entero para determinar la cantidad de dígitos que posee: "))
cant_digitos2 = 0

while num2 - int(num2) > 0:          #ciclo para verificación de que el número ingresado sea un número entero
    print (num2,"no es un número entero, inténtelo nuevamente")
    num2 = float (input ("ingrese un número entero para determinar la cantidad de dígitos que posee: "))

i2 = int (num2)

#opcion 1 para resolverla: (la dejo comentada porque no incluye ciclos)
# cant_digitos2= len(str(num2))
# print ("el número",num2,"contiene",cant_digitos2,"dígitos") #no uso f string porque mi teclado no tiene las llaves prometo configurarlo mas tarde =D

#opcion 2
while i2>=1:      #ciclo en el que disminuye el número un orden en cada iteración hasta que no queden digitos enteros. El número de iteraciones es el numero de digitos.
    cant_digitos2 += 1
    i2 /= 10
print ("el número",int(num2),"contiene",cant_digitos2,"dígitos")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

print ( "programa para cálcular la suma de todos los números enteros comprendidos entre dos valores extremos excluyendolos")

num3 = float(input("ingrese el primer valor: "))  #la consigna no dice que los valores extremos deben ser enteros por eso admito la posibilidad de que sean reales, pero la suma de los intermedios si sera solo de enteros
num3_2 = float(input("ingrese el segundo valor: "))
suma3 = 0

#decido resolver el ejercicio con un ciclo for donde in range (num_menor3, num_mayor3, + 1)
if num3 >= num3_2:   #primero definimos quienes son los valores menores y mayores
    num_menor3 = num3_2
    num_mayor3 = num3
else:
    num_menor3 = num3
    num_mayor3 = num3_2

#no es necesaria la verificación del número menor... si fuera un entero deberá ser excluido 
#y si fuera un decimal también su parte entera sera excluida avanzando al siguiente numero entero. Por tanto:
num_menor3 = int(num_menor3) + 1

if num_mayor3 - int(num_mayor3) == 0: #luego verificacion del número mayor ingresado 
   num_mayor3 = int(num_mayor3)  #si este es el caso significa que el numero ingresado es entero. Basta con dejarlo como esta ya que un ciclo for lo excluira
else:
   num_mayor3 = int (num_mayor3) + 1 #pero si fuera decimal, la parte entera no deberia ser excluida de la suma. Por eso a la parte entera le sumo uno


for x3 in range (num_menor3, num_mayor3):
    suma3 += x3

print (f"la suma de todos los números enteros comprendidos entre {num3} y {num3_2} es igual a {suma3}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

num4 = int (input ("Ingrese un valor entero para ser sumado (presione 0 cuando quiera finalizar a suma): "))
suma4 = 0

while num4 != 0:
    suma4 += num4
    num4 = int (input ("Ingrese un valor entero para ser sumado (presione 0 cuando quiera finalizar a suma): "))

print (f"el total acumulado con los números ingresados es de {suma4}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
num_adivinar5 = random.randint(1,9)
num5 = int (input ("Intente adivinar el número. Ingrese un número entre 1 y 9: "))
contador5 = 1

while num5 != num_adivinar5:
    contador5 += 1
    num5 = int (input ("incorrecto, vuelva a intentarlo, ingrese un número entre 1 y 9: "))

print (f"Acierto! {num5} es el número correcto. Número de intentos: {contador5}")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i6 in range (100, 0, -2):
    print (i6)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario

num7 = float (input ("Ingrese un valor entero positivo. A continuación de realizará la suma de todos los números enteros entre ese número y el cero: "))

while num7 <= 0 or num7 - int (num7) != 0:  #verificación del número ingresado
    print ("El número ingresado no es válido. Por favor ingrese un valor entero positivo: ")
    num7 = float (input ("Ingrese un valor entero positivo. A continuación de realizará la suma de todos los números enteros entre ese número y el cero: "))

num7 = int (num7)
suma7 = 0

for i7 in range (1, num7+1):
    suma7 += i7

print (f"la suma de todos los números enteros comprendidos entre 0 y {num7} es de {suma7}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

cant_num8 = 100
cant_pares8 = 0
cant_impares8 = 0
cant_positivos8 = 0
cant_negativos8 = 0

for i8 in range (cant_num8):
    num8 = int (input (f"Ingrese el valor #{i8+1} de {cant_num8}: "))
    if num8 % 2 == 0:
        cant_pares8 += 1
    else:
        cant_impares8 +=1
    
    if num8 > 0:
        cant_positivos8 += 1
    elif num8 < 0:
        cant_negativos8 += 1

print (f"Cantidad de números pares ingresados: {cant_pares8}")
print (f"Cantidad de números impares ingresados: {cant_impares8}")
print (f"Cantidad de números positivos ingresados: {cant_positivos8}")
print (f"Cantidad de números negativos ingresados: {cant_negativos8}")


# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

cant_num9 = 100
suma9 = 0

for i9 in range (cant_num9):
    num9 = int (input (f"Ingrese el valor #{i9+1} de {cant_num9}: "))
    suma9 += num9

print (f"El promedio de los valores ingresados es de {suma9/cant_num9}")


# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745

num10 = int (input ("Ingrese un número para invertir sus dígitos: "))
x10 = abs(num10)
cant_digitos10 = 0
num_invertido10 = 0

if num10 < 0: #se estandariza a positivos el número ingresado... si el valor es negativo se activara la bandera y mas adelante se le devovlera el signo.
    negative_flag = True
else:
    negative_flag = False

#primero determino la cantidad de dígitos que posee.. podría hacerlo mediante len(str(num10)) pero lo hare por medio de un ciclo
while x10 >= 1:
    cant_digitos10 += 1
    x10 /= 10

x10 = abs(num10) #restauro la variable a su valor original

#procedo a obtener los distintos digitos del numero y a reubicarlos
for i10 in range (1,cant_digitos10 + 1):
    num_invertido10 += (int(x10/10**(i10-1)) - int(x10/10**(i10))*10) * 10**(cant_digitos10 - i10)
    #el término int(x10/10**(i10-1)) ira eliminando el ultimo digito a medida que el ciclo avanza
    #al restarlo a int(x10/10**(i10))*10 se aisla la unidad del número resultante en el momento del ciclo
    #por último al multiplicarlo por 10**(cant_digitos10 - i10) se le asigna una nueva ubicación según el número invertido

if negative_flag == True: #si el número incial era negativo ahora se retoma el signo
    num_invertido10 *= -1

print (f"el número resultante de invertir todos los dígitos del número ingresado es {num_invertido10}")





