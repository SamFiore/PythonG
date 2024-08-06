print("""
      ------------------------------
      ¿Cuál es el número más grande?
      ------------------------------
""")

num_uno = int(input("Introduce el primer número:"))
num_dos = int(input("Introduce el segundo número:"))
num_tres = int(input("Introduce el segundo número:"))
print("")

if num_uno > num_dos and num_uno > num_tres:
    print("El número ", num_uno, " es el mayor de los tres.")
elif num_dos > num_uno and num_dos > num_tres:
    print("El número ", num_dos, " es el mayor de los tres.")
elif num_tres > num_dos and num_tres > num_uno:
    print("El número ", num_tres, " es el mayor de los tres.")
else:
    print("Los número son iguales.")
print("\n Fin.\n")

