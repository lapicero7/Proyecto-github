d = [[1,2,3,7],[4,5,6,8]]
print("arreglo original")

for i in range(2):
    for j in range(4):

        print(d[i][j],end=" ")
    
    print()


v = [0 for k in range(8)]
cont = 0
for j in range(4):
    for i in range(2):
        
        v[cont]=d[i][j]
        cont+=1
print("Arreglo")
print (v)
        
    
