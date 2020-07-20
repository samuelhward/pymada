import pymada
import pymada.errors


class Base:
    """Class describing Piece Base
    """

    def __init__(self):
        """Constructor for Base
        """
        pass

        # TODO add generic functions here e.g. for detecting collision i.e. if myShip.Base.overlaps(enemyFighter.Base()):
        # TODO add translate and rotate as helpers for inherited Move method
        # TODO add type of base e.g. FighterBase, ShipBase for specifics such as .move which first Base.rotates and then Base.translates for each notch for ship, or just Base.translates for fighters
        # TODO should take model and type as args and search for model in ship_data, fighter_data and scenery_data etc. (then it could look up base size from model name)
