import pymada.classes.hull_zone
import pymada.classes.dice


def test_create_hull_zone():
    """"""

    test_hull_zone = pymada.classes.hull_zone.HullZone(
        armament=3 * "red",
        shields=1,
        LoS_dot=0.5,
        arc_left=10,
        arc_right=10,
    )
    assert test_hull_zone.armament == pymada.classes.dice.Dice(3 * "red")
    assert test_hull_zone.armament == 3 * "red"
