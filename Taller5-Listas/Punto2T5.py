lista = []
final = []
i = 0

for i in range(5):
    print("Ingrese la string numero", i + 1)
    x = str(input())
    lista.append(x)

print("La lista inicial es ", lista)

for lista in lista[::-1]:
    final.append(lista)

print("La lista final es ", final)
