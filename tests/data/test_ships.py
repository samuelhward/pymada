import pymada.data.ships


def test_ship_data():
    """"""

    assert pymada.data.ships.ships["test_ship"]["armament"]["front"] == 1 * "red"
