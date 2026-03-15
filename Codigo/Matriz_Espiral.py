# Crear matriz 4x5 llena de ceros
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

matriz = [[0 for _ in range(columnas)] for _ in range(filas)]

# Límites de la espiral
arriba = 0
abajo = filas - 1
izquierda = 0
derecha = columnas - 1

numero = 1

while arriba <= abajo and izquierda <= derecha:
    
    # 1. Izquierda → Derecha
    for j in range(izquierda, derecha + 1):
        matriz[arriba][j] = numero
        numero += 1
    arriba += 1

    # 2. Arriba ↓ Abajo
    for i in range(arriba, abajo + 1):
        matriz[i][derecha] = numero
        numero += 1
    derecha -= 1

    # 3. Derecha ← Izquierda
    if arriba <= abajo:
        for j in range(derecha, izquierda - 1, -1):
            matriz[abajo][j] = numero
            numero += 1
        abajo -= 1

    # 4. Abajo ↑ Arriba
    if izquierda <= derecha:
        for i in range(abajo, arriba - 1, -1):
            matriz[i][izquierda] = numero
            numero += 1
        izquierda += 1

# Mostrar matriz
for fila in matriz:
    print(fila)