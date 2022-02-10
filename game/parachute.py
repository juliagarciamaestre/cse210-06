#!!! IMPORTS
class Parachute:
    
   def __init__(self):
        self._parachutte=[]
        self._parachutte2=[]
        #estos indices es donde estan las rayitas en el parachute
        self._indices=[2,1,2,3,3,0,3,1,3,3,3,4]#indices de las rayitas a borrar
   def build_parachutes(self):
        #Se separan los parachutes segun su roll
        #El primer parachute se muestra completo 
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
        #El segundo parachute se muestra con las lineas que se van quitando/borrando segun los errores del usuario.
        # El seguno parachute ayudara en la iteracion, cada vez que se equivoque el usuario se llamara al parachute que corresponde.                 
        self._parachutte2=[     ['_', '_', '_', '_', '_'],
                                [' ', ' ', ' ', ' ', ' '],
                                [' ', '_', ' ', '_', ' '],
                                ['/', '-', ' ', '-', '\\'],
                                ['\\', ' ', ' ', ' ', '/'],
                                [' ', '\\', ' ', '/', ' '],
                                [' ', ' ', 'O', ' ', ' '],
                                [' ', '/', '|', '\\', ' ', ' '],
                                [' ', '/', ' ', '\\', ' '],
                         ]        
       
   def delete_lines(self):
       print()
       #variable local auxiliar para guardar la opcion del usuario
       _c=""
       #borra 2 lineas  self._indices=[2,1,2,3,3,0,3,1,3,3,3,4]
       #Este loop va borrando en cada iteracion erronea.
       for i in range(len(self._indices)):
           #tomo el valor(indeces de las rayitas) para comparar si esos indices apuntan a las rayitas y poder borrarlas.
               primer_indice=self._indices[i]
               segundo_indice=self._indices[i+1]
               #Segun queden rayitas disponibles segun los indices se iran borrando.Cada if representa una rayita.
               #primer yayita
               if primer_indice==2 and segundo_indice==1:
                   #borrar rayita
                   self._parachutte2[2][1]=" "
                   #Actualizo parachute, este metodo deberia ir en updates()
                   self._display_parachute2()
                   #si se escoge "y" se vuelve a iterar sobre el parachute2 que tendra las rayitas borradas.
                   _c=input("Continua Borrando lineas ? [y/n] : ")
                   if _c.lower()=="y":
                       pass
                   else:
                       print("Thank you..")
                       exit()
                    #segunda yayita        
               elif primer_indice==2 and segundo_indice==3:    
                   self._parachutte2[2][3]=" "
                   self._display_parachute2()
                   #si se escoge "y" se vuelve a iterar sobre el parachute2 que ya tiene las rayitas borradas
                   _c=input("Continua borrando ? [y/n] : ")
                   if _c.lower()=="y":
                      pass
                   else:
                       print("Thank you..")
                       exit()
               elif primer_indice==3 and segundo_indice==0:
                   self._parachutte2[3][0]=" "
                   self._display_parachute2()
                   #si se escoge "y" se vuelve a iterar sobre el parachute2 que ya tiene las rayitas borradas
                   _c=input("Continua borrando ? [y/n] : ")
                   if _c.lower()=="y":
                      pass
                   else:
                       print("Thank you..")
                       exit()
               elif primer_indice==3 and segundo_indice==1:
                   self._parachutte2[3][1]=" "
                   self._display_parachute2()
                   #si se escoge "y" se vuelve a iterar sobre el parachute2 que ya tiene las rayitas borradas
                   _c=input("Continua borrando ? [y/n] : ")
                   if _c.lower()=="y":
                      pass
                   else:
                       print("Thank you..")
                       exit()
               elif primer_indice==3 and segundo_indice==4:
                   self._parachutte2[3][4]=" "
                   self._display_parachute2()
                   #si se escoge "y" se vuelve a iterar sobre el parachute2 que ya tiene las rayitas borradas
                   _c=input("Continua borrando ? [y/n] : ")
                   if _c.lower()=="y":
                      pass
                   else:
                       print("Thank you..")
                       exit()
               elif primer_indice==4 and segundo_indice==0:
                   self._parachute2[4][0]=" "
                   self._display_parachute2()
                   #si se escoge "y" se vuelve a iterar al loop for sobre el parachute2 que ya tiene las rayitas borradas
                   _c=input("Continua borrando ? [y/n] : ")
                   if _c.lower()=="y":
                       pass
                   else:
                       print("Thank you..")
                       exit()
               elif primer_indice==4 and segundo_indice==4:
                   x = self._parachute2[4][4]=" "
                   self._display_parachute2()
                    #si se escoge "y" se vuelve a iterar al loop for sobre el parachute2 que ya tiene las rayitas borradas
                   _c=input("Continua borrando ? [y/n] : ")
                   if _c.lower()=="y":
                       pass
                   else:
                       print("Thank you..")
                       exit()
                ##Agregar mas if por cada rayita que se borra.     
                #..........................................

       #imprimir parachute2. este metodo deberia ir en el output()
   def _display_parachute1(self):
       print("\t")
       #Imprimir parachute1 el dibujito
       # matrix : 7rows x 5 columns                          
       for i in range(0,9):
           for j in range(0,5):
               self._spl = self._parachutte[i][j]
               print(self._spl, end=" ")
           print("\n\t")
        #Ground    
       print("^^^^^^^^^^^^^^^^^")


   def _display_parachute2(self):
       print("\t")
       #Imprime el dibujito
       #matrix : 7rows x 5 columns                          
       print("Imprimir parachute2")
       for i in range(0,9):
           for j in range(0,5):
               self._spl = self._parachutte2[i][j]
               print(self._spl, end=" ")
           print()
