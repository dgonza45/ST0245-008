lista = []
y = 0
mayor = 0
menor = 11
for i in range(5):
    print("Ingrese la nota numero", i + 1)
    x = int(input())
    y = y + x
    lista.append(x)

promedio = y / 5

for i in range(len(lista)):
    if lista[i] > mayor:
        mayor = lista[i]
    if lista[i] < menor:
        menor = lista[i]


print("Las notas son", lista)
print("El promedio es", promedio)
print("La nota mayor fue", mayor)
print("La nota menor fue", menor)
