# !!! IMPORTS

class Parachute:
  def __init__(self):
        self._parachutte=[]
    
   def build_parachute(self):


        self._parachutte=[      ['_', '_', '_', '_', '_'],
                                [' ', ' ', ' ', ' ', ' '],
                                [' ', '_', ' ', '_', ' '],
                                ['/', '-', ' ', '-', '\\'],
                                ['\\', ' ', ' ', ' ', '/'],
                                [' ', '\\', ' ', '/', ' '],
                                [' ', ' ', 'O', ' ', ' '],
                                [' ', '/', '|', '\\', ' ', ' '],
                                [' ', '/', ' ', '\\', ' '],
                         ]
        
        print("\t")
        #print the parachutte 
        # matrix : 7rows x 5 columns                          
        for i in range(0,9):
            for j in range(0,5):
                self._spl = self._parachutte[i][j]
                print(self._spl, end=" ")
            print("\n\t")
        #Ground    
        print("^^^^^^^^^^^^^^^^^")    


