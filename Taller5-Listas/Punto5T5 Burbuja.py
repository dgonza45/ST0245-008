import random

lista = []

for x in range(9):
    n = random.randint(0, 100)
    lista.append(n)


def burbuja(listab):
    for a in range(len(listab) - 1, 0, -1):
        for i in range(a):
            if listab[i] > listab[i + 1]:
                temp = listab[i]
                listab[i] = listab[i + 1]
                listab[i + 1] = temp


print("La lista sin ordenar es", lista)
burbuja(lista)
print("Ordenadita es mas bonita", lista)
