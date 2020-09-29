# Presentado por: Daniel Gonzalez Bernal
# Codigo: 202023300010

lista = [4, 4, 7, 11, 12, 15, 15, 15, 17, 18, 20, 20, 20, 20, 22, 25, 35, 35]
aux = []


for i in range(0, len(lista)-1):
    if lista[i] != lista[i+1]:
        aux.append(lista[i])
if lista[len(lista)-1] == lista[len(lista)-2]:
    aux.append(lista[len(lista)-1])


print(lista)
print(aux)

# Este metodo tiene una complejidad de 2+2n+1+n+n+1+2 , para un total de 4n+4 y un O(n) lineal
# Mientras que el algoritmo en el punto 1 tiene una complijidad total de 3n al cuadrado + 4 y un O(n2) cuadrtica
# Por lo cual comprobamos que es muchisimo mas eficiente trabajar con los datos ordenados.
