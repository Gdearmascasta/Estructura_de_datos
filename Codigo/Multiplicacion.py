# Multiplicación de polinomios con una sola variable

# Multiplicación de polinomios con una sola variable

def leer_grado(mensaje):
    while True:
        try:
            grado = int(input(mensaje))
            if grado >= 0:
                return grado
            else:
                print("El grado del polinomio no puede ser negativo.")
        except ValueError:
            print("Error: debe ingresar un número entero.")


# Función para leer coeficientes sin usar append
def leer_coeficientes(grado, nombre):
    print(f"Ingrese los coeficientes del {nombre} polinomio desde el término independiente hasta x^{grado}:")
    
    coef = [0] * (grado + 1)  # Se crea una lista del tamaño necesario

    for i in range(grado + 1):
        while True:
            try:
                valor = int(input(f"Coeficiente de x^{i}: "))
                coef[i] = valor  # Se guarda directamente en la posición i
                break
            except ValueError:
                print("Error: debe ingresar un número entero.")

    return coef


# Convierte la lista de coeficientes en forma matemática
def polinomio_a_texto(coef):
    texto = ""
    primero = True

    for i in range(len(coef) - 1, -1, -1):
        c = coef[i]

        if c == 0:
            continue

        if not primero:
            texto += " + "

        if i == 0:
            texto += str(c)
        elif i == 1:
            texto += str(c) + "x"
        else:
            texto += str(c) + "x^" + str(i)

        primero = False

    if texto == "":
        return "0"

    return texto


# Programa principal

n = leer_grado("Ingrese el grado del 1er polinomio: ")
m = leer_grado("Ingrese el grado del 2do polinomio: ")

a = leer_coeficientes(n, "primer")
b = leer_coeficientes(m, "segundo")

resultado = [0] * (n + m + 1)

# Multiplicación de polinomios
for i in range(n + 1):
    for j in range(m + 1):
        resultado[i + j] += a[i] * b[j]

print("\nCoeficientes del resultado:")
print(resultado)

print("\nForma matemática del polinomio resultante:")
print(polinomio_a_texto(resultado))