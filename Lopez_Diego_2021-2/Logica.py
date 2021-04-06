import requests
from Games import Games
import random

api = requests.get("https://api-escapamet.vercel.app")# para llamar a la api

class Logica(Games):
    def __init__(self, lugar, interaccion):
        super().__init__(lugar, interaccion)
        print(self.game)
        print(self.rules)

        self.question = random.choice(api.json()[lugar]["objects"][interaccion]["game"]["questions"])  #sacar las cosas de la api con comodidad 
    
        if self.question == random.choice(api.json()[lugar]["objects"][interaccion]["game"]["questions"][1]):
            print(question)
            answer1 = "41"
            while True:
                self.user_respuesta = input('> ')
                if self.user_respuesta == answer1:#condicion de victoria
                    print('Correcto')
                    break
                else:
                    print('Prueba de nuevo')
        
        else:
            print(question)
            answer2 = "67"
            while True:
                self.user_respuesta = input('> ')
                if self.user_respuesta == answer2:
                    print('Correcto')
                    break
                else:
                    print('Prueba de nuevo')


#logica = Logica(lugar = 2, interaccion = 0)
