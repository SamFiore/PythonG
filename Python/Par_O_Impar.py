print("""
     --------------------
     Número ¿par o impar?
     --------------------
""")

numero = int(input("Introduce un número entero aquí:"))

resultado = numero % 2
print("")

if resultado == 0:
    print("El número es par.\n")
else :
    print("El número es impar.\n")
print("Fin.")
