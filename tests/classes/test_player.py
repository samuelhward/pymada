import pymada.classes.player


def test_player():
    """"""

    test_player = pymada.classes.player.Player(name="test", species="test")
    assert test_player.choose("porkins?") == "porkins!"
