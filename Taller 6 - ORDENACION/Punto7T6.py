# Presentado por: Daniel Gonzalez Bernal
# Codigo: 202023300010

lista = [2, -3, 45, 21, -77, 8, 14, -14, 22, 37, -9]
negativos = []


def busquemosnegativos(x):
    for i in range(len(x)):
        if x[i] < 0:
            negativos.append(x[i])
    return negativos


print("La lista original es: ", lista)
print("La lista solo con los numeros negativos es: ", busquemosnegativos(lista))

# La funcion tiene una complejidad de O(n), el peor de los casos seria si toda la lista esta formada por numeros
# negativos y el tiempo de ejecucion depende  directamente de N (numero de elemntos en la lista) debido a que es
# una funcion lineal.
