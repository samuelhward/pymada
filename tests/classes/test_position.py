import pymada.classes.position
import numpy as np


def test_position_rotation():
    """"""

    test_position = pymada.classes.position.Position(x=5.0, y=5.0, theta=0.0)
    test_position._rotate(theta=10)

    assert test_position.theta == 10.0


def test_position_translation():
    """"""

    test_position = pymada.classes.position.Position(x=5.0, y=5.0, theta=20.0)
    test_position._translate(theta=90.0, r=5.0)

    assert test_position.y == 10.0

    test_position._translate(theta=0.0, r=5.0)
    assert test_position.x == 10.0

    assert test_position.theta == 20.0


def test_position_move():
    """Test position compound move method"""

    test_position = pymada.classes.position.Position(x=5.0, y=5.0, theta=20.0)

    test_position.move(x=5.0)
    assert test_position.x == 10.0

    test_position.move(y=5.0)
    assert test_position.y == 10.0

    test_position.move(r=np.sqrt(2.0 * 10.0 ** 2), theta_translate=180.0 + 45.0)
    assert round(test_position.x, 0) == 0.0
    assert round(test_position.y, 0) == 0.0

    test_position.move(theta_rotate_first=-20.0)
    assert round(test_position.theta, 1) == 0.0

    test_position.move(theta_rotate_last=20.0)
    assert round(test_position.theta, 1) == 20.0


def test_position_eq():
    """Test position equals"""

    test_position = pymada.classes.position.Position(x=5.0, y=5.0, theta=20.0)
    different_test_position = pymada.classes.position.Position(x=6.0, y=5.0, theta=20.0)

    assert test_position == test_position
    assert test_position != different_test_position
