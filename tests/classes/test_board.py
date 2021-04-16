import pymada.classes.board


def test_board():
    """"""

    test_board = pymada.classes.board.Board()
    assert test_board.width == pymada.classes.board.Board.PLAY_AREA_WIDTH
