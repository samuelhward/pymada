import pymada
import pymada.errors


class HullZone:
    """class describing a hull zone
    """

    def __init__(self, model, zone):
        """Constructor for hull zone
        """

        self.model = model
        self.zone = zone
        # TODO add shields, armament, .fire() method
        # TODO add arc length 
        # TODO add theta