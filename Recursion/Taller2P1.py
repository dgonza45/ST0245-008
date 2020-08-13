x = int(input("Ingrese el primer numero: "))
y = int(input("Ingrese el segundo numero: "))


def mcd(a, b):
    if b > a:   # Organiza los numeros
        aux = b
        b = a
        a = aux
    if b < 0:   # Evita una recursion infinita si ingresan ambos numeros negativos
        aux = a * -1
        a = b * -1
        b = aux
    if a % b == 0:  # Detiene la recursion
        return b
    else:
        return mcd(b, a % b)  # Donde la magia sucede


print("El maximo comun divisor entre", x, "y", y, "es: ", mcd(x, y))
