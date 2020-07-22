import pymada
import pymada.errors
from pymada.classes.base import Base

class FighterBase(Base):
    """Class describing FighterBase
    """

    def __init__(self,model=None):
        """Constructor for FighterBase
        """
        super().__init__(model=model)

        # TODO should take model and type as args and search for model in ships, fighter_data and scenery_data etc. (then it could look up base size from model name)
