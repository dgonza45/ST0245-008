import random


def generador(x):
    lista = []
    for i in range(x):
        n = random.randint(1, 10)
        lista.append(n)
        print(lista[i])
        print("El cuadrado es", lista[i] ** 2)
        print("El cubo es", lista[i] ** 3)


generador(10)
