import pymada
import pymada.errors
import pymada.classes.die


class Dice:
    """Class describing dice pool
    """

    def __init__(self, *dice):
        """Constructor for dice pool
        """

        self._dice = {}
        self._dice["red"] = 0
        self._dice["blue"] = 0
        self._dice["black"] = 0

        for die in dice:
            if isinstance(die, pymada.classes.die.Die):
                self[die.colour] += 1

            elif isinstance(die, Dice):
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
            other_dice - other die to add [Die or Dice]
        """

        if isinstance(other_dice, pymada.classes.die.Die):

            return Dice(
                *[
                    self[colour] + 1 * pymada.classes.die.Die(colour)
                    if colour is other_dice.colour
                    else self[colour] * pymada.classes.die.Die(colour)
                    for colour in self.colours
                ]
            )

        elif isinstance(other_dice, Dice):

            return Dice(
                *[
                    (self[colour] + other_dice[colour]) * pymada.classes.die.Die(colour)
                    for colour in self.colours | other_dice.colours
                ]
            )

    def __mul__(self, other_factor):
        """Overload for multiplication to return Dice object

        args:
            other_factor - multiplication factor [int]
        """

        return Dice(
            *[
                (self[colour] * other_factor) * pymada.classes.die.Die(colour)
                for colour in self.colours
            ]
        )

    __rmul__ = __mul__
