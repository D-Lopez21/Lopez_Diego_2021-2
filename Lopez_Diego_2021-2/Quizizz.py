import requests
from Games import Games
import random

api = requests.get("https://api-escapamet.vercel.app")#llamar api

class Quizizz(Games):
    def __init__(self, lugar, interaccion):
        super().__init__(lugar, interaccion)
        print(self.game)
        print(self.rules)

        question = random.choice(api.json()[lugar]["objects"][interaccion]["game"]["questions"]) #para sacar la info de la informacion comodamente
        self.quizizz = question["question"]
        self.correct_answers = question["correct_answer"]
        self.answer1 = question["answer_2"]
        self.answer2 = question["answer_3"]
        self.answer3 = question["answer_4"]   
        print(self.quizizz)
        print(self.correct_answers)
        print(self.answer1)
        print(self.answer2)
        print(self.answer3)
            
        user_respuesta = input('> ')
        if user_respuesta in self.correct_answers:
            print('Correcto!')
        else:
            print('Intenta de nuevo!')

#quizizz = Quizizz(lugar = 2, interaccion = 1)

