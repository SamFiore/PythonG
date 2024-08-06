print("""
    -----------
    Calculadora
    -----------

  |
  | Sumas
  | Restas
  | División
  |
""")

numero = int(input("Pon tu opción aquí:"))
print("")
if numero == 1:
    print("Has elegido suma")
    numero = 0 
    numero = int(input("Pon el primer número aquí:")) 
    numero += int(input("Pon el segundo número aquí:"))
    print("\nEl resultado es:", numero)

elif numero == 2:
    print("Has elegido resta")
    numero = 0 
    numero = int(input("Pon el primer número aquí:")) 
    numero -= int(input("Pon el segundo número aquí:"))
    print("\nEl resultado es:", numero)

elif numero == 3:
    print("Has elegido División")
    numero = 0 
    numero = int(input("Pon el primer número aquí:")) 
    numero /= int(input("Pon el segundo número aquí:"))
    print("\nEl resultado es:", numero)

else:
    print("La opción no se reconoce. Vuelva a intentarlo.")