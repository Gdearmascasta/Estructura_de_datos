# Rotación tipo dominó de una matriz cuadrada

n = int(input("Ingrese el tamaño de la matriz cuadrada: "))

matriz = [[0]*n for _ in range(n)]

print("Ingrese los valores de la matriz:")
for i in range(n):
    for j in range(n):
        matriz[i][j] = int(input(f"Elemento [{i}][{j}]: "))

k = int(input("Ingrese el número de posiciones a rotar (K): "))
direccion = input("Ingrese direccion (derecha/izquierda): ").lower()

# Mostrar matriz original
print("\nMatriz original:")
for i in range(n):
    for j in range(n):
        print(f"{matriz[i][j]:4}", end="")
    print()

# Convertir matriz a lista
lista = []
for i in range(n):
    for j in range(n):
        lista.append(matriz[i][j])

tam = n*n
k = k % tam

# Rotación
if direccion == "derecha":
    lista = lista[-k:] + lista[:-k]
else:
    lista = lista[k:] + lista[:k]

# Crear matriz rotada
rotada = [[0]*n for _ in range(n)]
indice = 0

for i in range(n):
    for j in range(n):
        rotada[i][j] = lista[indice]
        indice += 1

# Mostrar matriz rotada
print("\nMatriz rotada:")
for i in range(n):
    for j in range(n):
        print(f"{rotada[i][j]:4}", end="")
    print()