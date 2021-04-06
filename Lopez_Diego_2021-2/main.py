from User import *
from Player import *
from Avatar import * 
from Games import Games
import Cuartos
import random
from movimiento import *


def registro_usuario(users): #Crear usuarios para poder iniciar el juego

    num_registro = len(users) + 1 #organizar a usuarios
    print('Tenga en cuenta que su usuario debe ser de al menos 6 caracteres de largo!')
    user = input('Escriba el nombre de su usuario: ')#para registrar el usuario
    while len(user) < 6:
        user = input("Tu nombre no es lo suficientemente largo, intenta con un nombre nuevo!\n >>>")

    if user in users:#validar si el usuario ya existe
        print(f"El usuario {user} ya existe en la base de datos. Por favor introduzca la contraseña")
    else:
        print('Usuario nuevo! Bienvenido!')

    password = input('Escriba su contraseña: ')#crear contraseña
    while len(password) < 6:
        password = input("Tu contraseña no es lo suficientemente largo, intenta con una contraseña nueva!\n >>>")
        
    if password in users:#validar contraseña
        print("Contraseña valida")
    else:
        print("Contraseña no compatible")

    print('Para poder jugar este juego, tu edad minima debe de ser de 8 años!')
    age = input('Ingrese su edad: ')#para registrar la edad
    if int(age) < 8 and age.isnumeric(): #validad edad
        age = input('No cumples con la edad minima para poder jugar, prueba de nuevo en unos años ;) , o simplemente prueba poniendo una edad nueva!\n >>> ') #Crear avatar

    avatar = input('Escoga un avatar\n-Scharifker\n-Eugenio Mendoza\n-Pelusa\n-Gandhi\n-Estudiante de sistemas promedio\n>>> ') #Crear avatar
    while avatar != "Scharifker" and avatar != "Eugenio Mendoza" and avatar != "Pelusa" and avatar != "Gandhi" and avatar != "Estudiante de sistemas promedio": #validar que el avatar sea seleccionable
        avatar = input('Personaje no seleccionable, escoga de nuevo!\n>>> ')

    inventario = [] #para almacenar los items

    dificultad = input('Escoga su dificultad\n1.Facil\n2.Normal\n3.Dificil\n>>>') #para registrar la dificultad
    while dificultad != "1" and dificultad != "2" and dificultad != "3": #validar que la dificultad sea seleccionable
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

    users.append(player) #para guardar los usuarios a la lista
    
    print("---------------------------------------------------------")
    print('Usuario registrado con exito!')
    print(player.mostrar()) #para mostrar todos los datos guardados con exito
  
    return users #para mandar los usuarios a la lista

#--------------------------------------------------------------------------------------------------------------
def main():

    users = [] #para almacenar a los usuarios
    while True:
        print("------------------------------------------------------")
        print('Bienvenido a Escapamet!\nDesea empezar una nueva partida?')
        opcion = input('1. Ingrese su usuario\n2. Instrucciones\n3. Salir\n>>>')
        print("------------------------------------------------------")

        if opcion == "1":
            registro_usuario(users) #para llamar al registro de usuarios
            movimiento(users, Games, User)#para llamar a la parte donde se va a jugar principalmente

        elif opcion == "2":
        
            print('1. Trata de conseguir todos los objetos para poder desbloquear nuevos juegos y zonas\n2. Trata de hecerlo en el tiempo mas rapido\n3. Utiliza las instrucciones que se te presenten en la pantalla para progresar mas comodamente\n4 Disfruta de el juego!')
        elif opcion == "3":
            break
        
        else:
            print("opcion invalida!")

main()        
                    
        