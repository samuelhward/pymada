import pytest
import os, sys  # explicitly modify path to avoid having to constantly run setup.py to test code

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pymada
import pymada.errors
import pymada.classes.position
import pymada.classes.piece

def create_test_piece():
    """
    """
    position = pymada.classes.position.Position(x=5.0, y=5.0)
    test_piece = pymada.classes.piece.Piece(position=position)
    return test_piece


def test_create_test_piece():
    """
    """

    assert isinstance(
        create_test_piece().position, type(pymada.classes.position.Position())
    )


"""
def test_raise_exception_type_error_position():

    with pytest.raises(pymada.errors.PieceException):
        position = pymada.classes.position(x="4", y=5.0)

def capital_case(x):
    if not isinstance(x, str):
        raise TypeError("Please provide a string argument")
    return x.capitalize()


def test_capital_case():
    assert capital_case("semaphore") == "Semaphore"


def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)
"""
