import pymada
import pymada.errors
import pymada.data.ship_data
from pymada.classes.position import Position
from pymada.classes.piece import Piece
from pymada.classes.hull_zone import HullZone


class PlayerPiece(Piece):
    """Class describing playable piece
    """

    def __init__(self, model, name, faction, upgrades=None):
        """Constructor for playable piece
        """
        super().__init__(model=model)

        self.name = name
        self.faction = faction

        self._upgrades = upgrades

        # TODO add points as property which, when accessed, total points of the model using helper function def calculate_points()

        # TODO add hull value from lookup
        # TODO add speed value from lookup
        # TODO add defense tokens from lookup --> needs to be a class e.g. if ship.defense_tokens['brace'][1].is_flipped()
        # TODO add upgrades
