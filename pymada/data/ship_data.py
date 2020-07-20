"""ship_data
"""
from pymada.classes.dice import Dice

ships = {}


def create_ship_data_template():
    """ Helper function to initialise ship information
    """

    ship_template = {}
    ship_template["hull_zones"] = {}
    ship_template["shields"] = {}
    ship_template["armament"] = {}
    ship_template["move"] = {}
    ship_template["upgrades"] = {}

    ship_template["command"] = None
    ship_template["hull"] = None
    ship_template["points"] = None
    ship_template["size"] = None  # small, medium, large, giant, flotilla
    ship_template["engineering"] = None
    ship_template["squadron"] = None

    return ship_template


# define a test ship

ships["test_ship"] = create_ship_data_template()
ships["test_ship"]["points"] = 100
ships["test_ship"]["defense_tokens"] = ["brace"]
ships["test_ship"]["hull_zones"] = {"front", "left", "right", "rear"}
ships["test_ship"]["shields"]["front"] = 1
ships["test_ship"]["shields"]["left"] = 1
ships["test_ship"]["shields"]["right"] = 1
ships["test_ship"]["shields"]["rear"] = 1
ships["test_ship"]["armament"]["front"] = 1 * "red"
ships["test_ship"]["armament"]["left"] = 1 * "blue"
ships["test_ship"]["armament"]["right"] = 1 * "blue"
ships["test_ship"]["armament"]["rear"] = 1 * "blue"
ships["test_ship"]["armament"]["anti-squad"] = 1 * "black"
ships["test_ship"]["move"][1] = [1]
ships["test_ship"]["move"][2] = [1, 0]
ships["test_ship"]["upgrades"]["turbolasers"] = []
ships["test_ship"]["upgrades"]["size"] = "small"
ships["test_ship"]["engineering"] = 2
ships["test_ship"]["squadron"] = 1
ships["test_ship"]["size"] = "small"
ships["test_ship"]["command"] = 1
ships["test_ship"]["hull"] = 2
