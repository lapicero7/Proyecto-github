# Pidiendo el número octal al usuario
octal = input("Ingrese un número octal: ")

# Convertir el número octal a decimal
decimal = int(octal, 8)

# Convertir el número decimal a binario
binario = bin(decimal)

# Imprimir el número binario resultante
print("El número binario es:", binario[2:])
