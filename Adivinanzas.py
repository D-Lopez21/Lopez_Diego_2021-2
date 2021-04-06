import requests
from Games import Games
import random

api = requests.get("https://api-escapamet.vercel.app")

class Adivinanzas(Games):
    def __init__(self, lugar, interaccion):
        super().__init__(lugar, interaccion)
        print(self.game)
        print(self.rules)

        question = random.choice(api.json()[lugar]["objects"][interaccion]["game"]["questions"])
        self.adivinanza = question["question"]
        self.answers = question["answers"]
        print(self.adivinanza)

    def respuesta(self, user_respuesta):
        user_respuesta = input('> ')
        if user_respuesta in self.answers:
            print('piola')
        else:
            print('no piola')

#adivinanza = Adivinanzas(lugar = 0, interaccion = 2)

