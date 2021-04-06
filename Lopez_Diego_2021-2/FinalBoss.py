import requests
from Games import Games
import random
import time

api = requests.get("https://api-escapamet.vercel.app") #para llamar la api

class FinalBoss(Games):
	def __init__(self, lugar, interaccion):
		super().__init__(lugar, interaccion)
	
		finalizar=[]
		while not "victoria" in finalizar: #condicion de victoria
			print('Elige entre piedra, papel o tijeras: ')
			eleccion = str(input()).lower()
			print("Mi eleccion es", eleccion)
			elecciones = ['piedra', 'papel', 'tijeras']
			eleccion_cpu = random.choice(elecciones) #para que la maquina no tenga siempre la misma opcion
			print('La eleccion del cpu es...', eleccion_cpu)
			if eleccion != 'piedra' or eleccion != 'papel' or eleccion != 'tijeras':
				eleccion = input('Podrias dejar de hacer trampa y escoger una opcion de verdad: ')
			else:
				if eleccion in elecciones:
					if eleccion == eleccion_cpu:
						print('Empate... Pero esto no acabara aqui')
						if eleccion == 'piedra':
							if eleccion_cpu == 'papel':
								print('Perdiste... Pero te dare otra oportunidad')
							elif eleccion_cpu == 'tijeras':
								print('Bueno, esto es incomodo. En fin, ganaste')
								finalizar.append("victoria")
						elif eleccion == 'papel':
							if eleccion_cpu == 'tijeras':
								print('Perdiste... Pero te dare otra oportunidad')
							elif eleccion_cpu == 'piedra':
								print('Bueno, esto es incomodo. En fin, ganaste')
								finalizar.append("victoria")
						elif eleccion == 'tijeras':
							if eleccion_cpu == 'piedra':
								print('Perdiste... Pero te dare otra oportunidad')
							elif eleccion_cpu == 'papel':
								print('Bueno, esto es incomodo. En fin, ganaste')
								finalizar.append("victoria")
		else:
			print('Victoria!')		
