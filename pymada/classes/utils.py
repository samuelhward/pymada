"""Helper functions for classes
"""

import numpy as np


def rotate_2D(x, y, theta):
    """Implement 2D rotation matrix 
    
    args:
        x - x vector from centre of rotation to point [float/array,cm]
        y - y vector from centre of rotation to point [float/array,cm]
        theta - rotation magnitude [float,deg]
    """

    theta*=np.pi/180.

    x_new = x * np.cos(theta) - y * np.sin(theta)
    y_new = x * np.sin(theta) + y * np.cos(theta)

    return x_new, y_new
