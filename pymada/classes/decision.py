"""Game and context
"""

import os, sys, ast

import pymada
import pymada.errors


def Decision(name, *args, **kwargs):
    """
    """

    DECISIONS = {}
    DECISIONS["select_player"] = DecideSelectPlayer
    DECISIONS["select_friendly_piece"] = DecideFriendlyPiece
    DECISIONS["select_enemy_piece"] = DecideEnemyPiece
    DECISIONS["clicks_to_move"] = DecideClicksToMove
    DECISIONS["select_hull_zone"] = DecideHullZone
    DECISIONS["test_choice"] = BaseDecision

    return DECISIONS[name](*args, **kwargs)


class BaseDecision:
    """
    """

    MESSAGE = ""

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.options = kwargs.get("options", "")
        if self.options:
            self.MESSAGE += " - options:" + "".join(
                ["\n{}".format(option) for option in self.options] + ["\n"]
            )

    def parse_choice_human(self, choice):
        """

        args:
            choice - human terminal input in response to MESSAGE [str]
        """

        raise NotImplmentedError

    def parse_choice_ai(self, choice):
        """
        """

        raise NotImplmentedError

    def parse_choice_test(self,choice):
        """
        """

        return str(choice[:-1])+'!'


class DecideSelectPlayer(BaseDecision):
    """
    """

    MESSAGE = "please select a player\n"

    def parse_choice_human(self, choice):
        """
        """

        # no parsing necessary since user inputs player name as string
        return choice


class DecideFriendlyPiece(BaseDecision):
    """
    """

    MESSAGE = "please select a friendly piece\n"

    def parse_choice_human(self, choice):
        """
        """

        # no parsing necessary since user inputs ship name as string
        return choice

class DecideEnemyPiece(BaseDecision):
    """
    """

    MESSAGE = "please choose an enemy piece\n"

    def parse_choice_human(self, choice):
        """
        """

        # no parsing necessary since user inputs enemy piece name as string
        return choice
        
class DecideClicksToMove(BaseDecision):
    """
    """

    MESSAGE = "please enter move command in format [clicks1, clicks2...]\n"

    def parse_choice_human(self, choice):
        """
        """

        # TODO CHECK CHOICE HERE - IF NOT CORRECT RAISE SOMETHING LIKE PYMADA.USERINPUTERROR

        return ast.literal_eval(choice)

class DecideHullZone(BaseDecision):
    """
    """

    MESSAGE = "please choose a hull zone\n"

    def parse_choice_human(self, choice):
        """
        """

        # no parsing necessary since user inputs enemy piece name as string
        return choice
