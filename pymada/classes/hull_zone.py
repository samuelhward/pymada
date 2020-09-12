import numpy as np

import pymada
import pymada.errors
import pymada.data.tools
from pymada.classes.dice import Dice
from pymada.classes.position import Position


class HullZone:
    """Class describing a hull zone
    """

    def __init__(self, armament, shields, LoS_dot, arc_left, arc_right):
        """Constructor for hull zone

        args:
            armament - battery armament [str or Dice]
            shields - XXX
            arc_left - angle describing left-most arc edge relative to position.theta [float, deg]
            arc_right - angle describing right-most arc edge relative to position.theta [float, deg]
            LoS_dot_position - position of line-of-sight dot [Position]
        attr:
            position - position of arc origin [Position] 
            _LoS_dot_radius - relative distance from HullZone.position to line of sight dot[float, cm]
        """

        self.armament = Dice(armament)
        self.shields = shields
        self.arc_left, self.arc_right = arc_left, arc_right
        self.position = Position(x=0.0, y=0.0, theta=0.0)
        self._LoS_dot_radius = LoS_dot

        self.LoS_dot_position = Position(
            x=self.position.x
            + self._LoS_dot_radius
            * np.cos(
                (self.position.theta + (arc_left + arc_right) / 2.0) * np.pi / 180
            ),
            y=self.position.y
            + self._LoS_dot_radius
            * np.sin(
                (self.position.theta + (arc_left + arc_right) / 2.0) * np.pi / 180
            ),
        )

        self.position.add_observer(self.LoS_dot_position.move)

    def move(self, *args, **kwargs):
        """
        """

        # move the HullZone position and watchers
        self.position.move(*args, **kwargs)

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
            (
                self.LoS_dot_position.x
                - defender.hull_zones[defending_hull_zone].LoS_dot_position.x
            )
            ** 2
            + (
                self.LoS_dot_position.y
                - defender.hull_zones[defending_hull_zone].LoS_dot_position.y
            )
            ** 2
        )

        colours = {
            colour
            for colour in pymada.data.tools.rulers["range"]
            if pymada.data.tools.rulers["range"][colour] <= distance_between_LoS_dots
        }
        return colours  # XXX multiple dispatch return distance 1 for squadrons?
