from .position import Position


class Piece:
    """Base class describing board pieces
    """

    def __init__(self, position):
        self.position = position

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):

        if not isinstance(position, Position):
            raise TypeError()
        self._position = position
