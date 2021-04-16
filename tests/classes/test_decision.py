import pymada.classes.decision


def test_decision():
    """"""

    test_decision = pymada.classes.decision.Decision("test_choice")
    assert test_decision.parse_choice_test("porkins?") == "porkins!"
