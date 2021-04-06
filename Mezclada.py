import requests
from Games import Games
import random
from User import *

api = requests.get("https://api-escapamet.vercel.app")

class Mezclada(Games):
    def __init__(self, lugar, interaccion):
        super().__init__(lugar, interaccion)
        print(self.game)
        print(self.rules)

        question = random.choice(api.json()[lugar]["objects"][interaccion]["game"]["questions"])
        self.pregunta = question["question"]
        self.categoria = question["category"]
        palabras = (question["words"])  
        print(self.pregunta)
        print(self.categoria)

        respuesta = []

        for letra in palabras:
            mezcla = random.sample(letra, len(letra))
            palabra = ''.join(mezcla)
            print(palabra)

        for letra in palabras:

            while True:
                answer = input('> ')
                if answer in palabras:
                    if answer in respuesta:
                        print('Letra ya utilizada')
                    else:
                        respuesta.append(answer)
                        print(respuesta)

                        if len(respuesta) == len(palabras):
                            print('Juego completado')
                        break
                else:
                    print('prueba de nuevo')


#mezclada = Mezclada(lugar = 4, interaccion = 1)