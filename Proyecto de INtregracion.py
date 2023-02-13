#Damos la bienvenida al usuario
print(" ")
print(" ")
print("                                   HOLA USUARIO!!")
print(" ")
print(" ")
#elec será la entrada para que el usuario tome el control sobre la calculadora
elec = 0
#Abro un while para iniciar un bucle
while elec != 5:
#Usamos algunos print para que el usuario pueda visualizar sus opciones dadas
   print("_______________________________________________________")
   print("""
        indique la operacion a realizar:
            
                 MENÚ PRINCIPAL

        1.- Calcular la Intensidad del circuito
        2.- Resistencia equivalente de un C.Serie
        3.- Resistencia equivalente de un C.Paralelo
        4.- Cacular el Torque de un motor
        5.- salir
        """)
   print("___________   _______   ________   ______    __________")
   print(" ")
#Usamos input con el suso de numeros enteros
   elec = int(input("Introduzca SU Elección :    "))
   print(" ")
   print("_______________________________________________________")
#Iniciamos con if y la variable elec para iniciar un camino con retorno a al menu principal
   if elec == 1:
       print(" ---------------------------")
       print("  Cual es el valor del voltaje del circuito :  ")
       x1 = float(input("      :"))
       print("  valor de la resistencia equivalente  :   ")
       x2 = float(input("      "))
       print("Resultado: ", x1, " / " , x2," = ",x1 / x2, "[Amperios]")
   if elec == 2:
#Iniciamos con if y la variable elec para iniciar un camino con retorno a al menu principal
       print(" ---------------------------")
       print("""  Cuantas resis. tiene el circuito en seria  :
             
             Esta calcladora calcula un max de [2 hasta 6] resistencias""")
       
       x3 = int(input("      :"))
       if x3 == 2:
           
           r1 = float(input("  valor de R1:  "))
           r2 = float(input("  valor de R1:  "))
           print(" ")
           print(" ---------------------------")
           print("Resultado: ", r1, " + " , r2," = ", r1 + r2, "[Ohnmios]" )
       if x3 == 3:
           
           r1 = float(input("  valor de R1:  "))
           r2 = float(input("  valor de R2:  "))
           r3 = float(input("  valor de R3:  "))
           print(" ")
           print(" ")
           print("Resultado: ", r1, " + " , r2, " + ", r3," = ", r1 + r2 + r3, "[Ohnmios]" )
       if x3 == 4:

           r1 = float(input("  valor de R1:  "))
           r2 = float(input("  valor de R2:  "))
           r3 = float(input("  valor de R3:  "))
           r4 = float(input("  valor de R4:  "))
           print(" ")
           print(" ---------------------------")
           print("Resultado: ", r1, " + " , r2, " + ", r3, " + ", r4, " = ", r1 + r2 + r3 + r4, "[Ohnmios]" )
       if x3 == 5:
           
           r1 = float(input("  valor de R1:  "))
           r2 = float(input("  valor de R2:  "))
           r3 = float(input("  valor de R3:  "))
           r4 = float(input("  valor de R4:  "))
           r5 = float(input("  valor de R5:  "))
           print(" ")
           print(" ---------------------------")
           print("Resultado: ", r1, " + " , r2, " + ", r3, " + ", r4," + ", r5, " = ", r1 + r2 + r3 + r4 + r5,"[Ohnmios]" )
       if x3 == 6:
           
           r1 = float(input("  valor de R1:  "))
           r2 = float(input("  valor de R2:  "))
           r3 = float(input("  valor de R3:  "))
           r4 = float(input("  valor de R4:  "))
           r5 = float(input("  valor de R5:  "))
           r6 = float(input("  valor de R6:  "))
           print(" ")
           print(" ---------------------------")
           print("Resultado: ", r1, " + " , r2, " + ", r3, " + ", r4," + ", r5," + ", r6, " = ", r1 + r2 + r3 + r4 + r5 + r6,"[Ohnmios]" )
          
   if elec == 3:
