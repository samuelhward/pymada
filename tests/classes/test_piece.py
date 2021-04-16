import pymada.classes.piece
import pymada.classes.position


def test_piece_position():
    """Check setting a piece's position incorrectly raises TypeError"""

    test_piece = pymada.classes.piece.Piece(name="test piece")
    test_piece.position = pymada.classes.position.Position(x=5.0, y=5.0, theta=0.0)
