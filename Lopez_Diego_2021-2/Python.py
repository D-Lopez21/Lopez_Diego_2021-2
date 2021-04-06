import requests
from Games import Games
import random

api = requests.get("https://api-escapamet.vercel.app")# llamar api

class Python(Games):
    def __init__(self, lugar, interaccion):
        super().__init__(lugar, interaccion)
        print(self.game)
        print(self.rules)

        question = random.choice(api.json()[lugar]["objects"][interaccion]["game"]["questions"]) #sacar info de la api comodamente
        self.python = question["question"]

        if self.python == api.json()[lugar]["objects"][interaccion]["game"]["questions"][0]["question"]:#para seleccionar la pregunta
            print(self.python)
            answer1 = "frase = int(float(((frase.split())[-2].replace(',','.')))" #validar respuesta
            while True:
                user_respuesta = input('> ')
                if user_respuesta == answer1:
                    print('piola')
                    break
                else:
                    print('no piola')
        
        else:
            print(self.python)
            answer2 = "frase = frase[::-1]" #validar respuesta
            while True:
                user_respuesta = input('> ')
                if user_respuesta == answer2:
                    print('piola')
                    break
                else:
                    print('no piola')

#python = Python(lugar = 0 , interaccion = 1)