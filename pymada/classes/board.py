"""Game board
"""
import sys
import os, sys  # explicitly modify path to avoid having to constantly run setup.py to test code

import pymada
import pymada.errors
import pymada.data.tools
from pymada.classes.position import Position


class Board:
    """Class describing the game board and all the pieces on it
    """

    PLAY_AREA_WIDTH = 6.0 * 30.48  # feet to cm
    PLAY_AREA_HEIGHT = 3.0 * 30.48  # feet to cm
    SETUP_AREA_WIDTH = 4.0 * 30.48  # feet to cm
    SETUP_AREA_HEIGHT = 3.0 * 30.48  # feet to cm
    DEPLOYMENT_AREA_WIDTH = 4.0 * 30.48
    DEPLOYEMENT_ZONE_DEPTH = pymada.data.tools.rulers["distance"][3]
    DEPLOYMENT_AREA_HEIGHT = 3.0 * 30.48 - 2.0 * DEPLOYEMENT_ZONE_DEPTH

    def __init__(self, width=PLAY_AREA_WIDTH, height=PLAY_AREA_HEIGHT, play_area=True):
        """
        """

        # board geometry
        self.origin = Position(x=0.0, y=0.0)
        self.width = width
        self.height = height
        self.outline = []

        for quadrant in [[1.0, 1.0], [1.0, -1.0], [-1.0, -1.0], [-1.0, 1.0]]:
            self.outline.append(
                Position(
                    x=quadrant[0] * self.width / 2.0, y=quadrant[1] * self.height / 2.0
                )
            )

        # if we are the main game board then attach sub-boards for setup and deployment
        if play_area:
            self.zones = {}
            self.zones["setup"] = Board(
                width=self.SETUP_AREA_WIDTH,
                height=self.SETUP_AREA_HEIGHT,
                play_area=False,
            )
            self.zones["deployment"] = Board(
                width=self.DEPLOYMENT_AREA_WIDTH,
                height=self.DEPLOYMENT_AREA_HEIGHT,
                play_area=False,
            )

        # add pieces
        self.ships = []
        self.obstacles = []

    def add_ships(self, *ships):
        """
        args:
            ships - ship instances to add to board *[Ship]
        """

        self.ships.extend(ships)

    def remove_ship(self, *names):
        """
        args:
            names - ship string names to remove from board *[str]
        """

        ships_to_remove = []
        for name in names:
            for counter, ship in enumerate(self.ships):
                if ship.name is name:
                    ships_to_remove.append(counter)
        for ship in ships_to_remove.reverse():
            del self.ships[counter]

    def add_obstacles(self, *obstacles):
        """
        args:
            obstacles - obstacle instances to add to board *[Obstacle]
        """

        self.obstacles.extend(obstacles)
