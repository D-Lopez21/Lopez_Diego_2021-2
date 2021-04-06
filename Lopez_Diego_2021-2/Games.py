import requests

api = requests.get("https://api-escapamet.vercel.app") #para llamar a la api

class Games:
    def __init__(self, lugar, interaccion): #para poder traer toda la informacion de la api necesaria
        self.game = api.json()[lugar]["objects"][interaccion]["game"]["name"]
        self.rules = api.json()[lugar]["objects"][interaccion]["game"]["rules"]
        self.award = api.json()[lugar]["objects"][interaccion]["game"]["award"]
        self.requirement = api.json()[lugar]["objects"][interaccion]["game"]["requirement"]