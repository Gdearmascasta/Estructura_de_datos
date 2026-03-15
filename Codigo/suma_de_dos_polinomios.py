# Suma de dos polinomios
# Pueden sumarse dos polinomios de diferente grado


# Función para leer el grado del polinomio 
def leer_grado(mensaje):

    while True:
        try:
            grado = int(input(mensaje))

            # el grado no puede ser negativo
            if grado >= 0:
                return grado
            else:
                print("El grado no puede ser negativo.")

        except ValueError:
            print("Debe ingresar un número entero.")


# Función para sumar dos polinomios
def suma_polinomios(a, b):

    n = len(a)
    m = len(b)

    # el tamaño del resultado será el mayor de los dos
    if n > m:
        tamaño = n
    else:
        tamaño = m

    resultado = [0] * tamaño

    # recorrer todos los coeficientes
    for i in range(tamaño):

        if i < n:
            coef_a = a[i]
        else:
            coef_a = 0

        if i < m:
            coef_b = b[i]
        else:
            coef_b = 0

        resultado[i] = coef_a + coef_b

    return resultado


# convertir el polinomio a forma matemática
def polinomio_a_texto(coef):

    texto = ""
    primero = True

    for i in range(len(coef) - 1, -1, -1):

        c = coef[i]

        if c == 0:
            continue

        if not primero:
            texto = texto + " + "

        if i == 0:
            texto = texto + str(c)

        elif i == 1:
            texto = texto + str(c) + "x"

        else:
            texto = texto + str(c) + "x^" + str(i)

        primero = False

    if texto == "":
        return "0"

    return texto





n = leer_grado("Ingrese el grado del primer polinomio: ")
m = leer_grado("Ingrese el grado del segundo polinomio: ")


# crear listas de coeficientes
a = [0] * (n + 1)
b = [0] * (m + 1)


# leer coeficientes del primer polinomio
print("Ingrese los coeficientes del primer polinomio")

for i in range(n + 1):

    while True:
        try:
            a[i] = int(input("Coeficiente de x^" + str(i) + ": "))
            break
        except ValueError:
            print("Debe ingresar un número entero.")


# leer coeficientes del segundo polinomio
print("Ingrese los coeficientes del segundo polinomio")

for i in range(m + 1):

    while True:
        try:
            b[i] = int(input("Coeficiente de x^" + str(i) + ": "))
            break
        except ValueError:
            print("Debe ingresar un número entero.")


resultado = suma_polinomios(a, b)


# mostrar resultados
print("\nCoeficientes del resultado:")
print(resultado)

print("\nForma matemática:")
print(polinomio_a_texto(resultado))