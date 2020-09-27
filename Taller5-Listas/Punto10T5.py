import random

listax = []
columsuma = []
filasuma = []
aux = []

for x in range(5):
    listay = []
    for y in range(5):
        n = random.randint(0, 5)
        listay.append(n)
    listax.append(listay)

for x in listax:
    print(x)

for x in range(5):
    aux = 0
    for y in range(5):
        aux = aux + listax[x][y]
    filasuma.append(aux)

for x in range(5):
    aux = 0
    for y in range(5):
        aux = aux + listax[y][x]
    columsuma.append(aux)


print("La suma de las columnas es: ", columsuma)
print("La suma de las filas es: ", filasuma)
