import pytest
import os, sys  # explicitly modify path to avoid having to constantly run setup.py to test code

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pymada
import pymada.errors
from pymada.classes.position import Position
from pymada.classes.piece import Piece
from pymada.classes.ship import Ship


def create_test_ship():
    """Creates test position object instance
    """

    test_ship = Ship(name="", faction="", model="", upgrades="")
    return test_ship


def test_create_test_ship():
    """Check test ship is of type Ship
    """

    assert isinstance(create_test_ship(), Ship)
