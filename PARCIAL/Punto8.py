x = int(input("Ingrese sus 2 ultimos digitos de la cedula: "))


def punto8(n):
    if n == 0:
        return
    else:
        print(n)
        punto8(n - 1)


punto8(x)
