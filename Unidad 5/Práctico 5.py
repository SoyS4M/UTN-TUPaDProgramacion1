#Práctico 5: Listas - Tecnicatura Universitaria en Programación a Distancia - UTN
#Alumno: Espinoza Hector Samuel - Programación I

#Ejercicio 1
# 1) Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja.

notas1 = [3, 4, 5, 1, 10, 7, 8, 2, 9, 6]
    
suma1 = 0
notaAlta1 = 0
notaBaja1 = 10

for i1 in range (len(notas1)):
    print (f"Nota #{i1+1}: {notas1[i1]}")         #muestra la nota que considera en cada iteracion del ciclo mientras procesa los datos
    suma1 = suma1 + notas1[i1]
    if notas1[i1] > notaAlta1:
        notaAlta1 = notas1[i1]
    if notas1[i1] < notaBaja1:
        notaBaja1 = notas1[i1]

promedio1 = suma1 / len (notas1)

print (f"El promedio de notas obtenidos es de {promedio1}")
print (f"la nota más baja obtenida fue de {notaBaja1}")
print (f"la nota más alta obtenida fue de {notaAlta1}")

#Ejercicio 2
# 2) Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

print ("Por favor cargue cinco productos a continuación: ")
productos2 = []                                                                 #se define una lista en la que se agregaran los productos
for i2 in range (5):
    productos2.append(input(f"Ingrese el producto #{i2+1}: ").lower())          #lower para estandarizar

ordenados2 = sorted (productos2)                                                #sorted devuelve una nueva lista sin alterar la anterior

print ("Productos ingresados ordenados alfabeticamente:")
for j2 in range (5):
    print("Producto #",j2+1,ordenados2[j2])

opcion2 = int(input("si desea terminar presione 1. Si desea eliminar algun dato presione 2. Si desea actualizar algun valor presione 3: "))
if opcion2 == 2:
    ordenados2.remove(input("Usted ha elegido eliminar un producto. Por favor, ingrese el producto a eliminar: ").lower())
    
elif opcion2 == 3:
    indiceActualizar2 = ordenados2.index(input("Ingrese el producto a actualizar: ").lower())
    ordenados2[indiceActualizar2] = input ("Ingrese el nuevo producto: ").lower()
    
for k2 in range (len(ordenados2)):
    print (ordenados2[k2])

# #ejercicio3
# # 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# # • Crear una lista con los pares y otra con los impares.
# # • Mostrar cuántos números tiene cada lista.

import random
numeros3 = []
listaPares = []
listaImpares = []
i3 = 0

for i3 in range(15):
    numeros3.append(random.randint(1,100))
    if numeros3[i3] % 2 == 0:
        listaPares.append(numeros3[i3])
    else:
        listaImpares.append(numeros3[i3])

numeros3.sort()
listaImpares.sort()
listaPares.sort()

print(f"números generados al azar: {numeros3}")
print(len(listaPares),f" números pares ingresados:")
for j3 in range (len(listaPares)):
    print (f"#{j3+1}: {listaPares[j3]}")
print(len(listaImpares),f" números impares ingresados:")
for k3 in range (len(listaImpares)):
    print (f"#{k3+1}: {listaImpares[k3]}")

#ejercicio 4
# Dada una lista con valores repetidos:
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado.

datos4 = [1, 3, 5, 3, 7, 1, 9, 5, 3]
datos4.sort()
datosSinRepet = [datos4[0]]

for i4 in range (len(datos4)-1):
    if datos4[i4] != datos4[i4+1]:                  
        datosSinRepet.append(datos4[i4+1])          #esto crea una nueva lista ordenada donde los datos consecutivos sin distintos entre si

print("Datos ordenados y sin repetir:")

for i4 in range (len(datosSinRepet)):
    print(datosSinRepet[i4])

# #ejercicio 5
# Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.

alumnosPresentes = ["Juan", "Carlos", "Martin", "Marcos", "Matias", "Gisela", "Romina", "Albertina"]

print("alumnos presente: ",alumnosPresentes)
decide5 = int(input("Si desea agregar un nuevo estudiante presione 1, si desea eliminar uno existente presione 2, si desea salir presione 3: "))

if decide5 == 1:
    print ("ha seleccionado agregar un alumno a la lista")
    alumnosPresentes.append(input("Ingrese el nombre del alumno que desea agregar: "))
elif decide5 == 2:
    print ("ha seleccionado eliminar un alumno")
    alumnosPresentes.remove(input("ingrese el nombre del alumno a eliminar de la lista: "))

print("Lista actualizada:")
for i5 in range (len(alumnosPresentes)):
    print (alumnosPresentes[i5])

# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
# último pasa a ser el primero).

lista6 = [3, 2, 4, 6, 5, 1, 8]

lista6.insert(0,lista6[6])

del lista6[7]

print("Lista desplazada: ")
for i6 in range (len(lista6)):
    print(lista6[i6])

#ejercicio 7
# Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
# semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica

temperaturas7 = [[23.1, 12.2], [19.3, 12.4], [20.5, 9.6], [25.7, 9.8], [19.9, 10.0], [21.1, 8.2], [24.3, 9.4]]
sumaMinimas = 0
sumaMaximas = 0
maximaAmplitud = 0
diaMaxAmplitud = 0



