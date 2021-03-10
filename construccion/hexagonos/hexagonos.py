import math
from os import system

suma=0
n=int(input("ingresa la distancia en bloques de un lado: "))
i=0
lonj = aux = 0
print("\npresiona \"entrer\" para cambiar de linea\n")
while (round(aux) < n) :
    y=(3**(1/2))*(i+1)-suma
    parte, x = math.modf(y)
    
    suma += x
    i+=1
    aux = lonj = (suma**2 + i**2)**(1/2)
    if(round(lonj) > n) :
        x-=1
        suma-=1
        lonj= (suma**2 + i**2)**(1/2)
        
    print("linea {0}: {1} bloques--------{2}".format(i,int(x), lonj))
    input()
print("terminanste un lado de {} metros".format(lonj))
system("PAUSE")