class Pato: 
    def __init__ (self):
        print ("pato")

print("""
       -----------
       Calculadora
       -----------
    ]-) Elige una opción:

    1.Suma
    2.Resta
    3.Multiplicación
    4.División
    5.División entera
    6.Módulo
    7.Exponente
    
""")
numero = int(input("Introducir el número de la opción:"))

if numero == 1: 
    vacio = "suma"
    
elif numero == 2:
    vacio = "resta"
    
elif numero == 8:
    vacio = Pato()

while vacio == "suma" :
    numero = 0
    numero = float(input("Introduce el primer número:"))
    numero += float (input("Introduce el segundo número:"))
    print("")
    print("El resultado es:",numero)
    pregunta = str(input("¿Quieres seguir?: "))
    if pregunta == "si":
        vacio == "suma"
    elif pregunta == "no":
        break
    else :
        break


    

while vacio == "resta":
    numero = 0
    numero = float(input("Introduce el primer número:"))
    numero -= float (input("Introduce el segundo número:"))
    print("")
    print("El resultado es:",numero)

#if numero == 3:
  #  numero = 0
 #   numero = float(input("Introduce el primer número:"))
  #  numero *= float (input("Introduce el segundo número:"))
   # print("")
    #print("El resultado es:",numero)

#if numero == 4:
 #   numero = 0
  #  numero = float(input("Introduce el primer número:"))
   # numero /= float (input("Introduce el segundo número:"))
    #print("")
    #print("El resultado es:",numero)

#if numero == 5:
 #   numero = 0
  #  numero = float(input("Introduce el primer número:"))
   # numero //= float (input("Introduce el segundo número:"))
    #print("")
    #print("El resultado es:",numero)

#if numero == 6:
 #   numero = 0
  #  numero = float(input("Introduce el primer número:"))
   # numero %= float (input("Introduce el segundo número:"))
    #print("")
    #print("El resultado es:",numero)

#if numero == 7:
 #   numero = 0
  #  numero = float(input("Introduce el primer número:"))
   # numero **= float (input("Introduce su exponente:"))
    #print("")
    #print("El resultado es:",numero)
    

#print("\nFin.")
