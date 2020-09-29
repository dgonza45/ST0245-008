# Presentado por: Daniel Gonzalez Bernal
# Codigo: 202023300010

futbolistasTup = [(1, "Casillas"), (15, "Ramos"), (3, "Pique"), (5, "Puyol"), (11, "Capdevila"),
                  (14, "Xabi Alonso"), (16, "Busquets"), (8, "Xavi Hernandez"), (18, "Pedrito"),
                  (6, "Iniesta"), (7, "Villa")]

futbolistasTup.sort(key=lambda futbolista: futbolista[0])

print(futbolistasTup)

#  A. El metodo .sort ordena las duplas, en este caso segun el numero de jugardor (la posicion 0).

#  B. El Key lambda se usa para definir una funcion que retornara solo un dato individual, en este caso
# el valor en la posicion 0 de la dupla y asi poder ejecutar el sort en base a el.

#  C. Puedo concluir que el metodo .sort en python sirve para ordenar (de menor a mayor en este caso)

lista = [4, 7, 11, 4, 9, 5, 11, 7, 3, 5]
lista2 = [47, 3, 21, 32, 56, 92]
listashell = [8, 43, 17, 6, 40, 16, 18, 97, 11, 7]
print("La lista 1 original es: ", lista)
print("La lista 2 original es: ", lista2)
print("La lista 3 original es: ", listashell)
lista.sort()
lista2.sort()
listashell.sort()
print("La lista 1 obtenida es: ", lista)
print("La lista 2 obtenida es: ", lista2)
print("La lista 3 obtenida es: ", listashell)

#  D.
inventos2019 = [("GeoOrbital", 70), ("Solar Suitcase", 80), ("Airpods Pro", 37), ("Mookkie", 55), ("LinkSquare", 50)]
inventos2019.sort(key=lambda inventos: inventos[1])
print(inventos2019)
