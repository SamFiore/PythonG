print("""    ---------
    Conversor
    ---------\n""")

print ("!-Menú de opciones-\n")
print ("Opción 1: Conversor de número a palabra.")
print ("Opción 2: Conversor de palabra a número.\n")

opcion = int(input("Poner número de la opción aquí:"))
print("")

if opcion == 1 :
    print ("   ------------------------")
    print ("   Conversor number to word")
    print ("   ------------------------\n")
    numero = int(input("Ingresa el número aquí:"))
    print ("")
    if numero == 1:
        print ('El número es "uno".\n')
    elif numero == 2:
        print ('El número es "dos".\n')
    elif numero == 3:
        print ('El número es "tres".\n')
    elif numero == 4:
        print ('El número es "cuatro".\n')
    elif numero == 5:
        print ('El número es "cinco".\n')
    else :
        print ("""El número no se reconoce, intente hasta el
numero '5'.\n""")
    

elif opcion == 2 :
    print ("   ------------------------")
    print ("   Conversor word to number")
    print ("   ------------------------\n")
    letra = input("Escriba su número aquí:")
    letra = letra.lower()
    print("")
    if letra == "uno":
        print ('El número es "1".\n')
    elif letra == "dos":
        print ('El número es "2".\n')
    elif letra == "tres":
        print ('El número es "3".\n')
    elif letra == "cuatro":
        print ('El número es "4".\n')
    elif letra == "cinco":
        print ('El número es "5".\n')
    else :
        print ("""El número no se reconoce, intente hasta el
numero 'cinco'.\n""")

else :
    print("Opcíon no encontrada, vuelva a intentarlo.\n")
print("Fin.")

