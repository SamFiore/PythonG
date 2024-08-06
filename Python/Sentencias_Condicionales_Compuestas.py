print ("Hola alumno, hoy calcularemos tu promedio.")
print ("------------")
print ("Para empezar necesito saber tu nombre.")
nombre = input("¿Cuál es tu nombre?: -")
print ("Bueno Sr/Sra " + nombre + ", ahora te pediré algunas notas.")
print("Luego sacaré tu promedio.")
nota_mat = float(input("¿Cuál es tu nota en matématicas?: -"))
nota_quimi = float(input("¿Cuál es tu nota en química?: -"))
nota_fisi = float(input("¿Cuál es tu nota en física?: -"))
resultado = (nota_mat + nota_quimi + nota_fisi) / 3
if resultado >= 6 :
    print (' "Aprobaste" con: ', int(resultado))
    print (' "Aprobaste" con: ', round(resultado,2))
else :
    print ("Desaprobaste con:", int(resultado))
    print ("Desaprobaste con:", round(resultado,2))
print("Eso ha sido todo. Suerte.")

