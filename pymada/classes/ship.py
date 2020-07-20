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

        self._data = pymada.data.ship_data.ships[model] #attach basic data

        self.hull_zone = {} #add hull-zones
        for zone in self._data["hull_zones"]:
            self.hull_zone[zone] = HullZone(
                armament=self._data["armament"][zone],
                shields=self._data["shields"][zone],
            )

        # TODO add command_dial list via command value from lookup
        # TODO add movement possibilities from lookup
        # TODO add speed as current speed
        # TODO add command token functionality e.g. if brace in Ship.command_tokens and brance is not 'exhausted':
        # TODO add .move(), which then translates and rotates the attached Base
