import pymada.classes.dice


def test_dice_add():
    """Check adding two Die yields a Dice instance with correct number of Die"""

    dice_1 = pymada.classes.dice.Dice("red")
    dice_2 = pymada.classes.dice.Dice(4 * "blue")

    assert isinstance(dice_1 + dice_2, pymada.classes.dice.Dice)
    assert (dice_1 + dice_2)["red"] == 1
    assert (dice_1 + dice_2)["blue"] == 4


def test_dice_multiply():
    """Check multiplying a Die yields a Dice instance with correct number of Die"""

    dice_1 = pymada.classes.dice.Dice(2 * "red")

    assert isinstance(dice_1 * 4, pymada.classes.dice.Dice)
    assert (dice_1 * 4)["red"] == 8


def test_dice_equals():
    """Check two Dice are equal"""

    assert pymada.classes.dice.Dice("blue") == pymada.classes.dice.Dice("blue")


def test_dice_roll():

    rolled_dice = pymada.classes.dice.Dice(4 * "red").roll(target_distance="red")
