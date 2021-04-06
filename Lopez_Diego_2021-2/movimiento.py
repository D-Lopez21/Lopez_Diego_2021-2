import requests
from User import *
from Player import *
import Cuartos
import random
import Adivinanzas
import Ahorcado
import Booleana
import Cripto
import Logica
import Mezclada
import Numero
import Python
import Quizizz
import FinalBoss

api = requests.get("https://api-escapamet.vercel.app")

def movimiento(users, Games, User):
    inventario = [] #para almacenar los items
    contador_puerta = 0
    contador_biblio = 0
    contador_lab = 0
    contador_plaza = 0
    contador_servidor = 0
    while not "Llaves del carro" in inventario: #para parar el juego
        print(Cuartos.biblioteca1)
        direccion = input('>>> ').lower()
        if direccion == 'f':
            while True:
                print(Cuartos.samancito)
                direccion = input('>>> ').lower()
                if direccion == 'l':   
                    if "libro de matematicas" in inventario: #para no jugar 2 veces
                        print("Ya obtuviste el objeto, pa que quieres volver a jugar?")
                    else:
                        quizizz = Quizizz.Quizizz(lugar = 2, interaccion = 1)
                        inventario.append("libro de matematicas")#para agregar los items ganados al inventario
                        print(inventario)
                elif direccion == 'c' and "Mensaje: Si estas gradudado puedes pisar el Samán" in inventario and "titulo universitario" in inventario:
                    print(Cuartos.samancito2)
                    if "disco duro" in inventario:
                        print("Ya obtuviste el objeto, pa que quieres volver a jugar?")                            
                    else:
                        logica = Logica.Logica(lugar = 2, interaccion = 0)
                        inventario.append("disco duro")#para agregar los items ganados al inventario
                        print(inventario)
                elif direccion == 'c':
                    print(Cuartos.samancito)
                    print("Chamo, tu no entiendes que no puedes pisar el saman? Perdiste una vida por eso")
                    if "disco duro" in inventario: #para no jugar 2 veces
                        print("Ya obtuviste el objeto, pa que quieres volver a jugar?")                            
                    else:
                        logica = Logica.Logica(lugar = 2, interaccion = 0)
                        inventario.append("disco duro") #para agregar los items ganados al inventario       
                elif direccion == 'r':
                    if "martillo" in inventario:#para no jugar 2 veces
                        print('Ya tienes el objeto, para que quieres entrar de nuevo?')
                    else:
                        inventario.append("martillo")#para agregar los items ganados al inventario
                        print(inventario)
                if direccion == 'b':
                    break                   
        elif direccion == 'b':
            while True:
                print(Cuartos.puertalab_cerrada)
                direccion = input('> ').lower()
                if direccion == 'f':
                    print(Cuartos.puertalab_abierta)
                    booleana = Booleana.Booleana(lugar = 3, interaccion = 0)                        
                    while True:
                        print(Cuartos.Laboratorios)
                        direccion = input('> ').lower()
                        if direccion == 'f':
                            while True:                                
                                print(Cuartos.CuartoServidores_cerrado)
                                direccion = input('> ').lower
                                if direccion == 'b':
                                    break
                                elif direccion == 'l':
                                    if "mezclada" in inventario:#para no jugar 2 veces
                                        print("Ya obtuviste el objeto, pa que quieres volver a jugar?")
                                    else:
                                        mezclada = Mezclada.Mezclada(lugar = 4, interaccion = 1)
                                        inventario.append("contraseña")#para agregar los items ganados al inventario
                                        print(inventario)
                                        print('La contraseña es yugioh... por que esperaba algo diferente?')     
                                elif direccion == 'r':
                                    if "titulo universitario" in inventario:#para no jugar 2 veces
                                        print("Ya obtuviste el objeto, pa que quieres volver a jugar?")   
                                    else:
                                        numero = Numero.Numero(lugar = 4, interaccion = 2)
                                        inventario.append("titulo universitario")#para agregar los items ganados al inventario
                                        print(inventario)
                                elif direccion == 'c':
                                    while True:
                                        print(Cuartos.CuartoServidores_abierto)
                                        respuesta = input('y / n')
                                        if respuesta == 'y':
                                            finalboss = FinalBoss.FinalBoss(lugar = 4, interaccion = 0)
                                            inventario.append("Llaves del carro")#para agregar los items ganados al inventario
                                            pass
                                        elif respuesta == 'n':
                                            break
                                        elif direccion == 'b':
                                            break
                                        
                        elif direccion == 'l':
                            while True:
                                if "HDMI" in inventario and "carnet" in inventario:     #para no jugar 2 veces                           
                                        print("Ya obtuviste el objeto, pa que quieres volver a jugar?")
                                elif "HDMI" in inventario:
                                    print(Cuartos.computadora1_encendida)
                                    respuesta = input('> ')
                                    if respuesta == 'f':
                                        python = Python.Python(lugar = 0 , interaccion = 1)
                                        inventario.append("carnet")#para agregar los items ganados al inventario
                                        print(inventario)
                                    elif respuesta == 'b':
                                        break
                                else:
                                    print(Cuartos.computadora1_apagada)
                                    direccion = input('> '.lower())
                                    if direccion == 'b':
                                        break
                                    
                        elif direccion == 'r':
                            while True:
                                if "contraseña" in inventario and "llave" in inventario:#para no jugar 2 veces
                                    print("Ya obtuviste el objeto, pa que quieres volver a jugar?")
                                if "contraseña" in inventario:
                                    print(Cuartos.computadora2_concontra)
                                    respuesta = input('> ').lower()
                                    respuesta = input('> ').lower
                                    if respuesta == 'yugioh':
                                        if respuesta == 'f':
                                            adivinanza = Adivinanzas.Adivinanzas(lugar = 0, interaccion = 2)
                                            inventario.append("llave")#para agregar los items ganados al inventario
                                            print(inventario)
                                        elif respuesta == 'b':
                                            break 
                                    else:
                                        pass    
                                else:
                                    print(Cuartos.computadora2_sincon)
                                    direccion = input('> '.lower())
                                    if direccion == 'b':
                                        break
                        elif direccion == 'b':
                            break                                              
                else: 
                    break                         
                    
        elif direccion == 'c':
            if "HDMI" in inventario:#para no jugar 2 veces
                print("Ya obtuviste el objeto, pa que quieres volver a jugar?")
                pass
            else:
                ahorcado = Ahorcado.Ahorcado(lugar = 1, interaccion = 0)
                inventario.append("HDMI")#para agregar los items ganados al inventario
                print(inventario)
        elif direccion == 'l':
            if "libro de matematicas" in inventario:#para no jugar 2 veces
                print("Ya obtuviste el objeto, pa que quieres volver a entrar?")
            else:
                print('empty')
                print(inventario)
        elif direccion == 'r':
            if "llave" in inventario:    #para no jugar 2 veces
                cripto = Cripto.Cripto(lugar = 1, interaccion = 2)
                inventario.append("Mensaje: Si estas gradudado puedes pisar el Samán")#para agregar los items ganados al inventario
                print(inventario)
            elif "Mensaje: Si estas gradudado puedes pisar el Samán" in inventario and "llave" in inventario:#para no jugar 2 veces
                print("Ya obtuviste el objeto, pa que quieres volver a jugar?")
                pass
            else:
                print('Creo que te falta una llave...')
        else:
            print('Podrias no chocarte con un muro? Por favor?')
