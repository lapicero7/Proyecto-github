import random

print("arreglo original")
d=[[0 for j in range(3)]for i in range(3)]
for i in range(3):
    for j in range(3):
        d[i][j]=random.randint(100,199)


for i in range(3):
    for j in range(3):
        print(d[i][j],end=" ")
    print("")


vec=[0 for i in range(3)]
cont=0
print("diagonal principal: ")
for i in range(3):
    for j in range(3):
        if i ==j:
            vec[cont]=d[i][j]
            cont+=1

for i in range(3):
    print(vec[i], end="  ")
print("")
            


