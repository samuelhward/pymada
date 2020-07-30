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

        self.name = name
        self.base = Base()
        self.position = Position()
        self.position.add_observer(
            # add base as observer
            self.base.move
        )
        self._damage = 0

    @property
    def damage(self):
        """

        notes:
            child classes may define damage in different ways so define as property 
        """

        return self._damage

    # XXX make ABC?
    def move(self, *args, **kwargs):
        """
        """

        self.position.move(*args, **kwargs)

    def suffer(*args, **kwargs):
        """
        """

        pass

    # Define multiple dispatch methods for targeting here (because for example LoS measured to objectives)
    # XXX MAKE ABCs?
    def LoS_to(self, defender, *args, **kwargs):
        """
        """
        pass

    def LoS_from(self, attacker, *args, **kwargs):
        """
        """
        return True

    def range_to(self, defender, *args, **kwargs):
        """
        """

        pass

    def range_from(self, attacker, *args, **kwargs):
        """
        """

        return True
