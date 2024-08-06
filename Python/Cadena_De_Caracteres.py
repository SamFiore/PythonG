print ("Cadena de carácteres:")

mensaje = "Hola"
mensaje += " "
mensaje += "mundo"
print (mensaje)

print ("----------")

print ("Concatenación:")

Mensaje = "Hola"
espacio = " "
nombre = "mundo"
print (Mensaje + espacio + nombre)

print ("----------")
print ("Cadena + concatación")
numero_uno = 3
numero_dos = 10
resultado = numero_uno + numero_dos
resultado = str(resultado)
print ("El resultado es: " + resultado)

print ("----------")
print ("Buscar subcadenas:")

mensaje2 = "Hola mundo"
buscar_subcadena = mensaje2.find("mundo")
print(buscar_subcadena)

print ("----------")
print ("Extraer subcadenas:")

mensaje3 = "Hola mundo"
extraer_subcadena = mensaje3[5:10]
print (extraer_subcadena)

print ("----------")
print ("Comparación:")
mensaje_uno = "Hola"
mensaje_dos = "Hola"
print (mensaje_uno == mensaje_dos)

mensaje_tres = "Hola"
mensaje_cuatro = "Adios"
print (mensaje_tres == mensaje_cuatro)
