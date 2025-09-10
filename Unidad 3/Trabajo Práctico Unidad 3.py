#Trabajo Práctico Unidad 3
#Alumno: Espinoza Hector Samuel

#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad1 = int(input("Introduce tu edad: "))
if (edad1 >= 18):
    print("Es mayor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

nota2 = int(input("Introduzca la nota obtenida: "))

if nota2 >= 6:
    print ("Aprobado")
else:
    print ("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

num3 = int(input("Por favor ingrese un número par: "))

if num3 % 2 == 0:
    print ("Ha ingresado un número par")
else:
    print ("Por favor, ingrese un número par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

edad4 = int(input("Por favor ingrese su edad: "))

if edad4 < 12:
    print ("Niño/a: menor de 12 años.")
elif edad4 >= 12 and edad4 < 18:
    print("Adolescente: mayor o igual que 12 años y menor que 18 años.")
elif edad4>=18 and edad4<30:
    print("Adulto/a joven: mayor o igual que 18 años y menor que 30 años.")
else:
    print ("Adulto/a: mayor o igual que 30 años.")

#5) escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

Rta6 = input ("el siguiente programa determinará el sesgo de un conjunto de datos generados al azar. Presione Y para continuar o N para finalizar: ").lower()
if Rta6 == "y":
    import random
    numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

    from statistics import mode, median, mean
    media5 = mean (numeros_aleatorios)
    mediana5 = median(numeros_aleatorios)
    moda5 = mode(numeros_aleatorios)

    if media5==mediana5 and mediana5 == moda5:
        print ("Los datos analizados no presentan sesgo")
    elif media5 > mediana5 and mediana5 > moda5:
        print ("los datos analizados presentan un sesgo positivo")
    elif media5 < mediana5 and mediana5 < moda5:
        print ("los datos analizados presentan sesgo negativo")
    else:
        print ("ERROR")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.

string7 = input ("ingrese un texto: ")
ult_letra = string7 [-1].lower()

if ult_letra == "a" or ult_letra == "e" or ult_letra == "i" or ult_letra == "o" or ult_letra == "u":
    print (string7+"!")
else:
    print (string7)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla.

nombre8 = input ("Ingrese su nombre: ") 
modo8 = int(input ("ingrese 1, 2 o 3 dependiendo de la opción que desee: \n 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. \n 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. \n 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. \n"))

if modo8 == 1:
    print (nombre8.upper())
elif modo8 == 2:
    print (nombre8.lower())
elif modo8 == 3:
    print (nombre8.title())
else:
    print ("error")

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud9 = float (input("Ingrese la magnitud de un terremoto para ser clasificada según la escala de Richter: "))

if magnitud9 < 3:
    print ("Muy leve (imperceptible).")
elif magnitud9  < 4:
    print ("Leve (ligeramente perceptible)")
elif magnitud9  < 5:
    print ("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud9  < 6:
    print ("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud9  < 7:
    print ("Muy Fuerte (puede causar daños significativos)")
elif magnitud9  >= 7:
    print ("Extremo (puede causar graves daños a gran escala)")

#10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano

hemisferio10 = input ("Ingrese el hemisferio en el que se encuentra (N o S) ").lower()
mes10 = int(input ("Ingrese el número del mes en curso: "))
dia10 = int(input ("Ingrese el número del día actual: "))

fecha10 = mes10*100+dia10

if fecha10<321 or fecha10>=1221:
    estacion10=1
elif fecha10<621:
    estacion10=2
elif fecha10<921:
    estacion10=3
elif fecha10<1221:
    estacion10=4

if hemisferio10 == "s":
    estacion10 = estacion10 + 2

if estacion10>4:
    estacion10 = estacion10 - 4

if estacion10 == 1:
    print ("INVIERNO")
elif estacion10 ==2:
    print ("PRIMAVERA")
elif estacion10 ==3:
    print ("VERANO")
elif estacion10 == 4:
    print ("OTOÑO")
