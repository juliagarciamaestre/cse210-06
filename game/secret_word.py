# !!! IMPORTS
import random

class SecretWord:
    def __init__(self):
        self._wordd=""
        #Counter for char found in self._word
        self._contador=0
        #container for the char index found in self._word
        self._indice=[]
        
    #Mezcla la lista
    def _word_list(self):
        self._word_list=["david","ernesto","benjamin","samuel","gerardo"]
        random.shuffle(self._word_list)
    #Retorna una palabra de la lista    
    def _word(self):
        z = random.randint(0,4)
        self._wordd = self._word_list[z]
        return self._wordd
        

    def _deleteLine():
        pass    

    def _display_word_lines(self):
        for i in range(len(self._wordd)):
            if self._indice==i:
                print(f"{self._word[i]}", end=" ")
            else:
                print("_", end="  ")
