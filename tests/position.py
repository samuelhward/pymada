import pytest
import os, sys  # explicitly modify path to avoid having to constantly run setup.py to test code

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pymada
import pymada.errors
from pymada.classes.position import Position
from pymada.classes.piece import Piece


def create_test_position():
    """Creates test position object instance
    """

    test_position = Position(x=5.0, y=5.0)
    return test_position


def test_create_test_position():
    """Check test position is of type Position
    """

    assert isinstance(create_test_position(), Position)
