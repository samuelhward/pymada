import pymada
import pymada.errors
from pymada.classes.base import Base
from pymada.classes.position import Position


class Piece:
    """Base class describing board pieces
    """

    def __init__(self, model=None):
        """Constructor for Piece

        args:
            model - name of the real plastic model [str]        
        """

        self.base=Base()

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
