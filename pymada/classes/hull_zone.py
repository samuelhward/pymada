import pymada
import pymada.errors
from pymada.classes.dice import Dice


class HullZone:
    """Class describing a hull zone
    """

    def __init__(self, armament, shields, LoS_dot, arc_left, arc_right, position):
        """Constructor for hull zone
        """

        self.armament = Dice(armament)
        self.shields = shields
        self.LoS_dot = LoS_dot
        self.arc_left, self.arc_right = arc_left, arc_right
        self.position = position
        # TODO .fire() method with .can_fire_on() method - NOTE that arc_left is measured from self.position.theta
        # TODO add arc length
        # TODO add hull_zone position (which is where the edges converge i.e. the centre of the model's base)
        # TODO add theta --> from arc length and theta can then calculate arcs