#Iniciamos con if y la variable elec para iniciar un camino con retorno a al menu principal
       print(" ---------------------------")
       print("""" Cuantos calculos en paralelo existen: 
             
             Recueerde esta calculaddora solo le permite usar un max de 4 calculos paralelos !!
             """)
       x4 = int(input("     :"))
       if x4 == 2:
           print(" ---------------------------")
           p1 = float(input("  valor de R1:  "))
           p2 = float(input("  valor de R2:  "))
           a = (p1 * p2)/(p1 + p2)
           print(" ")
           print("Resultado del 1° paralelo es:  ", a, "[Ohnmios]")
           p3 = float(input("  valor de R3:  "))
           p4 = float(input("  valor de R4:  "))
           a1 = (p3 * p4)/(p3 + p4)
           print("Resultado del 2° paralelo es:  ", a1, "[Ohnmios]")
           print(" ")
           print("  La resistencia equivalente del circuito en paralelo es: ", a + a1, "[Ohnmios]")
           
       if x4 == 3:
           print(" ---------------------------")
           p1 = float(input("  valor de R1:  "))
           p2 = float(input("  valor de R2:  "))
           a = (p1 * p2)/(p1 + p2)
           print(" ")
           print("Resultado del 1° paralelo es:  ", a, "[Ohnmios]")
           p3 = float(input("  valor de R3:  "))
           p4 = float(input("  valor de R4:  "))
           a1 = (p3 * p4)/(p3 + p4)
           print("Resultado del 2° paralelo es:  ", a1, "[Ohnmios]")
           print(" ")
           p5 = float(input("  valor de R5:  "))
           p6 = float(input("  valor de R6:  "))
           a2 = (p5 * p6)/(p5 + p6)
           print(" ")
           print("Resultado del 1° paralelo es:  ", a2, "[Ohnmios]")
           print(" ")
           print("  La resistencia equivalente del circuito en paralelo es: ", a + a1 + a2, "[Ohnmios]")
           
       if x4 == 4:
           print(" ---------------------------")
           p1 = float(input("  valor de R1:  "))
           p2 = float(input("  valor de R2:  "))
           a = (p1 * p2)/(p1 + p2)
           print(" ")
           print("Resultado del 1° paralelo es:  ", a, "[Ohnmios]")
           p3 = float(input("  valor de R3:  "))
           p4 = float(input("  valor de R4:  "))
           a1 = (p3 * p4)/(p3 + p4)
           print("Resultado del 2° paralelo es:  ", a1, "[Ohnmios]")
           print(" ")
           p5 = float(input("  valor de R5:  "))
           p6 = float(input("  valor de R6:  "))
           a2 = (p5 * p6)/(p5 + p6)
           print("Resultado del 3° paralelo es:  ", a2, "[Ohnmios]")
           print(" ")
           p7 = float(input("  valor de R7:  "))
           p8 = float(input("  valor de R8:  "))
           a3 = (p7 * p8)/(p7 + p8)
           print(" ")
           print("Resultado del 1° paralelo es:  ", a3, "[Ohnmios]")
           print(" ")
           print("  La resistencia equivalente del circuito en paralelo es: ", a + a1 + a2, "[Ohnmios]")

   if elec == 4:
#Iniciamos con if y la variable elec para iniciar un camino con retorno a al menu principal
       print(" ---------------------------")
       print("""         TORQUE  """)
       print(" ")
       hp = float(input("  Porvafor introduzca el valor de HP:  "))
       rpm = float(input("  Porfavor introduzcala rpm [revolucioes por minuto]:  "))
       Torque = (hp * 716) / rpm
       print(" ")
       print("  El resultado del Torque es: ", Torque, "[Newtons]")
       print(" ")
   if elec == 5:
#para finalizar el programa
       print(" ")
       print("""                  GRACIAS POR USARME!
                     TE EXTRAÑARÉ
                        (T.T)/  """)

   
            
