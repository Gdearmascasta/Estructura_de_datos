# Triángulo de Pascal ( con las consideraciones vistas en clase)

niveles = int(input("Ingrese el número de niveles: "))

# Crear matriz
matriz = [[0]*niveles for i in range(niveles)]

# Calcular valores
for i in range(niveles):
    for j in range(i+1):
        if j == 0 or j == i:
            matriz[i][j] = 1
        else:
            matriz[i][j] = matriz[i-1][j-1] + matriz[i-1][j]

# Encontrar número más grande
mayor = 0
for i in range(niveles):
    for j in range(niveles):
        if matriz[i][j] > mayor:
            mayor = matriz[i][j]

ancho = len(str(mayor)) + 2

print("\nTriángulo de Pascal:\n")

for i in range(niveles):

    # Espacios para centrar
    for s in range((niveles - i) * ancho // 2):
        print(" ", end="")

    # Imprimir números
    for j in range(i+1):
        print(str(matriz[i][j]).center(ancho), end="")

    print()