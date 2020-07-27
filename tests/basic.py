import pytest
import os, sys  # explicitly modify path to avoid having to constantly run setup.py to test code
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pymada
import pymada.errors
import pymada.data.ships
import pymada.classes.ship
import pymada.classes.hull_zone
from pymada.classes.base import Base
from pymada.classes.piece import Piece
from pymada.classes.player_piece import PlayerPiece
from pymada.classes.position import Position
from pymada.classes.dice import Dice

# TODO separate tests into multiple levels? since all rely on test ship initialisation for example

# ship data tests


def test_ships():
    """
    """

    assert pymada.data.ships.ships["test_ship"]["armament"]["front"] == 1 * "red"


# Ship tests


def test_Ship():
    """Test ship generation
    """

    test_ship = pymada.classes.ship.Ship(
        model="test_ship", name="a ship for testing", faction="neutral", upgrades=None
    )
    assert test_ship.hull_zones["front"].armament == 1 * "red"


def test_Ship_move():
    """Test basic ship movement including attached hull_zones
    """

    test_ship = pymada.classes.ship.Ship(
        model="test_ship",
        name="a ship for testing",
        faction="neutral",
        upgrades=None,
        speed=2,
    )

    test_ship.move(clicks=[1, 0])

    assert test_ship.position.theta == 20
    assert test_ship.hull_zones["front"].position.theta == 20


def test_Ship_move_exceptions():
    """Test basic ship movement exceptions
    """

    test_ship = pymada.classes.ship.Ship(
        model="test_ship",
        name="a ship for testing",
        faction="neutral",
        upgrades=None,
        speed=2,
    )

    with pytest.raises(pymada.errors.ShipYawError):
        test_ship.move(clicks=[0, 4])


# Piece tests


def test_piece_position():
    """Check setting a piece's position incorrectly raises TypeError
    """

    test_piece = Piece(name="test piece")
    test_piece.position = Position(x=5.0, y=5.0, theta=0.0)


# Position tests


def test_position_rotation():
    """
    """

    test_position = Position(x=5.0, y=5.0, theta=0.0)
    test_position._rotate(theta=10)

    assert test_position.theta == 10.0


def test_piece_base():
    """Check setting a piece's base incorrectly raises TypeError
    """

    test_piece = Piece(name="test piece")


# Dice tests


def test_dice_add():
    """Check adding two Die yields a Dice instance with correct number of Die
    """

    dice_1 = Dice("red")
    dice_2 = Dice(4 * "blue")

    assert isinstance(dice_1 + dice_2, Dice)
    assert (dice_1 + dice_2)["red"] == 1
    assert (dice_1 + dice_2)["blue"] == 4


def test_dice_multiply():
    """Check multiplying a Die yields a Dice instance with correct number of Die
    """

    dice_1 = Dice(2 * "red")

    assert isinstance(dice_1 * 4, Dice)
    assert (dice_1 * 4)["red"] == 8


def test_dice_equals():
    """Check two Dice are equal
    """

    assert Dice("blue") == Dice("blue")


# PlayerPiece tests


def test_player_piece_read():
    """
    """

    test_player_piece = PlayerPiece(
        name="ship for testing", model="test_ship", faction="imperial"
    )

    assert test_player_piece.faction is "imperial"


# HullZone tests


def test_create_hull_zone():
    """
    """

    test_hull_zone = pymada.classes.hull_zone.HullZone(
        armament=3 * "red",
        shields=1,
        LoS_dot=0.5,
        arc_left=10,
        arc_right=10,
        position=None,
    )
    assert test_hull_zone.armament == Dice(3 * "red")
    assert test_hull_zone.armament == 3 * "red"
