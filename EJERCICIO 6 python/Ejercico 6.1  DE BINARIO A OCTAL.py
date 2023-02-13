def es_palindromo(num):
    # Convertir el número a una cadena
    num_str = str(num)
    
    # Comprobar si la cadena es igual en ambos sentidos
    return num_str == num_str[::-1]
num = int(input("Ingrese el numero a evaluar como palindromo: "))

if es_palindromo(num):
    print(num, "es un número palíndromo")
else:
    print(num, "no es un número palíndromo")
