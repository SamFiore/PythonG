#Ejemplo para break
print("While con la sentencia break \n")
contador = 0
while contador < 10:
    contador += 1

    if contador == 6:
        break

    print("Valor actual de la variable:", contador)

print("\nFin del programa, la sentencia break se ha ejecutado.")

print("")

#Ejemplo para continue

print ("While con la sentencia continue \n")

contador = 0
while contador < 10:
    contador += 1

    if contador == 5:
        continue
    
    print("Valor actual de la variable:", contador)

print("\nFin del programa, la sentencia continue se ha ejecutado.")
    
