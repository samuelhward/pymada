import random

import pymada
import pymada.errors

# TODO need .roll() which returns a list of strings, or Roll object which we can then extract Damage, critical etc. then can have .roll(average=True) for training
# TODO need to add dice faces in data/dice.py
# TODO add red_die,all_other_dice=Dice.split() --> so can then do red_die.roll() again! then add things together again


class Dice:
    """Class describing dice pool
    """

    FACES = {}
    FACES["red"] = [
        "hit",
        "hit",
        "crit",
        "crit",
        "accuracy",
        "hit+hit",
        "blank",
        "blank",
    ]
    FACES["blue"] = [
        "hit",
        "hit",
        "hit",
        "hit",
        "crit",
        "crit",
        "accuracy",
        "accuracy",
    ]
    FACES["black"] = [
        "hit",
        "hit",
        "hit",
        "hit",
        "hit+crit",
        "hit+crit",
        "blank",
        "blank",
    ]

    DAMAGE_AVERAGE = {}
    DAMAGE_AVERAGE["ships"] = {}
    DAMAGE_AVERAGE["ships"]["red"] = 0.75
    DAMAGE_AVERAGE["ships"]["blue"] = 0.75
    DAMAGE_AVERAGE["ships"]["black"] = 1.0
    DAMAGE_AVERAGE["squadrons"] = {}
    DAMAGE_AVERAGE["squadrons"]["red"] = 0.50
    DAMAGE_AVERAGE["squadrons"]["blue"] = 0.50
    DAMAGE_AVERAGE["squadrons"]["black"] = 0.75

    RANGE_COLOURS = {}
    RANGE_COLOURS["red"] = {"red"}
    RANGE_COLOURS["blue"] = {"red", "blue"}
    RANGE_COLOURS["black"] = {"red", "blue", "black"}

    def __init__(self, *dice):
        """Constructor for dice pool

        Examples:
            my_dice=Dice("red")
            my_dice=Dice(4*"red")
            my_dice=Dice(4*"red"+"blue")
            my_dice=4*Dice("red")+Dice("blue")
        """

        self.has_rolled = False

        self._dice = {}
        self._dice["red"] = 0
        self._dice["blue"] = 0
        self._dice["black"] = 0

        if len(dice) is 0:
            pass
        elif len(dice) is 1:  # *dice is string
            for colour in self._dice.keys():
                self[colour] += dice[0].count(colour)
        else:  # *dice is list *args of Dice objects
            for die in dice:
                for colour in die.colours:
                    self[colour] += die[colour]

        self.colours = {colour for colour in self._dice.keys() if self[colour] > 0}
        self.results = {}

        # list of die faces representing roll results
        for colour in self._dice.keys():
            self.results[colour] = []

    def __getitem__(self, colour):
        """
        """

        return self._dice[colour]

    def __setitem__(self, colour, count):
        """
        """

        self._dice[colour] = count

    def __add__(self, other_dice):
        """Overload for addition to return Dice object
        
        args:
            other_dice - other die object [Dice]
        """

        pool = Dice(
            *[
                (self[colour] + other_dice[colour]) * Dice(colour)
                for colour in self.colours | other_dice.colours
            ]
        )

        for colour in self.colours | other_dice.colours:
            pool.results[colour] = self.results[colour] + other_dice.results[colour]

        pool.has_rolled = (
            True if (self.has_rolled) or (other_dice.has_rolled) else False
        )

        return pool

    def __mul__(self, other_factor):
        """Overload for multiplication to return Dice object

        args:
            other_factor - multiplication factor [int]
        """

        return Dice(
            "".join([self[colour] * other_factor * colour for colour in self.colours])
        )

    __rmul__ = __mul__

    def __eq__(self, other_dice):
        """Overload = operator
        
        args:
            other_dice - other die object [Dice] or [str]
        notes:
            does not compare roll results
        """

        # if string, first convert to Dice object
        if type(other_dice) is type(""):
            other_dice = Dice(other_dice)

        if all([self[colour] == other_dice[colour] for colour in self.colours]):
            return True
        else:
            return False

    @property
    def damage_normal(self):

        damage = 0.0
        for colour in self.colours:

            damage += sum(
                result.count("hit")
                for result in self.results[colour]
                if ("hit" in result)
            )

        return damage

    @property
    def damage_critical(self):

        damage = 0.0
        for colour in self.colours:

            damage += sum(
                result.count("crit")
                for result in self.results[colour]
                if ("crit" in result)
            )

        return damage

    def average_damage(self, target_type=None, target_distance="red"):
        """
        args:
            target_type - enemy type [str]
            target_distance - distance colour [str]
        """

        target_type_options = list(DAMAGE_AVERAGE.keys())

        if target_type is None:
            raise pymada.errors.DiceException(
                f"Dice.average_damage needs to know target_type - options = {target_type_options}"
            )

        damage = 0.0
        for colour in self.colours:
            damage += self[colour] * DAMAGE_AVERAGE[target_type][colour]

        return damage

    def roll(self, target_distance=None):
        """
        args:
            target_distance - distance colour [str]
        """

        if target_distance is None:
            raise pymada.errors.DiceException(
                "please specify target_distance when rolling Dice"
            )
            return

        attack_colours = self.RANGE_COLOURS[target_distance]
        # can only attack with dice that we have available for given target range
        available_attack_colours = attack_colours & self.colours

        if not available_attack_colours:
            raise pymada.errors.DiceException(
                f"defender at {target_distance} distance is out of range!"
            )
            return

        for colour in available_attack_colours:
            results = []
            for die_number in range(self[colour]):
                rand = random.randint(1, len(self.FACES[colour]))
                results.append(self.FACES[colour][rand - 1])

            self.results[colour] = results

        self.has_rolled = True
