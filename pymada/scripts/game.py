"""Game and context
"""

import os, sys  # explicitly modify path to avoid having to constantly run setup.py to test code

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pymada
import pymada.errors

from pymada.classes.board import Board

class Game:
    """
    """

    MAX_TURNS = 6

    def __init__(
        self, players,
    ):
        """
        """

        self.players = players
        self.turn = 0
        self.player_turn = itertools.cycle(players)
        self.board=Board()
    
    @property
    def over(self):
        """
        """

        return False is self.turn<=MAX_TURNS else return True

    def play_round(self):
        """
        """

        self.turn+=1

        for player in self.player_turn:

            player.input(ship_to_move) XXX make player agent a class with different input methods

            game.fleets[player][ship_name].move()


            if XXX CHECK WIN STATES e.g. if self.fleets[player_1].is_destroyed:
                player2.win() XXX make a player class?
                return 

    def ship_phase(self):
        """
        """

    def squadron_phase(self):
        """
        """

        pass

    def status_phase(self):
        """
        """

        pass