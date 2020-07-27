import numpy as np

import pymada
import pymada.errors


class Position:
    """Base class describing position and plane orientation
    """

    def __init__(self, x=0.0, y=0.0, theta=0.0, observers=[]):
        """Constructor for position including cartesian coordinates and rotation
        """
        self.x, self.y, self.theta = x, y, theta

        self._observers = observers

    def add_observer(self, observer):
        """
        """
        self._observers.append(observer)

    def _translate(self, x=0.0, y=0.0, r=None, theta=None):
        """
        """

        if theta is None:
            theta = self.theta

        if r is not None:
            self.x += r * np.cos(theta)
            self.y += r * np.sin(theta)
        else:
            self.x += x
            self.y += y

    def _rotate(self, theta):
        """
        """

        self.theta += theta

    def move(self, *args, **kwargs):
        """General movement with steps for first rotating then translating then rotating again

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

        self._rotate(theta=theta_rotate_first)
        self._translate(x=x, y=y, r=r, theta=theta_translate)
        self._rotate(theta=theta_rotate_last)

        if self._observers:
            for observer in self._observers:
                observer(*args, **kwargs)
