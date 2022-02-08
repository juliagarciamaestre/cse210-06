# !!!IMPORTS
from game.parachute import Parachute
from game.secret_word import SecretWord

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        # !!!ADD ATTRIBUTES HERE
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        # !!!ADD ATTRIBUTES HERE
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Moves the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        # !!!ADD LOGIC HERE
        # Prepare Objects for inputs.
        #Thes lines draw the parachute
        parachute=Parachute()
        parachute.build_parachute()
        
        #crea la lista de palabras a adivinar y la mezcla    ###NO escoge la palabra a adivinar##
        secret_word = SecretWord()
        secret_word._word_list()
        self._word = secret_word._word()
        
    def _do_updates(self):
        """Keeps watch on where the seeker is moving.

        Args:
            self (Director): An instance of Director.
        """
        # !!!ADD LOGIC HERE
        
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        # !!!ADD LOGIC HERE
