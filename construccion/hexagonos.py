import math
from os import system

fmd=0
suma=0
n=int(input("ingresa la distancia en bloques de un lado: "))
i=0
print("\npresiona \"entrer\" para cambiar de linea\n")
while ((suma**2 + i**2)**(1/2) < n) :
    y=(3**(1/2))*(i+1)-suma
    parte, x = math.modf(y)
    suma += x
    i+=1
    
    print("linea {0}: {1} bloques".format(i,int(x)))
    input()
print("terminanste un lado de {} metros".format(n))
system("PAUSE")