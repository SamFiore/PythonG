
print("   ===========")
print("      Rappi   ")
print("   ===========\n")

print("¡Hola! Bienevenido/a para saber tus días de vacaciones.\n")

print("""Empezaremos con el menú de opciones, para saber si eres un usuario que viene
o si no tiene una cuenta, crearemos una.\n""")

input("Press 'Enter' to continue...\n")

print("""
       |------------|
      Menú de opciones
       |------------|

    --
  T|
   | 1~ Unirse 
   |
   | 2~ Crear cuenta
  T| 
    --

""")

opcion = int(input("Escribe el número correspondiente a la opción: "))
print("\n")

if opcion == 2:
    print("Muy bien, necesitamos saber quién eres primero.\n")
    
    nombre = input("Escribe tu nombre a continuación: ")
    print("")
    
    print("Sr/a " + nombre + ", ahora deberás responder un pequeño formulario que determinará los días de vacaciones.\n")
    input ("Press 'Enter' to continue")
    print("")
    
    print("""
        ___________________________________________
       ¿A qué departamento de la empresa perteneces?\n""")
    print("  ]-Puedes escribir la clave o el nombre del departamento.\n")
    clave = input("Escribelo aquí(Sin acentos): ")
    clave = clave.lower()
    print("")
    if clave == "1" or clave == "atencion al cliente":
        print("Bien, sr/a " + nombre + ", vemos que pertenece al departamente de Atención al Cliente o clave 1. Aún nos queda una cosa que preguntarle.\n")
        print("""
           .--------------------------------.
            ¿Cuántos años de servicio tiene?

     ]-Solo es requerido el número sin ningún agregado.
""")
        servicio = int(input("Introduzca los años aquí:"))
        print("")
        if servicio == 1:
            print("\n A usted le corresponden 6 días de vacaciones.\n")
        elif servicio >= 2 and servicio <= 6:
            print("\n A usted le corresponden 14 días de vacaciones.\n")
        elif servicio > 7:
            print("\n A usted le corresponden 20 días de vacaciones.\n")
        else :
            print("\n A usted aún no se le han asignado vacaciones.\n")
            
    elif clave == "2" or clave == "logistica":
        print("Bien, sr/a " + nombre + ", vemos que pertenece al departamente de Logística o clave 2. Aún nos queda una cosa que preguntarle.\n")
        print("""
           .--------------------------------.
            ¿Cuántos años de servicio tiene?

     ]-Solo es requerido el número sin ningún agregado.
""")
        servicio = int(input("Introduzca los años aquí:"))
        print("")
        if servicio == 1:
            print("\n A usted le corresponden 7 días de vacaciones.\n")
        elif servicio >= 2 and servicio <= 6:
            print("\n A usted le corresponden 15 días de vacaciones.\n")
        elif servicio > 7:
            print("\n A usted le corresponden 22 días de vacaciones.\n")
        else :
            print("\n A usted aún no se le han asignado vacaciones.\n")

    elif clave == "3" or clave == "gerencia":
        print("Bien, sr/a " + nombre + ", vemos que pertenece al departamente de Gerencia o clave 3. Aún nos queda una cosa que preguntarle.\n")
        print("""
           .--------------------------------.
            ¿Cuántos años de servicio tiene?

     ]-Solo es requerido el número sin ningún agregado.
""")
        servicio = int(input("Introduzca los años aquí:"))
        print("")
        if servicio == 1:
            print("\n A usted le corresponden 10 días de vacaciones.\n")
        elif servicio >= 2 and servicio <= 6:
            print("\n A usted le corresponden 20 días de vacaciones.\n")
        elif servicio > 7:
            print("\n A usted le corresponden 30 días de vacaciones.\n")
        else :
            print("\n A usted aún no se le han asignado vacaciones.\n")
            
    else :
        print("Dicho departamento no se encuentra en la base de datos, disculpe las molestías. Vuelva a intentarlo.")


elif opcion == 1:
    print("\n ¡Que gusto verte de nuevo! \n")
    print("A continuación, tendrás que introducir los datos correspondientes.")

    print("""
           I-----------I
               Login
           I-----------I
""")

    usuario = input("Introduce tu nombre:")
    usuario = usuario.lower()
    print("")
    
    if usuario == "raul":
        contraseña = input("Introduce la contraseña:")
        if contraseña == "rul33" :
            print("Hola " + usuario + "! Esta es tu base de datos: ")
            print("""
         Y----!*Perfil*!----Y 
         |     __    __     |
         |    /        \    |
         |    |        |    |
         |    |        |    |
         |    \_      _/    |
         |  ____|    |____  |
         | /              \ |
         |------------------

         ]->Nombre: Raul
         ]->Clave: 1
         ]->Años de servicio: 5 años
         ]->Vacaciones: 14 días

""")
        else :
            print("Lo siento. la contraseña es incorrecta, vuelva a intentarlo.")

    elif usuario == "oscar":
        contraseña = input("Introduce la contraseña:")
        if contraseña == "osqui2":
            print("Hola " + usuario + "! Esta es tu base de datos: ")
            print("""
         Y----!*Perfil*!----Y 
         |     __    __     |
         |    /        \    |
         |    |        |    |
         |    |        |    |
         |    \_      _/    |
         |  ____|    |____  |
         | /              \ |
         |------------------

         ]->Nombre: Oscar
         ]->Clave: 2
         ]->Años de servicio: 1 años
         ]->Vacaciones: 7 días

""")
        else :
            print("Lo siento. la contraseña es incorrecta, vuelva a intentarlo.")

    elif usuario == "marina":
        contraseña = input("Introduce la contraseña:")
        if contraseña == "mar52":
            print("Hola " + usuario + "! Esta es tu base de datos: ")
            print("""
         Y----!*Perfil*!----Y 
         |   /-__----__-\   |
         |  / /        \ \  |
         |  | |        | |  |
         |  | |        | |  |
         |  | \_      _/ |  |
         |  | __|    |__ |  |
         |   /          \   |
         |------------------|

         ]->Nombre: Marina
         ]->Clave: 3
         ]->Años de servicio: 8 años
         ]->Vacaciones: 30 días

""")
        else :
            print("Lo siento. la contraseña es incorrecta, vuelva a intentarlo.")
            
    elif usuario == "ignacio":
        contraseña = input("Introduce la contraseña:")
        if contraseña == "igna7":
            print("Hola " + usuario + "! Esta es tu base de datos: ")
            print("""
         Y----!*Perfil*!----Y 
         |     __    __     |
         |    /        \    |
         |    |        |    |
         |    |        |    |
         |    \_      _/    |
         |  ____|    |____  |
         | /              \ |
         |------------------

         ]->Nombre: Ignacio
         ]->Clave: 1
         ]->Años de servicio: Recién iniciado
         ]->Vacaciones: Sin vacaciones disponibles

""")
        else :
            print("Lo siento. la contraseña es incorrecta, vuelva a intentarlo.")

else:
    print("Dicha opción no se reconocio, vuelva a intentarlo.\n")
print("Fin.")
