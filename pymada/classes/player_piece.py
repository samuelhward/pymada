import pymada
import pymada.errors
import pymada.data.ships
from pymada.classes.position import Position
from pymada.classes.piece import Piece
from pymada.classes.hull_zone import HullZone

# TODO add points as property which, when accessed, total points of the model using helper function def calculate_points()
# TODO add hull value from lookup
# TODO add speed value from lookup
# TODO add defense tokens from lookup --> needs to be a class e.g. if ship.defense_tokens['brace'][1].is_flipped()
# TODO add upgrades

class PlayerPiece(Piece):
    """Class describing playable piece
    """

    def __init__(self, model, name, faction, upgrades=None):
        """Constructor for playable piece
        """
        super().__init__(name=name)

        self.faction = faction
        self._upgrades = upgrades

    def fire(self, defender, *args, **kwargs):
        """
        
        args:
            defender -  
        """

        # TODO add some exception handling here?
        if self.LoS_to(defender, *args, **kwargs):
            attack_range = self.range_to(defender, *args, **kwargs)
            if attack_range:
                attack = self.create_attack_pool(*args, **kwargs)

                #XXX more modifications here

                attack.roll(attack_range)

                #XXX even more modifications here

                #XXX AT THIS POINT CHECK DEFENDING HULL ZONE IN ENEMY SHIP AND TAKE OFF SHIELDS ETC.
                defender.suffer(damage=attack.damage_normal+attack.damage_critical,*args,**kwargs) 

            # TODO add various attack stages here e.g. spend defense tokens

    # TODO make ABC
    def create_attack_pool(*args, **kwargs):
        """
        """

        attack_range

        return None
