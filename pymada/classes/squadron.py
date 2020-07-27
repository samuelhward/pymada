import pymada
import pymada.errors
from pymada.classes.position import Position
from pymada.classes.player_piece import PlayerPiece
from pymada.classes.hull_zone import HullZone


class Squadron(PlayerPiece):
    """Class describing squadron piece
    """

    def __init__(self, name, faction, model):
        """Constructor for squadron
        """
        super().__init__(name=name, faction=faction, model=model)


        #TODO add unique status
        #TODO make sure all Squadron hullzone arc lengths are 360 degrees

        '''
        #TODO
        def move(self, x=0.0, y=0.0, r=None, theta=0.): #do not use self.theta here like a ship! 
            self.position.translate(self, x=0.0, y=0.0, r=None, theta=0.)
        '''
