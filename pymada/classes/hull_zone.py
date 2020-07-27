import numpy as np

import pymada
import pymada.errors
import pymada.data.tools
from pymada.classes.dice import Dice
from pymada.classes.position import Position


class HullZone:
    """Class describing a hull zone
    """

    def __init__(self, armament, shields, LoS_dot, arc_left, arc_right, position):
        """Constructor for hull zone

        args:
            armament - battery armament [str or Dice]
            shields - XXX
            LoS_dot - distance from HullZone.position to line of sight dot[float, cm]
            arc_left - angle describing left-most arc edge relative to position.theta [float, deg]
            arc_right - angle describing right-most arc edge relative to position.theta [float, deg]
            position - position of arc origin [Position] 
        """

        self.armament = Dice(armament)
        self.shields = shields
        self.LoS_dot = LoS_dot
        self.arc_left, self.arc_right = arc_left, arc_right
        self.position = position
        # TODO add arc length
        # TODO add hull_zone position (which is where the edges converge i.e. the centre of the model's base)
        # TODO add theta --> from arc length and theta can then calculate arcs

    def move(self, *args, **kwargs):
        """
        """

        # first move the HullZone position
        self.position.move(*args, **kwargs)

        # then recalculate the x,y coordinates of the LoS dot regardless of move method above
        self.LoS_dot_x = self.position.x + self.LoS_dot * np.cos(self.position.theta)
        self.LoS_dot_y = self.position.y + self.LoS_dot * np.sin(self.position.theta)

    def has_LoS_to(defender, defending_hull_zone):
        """

        XXX requires multiple dispatch to measure against instances without hull_zones e.g. scenery
        """

        # TODO proper method here

        return True

    def in_range_of(defender, defending_hull_zone):
        """

        XXX requires multiple dispatch to measure against instances without hull_zones e.g. scenery
        XXX could have generic in_range_of function which just measures between any two objects no matter what type?

        args:
            defender - [Piece]
            defending_hull_zone []
        """

        # TODO proper method here

        distance_between_LoS_dots = np.sqrt(
            (self.LoS_dot_x - defender.hull_zones[defending_hull_zone].LoS_dot_x) ** 2
            + (self.LoS_dot_y - defender.hull_zones[defending_hull_zone].LoS_dot_y) ** 2
        )

        colours = {
            colour
            for colour in pymada.data.tools.rulers["range"]
            if pymada.data.tools.rulers["range"][colour] <= distance_between_LoS_dots
        }
        return colours  # XXX multiple dispatch return distance 1 for fighters?

    def fire(defender, defending_hull_zone):
        """
        """
