# Multiplicación de matrices 

# Tamaño de la matriz A
filasA = int(input("Ingrese número de filas de A: "))
columnasA = int(input("Ingrese número de columnas de A: "))

# Tamaño de la matriz B
filasB = int(input("Ingrese número de filas de B: "))
columnasB = int(input("Ingrese número de columnas de B: "))

# Verificar si se pueden multiplicar
if columnasA != filasB:
    print("No se pueden multiplicar las matrices")
else:

    # Crear matrices con tamaño fijo
    A = [[0]*columnasA for i in range(filasA)]
    B = [[0]*columnasB for i in range(filasB)]
    resultado = [[0]*columnasB for i in range(filasA)]

    # Ingresar datos de la matriz A
    print("Ingrese los valores de la matriz A")
    for i in range(filasA):
        for j in range(columnasA):
            A[i][j] = int(input("A["+str(i)+"]["+str(j)+"]: "))

    # Ingresar datos de la matriz B
    print("Ingrese los valores de la matriz B")
    for i in range(filasB):
        for j in range(columnasB):
            B[i][j] = int(input("B["+str(i)+"]["+str(j)+"]: "))

    # Multiplicación de matrices
    for i in range(filasA):
        for j in range(columnasB):
            for k in range(columnasA):
                resultado[i][j] = resultado[i][j] + A[i][k] * B[k][j]

    # Calcular el ancho máximo para alinear la salida
    mayor = 0
    for i in range(filasA):
        for j in range(columnasB):
            if resultado[i][j] > mayor:
                mayor = resultado[i][j]

    ancho = len(str(mayor)) + 2  # espacio extra

    # Mostrar matriz resultado 
    print("\nMatriz resultado:")
    for i in range(filasA):
        for j in range(columnasB):
            print(str(resultado[i][j]).rjust(ancho), end="")
        print()