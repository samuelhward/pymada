import pymada
import pymada.errors
from pymada.classes.base import Base
from pymada.classes.position import Position


class Piece:
    """Base class describing board pieces
    """

    def __init__(self, name):
        """Constructor for Piece

        args:
            name - unique string identifier [str]
        """

        self.base = Base()
        self.position = Position()
        self.name = name

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):

        if not isinstance(position, Position):
            raise TypeError("Piece.position must be of type Position")
        self._position = position

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base):

        if not isinstance(base, Base):
            raise TypeError("Piece.base must be of type Base")
        self._base = base

    # TODO make ABC
    def move(self, x, y, theta):
        """
        """

        self.position.translate(x=x, y=y)
        self.position.rotate(theta=theta)
