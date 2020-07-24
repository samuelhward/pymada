import copy
import numpy as np
import pymada
import pymada.errors
import pymada.data.ships
import pymada.data.tools
from pymada.classes.position import Position
from pymada.classes.player_piece import PlayerPiece
from pymada.classes.hull_zone import HullZone


class Ship(PlayerPiece):
    """Class describing a Ship
    """

    def __init__(self, model, name, faction, speed=0.0, upgrades=None):
        """Constructor for Ship
        """

        super().__init__(model=model, name=name, faction=faction, upgrades=upgrades)

        self._data = pymada.data.ships.ships[model]  # attach basic data

        self.speed = speed  # XXX should be property - since speed cannot ever go over max([speed for speed in self._data["move"]])

        self.position = Position(x=0.0, y=0.0, theta=0.0)

        self.hull_zones = {}  # add hull-zones
        for zone in self._data["hull_zones"]:
            self.hull_zones[zone] = HullZone(
                armament=self._data["armament"][zone],
                shields=self._data["shields"][zone],
                LoS_dot=self._data["LoS_dots"][zone],
                arc_left=self._data["arc_left"][zone],
                arc_right=self._data["arc_right"][zone],
                position=copy.deepcopy(self.position),
            )

    def move(self, clicks):
        """

        TODO implement collision checks, move can just call itself recursively with decreasing speed until no overlap event - could raise events.ShipOverlap()?
        """

        """
        if speed not in self._data["move"]:
            raise ShipSpeedError

        if not all([np.abs(clicks[sub_speed])<=self._data["move"][speed][sub_speed] for sub_speed in range(speed)]): #TODO this will need to regard command dial effects
            raise ShipYawError

        assert(len(clicks)>=speed) #clicks can be longer, since if testing for collisoin we just repeat but with speed-=1
        """

        # loop over sub_moves
        for click_values, sub_move_dist, click_options in zip(
            clicks,
            pymada.data.tools.maneuver["distance"][self.speed],
            pymada.data.tools.maneuver["yaw"][self.speed],
        ):

            # calculate total theta change for this sub_move
            rotation_theta = 0.0
            rotation_dir = (
                click_values if click_values == 0 else click_values / abs(click_values)
            )
            for click_value in range(abs(click_values)):
                rotation_theta += click_options[click_value] * rotation_dir

            # first translate forward at current theta then rotate to new theta
            super().move(
                x=sub_move_dist * np.cos(self.position.theta),
                y=sub_move_dist * np.sin(self.position.theta),
                theta=rotation_theta,
            )

        for zone in self.hull_zones:  # reposition all Ship's HullZones
            self.hull_zones[zone].position = copy.deepcopy(self.position)

        # then decorate with @move_ship which also rotates the HullZones etc, then in decorator just move 'forward' where we then calc x and y translate to feed to position.translate

        # def self.move() - which uses self.position.translate and self.position.rotate, which also rotates HullZones

        # TODO add command_dial list via command value from lookup
        # TODO add movement possibilities from lookup
        # TODO add command token functionality e.g. if brace in Ship.command_tokens and brance is not 'exhausted':
