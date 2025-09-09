#Trabajo Práctico N1 Secuenciales
#Alumno: Espinoza Hector Samuel

#ejercicio 1
print ("Hola Mundo!")

#ejercicio 2
nombre2 = input ("Por favor ingrese su nombre: ")
print (f"Hola {nombre}!")

#ejercicio 3
nombre3 = input ("Por favor ingrese su nombre: ")
apellido3 = input ("Por favor ingrese su apellido: ")
edad3 = input ("Por favor ingrese su edad: ")
residencia3 = input ("Por favor ingrese su lugar de residencia: ")
print (f"Hola soy {nombre3} {apellido3}, tengo {edad3} años y vivo en {residencia3}")

#ejercicio 4
print ("Calculadora de área y perímetro de un círculo")
radio4 = float (input ("Ingrese el radio: "))
import math
area4= math.pi * radio4 ** 2
perimetro4 = math.pi * radio4 *2
print ("área =",area4 )
print ("perímetro =",perimetro4)

#ejercicio 5
print ("Conversor segundos a horas")
segundos5 = int(input ("Ingrese la cantidad de segundos a convertir: "))
horas5 = int(segundos5 / 3600)
minutos5 = int((segundos5 % 3600)/60)
segundosRest5 = segundos5 - (horas5 * 3600 + minutos5 * 60)
print (segundos5,"segundos equivalen a",horas5,"horas con un resto de",minutos5,"minutos y",segundosRest5,"segundos.")

#ejercicio 6
print ("Tabla de multiplicar")
num6 = int(input ("Ingrese un número: "))
print (num6,"* 1 =",num6 * 1)
print (num6,"* 2 =",num6 * 2)
print (num6,"* 3 =",num6 * 3)
print (num6,"* 4 =",num6 * 4)
print (num6,"* 5 =",num6 * 5)
print (num6,"* 6 =",num6 * 6)
print (num6,"* 7 =",num6 * 7)
print (num6,"* 8 =",num6 * 8)
print (num6,"* 9 =",num6 * 9)
print (num6,"* 10 =",num6 * 10)

#ejercicio 7 
print ("Ingrese dos valores distintos de cero")
valor1_7 = int(input ("Ingrese el primer valor: "))
valor2_7 = int(input ("Ingrese el segundo valor: "))
print ("suma:",valor1_7+valor2_7)
print ("resta:",valor1_7-valor2_7)
print ("producto:",valor1_7*valor2_7)
print ("división:",valor1_7/valor2_7)

#ejercicio 8
print ("Calculadora de IMC")
altura8 = float(input ("Ingrese la altura (m): "))
peso8 = float(input ("Ingrese el peso (kg): "))
altura8_2 = altura8 ** 2
print ("Su índice de masa corporal es de",peso8/altura8_2)

#ejercicio 9
print ("Conversor de temperatura °C a °F")
tempC9 = int(input("Ingrese la temperatura en Celsius"))
tempF9 = tempC9 * 9/5 + 32
print (f"{tempC9}°C corresponden a {tempF9}°F")

#ejercicio 10
print ("Calculadora de promedio de tres números")
num10_1 = int (input("Ingrese el primer valor: "))
num10_2 = int (input("Ingrese el segundo valor: "))
num10_3 = int (input("Ingrese el tercer valor: "))
promedio10 = (num10_1+num10_2+num10_3)/3
print ("el promedio de los tres valores ingresados es de",promedio10)
