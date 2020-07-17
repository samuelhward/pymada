import pymada
import pymada.errors
import pymada.classes.dice


class Die:
    """Class describing dice
    """

    def __init__(self, colour):
        """Constructor for die
        
        args:
            colour - die colour [str]
        """

        self.colour = colour

    def __add__(self, other_die):
        """Overload for addition to return Dice object
        
        args:
            other_die - other die to add [Die or Dice]
        """

        return pymada.classes.dice.Dice(self, other_die)

    def __mul__(self, other_factor):
        """Overload for multiplication to return Dice object

        args:
            other_factor - multiplication factor [int]
        """

        return pymada.classes.dice.Dice(*[self for _ in range(other_factor)])

    __rmul__ = __mul__
