import pymada
import pymada.errors
import pymada.data.ships
from pymada.classes.position import Position
from pymada.classes.piece import Piece
from pymada.classes.hull_zone import HullZone


class PlayerPiece(Piece):
    """Class describing playable piece
    """

    def __init__(self, model, name, faction, upgrades=None):
        """Constructor for playable piece
        """
        super().__init__(name=name)

        self.faction = faction
        self._upgrades = upgrades

        # TODO add points as property which, when accessed, total points of the model using helper function def calculate_points()

        # TODO add hull value from lookup
        # TODO add speed value from lookup
        # TODO add defense tokens from lookup --> needs to be a class e.g. if ship.defense_tokens['brace'][1].is_flipped()
        # TODO add upgrades

    #'''
    def fire(self,attacking_hull_zone,defending_ship,defending_hull_zone=None):
        """
        """


        ShipA.hull_zones['front'].fire(['rear'])


        #TODO check attacking_hull_zone and defending_hull_zone are valid here

        #TODO add NotImplementedError for has_LoS_to
        if self.hull_zones[attacking_hull_zone].has_LoS_to(defending_ship.hull_zones[defending_hull_zone]):

    
            if self.hull_zones[attacking_hull_zone].has_LoS_to(defending_ship.hull_zones[defending_hull_zone]):

        else:
            raise pymada.errors.NoLoSError 


    #'''