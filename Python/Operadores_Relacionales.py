print ("   ----------")
print ("   Comparador")
print ("   ----------\n")

num_uno = int(input("Introduce el 1er número:"))
num_dos = int(input("Introduce el 2do número:"))
print("")
if num_uno < num_dos :
    print(num_uno, "es menor que ", num_dos)
if num_uno > num_dos :
    print(num_uno, "es mayor que ", num_dos)
if num_uno == num_dos :
    print(num_uno, "es igual a ", num_dos)
if num_uno != num_dos :
    print(num_uno, "no es igual a ", num_dos)
if num_uno <= num_dos :
    print(num_uno, "es menor o igual a ", num_dos)
if num_uno >= num_dos :
    print(num_uno, "es mayor o igual a ", num_dos)
else :
    ("Dicho código no se reconoce, vuelva a intentar")
print("")
print("Fin.")

