import requests
from Games import Games
import random

api = requests.get("https://api-escapamet.vercel.app")

class Numero(Games):
    def __init__(self, lugar, interaccion):
        super().__init__(lugar, interaccion)
        print(self.game)
        print(self.rules)

        question = random.choice(api.json()[lugar]["objects"][interaccion]["game"]["questions"])
        print('1-15')
        self.random_num = random.randint(1,15) 
        self.num_cpu = 0

        self.num_cpu = int(input('> '))
        while self.num_cpu != self.random_num:
            if self.num_cpu < self.random_num:
                print('ta bajo')
            elif self.num_cpu > self.random_num:
                print('ta alto')
                
        
        print(f'adivinaste {self.random_num}')                

#numero = Numero(lugar = 4, interaccion = 2)


