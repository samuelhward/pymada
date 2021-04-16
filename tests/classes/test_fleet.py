import pymada.classes.fleet


def test_fleet():
    """"""

    test_fleet = pymada.classes.fleet.Fleet()
    test_fleet.add_ship(model="test_ship", name="test_name", faction="test_faction")

    assert test_fleet.models[0] == "test_ship"
    assert test_fleet.names[0] == "test_name"
    assert test_fleet.factions[0] == "test_faction"
