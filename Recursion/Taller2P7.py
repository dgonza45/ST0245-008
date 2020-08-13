x = int(input("Ingrese el numero de discos: "))


def movertorre(altura, inicial, final, aux):
    if altura >= 1:
        movertorre(altura - 1, inicial, aux, final)
        print("Mueve el disco de", inicial, "a", final)
        movertorre(altura - 1, aux, final, inicial)


movertorre(x, "Torre 1", "Torre 3", "Torre 2")