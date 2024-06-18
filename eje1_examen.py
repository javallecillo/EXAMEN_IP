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