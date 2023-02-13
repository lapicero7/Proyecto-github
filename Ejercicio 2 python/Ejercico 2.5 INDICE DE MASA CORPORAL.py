def calc_IMC(name, mass, height):
  imc = mass / (height**2)
  print(name, "tiene un IMC de", imc, "kg/m^2")
  if imc < 18.5:
    print("Está por debajo del peso recomendado")
  elif 18.5 <= imc < 25:
    print("Está en el peso ideal")
  elif 25 <= imc < 30:
    print("Está por encima del peso ideal")
  else:
    print("Está en un nivel de obesidad")

name = input("Ingrese su nombre: ")
mass = float(input("Ingrese su masa en kg: "))
height = float(input("Ingrese su estatura en metros: "))
calc_IMC(name, mass, height)

