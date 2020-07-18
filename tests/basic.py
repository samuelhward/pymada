import pytest
import os, sys  # explicitly modify path to avoid having to constantly run setup.py to test code

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pymada
import pymada.errors
import pymada.data.ship_data
from pymada.classes.base import Base
from pymada.classes.piece import Piece
from pymada.classes.position import Position
from pymada.classes.die import Die
from pymada.classes.dice import Dice


# Ship data tests


def test_ship_data():
    """
    """

    assert (
        pymada.data.ship_data.ships["test_ship"]["armament"]["front"][0].colour == "red"
    )


# Piece tests


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
        test_piece.base = 5.0


# Die tests


def test_die_add():
    """Check adding two Die yields a Dice instance with correct number of Die
    """

    die_1 = Die("red")
    die_2 = Die("blue")

    assert isinstance(die_1 + die_2, Dice)


def test_die_multiply():
    """Check multiplying a Die yields a Dice instance with correct number of Die
    """

    die_1 = Die("red")

    assert isinstance(4 * die_1, Dice)
    assert isinstance(die_1 * 4, Dice)


# Dice tests


def test_dice_add():
    """Check adding two Die yields a Dice instance with correct number of Die
    """

    dice_1 = Dice(Die("red"))
    dice_2 = Dice(Die("blue"))

    assert isinstance(dice_1 + dice_2, Dice)
    assert (dice_1 + dice_2)["red"] == 1
    assert (dice_1 + dice_2)["blue"] == 1


def test_dice_multiply():
    """Check multiplying a Die yields a Dice instance with correct number of Die
    """

    dice_1 = Dice(Die("red"))

    assert isinstance(dice_1 * 4, Dice)
    assert (dice_1 * 4)["red"] == 4
