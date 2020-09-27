listax = []


for x in range(5):
    listay = []
    for y in range(15):
        n = 0
        listay.append(n)
    listax.append(listay)

for x in range(15):
    listax[0][x] = 1
    listax[4][x] = 1
for x in range(5):
    listax[x][0] = 1
    listax[x][14] = 1

for x in listax:
    print(x)
