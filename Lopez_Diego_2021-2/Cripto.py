import requests
from Games import Games
import random

api = requests.get("https://api-escapamet.vercel.app") #para llamar la api

class Cripto(Games):
    def __init__(self, lugar, interaccion):
        super().__init__(lugar, interaccion)
        print(self.game)
        print(self.rules)
        
        question = random.choice(api.json()[lugar]["objects"][interaccion]["game"]["questions"]) #para buscar en la api
        self.criptograma = question["question"]
        self.desplazamiento = question["desplazamiento"]

        frase = self.criptograma #para organizar la frase decifrada
        if self.desplazamiento == 2:
            desplazamiento2 = frase.maketrans("abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóúÁÉÍÓÚ", "cdefghijklmnñopqrstuvwxyzabCDEFGHIJKLMNÑOPQRSTUVWXYZABcgkqwCGKQW")
            frase = frase.translate(desplazamiento2)
            print(frase)
            print('''

               A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
                                        |  |
                                        |  |
                                       \    /
                                        \  /
                                         \/
               C D E F G H I J K L M N O P Q R S T U V W X Y Z A B

                ''')
        elif self.desplazamiento == 4:
            desplazamiento4 = frase.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZáéíóúÁÉÍÓÚ", "efghijklmnopqrstuvwxyzabcdEFGHIJKLMNOPQRSTUVWXYZABCDeimsyEIMSY")
            frase = frase.translate(desplazamiento4)
            print(frase)
            print('''

                A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
                                       |  |
                                       |  |
                                      \    /
                                       \  /
                                        \/
                E F G H I J K L M N O P Q R S T U V W X Y Z A B C D

            ''')
        else:
            desplazamiento5 = frase.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZáéíóúÁÉÍÓÚ", "fghijklmnopqrstuvwxyzabcdeFGHIJKLMNOPQRSTUVWXYZABCDEfjntzFJNTZ")
            frase = frase.translate(desplazamiento5)
            print(frase)
            print('''
               
                A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
                                       |  |
                                       |  |
                                      \    /
                                       \  /
                                        \/
                F G H I J K L M N O P Q R S T U V W X Y Z A B C D E
            ''')
        new_frase = self.criptograma
        a,b =  'áéíóúüÁÉÍÓÚÜ','aeiouuAEIOUU' #para reemplazar las letras con acentos
        trans = str.maketrans(a,b)
        new_frase.translate(trans)
        respuesta = input("> ")
        if respuesta == new_frase.translate(trans):
            print("Has decifrado el codigo!!")

#cripto = Cripto(lugar = 1, interaccion = 2)