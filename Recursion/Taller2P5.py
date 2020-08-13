x = str(input("Digite una palabra o numero: "))
x = x.replace(" ", "")  # Quita los espacios en blanco para poder analizar los caracteres correctamente
y = len(x) - 1
z = 0


def palindromos(a, b, c):
    if c == len(a) - 1:  # Detiene la recursion al llegar al ultimo valor de la string
        # Si llega hasta aqui es palindromo o capicua
        print("La palabra o numero", a, "es un palindromo o un numero capicua")
        return
    else:
        if a[c] == a[b]:  # Compara el primer caracter con el ultimo
            return palindromos(a, b - 1, c + 1)  # Inicia la recursion moviendo los indices
        else:
            # Si los extremos no son iguales terminara el programa
            return print("La palabra o numero", a, "no es un palindromo ni un numero capicua")


palindromos(x, y, z)
