# !!! IMPORTS
import random

class SecretWord:
  def __init__(self):
        #Container for the word to guess
        self._wordd=""
        #Counter for chars found in self._wordd
        self._contador=0
        #container for the char index found in self._word
        self._indice=[]
        

    def _word_list(self):
        self._word_list=["david","ernesto","benjamin","samuel","gerardo"]
        random.shuffle(self._word_list)
        
    def _word(self):
        z = random.randint(0,4)
        self._wordd = self._word_list[z]
        return self._wordd
