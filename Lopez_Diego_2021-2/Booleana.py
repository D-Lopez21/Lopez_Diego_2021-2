from User import User
import requests
from Games import Games
import random

api = requests.get("https://api-escapamet.vercel.app") #para llamar a la api

class Booleana(Games):
    def __init__(self, lugar, interaccion):
        super().__init__(lugar, interaccion)
        print(self.game)
        print(self.rules)

        question = random.choice(api.json()[lugar]["objects"][interaccion]["game"]["questions"]) #para buscar en la api
        self.booleana = question["question"]
        self.answers = question["answer"]
        print(self.booleana)

        user_respuesta = input('> ')
        if not user_respuesta in self.answers:
            print('Respuesta incorrecta, pierdes media vida!')
        else:
            print('Respuesta correcta, obtienes una vida extra!')
            
            