import requests
from Games import Games
import random
import time

api = requests.get("https://api-escapamet.vercel.app")

class FinalBoss(Games):
	def __init__(self, lugar, interaccion):
		super().__init__(lugar, interaccion)
	
		finalizar=[]
		while not "victoria" in finalizar:
			print('Elige entre piedra, papel o tijeras: ')
			eleccion = str(input()).lower()
			print("Mi eleccion es", eleccion)
			elecciones = ['piedra', 'papel', 'tijeras']
			eleccion_cpu = random.choice(elecciones)
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



		
#		print('Elige entre piedra, papel o tijeras:')
#		choice = str(input())
#		choice = choice.lower()
#		print("Mi eleccion es", choice)
#		choices = ['piedra', 'papel', 'tijeras']
#		computer_choice = random.choice(choices)
#		print("La eleccion del servidor", computer_choice)
#		if choice in choices:
#			if choice == computer_choice:
#				print('Empate')
#			if choice == 'piedra':
#				if computer_choice == 'papel':
#					print('Perdiste... Pero no te rindas!')
#				elif computer_choice == 'tijeras':
#					print('GANASTE!!!!! FELICITACIONES!')
#					self.finalizar.append("end")
#					break
#			if choice == 'papel':
#				if computer_choice == 'tijeras':
#					print('Perdiste... Pero no te rindas!')
#				elif computer_choice == 'piedra':
#					print('GANASTE!!!!! FELICITACIONES!')
#					self.finalizar.append("end")
#					break
#			if choice == 'tijeras':
#				if computer_choice == 'piedra':
#					print('Perdiste... Pero no te rindas!')
#				elif computer_choice == 'papel':
#					print('GANASTE!!!!! FELICITACIONES!')
#					self.finalizar.append("end")						
#					break
#		else:
#			print('No hagas trampa, escoge de nuevo')
#