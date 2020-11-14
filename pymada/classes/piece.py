import random
import pymada
import pymada.errors
from pymada.classes.base import Base
from pymada.classes.position import Position


class Piece:
    """Base class describing board pieces
    """

    def __init__(self, name, *args, **kwargs):
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
        self.colour=kwargs.get("colour", '#'+''.join([format(random.randint(0,255),'02X') for _ in range(3)]))

        self._damage = 0
        self._is_destroyed = False

    @property
    def is_destroyed(self):
        return self._is_destroyed

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

    def suffer(self, attack, *args, **kwargs):
        """
        """

        raise NotImplmentedError

    # Define multiple dispatch methods for targeting here (because for example LoS measured to objectives)
    # XXX MAKE ABCs?
    def LoS_to(self, defender, *args, **kwargs):
        """
        """
        raise NotImplmentedError

    def LoS_from(self, attacker, *args, **kwargs):
        """
        """

        raise NotImplmentedError

    def range_to(self, defender, *args, **kwargs):
        """
        """

        raise NotImplmentedError

    def range_from(self, attacker, *args, **kwargs):
        """
        """

        raise NotImplmentedError
