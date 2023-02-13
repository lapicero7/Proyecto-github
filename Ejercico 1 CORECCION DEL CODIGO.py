def classify_ACL(ACL_number):
    if (ACL_number >= 1 and ACL_number <= 99):
        return "ACL estándar"
    if (ACL_number >= 1300 and ACL_number <= 1999):
        return "ACL estadar extendido"
    elif (ACL_number >= 100 and ACL_number <= 199):
        return "ACL extendida"
    elif (ACL_number >= 2000 and ACL_number <= 2699):
        return "ACL extendida plus"
    else:
        return "Número de ACL inválido"

ACL_number = int(input("Ingrese el número de ACL: "))
print("El tipo de ACL es:", classify_ACL(ACL_number))
