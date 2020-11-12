# Presentado por: Daniel Gonzalez Bernal
# Codigo: 202023300010

class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        self.stack.pop()

    def esta_vacia(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def inspeccionar(self):
        assert not self.esta_vacia()
        return self.stack[-1]


def pasar(pila):
    if pila.esta_vacia():
        return
    else:
        pilaFinal.push(pila.inspeccionar())
        pilaOriginal.stack.pop()
        pasar(pila)


pilaOriginal = Stack()
pilaFinal = Stack()
datos = [2, 5, 15, 27, 33, 48, 55, 65]
for i in datos:
    pilaOriginal.push(i)

print("La pila Original es: ", pilaOriginal)
print("La pila Final es: ", pilaFinal)
print("Aplicamos el algoritmo...")
pasar(pilaOriginal)
print("La pila Original quedo: ", pilaOriginal)
print("La pila Final quedo: ", pilaFinal)
