import random
print("A")
co1=int(input("ingrese #columnas: "))
fi1=int(input("ingrese #filas: "))
ma1=[[0 for j in range(co1)]for i in range(fi1)]
print("B")
co2=int(input("ingrese #columnas: "))
fi2=int(input("ingrese #filas: "))
ma2=[[0 for j in range(co2)]for i in range(fi2)]



while(co1!=fi2):
    print("A")
    co1=int(input("ingrese #columnas: "))
    fi1=int(input("ingrese #filas: "))
    ma1=[[0 for j in range(co1)]for i in range(fi1)]
    print("B")
    co2=int(input("ingrese #columnas: "))
    fi2=int(input("ingrese #filas: "))
    ma2=[[0 for j in range(co2)]for i in range(fi2)]

print("A")
for i in range(fi1):
    for j in range(co1):
        ma1[i][j]=int(input("ingrese valores posicion "))
print("B")
for i in range(fi2):
    for j in range(co2):
        ma2[i][j]=int(input("ingrese valores posicion "))


matriz=[[0 for j in range(co2)]for i in range(fi1)]

suma=0
for k in range(co2):
    for i in range(fi1):
        suma=0
        for j in range(co1):
            suma+=ma1[i][j]*ma2[j][k]
        matriz[i][k]=suma
print("resultado: ")
for i in range(fi1):
    for j in range(co2):
        print(matriz[i][j],end=" ")
    print()
        
        
    
