import pymada
import pymada.errors


class Position:
    """Base class describing positions
    """

    def __init__(self, x=0.0, y=0.0, theta=0.0):
        """Constructor for position including cartesian coordinates and rotation
        """
        self.x, self.y, self.theta = x, y, theta
