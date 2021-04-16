import pymada.classes.ship
import pytest


def test_ship():
    """Test ship generation"""

    test_ship = pymada.classes.ship.Ship(
        model="test_ship",
        name="a ship for testing",
        faction="neutral",
        upgrades=None,
        player_name="porkins",
        speed=2,
        x=5.0,
        y=10.0,
        theta=20.0,
    )
    assert test_ship.hull_zones["front"].armament == 1 * "red"
    assert test_ship.position == test_ship.base.centre
    test_ship.move(clicks=[0, 1])
    assert test_ship.position == test_ship.base.centre


def test_ship_move():
    """Test basic ship movement including attached hull_zones"""

    test_ship = pymada.classes.ship.Ship(
        model="test_ship",
        name="a ship for testing",
        faction="neutral",
        upgrades=None,
        speed=2,
    )

    test_ship.move(clicks=[0, 1])

    assert round(test_ship.position.theta, 0) == -20
    assert round(test_ship.hull_zones["front"].position.theta, 0) == -20
    assert round(test_ship.base.centre.theta, 0) == -20.0


def test_ship_move_exceptions():
    """Test basic ship movement exceptions"""

    test_ship = pymada.classes.ship.Ship(
        model="test_ship",
        name="a ship for testing",
        faction="neutral",
        upgrades=None,
        speed=2,
    )

    with pytest.raises(pymada.errors.ShipYawError):
        test_ship.move(clicks=[0, 4])
