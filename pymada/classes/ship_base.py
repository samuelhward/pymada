import pymada
import pymada.errors
from pymada.classes.base import Base
import pymada.data.ships

class ShipBase(Base):
    """Class describing ShipBase
    """

    def __init__(self,model=None):
        """Constructor for ShipBase
        """
        super().__init__(model=model)

        self._data = pymada.data.ships.ships[model]  # attach basic data

        # TODO should take model and type as args and search for model in ships, fighter_data and scenery_data etc. (then it could look up base size from model name)
