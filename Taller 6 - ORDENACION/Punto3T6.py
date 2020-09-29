# Presentado por: Daniel Gonzalez Bernal
# Codigo: 202023300010

lista = [47, 3, 21, 32, 56, 92]
finaldeseado = [3, 21, 47, 32, 56, 92]


def burbuja(listab):
    stop = 0
    print("Lista original", listab)
    for a in range(len(listab) - 1, 0, -1):
        for i in range(a):
            if listab[i] > listab[i + 1]:
                if stop == 2:
                    break
                temp = listab[i]
                listab[i] = listab[i + 1]
                listab[i + 1] = temp
                stop += 1
                print("Pasada", stop, "burbuja: ", listab)
    print("lista objetivo: ", finaldeseado)


burbuja(lista)
if lista == finaldeseado:
    print("Comprobamos que se uso ordenamiento de burbuja")
# Se puede deducir que se uso el ordenamiento burbuja debido a que este solo ordena 1 numero por pasada
# y en la lista final solo se habian ordenado los 2 numeros mas pequeños, adicionalmente dejo el codigo
# de un burbuja con break a 2 pasadas para comprobar lo que respondi.
