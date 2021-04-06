import requests
from Games import Games
import random

api = requests.get("https://api-escapamet.vercel.app") #Para llamar a la api

class Adivinanzas(Games):
    def __init__(self, lugar, interaccion):
        super().__init__(lugar, interaccion)
        print(self.game)
        print(self.rules)

        question = random.choice(api.json()[lugar]["objects"][interaccion]["game"]["questions"]) #Para sacar informacion de la api
        self.adivinanza = question["question"] #Para llamar a las preguntas de una manera comoda
        self.answers = question["answers"] #para almacenar las respuesta de una manera comdoa
        print(self.adivinanza)

    def respuesta(self, user_respuesta): #para poder realizar el juego
        user_respuesta = input('> ')
        if user_respuesta in self.answers:
            print('Ganaste!')
        else:
            print('Perdiste...') 

#adivinanza = Adivinanzas(lugar = 0, interaccion = 2)

