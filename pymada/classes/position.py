import copy
import numpy as np
import pymada
import pymada.errors
import pymada.classes.utils


class Position:
    """Base class describing position and plane orientation

    notes:
        can also represent generic vector
    """

    def __init__(self, x=None, y=None, theta=None):
        """Constructor for position including cartesian coordinates and rotation
        """

        self.x = x
        self.y = y
        self.theta = theta

        self._observers = []

    def __sub__(self, other_position):
        """Return vector joining two positions

        args:
            other_position - other position to subtract [Position]
        returns:
            new Position instance representing vector between instances
        """

        dx = self.x - other_position.x
        dy = self.y - other_position.y
        theta = np.arctan2(dy, dx) * 180.0 / np.pi

        return Position(x=dx, y=dy, theta=theta)

    def add_observer(self, observer):
        """
        """
        self._observers.append(observer)

    def _translate(self, x=0.0, y=0.0, r=None, theta=None):
        """
        """

        if r is not None:

            if theta is None:
                try:
                    theta = self.theta
                except UnboundLocalError as err:
                    print(err)
                    print(
                        "could not translate position in polar coordinates - theta required!"
                    )
                    return

            self.x += r * np.cos(theta * np.pi / 180.0)
            self.y += r * np.sin(theta * np.pi / 180.0)
        else:
            self.x += x
            self.y += y

    def _rotate(self, theta, centre_x=None, centre_y=None):
        """
        """

        # if no rotation centre supplied assume origin at position
        if centre_x is None:
            centre_x = self.x
        if centre_y is None:
            centre_y = self.y

        # tranform self.theta heading by first converting to cartesian unit vector
        # and finding vector from rotation axis
        if self.theta is not None:
            theta_vector_x = np.cos(self.theta * np.pi / 180.0) + self.x - centre_x
            theta_vector_y = np.sin(self.theta * np.pi / 180.0) + self.y - centre_y

            (
                theta_vector_x_rotated,
                theta_vector_y_rotated,
            ) = pymada.classes.utils.rotate_2D(theta_vector_x, theta_vector_y, theta)

            # transform back
            theta_vector_x_rotated += centre_x - self.x
            theta_vector_y_rotated += centre_y - self.y
            self.theta = (
                np.arctan2(theta_vector_y_rotated, theta_vector_x_rotated)
                * 180.0
                / np.pi
            )

        # calculate vector from rotation axis to this point
        position_vector_x = self.x - centre_x
        position_vector_y = self.y - centre_y

        # rotate vector about rotation point
        (
            position_vector_x_rotated,
            position_vector_y_rotated,
        ) = pymada.classes.utils.rotate_2D(position_vector_x, position_vector_y, theta)

        # recalculate vector in original coordinate system
        self.x = position_vector_x_rotated + centre_x
        self.y = position_vector_y_rotated + centre_y

    def move(self, *args, **kwargs):
        """General compound movement with steps for first rotating then translating then rotating again

        args:
            x - horizontal distance to translate by [cm]
            y - vertical distance to translate by [cm]
            r - distance to translate by on heading theta_translate [cm]
            theta_rotate_first - rotation amount before translation [deg]
            theta_translate - heading to translate on [deg]
            theta_rotate_last - rotation amount after translation [deg]
        notes:
            all movement stages performed but controlled by signature --> many different move styles possible
            all observers moved in same way as requested here
            passes *args **kwargs to all attached observers
        """

        x = kwargs.get("x", 0.0)
        y = kwargs.get("y", 0.0)
        r = kwargs.get("r", None)
        theta_translate = kwargs.get("theta_translate", self.theta)
        theta_rotate_first = kwargs.get("theta_rotate_first", 0.0)
        theta_rotate_last = kwargs.get("theta_rotate_last", 0.0)

        centre_x_rotate_first = kwargs.get("centre_x_rotate_first", self.x)
        centre_y_rotate_first = kwargs.get("centre_y_rotate_first", self.y)

        centre_x_rotate_last = kwargs.get("centre_x_rotate_last", self.x)
        centre_y_rotate_last = kwargs.get("centre_y_rotate_last", self.y)

        self._rotate(
            theta=theta_rotate_first,
            centre_x=centre_x_rotate_first,
            centre_y=centre_y_rotate_first,
        )
        self._translate(x=x, y=y, r=r, theta=theta_translate)

        self._rotate(
            theta=theta_rotate_last,
            centre_x=centre_x_rotate_last,
            centre_y=centre_y_rotate_last,
        )

        if self._observers:
            for observer in self._observers:
                observer(*args, **kwargs)
