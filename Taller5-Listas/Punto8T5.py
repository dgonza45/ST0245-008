nombre = None
edad = 0
mayor = 0
viejo = 0
lista = []


while nombre != "*":
    nombre = str(input("Ingrese el nombre"))
    if nombre == "*":
        break
    edad = int(input("Ingrese la edad"))
    lista.append([nombre, edad])

print("Los mayores de edad son: ")
for i in lista:
    if i[1] > 17:
        print(i)

for i in lista:
    if i[1] > mayor:
        mayor = i[1]
        viejo = i
print("La persona con mas edad es: ", viejo)
