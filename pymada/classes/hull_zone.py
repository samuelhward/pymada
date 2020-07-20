import pymada
import pymada.errors
from pymada.classes.dice import Dice


class HullZone:
    """Class describing a hull zone
    """

    def __init__(self, armament, shields):
        """Constructor for hull zone
        """

        self.armament = Dice(armament)
        self.shields = shields

        # TODO .fire() method
        # TODO add arc length
        # TODO add LoS dot position + hull_zone position (which is where the edges converge i.e. the centre of the model's base)
        # TODO add theta --> from arc length and theta can then calculate arcs
