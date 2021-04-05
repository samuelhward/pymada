import pymada
import pymada.errors
import pymada.data.ships
from pymada.classes.dice import Dice
from pymada.classes.position import Position
from pymada.classes.piece import Piece
from pymada.classes.hull_zone import HullZone

# TODO add points as property which, when accessed, total points of the model using helper function def calculate_points()
# TODO add defense tokens from lookup --> needs to be a class e.g. if ship.defense_tokens['brace'][1].is_flipped()
# TODO add upgrades


class PlayerPiece(Piece):
    """Class describing playable piece
    """

    def __init__(self, model, name, faction, player_name=None, upgrades=None):
        """Constructor for playable piece
        """
        super().__init__(name=name)

        self.faction = faction
        self._upgrades = upgrades
        self.has_activated = False
        self.player_name = player_name

    def activate(self):
        """
        """

        self.has_activated = True

    def deactivate(self):
        """
        """

        self.has_activated = False

    def can_fire(self, defender, *args, **kwargs):
        """
        """

        # first check line of sight

        if self.LoS_to(defender, *args, **kwargs):

            # calculate range to target

            range_to = self.range_to(defender, *args, **kwargs)

            # does attacker possess necessary attack dice for this range
            if range_to:

                if (
                    Dice.RANGE_COLOURS[range_to]
                    & self.create_attack_pool(*args, **kwargs).colours
                ):
                    return True

        return False

    def fire(self, defender, *args, **kwargs):
        """
        
        args:
            defender -  
        """

        if self.can_fire(defender, *args, **kwargs):

            attack_range = self.range_to(defender, *args, **kwargs)

            attack = self.create_attack_pool(*args, **kwargs)

            # XXX more modifications here

            attack.roll(attack_range)

            # XXX even more modifications here

            # TODO add various attack stages here e.g. spend defense tokens

            defender.suffer(attack, *args, **kwargs)

    # TODO make ABC
    def create_attack_pool(*args, **kwargs):
        """Return deep copy of attacking Dice armament
        """

        raise NotImplmentedError
