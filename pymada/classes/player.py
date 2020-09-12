"""
"""

import os, sys

import pymada
import pymada.errors
from pymada.classes.board import Board


class Player:
    """
    """

    def __init__(self, name, faction=None, species="human"):
        """

        args:
            name - unique name for player
        """

        self.name = name
        self.species = species
        self.is_eliminated = False
        self.faction = faction

    def choose(self, decision):
        """

        args:
            decision - [Decision]
        """

        # XXX COULD LOG EVENT HERE

        choose_dispatch = {}
        choose_dispatch["human"] = self.choose_human
        choose_dispatch["test"] = self.choose_test

        return choose_dispatch[self.species](decision)

    @staticmethod
    def choose_human(decision):
        """Choose method for collecting input as string from terminal stream

        args:
            decision - [Decision]
        """

        # XXX ADD TRY CATCH STATEMENT HERE IN CASE USER HAS INPUTTED SOMETHING INCORRECT - COULD RAISE PYMADA.USERINPUTERROR
        choice = input(decision.MESSAGE)
        # XXX if choice == 'draw_board' ... then re-ask. maybe could even string inject here.
        choice_parsed = decision.parse_choice_human(choice)
        return choice_parsed

    @staticmethod
    def choose_test(decision):
        """
        args:
            decision - 
        """

        return str(decision[:-1])+'!'

    @staticmethod
    def choose_ai(decision):
        """
        args:
            decision - [Decision]
        """

        # XXX ASK NN HERE

        return decision.parse_choice_ai()
