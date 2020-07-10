import pytest
import os, sys  # explicitly modify path to avoid having to constantly run setup.py to test code

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pymada
import pymada.errors
from pymada.classes.position import Position
from pymada.classes.piece import Piece


def test_set_position():
    """Check set position assigns a position instance
    """

    test_piece = Piece()
    test_piece.position = Position(x=5.0, y=5.0, theta=0.0)

    with pytest.raises(TypeError):
        test_piece.position = 5.0
