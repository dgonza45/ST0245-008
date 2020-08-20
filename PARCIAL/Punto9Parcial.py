x = int(input("Ingrese fila a calcular "))
y = int(input("Ingrese columna a calcular "))


def pascal(row, column):
    if row < 0 and column < 0:
        return 0
    elif row == 0 and column == 0:
        return 1
    else:
        print("", combinacion(row-1, column-1), end="")


def combinacion(n, k):
    return int((factorial(n)) / (factorial(k) * (factorial(n - k))))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


pascal(x, y)

