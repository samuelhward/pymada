import pymada
import pymada.errors
from pymada.classes.position import Position
from pymada.classes.player_piece import PlayerPiece
from pymada.classes.hull_zone import HullZone


class Ship(PlayerPiece):
    """Class describing a Ship
    """

    def __init__(self, model, name, faction, upgrades=None):
        """Constructor for Ship
        """

        super().__init__(model=model, name=name, faction=faction, upgrades=upgrades)

        self._data = pymada.data.ship_data.ships[model]

        """
        self.hull_zone={}
        for zone in self._ship_data["hull_zones"]:
            self.hull_zone[zone] = HullZone(
                armament=self._ship_data["armament"][zone],
                shields=self._ship_data["shields"][zone],
            )
        """

        # TODO add hullzones reading
        # TODO add command value from lookup
        # TODO add movement possibilities from lookup
