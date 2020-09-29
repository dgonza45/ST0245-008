# Presentado por: Daniel Gonzalez Bernal
# Codigo: 202023300010

listax = [21, 1, 26, 45, 29, 28, 2, 9, 16, 49, 39, 27, 43, 34, 46, 40]


# El resultado despues de 3 llamadas recursivas sera  [21,1], en la primera llamada toma la mitad de la lista
# quedando como resultado [21, 1, 26, 45, 29, 28, 2, 9], en la segunda llamada recursiva se parte de nuevo
# a la mitad quedando [21, 1, 26, 45] y en la 3er llamada se parte a la mitad quedando [21, 1].

# Para probar lo dicho anteriormente implementare el algoritmo con un stop al 3r paso e imprimir el resultado.
contador = 0


def ordenamientopormezcla(lista):
    global contador
    if contador == 3:
        print(lista)
        quit()
    contador += 1

    if len(lista) > 1:
        mitad = len(lista) // 2
        mitadIzquierda = lista[:mitad]
        mitadDerecha = lista[mitad:]

        ordenamientopormezcla(mitadIzquierda)
        ordenamientopormezcla(mitadDerecha)

        i = 0
        j = 0
        k = 0
        while i < len(mitadIzquierda) and j < len(mitadDerecha):
            if mitadIzquierda[i] < mitadDerecha[j]:
                lista[k] = mitadIzquierda[i]
                i = i + 1
            else:
                lista[k] = mitadDerecha[j]
                j = j + 1
            k = k + 1

        while i < len(mitadIzquierda):
            lista[k] = mitadIzquierda[i]
            i = i + 1
            k = k + 1

        while j < len(mitadDerecha):
            lista[k] = mitadDerecha[j]
            j = j + 1
            k = k + 1
    return lista


print(ordenamientopormezcla(listax))
