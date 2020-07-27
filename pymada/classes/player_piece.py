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
        self.hull_zones = None

        # TODO add points as property which, when accessed, total points of the model using helper function def calculate_points()

        # TODO add hull value from lookup
        # TODO add speed value from lookup
        # TODO add defense tokens from lookup --> needs to be a class e.g. if ship.defense_tokens['brace'][1].is_flipped()
        # TODO add upgrades

    def fire(self, attacking_hull_zone, defender, defending_hull_zone=None):
        """
        """

        if not attacking_hull_zone in self.hull_zones:
            raise ShipHullZoneError(
                self, f"'{attacking_hull_zone}' hull zone not found in {self.name}"
            )

        if not defending_hull_zone in defender.hull_zones:
            raise ShipHullZoneError(
                self, f"'{defending_hull_zone}' hull zone not found in {defender.name}",
            )

        if self.hull_zones[attacking_hull_zone].has_LoS_to(
            defender, defending_hull_zone
        ):
            if self.hull_zones[attacking_hull_zone].in_range_of(
                defender, defending_hull_zone
            ):

                attack_pool = self.hull_zones[attacking_hull_zone].fire(
                    defender, defending_hull_zone
                )

                # TODO add various attack stages here e.g. spend defense tokens

            else:
                raise pymada.errors.NoLoS(
                    self.hull_zones[attacking_hull_zone],
                    f"'{attacking_hull_zone}' hull zone of {self.name} is not in range '{defending_hull_zone}' hull zone of {defender.name}",
                )
        else:
            raise pymada.errors.NotInRange(
                self.hull_zones[attacking_hull_zone],
                f"'{attacking_hull_zone}' hull zone of {self.name} has no line of sight to '{defending_hull_zone}' hull zone of {defender.name}",
            )
