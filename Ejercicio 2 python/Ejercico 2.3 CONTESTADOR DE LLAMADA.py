def contestar_llamada(num_tlf, h, m):
    if h >= 0 and h < 8:
        return True
    elif h == 8 and m <= 20:
        return True
    elif h >= 13 and h < 20:
        return num_tlf[:3] != "877"
    elif h >= 20 or h < 0:
        return False
    else:
        return num_tlf[-3:] == "909"

num_tlf = input("Ingrese el número de teléfono: ")
h = int(input("Ingrese la hora: "))
m = int(input("Ingrese los minutos: "))

if contestar_llamada(num_tlf, h, m):
    print("Contestar la llamada")
else:
    print("No contestar la llamada")
