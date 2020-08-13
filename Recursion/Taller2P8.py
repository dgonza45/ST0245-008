i = int(input("Ingrese el número de filas: "))

def pascal(n):
    if (n == 0):
       print("1")
    else:
        pascal(n-1)

        print("1",end = "")
        for i in range(1,n):
            print("",combinacion(n,i),end = "")
        print(" 1")
           
def combinacion(n,k):
    return int((factorial(n))/(factorial(k)*(factorial(n-k))))

def factorial(n):
    if (n == 0):
        return 1
    else:
        return n * factorial(n-1)

pascal(i)