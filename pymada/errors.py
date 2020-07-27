class PositionException(Exception):
    """Except raised for errors in Piece 
    """


class PieceException(Exception):
    """Except raised for errors in Piece 
    """

    piece_type = "Piece"

    def __init__(self, piece_instance, message):
        """Include extra name information for identifying offending instance
        """

        self.message = "".join(
            f"Error with {piece_type} {piece_instance.name}\n", message
        )
        super().__init__(self.message)


class PlayerPieceException(PieceException):
    """Except raised for errors in PlayerPiece 
    """

    piece_type = "PlayerPiece"


class ShipException(PlayerPieceException):
    """Except raised for errors in Ship 
    """

    piece_type = "Ship"


class ShipSpeedError(ShipException):
    """Except raised for errors with Ship speed
    """


class ShipYawError(ShipException):
    """Except raised for errors with Ship yaw 
    """


class ShipHullZoneError(ShipException):
    """Except raised for errors with Ship HullZones 
    """


class HullZoneError(Exception):
    """Except raised by HullZone
    """

    def __init__(self, hull_zone_instance, message):
        """Include instance information
        """

        self.message = message
        super().__init__(self.message)


class NoLoSError(HullZoneError):
    """Except raised when no line of sight between HullZones
    """
