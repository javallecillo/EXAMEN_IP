#limpiar consola
import os
os.system('cls' if os.name == 'nt' else 'clear')
import  TotalDepartamentos 

#declaracion de variables para iniciar sesion
usuario = "admin"
contrasenia = "admin123"
contraseniaInversa = contrasenia[::-1]
acceso = False

#Inicio de sesion
usu = input("Ingrese el usuario: ")

#Verificacion de usuario
if usu == usuario:
    intento = input("Ingresa tu contraseña: ")
    intentoInverso = intento[::-1]

    #Verificacion de contraseña
    if intento == contrasenia and intentoInverso == contraseniaInversa and contraseniaInversa[2::2] == intentoInverso[2::2]:
        acceso = True

        #Menu de opciones y hacer mayusculas las opciones
        import os
        os.system('cls' if os.name == 'nt' else 'clear')

        opcion = "S"
        while opcion.upper() == "S":
            print("Ingrese lo que desea hacer \n 1. Ver su departamento y municipio junto con su edad \n 2. Ver solo su municipio \n 3. Saber si eres mayor de edad \n 4. Separar palabra letra por letra \n 5. Salir")
            deseo = int(input("\nIngresa un numero de las opciones: "))

            if deseo == 1:
                import os
                os.system('cls' if os.name == 'nt' else 'clear')
                
                #petición de cedula
                print("Ingrese su numero de cedula")
                cedula = input()
                if len(cedula) >= 8 :  
                    try:
                        ano = int(cedula[4:8])
                        departamento = str(cedula[0:4])
                        edad = 2024 - ano

                        #if para mostrat el departamento y la edad
                        if departamento in TotalDepartamentos.Departamentos and ano <= 2024:  
                            print("Su departamento es:", TotalDepartamentos.Departamentos[departamento], "\nSu edad es:", edad)
                        else:
                            print("Algo salio mal, vuelve a intentarlo")

                    except ValueError:
                        print("La cedula debe contener numeros validos para el año y el departamento")
                    
                    #peticion para hacer nueva accion
                    print("Desea Hacer otra cosa? S/N")
                    opcion = input()
                    import os
                    os.system('cls'if os.name == 'nt' else 'clear')
                    




#if para comparar departamento y mostrar sus municipios
            elif deseo == 2:
                import os
                os.system('cls' if os.name == 'nt' else 'clear')
                

                print("Ingrese su numero de cedula")
                cedula = input()
                municipio = str(cedula[0:2])
                print("Los municipios de su departamento son:")
                if municipio == "01":
                    for clave, valor in TotalDepartamentos.Atlantida.items():
                        print(clave, valor)
                elif municipio == "02":
                        for clave, valor in TotalDepartamentos.Colon.items():
                            print(clave, valor)
                elif municipio == "03":
                        for clave, valor in TotalDepartamentos.Comayagua.items():
                            print(clave, valor)        
                elif municipio == "04":
                        for clave, valor in TotalDepartamentos.Copan.items():
                            print(clave, valor)
                elif municipio == "05":
                        for clave, valor in TotalDepartamentos.Cortes.items():
                            print(clave, valor)
                elif municipio == "06":
                        for clave, valor in TotalDepartamentos.Choluteca.items():
                            print(clave, valor)
                elif municipio == "07":
                        for clave, valor in TotalDepartamentos.Paraiso.items():
                            print(clave, valor)
                elif municipio == "08":
                        for clave, valor in TotalDepartamentos.Morazan.items():
                            print(clave, valor)
                elif municipio == "09":
                        for clave, valor in TotalDepartamentos.Gracias.items():
                            print(clave, valor)
                elif municipio == "10":
                        for clave, valor in TotalDepartamentos.Intibuca.items():
                            print(clave, valor)
                elif municipio == "11":
                        for clave, valor in TotalDepartamentos.Isla.items():
                            print(clave, valor)
                elif municipio == "12":
                        for clave, valor in TotalDepartamentos.Paz.items():
                            print(clave, valor)
                elif municipio == "13":
                        for clave, valor in TotalDepartamentos.Lempira.items():
                            print(clave, valor)
                elif municipio == "14":
                        for clave, valor in TotalDepartamentos.Ocotepeque.items():
                            print(clave, valor)
                elif municipio == "15":
                        for clave, valor in TotalDepartamentos.Olancho.items():
                            print(clave, valor)
                elif municipio == "16":
                        for clave, valor in TotalDepartamentos.Santa.items():
                            print(clave, valor)
                elif municipio == "17":
                        for clave, valor in TotalDepartamentos.Valle.items():
                            print(clave, valor)
                elif municipio == "18":
                        for clave, valor in TotalDepartamentos.Yoro.items():
                            print(clave, valor)  
            
                print("Desea Hacer otra cosa? S/N")
                opcion = input() 
                import os
                os.system('cls'if os.name == 'nt' else 'clear')

            #ejercicio 1
            elif deseo == 3:
                import os
                os.system('cls' if os.name == 'nt' else 'clear')

                print("Desea saber si es mayor de edad o no?\n")

                edad = int(input("Ingrese su edad en numeros: "))

                if edad > 0 and edad < 18:
                    print("Aún eres menor de edad!")
                elif edad >= 18:
                    print("Ya eres mayor de edad!")
                else:
                    print("El dato ingresado es incorrecto")

                #peticion para hacer nueva accion
                print("Desea Hacer otra cosa? S/N")
                opcion = input()
                import os
                os.system('cls'if os.name == 'nt' else 'clear')

            #ejercicio 11
            elif deseo == 4:
                import os
                os.system('cls' if os.name == 'nt' else 'clear')

                print("Vamos a separar letra por letra una palabra \n")

                palabra = input("Ingresa una palabra cualquiera: ")

                print("Tu palabra letra por letra es: ")

                for i in palabra:
                    print(i)

                #peticion para hacer nueva accion
                print("Desea Hacer otra cosa? S/N")
                opcion = input()
                import os
                os.system('cls'if os.name == 'nt' else 'clear')

            elif deseo == 5:
                 exit(0)

    #deteccion de usuarios incorrectas
    else:
        print("Credenciales incorrectas")
else:
    print("Credenciales incorrectas")
            