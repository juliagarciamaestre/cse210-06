from numpy import character
from game.parachute import Parachute
from game.secret_word import SecretWord
from game.terminal_service import TerminalService

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        # !!!ADD ATTRIBUTES HERE
    """

    def __init__(self):
        self._terminalService=TerminalService()
        self._secretWord=SecretWord()
        self._parachu=Parachute()
        self._is_playing=True    
        self._word=""

        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        # !!!ADD ATTRIBUTES HERE       
                
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
    def start_game(self):
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            self._is_playing=False    

    def _get_inputs(self):
        """Moves the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        # !!!ADD LOGIC HERE
       
        #Construyo el dos paracaidas ,el primero muestra todas las yayitas, el segundo empieza a iterar y va borrando las rayitas.
        self._parachu.build_parachutes()
        self._parachu._display_parachute1()
        #crea la lista de palabras a adivinar y la mezcla    ###NO escoge la palabra a adivinar##
        self._secretWord._word_list()
        #Escoger la palabra de la lista
        self._secretWord._word()
        print(self._secretWord._wordd)
        #Mostrar rayitas segun cantidad de letras en la palabra.
        self._secretWord._display_word_lines()
        print()
        #solicitar una letra
        _character =self._terminalService.read_text("Input a Character to Guess the Word : ")
        
    def _do_updates(self):
        
        """Keeps watch on where the seeker is moving.

        Args:
            self (Director): An instance of Director.
        """
        # !!!ADD LOGIC HERE
        #Muestra el primer paracaidas
        self._parachu._display_parachute1()
        
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        # !!!ADD LOGIC HERE
        _w=self._secretWord._wordd
        self._terminalService.write_text(_w)
