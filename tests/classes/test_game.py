import pymada.classes.player
import pymada.classes.game


def test_game():
    """"""

    test_player = pymada.classes.player.Player(name="test", species="test")
    test_game = pymada.classes.game.Game(players=[test_player], fleets=None)

    assert test_game.is_over is False
    test_game.turn = 10
    assert test_game.is_over is True
