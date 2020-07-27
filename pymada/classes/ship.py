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

        # XXX should be property - since speed cannot ever go over max([speed for speed in self._data["move"]])
        # TODO check here if speed is valid
        self.speed = speed

        # XXX IN FUTURE ATTACH HULLZONES AND POSITION TO BASE HERE BECAUSE RANGE IS HULLZONE-DEPENDENT
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
            self.position.add_observer(
                self.hull_zones[zone].move
            )  # attach this hull_zone.move() method as observer of Ship position

    def move(self, clicks):
        """Ship-specific implementation of move() method

        args:
        notes:
            ships in armada move THEN rotate
        XXX ship moves in armada are actually not from the centre - this is definitely different
        TODO implement collision checks, move can just call itself recursively with decreasing speed until no overlap event - could raise events.ShipOverlap()?
        """

        # first test move is valid
        if self.speed not in self._data["move"]:
            raise pymada.errors.ShipSpeedError(
                self,
                f"requested speed={self.speed} not available - options = {[speed for speed in self._data['move']]}",
            )

        if not all(
            [
                np.abs(clicks[sub_speed]) <= self._data["move"][self.speed][sub_speed]
                for sub_speed in range(self.speed)
            ]
        ):

            # TODO this will need to regard command dial effects
            raise pymada.errors.ShipYawError(
                self,
                f"requested yaw too high in maneuver {[clicks[sub_speed] for sub_speed in range(self.speed)]} - maximum = {[self._data['move'][self.speed][sub_speed] for sub_speed in range(self.speed)]}",
            )

        # allow clicks at higher speeds to be specified - if testing for collisions we just repeat but with speed-=1
        assert len(clicks) >= self.speed

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

            # first translate forward at current theta then rotate to new theta - this same method will be passed to all observers
            self.position.move(
                r=sub_move_dist,
                theta_translate=self.position.theta,
                theta_rotate_last=rotation_theta,
            )

        # TODO add command_dial list via command value from lookup
        # TODO add command token functionality e.g. if brace in Ship.command_tokens and brance is not 'exhausted':
