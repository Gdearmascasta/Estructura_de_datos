#derivada de un polinimio
def derivada_polinomio(coef):
    n = len(coef)

    if n <= 1:
        return [0]

    resultado = [0] * (n - 1)

    for i in range(1, n):
        resultado[i - 1] = coef[i] * i

    return resultado


def polinomio_a_texto(coef):
    texto = ""
    primero = True

    for i in range(len(coef)-1, -1, -1):
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


n = int(input("Ingrese el grado del polinomio: "))

polinomio = [0] * (n + 1)

for i in range(n + 1):
    polinomio[i] = int(input(f"Coeficiente de x^{i}: "))

derivada = derivada_polinomio(polinomio)

print("Derivada (coeficientes):", derivada)
print("Derivada en forma matemática:", polinomio_a_texto(derivada))