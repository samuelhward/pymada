"""ships
"""

import copy
import numpy as np
from pymada.classes.dice import Dice

bases = {}
for size in ["small", "medium", "large"]:
    bases[size] = {}
bases["small"]["width"] = 4.3
bases["small"]["height"] = 7.2
bases["medium"]["width"] = 6.3
bases["medium"]["height"] = 10.35
bases["large"]["width"] = 7.75
bases["large"]["height"] = 13.1


ships = {}


def create_ships_template():
    """ Helper function to initialise ship information
    """

    ship_template = {}
    ship_template["hull_zones"] = {}
    ship_template["shields"] = {}
    ship_template["armament"] = {}
    ship_template["arc"] = {}
    ship_template["move"] = {}
    ship_template["upgrades"] = {}
    ship_template["LoS_dots"] = {}

    ship_template["command"] = None
    ship_template["hull"] = None
    ship_template["points"] = None
    ship_template["size"] = None  # small, medium, large, giant, custom
    ship_template["engineering"] = None
    ship_template["squadron"] = None

    return ship_template


# define a test ship

ships["test_ship"] = create_ships_template()
ships["test_ship"]["engineering"] = 2
ships["test_ship"]["squadron"] = 1
ships["test_ship"]["size"] = "small"
ships["test_ship"]["command"] = 1
ships["test_ship"]["hull"] = 2
ships["test_ship"]["points"] = 100
ships["test_ship"]["defense_tokens"] = ["brace"]
ships["test_ship"]["hull_zones"] = {"front", "left", "right", "rear"}
ships["test_ship"]["shields"]["front"] = 1
ships["test_ship"]["shields"]["left"] = 1
ships["test_ship"]["shields"]["right"] = 1
ships["test_ship"]["shields"]["rear"] = 1
ships["test_ship"]["LoS_dots"]["front"] = (
    bases[ships["test_ship"]["size"]]["height"] / 4.0
)
ships["test_ship"]["LoS_dots"]["left"] = (
    bases[ships["test_ship"]["size"]]["width"] / 4.0
)
ships["test_ship"]["LoS_dots"]["right"] = (
    bases[ships["test_ship"]["size"]]["width"] / 4.0
)
ships["test_ship"]["LoS_dots"]["rear"] = (
    bases[ships["test_ship"]["size"]]["height"] / 4.0
)
ships["test_ship"]["armament"]["front"] = 1 * "red"
ships["test_ship"]["armament"]["left"] = 1 * "blue"
ships["test_ship"]["armament"]["right"] = 1 * "blue"
ships["test_ship"]["armament"]["rear"] = 1 * "blue"
ships["test_ship"]["arc"]["front"] = 2.0 * np.arctan2(
    bases[ships["test_ship"]["size"]]["width"],
    bases[ships["test_ship"]["size"]]["height"],
)
ships["test_ship"]["arc"]["left"] = 180.0 - ships["test_ship"]["arc"]["front"]
ships["test_ship"]["arc"]["right"] = copy.deepcopy(ships["test_ship"]["arc"]["left"])
ships["test_ship"]["arc"]["rear"] = copy.deepcopy(ships["test_ship"]["arc"]["front"])
ships["test_ship"]["armament"]["anti-squad"] = 1 * "black"
ships["test_ship"]["move"][1] = [1]
ships["test_ship"]["move"][2] = [1, 0]
ships["test_ship"]["upgrades"]["turbolasers"] = []
ships["test_ship"]["upgrades"]["size"] = "small"

# TODO need load_from_RK() here which translates RK list to data above
