listax = []
columsuma = []
filasuma = []
aux = []
a = 0
b = 0

for x in range(5):
    listay = []
    for y in range(5):
        n = 0
        listay.append(n)
    listax.append(listay)

for x in range(5):
    for y in range(5):
        if a == x and b == y:
            listax[x][y] = 1
            a += 1
            b += 1
for x in listax:
    print(x)

