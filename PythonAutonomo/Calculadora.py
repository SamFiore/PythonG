class Opciones:
    def __init__(self):
        print("""
            Selecione su opción:
          1_Suma
          2_Resta
          3_Multiplicación
          4_División
          
        """)
        numero1 =  1 #Eliminar
        numero2 = 2 #Eliminar
        print (numero1)
        opcion = int(input("Ponga el número de la opción aquí: "))
        inicio = Cuenta()

class Numeros:
    def __init__(self):
        numero1 = int(input("\n Ingrese el primer número: "))
        numero2 = int(input("\n Ingrese el segundo número: "))
        inicio = Opciones()

opcion = 2 #eliminar

class Cuenta:
    def __init__(self):
        if opcion == "1": 
            numero1 =  1 #Eliminar
            numero2 = 2 #Eliminar
            resultado = numero1 + numero2
            print(resultado)




print("\n       ///CALCULADORA/// \n")

inicio = Numeros()


