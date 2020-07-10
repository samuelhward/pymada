import pytest
import os, sys  # explicitly modify path to avoid having to constantly run setup.py to test code

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pymada
import pymada.errors
from pymada.classes.position import Position
from pymada.classes.piece import Piece


def create_test_piece():
    """Creates test piece object instance
    """

    test_piece = Piece()
    return test_piece


def test_create_test_piece():
    """Check test piece is of type Piece
    """

    assert isinstance(create_test_piece(), Piece)


def test_set_position():
    """Check set position assigns a position instance
    """

    test_piece = create_test_piece()
    test_piece.position = Position()

    assert isinstance(test_piece.position, Position)

    with pytest.raises(TypeError):
        test_piece.position = 5.0
