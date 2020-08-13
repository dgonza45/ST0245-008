x = int(input("Ingrese la base: "))
y = int(input("Ingrese el exponente: "))

switch = 0  # Estado de respuesta para el print final en un caso normal

if y < 0:  # Estado 1 de respuesta para el print final cuando hay exponente negativo
    switch = 1

if y < 0 and x < 0:  # Estado 2 de respuesta para el print final cuando hay base y exponente negativo
    switch = 2

if y <= 0 and x == 0:  # Casos indeterminados en matematicas
    print("El resultado es indeterminado")
    exit()


def pot(a, b):
    if b < 0:  # Si es necesario modifica el exponente negativo a uno positivo para el calculo
        b = b * -1
    if b == 0:  # Detiene la recursion
        return 1
    else:
        potencia = a * pot(a, b - 1)  # Inicia la recursion
        return potencia


resultado = pot(x, y)  # Inicializa el programa

if switch == 0:
    print("La potencia de", x, "elevado a la", y, "es ", resultado)
if switch == 1:
    print("La potencia de", x, "elevado a la", y, "es  1/", resultado)
if switch == 2:
    print("La potencia de", x, "elevado a la", y, "es  -1/", resultado * -1)
