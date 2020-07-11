import pytest
import os, sys  # explicitly modify path to avoid having to constantly run setup.py to test code

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pymada
import pymada.errors
from pymada.classes.base import Base
from pymada.classes.piece import Piece
from pymada.classes.position import Position


def test_piece_position():
    """Check setting a piece's position incorrectly raises TypeError
    """

    test_piece = Piece()
    test_piece.position = Position(x=5.0, y=5.0, theta=0.0)

    with pytest.raises(TypeError):
        test_piece.position = 5.0

def test_piece_base():
    """Check setting a piece's base incorrectly raises TypeError
    """

    test_piece = Piece()
    test_piece.base = Base()

    with pytest.raises(TypeError):
        test_piece.base = 5.
