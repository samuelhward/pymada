import numpy as np

import pymada
import pymada.errors
from pymada.classes.position import Position

# TODO add dimensions from ship_data
# TODO add generic functions here e.g. for detecting collision i.e. if myShip.Base.overlaps(enemysquadron.Base()):
# TODO add translate and rotate as helpers for inherited Move method
# TODO add type of base e.g. squadronBase, ShipBase for specifics such as .move which first Base.rotates and then Base.translates for each notch for ship, or just Base.translates for squadrons
# TODO should take model and type as args and search for model in ships, squadron_data and scenery_data etc. (then it could look up base size from model name)


class Base:
    """Class describing Base of a model on the board
    """

    def __init__(self, outline_points_x=None, outline_points_y=None):
        """Constructor for Base
        """

        self.centre = Position(x=0.0, y=0.0, theta=0.0)
        self.outline = []

        if outline_points_x and outline_points_y:
            for x, y in zip(outline_points_x, outline_points_y):
                self.outline.append(Position(x=x, y=y))
            # add outline points as observers to centre position
            for position, _ in enumerate(self.outline):
                self.centre.add_observer(self.outline[position].move)

    def move(self, *args, **kwargs):
        """Move base centre with outline using rotation matrix
        """

        # apply move to Base centre and watchers
        self.centre.move(*args, **kwargs)
