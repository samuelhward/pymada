import pymada
import pymada.errors
from pymada.classes.position import Position
from pymada.classes.player_piece import PlayerPiece
from pymada.classes.hull_zone import HullZone


class Ship(PlayerPiece):
    """Class describing ship piece
    """

    def __init__(self, name, faction, model, upgrades):
        """Constructor for ship
        """

        super().__init__(name=name, faction=faction, model=model)

        self.upgrades = upgrades


        #TODO add command value from lookup
        #TODO add movement possibilities from lookup
        #TODO add possible upgrade slots from lookup
