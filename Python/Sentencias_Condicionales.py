num_uno = 5

if num_uno == 5:
    print("El número es cinco")
print("Fin.")

print("--------")

num_dos = 8

if num_dos == 5:
    print("Hola")
print ("Fin.")

print ("-------")

nombre = input("¿Cuál es tu nombre: ")
print ("Hola " + nombre + ", vamos a calcular tu promedio")
nota_mate = int(input("Tu nota en Matématica: "))
nota_fisica = int (input ("Tu nota en Física: "))
nota_quimi = int (input ("Tu nota en Química: "))
resultado = (nota_mate + nota_fisica + nota_quimi) / 3
print ("Tu promedio es: ", int(resultado))
if resultado >= 6 :
    print ("Aprobaste")
print("Fin.")
