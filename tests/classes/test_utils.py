import pymada.classes.utils


def test_rotate_2D():
    """"""

    x, y = pymada.classes.utils.rotate_2D(x=1.0, y=0.0, theta=90.0)

    assert round(x, 0) == 0
    assert round(y, 0) == 1

    x, y = pymada.classes.utils.rotate_2D(x=1.0, y=1.0, theta=90.0)

    assert round(x, 0) == -1
    assert round(y, 0) == 1
