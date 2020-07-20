import pymada
import pymada.errors


class Dice:
    """Class describing dice pool
    """

    def __init__(self, *dice):
        """Constructor for dice pool

        Examples:
            my_dice=Dice("red")
            my_dice=Dice(4*"red")
            my_dice=Dice(4*"red"+"blue")
            my_dice=4*Dice("red")+Dice("blue")
        """

        self._dice = {}
        self._dice["red"] = 0
        self._dice["blue"] = 0
        self._dice["black"] = 0

        if len(dice) is 1:  # *dice is string
            for colour in self._dice.keys():
                self[colour] += dice[0].count(colour)
        else:  # *dice is list *args of Dice objects
            for die in dice:
                for colour in die.colours:
                    self[colour] += die[colour]

        self.colours = {colour for colour in self._dice.keys() if self[colour] > 0}

    def __getitem__(self, colour):
        """
        """

        return self._dice[colour]

    def __setitem__(self, colour, count):
        """
        """

        self._dice[colour] = count

    def __add__(self, other_dice):
        """Overload for addition to return Dice object
        
        args:
            other_dice - other die to add [Dice]
        """

        return Dice(
            *[
                (self[colour] + other_dice[colour]) * Dice(colour)
                for colour in self.colours | other_dice.colours
            ]
        )

    def __mul__(self, other_factor):
        """Overload for multiplication to return Dice object

        args:
            other_factor - multiplication factor [int]
        """

        return Dice(
            "".join([self[colour] * other_factor * colour for colour in self.colours])
        )

    __rmul__ = __mul__
