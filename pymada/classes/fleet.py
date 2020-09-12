import pymada
import pymada.errors

# TODO add def draw() ship.draw() for ship in self.ships

# SHOULD CONTAIN SHIP DATA BUT NOT SHIP OBJECTS


class Fleet:
    """Class describing fleet
    """

    def __init__(self):
        """Constructor for fleet
        """

        self.ship_data = []
        self.scenarios = []

        # Ship class signature data
        self.models = []
        self.names = []
        self.factions = []
        self.upgrades = []

    def add_ship(self, model, name, faction, upgrades=None):
        """Add basic ship data to fleet
        """

        self.models.append(model)
        self.names.append(name)
        self.factions.append(faction)
        self.upgrades.append(upgrades)
