import pymada
import pymada.errors
from pymada.classes.position import Position
from pymada.classes.piece import Piece
from pymada.classes.hull_zone import HullZone


class PlayerPiece(Piece):
    """Class describing playable piece
    """

    def __init__(self, name, faction, model):
        """Constructor for playable piece
        """
        super().__init__()

        self.name = name
        self.faction = faction
        self.model = model
        self.hull_zone = {}

        # TODO instead of ["front", "rear", "left", "right"] look up pymada.data.ships[self.model]['hull_zones'].keys()
        # TODO to allow for SSD, squadrons etc.
        for zone in ["front", "rear", "left", "right"]:
            self.hull_zone[zone] = HullZone(model=self.model, zone=zone)


        # TODO calculate points here
        # TODO self.points=pymada.data.ships[self.model]['points']

        # TODO add base hull value from lookup
        # TODO add base speed value from lookup
        # TODO add defense tokens from lookup --> needs to be a class e.g. if ship.defense_tokens['brace'][1].is_flipped()