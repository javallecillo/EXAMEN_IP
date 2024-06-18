import os
os.system('cls' if os.name == 'nt' else 'clear')

print("Vamos a separar letra por letra una palabra \n")

palabra = input("Ingresa una palabra cualquiera: ")

print("Tu palabra letra por letra es: ")

for i in palabra:
    print(i)
