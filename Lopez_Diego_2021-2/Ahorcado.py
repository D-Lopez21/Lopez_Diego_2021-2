import requests
from Games import Games
import random

api = requests.get("https://api-escapamet.vercel.app") #para llamar a la api

class Ahorcado(Games):
    def __init__(self, lugar, interaccion): #para establecer el lugar y el juego
        super().__init__(lugar, interaccion)
        print(self.game)
        print(self.rules)
        
        question = random.choice(api.json()[lugar]["objects"][interaccion]["game"]["questions"]) #Para sacar informacion de la api
        self.pregunta = question["question"]
        ahorcado_word = question["answer"]
        print(self.pregunta)

        word = ahorcado_word #para almacenar las palabras del ahorcado de una manera mas comoda
        word_letters = set(word)
        alphabet = set( 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' )
        used_letters = set()        
        
        while len(word_letters) > 0: #para separar las letras
            print('letras utilizadas: ', ' '.join(used_letters)) #para ver las letras usadas
            
            word_list = [letter if letter in used_letters else '-' for letter in word] #buscar si la palabra tiene una letra seleccionada
            print('Letras actuales: ', ' '.join(word_list)) #para ver las letras de la palabra seleccioanda

            user_letter = input('Escoge una letra: ') 
            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)        

            elif user_letter in used_letters:
                print('ya la usaste rey')
            else:
                print('letra invalida, usa otra')

    def validar_palabra(self, ahorcado_word): 
        word = ahorcado_word
        while '-' in word or ' ' in word:
            word = ahorcado_word

        return word

#ahorcado = Ahorcado(lugar = 1, interaccion = 0)



