lista1 = []
lista2 = []
lista3 = []
y = 0

for i in range(5):
    x = int(input("Lista 1"))
    lista1.append(x)

for i in range(5):
    x = int(input("Lista 2"))
    lista2.append(x)

print(lista1)
print(lista2)

for i in range(len(lista1)):
    y = y + lista1[i] + lista2[i]

lista3.append(y)
print(lista3)
