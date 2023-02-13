
tbl = [['a','b','c'],['d','e','f'],['g','h','i']]
for i in range(3):
    for j in range(3):
        print(tbl[i][j],end=" ")
    print(" ")

c = int(input("ingrese la columna a imprimir:  "))

while c > 2:
   c = int(input("ingrese la columna a imprimir:  "))
 
v1 = [0 for i in range(3)]
for acum in range(3):
    v1[acum]=tbl[acum][c]
print("columna ",c," : ",end=" ")
for i in range(3):
    print(v1[i],end=" ")
print(" ")


