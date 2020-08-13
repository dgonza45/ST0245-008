s = input("Ingrese una palabra: ")

def imprimir(s):
    if(len(s) == 1):
        print(s)
    else:
        imprimir(s[0:len(s)-1])
        print(s)

imprimir(s)        