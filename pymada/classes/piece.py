import pymada
import pymada.errors
from pymada.classes.position import Position


class Piece:
    """Base class describing board pieces
    """

    def __init__(self):
        pass

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):

        if not isinstance(position, Position):
            raise TypeError("Piece.position must be of type Position")
        self._position = position
