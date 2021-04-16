import pymada.classes.player_piece


def test_player_piece_read():
    """"""

    test_player_piece = pymada.classes.player_piece.PlayerPiece(
        name="ship for testing", model="test_ship", faction="imperial"
    )

    assert test_player_piece.faction is "imperial"
