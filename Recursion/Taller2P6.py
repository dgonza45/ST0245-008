i = int(input("Ingrese la posición de la serie de fibonacci: "))

def fibonacci(i):
    if(i < 2):
        return i
    else: 
        return fibonacci(i-1) + fibonacci(i-2)

print("El número %d de la serie de fibonacci es: %d" %(i,fibonacci(i)))