for i7 in range (len(temperaturas7)):
    for j7 in range (2):
        if j7 == 0:
            sumaMaximas = sumaMaximas + temperaturas7[j7][0]
        elif j7 == 1:
            sumaMinimas = sumaMinimas + temperaturas7[j7][1]
if maximaAmplitud < temperaturas7[i7][0] - temperaturas7[i7][1]:
    maximaAmplitud = temperaturas7[i7][0] - temperaturas7[i7][1]
    diaMaxAmplitud = i7+1

print (f"El promedio de las mínimas temperaturas en la semana fue de {sumaMinimas/7}")
print (f"El promedio de las máximas temperaturas en la semana fue de {sumaMaximas/7}")
print (f"El día en el que se registró mayor amplitud térmica fue el día {diaMaxAmplitud} ({maximaAmplitud}°C)")

#ejercicio 8
# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.

notas8 = [[5, 7, 6], [6, 7, 7], [2, 2, 4], [9, 8, 10], [10, 10, 10]]          #cada lista anidada corresponde al conjunto de notas de un alumno en cada materia
sumaMateria1 = 0
sumaMateria2 = 0
sumaMateria3 = 0

for i8 in range (len(notas8)):
    for j8 in range (3):
        if j8 == 0:
            sumaMateria1 = sumaMateria1 + notas8[i8][j8]
            tempPromedio = notas8[i8][j8]
        elif j8 == 1:
            sumaMateria2 = sumaMateria2 + notas8[i8][j8]
            tempPromedio = tempPromedio + notas8[i8][j8]
        elif j8 == 2:
            sumaMateria3 = sumaMateria3 + notas8[i8][j8]
            tempPromedio = tempPromedio + notas8[i8][j8]
    print (f"el promedio del alumno #{i8+1} es de: {tempPromedio/3}")

print(f"el promedio de notas obtenidas en la materia 1 fue de: {sumaMateria1/5}")
print(f"el promedio de notas obtenidas en la materia 2 fue de: {sumaMateria2/5}")
print(f"el promedio de notas obtenidas en la materia 3 fue de: {sumaMateria3/5}")

#ejercicio 9
# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.

print("Juego del Ta Te Ti")
casillas = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
sigue = "s"

def tablero(casillas):
    for i9 in range (3):
        for j9 in range (3):
            if j9 < 2:
                print (casillas[i9][j9], end="\t")
            else:
                print (casillas[i9][j9], end="\n")

def turno1(casillas):
    casillas[int(input("Turno del jugador 1 (O). Ingrese la fila seleccionada: "))-1][int(input("Ingrese la columna seleccionada: "))-1] = "O"
    

def turno2(casillas):
    casillas[int(input("Turno del jugador 2 (X). Ingrese la fila seleccionada: "))-1][int(input("Ingrese la columna seleccionada: "))-1] = "X"

tablero(casillas)

while sigue == "s":
    turno1(casillas)
    tablero(casillas)
    sigue = input ("el juego continua? (s/n): ")
    if sigue == "n":
        print("Ganador jugador 1!")
        break
    turno2(casillas)
    tablero(casillas)
    sigue = input ("el juego continua? (s/n): ")
    if sigue == "n":
        print("Ganador jugador 2!")

#ejercicio 10
# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana

totalVendido = [[10, 8, 15, 4], [4, 7, 10, 1], [3, 7, 9, 8], [2, 1, 5, 7], [4, 7, 9, 1], [2, 8, 7, 6], [1, 9, 2, 2]]

producto1 = 0
producto2 = 0
producto3 = 0
producto4 = 0
diaMayorVentas = 0


for i10 in range (len (totalVendido)):
    for j10 in range (4):
        if j10 == 0:
            producto1 = producto1 + totalVendido[i10][j10]
            tempDia = totalVendido[i10][j10]
        elif j10 == 1:
            producto2 = producto2 + totalVendido[i10][j10]
            tempDia = tempDia + totalVendido[i10][j10]
        elif j10 == 2:
            producto3 = producto3 + totalVendido[i10][j10]
            tempDia = tempDia + totalVendido[i10][j10]
        elif j10 == 3:
            producto4 = producto4 + totalVendido[i10][j10]
            tempDia = tempDia + totalVendido[i10][j10]
        if diaMayorVentas < tempDia:
            diaMayorVentas = tempDia
            nroDiaMayorDia = i10 + 1

print(f"Totales vendidos: \n Producto n1: {producto1} unidades \n Producto n2: {producto2} unidades \n Producto n3: {producto3} unidades \n Producto n4: {producto4} unidades")
print(f"el día que más unidades se vendieron en total fue el dia #{nroDiaMayorDia} con {diaMayorVentas} unidades vendidas")

totalPorProducto = [[producto1, "Producto 1"], [producto2, "Producto 2"], [producto3, "Producto 3"], [producto4, "Producto 4"]]
totalPorProducto.sort()
print(f"el producto más vendido fue el {totalPorProducto[3][1]} con {totalPorProducto[3][0]} unidades vendidas")