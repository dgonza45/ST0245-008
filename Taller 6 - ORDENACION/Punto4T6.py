# Presentado por: Daniel Gonzalez Bernal
# Codigo: 202023300010

listashell = [8, 43, 17, 6, 40, 16, 18, 97, 11, 7]
pasadas = 0

print("La lista inicial es: ", listashell)


def shellsort(lista):
    mitad = len(lista) // 2
    while mitad > 0:
        for posicion_inicial in range(mitad):  # ir al esta el rango que se llama mitad
            reducir_busqueda(lista, posicion_inicial, mitad)
        mitad = mitad // 2


def reducir_busqueda(nlist, start, gap):
    global pasadas
    for i in range(start + gap, len(nlist), gap):  # gap es el salto que se va dar
        pasadas += 1
        print("Pasada", pasadas, "con brecha de", gap, "la lista es: ", listashell)
        current_value = nlist[i]
        posicion = i
        while posicion >= gap and nlist[posicion - gap] > current_value:
            nlist[posicion] = nlist[posicion - gap]
            posicion = posicion - gap
        nlist[posicion] = current_value


shellsort(listashell)
print("La lista final quedo ordenada: ", listashell)
