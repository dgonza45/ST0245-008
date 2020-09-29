# Presentado por: Daniel Gonzalez Bernal
# Codigo: 202023300010

#  Algoritmo de orden O(n), orden Lineal, abajo explicacion paso a paso

votos = []
lista = []
candidato1 = "Federico"
candidato2 = "Sara"
candidato3 = "Luisa"
c1 = 0
c2 = 0
c3 = 0

print("Para finalizar la votacion ingrese como  ID el numero 0")
print("ID del candidato Federico = 1")
print("ID de la candidata Sara = 2")
print("ID de la candidata Luisa = 3")


# Hasta aqui complejidad de 12 por 12 variables definidas


def votar():
    global c1, c2, c3
    x = -1
    while x != 0:  # Complejidad n + 13 hasta aqui
        x = int(input("Ingrese el ID de su candidato:"))
        votos.append(x)
        if x == 1:  # Ya que solo se aplica maximo un IF por pasada iriamos 4n + 13
            c1 += 1
        if x == 2:
            c2 += 1
        if x == 3:
            c3 += 1
    votos.pop()
    print("Los votos fueron:", votos)
    lista.append(c1)
    lista.append(c2)
    lista.append(c3)  # 4n + 18 hasta aqui
    conteo(lista)  # En la funcion conteo hay un total de +16, quedamos con complejidad de 4n + 34
    # Para una complejidad total del algoritmo de O(n), orden lineal


def conteo(a):
    global c1, c2, c3
    m = 0  # +1
    for i in range(len(a)):  # Aunque es un For en este caso siempre se hara solo con 3 elementos independiente
        if a[i] > m:  # del numero de votos, complejidad 2*(3)+1, para un total de +8 hasta el FOR
            m = a[i]
    if m == c1:
        print("El candidato ID:1", candidato1, "gano con", c1, "votos")
    if m == c2:
        print("El candidato ID:2", candidato2, "gano con", c2, "votos")
    if m == c3:
        print("El candidato ID:3", candidato3, "gano con", c3, "votos")  # Hasta aqui +16


votar()
