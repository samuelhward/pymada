import numpy as np

import pymada
import pymada.errors
import pymada.data.ships
import pymada.classes.utils
from pymada.classes.position import Position


class Base:
    """Class describing Base of a model on the board
    """

    def __init__(self, size=None):
        """Constructor for Base
        """

        self.size = size
        self.centre = Position(x=0.0, y=0.0, theta=0.0)

        # all ships start on heading theta=0. degrees - define base points accordingly

        if self.size:
            width = pymada.data.ships.bases[self.size]["width"]
            height = pymada.data.ships.bases[self.size]["height"]

            # XXX corners for ship, just linspace for fighters - make a Position() and add as observer to base.Position
            self.outline = []

            # XXX define square for now
            for quadrant in [[1.0, 1.0], [1.0, -1.0], [-1.0, -1.0], [-1.0, 1.0]]:
                point = Position(
                    x=self.centre.x + quadrant[0] * width / 2.0,
                    y=self.centre.y + quadrant[1] * height / 2.0,
                )
                self.outline.append(point)
                # add this point as observer to centre position
                self.centre.add_observer(point.move)

    def move(self, *args, **kwargs):
        """Move base centre with outline using rotation matrix
        """

        # apply move to Base centre and watchers
        self.centre.move(*args, **kwargs)

        # TODO add dimensions from ship_data
        # TODO add generic functions here e.g. for detecting collision i.e. if myShip.Base.overlaps(enemyFighter.Base()):
        # TODO add translate and rotate as helpers for inherited Move method
        # TODO add type of base e.g. FighterBase, ShipBase for specifics such as .move which first Base.rotates and then Base.translates for each notch for ship, or just Base.translates for fighters
        # TODO should take model and type as args and search for model in ships, fighter_data and scenery_data etc. (then it could look up base size from model name)
