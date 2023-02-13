def imprime_piramide(altura):
    # Crear un bucle para recorrer cada fila de la pirámide
    for i in range(altura):
        # Calcular el número de asteriscos en cada fila
        num_asteriscos = 2 * i + 1
        
        # Calcular el número de espacios antes de los asteriscos
        num_espacios = altura - i - 1
        
        # Imprimir los espacios y los asteriscos
        print(" " * num_espacios + "*" * num_asteriscos)
altura = int(input("Indique la altura de su pirámide:  "))
imprime_piramide(altura)
