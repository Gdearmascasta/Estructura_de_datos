# Traspuesta de una matriz 

# Tamaño de la matriz
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

# Crear matrices con tamaño fijo
matriz = [[0]*columnas for i in range(filas)]
traspuesta = [[0]*filas for i in range(columnas)]

# Ingreso de valores
print("Ingrese los valores de la matriz:")
for i in range(filas):
    for j in range(columnas):
        matriz[i][j] = int(input("Elemento ["+str(i)+"]["+str(j)+"]: "))

# Calcular traspuesta
for i in range(filas):
    for j in range(columnas):
        traspuesta[j][i] = matriz[i][j]

# Calcular ancho máximo para alinear la salida
mayor = 0
for i in range(filas):
    for j in range(columnas):
        if matriz[i][j] > mayor:
            mayor = matriz[i][j]
for i in range(columnas):
    for j in range(filas):
        if traspuesta[i][j] > mayor:
            mayor = traspuesta[i][j]

ancho = len(str(mayor)) + 2  

# Mostrar matriz original
print("\nMatriz original:")
for i in range(filas):
    for j in range(columnas):
        print(str(matriz[i][j]).rjust(ancho), end="")
    print()

# Mostrar matriz traspuesta
print("\nMatriz traspuesta:")
for i in range(columnas):
    for j in range(filas):
        print(str(traspuesta[i][j]).rjust(ancho), end="")
    print()