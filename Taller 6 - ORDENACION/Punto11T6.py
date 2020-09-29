# Presentado por: Daniel Gonzalez Bernal
# Codigo: 202023300010

import random

listaa = []
listab = []
listac = []

for q in range(100):
    m = random.randint(1, 100)
    listaa.append(m)

for e in range(60):
    y = random.randint(1, 100)
    listab.append(y)

print("La lista A es:", listaa)
print("La lista B es:", listab)


def sort(array):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return sort(less) + equal + sort(greater)
    else:
        return array


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


print("La lista A ordenada es :", quicksort(listaa))
print("La lista B ordenada es :", quicksort(listab))
listac = listaa + listab
print("La lista C es:", listac)
print("La lista C ordenada es :", quicksort(listac))
