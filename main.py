from User import *
from Player import *
from Avatar import * 
from Games import Games
import Cuartos
import random
from movimiento import *


def registro_usuario(users):

    num_registro = len(users) + 1
    print('Tenga en cuenta que su usuario debe ser de al menos 6 caracteres de largo!')
    user = input('Escriba el nombre de su usuario: ')
    while len(user) < 6:
        user = input("Tu nombre no es lo suficientemente largo, intenta con un nombre nuevo!\n >>>")

    if user in users:#in data.txt
        print(f"El usuario {user} ya existe en la base de datos. Por favor introduzca la contraseña")
    else:
        print('Usuario nuevo! Bienvenido!')

    password = input('Escriba su contraseña: ')
    while len(password) < 6:
        password = input("Tu contraseña no es lo suficientemente largo, intenta con una contraseña nueva!\n >>>")
        
    if password in users:#in data.txt
        print("Contraseña valida")
    else:
        print("Contraseña no compatible")

    print('Para poder jugar este juego, tu edad minima debe de ser de 8 años!')
    age = input('Ingrese su edad: ')
    if int(age) < 8 and age.isnumeric():
        age = input('No cumples con la edad minima para poder jugar, prueba de nuevo en unos años ;) , o simplemente prueba poniendo una edad nueva!\n >>> ') 

    avatar = input('Escoga un avatar\n-Scharifker\n-Eugenio Mendoza\n-Pelusa\n-Gandhi\n-Estudiante de sistemas promedio\n>>> ')
    while avatar != "Scharifker" and avatar != "Eugenio Mendoza" and avatar != "Pelusa" and avatar != "Gandhi" and avatar != "Estudiante de sistemas promedio":
        avatar = input('Personaje no seleccionable, escoga de nuevo!\n>>> ')

    inventario = []

    dificultad = input('Escoga su dificultad\n1.Facil\n2.Normal\n3.Dificil\n>>>')
    while dificultad != "1" and dificultad != "2" and dificultad != "3":
        dificultad = input('Dificultad no valida, escoga una dificultad!\n>>>')

    if dificultad == "1":
        dificultad = Facil
        lives = "5"
        clues = "5"
        player = Facil(num_registro, user, password, age, avatar, inventario, dificultad, lives, clues)

    if dificultad == "2":
        dificultad = Normal
        lives = "3"
        clues = "3"
        player = Normal(num_registro, user, password, age, avatar, inventario, dificultad, lives, clues)

    if dificultad == "3":
        dificultad = Dificil
        lives = "1"
        clues = "2"
        player = Dificil(num_registro, user, password, age, avatar, inventario, dificultad, lives, clues) 

    users.append(player)
    
    print("---------------------------------------------------------")
    print('Usuario registrado con exito!')
    print(player.mostrar())
  
    return users
       

#def mostrar_registros(users):
#    
#    for i,p in enumerate(users):
#        print("---",i+1,"---------------")
#        print(p.mostrar())
#

#--------------------------------------------------------------------------------------------------------------
def main():

    users = []
    while True:
        print("------------------------------------------------------")
        print('Bienvenido a Escapamet!\nDesea empezar una nueva partida?')
        opcion = input('1. Ingrese su usuario\n2. Instrucciones\n3. Salir\n>>>')
        print("------------------------------------------------------")

        if opcion == "1":
            registro_usuario(users)
            movimiento(users, Games, User)
            #mostrar_registros(users)

        elif opcion == "2":
            pass
        
        elif opcion == "3":
            break
        
        else:
            print("opcion invalida!")

main()        
                    
        