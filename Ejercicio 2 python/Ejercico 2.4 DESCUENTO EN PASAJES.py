# Recibir datos de entrada
nombre = input("Ingrese el nombre del pasajero: ")
costo_pasaje = float(input("Ingrese el costo del pasaje: "))
edad = int(input("Ingrese la edad del pasajero: "))
nacionalidad = input("Ingrese la nacionalidad del pasajero: ")

# Aplicar descuento si cumple con los criterios
descuento = 0.0
if (edad <= 12 or (edad > 65 and nacionalidad == "ecuatoriana")):
  descuento = costo_pasaje * 0.4

costo_total = costo_pasaje - descuento

# Mostrar resultados
print("Nombre del pasajero:", nombre)
print("Costo original del pasaje:", costo_pasaje)
print("Descuento aplicado:", descuento)
print("Costo final del pasaje:", costo_total)

